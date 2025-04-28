---
nav_title: Extensiones de segmento
article_title: Extensiones de segmento
page_order: 3.1

page_type: tutorial
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

{% alert note %}
Si está utilizando la [navegación antigua]({{site.baseurl}}/navigation), puede encontrar esta página en **Compromiso** > **Segmentos** > **Extensiones de segmento**.
{% endalert %}

En la tabla Extensiones de segmento, selecciona **Crear nueva extensión** y, a continuación, selecciona tu experiencia de creación de extensiones de segmento:

- **Extensión sencilla:** Crear la extensión de segmento enfocada en un solo evento usando un formulario guiado.
Lo mejor para cuando no se quiere utilizar SQL.
- **Empieza con una plantilla:** Crea un segmento SQL con una plantilla personalizable usando datos de Snowflake.
- **Actualización incremental:** Escribe un segmento SQL de Snowflake que automáticamente actualice los últimos 2 días de datos, o puedes actualizar manualmente en caso de ser necesario. Esta es la mejor opción para equilibrar precisión y eficiencia de costos.
- **Actualización completa:** Escribe un segmento SQL de Snowflake que recalcule toda la audiencia después de actualizar manualmente. La mejor opción cuando necesitas una actualización total de la vista de tu audiencia.

![""][20]{: style="max-width:50%"}

Si seleccionas una experiencia que utiliza SQL, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para más información.

Si selecciona la **extensión Simple**, continúe con los pasos siguientes.

### Paso 2: Nombre de su extensión de segmento

Nombre su Extensión de Segmento describiendo el tipo de usuarios que pretende filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en su segmento.

![Extensión de segmento denominada "Extensión Compradores Online - 90 Días" con la casilla "Regenerar extensión diariamente" seleccionada.][2]

### Paso 3: Elija sus criterios

Seleccione entre criterios de compra, participación en mensajes o eventos personalizados para la segmentación. Una vez que haya seleccionado los criterios de tipo de evento deseados, elija el artículo comprado, la interacción de mensaje o el evento personalizado específico al que desea dirigir su lista de usuarios. A continuación, elija cuántas veces (más, menos o igual) el usuario tendría que haber completado el evento, y el período de tiempo-para las Extensiones de Segmento específicamente, puede retroceder hasta los últimos 730 días (2 años).

La segmentación basada en datos de eventos de más de 730 días puede realizarse utilizando otros filtros situados en **Segmentos**. Al elegir el periodo de tiempo, puede especificar un intervalo de fechas relativo (por ejemplo, los últimos X días), una fecha de inicio, una fecha final o un intervalo de fechas exacto (de la fecha A a la fecha B).

![""][3]

#### Segmentación de propiedades de eventos

Para aumentar la precisión de la orientación, seleccione la casilla **Añadir filtros de propiedades**. Esto le permitirá desglosar en función de las propiedades específicas de su compra o evento personalizado. Admitimos la segmentación de propiedades del evento basada en objetos de cadena, numéricos, booleanos y temporales.

Para las propiedades de cadena, puede introducir varios valores a la vez. En el ejemplo siguiente, este filtro busca usuarios con un estado igual a cualquiera de los siguientes: oro, plata o bronce.

![Segmentación basada en las propiedades de las cadenas.][13.5]

![Segmentación basada en propiedades numéricas.][13]

![Segmentación basada en propiedades booleanas.][14]

![Segmentación basada en objetos de fecha y hora.][15]

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentación basada en propiedades de eventos anidados.][18]

Las extensiones de segmento se basan en el almacenamiento a largo plazo de las propiedades de los eventos y no tienen un límite de almacenamiento de propiedades con marca de tiempo. Puede echar un vistazo a las propiedades de eventos rastreadas en los últimos dos años. El uso de propiedades de eventos dentro de las Extensiones de Segmento no afecta al uso de puntos de datos.

{% alert note %}
No necesitas extensiones de segmento para utilizar propiedades de eventos o atributos personalizados anidados en tu segmento. Las extensiones de segmento sólo amplían la ventana histórica utilizada para crear un segmento. Puedes crear un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) en tiempo real que utilice propiedades de eventos de los últimos 30 días o que utilice atributos personalizados anidados. Del mismo modo, puedes [programar tu mensaje]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para que se desencadene en tiempo real en función de una propiedad del evento, sin necesidad de extensión de segmento.
{% endalert %}

### Paso 4: Designar configuración de actualización (opcional)

Si no necesitas que tu extensión se actualice de forma periódica, puedes guardarla sin utilizar la configuración de actualización, y Braze generará por defecto tu Extensión de segmento basándose en tu número de usuarios en ese momento. Utiliza el comportamiento predeterminado si sólo quieres generar la audiencia una vez y luego dirigirte a ella con una campaña puntual.

Tu segmento siempre empezará a procesarse después del guardado inicial. Cada vez que se actualice tu segmento, Braze volverá a ejecutar el segmento y actualizará la pertenencia al mismo para reflejar los usuarios de tu segmento en el momento de la actualización. Esto puede ayudar a que tus campañas recurrentes lleguen a los usuarios más relevantes.

#### Configurar una actualización periódica

Para establecer una programación recurrente, selecciona **Actualizar configuración** en la esquina superior derecha de tu extensión específica. La opción de designar la configuración de actualización está disponible para todos los tipos de extensiones de segmento, incluidos los segmentos SQL, los segmentos CDI y las extensiones de segmento simples basadas en formularios.

{% alert important %}
Para optimizar tu gestión de datos, la configuración de actualización se desactiva automáticamente para las extensiones de segmento no utilizadas. Las extensiones de segmento se consideran no utilizadas cuando lo están:

- No se utiliza en ninguna campaña, lienzo o segmento activo o inactivo (borrador, detenido, archivado).
- No tuvo modificaciones en los últimos 7 días

Braze notificará al contacto de la empresa y al creador de la extensión si se desactiva esta configuración. La opción de regenerar las extensiones diariamente puede volver a activarse en cualquier momento.
{% endalert %}

#### Seleccionar tu configuración de actualización

![Configuración del intervalo de actualización con una frecuencia de actualización semanal, hora de inicio a las 10 de la mañana y lunes seleccionado como día.][21]{: style="max-width:60%;"}

En el panel **Configuración de actualización**, puedes seleccionar la frecuencia con la que se actualizará esta extensión de segmento: cada hora, cada día, cada semana o cada mes. También se te pedirá que selecciones la hora concreta (que esté en la zona horaria de tu empresa) a la que se produciría la actualización, por ejemplo:

- Si tienes una campaña de correo electrónico que se envía todos los lunes a las 11 de la mañana, hora de la empresa, y quieres asegurarte de que tu segmento se actualiza justo antes de enviarlo, debes elegir un programa de actualización semanal a las 10 de la mañana de los lunes.
- Si quieres que tu segmento se actualice todos los días, selecciona la frecuencia de actualización diaria y, a continuación, elige la hora del día en que se actualizará.

{% alert note %}
La posibilidad de establecer un programa de actualización por horas no está disponible para las extensiones de segmento basadas en formularios (pero puedes establecer programas diarios, semanales o mensuales).
{% endalert %}

#### Consumo de créditos y costes adicionales

Como las actualizaciones vuelven a ejecutar la consulta de tu segmento, cada actualización para segmentos SQL consumirá créditos de segmentos SQL, y cada actualización para segmentos CDI supondrá un coste dentro de tu almacén de datos de terceros.

{% alert note %}
La actualización de los segmentos podría requerir hasta 60 minutos debido a los tiempos de procesamiento de los datos. Los segmentos que estén actualmente en proceso de actualización tendrán un estado de "Procesando" dentro de tu lista de Extensiones de segmento. Esto tiene un par de implicaciones:

- Para terminar de procesar tu segmento antes de una hora determinada, elige una hora de actualización que sea 60 minutos antes. 
- Sólo puede producirse una actualización a la vez para una extensión de segmento específica. Si hay un conflicto en el que se inicia una nueva actualización cuando una actualización existente ya ha comenzado a procesarse, Braze cancelará la nueva solicitud de actualización y continuará el procesamiento en curso.
{% endalert %}

### Paso 5: Guarda tu extensión de segmento

Una vez que selecciones **Guardar**, tu extensión comenzará a procesarse. El tiempo que se tarda en generar la extensión depende del número de usuarios que tengas, de cuántos eventos personalizados o de compra estés capturando y de cuántos días estés mirando hacia atrás en el historial.

Mientras su extensión se está procesando, verá una pequeña animación junto al nombre de la extensión, y la palabra "Procesando" en la columna **Último Procesado** de la lista de extensiones. Tenga en cuenta que no podrá editar una extensión mientras se esté procesando.

![""][5]

### Paso 6: Utilice su extensión en un segmento

Una vez creada una extensión, puede utilizarla como filtro al crear un segmento o definir un público para una campaña o Canvas. Para empezar, seleccione **Extensión de segmento Braze** en la lista de filtros de la sección **Atributos de usuario**.

![""][6]

En la lista de filtros Extensión de segmento Braze, elija la extensión que desea incluir o excluir en este segmento.

![""][7]

Para ver los criterios de la extensión, selecciona **Ver detalles de la extensión** para mostrar los detalles en una ventana emergente modal.

![""][8]{: style="max-width:70%;"}

Ahora puedes proceder como de costumbre con [la creación de tu segmento][11].

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13,5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
