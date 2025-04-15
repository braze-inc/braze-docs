---
nav_title: Integraciones de almacenamiento de archivos
article_title: Integraciones de almacenamiento de archivos
description: "Esta página cubre la ingesta de datos en la nube Braze y cómo sincronizar datos relevantes de S3 a Braze"
page_order: 3
page_type: reference

---

# Integraciones de almacenamiento de archivos

> Esta página explica cómo configurar la ingesta de datos en la nube y sincronizar los datos relevantes de S3 con Braze.

Puede utilizar Cloud Data Ingestion (CDI) para S3 para integrar directamente uno o varios buckets S3 de su cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS, y la ingesta de datos en la nube de Braze toma esos nuevos archivos. 

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet, y datos de atributos, eventos, compras y eliminación de usuarios.

La integración requiere los siguientes recursos:
 - Contenedor de S3 para almacenamiento de datos 
 - Cola SQS para notificaciones de nuevos archivos 
 - Función IAM para el acceso a Braze  


## Definiciones de AWS

En primer lugar, definamos algunos de los términos utilizados durante esta tarea.

| Palabra | Definición |
| --- | --- |
| Nombre de recurso de Amazon (ARN) | El ARN es un identificador único para los recursos de AWS. |
| Gestión de identidades y accesos (IAM) | IAM es un servicio web que le permite controlar de forma segura el acceso a los recursos de AWS. En este tutorial, crearás una política IAM y la asignarás a un rol IAM para integrar tu contenedor de S3 con la ingesta de datos en la nube de Braze. |
| Amazon Simple Queue Service (SQS) | SQS es una cola alojada que permite integrar sistemas y componentes de software distribuidos. |
{: .reset-td-br-1 .reset-td-br-2 }
 

## Configuración de la ingesta de datos en la nube en AWS

### Paso 1: Crear un contenedor de origen

Cree un bucket de S3 de uso general con la configuración predeterminada en su cuenta de AWS. 

La configuración predeterminada es:
  - ACL deshabilitadas
  - Bloquear todo acceso público
  - Deshabilitar el versionado de contenedores
  - Cifrado SSE-S3

Toma nota de la región en la que has creado el contenedor, ya que en el siguiente paso crearás una cola SQS en la misma región.

### Paso 2: Crear cola SQS

Cree una cola SQS para controlar cuándo se añaden objetos al bucket que ha creado. Utilice por ahora los ajustes de configuración por defecto.

{% alert important %}
Asegúrese de crear este SQS en la misma región en la que creó el bucket.
{% endalert %}

Asegúrate de tomar nota del ARN y la URL del SQS, ya que lo utilizarás con frecuencia durante esta configuración.
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

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

3. En **Destino** selecciona **Cola SQS** e indica el ARN del SQS que creaste en el paso 2.

### Paso 5: Crear una política IAM

Crea una política IAM para permitir que Braze interactúe con tu contenedor de origen. Para comenzar, inicie sesión en la consola de administración de AWS como administrador de cuenta. 

1. Vaya a la sección IAM de la consola de AWS, seleccione **Políticas** en la barra de navegación y, a continuación, seleccione **Crear política**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

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

4. Dé un nombre y una descripción a la política y seleccione **Crear política**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Paso 6: Crear un rol IAM

Para completar la configuración en AWS, crearás un rol IAM y le adjuntarás la política IAM del paso 4. 

1. Dentro de la misma sección IAM de la consola donde creó la política IAM, vaya a **Roles** > **Crear Rol**. <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Copia el ID de cuenta de AWS Braze de tu panel Braze. Ve a **Ingesta de datos en la nube**, haz clic en **Crear nueva sincronización de datos** y selecciona **Importación S3**. <br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_copy_braze_account_id.png)<br><br>

3. En AWS, seleccione **Otra cuenta de AWS** como tipo de selector de entidad de confianza. Proporcione su ID de cuenta Braze, seleccione la casilla de verificación **Requerir ID externo** e introduzca un ID externo para que Braze lo utilice. Seleccione **Siguiente** cuando haya terminado. <br><br> ![La página S3 "Crear rol". Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Adjunte al rol la política creada en el paso 4. Busque la póliza en la barra de búsqueda y seleccione una marca de verificación junto a la póliza para adjuntarla. Seleccione **Siguiente** cuando haya terminado.<br><br>![ARN del rol]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Asigne un nombre y una descripción a la función y haga clic en **Crear función**.<br><br>![ARN del rol]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5\. Tome nota del ARN del rol que acaba de crear y del identificador externo que ha generado, ya que los utilizará para crear la integración de Cloud Data Ingestion.  

## Configuración de la ingesta de datos en la nube en Braze

1. Para crear una nueva integración, vaya a **Configuración de datos** > **Ingestión de datos en la nube**, seleccione **Crear nueva sincronización de datos** y seleccione **Importación de S3** en la sección de fuentes de archivos. 

2. Introduce la información del proceso de configuración de AWS para crear una nueva sincronización. Especifica lo siguiente:
- ARN del rol
- ID externo
- URL de SQS (debe ser única para cada nueva integración)
- Nombre del contenedor
- Ruta de la carpeta (opcional)
- Región  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Dé un nombre a su integración y seleccione el tipo de datos para esta integración. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. Añade un correo electrónico de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Si lo desea, puede activar las notificaciones de errores de usuario y de sincronización correcta. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Por último, prueba la conexión y guarda la sincronización. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## Formatos de archivo necesarios

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet. Cada archivo debe contener una o varias de las columnas de identificadores admitidas y una columna de carga útil en forma de cadena JSON. 

- Identificadores de usuario. Su fichero fuente puede contener una o varias columnas o claves de identificador de usuario. Cada fila sólo debe contener un identificador, pero un archivo fuente puede tener varios tipos de identificador. 
    - `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que desea sincronizar con el usuario en Braze.

{% alert note %}
A diferencia de las fuentes de almacén de datos, la columna `UPDATED_AT` no es necesaria ni compatible.
{% endalert %}

{% alert note %}
Los archivos añadidos al contenedor de S3 de origen no deben superar los 512 MB. Los archivos de más de 512 MB producirán un error y no se sincronizarán con Braze.
{% endalert %}

{% tabs %}
{% tab Atributos JSON %}
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
{% tab Eventos personalizados JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un archivo JSON válido o este será omitido.
{% endalert %}
{% endtab %}
{% tab Eventos de compra JSON %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un archivo JSON válido o este será omitido.
{% endalert %}

{% endtab %}
{% tab Atributos CSV %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

Para ver ejemplos de todos los tipos de archivos compatibles, consulte los archivos de ejemplo en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  
