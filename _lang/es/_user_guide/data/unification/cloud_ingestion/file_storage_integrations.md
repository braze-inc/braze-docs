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

Puede utilizar Cloud Data Ingestion (CDI) para S3 para integrar directamente uno o varios buckets S3 de su cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS, y la ingesta de datos en la nube de Braze recoge esos nuevos archivos. 

La Ingesta de datos en la nube admite lo siguiente:

- Archivos JSON
- Archivos CSV
- Archivos de parquet
- Atributo, evento personalizado, evento de compra, borrado de usuario y datos de catálogo.

## Requisitos previos

La integración requiere los siguientes recursos:

 - Contenedor de S3 para almacenamiento de datos 
 - Cola SQS para notificaciones de nuevos archivos 
 - Función IAM para el acceso a Braze  

### Definiciones de AWS

En primer lugar, define los términos utilizados durante esta tarea.

| Plazo | Definición |
| --- | --- |
| Nombre de recurso de Amazon (ARN) | El ARN es un identificador único para los recursos de AWS. |
| Gestión de identidades y accesos (IAM) | IAM es un servicio web que le permite controlar de forma segura el acceso a los recursos de AWS. En este tutorial, crearás una política IAM y la asignarás a un rol IAM para integrar tu contenedor de S3 con la ingesta de datos en la nube de Braze. |
| Amazon Simple Queue Service (SQS) | SQS es una cola alojada que permite integrar sistemas y componentes de software distribuidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de la ingesta de datos en la nube en AWS

### Paso 1: Crear un contenedor de origen

Crea un contenedor de S3 de uso general con la configuración predeterminada en tu cuenta de AWS. Los contenedores de S3 pueden reutilizarse entre sincronizaciones siempre que la carpeta sea única.

La configuración predeterminada es:

- ACL deshabilitadas
- Bloquear todo acceso público
- Deshabilitar el versionado de contenedores
- Cifrado SSE-S3
  - SSE-S3 es el único tipo de encriptación del servidor admitido. No se admite el cifrado KMS de Amazon.

Toma nota de la región en la que has creado el contenedor, ya que en el siguiente paso crearás una cola SQS en la misma región.

### Paso 2: Crear cola SQS

Cree una cola SQS para controlar cuándo se añaden objetos al bucket que ha creado. Utilice por ahora los ajustes de configuración por defecto. 

Una cola SQS debe ser única globalmente (por ejemplo, sólo se puede utilizar una para una sincronización CDI y no se puede reutilizar en otro espacio de trabajo).

{% alert important %}
Asegúrate de crear este SQS en la misma región en la que creaste el contenedor.
{% endalert %}

Asegúrate de tomar nota del ARN y la URL del SQS, ya que lo utilizarás con frecuencia durante esta configuración.

![Seleccionando "Avanzado" con un objeto JSON de ejemplo para definir quién puede acceder a una cola.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Paso 3: Establecer la política de acceso

Para configurar la política de acceso, seleccione **Opciones avanzadas**. 

Añada la siguiente declaración a la política de acceso de la cola, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de su bucket, `YOUR-SQS-ARN` por el ARN de su cola SQS y `YOUR-AWS-ACCOUNT-ID` por el ID de su cuenta AWS: 

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

### Paso 4: Añadir una notificación de evento al bucket S3

1. En el cubo creado en el paso 1, vaya a **Propiedades** > **Notificaciones de eventos**.
2. Asigne un nombre a la configuración. Opcionalmente, especifique un prefijo o sufijo de destino si sólo desea que Braze ingiera un subconjunto de archivos.
3. En **Destino**, selecciona **Cola SQS** e indica el ARN del SQS que creaste en el paso 2.

{% alert note %}
Si subes tus archivos a la carpeta raíz de un contenedor de S3 y luego mueves algunos de los archivos a una carpeta específica del contenedor, puedes encontrarte con un error inesperado. En su lugar, puedes cambiar las notificaciones de eventos para que se envíen sólo para los archivos del prefijo, evitar colocar archivos en el contenedor de S3 fuera de ese prefijo o actualizar la integración sin prefijo, que entonces ingestará todos los archivos.
{% endalert %}

### Paso 5: Crear una política IAM

Crea una política IAM para permitir que Braze interactúe con tu contenedor de origen. Para comenzar, inicie sesión en la consola de administración de AWS como administrador de cuenta. 

1. Vaya a la sección IAM de la consola de AWS, seleccione **Políticas** en la barra de navegación y, a continuación, seleccione **Crear política**.<br><br>![El botón "Crear política" de la consola de AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abra la pestaña **JSON** e introduzca el siguiente fragmento de código en la sección **Policy Document**, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de su cubo y `YOUR-SQS-ARN-HERE` por el nombre de su cola SQS: 

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
3\. Seleccione **Revisar política** cuando haya terminado.

4. Dale un nombre y una descripción a la política y, a continuación, selecciona **Crear política**.  

![Una política de ejemplo llamada "nombre-nueva-política".]({% image_buster /assets/img/create_policy_3_name.png %})

![El campo de descripción de la política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Paso 6: Crear un rol IAM

Para completar la configuración en AWS, crearás un rol IAM y le adjuntarás la política IAM del paso 4. 

1. Dentro de la misma sección IAM de la consola donde creó la política IAM, vaya a **Roles** > **Crear Rol**. 

![El botón "Crear rol".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2\. Copia el ID de cuenta de AWS Braze de tu panel Braze. Ve a **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y selecciona **Importación S3**.
3\. En AWS, seleccione **Otra cuenta de AWS** como tipo de selector de entidad de confianza. Proporciona tu ID de cuenta Braze. Selecciona la casilla **Requerir ID externo**.
4\. En Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y selecciona **Importación S3** en la sección de fuentes de archivos.
5\. Copia el **ID de cuenta Braze** generado automáticamente. 

![Sección de credenciales con el campo ID de cuenta Braze.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
6\. En AWS, pega el ID de la cuenta y selecciona **Siguiente**.

![La página S3 "Crear rol". Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
7\. Adjunte al rol la política creada en el paso 4. Busque la póliza en la barra de búsqueda y seleccione una marca de verificación junto a la póliza para adjuntarla. Seleccione **Siguiente** cuando haya terminado.

![ARN del rol con el nombre de la nueva política seleccionada.]({% image_buster /assets/img/create_role_3_attach.png %})

Dale al rol un nombre y una descripción, y selecciona **Crear rol**.

![Un ejemplo de rol llamado "nuevo-nombre-de-rol".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
8\. Toma nota del ARN del rol que has creado y del ID externo que has generado, porque los necesitas para crear la integración de la Ingesta de datos en la nube.

## Configuración de la ingesta de datos en la nube en Braze

1. Para crear una nueva integración, vaya a **Configuración de datos** > **Ingestión de datos en la nube**, seleccione **Crear nueva sincronización de datos** y seleccione **Importación de S3** en la sección de fuentes de archivos. 
2. Introduce la información del proceso de configuración de AWS para crear una nueva sincronización. Especifica lo siguiente:

  - ARN del rol
  - ID externo
  - URL de SQS (debe ser única para cada nueva integración)
  - Nombre de contenedor
  - Ruta de la carpeta (opcional, debe ser única en todas las sincronizaciones de un espacio de trabajo)
  - Región

![Ejemplo de credenciales de seguridad tal y como se muestran en S3 para crear una nueva sincronización de importación.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Dale un nombre a tu integración y selecciona el tipo de datos para esta integración. 

![Configuración de los detalles de sincronización para "cdi-s3-como-fuente-integración" con atributos de usuario como tipo de datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})

{: start="4"}
4\. Añade un correo electrónico de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Si lo desea, puede activar las notificaciones de errores de usuario y de sincronización correcta. 

![Configuración de las preferencias de notificación de errores de sincronización.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5\. Por último, selecciona **Probar conexión** para confirmar que Braze puede acceder a tu contenedor y enumerar los archivos disponibles para la ingesta (no los datos que contienen esos archivos). Después, guarda la sincronización. 

![Una opción para probar la conexión con una vista previa de los datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Formatos de archivo necesarios

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet. Cada archivo debe contener una o varias de las columnas identificadoras admitidas y una columna de carga útil como cadena JSON.

Braze no impone ningún requisito de nombre de archivo adicional al que impone AWS. Los nombres de los archivos deben ser únicos. Recomendamos añadir una marca de tiempo para que sea único.

### Identificadores de usuario

Su fichero fuente puede contener una o varias columnas o claves de identificador de usuario. Cada fila sólo debe contener un identificador, pero un archivo fuente puede tener varios tipos de identificador.

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Esto identifica al usuario que quieres actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
| `BRAZE_ID` | El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal. |
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
Cada línea de tu archivo fuente debe contener un archivo JSON válido o este será omitido.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un archivo JSON válido o este será omitido.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un archivo JSON válido o este será omitido.
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
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluye una columna **SUPRIMIDA** opcional. Cuando `DELETED` es `true`, ese elemento del catálogo se elimina del catálogo en Braze. Ver [Borrar elementos del catálogo](#deleting-catalog-items).
{% endtab %}

{% endtabs %}  

Para ver ejemplos de todos los tipos de archivo admitidos, consulta los archivos de ejemplo en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Borrar datos

La ingesta de datos en la nube para S3 permite eliminar usuarios y elementos del catálogo mediante la carga de archivos. Utiliza sincronizaciones y formatos de archivo distintos para cada uno.

- **[Borrar usuarios](#deleting-users)** \- Crea una sincronización con el tipo de datos **Eliminar usuarios** y sube archivos que sólo contengan identificadores de usuario (sin carga útil).
- **[Eliminar elementos del catálogo](#deleting-catalog-items)** \- Utiliza la sincronización existente de tu catálogo y añade una columna `deleted` (o `DELETED`) para marcar los elementos a eliminar.

### Eliminar usuarios

Para eliminar perfiles de usuario en Braze utilizando archivos en S3:

1. Crea una nueva sincronización de Ingesta de datos en la nube (la misma [configuración de AWS y Braze](#setting-up-cloud-data-ingestion-in-aws) que para otras sincronizaciones).
2. Cuando configures la sincronización en Braze, establece **Tipo de datos** en **Eliminar usuarios**.
3. Sube archivos a tu contenedor de S3 que sólo contengan columnas identificadoras de usuario. No incluyas una columna `PAYLOAD`: la sincronización falla si hay carga útil, para evitar eliminaciones accidentales.

Cada fila del archivo debe identificar exactamente a un usuario utilizando una de las siguientes opciones:

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Coincide con el `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Ambas columnas juntas identifican al usuario por su alias. |
| `BRAZE_ID` | ID de usuario generado por Braze (sólo usuarios existentes). |

{% alert important %}
La eliminación de usuarios es permanente y no puede deshacerse. Incluye sólo a los usuarios que pretendas eliminar. Para más detalles, consulta [Eliminar usuarios con la ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/).
{% endalert %}

**Ejemplo - JSON (eliminaciones de usuarios):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Ejemplo - CSV (borrados de usuario):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Cuando se ejecuta la sincronización, Braze procesa los archivos nuevos del contenedor y elimina los perfiles de usuario correspondientes.

### Borrar elementos del catálogo

Para eliminar elementos de un catálogo utilizando el almacenamiento de archivos:

1. Utiliza la misma sincronización S3 que utilizas para [sincronizar los datos del catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) (tipo de datos **Catálogos**).
2. En tus archivos CSV o JSON, añade un elemento opcional **`deleted`** (o **`DELETED`**) opcional.
3. Configura `deleted` en `true` para cualquier elemento del catálogo que quieras eliminar del catálogo en Braze.

Cada fila sigue necesitando `ID` y `PAYLOAD`. Para las filas marcadas para ser eliminadas, la carga útil puede ser mínima; Braze elimina el elemento mediante `ID`.

**Ejemplo - JSON (eliminar elemento del catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Ejemplo - CSV (eliminar elemento de catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Cuando se ejecuta la sincronización, las filas con `deleted: true` hacen que el elemento de catálogo correspondiente se elimine en Braze. Para conocer el comportamiento completo de [sincronización y]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) eliminación del catálogo, consulta [Sincronizar y eliminar datos del catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/).

## Lo que hay que saber

- Los archivos añadidos al contenedor de origen de S3 no deben superar los 512 MB. Los archivos de más de 512 MB producirán un error y no se sincronizarán con Braze.
- Aunque no hay límite adicional en el número de filas por archivo, te recomendamos que utilices archivos más pequeños para mejorar la velocidad de ejecución de tus sincronizaciones. Por ejemplo, la ingesta de un archivo de 500 MB tardaría bastante más que la de cinco archivos distintos de 100 MB.
- No hay límite adicional en el número de archivos subidos en un tiempo determinado.
- No es posible ordenar en o entre archivos. Te recomendamos que actualices por lotes periódicamente si vigilas cualquier condición de carrera prevista.

## Solución de problemas

### Cargar archivos y procesar

CDI sólo procesará los archivos que se añadan después de crear la sincronización. En este proceso, Braze busca nuevos archivos que añadir, lo que desencadena un nuevo mensaje a SQS. Esto iniciará una nueva sincronización para procesar el nuevo archivo.

Puedes utilizar archivos existentes para validar que Braze puede acceder a tu contenedor y detectar archivos para ingestar, pero no se sincronizan con Braze. Para que el CDI los procese, debes volver a subir al S3 los archivos existentes que quieras sincronizar. 

### Tratamiento de errores de archivo inesperados

Si observas un elevado número de errores o archivos fallidos, es posible que tengas otro proceso añadiendo archivos al contenedor de S3 en una carpeta distinta de la carpeta de destino para CDI.

Cuando los archivos se cargan en el contenedor de origen pero no en la carpeta de origen, CDI procesará la notificación SQS, pero no realizará ninguna acción sobre el archivo, por lo que puede aparecer como un error.
