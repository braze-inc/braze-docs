---
nav_title: Filtro de canal
article_title: Filtro Intelligent Channel
page_order: 1.5
description: "Este artículo describe el filtro Intelligent Channel, que selecciona la parte de tu audiencia para la cual el canal de mensajería seleccionado es su canal \"mejor\". Aquí, \"mejor\" significa la mayor probabilidad de interacción según el historial del usuario."
search_rank: 11
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtro Intelligent Channel

> El filtro **Intelligent Channel** (anteriormente **Most Engaged**) selecciona la parte de tu audiencia para la cual el canal de mensajería seleccionado es su canal \"mejor\".

## Acerca del filtro de canal

![El filtro Intelligent Channel con un menú desplegable de los distintos canales que se pueden seleccionar.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Aquí, \"mejor\" significa el canal con la mayor probabilidad de interacción según el historial del usuario. Puedes seleccionar correo electrónico, SMS, WhatsApp, push web o push móvil (incluido cualquier OS o dispositivo móvil disponible) como canal.

Intelligent Channel calcula la tasa de interacción por usuario y por canal tomando la ratio de interacciones con mensajes (aperturas o clics) al número de mensajes recibidos en los últimos seis meses. Los canales se clasifican según sus ratios de interacción y el canal con la ratio más alta es el \"Most Engaged\" para ese usuario.

Cada vez que se envía un mensaje a un usuario o un usuario interactúa con un mensaje, la tasa de interacción se recalcula en segundos. Un usuario solo puede contarse como interactuando con un mensaje una vez (por ejemplo, abrir y hacer clic en el mismo correo electrónico cuenta como una sola interacción).

Para activar el filtro Intelligent Channel, selecciona el filtro **Intelligent Channel** en la página **Audiencias objetivo** al crear una campaña de correo electrónico, push web o push móvil.

{% alert important %}
Para calcular la tasa de interacción del canal SMS, activa el [acortamiento de enlaces SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) con seguimiento avanzado y de clics. Sin este seguimiento, el SMS puede seleccionarse como Intelligent Channel con una tasa de interacción del 0 % debido a nuestro [comportamiento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#tie-breaking).
{% endalert %}

## Opción \"Datos insuficientes\"

Para que Braze determine qué canal es \"mejor\", hacen falta suficientes datos: un usuario debe haber recibido al menos tres mensajes por canal en al menos dos de los tres canales disponibles (no es necesario que los mensajes se hayan abierto).

Los usuarios que no han recibido suficientes mensajes en los canales entrarán en la opción \"Datos insuficientes\" de este filtro. Puedes usar cualquiera de los tres canales para dirigirte a estos usuarios.

Por ejemplo, para enviar push a usuarios que prefieren push y el mismo push a usuarios sin suficientes datos: configura el filtro Intelligent Channel en **Push móvil** y añade con **OR** un segundo filtro Intelligent Channel configurado en **Datos insuficientes**. Una campaña separada con el filtro Intelligent Channel en **correo electrónico** puede dirigirse a usuarios que prefieren correo electrónico.

![Filtros Intelligent Channel para push móvil o datos insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Las campañas y pasos de Canvas que ignoran la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) no se tienen en cuenta para Intelligent Channel y no contribuyen a los requisitos de datos.
{% endalert %}

Para buenas prácticas sobre desempate, canales inalcanzables y tamaño de audiencia, consulta la versión completa de este artículo en el índice de la izquierda o la ayuda del dashboard de Braze.
