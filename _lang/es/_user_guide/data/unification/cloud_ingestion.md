---
nav_title: Ingesta de datos de Cloud
article_title: Ingesta de datos de Cloud de Braze
alias: /cloud_ingestion/
description: "Este artículo de referencia cubre las fuentes de ingesta de datos en la nube Braze y las recomendaciones de configuración de datos."
page_order: 0.1
toc_headers: h2
---

# Ingesta de datos de Cloud de Braze

> La ingesta de datos en la nube Braze (CDI) te permite configurar una conexión directa desde tu solución de almacenamiento de datos para sincronizar con Braze los datos de usuario relevantes y otros datos que no sean de usuario. Estos datos pueden utilizarse para la personalización o segmentación para potenciar tus casos de uso de marketing. La integración flexible de Cloud Data Ingestion admite estructuras de datos complejas, como JSON anidado y matrices de objetos.

## Cómo funciona

Con Braze Cloud Data Ingestion (CDI), puede configurar una integración entre su instancia de almacén de datos y el espacio de trabajo Braze para sincronizar los datos de forma periódica. Esta sincronización se ejecuta según el calendario que establezcas, y cada integración puede tener un calendario diferente. Las sincronizaciones pueden ser tan frecuentes como cada 15 minutos o tan infrecuentes como una vez al mes. Si necesitas que las sincronizaciones se produzcan con una frecuencia superior a 15 minutos, ponte en contacto con tu administrador del éxito del cliente o considera la posibilidad de utilizar llamadas a la API REST para la ingesta de datos en tiempo real.

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel Braze. Cada vez que se ejecuta la sincronización, los datos actualizados se reflejan en Braze.

### Encontrar tu ID de integración

Puedes encontrar tu ID de integración en la URL cuando veas una integración en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos en la nube** y selecciona una integración. El ID de integración aparece en la URL con el formato `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Por ejemplo, si tu URL es `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, tu ID de integración es `abc123xyz`. Puedes utilizar este ID cuando realices llamadas a la API para desencadenar sincronizaciones o comprobar el estado de las mismas.

## Ejemplos

Con las funciones de ingesta de datos en la nube de Braze, puedes:

- Crea una integración sencilla directamente desde tu almacén de datos o tu solución de almacenamiento de archivos en Braze en solo unos minutos.
- Sincroniza de forma segura los datos de usuario, incluyendo atributos, eventos y compras desde tu almacén de datos a Braze.
- Cierra el bucle de datos con Braze combinando la ingesta de datos en la nube con la compartición de datos Currents o Snowflake.

Además, [las Fuentes Conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) son una alternativa de copia cero. Puedes hacer que Braze consulte directamente tu almacén de datos o solución de almacenamiento de archivos para construir segmentos CDI, todo ello sin copiar los datos subyacentes a Braze.

## Fuentes de datos compatibles

La Ingesta de Datos en la Nube puede sincronizar datos de:

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Tipos de datos admitidos 

La ingesta de datos en la nube admite los siguientes tipos de datos:

### Datos de usuario
- Atributos de usuario, incluyendo:
   - Atributos personalizados anidados
   - Matrices de objetos
   - Estados de suscripción
- Eventos personalizados
- Eventos de compra
- Solicitudes de eliminación de usuarios

### Objetos no usuarios
- Artículos del catálogo

### Mensajería de copia cero
- Fuentes conectadas

## Identificadores de usuario para la ingesta de datos

Al sincronizar datos de usuario a través de la Ingesta de datos en la nube, puedes identificar a los usuarios utilizando uno o varios de los siguientes tipos de identificadores. Cada fila de tu tabla de origen debe contener un valor para un solo tipo de identificador a la vez, pero tu tabla puede incluir columnas para uno, dos, tres, cuatro o los cinco tipos de identificador.

| Identificador | Descripción |
|------------|-------------|
| `EXTERNAL_ID` | El ID externo que identifica el perfil de usuario a crear o actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
| `BRAZE_ID` | El identificador de usuario Braze generado por el SDK Braze. No se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se da prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, se utilizará el correo electrónico como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener información detallada sobre la configuración de tablas con estos identificadores, consulta la documentación [de las integraciones del almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Utilización de puntos de datos

Para los clientes con facturación basada en puntos de datos, la facturación por puntos de datos para la Ingesta de Datos en la Nube es equivalente a la facturación de actualizaciones a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consulte [Puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) para obtener más información. 

{% alert important %}
La ingesta de datos en la nube Braze cuenta para el límite de velocidad disponible, por lo que si envías datos utilizando otro método, el límite de velocidad se combina entre la API Braze y la ingesta de datos en la nube.
{% endalert %}

## Limitaciones del producto

| Limitación            | Descripción                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en el número de integraciones que puedes configurar. Sin embargo, sólo puedes configurar una integración por tabla o vista.                                             |
| Cantidad de filas         | Por defecto, cada ejecución puede sincronizar hasta 500 millones de filas. Se detiene cualquier sincronización con más de 500 millones de filas nuevas. Si necesitas un límite superior, ponte en contacto con tu administrador del éxito del cliente de Braze o con el soporte de Braze. |
| Atributos por fila     | Cada fila debe contener un único ID de usuario y un objeto JSON con un máximo de 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, un array cuenta como un atributo). |
| Tamaño de la carga útil           | Cada fila puede contener una carga útil de hasta 1 MB. Las cargas útiles superiores a 1 MB se rechazan, y el error "La carga útil era superior a 1 MB" se registra en el registro de sincronización junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos              | Puedes sincronizar atributos de usuario, eventos y compras a través de la ingesta de datos en la nube.                                                                                                  |
| Región de Braze           | Este producto está disponible en todas las regiones Braze. Cualquier región Braze puede conectarse a cualquier región de datos de origen.                                                                              |
| Región de origen       | Braze se conecta a tu almacén de datos o entorno de nube en cualquier región o proveedor de nube.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
