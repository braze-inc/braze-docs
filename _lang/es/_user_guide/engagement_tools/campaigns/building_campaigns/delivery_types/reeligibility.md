---
nav_title: Reelegibilidad para campañas y Canvas
article_title: Reelegibilidad para campañas y Canvas
page_order: 3
page_type: reference
description: "Este artículo de referencia ofrece una visión general de lo que significa permitir que los usuarios vuelvan a ser elegibles para recibir o volver a entrar en una campaña o Canvas."
tool:
  - Campaigns
  - Canvas

---

# Reelegibilidad para campañas y Canvas

> Siempre que programe una campaña o lienzo recurrente o activado, tiene la opción de permitir que los usuarios vuelvan a ser elegibles para ella (de modo que los usuarios puedan entrar en la campaña o lienzo varias veces en función del activador). Por defecto, Braze envía un mensaje a un usuario una sola vez, incluso si se recalifica varias veces, ya que la recalificación debe activarse por separado. 

Si activa la reelegibilidad, anulará este comportamiento predeterminado y permitirá que los miembros cualificados vuelvan a recibir mensajes después de haber recibido la primera instancia de la campaña o Canvas. Puede indicar el plazo en el que los usuarios volverían a ser elegibles en última instancia.

## Canvas

Para activar la reintroducción en un Canvas, marque **Permitir a los usuarios reintroducir este Canvas** en la sección **Controles de entrada**. Puede elegir entre permitir a los usuarios volver a entrar después de la duración máxima del lienzo, o después de una ventana especificada.

![Controles de entrada][2]

La posibilidad de volver a optar a las variantes de Canvas está vinculada a la entrada en Canvas y no a la recepción del mensaje. Los usuarios que entren en un lienzo y no reciban ningún mensaje no podrán volver a entrar en el lienzo a menos que se active la reelección. 

Por ejemplo, supongamos que un usuario sin dirección de correo electrónico entra en un Canvas recurrente diario que contiene un paso en el recorrido del usuario. El componente Canvas sólo contiene un mensaje de correo electrónico, por lo que el usuario no recibe el compromiso. Este usuario no podrá volver a entrar en el Lienzo a menos que el Lienzo tenga activada la re-elegibilidad. Si tiene un lienzo activo recurrente o activado sin reelegibilidad, y desea que los usuarios vuelvan a entrar en el lienzo hasta que reciban un mensaje del mismo, puede considerar permitir que los usuarios vuelvan a ser elegibles para la entrada añadiendo un filtro a los criterios de entrada que excluya a los clientes que han recibido un mensaje del lienzo.

Si la reelegibilidad para un lienzo es inferior a la duración del lienzo, es posible que los usuarios entren en el lienzo más de una vez, lo que puede dar lugar a un comportamiento engañoso para los lienzos que utilizan mensajes dentro de la aplicación con retrasos especialmente largos. Dado que varios mensajes dentro de la aplicación en Canvas podrían desencadenarse con el mismo inicio de sesión, el usuario podría tener la experiencia de recibir el mismo mensaje repetidamente, si un componente específico se presenta más rápido que otros.

## Campañas

Para activar la reelegibilidad de una campaña, seleccione la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la sección **Controles de entrega**. El plazo máximo para volver a ser elegible para una campaña es de 720 días.

![][1]

En el caso de las campañas activadas con la opción de reelegibilidad activada, los usuarios que [no hayan recibido el mensaje de la campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (a pesar de haber completado el evento de activación) recibirán automáticamente el mensaje la próxima vez que completen el evento de activación, incluso si no ha hecho que los usuarios vuelvan a ser elegibles. Esto se debe a que la reelegibilidad se basa en la recepción del mensaje y no en la entrada en la campaña. Al hacer que los usuarios vuelvan a ser elegibles para una campaña activada, les permite recibir realmente (y no simplemente activar) el mensaje más de una vez.

Además, si está intentando enviar un mensaje de forma inmediata con una reelegibilidad de cero minutos, siempre intentaremos programarlo de inmediato, independientemente de cómo haya recibido el usuario las versiones anteriores de la campaña o Canvas.

![][24]

## Cálculo del plazo de readmisión

La reelegibilidad tanto de las campañas como de los lienzos se calcula en segundos, no en días naturales. Esto significa que un día cuenta como 24 horas (u 86.400 segundos) a partir del momento en que el usuario recibe el mensaje, no como el siguiente día natural a medianoche.

Del mismo modo, un mes cuenta exactamente como 2 592 000 segundos, lo que equivale aproximadamente a 30 días.

### Caso de uso

Considera el siguiente escenario:
* Se ha configurado una campaña para que se envíe mensualmente el día 15, con la posibilidad de volver a ser elegible establecida en 30 días.
* Hay menos de 30 días entre el 15 de febrero y el 15 de marzo. 

Esto significa que los usuarios que recibieron la campaña el 15 de febrero no podrán optar a la campaña que se enviará el 15 de marzo.

Si la campaña está configurada para que se envíe diariamente a las 8 de la mañana con un plazo de reelección de 1 día y hay una latencia en el envío del mensaje, los usuarios que hayan recibido la campaña a las 8:30 de la mañana, por ejemplo, aún no serán reelegibles al día siguiente a las 8 de la mañana.

## Pruebas multivariantes

En lo que respecta a las pruebas multivariantes, Braze determina la reelegibilidad de variantes para todas las campañas, mensajes activados en la aplicación y lienzos utilizando las siguientes reglas:

- Cuando los porcentajes de las variantes no se modifican, cada usuario introducirá siempre la misma variante de una campaña, mensaje in-app activado o entrada de Canvas cada vez que vuelva a ser elegible.
- Si los porcentajes de variantes cambian, los usuarios pueden redistribuirse a otras variantes.
- Los grupos de control seguirán siendo coherentes si el porcentaje de variantes no varía, y ningún usuario que haya recibido mensajes anteriormente entrará en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibirá nunca un mensaje.

[1]: {% image_buster /assets/img_archive/reeligibility_controls_campaign.png %}
[2]: {% image_buster /assets/img_archive/reeligibility_controls_canvas.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
