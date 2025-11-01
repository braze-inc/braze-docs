---
nav_title: Creación de mensajes por canal
article_title: Creación de mensajes por canal
page_order: 5
layout: dev_guide

guide_top_header: "Creación de mensajes por canal"
guide_top_text: "Los canales de mensajería son formas de comunicarte virtualmente con tus clientes a través de notificaciones push en su teléfono o navegador Web, correo electrónico, mensajes dentro de la aplicación, ¡y mucho más! Si quieres saber más sobre estos canales y cómo utilizarlos con Braze, consulta las siguientes secciones enumeradas. ¡O echa un vistazo a nuestros cursos de Braze Learning sobre <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>canales de mensajería</a>!<br><br>Puedes utilizar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus ingenieros para asegurarte de que cumples las normas de accesibilidad en tu implementación."
description: "Esta página de destino cubre los canales de mensajería Braze. Los canales de mensajería son formas de comunicarte virtualmente con tus clientes a través de notificaciones push en su teléfono o navegador Web, correo electrónico, mensajes dentro de la aplicación, ¡y mucho más!"

guide_featured_title: "Canales disponibles"
guide_featured_list:
- name: Pancartas
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Tarjetas de contenido
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Mensajería por correo electrónico
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "Mensajería dentro de la aplicación"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Mensajería push
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS y RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Recursos de accesibilidad

Puedes utilizar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus ingenieros para asegurarte de que cumples las normas de accesibilidad en tu implementación. Si deseas orientación adicional, te recomendamos:

- [Fundamentos de la mensajería accesible](https://learning.braze.com/accessible-messaging-foundations): Aprende los principios fundamentales de accesibilidad que se aplican a las comunicaciones de marca en este curso de Braze Learning.
- [Construir mensajes accesibles]({{site.baseurl}}/help/accessibility/): Aprende a añadir texto alternativo y a estructurar tu contenido para tecnologías de apoyo directamente desde Braze.

{% multi_lang_include accessibility/feedback.md %}

## Elegir un canal de mensajería

Cuando determines qué canal de mensajería es mejor para tus campañas y Lienzos, piensa siempre en el contenido y la urgencia de tu mensaje:

- **El contenido** es el grado de interacción visual de tu mensaje. Puedes añadir multimedia y otros activos a tu texto para enriquecer tu contenido.
- **La urgencia** es una medida de la rapidez con la que un mensaje es capaz de notificar a tu usuario y atraer su atención. Las notificaciones que el usuario puede ver inmediatamente tienen una urgencia alta, mientras que los mensajes que necesitan que el usuario inicie sesión en tu aplicación tienen una urgencia baja.

La siguiente matriz ilustra los puntos fuertes y débiles de los canales de mensajería clave en términos de contenido y urgencia. Piensa siempre en lo urgente y rico en contenido que debe ser tu mensaje, y luego elige el canal adecuado para tu campaña.

Los mensajes push web/móvil son de contenido sencillo y urgencia alta; los correos electrónicos son de contenido rico y urgencia alta; los mensajes dentro de la aplicación/navegador son de contenido sencillo y urgencia baja; las tarjetas de contenido son de urgencia baja y contenido rico.]({% image_buster /assets/img_archive/messaging_matrix.png %})

Para saber más sobre cómo puedes aprovechar esta matriz, consulta nuestro curso de Braze Learning sobre [Comprender la matriz de mensajería](https://learning.braze.com/understand-the-messaging-matrix).

<br><br>
