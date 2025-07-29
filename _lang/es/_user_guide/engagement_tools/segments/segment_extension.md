---
nav_title: Extensiones de segmento
article_title: Extensiones de segmento
page_order: 6
page_type: reference
description: "Este artículo le mostrará cómo configurar y utilizar una extensión de segmento para mejorar sus capacidades de segmentación."
tool: Segments
---

# Extensiones de segmento

> Las extensiones de segmento te permiten construir segmentos muy precisos a lo largo de un periodo prolongado del historial de un usuario. Por ejemplo, con las extensiones de segmento puedes dirigirte a usuarios que hayan comprado un producto concreto en los últimos dieciséis meses o que hayan gastado una determinada cantidad de dinero con tu servicio. Refina esta audiencia utilizando las propiedades del evento para que la segmentación sea aún más granular.

La segmentación Braze te permite dirigirte a los usuarios en función del evento personalizado o del comportamiento de compra. Las extensiones de segmento aumentan esta capacidad, permitiéndote recurrir a los datos históricos guardados en el perfil de usuario. Utilizando las extensiones de segmento, puedes identificar y llegar a los usuarios que han completado cualquier evento personalizado o evento de compra cualquier número de veces en los últimos dos años (730 días). 

## ¿Por qué utilizar extensiones de segmento?

Los segmentos Braze te ofrecen potentes herramientas de segmentación para crear grupos dinámicos de usuarios. Para la mayoría de los casos de uso, esto es suficiente para llegar a tu audiencia con eficacia. Las extensiones de segmento están diseñadas para casos de uso avanzado en los que necesitas analizar comportamientos de hasta dos años atrás o aplicar una lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Puedes utilizar consultas [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) o datos de tu propio [almacén de datos]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) para afinar aún más tu audiencia.

Por ejemplo, la segmentación predeterminada de Braze encontrará usuarios que se ajusten a los criterios específicos que definas, como identificar a un usuario que haya comprado recientemente uno de tus productos. Las extensiones de segmento te permiten profundizar más, como identificar a los usuarios que compraron un color concreto de un producto específico al menos dos veces hace entre 18 y 24 meses. Las extensiones de segmento son una mejora, no un requisito. Si necesitas filtros más avanzados o una ventana retrospectiva más larga, son una gran herramienta para ayudarte mientras mantienes optimizado tu uso de datos.

{% alert note %}
Existe una asignación por defecto de 25 Extensiones de Segmento activas por área de trabajo en un momento determinado. Si necesita aumentar este límite, póngase en contacto con su gestor de éxito de clientes de Braze para analizar su caso de uso.
{% endalert %}

## Crear una extensión de segmento

Para crear una extensión de segmento, crearás un filtro para refinar un segmento de tus usuarios basándote en las propiedades del evento personalizado. Al crear una Extensión de segmento, elegirás si el segmento será estático o se actualizará dinámicamente a un intervalo establecido.

### Paso 1: Vaya a Extensiones de segmento

Vaya a **Audiencia** > **Extensiones de segmento**.

En la tabla Extensiones de segmento, selecciona **Crear nueva extensión** y, a continuación, selecciona tu experiencia de creación de extensiones de segmento:

- **Extensión sencilla:** Crear la extensión de segmento enfocada en un solo evento usando un formulario guiado.
Lo mejor para cuando no se quiere utilizar SQL.
- **Empieza con una plantilla:** Crea un segmento SQL con una plantilla personalizable usando datos de Snowflake.
- **Actualización incremental:** Escribe un segmento SQL de Snowflake que automáticamente actualice los últimos 2 días de datos, o puedes actualizar manualmente en caso de ser necesario. Esta es la mejor opción para equilibrar precisión y eficiencia de costos.
- **Actualización completa:** Escribe un segmento SQL de Snowflake que recalcule toda la audiencia después de actualizar manualmente. La mejor opción cuando necesitas una actualización total de la vista de tu audiencia.



Si seleccionas una experiencia que utiliza SQL, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para más información.

Si selecciona la **extensión Simple**, continúe con los pasos siguientes.

### Paso 2: Nombre de su extensión de segmento

Nombre su Extensión de Segmento describiendo el tipo de usuarios que pretende filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en su segmento.



### Paso 3: Elija sus criterios

Seleccione entre criterios de compra, participación en mensajes o eventos personalizados para la segmentación. Una vez que haya seleccionado los criterios de tipo de evento deseados, elija el artículo comprado, la interacción de mensaje o el evento personalizado específico al que desea dirigir su lista de usuarios. A continuación, elija cuántas veces (más, menos o igual) el usuario tendría que haber completado el evento, y el período de tiempo-para las Extensiones de Segmento específicamente, puede retroceder hasta los últimos 730 días (2 años).

La segmentación basada en datos de eventos de más de 730 días puede realizarse utilizando otros filtros situados en **Segmentos**. 



#### Segmentación de propiedades de eventos

Para aumentar la precisión de la orientación, seleccione la casilla **Añadir filtros de propiedades**. Esto le permitirá desglosar en función de las propiedades específicas de su compra o evento personalizado. Admitimos la segmentación de propiedades del evento basada en objetos de cadena, numéricos, booleanos y temporales.

Para las propiedades de cadena, puede introducir varios valores a la vez. En el ejemplo siguiente, este filtro busca usuarios con un estado igual a cualquiera de los siguientes: oro, plata o bronce.









También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).



Las extensiones de segmento se basan en el almacenamiento a largo plazo de las propiedades de los eventos y no tienen un límite de almacenamiento de propiedades con marca de tiempo. Puede echar un vistazo a las propiedades de eventos rastreadas en los últimos dos años. El uso de propiedades de eventos dentro de las Extensiones de Segmento no afecta al uso de puntos de datos.

{% alert note %}
No necesitas extensiones de segmento para utilizar propiedades de eventos o atributos personalizados anidados en tu segmento. Las extensiones de segmento sólo amplían la ventana histórica utilizada para crear un segmento. Puedes crear un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) en tiempo real que utilice propiedades de eventos de los últimos 30 días o que utilice atributos personalizados anidados. Del mismo modo, puedes [programar tu mensaje]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para que se desencadene en tiempo real en función de una propiedad del evento, sin necesidad de extensión de segmento.
{% endalert %}

### Paso 4: Designar configuración de actualización (opcional)



### Paso 5: Guarda tu extensión de segmento

 El tiempo que se tarda en generar la extensión depende del número de usuarios que tengas, de cuántos eventos personalizados o de compra estés capturando y de cuántos días estés mirando hacia atrás en el historial.

Mientras su extensión se está procesando, verá una pequeña animación junto al nombre de la extensión, y la palabra "Procesando" en la columna **Último Procesado** de la lista de extensiones. Tenga en cuenta que no podrá editar una extensión mientras se esté procesando.



   

### Paso 6: Utilice su extensión en un segmento

 Para empezar, seleccione **Extensión de segmento Braze** en la lista de filtros de la sección **Atributos de usuario**.



En la lista de filtros Extensión de segmento Braze, elija la extensión que desea incluir o excluir en este segmento.









## Preguntas más frecuentes

### ¿Puedo crear una extensión de segmento que utilice varios eventos personalizados?

Sí. Puedes añadir varios eventos o hacer referencia a varias tablas Snowflake cuando utilices [las extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Al utilizar **la extensión Simple** Extensiones de segmento, puedes seleccionar un evento personalizado, un evento de compra o una interacción de canal. Sin embargo, puedes combinar varias extensiones de segmento con un Y u O al crear el segmento.

### ¿Puedo archivar extensiones de segmento si existen en una campaña activa?

No. Antes de archivar una extensión de segmento, tienes que eliminarla de toda la mensajería activa.

### 

Sí.   

 

### 

  



