---
nav_title: Integraciones de almacenamiento de archivos
article_title: Integraciones de almacenamiento de archivos
description: "Esta página cubre la ingesta de datos en la nube Braze y cómo sincronizar datos relevantes de S3 a Braze."
page_order: 3
page_type: reference

---

# Integraciones de almacenamiento de archivos

> Esta página explica cómo configurar la ingesta de datos en la nube y sincronizar los datos relevantes de S3 con Braze.

## Cómo funciona

Puedes utilizar Cloud Data Ingestion (CDI) para S3 para integrar directamente uno o varios contenedores de S3 de tu cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS, y Braze Cloud Data Ingestion recoge esos nuevos archivos. 

La Ingesta de Datos en la Nube admite lo siguiente:

- Archivos JSON
- Archivos CSV
- Archivos de parquet
- Atributo, evento personalizado, evento de compra, borrado de usuario y datos de catálogo.

## Requisitos previos

La integración requiere los siguientes recursos:

 - Contenedor de S3 para almacenamiento de datos 
 - Cola SQS para notificaciones de archivos nuevos 
 - Función IAM para el acceso a Braze  

### Definiciones de AWS

En primer lugar, definamos algunos de los términos utilizados durante esta tarea.

| Plazo | Definición |
| --- | --- |
| Nombre de recurso de Amazon (ARN) | El ARN es un identificador único para los recursos de AWS. |
| Gestión de Identidades y Accesos (IAM) | IAM es un servicio Web que te permite controlar de forma segura el acceso a los recursos de AWS. En este tutorial, crearás una política de IAM y la asignarás a un rol de IAM para integrar tu contenedor de S3 con Braze Cloud Data Ingestion. |
| Servicio de cola simple de Amazon (SQS) | SQS es una cola alojada que te permite integrar sistemas y componentes de software distribuidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de la ingesta de datos en la nube en AWS

### Paso 1: Crear un contenedor fuente

Crea un contenedor de S3 de uso general con la configuración predeterminada en tu cuenta de AWS. Los contenedores de S3 pueden reutilizarse entre sincronizaciones siempre que la carpeta sea única.

Las configuraciones predeterminadas son:

- ACLs desactivadas
- Bloquea todo acceso público
- Desactivar el versionado de contenedores
- Encriptación SSE-S3

Toma nota de la región en la que has creado el contenedor, ya que en el siguiente paso crearás una cola SQS en la misma región.

### Paso 2: Crear cola SQS

Crea una cola SQS para hacer un seguimiento de cuándo se añaden objetos al contenedor que has creado. Utiliza por ahora la configuración predeterminada. 

Una cola SQS debe ser única globalmente (por ejemplo, sólo se puede utilizar una para una sincronización CDI y no se puede reutilizar en otro espacio de trabajo).

{% alert important %}
Asegúrate de crear este SQS en la misma región en la que creaste el contenedor.
{% endalert %}

Asegúrate de tomar nota del ARN y la URL del SQS, ya que lo utilizarás con frecuencia durante esta configuración.

\![Seleccionar "Avanzado" con un objeto JSON de ejemplo para definir quién puede acceder a una cola.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Paso 3: Configura la política de acceso

Para configurar la política de acceso, elige **Opciones avanzadas**. 

Añade la siguiente declaración a la política de acceso de la cola, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de tu contenedor, y `YOUR-SQS-ARN` por el ARN de tu cola SQS, y `YOUR-AWS-ACCOUNT-ID` por el ID de tu cuenta AWS: 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### Paso 4: Añade una notificación de evento al contenedor de S3

1. En el contenedor creado en el paso 1, ve a **Propiedades** > **Notificaciones de eventos**.
2. Dale un nombre a la configuración. Opcionalmente, especifica un prefijo o sufijo de destino si sólo quieres que Braze ingiera un subconjunto de archivos.
3. En **Destino**, selecciona **Cola SQS** e indica el ARN del SQS que creaste en el paso 2.

{% alert note %}
Si subes tus archivos a la carpeta raíz de un contenedor de S3 y luego mueves algunos de los archivos a una carpeta específica del contenedor, puedes encontrarte con un error inesperado. En su lugar, puedes cambiar las notificaciones de eventos para que se envíen sólo para los archivos del prefijo, evitar colocar archivos en el contenedor de S3 fuera de ese prefijo, o actualizar la integración sin prefijo, que entonces ingestará todos los archivos.
{% endalert %}

### Paso 5: Crear una política IAM

Crea una política IAM para permitir que Braze interactúe con tu contenedor fuente. Para empezar, inicia sesión en la consola de administración de AWS como administrador de cuentas. 

1. Ve a la sección IAM de la consola de AWS, selecciona **Políticas** en la barra de navegación y, a continuación, selecciona **Crear política**.<br><br>\![El botón "Crear política" de la consola de AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Documento de política**, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de contenedor y `YOUR-SQS-ARN-HERE` por el nombre de tu cola SQS: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3\. Selecciona **Revisar Política** cuando hayas terminado.

4. Dale un nombre y una descripción a la política y, a continuación, selecciona **Crear política**.  

\![Una política de ejemplo llamada "nombre-nueva-política".]({% image_buster /assets/img/create_policy_3_name.png %})

\![El campo de descripción de la política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Paso 6: Crear un rol IAM

Para completar la configuración en AWS, crearás un rol IAM y le adjuntarás la política IAM del paso 4. 

1. Dentro de la misma sección IAM de la consola donde creaste la política IAM, ve a **Roles** > **Crear Rol**. 

<br><br>\![El botón "Crear rol".]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2\. Copia el ID de cuenta de AWS Braze de tu panel Braze. Ve a **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y selecciona **Importación S3**.

3. En AWS, selecciona **Otra cuenta de AWS** como tipo de selector de entidad de confianza. Proporciona tu ID de cuenta Braze. Marca la casilla **Requerir ID externo** e introduce un ID externo para que lo utilice Braze. Es el ID externo generado al crear una conexión S3 Currents en la sección **Credenciales** de tu conexión Currents en el panel de Braze. Selecciona **Siguiente** cuando hayas terminado. 

<br><br> \![La página S3 "Crear rol". Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4\. Adjunta al rol la política creada en el paso 4. Busca la póliza en la barra de búsqueda, y selecciona una marca de verificación junto a la póliza para adjuntarla. Selecciona **Siguiente** cuando hayas terminado.

<br><br>\![ARN de rol con el nombre de la nueva política seleccionada.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

Dale al rol un nombre y una descripción, y selecciona **Crear rol**.

<br><br>\![Un ejemplo de rol llamado "nuevo-nombre-de-rol".]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5\. Toma nota del ARN del rol que acabas de crear y del ID externo que has generado, ya que los utilizarás para crear la integración de la Ingesta de datos en la nube.

## Configuración de la ingesta de datos en la nube en Braze

1. Para crear una nueva integración, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y selecciona **Importación S3** en la sección de fuentes de archivos. 
2. Introduce la información del proceso de configuración de AWS para crear una nueva sincronización. Especifica lo siguiente:

  - Función ARN
  - ID externo
  - URL de SQS (debe ser única para cada nueva integración)
  - Nombre de contenedor
  - Ruta de la carpeta (opcional, debe ser única en todas las sincronizaciones de un espacio de trabajo)
  - Región

\![Ejemplo de credenciales de seguridad tal y como se muestran en S3 para crear una nueva sincronización de importación.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Dale un nombre a tu integración y selecciona el tipo de datos para esta integración. 

<br><br>\![Configuración de los detalles de sincronización para "cdi-s3-como-fuente-integración" con atributos de usuario como tipo de datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4\. Añade un correo electrónico de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Opcionalmente, activa las notificaciones para errores a nivel de usuario y éxitos de sincronización. 

<br><br> Configuración de las preferencias de notificación de errores de sincronización.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Por último, prueba la conexión y guarda la sincronización. 

<br><br>Una opción para probar la conexión con una vista previa de los datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Formatos de archivo necesarios

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet. Cada archivo debe contener una o varias de las columnas identificadoras admitidas y una columna de carga útil como cadena JSON.

Braze no impone ningún requisito de nombre de archivo adicional al que impone AWS. Los nombres de los archivos deben ser únicos. Recomendamos añadir una marca de tiempo para que sea único.

### Identificadores de usuario

Tu archivo fuente puede contener una o varias columnas o claves de identificador de usuario. Cada fila sólo debe contener un identificador, pero un archivo fuente puede tener varios tipos de identificador.

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
| `BRAZE_ID` | El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. |
|`PAYLOAD` | Se trata de una cadena JSON de los campos que quieres sincronizar con el usuario en Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A diferencia de las fuentes de almacén de datos, la columna `UPDATED_AT` no es necesaria ni compatible.
{% endalert %}

{% tabs %}
{% tab JSON Attributes %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener JSON válido, o se omitirá el archivo.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener JSON válido, o se omitirá el archivo.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener JSON válido, o se omitirá el archivo.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

Para ver ejemplos de todos los tipos de archivo admitidos, consulta los archivos de ejemplo en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Lo que debes saber

- Los archivos añadidos al contenedor de origen de S3 no deben superar los 512 MB. Los archivos de más de 512 MB producirán un error y no se sincronizarán con Braze.
- Aunque no hay límite adicional en el número de filas por archivo, te recomendamos que utilices archivos más pequeños para mejorar la velocidad de ejecución de tus sincronizaciones. Por ejemplo, un archivo de 500 MB tardaría bastante más en ser ingerido que cinco archivos distintos de 100 MB.
- No hay límite adicional en el número de archivos subidos en un tiempo determinado.
- No es posible ordenar en o entre archivos. Te recomendamos que actualices por lotes periódicamente si vigilas cualquier condición de carrera prevista.

## Solución de problemas

### Cargar archivos y procesar

CDI sólo procesará los archivos que se añadan después de crear la sincronización. En este proceso, Braze busca nuevos archivos que añadir, lo que desencadena un nuevo mensaje a SQS. Esto iniciará una nueva sincronización para procesar el nuevo archivo.

Los archivos existentes pueden utilizarse para validar la estructura de datos en la conexión de prueba, pero no se sincronizarán con Braze. Los archivos existentes que deban sincronizarse deben volver a cargarse en S3 para que los procese CDI.

### Tratamiento de errores de archivo inesperados

Si observas un elevado número de errores o archivos fallidos, es posible que tengas otro proceso añadiendo archivos al contenedor de S3 en una carpeta distinta de la carpeta de destino para CDI.

Cuando los archivos se cargan en el contenedor de origen pero no en la carpeta de origen, CDI procesará la notificación SQS, pero no realizará ninguna acción sobre el archivo, por lo que puede aparecer como un error.
