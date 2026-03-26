---
nav_title: "Notificación push web"
article_title: Notificaciones push web
page_order: 8.5
page_type: reference
description: "Esta página de referencia cubre brevemente las notificaciones push web y enlaza con los pasos necesarios para crear una."
platform: Web
channel:
  - push

---

# Notificación push web

> Infórmate sobre las notificaciones push web en Braze y encuentra recursos para crear las tuyas propias.

La notificación push web es otra forma estupenda de interactuar con los usuarios de tu aplicación web. Los clientes que visiten tu sitio web desde [navegadores compatibles](#supported-browsers) pueden optar por recibir notificaciones push web desde tu aplicación web, tanto si la página web está cargada como si no.

## Resumen

Las notificaciones push web ofrecen actualizaciones urgentes y prácticas que impulsan conversiones rápidas. Con la notificación push web, puedes:

- Desencadenar mensajes justo cuando cambien datos importantes, como una bajada de precios
- Atraer a los usuarios a tu sitio web con botones de acción claros
- Personalizar tu push con información sobre productos y clientes para que tu mensaje sea relevante

La notificación push web funciona de la misma manera que las notificaciones push de las aplicaciones en tu teléfono. Para obtener más información sobre cómo redactar una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Ejemplo de push web con el mismo mensaje push mostrado en un portátil y en un teléfono.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Posibles casos de uso

Aquí tienes algunos ejemplos de casos de uso habituales de la mensajería push web.

| Caso de uso | Descripción |
| --- | --- | 
| Prueba gratuita | Anima a los nuevos visitantes de tu sitio web a registrarse en pruebas gratuitas. Al ofrecer a los usuarios la oportunidad de experimentar lo que te hace especial, es más probable que se conviertan en clientes de pago. |
| Descarga de la aplicación | Atrae a los usuarios web a tu aplicación móvil para ayudarles a obtener aún más valor de tus productos. Considera aprovechar la personalización para destacar las ventajas de la aplicación en función de sus patrones de interacción actuales. |
| Descuentos y rebajas | Aumenta el conocimiento de los clientes sobre eventos y promociones con tiempo limitado. Envía mensajes a través de múltiples canales, incluida la notificación push web, para aumentar la visibilidad de las promociones de tu marca. |
| Abandono del carrito de compras | Envía recordatorios automáticos a los usuarios que no hayan finalizado sus transacciones para que vuelvan al flujo de pago. <br><br>Según un estudio realizado por Braze, la notificación push web es un 53 % más eficaz que el correo electrónico y un 23 % más impactante que la notificación push móvil a la hora de conseguir que los destinatarios vuelvan y completen una compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos previos para utilizar la notificación push web

Antes de poder crear y enviar mensajes push con Braze, necesitas trabajar con tus desarrolladores para integrar push en tu sitio web. Para conocer los pasos detallados, consulta nuestra [guía de integración de notificación push web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Permiso push

Cualquier marca puede integrar y utilizar notificaciones push web en su sitio web. Las notificaciones pueden llegar tanto a los visitantes actuales como a los anteriores, siempre que tengan abierto un navegador web, pero los visitantes deben [dar su adhesión voluntaria para recibir notificaciones]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission), al igual que con la notificación push tradicional de las aplicaciones móviles.

{% alert tip %}
Considera utilizar un mensaje en el explorador para preparar a los usuarios para la adhesión voluntaria a la notificación push web, también conocido como [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Navegadores compatibles

Los siguientes navegadores admiten notificaciones push web.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (y Chrome para Android móvil)
- Safari (versión 16 o posterior)
- Firefox (y Firefox para Android móvil)
- Opera
- Edge

Para más información sobre los estándares del protocolo push y la compatibilidad con los navegadores, puedes consultar los recursos según tu navegador:

- [Safari (escritorio)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (móvil)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)