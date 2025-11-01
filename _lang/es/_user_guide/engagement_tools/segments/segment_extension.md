---
nav_title: Extensiones de segmento
article_title: Extensiones de segmento
page_order: 6
page_type: reference
description: "Este artículo te mostrará cómo configurar y utilizar una extensión de segmento para mejorar tus capacidades de segmentación."
tool: Segments
---

# Extensiones de segmento

> Las extensiones de segmento te permiten construir segmentos muy precisos a lo largo de un periodo prolongado del historial de un usuario. Por ejemplo, con las extensiones de segmento puedes dirigirte a usuarios que hayan comprado un producto concreto en los últimos dieciséis meses o que hayan gastado una determinada cantidad de dinero con tu servicio. Refina esta audiencia utilizando las propiedades del evento para que la segmentación sea aún más granular.

La segmentación Braze te permite dirigirte a los usuarios en función del evento personalizado o del comportamiento de compra. Las extensiones de segmento aumentan esta capacidad, permitiéndote recurrir a los datos históricos guardados en el perfil de usuario. Utilizando las extensiones de segmento, puedes identificar y llegar a los usuarios que hayan completado cualquier evento personalizado o evento de compra cualquier número de veces en los últimos dos años (730 días). 

## ¿Por qué utilizar extensiones de segmento?

Los segmentos Braze te ofrecen potentes herramientas de segmentación para crear grupos dinámicos de usuarios. Para la mayoría de los casos de uso, esto es suficiente para llegar a tu audiencia con eficacia. Las extensiones de segmento están diseñadas para casos de uso avanzado en los que necesitas analizar comportamientos de hasta dos años atrás o aplicar una lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Puedes utilizar consultas [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) (extensiones de segmento SQL) o datos de tu propio [almacén de datos]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) para refinar aún más tu audiencia.

Por ejemplo, la segmentación predeterminada de Braze encontrará usuarios que se ajusten a los criterios específicos que definas, como identificar a un usuario que haya comprado recientemente uno de tus productos. Las extensiones de segmento te permiten profundizar más, como identificar a los usuarios que compraron un color concreto de un producto específico al menos dos veces hace entre 18 y 24 meses. Las extensiones de segmento son una mejora, no un requisito. Si necesitas filtros más avanzados o una ventana retrospectiva más larga, son una gran herramienta para ayudarte mientras mantienes optimizado tu uso de datos.

{% alert note %}
Hay una asignación predeterminada de 25 extensiones de segmento activas por espacio de trabajo en un momento determinado. Si necesitas aumentar este límite, ponte en contacto con tu administrador del éxito del cliente de Braze para comentar tu caso de uso.
{% endalert %}

## Crear una extensión de segmento

Para crear una extensión de segmento, crearás un filtro para refinar un segmento de tus usuarios basándote en las propiedades del evento personalizado. Al crear una Extensión de segmento, elegirás si el segmento será estático o se actualizará dinámicamente a un intervalo establecido.

### Paso 1: Navegar a Extensiones de segmento

Ve a **Audiencia** > **Extensiones** de segmento **.**

En la tabla Extensiones de segmento, selecciona **Crear nueva extensión** y, a continuación, selecciona tu experiencia de creación de extensiones de segmento:

- **Ampliación sencilla:** Crea una Extensión de Segmento centrada en un único evento utilizando un formulario guiado.
Lo mejor para cuando no quieras utilizar SQL.
- **Empieza con una plantilla:** Crea un segmento SQL con una plantilla personalizable utilizando los datos de Snowflake.
- **Actualización incremental:** Escribe un segmento SQL Snowflake que actualice automáticamente los datos de los 2 últimos días o actualízalos manualmente cuando sea necesario. Lo mejor para equilibrar precisión y rentabilidad.
- **Refresco completo:** Escribe un segmento SQL con datos Snowflake o cualquier [origen de datos conectado a CDI]({{site.baseurl}}/cdi_segment_extensions/) que recalcule toda la audiencia al actualizar manualmente. Lo mejor para cuando necesitas una visión completa y actualizada de tu audiencia.

\![Tabla con diferentes experiencias de creación de extensiones de segmento para seleccionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si seleccionas una experiencia que utiliza SQL, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para obtener más información. Si seleccionas **Extensión simple**, continúa con el paso 2.

#### Uso de créditos SQL

Los siguientes tipos de extensiones de segmento consumen créditos SQL:

- Extensiones de segmento SQL (tanto actualización incremental como completa)
- Segmentos del catálogo
- Segmentos CDI 
    - Los créditos se consumen en tu propio almacén de datos

### Paso 2: Nombra tu extensión de segmento

Nombra tu extensión de segmento describiendo el tipo de usuarios por los que pretendes filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en tu segmento.

\![Extensión de segmento denominada "Extensión para compradores online - 90 días".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Paso 3: Elige tus criterios

Selecciona entre criterios de compra, interacción con mensajes o eventos personalizados para la segmentación. Después de seleccionar los criterios de tipo de evento deseados, elige el artículo comprado, la interacción de mensaje o el evento personalizado específico al que te gustaría dirigirte para tu lista de usuarios. A continuación, elige cuántas veces (más, menos o igual) tendría que haber completado el usuario el evento, y el periodo de tiempo: en el caso concreto de las extensiones de segmento, puedes retroceder hasta los últimos 730 días (2 años).

La segmentación basada en datos de eventos de más de 730 días puede hacerse utilizando otros filtros situados en **Segmentos**. Cuando elijas tu periodo de tiempo, puedes especificar un intervalo de fechas relativo para seleccionar el último X número de días, una fecha de inicio, una fecha final o un intervalo de fechas exacto (fecha A a fecha B).

\![Criterios de segmentación para usuarios que realizaron un evento personalizado más de 2 veces en el intervalo de fechas del 1 de marzo de 2025 al 31 de marzo de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentación de propiedades del evento

Para aumentar la precisión de los objetivos, selecciona la casilla **Añadir filtros de propiedad**. Esto te habilitará para desglosar en función de las propiedades específicas de tu compra o evento personalizado. Admitimos la segmentación de propiedades del evento basada en objetos de cadena, numéricos, booleanos y temporales.

Para las propiedades de cadena, puedes introducir varios valores a la vez. En el ejemplo siguiente, este filtro busca usuarios con un estado igual a cualquiera de los siguientes: oro, plata o bronce.

Segmentación basada en las propiedades de las cadenas.]({% image_buster /assets/img/segment/property5.png %})

Segmentación basada en propiedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

Segmentación basada en propiedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

\![Segmentación basada en objetos fecha-hora.]({% image_buster /assets/img/segment/property4.png %})

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Segmentación basada en propiedades de eventos anidados.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Las extensiones de segmento se basan en el almacenamiento a largo plazo de las propiedades del evento y no tienen un límite de almacenamiento de propiedades con marca de tiempo. Puedes consultar las propiedades del evento que han sido objeto de seguimiento en los dos últimos años. El uso de propiedades del evento dentro de las extensiones de segmento no afecta al uso de punto de datos.

{% alert note %}
No necesitas extensiones de segmento para utilizar propiedades de eventos o atributos personalizados anidados en tu segmento. Las extensiones de segmento sólo amplían la ventana histórica utilizada para crear un segmento predeterminado. Puedes crear un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) predeterminado en tiempo real que utilice propiedades de eventos de los últimos 30 días o que utilice atributos personalizados anidados. Del mismo modo, puedes [programar tu mensaje]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para que se desencadene en tiempo real en función de una propiedad del evento, sin necesidad de extensión de segmento.
{% endalert %}

### Paso 4: Designar configuración de actualización (opcional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Paso 5: Guarda tu extensión de segmento

Después de seleccionar **Guardar**, tu Extensión de segmento comenzará a procesarse. El tiempo que se tarda en generar tu extensión de segmento depende del número de usuarios que tengas, de cuántos eventos personalizados o eventos de compra estés capturando y de cuántos días estés mirando atrás en el historial.

Mientras tu Extensión de segmento se está procesando, verás una pequeña animación junto al nombre de la Extensión de segmento, y la palabra "Procesando" en la columna **Último procesado** de la lista de Extensiones de segmento. Ten en cuenta que no podrás editar una Extensión de segmento mientras se esté procesando.

\!["Extensiones de segmento" página con dos extensiones activas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Cuando se esté procesando una Extensión de segmento, Braze seguirá utilizando el historial de versiones del segmento predeterminado de antes de que comenzara el procesamiento a efectos de segmentación de la audiencia. El procesamiento tiene lugar cada vez que se guarda o actualiza, e implica la consulta y actualización de los perfiles de usuario; en otras palabras, la pertenencia a tu segmento predeterminado no se actualiza instantáneamente. Esto significa que, a menos que la acción de un usuario se realice antes de que la actualización comience a procesarse, no podemos garantizar que el usuario se incluya en la extensión de segmento una vez que se complete esa actualización concreta. Por el contrario, los usuarios que estaban en la extensión de segmento antes de la actualización y que ya no cumplan los criterios seguirán coincidiendo con tu segmento de sordos hasta que se complete el proceso de actualización y se apliquen las actualizaciones.

### Paso 6: Utiliza tu extensión en un segmento

Después de crear una Extensión de segmento, puedes utilizarla como filtro al crear un segmento o definir una audiencia para una campaña o Canvas. Empieza por elegir **Extensión de segmento Braze** en la lista de filtros de la sección **Atributos de usuario**.

\!["Filtros" sección con un filtro desplegable que muestra "Extensiones de segmento Braze".]({% image_buster /assets/img/segment/segment_extension7.png %})

En la lista de filtros de Extensiones de Segmento Braze, elige la Extensión de Segmento que deseas incluir o excluir en este segmento.

\![Un filtro "Extensiones de segmento Braze" que incluye un segmento "1 clic de correo electrónico en los últimos 56 días".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para ver los criterios de extensión de segmento, selecciona **Ver detalles de extensión** para mostrar los detalles en una nueva ventana.

Extensión para "1 clic de correo electrónico en los últimos 56 días".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Ahora puedes proceder como de costumbre a [crear tu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Preguntas más frecuentes

### ¿Puedo crear una extensión de segmento que utilice varios eventos personalizados?

Sí. Puedes añadir varios eventos o hacer referencia a varias tablas Snowflake cuando utilices [las extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

Al utilizar **la extensión Simple** Extensiones de segmento, puedes seleccionar un evento personalizado, un evento de compra o una interacción de canal. Sin embargo, puedes combinar varias extensiones de segmento con un Y u O al crear el segmento predeterminado.

### ¿Puedo archivar extensiones de segmento si existen en una campaña activa?

No. Antes de archivar una extensión de segmento, tienes que eliminarla de toda la mensajería activa.

### ¿Puedo utilizar matrices en las extensiones de segmento?

Sí. Para utilizar matrices, añade corchetes (`[]`) al nombre de tu propiedad. Si tu propiedad es `location_code`, introducirías `location_code[]`. 

Braze utiliza `[]` para recorrer matrices y comprobar si algún elemento de la matriz recorrida coincide con la propiedad del evento. Por ejemplo, podrías crear una Extensión de segmento de usuarios que coincidan al menos con un valor de una propiedad de la matriz.

### ¿Cómo calcula Braze el periodo de tiempo para un periodo de tiempo relativo de "últimos __ días"?

Cuando las extensiones de segmento calculan el periodo de tiempo relativo ("últimos X días"), la hora de inicio se establece en medianoche UTC. Por ejemplo, para una Extensión de segmento que se actualiza a las 2024-09-16 21:00 UTC y especifica 10 días, la hora de inicio se establece en 2024-09-06 00:00 UTC, no en 2024-09-06 21:00 UTC. 

Sin embargo, puedes especificar las zonas horarias utilizando segmentos SQL para identificar a los usuarios que realizaron el evento personalizado hace 10 días basándote en la medianoche de la hora de la empresa, o a los usuarios que realizaron el evento hace 10 días basándose en la hora actual.

