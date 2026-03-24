---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artículo describe la asociación entre Braze y Snowflake, cubriendo tanto la compartición de datos (de Braze a Snowflake) como la ingesta de datos en la nube (de Snowflake a Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) es un almacén de datos SQL en la nube creado específicamente y proporcionado como software como servicio (SaaS). Snowflake proporciona un almacén de datos más rápido, fácil de usar y mucho más flexible que las ofertas tradicionales de almacén de datos. Con la arquitectura única y patentada de Snowflake, es fácil acumular todos tus datos, habilitar análisis rápidos y obtener información basada en datos para todos tus usuarios.

Braze ofrece dos integraciones con Snowflake. Juntas, proporcionan un pipeline de datos bidireccional completo entre tus entornos de Braze y Snowflake.

## Elegir una integración

### Compartición de datos (de Braze a Snowflake)

La [compartición segura de datos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) de Snowflake te da acceso seguro y en tiempo real a los datos de interacción y campañas de Braze directamente en tu instancia de Snowflake. No se copian ni transfieren datos entre cuentas: toda la compartición se realiza a través de la capa de servicios y el almacén de metadatos únicos de Snowflake.

**Usa la compartición de datos cuando quieras:**
- Consultar datos de eventos y campañas de Braze usando SQL de Snowflake
- Crear informes complejos y realizar modelos de atribución
- Unir datos de Braze con otros datos en tu almacén de Snowflake
- Comparar tus datos de interacción entre canales, sectores y plataformas de dispositivos

Para instrucciones de configuración, consulta [Compartición de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Ingesta de datos en la nube (de Snowflake a Braze)

La [ingesta de datos en la nube (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) te permite sincronizar datos desde tu instancia de Snowflake directamente en Braze. Esto te permite mantener los atributos de usuario, eventos y compras en Braze actualizados con tu almacén de datos como fuente de la verdad.

**Usa la ingesta de datos en la nube cuando quieras:**
- Sincronizar atributos de usuario desde Snowflake a perfiles de usuario de Braze
- Enviar datos de eventos o compras desde Snowflake a Braze
- Mantener Braze sincronizado con las transformaciones de datos que ocurren en tu almacén
- Evitar construir y mantener pipelines ETL personalizados de Snowflake a Braze

Para saber más sobre la compartición de datos de Snowflake, consulta [Introducción a la compartición segura de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Requisitos previos

Antes de poder utilizar esta característica, tendrás que completar lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Para acceder a esta característica en Braze, tendrás que ponerte en contacto con tu administrador de cuenta o administrador del éxito del cliente de Braze. |
| Cuenta de Snowflake | Una cuenta de Snowflake con permisos `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de la compartición segura de datos

En Snowflake, los datos se comparten entre un [proveedor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) y un [consumidor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). En este contexto, tu cuenta de Braze es el proveedor de datos porque crea y envía el datashare, mientras que tu cuenta de Snowflake es el consumidor de datos porque utiliza el datashare para crear una base de datos. Para más detalles, consulta [Snowflake: Consumir datos compartidos](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Paso 1: Enviar el datashare desde Braze

1. En Braze, ve a **Integraciones de socios** > **Compartir datos**.
2. Introduce los datos de tu cuenta de Snowflake y el localizador. Para obtener el localizador de tu cuenta, ejecuta `SELECT CURRENT_ACCOUNT()` en la cuenta de destino.
3. Si utilizas un recurso compartido CRR, especifica el proveedor de la nube y la región.
4. Cuando hayas terminado, selecciona **Crear Datashare**. Esto enviará el datashare a tu cuenta de Snowflake.

### Paso 2: Crea la base de datos en Snowflake

1. Al cabo de unos minutos, deberías recibir el datashare de entrada en tu cuenta de Snowflake.
2. Utilizando el datashare de entrada, crea una base de datos para ver y consultar las tablas. Por ejemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Concede privilegios para consultar la nueva base de datos.

{% alert warning %}
Si eliminas y vuelves a crear un recurso compartido en el panel de Braze, debes eliminar la base de datos creada anteriormente y volver a crearla utilizando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar el recurso compartido de entrada.
Si tienes varios espacios de trabajo que comparten datos con la misma cuenta de Snowflake, consulta las [preguntas frecuentes sobre la compartición de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) para obtener orientación sobre la gestión de configuraciones con varios espacios de trabajo.
{% endalert %}

## Uso y visualización

Una vez aprovisionado el recurso compartido de datos, tendrás que crear una base de datos a partir del recurso compartido de datos de entrada, para que todas las tablas compartidas aparezcan en tu instancia de Snowflake y puedan consultarse como cualquier otro dato que almacenes en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de solo lectura y solo pueden consultarse, pero no modificarse ni eliminarse de ninguna manera.

De forma similar a Currents, puedes utilizar tu compartición segura de datos de Snowflake para:

- Crear informes complejos
- Realizar modelos de atribución
- Compartir de forma segura dentro de tu propia empresa
- Mapear los datos brutos de eventos o usuarios a un CRM (como Salesforce)
- Y más

Para obtener una lista completa de las tablas y columnas disponibles, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). La compartición de datos de Snowflake incluye todas las tablas de esa referencia, además de tablas exclusivas de Snowflake para instantáneas, registros de cambios de campañas y Canvas, eventos de la consola de agentes y eventos de reintentos de mensajes.

También puedes [descargar los esquemas de las tablas sin procesar]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) como archivo de texto.

### Esquema de ID de usuario

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Snowflake para los ID de usuario.

| Esquema de Braze | Esquema de Snowflake | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que asigna automáticamente Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Información importante y limitaciones

### Cambios de ruptura frente a cambios sin ruptura

#### Cambios sin ruptura

Los cambios sin ruptura pueden producirse en cualquier momento y generalmente proporcionan funcionalidad adicional. Ejemplos de cambios sin ruptura:
- Añadir una nueva tabla o vista
- Añadir una columna a una tabla o vista existente

{% alert important %}
Dado que las columnas nuevas se consideran cambios sin ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta, en lugar de utilizar consultas `SELECT *`. Otra posibilidad es crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios de ruptura

Siempre que sea posible, los cambios de ruptura irán precedidos de un anuncio y de un periodo de migración. Algunos ejemplos de cambios de ruptura son:
- Eliminar una tabla o una vista
- Eliminar una columna de una tabla o vista existente
- Cambiar el tipo o la nulabilidad de una columna existente

### Regiones de Snowflake

Braze aloja actualmente todos los datos de usuario en las regiones de Snowflake AWS US East-1, EU-Central (Frankfurt), AP-Southeast-2 (Sídney) y AP-Southeast-3 (Yakarta). Para los usuarios de fuera de esas regiones, Braze puede proporcionar datos compartidos a clientes conjuntos que alojen su infraestructura de Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos

#### Política de retención

Los datos que tengan más de dos años se archivarán y se trasladarán a un almacenamiento a largo plazo. Como parte del proceso de archivo, todos los eventos se anonimizan y se elimina cualquier campo confidencial de información personal identificable (PII) (esto incluye campos PII opcionales como `properties`). Los datos archivados siguen conteniendo el campo `user_id`, que permite el análisis por usuario de todos los datos de eventos.

Podrás consultar los datos de los dos últimos años de cada evento en la vista correspondiente `USERS_*_SHARED`. Además, cada evento tendrá una vista `USERS_*_SHARED_ALL` que puede consultarse para obtener datos tanto anonimizados como no anonimizados.

#### Datos históricos

El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. Durante los primeros meses en los que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber provocado que algunos de esos datos tengan un aspecto ligeramente diferente o algunos valores nulos (ya que en ese momento no pasábamos datos a todos los campos disponibles). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede ser ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD)

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Velocidad, rendimiento y coste de las consultas

La velocidad, el rendimiento y el coste de cualquier consulta realizada sobre los datos vienen determinados por el tamaño del almacén que utilices para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para el análisis, puede que necesites utilizar un almacén de mayor tamaño para que la consulta tenga éxito. Snowflake dispone de excelentes recursos sobre la mejor forma de determinar qué tamaño utilizar, entre los que se incluyen [Resumen de los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Si quieres consultar un conjunto de consultas de ejemplo para configurar Snowflake, echa un vistazo a nuestros ejemplos de [consultas de ejemplo]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) y de [configuración de canalización de eventos ETL]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

Para instrucciones de configuración, consulta [Ingesta de datos en la nube: integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).