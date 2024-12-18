---
nav_title: Uso compartido de datos de Snowflake
hidden: true
---

# Integración de datos compartidos Snowflake

> Cuando se utiliza Snowflake Data Share como método de integración, Braze proporcionará un recurso compartido a su instancia de Snowflake en nombre del cliente. Esta acción incluirá automáticamente todos los eventos de participación en los mensajes y de comportamiento de los usuarios.

Las acciones se aprovisionan por cliente después de que este haya comprado un derecho a compartir datos de Snowflake. Cuando un cliente solicita un uso compartido de datos, Braze añadirá un uso compartido al espacio de trabajo del cliente, y éste podrá utilizar la interfaz de usuario de autoservicio para añadir los datos de la cuenta Snowflake del socio correspondiente.

![]({% image_buster /assets/img/snowflake.png %})

Una vez aprovisionado el recurso compartido, se puede acceder inmediatamente a todos los datos desde la instancia Snowflake como recurso compartido de datos entrantes.

![]({% image_buster /assets/img/snowflake2.png %})

Dentro de tu instancia Snowflake, verás una acción por región. Cada tabla tiene una columna, `app_group_id`, que es efectivamente una clave de inquilino para Braze. A medida que se añadan nuevos clientes a una acción dentro de la misma región, aparecerán como diferentes `app_group_ids` dentro de las tablas existentes.

{% alert important %}
Braze aloja actualmente todos los datos a nivel de usuario en las regiones Snowflake AWS US East-1 y EU-Central (Frankfurt). Aunque Braze puede compartir entre regiones, es más rentable para los clientes si compartimos con `US-EAST-1` y/o `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Descargue aquí los [esquemas de tablas sin procesar]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) o utilice este conjunto de [datos de eventos de muestra](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponibles en el mercado Snowflake para familiarizarse con los eventos compartidos.
{% endalert %}

## Gestión de eventos duplicados

Se esperan duplicados, pero todos los eventos tienen un identificador único, la columna ID. Los duplicados pueden eliminarse en `select distinct(id)`.

## Cambios de ruptura frente a cambios sin ruptura

### Cambios sin ruptura

Los cambios no rupturistas pueden producirse en cualquier momento y generalmente proporcionan funcionalidad adicional. Ejemplos de cambios sin ruptura:
- Añadir una nueva tabla o vista
- Añadir una columna a una tabla o vista existente

{% alert important %}
Dado que las columnas nuevas se consideran de no ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta en lugar de utilizar consultas de `SELECT *`. Otra posibilidad es crear vistas que nombren explícitamente las columnas y, a continuación, consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

### Cambios de última hora

Siempre que sea posible, los cambios de última hora irán precedidos de un anuncio y de un periodo de migración. Algunos ejemplos de cambios de última hora son:
- Eliminar una tabla o una vista
- Eliminar una columna de una tabla o vista existente
- Modificar el tipo o la anulabilidad de una columna existente

## Cumplimiento del Reglamento General de Protección de Datos (RGPD)

Casi todos los registros de eventos que almacena Braze incluyen algunos campos que representan información personal identificable (IPI) de los usuarios. Algunos eventos pueden incluir la dirección de correo electrónico, el número de teléfono, el identificador del dispositivo, el idioma, el sexo e información sobre la ubicación. Si se envía a Braze la solicitud de olvido de un usuario, anularemos esos campos de IIP para cualquier evento que pertenezca a esos usuarios. De este modo, no eliminamos el registro histórico del acontecimiento, pero ahora el acontecimiento nunca podrá vincularse a un individuo concreto.
