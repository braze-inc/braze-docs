---
nav_title: Crear un mensaje LINE
article_title: Crear un mensaje LINE
page_order: 1
description: "Este artículo explica cómo crear una campaña de mensajería LINE o Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Crear un mensaje LINE

> Las campañas de LINE pueden llegar directamente a tus clientes y chatear programáticamente con ellos. Puedes utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con tus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con tu marca.

## Requisitos previos

Antes de crear un mensaje LINE, haz lo siguiente:

1. Lee el resumen de LINE.
2. Reconoce las políticas, los límites y las normas de contenido.
3. [Configura tu conexión LINE]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

Al enviar mensajes de LINE desde Braze, se utilizarán los créditos de mensajes de tu cuenta.

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **LÍNEA** o, para campañas dirigidas a varios canales, selecciona **Campaña multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Elige un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Redacta tu mensaje LINE

Escribe tu mensaje utilizando la personalización (como Liquid o Contenido conectado) según sea necesario. LINE permite hasta cinco burbujas de mensaje en cada mensaje, que pueden ser de cualquiera de los diseños de mensajes disponibles: texto, imagen, enriquecido o basado en tarjetas.

\![LÍNEA compositora con un mensaje mostrado en la vista previa.]({% image_buster /assets/img/line/line_composer.png %})

### Consejos

#### Utilizar Liquid

Si piensas utilizar Liquid, asegúrate de incluir un valor predeterminado para tu personalización. Esto evitará que los destinatarios con perfiles de usuario incompletos reciban un marcador de posición en blanco. Por ejemplo, en lugar de que un usuario reciba el mensaje "¡Hola, !", podría recibir el mensaje "¡Hola, nuevo suscriptor!".

#### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 3: Vista previa y prueba de tu mensaje

Cambia a la pestaña de **Prueba** para enviar un mensaje LINE de prueba a grupos de prueba de contenido o a usuarios individuales, o ve previa del mensaje como usuario directamente en Braze.

La pestaña "Pruebas" muestra una vista previa de un mensaje de prueba.]({% image_buster /assets/img/line/test_preview.png %})

## Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña. Consulta las secciones siguientes para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear mensajes LINE.

### Elige el calendario o desencadenar la entrega

Los mensajes de LINE se pueden entregar en función de una hora programada, una acción o un desencadenante de la API. Para más información sobre las opciones de desencadenar y programar, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Puedes especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña, o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las horas tranquilas.

### Elige los usuarios a los que dirigirte

[Dirígete a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Ya deberías haber elegido el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que desean tener contigo. 

Selecciona la audiencia más amplia de tus segmentos y, opcionalmente, acota aún más ese segmento con nuestros [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Automáticamente recibirás una instantánea de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:

- Si utilizas geotargeting para desencadenar un mensaje LINE cuyo objetivo final es que el usuario realice una compra, configura el evento de conversión en `Purchase`.
- Si intentas llevar al usuario a tu aplicación, configura el evento de conversión en `Starts Session`.

También puedes establecer eventos de conversión personalizados basados en tu caso de uso específico. Sé creativo y piensa cómo quieres medir el éxito de esta campaña.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, utilizar pruebas multivariantes e Intelligent Selection, y mucho más, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Paso 5: Revisar y desplegar

Cuando hayas terminado de construir la última parte de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, consulta [los informes de LINE]({{site.baseurl}}/line/reporting/) para saber cómo puedes acceder a los resultados de tus campañas en LINE.


