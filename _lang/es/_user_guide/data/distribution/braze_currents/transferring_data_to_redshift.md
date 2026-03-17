---
nav_title: Transferir datos a Redshift
article_title: Transferencia de datos a Redshift
page_order: 8
page_type: tutorial
description: "Este artículo te explicará cómo transferir datos de Amazon S3 a Redshift mediante un proceso de extraer, transformar, cargar (ETL)."
tool: Currents

---

# Transferir datos a Redshift

> [Amazon Redshift](https://aws.amazon.com/redshift/) es un popular almacén de datos que se ejecuta en Amazon Web Services junto con Amazon S3. Los datos de Braze de Currents están estructurados para su transferencia directa a Redshift.

A continuación se describe cómo transferir datos de Amazon S3 a Redshift mediante un proceso de extracción, transformación y carga (ETL). Para obtener el código fuente completo, consulta el [repositorio GitHub](https://github.com/Appboy/currents-examples) de ejemplos de Currents.

{% alert important %}
Ésta es sólo una de las muchas opciones que puedes elegir a la hora de transferir tus datos a los lugares que te resulten más ventajosos.
{% endalert %}

## Resumen del cargador de S3 a Redshift

El[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader)script utiliza una tabla de manifiesto independiente en la misma base de datos Redshift para realizar el seguimiento de los archivos que ya se han copiado. La estructura general es la siguiente:

1. Enumera todos los archivos en S3 y, a continuación, identifica los archivos nuevos desde la última vez que ejecutaste`s3loader.py`  comparando la lista con el contenido de la tabla del manifiesto.
2. Crea un archivo [manifiesto](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) que contenga los nuevos archivos.
3. Ejecuta una`COPY`consulta para copiar los nuevos archivos de S3 a Redshift utilizando el archivo de manifiesto.
4. Inserta los nombres de los archivos que se copian en la tabla de manifiesto independiente en Redshift.
5. Comprométete.

## Dependencias

Debes instalar AWS Python SDK y Psycopg para poder ejecutar el cargador:

```bash
pip install boto3
pip install psycopg2
```

## Permisos

### Función Redshift con acceso de lectura a S3

Si aún no lo has hecho, sigue la [documentación de AWS](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) para crear una función que pueda ejecutar`COPY`  comandos en tus archivos en AWS S3.

### Reglas de entrada de Redshift VPC

Si tu clúster Redshift se encuentra en una VPC, debes configurar la VPC para permitir las conexiones desde el servidor en el que se ejecuta S3 Loader. Entra en tu clúster de Redshift y selecciona la entrada de grupos de seguridad de VPC a la que deseas que se conecte el cargador. A continuación, añade una nueva regla de entrada: **Tipo** = Redshift, **Protocolo** = TCP, **Puerto** = el puerto de tu clúster, **Origen** = la IP del servidor que ejecuta el cargador (o «Cualquiera» para realizar pruebas).

### Usuario de gestión de identidades y accesos (IAM) con acceso completo a S3

El cargador S3 requiere acceso de lectura a los archivos que contienen tus datos de Currents y acceso completo a la ubicación de los archivos de manifiesto que genera para los comandos `COPY`Redshift. Crea un nuevo usuario de Gestión de identidades y accesos (IAM) con el`AmazonS3FullAccess`permiso de la [consola de IAM](https://console.aws.amazon.com/iam/home#/users). Guarda las credenciales, ya que tendrás que pasárselas al cargador.

Puedes pasar las credenciales de acceso al cargador a través de variables de entorno, el archivo de credenciales compartidas (`~/.aws/credentials`) o el [archivo de configuración de AWS](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials). Como alternativa, puedes incluirlas directamente en el cargador asignándolas a los`aws_secret_access_key`campos`aws_access_key_id`  y  dentro de un`S3LoadJob`objeto , pero no recomendamos codificar las credenciales en tu código fuente.

## Uso

### Ejemplo de uso

El siguiente programa de ejemplo carga datos para el`users.messages.contentcard.Impression`evento desde S3 a la`content_card_impression`tabla en Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Credenciales

Para ejecutar el cargador, primero debes proporcionar el `host`, `port`, y`database`  de tu clúster Redshift, así como el`user`  y`password`  de un usuario Redshift que pueda ejecutar`COPY`consultas . Además, debes proporcionar el ARN de la función de Redshift con acceso de lectura a S3 que creaste en una sección anterior.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Configuración del trabajo

Debes proporcionar el contenedor de S3 y el prefijo de tus archivos de eventos, así como el nombre de la tabla Redshift en la que deseas`COPY`  los datos.

Además, para los archivos`COPY` Avro con la opción «auto» requerida por el cargador, la definición de columna en tu tabla Redshift debe coincidir con los nombres de campo del esquema Avro, tal y como se muestra en el programa de ejemplo, con los tipos mapeados (por ejemplo,`string`  a `text`,`int`  a `integer`).

También puedes pasar una`batch_size`opción al cargador si consideras que tarda demasiado en copiar todos los archivos a la vez. Al pasar un`batch_size`  , el cargador puede copiar y confirmar de forma incremental un lote cada vez sin tener que copiar todo al mismo tiempo. El tiempo que tarda en cargarse un lote depende del`batch_size`  , así como del tamaño de los archivos y del tamaño del clúster de Redshift.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```