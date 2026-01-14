---
nav_title: Crear un mensaje SMS
article_title: Crear un mensaje SMS
page_order: 5
description: "Este artículo de referencia cubre los pasos necesarios para elaborar y crear un mensaje SMS."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Crear un mensaje SMS

> Las campañas de SMS son estupendas para llegar directamente a tus clientes y conversar con ellos de forma programática. Puedes utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con tus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con tu marca. 

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **SMS** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) para asegurarte de que envías tu mensaje a los usuarios adecuados. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos reciban la campaña. Sólo se utilizarán los códigos largos y los códigos abreviados que pertenezcan a ese grupo de suscripción para enviar SMS a los usuarios objetivo.

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

## Paso 2: Redacta tu mensaje SMS

Escribe tu mensaje utilizando los idiomas y la personalización (Liquid, contenido conectado y emojis) que necesites. Asegúrate de respetar nuestros límites de copia de mensajes para reducir las posibilidades de que te cobren cargos por excedente.

{% alert important %}
Antes de continuar, lee nuestras directrices sobre los [segmentos del mensaje SMS y los límites de copia]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). Los segmentos del mensaje SMS son los lotes de caracteres que los operadores telefónicos utilizan para medir los mensajes de texto. Los mensajes se cobran por segmento del mensaje, por lo que conviene entender los matices de cómo se dividirán los mensajes.
{% endalert %}

¡\![Compositor de SMS en Braze con el mensaje "¡Hola first_name, agradecemos tu apoyo! ¿Por qué no te pasas por una de nuestras tiendas y les enseñas este SMS para obtener un descuento exclusivo? Responde STOP para dejar de recibir mensajes nuestros".]({% image_buster /assets/img/sms_campaign_compose.png %})

### Añadir una tarjeta de contacto

Puedes añadir una tarjeta de contacto a tu mensaje SMS para que a tus clientes les resulte más fácil añadir tu empresa e información de contacto a sus contactos. Puedes asignar propiedades comunes a estas tarjetas, como el nombre de tu empresa, el número de teléfono, la dirección, el correo electrónico y una pequeña foto. Consulta [las tarjetas de contacto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) para saber más.

### Consejos

#### Utilizar Liquid

{% raw %}
Si piensas utilizar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, en caso de que el perfil de usuario del destinatario esté incompleto, no reciba un marcador de posición en blanco `Hi, !`, en lugar de su nombre o una frase coherente.
{% endraw %}

#### Generar copia de IA

¿Necesitas ayuda para crear un texto impresionante? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

\![Iniciar el botón AI Copywriter, situado en el campo Mensaje del compositor de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 3: Vista previa y prueba de tu mensaje

Braze recomienda siempre previsualizar y probar tu mensaje antes de enviarlo. Cambia a la pestaña de **Prueba** para enviar un SMS de prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, o para obtener una vista previa del mensaje como usuario directamente en Braze.

\![Vista previa de la copia del SMS desde la pestaña Prueba del compositor. En la sección de perfil, el campo Nombre está configurado como "James". En la vista previa, el SMS ahora dice "Hola James, ¡agradecemos tu apoyo!".]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Si quieres probar en cuántos segmentos puede dividirse tu SMS, comprueba la longitud de tu texto con nuestra [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu campaña. Consulta las secciones siguientes para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear mensajes SMS.

#### Elige el calendario o desencadenar la entrega

Los mensajes SMS pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las horas tranquilas.

En este paso también puedes especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Ya deberías haber elegido el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que desean tener contigo. 

{% multi_lang_include target_audiences.md %}

En este paso, seleccionarás la audiencia más amplia de tus segmentos, y reducirás aún más ese segmento con nuestros filtros, si así lo deseas. Automáticamente recibirás una vista previa de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% alert tip %}
¿Te interesa el SMS reorientado? Visita nuestro [artículo sobre reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) por SMS para saber más.
{% endalert %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:

- Si utilizas la geolocalización para desencadenar un mensaje SMS cuyo objetivo final es que el usuario realice una compra, configura el evento de conversión en `Purchase`.
- Si intentas llevar al usuario a tu aplicación, configura el evento de conversión en `Starts Session`.

También puedes establecer eventos de conversión personalizados basados en tu caso de uso específico. Sé creativo y piensa cómo quieres medir realmente el éxito de esta campaña.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

## Paso 5: Revisar y desplegar

Cuando hayas terminado de construir la última parte de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, consulta [los informes SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber cómo puedes acceder a los resultados de tus campañas SMS.
