---
nav_title: Saber antes de enviar
article_title: Saber antes de enviar
description: "Después de visitar nuestra guía previa al lanzamiento, consulta esta lista final de comprobaciones o \"gotchas\" para las tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push y SMS."
alias: /know_before_send/
page_order: 10
tool:
    - Campaigns
    - Canvas
---

# Saber antes de enviar: canales

¡Lanza campañas y Canvas con confianza! Consulta esta lista final de comprobaciones o "gotchas" para tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push y SMS.

{% alert note %}
Aunque proporcionamos una extensa lista de recursos de referencia previa al envío, cada canal tiene matices individuales que siguen creciendo a medida que evolucionamos nuestros productos. Las comprobaciones que se indican a continuación son sugerencias útiles, y te recomendamos que pruebes a fondo tus campañas y grandes envíos antes de enviarlos.
{% endalert %}

## General

#### Cosas que hay que comprobar
- [**Límites de velocidad de la API**](https://braze.com/resources/articles/whats-rate-limiting): Revisa los [límites de velocidad]({{site.baseurl}}/api/api_limits/) de la API Braze de tus espacios de trabajo para evitar errores. Si quieres aumentar los límites de velocidad (y ya estás acumulando solicitudes), ponte en contacto con tu administrador del éxito del cliente. Ten en cuenta que este proceso requiere tiempo, así que planifícalo en consecuencia.
- [**La limitación de frecuencia necesaria anula**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Hay algunas campañas, como los mensajes transaccionales, que querrás que lleguen siempre al usuario, aunque ya hayas alcanzado su límite de frecuencia (por ejemplo, una notificación de entrega). Si quieres que una campaña concreta anule las normas de limitación de frecuencia, puedes configurarlo en el panel de Braze al programar la entrega de esa campaña, alternando la desactivación de la limitación de frecuencia.

#### Lo que debes saber
- [**Grupos de control global**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Si utilizas un grupo de control global, un porcentaje de usuarios no recibirá ninguna campaña ni ningún Lienzo. (Puedes crear excepciones con la [configuración de exclusión]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). Para ver una lista de estos usuarios, expórtalos mediante CSV o [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Límites de velocidad de Canvas**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): En un Canvas, el límite de velocidad se aplica a todo el Canvas, no a los pasos individuales. Por ejemplo, si establecieras un límite de tasa de 10.000 mensajes por minuto en un Canvas con varios pasos, seguirá estando limitado a 10.000 mensajes porque el límite se habrá alcanzado en el primer paso.
- **Limitación de frecuencia**: 
  - Las normas de limitación de frecuencia se aplicarán a push, correo electrónico, SMS y webhooks, pero no a los mensajes dentro de la aplicación ni a las tarjetas de contenido.
  - La limitación de frecuencia global se programa en función de la zona horaria del usuario y se calcula por días naturales, no por periodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de envío de no más de una campaña al día, un usuario puede recibir un mensaje a las 11 de la noche en su zona horaria local, y sería elegible para recibir otro mensaje una hora más tarde.

{% alert tip %}
Para obtener más ayuda con Canvas y la solución de problemas de campaña, asegúrate de ponerte en contacto con el soporte de Braze en los 30 días siguientes a la aparición del problema, ya que sólo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

## Correo electrónico

#### Cosas que hay que comprobar
- **Consentimiento del cliente**: Antes de enviar tus correos electrónicos iniciales, es importante obtener primero el permiso de tus clientes. Consulta [Consentimiento y recopilación de direcciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) y nuestra [Política de uso aceptable de Braze](https://www.braze.com/company/legal/aup) para obtener más información.
- **Volumen previsto**: 2 millones de correos electrónicos al día para una sola IP es la recomendación general, siempre que ese volumen se haya [calentado adecuadamente]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - Si planeas enviar sistemáticamente un volumen superior a este, para evitar que los proveedores limiten la recepción de correos electrónicos, lo que provocaría una gran cantidad de rebotes blandos, una tasa de capacidad de entrega más baja y una menor reputación de la IP, considera la posibilidad de utilizar varias direcciones IP agrupadas en un conjunto de IP. 
  - Si sólo quieres enviar en un plazo de tiempo más corto, te recomendamos que investigues con qué rapidez aceptan el correo los distintos proveedores para calibrar el número adecuado de IP desde las que enviar. 

#### Lo que debes saber
- **Factores de volumen de envío**: Algunos factores que determinan los volúmenes de envío capaces de una IP son:
  - Buzones: Es probable que los grandes proveedores de correo electrónico puedan gestionar millones al día desde una sola IP, mientras que un proveedor de buzones regional más pequeño o con una infraestructura menor podría no ser capaz de gestionar esa cantidad.
  - Reputación del remitente: Es posible que puedas enviar un volumen mayor al día desde una sola IP si el remitente está preparado para ese volumen y si la reputación del remitente es lo suficientemente fuerte en cada buzón o dominio al que envía.
- **Buenas prácticas**: Revisa [las mejores prácticas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) Braze y ponte en contacto con tu equipo de cuenta Braze si deseas obtener más información sobre los servicios de capacidad de entrega.

## Push

#### Cosas que hay que comprobar
- [**Adhesión voluntaria/suscrito y habilitación push**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Para que los usuarios reciban un mensaje push de Braze, necesitan que sus estados de suscripción sean de adhesión voluntaria (iOS) o de suscripción (Android) y `Push Enabled = True`. Ten en cuenta que Android 13 introduce un cambio importante en la forma en que los usuarios administran las aplicaciones que envían notificaciones push. La [guía de actualización del SDK de Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/) de Braze seguirá actualizándose a medida que se publiquen nuevas versiones beta de Android 13.

#### Lo que debes saber
- **Notificación push web**: Si tienes [configurado el SDK Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) de Braze, considera la posibilidad de utilizar el push web para interactuar con los usuarios. Web push funciona de la misma manera que las notificaciones push de las aplicaciones en tu teléfono. Para más información sobre cómo componer una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Segmentación de una aplicación singular**: Revisa las [diferencias de segmentación]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) para dirigirte a una aplicación singular y a sus usuarios.

## SMS

#### Cosas que hay que comprobar
- **Adjudicaciones y rendimiento**: Comprende qué asignaciones de SMS están actualmente vinculadas a tu cuenta (código abreviado, código largo y similares) y [cuánto caudal te proporciona eso]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) para confirmar que tienes suficiente caudal para enviar en el tiempo que deseas.
- **Estima el segmento a partir de la copia del SMS**: Prueba tu copia SMS en la [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Ten en cuenta que el número de segmentos de SMS debe tenerse en cuenta junto con tu capacidad de rendimiento. (Audiencia * segmentos de SMS = rendimiento necesario). Consulta las FAQ de SMS para [evitar excedentes]({{site.baseurl}}/sms_faq/).
- **Leyes y reglamentos de SMS**: [Revisa las leyes, reglamentos y prevención de abusos de los]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) SMS para confirmar que utilizas los servicios SMS de acuerdo con todas las leyes aplicables. Asegúrate de que debes pedir consejo a tu asesor jurídico antes de enviar.

#### Lo que debes saber
- **Mensajes SMS predeterminados**: Normalmente, los mensajes SMS están predeterminados para ser enviados desde el código abreviado del grupo de remitentes.
- **ID alfanumérico del remitente**: La mensajería bidireccional ya no funcionará si utilizas un ID de remitente alfanumérico; ahora son sólo unidireccionales.
- **Rendimiento actualizado en EE. UU.**: El rendimiento en EE. UU. cambió con el [registro A2P 10DLC](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Ten en cuenta que no nos comprometemos contractualmente a ningún SLA de velocidad de envío debido a múltiples factores, como congestión del tráfico y problemas del operador, que podrían afectar las tasas de entrega reales.
- **Grupo de suscripción**: Para lanzar una campaña SMS a través de Braze, hay que seleccionar un grupo de suscripción. Además, para cumplir las [normas y directrices internacionales de telecomunicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze nunca enviará SMS a usuarios que no [se hayan suscrito al grupo de suscripción seleccionado]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## WhatsApp

#### Lo que debes saber

- [**Las mejores prácticas**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Revisa las buenas prácticas que sugerimos para WhatsApp.

## Banners

#### Cosas que hay que comprobar
- **Dimensiones de la pancarta:** Construye tus Banners utilizando un elemento de dimensión fija y pruébalos en el editor.
- **Prioridad:** Si lanzas varios banners, puedes establecer manualmente la prioridad de visualización de cada banner.

#### Lo que hay que saber
- **Personalización líquida:** La personalización Liquid se actualiza cada vez que se inicia una sesión.
- **Ratio de colocación y Banner:** Cada colocación de Banner puede utilizarse en hasta 10 campañas en un espacio de trabajo.  
- **Clics e impresiones:** Los clics y las impresiones de los banners se siguen automáticamente con el SDK.
- **Limitaciones:**  Actualmente, no se admiten las siguientes características: Integración de Canvas, campañas desencadenadas por API y basadas en acciones, Currents, Contenido conectado, códigos promocionales, despidos controlados por el usuario y `catalog_items` utilizando la [etiqueta`:rerender` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).
- **Pruebas:** Para mostrar el Banner de prueba, el dispositivo que estés utilizando debe poder recibir notificaciones push en primer plano.
- **HTML personalizado:** Aprovecha [el puente JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) para registrar los clics cuando utilices HTML personalizado para definir acciones de clic, como enlaces y botones. Las acciones de clic sólo se registran automáticamente cuando se utilizan los componentes preconstruidos en el editor de arrastrar y soltar.
- **Solicitud de Colocaciones:** Se pueden devolver al SDK hasta 10 colocaciones por sesión. Cada colocación incluirá el Banner de mayor prioridad al que sea elegible un usuario.

## Tarjetas de contenido

#### Cosas que hay que comprobar
- **Tamaño de la tarjeta de contenido**: Los campos de mensaje de la tarjeta de contenido están limitados a 2 KB de tamaño de precompresión, calculado sumando la longitud en bytes de los siguientes campos: título, mensaje, URL de imagen, texto de enlace, URL de enlace y pares clave-valor. Los mensajes que superen este tamaño no se enviarán. Ten en cuenta que esto no incluye el tamaño de la imagen, sino la longitud de la URL de la imagen.
- **Actualizar la copia después del envío**: Después de enviar una tarjeta, no podrás actualizar la copia de esa misma tarjeta. Consulta [Actualizar tarjetas enviadas]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards) para entender cómo puedes enfocar este escenario.

#### Lo que debes saber
- **Límite de campañas activas de la tarjeta de contenido**: Puedes tener hasta 500 campañas de tarjeta de contenido activas. Este recuento incluye las tarjetas de contenido enviadas con cualquiera de las opciones de [creación de tarjetas]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).  
- [**Condiciones de notificación**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Revisa términos como impresiones totales, impresiones únicas y destinatarios únicos, ya que las definiciones a veces pueden causar confusión.
- **Actualización de la tarjeta de contenido**: Por defecto, Braze actualiza las solicitudes de tarjetas de contenido cuando se sincronizan al inicio de la sesión, al deslizar hacia abajo la fuente (móvil) y cuando se abre la vista de tarjetas si la última actualización fue hace más de un minuto.
- **Almacenamiento en caché de tarjetas de contenido**: Puedes encontrar las opciones de almacenamiento en caché de la tarjeta de contenido en nuestros documentos de [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) y [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Limitación de frecuencia**: La limitación de frecuencia no se aplica a las tarjetas de contenido.
- **Impresiones**: Por lo general, las impresiones se registran cuando se ve una tarjeta. Por ejemplo, si tienes un buzón de entrada lleno de tarjetas de contenido, no se registrará una impresión hasta que el usuario se desplace hasta la tarjeta de contenido específica. Existen algunos matices entre las plataformas Web, Android e iOS.  

## Mensajes dentro de la aplicación

#### Lo que debes saber
- **Desencadenar mensajes dentro de la aplicación**: Al inicio de la sesión, el SDK solicita que se envíen al dispositivo todos los mensajes dentro de la aplicación elegibles junto con sus desencadenantes, de modo que si realizan el evento durante la sesión, puedan recibir el mensaje dentro de la aplicación de forma rápida y fiable.
- **Enviados frente a impresiones**: Para los mensajes dentro de la aplicación, el concepto de "enviado" difiere de los otros canales disponibles. Para ver un mensaje dentro de la aplicación, un usuario tiene que iniciar una sesión, pertenecer a la audiencia elegible y desencadenar la acción. Por ello, hacemos un seguimiento de las "impresiones", ya que es más claro.
- **Desencadenamiento**: De manera predeterminada, los mensajes dentro de la aplicación se desencadenan por eventos registrados por el SDK. Si quieres desencadenar mensajes dentro de la aplicación mediante eventos enviados por el servidor, también puedes conseguirlo mediante estas guías para [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) y [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
- [Mensajes dentro de la aplicación Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Estos mensajes aparecen la primera vez que tu usuario abre la aplicación (desencadenados por la sesión de inicio) después de que se le haya enviado el mensaje programado en el componente Canvas.
- **Llamadas de contenido conectado**: Utilizar Contenido conectado te permite enviar contenido dinámico en mensajes. Cuando envías mensajes a través de un canal como los mensajes dentro de la aplicación, esto puede crear más conexiones simultáneas con los dispositivos de tus usuarios (los mensajes se envían uno a uno en lugar de por lotes). Para gestionarlo, te recomendamos [limitar la tasa de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) tus mensajes.
