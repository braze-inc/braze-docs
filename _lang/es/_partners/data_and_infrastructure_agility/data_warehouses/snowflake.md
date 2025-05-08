---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artículo de referencia describe la asociación entre Braze y Snowflake, un almacén de datos en la nube SQL creado específicamente para todos tus datos y usuarios."
page_type: partner
search_tag: Partner

---

# [![Curso de Braze Learning]( {% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) es un almacén de datos SQL en la nube creado específicamente y proporcionado como software como servicio (SaaS). Snowflake proporciona un almacén de datos más rápido, fácil de usar y mucho más flexible que las ofertas tradicionales de almacén de datos. Con la arquitectura única y patentada de Snowflake, es fácil acumular todos tus datos, habilitar análisis rápidos y obtener información basada en datos para todos tus usuarios.

Las campañas de marketing personalizadas y relevantes requieren un acceso a los datos en el momento. Por eso Braze se asoció con Snowflake para lanzar el intercambio de datos. Esta oferta conjunta habilita a los especialistas en marketing a liberar el potencial de la interacción con los clientes y los datos de campaña más rápido que nunca.

La [integración de Braze y Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) aprovecha el intercambio de datos de Snowflake para construir una presencia, encontrar nuevos clientes y ampliar el alcance a través de la creciente base de clientes de Snowflake.

{% alert tip %}
**¿Te interesa tener acceso a los datos a nivel de Snowflake sin necesidad de tener una cuenta Snowflake?**<br>Consulta [las cuentas de los lectores de Snowflake]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Con las Cuentas de Lector, Braze creará y compartirá tus datos en una cuenta y te proporcionará credenciales para iniciar sesión y acceder a tus datos. De este modo, todos los datos compartidos y la facturación por uso serán gestionados íntegramente por Braze.
{% endalert %}

## ¿Qué es compartir datos?

La funcionalidad de [Compartición Segura de Datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permite a Braze darte acceso seguro a los datos de nuestro portal Snowflake sin preocuparte por la fricción o ralentización del flujo de trabajo, los puntos de fallo y los costes innecesarios que conllevan las relaciones típicas con los proveedores de datos. El intercambio de datos puede configurarse mediante la siguiente integración o a través de [las cuentas de Snowflake Reader]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

- **Reduce el tiempo para obtener información**<br>Di adiós a los procesos ETL que tardan semanas en crearse. Las arquitecturas únicas de Braze y Snowflake hacen que todos los datos de interacción con los clientes y de campañas sean inmediatamente accesibles y consultables desde el instante en que llegan al «data lake». No se copian ni se trasladan datos, por lo que puedes entregar experiencias del cliente basadas únicamente en la información más relevante y actualizada.
- **Analiza los silos de datos**<br>Crea una visión holística de tus clientes a través de canales y plataformas. Compartir datos hace que unir tus datos de interacción con los clientes de Braze con el resto de tus datos de Snowflake sea más fácil que nunca, creando información más rica a través de una única fuente fiable de la verdad.
- **Comprueba cómo funciona tu interacción**<br>Optimiza tus estrategias de interacción con los clientes con Braze Benchmarks. Esta herramienta interactiva, desarrollada por Braze y Snowflake, te permite comparar los datos de interacción de tu marca con puntos de referencia de distintos canales, sectores y plataformas de dispositivos.

Con la compartición de datos, no se copian ni transfieren datos reales entre cuentas. Todo el intercambio se realiza a través de la capa de servicios y el almacén de metadatos únicos de Snowflake. Se trata de un concepto importante porque los datos compartidos no ocupan almacenamiento en la cuenta del consumidor y, por tanto, no contribuyen a los gastos mensuales de almacenamiento de datos del consumidor. **Lo único que** se cobra a los consumidores son los recursos informáticos (como los almacenes virtuales) utilizados para consultar los datos compartidos.

Además, utilizando las funciones y permisos incorporados de Snowflake, el acceso a los datos compartidos desde Braze puede controlarse y gobernarse utilizando los controles de acceso ya existentes para tu cuenta de Snowflake y los datos que contiene. El acceso puede restringirse y controlarse del mismo modo que tus propios datos.

Consulta [Introducción a la compartición segura de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work) para saber más sobre cómo funciona la compartición de datos de Snowflake.

## Requisitos previos

Si te interesa esta integración, ponte en contacto con tu administrador del éxito del cliente o de tu cuenta Braze y pídeles que consulten los servicios de estrategia de datos de Braze sobre el Intercambio seguro de datos de clientesDatos con Snowflake. Esto pondrá en marcha los engranajes dentro de Braze, ¡y tendremos tus vistas configuradas en un abrir y cerrar de ojos!

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Snowflake | Se necesita una cuenta Snowflake con permisos de nivel de administrador para aprovechar esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Para configurar el Uso Compartido Seguro de Datos con tu cuenta Braze, sigue estos pasos.

1. Ve a **Integraciones de socios** > **Compartir datos** en el panel de Braze.
2. Introduce los datos de tu cuenta Snowflake. Puedes encontrar el ID de tu cuenta Snowflake ejecutando `SELECT CURRENT_ACCOUNT()` en la cuenta de destino.
3. Si utilizas un recurso compartido CRR, especifica el proveedor de la nube y la región.
4. Selecciona **Crear Datashare**.

En unos instantes, tus datos compartidos deberían ser visibles en tu instancia de Snowflake. Crea una base de datos a partir del recurso compartido para que puedas ver y consultar las tablas. Ten en cuenta que necesitarás ser administrador de la cuenta para ver los datos compartidos.

![Compartir datos entrantes]({% image_buster /assets/img/inbound-data-share.png %})

En el contexto de la compartición de datos, Braze es un [proveedor de datos: cualquier](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) cuenta Snowflake que crea comparticiones y las pone a disposición de otras cuentas Snowflake para que las consuman. Eres un [consumidor de datos, es decir, una](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) cuenta que decide crear una base de datos a partir de una acción puesta a disposición por un proveedor de datos.

## Utilización y visualización

Una vez aprovisionado el recurso compartido de datos, tendrás que crear una base de datos a partir del recurso compartido de datos entrante, haciendo que todas las tablas compartidas aparezcan en tu instancia Snowflake y puedan consultarse como cualquier otro dato que estés almacenando en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de sólo lectura y sólo pueden consultarse, pero no modificarse ni borrarse de ninguna manera.

De forma similar a Currents, puedes utilizar tu compartición segura de datos de Snowflake para:
- Crear informes complejos
- Realizar modelos de atribución
- Compartir de forma segura dentro de tu propia empresa
- Mapear los datos brutos de eventos o usuarios a un CRM (como Salesforce)
- Y más

[Descarga aquí los esquemas de las tablas en bruto.][esquemas]

### Esquema de ID de usuario

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Snowflake para los ID de usuario.

| Esquema Braze | Esquema Snowflake | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que asigna automáticamente Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Información importante y limitaciones

### Cambios de ruptura frente a cambios sin ruptura

#### Cambios sin ruptura
Los cambios no rupturistas pueden producirse en cualquier momento y generalmente proporcionan funcionalidad adicional. Ejemplos de cambios sin ruptura:
- Añadir una nueva tabla o vista
- Añadir una columna a una tabla o vista existente

{% alert important %}
Dado que las columnas nuevas se consideran de no ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta, en lugar de utilizar las consultas de `SELECT *`. Otra posibilidad es crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios de última hora
Siempre que sea posible, los cambios de última hora irán precedidos de un anuncio y de un periodo de migración. Algunos ejemplos de cambios de última hora son:
- Eliminar una tabla o una vista
- Eliminar una columna de una tabla o vista existente
- Cambiar el tipo o la anulabilidad de una columna existente

### Regiones Snowflake
Braze aloja actualmente todos los datos a nivel de usuario en las regiones Snowflake AWS US East-1 y EU-Central (Frankfurt). Para los usuarios de fuera de esas regiones, Braze puede proporcionar datos compartidos a clientes conjuntos que alojen su infraestructura Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos

#### Política de retención
Los datos que tengan más de dos años se archivarán y se trasladarán a un almacenamiento a largo plazo. Como parte del proceso de archivo, todos los eventos se anonimizan y se elimina cualquier campo confidencial de información personal identificable (PII) (esto incluye opcionalmente campos PII como `properties`). Los datos archivados siguen conteniendo el campo `user_id`, que permite el análisis por usuario de todos los datos de eventos.

Podrás consultar los datos de los dos últimos años de cada evento en la vista correspondiente de `USERS_*_SHARED`. Además, cada suceso tendrá una vista `USERS_*_SHARED_ALL` que puede consultarse para obtener datos anonimizados y no anonimizados.

#### Datos históricos
El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. Durante los primeros meses en los que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber provocado que algunos de esos datos tengan un aspecto ligeramente diferente o algunos valores nulos (ya que en ese momento no pasábamos datos a todos los campos disponibles). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede ser ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD)
Casi todos los registros de eventos que almacena Braze incluyen algunos campos que representan la información personal identificadora (PII) de los usuarios. Algunos eventos pueden incluir la dirección de correo electrónico, el número de teléfono, el ID del dispositivo, el idioma, el sexo y la información sobre la ubicación. Si se envía a Braze la solicitud de olvido de un usuario, anularemos esos campos de PII para cualquier evento que pertenezca a esos usuarios. De este modo, no eliminamos el registro histórico del acontecimiento, pero ahora el acontecimiento nunca podrá vincularse a un individuo concreto.

### Velocidad, rendimiento, coste de las consultas
La velocidad, el rendimiento y el coste de cualquier consulta realizada sobre los datos vienen determinados por el tamaño del almacén que utilices para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para el análisis, puede que necesites utilizar un almacén de mayor tamaño para que la consulta tenga éxito. Snowflake dispone de excelentes recursos sobre la mejor forma de determinar qué tamaño utilizar, entre los que se incluyen [Resumen de los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

## Puntos de referencia Braze

Benchmarks, [una herramienta de datos creada por Braze](https://www.braze.com/perspectives/benchmarks), permite a los clientes potenciales y a los clientes de Braze ver cómo se comparan con los principales actores de su sector comparando sus métricas con los puntos de referencia del sector de Braze.

Los sectores iniciales incluyen:
- Servicios de entrega
- Comercio electrónico
- Educación
- Entretenimiento
- Finanzas
- Juegos
- Salud
- Estilo de vida
- Restaurantes
- Comercio minorista
- Tecnología
- Transporte
- Viajes

Nuestros datos de evaluación comparativa también están disponibles directamente en el [Intercambio de Datos de Snowflake](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR).

> Si quieres consultar un conjunto de consultas de ejemplo para configurar Snowflake, consulta nuestros ejemplos de [consultas de ejemplo][SQ] y de [configuración de canalización de eventos ETL][ETL].

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[esquemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
