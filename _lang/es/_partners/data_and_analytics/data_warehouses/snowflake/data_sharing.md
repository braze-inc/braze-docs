---
nav_title: "Compartir datos"
article_title: Compartir datos con Snowflake
page_order: 0
description: "Este artículo de referencia cubre la integración de Snowflake Secure Data Sharing, que te permite acceder a los datos de interacción y campañas de Braze directamente en tu instancia de Snowflake."
page_type: partner
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Compartir datos con Snowflake

> [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permite a Braze darte acceso seguro a los datos en nuestro portal de Snowflake sin preocuparte por fricciones o ralentizaciones en el flujo de trabajo, puntos de fallo y costes innecesarios que vienen con las relaciones típicas con proveedores de datos. El uso compartido de datos se puede configurar a través de la siguiente integración o a través de [cuentas de lectura de Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

{% alert tip %}
**¿Te interesa tener acceso a datos a nivel de Snowflake sin necesidad de una cuenta de Snowflake?**<br>Consulta las [cuentas de lectura de Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Con las cuentas de lectura, Braze creará y compartirá tus datos en una cuenta y te proporcionará credenciales para iniciar sesión y acceder a tus datos. Esto hará que toda la facturación del uso compartido de datos y del uso sea gestionada íntegramente por Braze.
{% endalert %}

## Acerca de Secure Data Sharing

Con el uso compartido de datos, no se copian ni transfieren datos reales entre cuentas. Todo el uso compartido se realiza a través de la capa de servicios única de Snowflake y el almacén de metadatos. Este es un concepto importante porque los datos compartidos no ocupan almacenamiento en tu cuenta y, por lo tanto, no contribuyen a tus cargos mensuales de almacenamiento de datos. Los **únicos** cargos son por los recursos de computación (como los almacenes virtuales) utilizados para consultar los datos compartidos.

Además, utilizando las capacidades integradas de roles y permisos de Snowflake, el acceso a los datos compartidos desde Braze puede controlarse y gobernarse utilizando los controles de acceso ya existentes para tu cuenta de Snowflake y los datos que contiene. El acceso puede restringirse y monitorizarse de la misma manera que tus propios datos.

- **Reduce el tiempo para obtener información**<br>Di adiós a los procesos ETL que tardan semanas en construirse. Las arquitecturas únicas de Braze y Snowflake hacen que todos los datos de interacción con los clientes y campañas sean inmediatamente accesibles y consultables desde el instante en que llegan al data lake. No se copian ni mueven datos, por lo que puedes ofrecer experiencias del cliente basadas únicamente en la información más relevante y actualizada.
- **Elimina los silos de datos**<br>Crea una visión holística de tus clientes a través de canales y plataformas. El uso compartido de datos hace que unir tus datos de interacción con los clientes de Braze con todos tus demás datos de Snowflake sea más fácil que nunca, creando información más rica a través de una única fuente de verdad fiable.
- **Compara tu rendimiento de interacción**<br>Optimiza tus estrategias de interacción con los clientes con Braze Benchmarks. Esta herramienta interactiva, impulsada por Braze y Snowflake, te permite comparar los datos de interacción de tu marca con puntos de referencia en canales, industria y plataformas de dispositivos.

Para obtener más información sobre el uso compartido de datos de Snowflake, consulta [Introducción a Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Ponte en contacto con tu administrador de cuenta o administrador del éxito del cliente de Braze para configurar el uso compartido de datos. |
| Cuenta de Snowflake | Una cuenta de Snowflake con permisos de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurar Secure Data Sharing

En Snowflake, el uso compartido de datos se realiza entre un [proveedor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) y un [consumidor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). En este contexto, tu cuenta de Braze es el proveedor de datos porque crea y envía el datashare&#8212;mientras que tu cuenta de Snowflake es el consumidor de datos porque utiliza el datashare para crear una base de datos. Para más detalles, consulta [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Paso 1: Enviar el datashare desde Braze

1. En Braze, ve a **Integraciones de socios** > **Compartir datos**.
2. Introduce los detalles y el localizador de tu cuenta de Snowflake. Para obtener tu localizador de cuenta, ejecuta `SELECT CURRENT_ACCOUNT()` en la cuenta de destino.
3. Si estás utilizando un recurso compartido CRR, especifica el proveedor de nube y la región.
4. Cuando hayas terminado, selecciona **Crear datashare**. Esto enviará el datashare a tu cuenta de Snowflake.

### Paso 2: Crear la base de datos en Snowflake

1. Después de unos minutos, deberías recibir el datashare de entrada en tu cuenta de Snowflake.
2. Usando el datashare de entrada, crea una base de datos para ver y consultar las tablas. Por ejemplo:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Otorga privilegios para consultar la nueva base de datos.

{% alert warning %}
Si eliminas y recreas un recurso compartido en el panel de Braze, debes eliminar la base de datos creada previamente y recrearla usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar el recurso compartido de entrada.
Si tienes múltiples espacios de trabajo compartiendo datos a la misma cuenta de Snowflake, consulta las [preguntas frecuentes sobre Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) para obtener orientación sobre la gestión de configuraciones con múltiples espacios de trabajo.
{% endalert %}

## Uso y visualización

Una vez que el recurso compartido de datos esté aprovisionado, crea una base de datos a partir del recurso compartido de datos entrante, haciendo que todas las tablas compartidas aparezcan en tu instancia de Snowflake y sean consultables como cualquier otro dato que estés almacenando en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de solo lectura y solo pueden consultarse, pero no modificarse ni eliminarse de ninguna manera.

De forma similar a Currents, puedes usar Snowflake Secure Data Sharing para:

- Crear informes complejos
- Realizar modelado de atribución
- Compartir de forma segura dentro de tu propia empresa
- Mapear datos de eventos sin procesar o datos de usuario a un CRM (como Salesforce)
- Y más

[Descarga los esquemas de tablas sin procesar aquí.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Esquema de ID de usuario

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Snowflake para los ID de usuario.

| Esquema de Braze | Esquema de Snowflake | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que Braze asigna automáticamente. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario que establece el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Información importante y limitaciones

### Cambios con y sin interrupción

#### Cambios sin interrupción

Los cambios sin interrupción pueden ocurrir en cualquier momento y generalmente proporcionan funcionalidad adicional. Ejemplos de cambios sin interrupción:
- Añadir una nueva tabla o vista
- Añadir una columna a una tabla o vista existente

{% alert important %}
Dado que las nuevas columnas se consideran cambios sin interrupción, Braze recomienda encarecidamente listar explícitamente las columnas de interés en cada consulta en lugar de usar consultas `SELECT *`. Alternativamente, podrías crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios con interrupción

Cuando sea posible, los cambios con interrupción irán precedidos de un anuncio y un período de migración. Ejemplos de cambios con interrupción incluyen:
- Eliminar una tabla o vista
- Eliminar una columna de una tabla o vista existente
- Cambiar el tipo o la nulabilidad de una columna existente

### Regiones de Snowflake

Braze actualmente aloja todos los datos a nivel de usuario en estas regiones de Snowflake en AWS:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)
 
Para usuarios fuera de esas regiones, Braze puede proporcionar uso compartido de datos a clientes conjuntos que alojan su infraestructura de Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos

#### Política de retención

Cualquier dato con más de dos años de antigüedad será archivado y trasladado a almacenamiento a largo plazo. Como parte del proceso de archivado, todos los eventos se anonimizan y cualquier campo sensible de información de identificación personal (PII) se elimina (esto incluye campos opcionalmente PII como `properties`). Los datos archivados aún contienen el campo `user_id`, lo que permite análisis por usuario en todos los datos de eventos.

Podrás consultar los dos años más recientes de datos para cada evento en la vista `USERS_*_SHARED` correspondiente. Además, cada evento tendrá una vista `USERS_*_SHARED_ALL` que se puede consultar para devolver tanto datos anonimizados como no anonimizados.

#### Datos históricos

El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. En los primeros meses en que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber provocado que algunos de esos datos se vean ligeramente diferentes o tengan algunos valores nulos (ya que no estábamos pasando datos a todos los campos disponibles en ese momento). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede verse ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD)

{% include partners/snowflake_pii_gdpr.md %}

### Velocidad, rendimiento y coste de las consultas

La velocidad, el rendimiento y el coste de cualquier consulta ejecutada sobre los datos están determinados por el tamaño del almacén que utilices para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para análisis, puede que necesites usar un tamaño de almacén más grande para que la consulta sea exitosa. Snowflake tiene excelentes recursos disponibles sobre cómo determinar mejor qué tamaño usar, incluyendo [Resumen de almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Para un conjunto de consultas de ejemplo como referencia al configurar Snowflake, consulta nuestros ejemplos de [consultas de muestra]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/) y [configuración de pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/).
{% endalert %}