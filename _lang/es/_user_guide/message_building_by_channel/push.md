---
nav_title: Push
article_title: Push
page_order: 4
layout: dev_guide
guide_top_header: "Push"
guide_top_text: "Las notificaciones push son una forma probada de enviar llamadas a la acción urgentes a través del móvil o la Web, así como de reactivar la interacción de los usuarios que hace tiempo que no entran en la aplicación. Llevan al usuario directamente al contenido y demuestran el valor de tu aplicación. Las notificaciones push son útiles para conducir a los usuarios a un lugar concreto, pero debes utilizarlas con prudencia. <br><br> Lee cualquiera de los siguientes artículos o consulta nuestro [curso de Braze Learning sobre push](https://learning.braze.com/messaging-channels-push) para saber a quién puedes enviar un push, cómo enviarlo y qué funciones avanzadas de push ofrece Braze. Para ver ejemplos de notificaciones push, consulta nuestras [historias de clientes](https://www.braze.com/customers)."
description: "Esta página de inicio alberga mensajes push. Aquí encontrarás artículos sobre tipos de push, registro push, habilitación push, primers push, informes push y mucho más."
channel:
  - push

guide_featured_title: "Artículos populares"
guide_featured_list:
- name: Tipos de push
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: Registro Push
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Habilitación push y suscripción
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: Crear un mensaje push
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: Opciones avanzadas
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: Cebadores Push
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Informar
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Opciones de Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Opciones de iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Web Push
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Buenas prácticas
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Localizaciones en mensajes
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: Mensajes de error push comunes
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: Solución de problemas
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: Preguntas frecuentes
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso

\![Ejemplo de mensaje push entre productos Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"} Ejemplo de mensaje push de Cronómetro en la pantalla de inicio de un iPhone: "¡Hola! Esto es un push de iOS".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Las notificaciones push son una gran herramienta para atraer a nuevos usuarios y hacer campañas de reactivación de la interacción. Aquí tienes algunos ejemplos de casos de uso habituales de los mensajes push.

| Casos de uso | Explicación |
| -------- | ----------- |
| Incorporación inicial | Hasta que los usuarios no den los pasos iniciales para utilizar tu aplicación (como registrar una cuenta), su valor estará muy limitado. Utiliza notificaciones push para instar a los usuarios a completar estos pasos para que puedan empezar a utilizar tu aplicación en su totalidad. |
| Primeras compras | Cuando los usuarios se sientan cómodos utilizando tu aplicación, puedes utilizar las notificaciones push para convertirlos en compradores dentro de la aplicación. |
| Nuevas características | Las notificaciones push pueden ser eficaces para notificar a los usuarios desvinculados las nuevas características que podrían atraerlos de nuevo a tu aplicación. |
| Ofertas sensibles al tiempo | Si tienes una oferta pendiente, a veces el push es una buena forma de informar a tus usuarios antes de que caduque. Estos mensajes suelen tener un alto sentido de la urgencia y son óptimos para recordar tu aplicación a los usuarios que la han perdido recientemente.<br><br> Por ejemplo, supongamos que tu aplicación es un juego y ofreces a tus usuarios una bonificación en moneda del juego si mantienen una racha de juego diario. Avisar a un usuario de que esa racha corre peligro de romperse podría ser un push razonable si ha superado un determinado número de días. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre la reactivación de la interacción de los usuarios que han dejado de serlo, consulta nuestra página de [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sobre el tema.

## Requisitos previos para utilizar push

Antes de que puedas crear y enviar mensajes push con Braze, tienes que trabajar con tus desarrolladores para integrar push en tu sitio web o aplicación. Para conocer los pasos detallados, consulta nuestras guías de integración para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Preparación para las notificaciones push

Ten en cuenta que los usuarios necesitan la adhesión voluntaria a la función push para recibir tus mensajes, lo que significa que es una buena idea utilizar mensajes dentro de la aplicación para explicar a tus clientes por qué quieres enviarles notificaciones push y cómo les beneficiará habilitar la función push. Este proceso se llama [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Normativa sobre mensajes push

Dado que los mensajes push son un tipo de mensajería intrusiva que va directamente al teléfono o al navegador de tu cliente, existen directrices para enviar mensajes push a través de aplicaciones y sitios web.

### Normativa push móvil para aplicaciones

{% alert important %}
Tus mensajes push deben cumplir las directrices de las políticas de la App Store de Apple y de la Play Store de Google, específicamente en lo que respecta al uso de mensajes push como publicidad, correo no deseado, promociones, etc.
{% endalert %}

|Políticas de la App Store de Apple|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceptable: (i) Crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar a la App Store o como una colección de interés general.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Las notificaciones push no deben ser necesarias para que la aplicación funcione, y no deben utilizarse para enviar información personal sensible o confidencial. Las notificaciones push no deben utilizarse para promociones o fines de marketing directo, a menos que los clientes hayan optado explícitamente por recibirlas a través del lenguaje de consentimiento que aparece en la interfaz de usuario de tu aplicación, y proporciones un método en tu aplicación para que un usuario pueda optar por no recibir dichos mensajes.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) No puedes monetizar las capacidades integradas proporcionadas por el hardware o el sistema operativo, como las notificaciones push, la cámara o el giroscopio; o los servicios y tecnologías de Apple, como el acceso a Apple Music, el almacenamiento en iCloud o las API de Screen Time.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Política de Google Play Store|
|---|
|[Uso no autorizado o imitación de la funcionalidad del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) No permitimos aplicaciones o anuncios que imiten o interfieran con la funcionalidad del sistema, como notificaciones o advertencias. Las notificaciones a nivel de sistema sólo pueden utilizarse para las características integrales de una aplicación, como una aplicación de aerolínea que notifica a los usuarios las ofertas especiales, o un juego que notifica a los usuarios las promociones dentro del juego.|
{: .reset-td-br-1 role="presentation" }
