---
nav_title: "Listas de correo electrónico y direcciones"
article_title: Puntos finales de listas y direcciones de correo electrónico
search_tag: Endpoint
page_order: 1
layout: dev_guide

description: "Esta página de inicio explica y enumera los puntos finales de listas de correo electrónico y direcciones de Braze."
page_type: landing

guide_top_header: "Puntos finales de listas y direcciones de correo electrónico"
guide_top_text: "Usando este conjunto de puntos finales, puedes actualizar el estado de suscripción de correo electrónico de un usuario y utilizar la API de Braze para configurar la sincronización bidireccional entre Braze y otros sistemas de correo electrónico o tu propia base de datos."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: Enumerar rebotes duros"
    link: /docs/api/endpoints/email/get_list_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Consultar direcciones de correo electrónico con suscripción cancelada"
    link: /docs/api/endpoints/email/get_query_unsubscribed_email_addresses/
    image: /assets/img/braze_icons/mail-01.svg
  - name: "POST: Cambiar el estado de suscripción de correo electrónico"
    link: /docs/api/endpoints/email/post_email_subscription_status/
    image: /assets/img/braze_icons/at-sign.svg
  - name: "POST: Quitar rebotes duros"
    link: /docs/api/endpoints/email/post_remove_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "POST: Quitar correo no deseado"
    link: /docs/api/endpoints/email/post_remove_spam/
    image: /assets/img/braze_icons/mail-04.svg
  - name: "POST: Añadir correo electrónico a la lista de bloqueo"
    link: /docs/api/endpoints/email/post_blocklist/
    image: /assets/img/braze_icons/mail-04.svg
---
{% comment %}
redirigir desde email_sync.md
{% endcomment %}