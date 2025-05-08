---
nav_title: Reelegibilidad
article_title: Reelegibilidad
page_order: 8
page_type: reference
description: "Este artículo de referencia define la reelegibilidad para campañas y Lonas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Reelegibilidad para campañas y Canvas

> Cuando programes una campaña recurrente o desencadenada o Canvas, tienes la opción de permitir que los usuarios vuelvan a ser elegibles para ella. Volver a ser elegible significa que los usuarios pueden entrar en la campaña o en el Canvas varias veces en función del desencadenante.

## Cómo funciona

Por defecto, Braze envía un mensaje a un usuario sólo una vez, aunque se vuelva a clasificar varias veces, ya que la nueva elegibilidad debe activarse por separado. Una vez activada, los miembros cualificados podrán volver a recibir mensajes después de haber recibido la primera instancia de la campaña o Canvas. Puede indicar el plazo en el que los usuarios volverían a ser elegibles en última instancia.

## Volver a ser elegible

{% tabs local %}
{% tab campaña %}
Para activar la reelegibilidad de una campaña, seleccione la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la sección **Controles de entrega**. El plazo máximo para volver a ser elegible para una campaña es de 720 días.

En las campañas desencadenadas con la reelección activada, los usuarios que [no hayan recibido realmente el mensaje de la campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (a pesar de haber completado el evento desencadenante) se clasificarán automáticamente para recibir el mensaje la próxima vez que completen el evento desencadenante. Esto se debe a que la reelegibilidad se basa en la recepción del mensaje y no en la entrada en la campaña. Al hacer que los usuarios vuelvan a ser elegibles para una campaña activada, les permite recibir realmente (y no simplemente activar) el mensaje más de una vez.

Además, si intentas enviar un mensaje inmediatamente con una elegibilidad de cero minutos, siempre intentaremos programarlo de inmediato, independientemente de cómo haya recibido el usuario las versiones anteriores de la campaña o del Canvas.

#### Reelegibilidad con campañas desencadenadas por la API

El número de veces que un usuario recibe una campaña activada por la API puede limitarse mediante la configuración de la reelegibilidad. Esto significa que el usuario recibirá la campaña sólo una vez o una vez en una ventana determinada, independientemente de cuántas veces se dispare el activador de la API.

Por ejemplo, supongamos que utilizas una campaña desencadenada por la API para enviar al usuario una campaña sobre un artículo que ha visto recientemente. En este caso, puede limitar la campaña para que envíe un máximo de un mensaje al día, independientemente del número de artículos que hayan visto, a la vez que dispara el activador de la API para cada artículo. Por otro lado, si su campaña activada por API es transaccional, querrá asegurarse de que el usuario recibe la campaña cada vez que realiza la transacción estableciendo el retraso en cero minutos.
{% endtab %}

{% tab Canvas %}
Para activar la **reintroducción** en un Canvas, selecciona **Permitir a los usuarios reintroducir este Canvas** en la sección **Controles de entrada**. Puede elegir entre permitir a los usuarios volver a entrar después de la duración máxima del lienzo, o después de una ventana especificada.

La posibilidad de volver a optar a las variantes de Canvas está vinculada a la entrada en Canvas y no a la recepción del mensaje. Los usuarios que entren en un lienzo y no reciban ningún mensaje no podrán volver a entrar en el lienzo a menos que se active la reelección.

### Ejemplo

Por ejemplo, supongamos que un usuario sin dirección de correo electrónico entra en un Canvas recurrente diario que contiene un paso en el recorrido del usuario. Este paso sólo contiene un mensaje de correo electrónico, por lo que el usuario no recibe la interacción. Este usuario no podrá volver a entrar en el Canvas a menos que el Canvas tenga activada la reelegibilidad. 

Si tiene un lienzo activo recurrente o activado sin reelegibilidad, y desea que los usuarios vuelvan a entrar en el lienzo hasta que reciban un mensaje del mismo, puede considerar permitir que los usuarios vuelvan a ser elegibles para la entrada añadiendo un filtro a los criterios de entrada que excluya a los clientes que han recibido un mensaje del lienzo.

Si la reelegibilidad para un lienzo es inferior a la duración del lienzo, es posible que los usuarios entren en el lienzo más de una vez, lo que puede dar lugar a un comportamiento engañoso para los lienzos que utilizan mensajes dentro de la aplicación con retrasos especialmente largos. Dado que varios mensajes dentro de la aplicación en Canvas podrían desencadenarse con el mismo inicio de sesión, el usuario podría tener la experiencia de recibir el mismo mensaje repetidamente, si un componente específico se presenta más rápido que otros.
{% endtab %}
{% endtabs %}

## Cálculo del plazo de readmisión

La reelegibilidad tanto de las campañas como de los lienzos se calcula en segundos, no en días naturales. Esto significa que un día cuenta como 24 horas (u 86.400 segundos) a partir del momento en que el usuario recibe el mensaje, no como el siguiente día natural a medianoche. Del mismo modo, un mes cuenta exactamente como 2 592 000 segundos, lo que equivale aproximadamente a 30 días.

### Ejemplo

Considera el siguiente escenario:

* Se ha configurado una campaña para que se envíe mensualmente el día 15, con la posibilidad de volver a ser elegible establecida en 30 días.
* Hay menos de 30 días entre el 15 de febrero y el 15 de marzo. 

Esto significa que los usuarios que recibieron la campaña el 15 de febrero no podrán optar a la campaña que se enviará el 15 de marzo. Si la campaña está configurada para que se envíe diariamente a las 8 de la mañana con una reelegibilidad de 1 día y hay una latencia en el envío del mensaje, los usuarios que recibieron la campaña a las 8:30 de la mañana aún no serán elegibles al día siguiente a las 8 de la mañana.

## Pruebas multivariantes

Para las pruebas multivariantes, Braze determina la reelegibilidad de las variantes para todas las campañas, mensajes dentro de la aplicación desencadenados y Lienzos utilizando las siguientes reglas:

- Cuando los porcentajes de las variantes no se modifican, cada usuario introducirá siempre la misma variante de una campaña, mensaje in-app activado o entrada de Canvas cada vez que vuelva a ser elegible.
- Si los porcentajes de variantes cambian, los usuarios pueden redistribuirse a otras variantes.
- Los grupos de control seguirán siendo coherentes si el porcentaje de variantes no varía, y ningún usuario que haya recibido mensajes anteriormente entrará en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibirá nunca un mensaje.

