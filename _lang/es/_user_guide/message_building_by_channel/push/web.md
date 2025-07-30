---
nav_title: "Notificación push web"
article_title: Notificaciones Web Push
page_order: 8.5
page_type: reference
description: "Esta página de referencia cubre brevemente las notificaciones push web, y enlaza con los pasos necesarios para crear una."
platform: Web
channel:
  - push

---

# Web push

> Infórmate sobre las notificaciones web push en Braze y encuentra recursos para crear las tuyas propias.

Web push es otra forma estupenda de interacción con los usuarios de tu aplicación web. Los clientes que visiten su sitio web desde [navegadores compatibles](#supported-browsers) pueden optar por recibir web push desde su aplicación web, tanto si la página web está cargada como si no.

## Resumen

Las notificaciones web push ofrecen actualizaciones urgentes y prácticas que impulsan conversiones rápidas. Con web push, puedes:

- Activar mensajes justo cuando cambien datos importantes, como una bajada de precios
- Haga que la gente vuelva a su sitio web con sencillos botones de llamada a la acción
- Personalice su push con información sobre productos y clientes para que su mensaje sea relevante

Web push funciona de la misma manera que las notificaciones push de las aplicaciones en tu teléfono. Para más información sobre cómo componer una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Ejemplo de push web con el mismo mensaje push mostrado en un portátil y en un teléfono.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Posibles casos de uso

He aquí algunos ejemplos de casos de uso habituales de la mensajería push web.

| Caso de uso | Descripción |
| --- | --- | 
| Prueba gratuita | Anime a los nuevos visitantes de su sitio web a suscribirse a pruebas gratuitas. Si ofrece a los usuarios la oportunidad de experimentar lo que le hace especial, es más probable que se conviertan en clientes de pago. |
| Descarga de la aplicación | Atraiga a los internautas a su aplicación móvil para ayudarles a obtener aún más valor de sus productos. Considere la posibilidad de aprovechar la personalización para destacar las ventajas de la aplicación en función de sus patrones de interacción actuales. |
| Descuentos y rebajas | Aumente la concienciación de los clientes sobre eventos y promociones sensibles al tiempo. Envía mensajes a través de múltiples canales, incluido el push web, para aumentar el conocimiento de las promociones de tu marca. |
| Abandono del carro | Envíe recordatorios automáticos a los usuarios que no hayan finalizado sus transacciones para que vuelvan al flujo de pago. <br><br>Según un estudio realizado por Braze, el push web es un 53% más eficaz que el correo electrónico y un 23% más impactante que el push móvil a la hora de conseguir que los destinatarios vuelvan y completen una compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos previos para utilizar la notificación push web

Antes de poder crear y enviar mensajes push con Braze, debe trabajar con sus desarrolladores para integrar push en su sitio web. Para conocer los pasos detallados, consulta nuestra [guía de integración push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permiso de notificaciones push

Cualquier marca puede integrar y utilizar notificaciones push web en su sitio web. Las notificaciones pueden llegar tanto a los visitantes actuales de la web como a los anteriores, siempre que tengan abierto un navegador web, pero los visitantes deben [optar por recibir notificaciones,]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)al igual que con el push tradicional de las aplicaciones móviles.

{% alert tip %}
Considere la posibilidad de utilizar un mensaje en el navegador para incitar a los usuarios a optar por el push web, también conocido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatibles

Los siguientes navegadores admiten notificaciones web push. Sin embargo, las ventanas de navegación privada no admiten actualmente la notificación push web.

- Chrome (y Chrome para móviles Android)
- Safari
- Firefox (y Firefox para móviles Android)
- Opera
- Edge

Para más información sobre los estándares del protocolo push y la compatibilidad con los navegadores, puedes consultar los recursos basados en tu navegador:

- [Safari (escritorio)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (móvil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


