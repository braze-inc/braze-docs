---
nav_title: Septiembre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2019."
---

# Septiembre de 2019

## Aplicación Braze dentro de OneLogin

Los clientes podrán simplemente buscar y seleccionar Braze dentro de [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) para iniciar sesión como SP o IdP. Esto significa que los clientes no tendrán que añadir una aplicación personalizada dentro de OneLogin. Como resultado, esto debería rellenar previamente ciertas configuraciones como los atributos que vimos aparecer desde el lanzamiento de SAML SSO.

## Colaboración en el calendario Rokt

[Rokt Calendar]({{site.baseurl}}/partners/home/) ofrece a los clientes de Braze la posibilidad de alinear sus iniciativas de marketing personalizado y ampliar el contenido personalizado al calendario del usuario final. De este modo, se consigue una experiencia más fluida para el usuario final y se desarrolla aún más la adherencia a los servicios de nuestros clientes. Los clientes podrán...

- Envía una invitación de calendario a través de la plataforma Braze para "guardar la fecha" y ampliar nuestra comunicación
- Actualiza una invitación existente si el contenido del evento ha cambiado.

## Asociación Passkit

Con [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), los clientes de Braze podrán ampliar su interacción con los clientes a la billetera móvil. Podrán usar la potente segmentación de Braze para personalizar campañas de billetera y orquestarlas junto con canales como push, mensajes dentro de la aplicación y más.

## Devolución del valor del ID de envío a través de los puntos finales de mensajería

La dirección `dispatch_id` de un mensaje se incluirá en las siguientes respuestas del punto final de mensajería:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

De este modo, los clientes que utilicen mensajería transaccional podrán rastrear la llamada a través de Currents.

## Registros de cambios de Canvas

¿Te has preguntado más detalles sobre quién está trabajando en un Canvas en tu cuenta? ¡No te lo preguntes más! Ahora puedes acceder a los registros de cambios de Canvas.

![Registro de cambios de Canvas]({% image_buster /assets/img/canvas-changelog1.png %})
![Registro de cambios de Canvas]({% image_buster /assets/img/canvas-changelog2.png %})
