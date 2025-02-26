---
nav_title: "Acerca de las notificaciones push"
article_title: Acerca de las notificaciones Push
page_order: 0
page_type: reference
description: "Este artículo de referencia ofrece un breve resumen de las notificaciones push, proporciona recursos para empezar a utilizar mensajes push y menciona algunas normas."
channel:
  - Push

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}Acerca de las notificaciones push

> Las notificaciones push son magníficas para las llamadas a la acción urgentes, así como para volver a atraer a los usuarios que hace tiempo que no entran en la aplicación. Las campañas push exitosas llevan al usuario directamente al contenido y demuestran el valor de su aplicación.

Tenga en cuenta que los usuarios deben optar por recibir notificaciones push para recibir sus mensajes, lo que significa que es una buena idea utilizar mensajes dentro de la aplicación para explicar a sus clientes por qué desea enviarles notificaciones push y en qué les beneficiará activarlas. Este proceso se llama [preparación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/create_push_primer/).

![Ejemplo de mensaje push en los productos Apple.][1]{: height="400px"}  ![Ejemplo de mensaje push de Cronómetro en una pantalla de inicio de iPhone que dice: "¡Hola! Esto es un push de iOS".][2]{: height="400px"}

Para ver más ejemplos de notificaciones push, consulte nuestros [Estudios de casos][8].

## Posibles casos de uso

Las notificaciones push son una gran herramienta para atraer a nuevos usuarios y hacer campañas de reenganche. He aquí algunos ejemplos de casos de uso habituales de los mensajes push.

| Casos de uso | Explicación |
| -------- | ----------- |
| Incorporación inicial | Hasta que los usuarios no den los pasos iniciales para utilizar su aplicación (como el registro de una cuenta), su valor es muy limitado. Utilice las notificaciones push para instar a los usuarios a completar estos pasos para que puedan empezar a utilizar su aplicación en su totalidad. |
| Primeras compras | Una vez que los usuarios se sientan cómodos utilizando su aplicación, puede utilizar las notificaciones push para convertirlos en compradores dentro de la aplicación. |
| Novedades | Las notificaciones push pueden ser eficaces para notificar a los usuarios desvinculados nuevas funciones que podrían atraerlos de nuevo a su aplicación. |
| Ofertas sensibles al tiempo | Si una oferta tiene fecha de caducidad, a veces los mensajes push son una buena forma de informar a los usuarios antes de que caduque. Estos mensajes generalmente tienen un alto sentido de urgencia y son óptimos para recordar su aplicación a los usuarios que la han abandonado recientemente.<br><br> Por ejemplo, supongamos que tu aplicación es un juego y ofreces a tus usuarios una bonificación en moneda del juego si mantienen una racha de juego diario. Avisar a un usuario de que esa racha está en peligro de romperse podría ser un empujón razonable si ha superado un determinado número de días. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más información sobre la reactivación de la interacción de los usuarios inactivos, consulta nuestra página [Quick Wins][23] sobre el tema.

## Requisitos previos para utilizar push

Antes de poder crear y enviar mensajes push con Braze, debe trabajar con sus desarrolladores para integrar la función push en su sitio web o aplicación. Para conocer los pasos detallados, consulta nuestras guías de integración para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)

## Normativa sobre mensajes push

Dado que los mensajes push son un tipo de mensajería intrusiva que va directamente al teléfono o al navegador del cliente, existen directrices para el envío de mensajes push a través de aplicaciones y sitios.

### Normativa de notificaciones push móviles para aplicaciones

{% alert important %}
Tus mensajes push deben ajustarse a las directrices de las políticas de la App Store de Apple y la Play Store de Google, concretamente en lo que respecta al uso de mensajes push como publicidad, spam, promociones, etc.
{% endalert %}

|Políticas de Apple App Store|
|---|
|[3.2.2][9] Inaceptable: (i) Crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar a la App Store o como una colección de interés general.| 
|[4.5.4][7] Las notificaciones push no deben ser necesarias para el funcionamiento de la aplicación y no deben utilizarse para enviar información personal sensible o confidencial. Las notificaciones push no deben utilizarse con fines promocionales o de marketing directo a menos que los clientes hayan optado explícitamente por recibirlas a través de un lenguaje de consentimiento que aparezca en la interfaz de usuario de su aplicación, y usted proporcione un método en su aplicación para que un usuario pueda optar por no recibir tales mensajes.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) No podrá monetizar las capacidades integradas proporcionadas por el hardware o el sistema operativo, como las notificaciones Push, la cámara o el giroscopio; o los servicios y tecnologías de Apple, como el acceso a Apple Music, el almacenamiento en iCloud o las API de Screen Time.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Política de Google Play Store|
|---|
|[Uso no autorizado o imitación de la funcionalidad del sistema][10] No permitimos aplicaciones o anuncios que imiten o interfieran con la funcionalidad del sistema, como notificaciones o avisos. Las notificaciones a nivel de sistema sólo pueden utilizarse para las funciones integrales de una aplicación, como una aplicación de aerolínea que notifica a los usuarios ofertas especiales, o un juego que notifica a los usuarios promociones dentro del juego.|
{: .reset-td-br-1 role="presentation" }

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]: https://www.braze.com/customers
[7]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]: https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
