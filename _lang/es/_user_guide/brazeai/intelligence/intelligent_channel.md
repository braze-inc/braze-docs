---
nav_title: Filtro de canal
article_title: Filtro de canal inteligente
page_order: 1.5
description: "Este artículo cubre el filtro El canal inteligente, un filtro que selecciona la parte de tu audiencia para la que el canal de mensajería seleccionado es su mejor canal. En este caso, el mejor medio tiene la mayor probabilidad de interacción, dado el historial del usuario."
search_rank: 11
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtro de canal inteligente

> El filtro `Intelligent Channel` (antes `Most Engaged`) selecciona la parte de tu audiencia para la que el canal de mensajería seleccionado es su "mejor" canal. 

## Acerca del filtro de canales

\![El filtro Canal inteligente con un desplegable para los distintos canales que se pueden seleccionar.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

En este caso, mejor significa el canal que tiene la mayor probabilidad de interacción, dado el historial del usuario. Puedes seleccionar como canal correo electrónico, SMS, WhatsApp, web push o mobile push (incluyendo cualquier SO o dispositivo móvil disponible).

El canal inteligente calcula la tasa de interacción de cada usuario para cada uno de los tres canales, tomando la relación entre las interacciones de los mensajes (aperturas o clics) y el número de mensajes recibidos en los últimos seis meses de actividad. Los canales disponibles se clasifican según sus respectivos ratios de interacción, y el canal con el ratio más alto es el "Más interactuado" para ese usuario. 

Cada vez que se envía un mensaje a un usuario, o un usuario interactúa con un mensaje, el ratio de interacción se recalcula en cuestión de segundos. Un usuario sólo puede ser contabilizado como que ha interactuado con un mensaje una vez (por ejemplo, una apertura y un clic en el mismo correo electrónico hará que ese mensaje sea marcado como que ha interactuado con él sólo una vez, no dos). 

Para habilitar el filtro de canal inteligente, selecciona el filtro de **canal** inteligente en la página **Audiencias objetivo** al crear una campaña de correo electrónico, push web o push móvil.

{% alert important %}
Para calcular la tasa de interacción del canal SMS, activa [el acortamiento de enlaces SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) con seguimiento avanzado y seguimiento de clics. Sin este seguimiento, el SMS puede ser seleccionado como canal inteligente para una tasa de interacción del 0% debido a nuestro [comportamiento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## La opción "Datos insuficientes

Para que Braze determine qué canal es "el mejor", tiene que haber datos suficientes. Esto significa que un usuario debe haber recibido al menos tres o más mensajes por canal a través de al menos dos de los tres canales disponibles. No es necesario que los mensajes se hayan abierto. 

Si los usuarios no han recibido suficientes mensajes a través de los canales, esos usuarios entrarán en la opción "Datos insuficientes" de este filtro. Esto te permite utilizar cualquiera de los tres canales de mensajería disponibles para dirigirte a estos usuarios.

Por ejemplo, supongamos que quieres que los usuarios que prefieren los mensajes push reciban un push y que los usuarios que no tienen suficientes datos reciban el mismo mensaje push. En ese caso, podrías establecer el filtro de canal inteligente en **Push móvil** y utilizar **OR** para añadir un segundo filtro de canal inteligente establecido en **Datos insuficientes**. Una campaña independiente con el filtro de canal inteligente ajustado a correo electrónico podría dirigirse a los usuarios que prefieren el correo electrónico.

\![Los canales inteligentes filtran los datos móviles push o insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Las campañas y los pasos en Canvas que ignoren la [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) no serán tenidos en cuenta por el canal inteligente y no podrán contribuir a los requisitos de datos.
{% endalert %}

## La opción "Mobile push

El push móvil incorpora Android, iOS, Kindle y otros canales de dispositivos móviles disponibles en Braze. Al calcular el canal inteligente, Braze examina cada tipo de dispositivo móvil por separado y luego elige la tasa de interacción más alta entre ellos para representar la categoría "Mobile Push" al compararla con el correo electrónico y el push Web. 

Por ejemplo, si un usuario tiene varios dispositivos móviles, su tasa de interacción móvil estaría representada por la tasa más alta mostrada en todos los dispositivos. Sin embargo, esto no obligaría al usuario a recibir notificaciones push exclusivamente en ese dispositivo. Esta tasa sólo se utiliza cuando se comparan las tasas contra el correo electrónico y la notificación push web.

## Canales individuales

En lugar de dejar que Braze elija el mejor canal para un usuario, también puedes filtrar simplemente a los usuarios en función de si es probable o no que abran un mensaje en un canal específico que elijas. Para ello puedes utilizar el filtro Probabilidad de apertura de mensajes en [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Mejores prácticas y estrategia de uso eficaz

### Desempate

Como algunos usuarios recibirán pocos mensajes, no es raro que haya empates en las tasas de interacción entre los canales disponibles para un usuario determinado (por ejemplo, un solo usuario tiene una tasa de interacción de 0,2 **tanto** para el correo electrónico como para el push móvil). En tales casos, los empates se desharán dando prioridad (otorgando una clasificación más alta) al canal con los eventos abiertos más recientes.

### Canales inalcanzables

Cuando el usuario tiene datos suficientes para que se determine una clasificación, pero se vuelve ilocalizable en su canal de mayor interacción, el usuario se "caerá" y no recibirá ningún mensaje. Los usuarios que no son localizables en canales específicos deben ser objeto de un tratamiento separado.

### Dimensionamiento de la audiencia

El canal inteligente te permite dirigirte selectivamente y por adelantado a la fracción de usuarios que tienen muchas más probabilidades de interactuar con un mensaje que el resto de tu audiencia. No es probable que represente a la mayoría de los usuarios de una audiencia típica. Más bien, puedes esperar que este filtro encuentre el 5-20% de tu audiencia habitual que tiene un historial establecido de interacción en un canal concreto.


