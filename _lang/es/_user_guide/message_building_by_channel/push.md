---
nav_title: Push
article_title: Push
page_order: 4
layout: dev_guide
guide_top_header: "Push"
guide_top_text: "Las notificaciones push son una forma probada de enviar llamadas a la acción urgentes a través del móvil o la Web, así como de reactivar la interacción de los usuarios que hace tiempo que no entran en la aplicación. Llevan al usuario directamente al contenido y demuestran el valor de tu aplicación. Las notificaciones push son útiles para conducir a los usuarios a un lugar concreto, pero debes utilizarlas con prudencia. <br><br> Lea cualquiera de los siguientes artículos o consulte nuestro curso [Push Braze Learning course](https://learning.braze.com/messaging-channels-push) para saber a quién puede enviar un push, cómo enviarlo y qué funciones avanzadas de push ofrece Braze. Para ver ejemplos de notificaciones push, consulta nuestras [historias de clientes](https://www.braze.com/customers)."
description: "Esta página de destino alberga mensajes push. Aquí encontrará artículos sobre tipos de push, registro push, habilitación push, primers push, informes push, etc."
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
- name: Habilitación y suscripción push
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
- name: Push primers
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: Informe
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Opciones de Android
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: Opciones de iOS
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: Notificación push web
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: Buenas prácticas
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Locales en los mensajes
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

## [![Curso de Braze](https://learning.braze.com/path/push-fundamentals) Learning []({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso

![Ejemplo de mensaje push en los productos Apple.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  ![Ejemplo de mensaje push de Cronómetro en una pantalla de inicio de iPhone que dice: "¡Hola! Esto es un push de iOS".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

Las notificaciones push son una gran herramienta para atraer a nuevos usuarios y hacer campañas de reenganche. He aquí algunos ejemplos de casos de uso habituales de los mensajes push.

| Casos de uso | Explicación |
| -------- | ----------- |
| Incorporación inicial | Hasta que los usuarios no den los pasos iniciales para utilizar su aplicación (como el registro de una cuenta), su valor es muy limitado. Utilice las notificaciones push para instar a los usuarios a completar estos pasos para que puedan empezar a utilizar su aplicación en su totalidad. |
| Primeras compras | Una vez que los usuarios se sientan cómodos utilizando su aplicación, puede utilizar las notificaciones push para convertirlos en compradores dentro de la aplicación. |
| Novedades | Las notificaciones push pueden ser eficaces para notificar a los usuarios desvinculados nuevas funciones que podrían atraerlos de nuevo a su aplicación. |
| Ofertas sensibles al tiempo | Si una oferta tiene fecha de caducidad, a veces los mensajes push son una buena forma de informar a los usuarios antes de que caduque. Estos mensajes generalmente tienen un alto sentido de urgencia y son óptimos para recordar su aplicación a los usuarios que la han abandonado recientemente.<br><br> Por ejemplo, supongamos que tu aplicación es un juego y ofreces a tus usuarios una bonificación en moneda del juego si mantienen una racha de juego diario. Avisar a un usuario de que esa racha está en peligro de romperse podría ser un empujón razonable si ha superado un determinado número de días. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre la reactivación de la interacción de los usuarios que han dejado de serlo, consulta nuestra página de [Quick Wins]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) sobre el tema.

## Requisitos previos para utilizar push

Antes de poder crear y enviar mensajes push con Braze, debe trabajar con sus desarrolladores para integrar la función push en su sitio web o aplicación. Para conocer los pasos detallados, consulta nuestras guías de integración para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Preparación para las notificaciones push

Tenga en cuenta que los usuarios deben optar por recibir notificaciones push para recibir sus mensajes, lo que significa que es una buena idea utilizar mensajes dentro de la aplicación para explicar a sus clientes por qué desea enviarles notificaciones push y en qué les beneficiará activarlas. Este proceso se llama [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Normativa sobre mensajes push

Dado que los mensajes push son un tipo de mensajería intrusiva que va directamente al teléfono o al navegador de tu cliente, existen directrices para enviar mensajes push a través de aplicaciones y sitios web.

### Normativa de notificaciones push móviles para aplicaciones

{% alert important %}
Tus mensajes push deben ajustarse a las directrices de las políticas de la App Store de Apple y la Play Store de Google, concretamente en lo que respecta al uso de mensajes push como publicidad, spam, promociones, etc.
{% endalert %}

|Políticas de Apple App Store|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceptable: (i) Crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar a la App Store o como una colección de interés general.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Las notificaciones push no deben ser necesarias para que la aplicación funcione, y no deben utilizarse para enviar información personal sensible o confidencial. Las notificaciones push no deben utilizarse con fines promocionales o de marketing directo a menos que los clientes hayan optado explícitamente por recibirlas a través de un lenguaje de consentimiento que aparezca en la interfaz de usuario de su aplicación, y usted proporcione un método en su aplicación para que un usuario pueda optar por no recibir tales mensajes.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) No podrá monetizar las capacidades integradas proporcionadas por el hardware o el sistema operativo, como las notificaciones Push, la cámara o el giroscopio; o los servicios y tecnologías de Apple, como el acceso a Apple Music, el almacenamiento en iCloud o las API de Screen Time.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Política de Google Play Store|
|---|
|[Uso no autorizado o imitación de la funcionalidad del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) No permitimos aplicaciones o anuncios que imiten o interfieran con la funcionalidad del sistema, como notificaciones o advertencias. Las notificaciones a nivel de sistema sólo pueden utilizarse para las funciones integrales de una aplicación, como una aplicación de aerolínea que notifica a los usuarios ofertas especiales, o un juego que notifica a los usuarios promociones dentro del juego.|
{: .reset-td-br-1 role="presentation" }
