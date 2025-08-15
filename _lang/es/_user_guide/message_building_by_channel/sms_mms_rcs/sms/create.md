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

> Las campañas de SMS son excelentes para llegar directamente a sus clientes y conversar con ellos de forma programática. Puede utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con sus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con su marca. 

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaña %}

**Pasos:**

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **SMS** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) para asegurarte de que envías tu mensaje a los usuarios adecuados. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos recibirán la campaña. Sólo los códigos largos y cortos que pertenezcan a ese grupo de suscripción se utilizarán para enviar SMS a los usuarios objetivo.

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

## Paso 2: Redacta tu mensaje SMS

Escribe tu mensaje utilizando los idiomas y la personalización (Liquid, Connected Content y emojis) que necesites. Asegúrate de respetar nuestros límites de copia de mensajes para reducir las posibilidades de que te cobren más de la cuenta.

{% alert important %}
Antes de continuar, lea nuestras directrices sobre [segmentos de mensajes SMS y límites de copia]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). Los segmentos de mensajes SMS son los lotes de caracteres que las compañías telefónicas utilizan para medir los mensajes de texto. Los mensajes se cobran por segmento de mensaje, por lo que conviene entender los matices de cómo se dividirán los mensajes.
{% endalert %}

![Compositor de SMS en Braze con el mensaje "Hola, first_name, ¡agradecemos tu apoyo! ¿Por qué no te pasas por una de nuestras tiendas y les enseñas este SMS para obtener un descuento exclusivo? Responda STOP para dejar de recibir mensajes nuestros".]({% image_buster /assets/img/sms_campaign_compose.png %})

### Añadir una tarjeta de contacto

Puedes añadir una tarjeta de contacto a tu mensaje SMS para que a tus clientes les resulte más fácil añadir tu empresa e información de contacto a sus contactos. Puede asignar propiedades comunes a estas tarjetas, como el nombre de su empresa, el número de teléfono, la dirección, el correo electrónico y una pequeña foto. Consulta [las tarjetas de contacto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) para saber más.

### Consejos

#### Utilizar Liquid

{% raw %}
Si piensa utilizar Liquid, asegúrese de incluir un valor predeterminado para la personalización elegida, de modo que, en caso de que el perfil de usuario del destinatario esté incompleto, no reciba un marcador de posición en blanco `Hi, !`, en lugar de su nombre o una frase coherente.
{% endraw %}

#### Generar copia de IA

¿Necesitas ayuda para crear textos impactantes? Prueba a utilizar el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduzca el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para utilizarlo en sus mensajes.

![Inicia el botón de redactor de IA, situado en el campo Mensaje del compositor de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 3: Vista previa y prueba de tu mensaje

Braze recomienda siempre previsualizar y probar el mensaje antes de enviarlo. Cambia a la pestaña **Prueba** para enviar un SMS de prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, o previsualiza el mensaje como usuario directamente en Braze.

![Vista previa de la copia del SMS desde la pestaña Prueba del compositor. En la sección de perfil, el campo Nombre está configurado como "James". En la sección de previsualización, el SMS ahora dice "Hola, James, ¡agradecemos tu apoyo!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Si quieres comprobar en cuántos segmentos se puede dividir tu SMS, prueba la longitud de tu texto con nuestra [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaña %}

A continuación, ¡construye el resto de tu campaña! En las secciones siguientes encontrarás más información sobre cómo utilizar mejor nuestras herramientas para crear mensajes SMS.

#### Elige la programación o desencadenante de la entrega

Los mensajes SMS pueden enviarse en función de una hora programada, una acción o un activador de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

En este paso también puede especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Ya deberías haber elegido el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que desean tener contigo. En este paso, seleccionará la audiencia más amplia de sus segmentos, y reducirá aún más ese segmento con nuestros Filtros, si así lo desea. Automáticamente obtendrá una instantánea de cómo es la población de ese segmento aproximado en este momento. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% alert tip %}
¿Te interesa la reorientación por SMS? Visita nuestro [artículo sobre reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) por SMS para saber más.
{% endalert %}

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión le ayudan a medir el éxito de su campaña. Por ejemplo:

- Si utiliza la geolocalización para activar un mensaje SMS cuyo objetivo final es que el usuario realice una compra, configure el evento de conversión en `Purchase`.
- Si está intentando conducir al usuario a su aplicación, establezca el evento de conversión en `Starts Session`.

También puede establecer eventos de conversión personalizados basados en su caso de uso específico. Sea creativo y piense cómo quiere medir realmente el éxito de esta campaña.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de su Canvas, implementar pruebas multivariantes y Selección Inteligente, y más, consulte el paso [Construya su Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 5: Revisar y desplegar

Cuando hayas terminado de crear lo último de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, consulta [los informes de SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber cómo puedes acceder a los resultados de tus campañas por SMS.
