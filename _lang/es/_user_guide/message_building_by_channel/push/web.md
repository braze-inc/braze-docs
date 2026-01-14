---
nav_title: "Web push"
article_title: Notificaciones push web
page_order: 8.5
page_type: reference
description: "Esta página de referencia cubre brevemente las notificaciones push web, y enlaza con los pasos necesarios para crear una."
platform: Web
channel:
  - push

---

# Web push

> Infórmate sobre las notificaciones push web en Braze y encuentra recursos para crear las tuyas propias.

Web push es otra forma estupenda de interacción con los usuarios de tu aplicación web. Los clientes que visiten tu sitio web desde [navegadores compatibles](#supported-browsers) pueden optar por recibir notificaciones push web de tu aplicación web, tanto si la página web está cargada como si no.

## Resumen

Las notificaciones push web entregan actualizaciones urgentes y procesables que impulsan rápidas conversiones. Con la notificación push web, puedes:

- Desencadena mensajes justo cuando cambien datos importantes, como la bajada de un precio
- Haz que la gente vuelva a tu sitio web con sencillos botones de llamada a la acción
- Personaliza tu push con información sobre productos y clientes para que tu mensaje sea relevante

Web push funciona de la misma manera que las notificaciones push de las aplicaciones en tu teléfono. Para más información sobre cómo componer una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

\![Ejemplo de push web con el mismo mensaje push mostrado en un portátil y en un teléfono.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Casos de uso potenciales

He aquí algunos ejemplos de casos de uso habituales de la mensajería push web.

| Casos de uso | Descripción |
| --- | --- | 
| Prueba gratuita | Anima a los nuevos visitantes de tu sitio web a registrarse para obtener pruebas gratuitas. Si enganchas a los usuarios con la oportunidad de experimentar lo que te hace especial, es más probable que se conviertan en clientes de pago. |
| Descarga de la aplicación | Atrae a los usuarios Web a tu aplicación móvil para ayudarles a obtener aún más valor de tus productos. Considera la posibilidad de aprovechar la personalización para destacar las ventajas de la aplicación en función de sus patrones de interacción actuales. |
| Descuentos y rebajas | Aumenta el conocimiento de los clientes sobre eventos y promociones sensibles al tiempo. Envía mensajes a través de múltiples canales, incluido el push web, para aumentar el conocimiento de las promociones de tu marca. |
| Abandono del carrito de la compra | Envía recordatorios automatizados a los usuarios que no hayan finalizado sus transacciones para que vuelvan al flujo de pago. <br><br>Una investigación realizada por Braze descubrió que el push web es un 53% más eficaz que el correo electrónico y un 23% más impactante que el push móvil a la hora de conseguir que los destinatarios vuelvan y completen una compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos previos para utilizar la notificación push web

Antes de que puedas crear y enviar mensajes push con Braze, tienes que trabajar con tus desarrolladores para integrar push en tu sitio web. Para conocer los pasos detallados, consulta nuestra [guía de integración push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Push permiso

Cualquier marca puede integrar y utilizar notificaciones push web en su sitio web. Las notificaciones pueden llegar tanto a los visitantes actuales de la web como a los anteriores, siempre que tengan un navegador web abierto, pero los visitantes deben [optar por recibir notificaciones,]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)igual que con el push tradicional de las aplicaciones móviles.

{% alert tip %}
Considera la posibilidad de utilizar un mensaje en el explorador para preparar a los usuarios para la adhesión voluntaria al push web, también conocido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatibles

Los siguientes navegadores admiten notificaciones push web. Sin embargo, las ventanas de navegación privada no admiten actualmente la notificación push web.

- Chrome (y Chrome para móviles Android)
- Safari
- Firefox (y Firefox para móviles Android)
- Ópera
- Arista

Para obtener más información sobre las normas del protocolo push y la compatibilidad de los navegadores, puedes consultar los recursos basados en tu navegador:

- [Safari (escritorio)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (móvil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


