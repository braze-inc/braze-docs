---
nav_title: Creación de un mensaje LINE
article_title: Creación de un mensaje LINE
page_order: 1
description: "Este artículo explica cómo crear una campaña de mensajes LINE o Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Creación de un mensaje LINE

> Las campañas de LINE pueden llegar directamente a sus clientes y chatear con ellos de forma programática. Puede utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con sus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con su marca.

## Requisitos previos

Antes de crear un mensaje LINE, haga lo siguiente:

1. Lea el resumen de LINE.
2. Reconoce las políticas, los límites y las normas de contenido.
3. [Configura tu conexión LINE]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

Al enviar mensajes de LINE desde Braze, se utilizarán los créditos de mensajes de tu cuenta.

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaña %}

**Pasos:**

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Seleccione **LÍNEA** o, para campañas dirigidas a varios canales, seleccione **Campaña multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añada [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que haya configurado su lienzo, añada un paso en el constructor de lienzos. Nombra tu paso con algo claro y significativo.
3. Elija un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifique un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puede afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elija cualquier otro canal de mensajería que desee asociar a su mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Redacta tu mensaje LINE

Escribe tu mensaje utilizando la personalización (como Liquid o Contenido conectado) según sea necesario. LINE permite hasta cinco burbujas de mensaje en cada mensaje, que pueden ser de cualquiera de los diseños de mensajes disponibles: texto, imagen, enriquecido o basado en tarjetas.

![Compositor de LINE con un mensaje mostrado en la vista previa.]({% image_buster /assets/img/line/line_composer.png %})

### Consejos

#### Utilizar Liquid

Si piensa utilizar Liquid, asegúrese de incluir un valor por defecto para su personalización. Esto evitará que los destinatarios con perfiles de usuario incompletos reciban un marcador de posición en blanco. Por ejemplo, en lugar de que un usuario reciba el mensaje "¡Hola, !", podría recibir el mensaje "¡Hola, nuevo abonado!".

#### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 3: Vista previa y prueba de tu mensaje

Cambia a la pestaña **Prueba** para enviar un mensaje LINE de prueba a grupos de prueba de contenido o a usuarios individuales, o previsualiza el mensaje como usuario directamente en Braze.

![La pestaña "Pruebas" muestra una vista previa de un mensaje de prueba.]({% image_buster /assets/img/line/test_preview.png %})

## Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaña %}

Construye el resto de tu campaña. Consulte las secciones siguientes para obtener más información sobre la mejor manera de utilizar nuestras herramientas para crear mensajes LINE.

### Elige la programación o desencadenante de la entrega

Los mensajes de LINE pueden enviarse en función de una hora programada, una acción o un activador de la API. Para obtener más información sobre las opciones de programación y activación, consulte [Programación de la campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Puede especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Para la entrega basada en acciones, también puedes configurar la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

### Elige los usuarios a los que dirigirte

[Dirígete a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para acotar tu audiencia. Ya deberías haber elegido el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que desean tener contigo. 

Selecciona la audiencia más amplia de tus segmentos y, opcionalmente, acota aún más ese segmento con nuestros [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Automáticamente obtendrá una instantánea de cómo es la población de ese segmento aproximado en este momento. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión le ayudan a medir el éxito de su campaña. Por ejemplo:

- Si utiliza geotargeting para activar un mensaje de LÍNEA cuyo objetivo final es que el usuario realice una compra, establezca el evento de conversión en `Purchase`.
- Si estás intentando llevar al usuario a tu aplicación, establece el evento de conversión en `Starts Session`.

También puede establecer eventos de conversión personalizados basados en su caso de uso específico. Sea creativo y piense cómo quiere medir el éxito de esta campaña.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu Canvas. Para obtener más información sobre cómo crear el resto del lienzo, utilizar las pruebas multivariantes y la selección inteligente, etc., consulte [Creación de un lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Paso 5: Revisar y desplegar

Cuando hayas terminado de crear lo último de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, echa un vistazo a [los informes de LINE]({{site.baseurl}}/line/reporting/) para saber cómo puedes acceder a los resultados de tus campañas LINE.


