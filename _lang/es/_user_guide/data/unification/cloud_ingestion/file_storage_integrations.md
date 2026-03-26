---
nav_title: Integraciones de almacenamiento de archivos
article_title: Integraciones de almacenamiento de archivos
description: "Esta página trata sobre la ingesta de datos en la nube de Braze y cómo sincronizar datos relevantes de S3 a Braze."
page_order: 3
page_type: reference

---

# Integraciones de almacenamiento de archivos

> Esta página explica cómo configurar la ingesta de datos en la nube y sincronizar los datos relevantes de S3 con Braze.

Esta página muestra los pasos de sincronización y fuente que actualmente se encuentran en acceso anticipado (EA). Para los pasos de la experiencia de disponibilidad general, despliega **Experiencia de disponibilidad general** a continuación.

## Cómo funciona

Puedes utilizar Cloud Data Ingestion (CDI) para S3 para integrar directamente uno o varios contenedores de S3 de tu cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS, y la ingesta de datos en la nube de Braze recoge esos nuevos archivos. 

La ingesta de datos en la nube admite lo siguiente:

- Archivos JSON
- Archivos CSV
- Archivos Parquet
- Datos de atributos, eventos personalizados, eventos de compra, eliminación de usuarios y catálogos

## Requisitos previos

La integración requiere los siguientes recursos:

 - Contenedor de S3 para almacenamiento de datos 
 - Cola SQS para notificaciones de nuevos archivos 
 - Rol IAM para el acceso de Braze  

### Definiciones de AWS

En primer lugar, definamos los términos utilizados en esta tarea.

| Término | Definición |
| --- | --- |
| Nombre de recurso de Amazon (ARN) | El ARN es un identificador único para los recursos de AWS. |
| Gestión de identidades y accesos (IAM) | IAM es un servicio web que te permite controlar de forma segura el acceso a los recursos de AWS. En este tutorial, crearás una política IAM y la asignarás a un rol IAM para integrar tu contenedor de S3 con la ingesta de datos en la nube de Braze. |
| Amazon Simple Queue Service (SQS) | SQS es una cola alojada que permite integrar sistemas y componentes de software distribuidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de la ingesta de datos en la nube en AWS

### Paso 1: Crear un contenedor de origen

Crea un contenedor de S3 de uso general con la configuración predeterminada en tu cuenta de AWS. Los contenedores de S3 se pueden reutilizar en todas las sincronizaciones, siempre y cuando la carpeta sea única.

La configuración predeterminada es:

- ACL deshabilitadas
- Bloquear todo acceso público
- Deshabilitar el versionado de contenedores
- Cifrado SSE-S3
  - SSE-S3 es el único tipo de cifrado del lado del servidor compatible. No se admite el cifrado de Amazon KMS.

Toma nota de la región en la que has creado el contenedor, ya que en el siguiente paso crearás una cola SQS en la misma región.

### Paso 2: Crear cola SQS

Crea una cola SQS para controlar cuándo se añaden objetos al contenedor que has creado. Utiliza por ahora los ajustes de configuración predeterminados. 

Una cola SQS debe ser única a nivel global (por ejemplo, solo se puede utilizar una para una sincronización CDI y no se puede reutilizar en otro espacio de trabajo).

{% alert important %}
Asegúrate de crear este SQS en la misma región en la que creaste el contenedor.
{% endalert %}

Toma nota del ARN y la URL de la cola SQS, ya que los necesitarás con frecuencia durante esta configuración.

![Selecciona «Advanced» con un objeto JSON de ejemplo para definir quién puede acceder a una cola.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Paso 3: Establecer la política de acceso

Para configurar la política de acceso, selecciona **Advanced options**. 

Añade la siguiente declaración a la política de acceso de la cola, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de tu contenedor, `YOUR-SQS-ARN` por el ARN de tu cola SQS y `YOUR-AWS-ACCOUNT-ID` por el ID de tu cuenta de AWS: 

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

### Paso 4: Añadir una notificación de evento al contenedor de S3

1. En el contenedor creado en el paso 1, ve a **Properties** > **Event notifications**.
2. Asigna un nombre a la configuración. Opcionalmente, especifica un prefijo o sufijo de destino si solo deseas que Braze ingeste un subconjunto de archivos.
3. En **Destination**, selecciona **SQS queue** y proporciona el ARN de la cola SQS que creaste en el paso 2.

{% alert note %}
Si subes tus archivos a la carpeta raíz de un contenedor de S3 y luego mueves algunos de ellos a una carpeta específica dentro del contenedor, es posible que se produzca un error inesperado. En su lugar, puedes cambiar las notificaciones de eventos para que solo se envíen para los archivos con el prefijo, evitar colocar archivos en el contenedor de S3 fuera de ese prefijo o actualizar la integración sin prefijo, lo que hará que se ingesten todos los archivos.
{% endalert %}

### Paso 5: Crear una política IAM

Crea una política IAM para permitir que Braze interactúe con tu contenedor de origen. Para comenzar, inicia sesión en la consola de administración de AWS como administrador de cuenta. 

1. Ve a la sección IAM de la consola de AWS, selecciona **Policies** en la barra de navegación y, a continuación, selecciona **Create Policy**.<br><br>![El botón «Create Policy» en la consola de AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Policy Document**, teniendo cuidado de sustituir `YOUR-BUCKET-NAME-HERE` por el nombre de tu contenedor y `YOUR-SQS-ARN-HERE` por el nombre de tu cola SQS: 

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
3. Selecciona **Review Policy** cuando hayas terminado.

4. Asigna un nombre y una descripción a la política y, a continuación, selecciona **Create Policy**.  

![Una política de ejemplo denominada «new-policy-name».]({% image_buster /assets/img/create_policy_3_name.png %})

![El campo de descripción de la política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Paso 6: Crear un rol IAM

Para completar la configuración en AWS, crea un rol IAM y adjúntale la política IAM del paso 5. 

1. Dentro de la misma sección IAM de la consola donde creaste la política IAM, ve a **Roles** > **Create Role**. 

![El botón «Create Role».]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. En AWS, selecciona **Another AWS Account** como tipo de selector de entidad de confianza. Proporciona tu ID de cuenta de Braze. Selecciona la casilla de verificación **Require external ID**.
3. En Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y selecciona **Amazon S3** en la sección de fuentes de archivos.
4. Copia el **Braze Account ID** generado automáticamente. 

![La página «Add New Source» que muestra las secciones de nombre de fuente y detalles de conexión de S3.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. En AWS, pega el ID de la cuenta y selecciona **Next**.

![La página S3 «Create Role». Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Adjunta al rol la política creada en el paso 5. Busca la política en la barra de búsqueda y selecciona la marca de verificación junto a la política para adjuntarla. Selecciona **Next** cuando hayas terminado.

![ARN de rol con el nombre de la nueva política seleccionado.]({% image_buster /assets/img/create_role_3_attach.png %})

Asigna un nombre y una descripción al rol y selecciona **Create Role**.

![Un ejemplo de rol llamado «new-role-name».]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Toma nota del ARN del rol que has creado y del ID externo que has generado, ya que los necesitarás para crear la integración de Cloud Data Ingestion.

## Configuración de la ingesta de datos en la nube en Braze

1. Primero, crea una nueva fuente en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y luego selecciona **Amazon S3**.
2. Elige un nombre para tu fuente e introduce la información del proceso de configuración de AWS para crear una nueva fuente. Especifica lo siguiente:

  - ARN del rol
  - ID externo
  - Nombre de contenedor
  - Región

![La sección de detalles de conexión de S3 que muestra las credenciales (configuración de AWS y configuración de Braze) y los campos de configuración.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecciona **Test connection** para confirmar que Braze puede acceder a tu contenedor. Después de una prueba exitosa, selecciona **Connect to Source**. Si la conexión falla, aparecerá un mensaje de error para ayudarte a solucionar el problema.

{: start="4"}
4. A continuación, crea una nueva sincronización. Ve a **Data Settings** > **Cloud Data Ingestion** > **Syncs** y selecciona **Create data sync**.

![La página «Create New Sync» que muestra el nombre de la sincronización y la configuración del origen de datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente S3 activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y selecciona **Test Connection**.

![Una opción para probar la conexión con una vista previa de los datos.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Introduce la información restante del proceso de configuración de AWS. Especifica lo siguiente:
- URL de SQS (debe ser única para cada nueva integración)
- Ruta de la carpeta (opcional, debe ser única en todas las sincronizaciones de un espacio de trabajo)

7. Selecciona un tipo de datos y selecciona **Test Connection** para confirmar que Braze puede listar los archivos disponibles para ingestar (no los datos dentro de esos archivos). Una vez exitoso, selecciona **Next: Notifications**.
8. Añade correo(s) electrónico(s) de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Opcionalmente, activa las notificaciones de errores a nivel de usuario y de sincronizaciones correctas.
9. Crea la sincronización.

{% details Experiencia de disponibilidad general %}

1. Para crear una nueva integración, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y selecciona **S3 Import** en la sección de fuentes de archivos. 
2. Introduce la información del proceso de configuración de AWS para crear una nueva sincronización. Especifica lo siguiente:

  - ARN del rol
  - ID externo
  - URL de SQS (debe ser única para cada nueva integración)
  - Nombre de contenedor
  - Ruta de la carpeta (opcional, debe ser única en todas las sincronizaciones de un espacio de trabajo)
  - Región

{: start="3"}
3. Ponle un nombre a tu integración y selecciona el tipo de datos para esta integración. 

{: start="4"}
4. Añade un correo electrónico de contacto para recibir notificaciones si la sincronización se interrumpe por problemas de acceso o permisos. Opcionalmente, activa las notificaciones de errores a nivel de usuario y de sincronizaciones correctas. 

{: start="5"}
5. Por último, selecciona **Test connection** para confirmar que Braze puede acceder a tu contenedor y listar los archivos disponibles para ingestar (no los datos dentro de esos archivos). A continuación, guarda la sincronización. 

{% enddetails %}

## Formatos de archivo necesarios

La ingesta de datos en la nube admite archivos JSON, CSV y Parquet. Las columnas requeridas dependen del tipo de datos: 

- Los datos de usuario (atributos, eventos personalizados, eventos de compra) utilizan identificadores de usuario y una carga útil
- Los datos de catálogo utilizan identificadores de catálogo

Braze no impone ningún requisito adicional para los nombres de archivo más allá de los que impone AWS. Los nombres de los archivos deben ser únicos. Añadir una marca de tiempo ayuda a garantizar la unicidad.

Para ver ejemplos de todos los tipos de archivos compatibles (atributos, eventos personalizados, compras, catálogos y eliminaciones de usuarios), consulta los archivos de ejemplo en [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuario {#user-identifiers}

Para las sincronizaciones de datos de usuario (atributos, eventos personalizados, eventos de compra), cada fila de tu archivo fuente requiere exactamente un identificador de usuario y una columna `PAYLOAD`. Un archivo fuente puede contener filas con diferentes tipos de identificador, pero cada fila individual solo debe usar uno.

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`. |
| `BRAZE_ID` | El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, Braze utilizará el correo electrónico como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Además de un identificador, cada fila debe incluir una columna `PAYLOAD` que contenga una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

{% alert note %}
A diferencia de las fuentes de almacén de datos, la columna `UPDATED_AT` no es necesaria ni está admitida para las sincronizaciones de almacenamiento de archivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para las sincronizaciones de catálogo, tu archivo fuente debe contener las siguientes columnas. Los archivos de catálogo utilizan identificadores diferentes a los archivos de datos de usuario.

| Columna | Obligatoria | Descripción |
| --- | --- | --- |
| `ID` | Sí | El identificador único del elemento del catálogo. Se utiliza para crear, actualizar o eliminar el elemento en Braze. |
| `PAYLOAD` | Sí | Una cadena JSON de los campos y valores del catálogo a sincronizar. Debe coincidir con el esquema de tu catálogo en Braze. |
| `DELETED` | No | Cuando es `true`, el elemento del catálogo con el `ID` correspondiente se elimina del catálogo en Braze. Omite esta columna o establécela en `false` para operaciones de creación o actualización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Ejemplos

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
Cada línea de tu archivo fuente debe contener un JSON válido o el archivo será omitido. 
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un JSON válido o el archivo será omitido. 
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Cada línea de tu archivo fuente debe contener un JSON válido o el archivo será omitido.
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
Incluye una columna `DELETED` opcional. Cuando `DELETED` es `true`, ese elemento del catálogo se elimina del catálogo en Braze. Para ver la lista completa de columnas requeridas, consulta [Identificadores de catálogo](#catalog-identifiers). Para el comportamiento de eliminación, consulta [Eliminación de elementos del catálogo](#deleting-catalog-items).
{% endtab %}

{% endtabs %}  

## Eliminación de datos

La ingesta de datos en la nube para S3 admite la eliminación de usuarios y elementos del catálogo mediante la carga de archivos. Utiliza sincronizaciones y formatos de archivo distintos para cada uno.

- **[Eliminación de usuarios](#deleting-users)**: crea una sincronización con el tipo de datos **Delete Users** y carga archivos que solo contengan identificadores de usuario (sin carga útil).
- **[Eliminación de elementos del catálogo](#deleting-catalog-items)**: utiliza la sincronización del catálogo existente y añade una columna `deleted` (o `DELETED`) para marcar los elementos que deseas eliminar.

### Eliminación de usuarios

Para eliminar perfiles de usuario en Braze utilizando archivos en S3:

1. Crea una nueva sincronización de Cloud Data Ingestion (con la misma [configuración de AWS y Braze](#setting-up-cloud-data-ingestion-in-aws) que para otras sincronizaciones).
2. Al configurar la sincronización en Braze, establece **Data Type** en **Delete Users**.
3. Sube archivos a tu contenedor de S3 que solo contengan columnas de identificadores de usuario. No incluyas una columna `PAYLOAD`: la sincronización falla si hay carga útil, para evitar eliminaciones accidentales.

Cada fila del archivo debe identificar exactamente a un usuario utilizando uno de los siguientes:

| Identificador | Descripción |
| --- | --- |
| `EXTERNAL_ID` | Coincide con el `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Ambas columnas juntas identifican al usuario por su alias. |
| `BRAZE_ID` | ID de usuario generado por Braze (solo usuarios existentes). |

{% alert important %}
La eliminación de usuarios es permanente y no se puede deshacer. Incluye solo los usuarios que deseas eliminar. Para obtener más información, consulta [Eliminar usuarios con Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/).
{% endalert %}

**Ejemplo – JSON (eliminación de usuarios):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Ejemplo – CSV (eliminación de usuarios):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Cuando se ejecuta la sincronización, Braze procesa los nuevos archivos del contenedor y elimina los perfiles de usuario correspondientes.

### Eliminación de elementos del catálogo

Para eliminar elementos de un catálogo utilizando el almacenamiento de archivos:

1. Utiliza la misma sincronización S3 que utilizas para [sincronizar los datos del catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) (tipo de datos **Catalogs**).
2. En tus archivos CSV o JSON, añade una columna opcional **`deleted`** (o **`DELETED`**).
3. Establece `deleted` en `true` para cualquier elemento del catálogo que quieras eliminar del catálogo en Braze.

Cada fila aún necesita `ID` y `PAYLOAD`. Para las filas marcadas para eliminación, la carga útil puede ser mínima; Braze elimina el elemento mediante `ID`.

**Ejemplo – JSON (eliminación de elemento del catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Ejemplo – CSV (eliminación de elemento del catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Cuando se ejecuta la sincronización, las filas con `deleted: true` provocan que el elemento del catálogo correspondiente se elimine en Braze. Para obtener información completa sobre la sincronización y eliminación del catálogo, consulta [Sincronizar y eliminar datos del catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/).

## Lo que hay que saber

- Los archivos añadidos al contenedor de origen de S3 no deben superar los 512&nbsp;MB. Los archivos de más de 512&nbsp;MB darán lugar a un error y no se sincronizarán con Braze.
- Aunque no hay ningún límite adicional en cuanto al número de filas por archivo, recomendamos utilizar archivos más pequeños para mejorar la velocidad de las sincronizaciones. Por ejemplo, un archivo de 500&nbsp;MB tardaría considerablemente más en importarse que cinco archivos separados de 100&nbsp;MB.
- No hay ningún límite adicional en cuanto al número de archivos que puedes subir en un tiempo determinado.
- No se admite el orden en los archivos ni entre ellos. Recomendamos agrupar las actualizaciones periódicamente si estás supervisando cualquier condición de carrera prevista.

## Solución de problemas

### Carga y procesamiento de archivos

CDI solo procesará los archivos que se añadan después de crear la sincronización. En este proceso, Braze busca nuevos archivos que se añadan, lo que desencadena un nuevo mensaje a SQS. Esto inicia una nueva sincronización para procesar el nuevo archivo.

Puedes utilizar archivos existentes para validar que Braze puede acceder a tu contenedor y detectar archivos para ingestar, pero estos no se sincronizan con Braze. Para que CDI los procese, debes volver a subir a S3 cualquier archivo existente que desees sincronizar. 

### Manejo de errores inesperados en los archivos

Si observas un número elevado de errores o archivos fallidos, es posible que haya otro proceso añadiendo archivos al contenedor de S3 en una carpeta distinta a la carpeta de destino para CDI.

Cuando los archivos se cargan en el contenedor de origen pero no en la carpeta de origen, CDI procesará la notificación SQS, pero no realizará ninguna acción sobre el archivo, por lo que esto puede aparecer como un error.