---
nav_title: Trampas de capacidad de entrega y trampas de correo no deseado
article_title: Trampas de capacidad de entrega y trampas de correo no deseado
page_order: 7
page_type: reference
description: "Este artículo de referencia trata de las posibles trampas de la capacidad de entrega del correo electrónico, las trampas del correo no deseado y cómo evitarlas."
channel: email

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Trampas de capacidad de entrega y correo no deseado

La capacidad de entrega de tu correo electrónico puede verse afectada por alguna de las siguientes trampas de correo no deseado:

| Tipo de trampa | Descripción |
|---|---|
| Trampas Prístinas | Direcciones de correo electrónico y dominios que nunca se han utilizado. |
| Trampas recicladas | Direcciones de correo electrónico que originalmente eran usuarios reales, pero que ahora están inactivas. |
| Trampas tipográficas | Direcciones de correo electrónico que contienen erratas comunes. |
| Quejas por correo no deseado | Cuando tu correo electrónico es marcado como correo no deseado por un cliente. |
| Alta tasa de rebote | Cuando tu correo electrónico falla sistemáticamente al entregarlo porque la dirección del destinatario no es válida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cómo evitar las trampas de correo no deseado

Estas trampas pueden evitarse si estableces un proceso de adhesión voluntaria confirmada. Al enviar un correo electrónico de adhesión voluntaria inicial y pedir a los clientes que verifiquen que quieren tus mensajes, te aseguras de que tus destinatarios quieren saber de ti y de que estás enviando a direcciones reales y válidas. Aquí tienes otras formas de evitar las trampas de correo no deseado:

1. Envía un correo electrónico de doble adhesión voluntaria. Se trata de un correo electrónico que pedirá a los usuarios que confirmen sus opciones de suscripción haciendo clic en un enlace.
2. Como mejor práctica, aplica una [política de extinción]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).
3. **Nunca compres listas de correo electrónico.** 

{% alert tip %}
Los equipos de éxito del cliente y capacidad de entrega de Braze pueden ayudarte a asegurarte de que sigues las mejores prácticas para maximizar la capacidad de entrega en todo el mundo.
{% endalert %}

## Eliminar una dirección de correo electrónico de tu lista de correo no deseado o rebotado

Puedes eliminar los correos electrónicos rebotados y los correos de tu lista de correo no deseado de Braze con los siguientes puntos finales:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)