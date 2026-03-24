---
nav_title: Reelegibilidad
article_title: Reelegibilidad
page_order: 10
page_type: reference
description: "Este artículo de referencia define la reelegibilidad para campañas y Canvases."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Reelegibilidad para campañas y Canvas

> Cuando programas una campaña recurrente o desencadenada, o un Canvas, tienes la opción de permitir que los usuarios vuelvan a ser elegibles para ella. La reelegibilidad significa que los usuarios pueden participar en la campaña o Canvas varias veces en función del desencadenante.

## Cómo funciona

De forma predeterminada, Braze envía un mensaje a un usuario solo una vez, incluso si re-califica varias veces, ya que la re-elegibilidad debe activarse por separado. Una vez activada, los miembros cualificados podrán volver a recibir mensajes después de haber recibido la primera instancia de la campaña o Canvas. Puede indicar el plazo en el que los usuarios volverían a ser elegibles en última instancia.

## Activación de la reelección para personas elegibles

{% tabs local %}
{% tab campaign %}
Para activar la reelegibilidad de una campaña, seleccione la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la sección **Controles de entrega**. El plazo máximo para volver a ser elegible para una campaña es de 720 días.

En el caso de las campañas activadas con la reelegibilidad activada, los usuarios que [no hayan recibido realmente el mensaje de la campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (a pesar de haber completado el evento desencadenante) se clasificarán automáticamente para recibir el mensaje la próxima vez que completen el evento desencadenante. Esto se debe a que la reelegibilidad se basa en la recepción del mensaje y no en la entrada en la campaña. Al hacer que los usuarios vuelvan a ser elegibles para una campaña activada, les permite recibir realmente (y no simplemente activar) el mensaje más de una vez.

Además, si intentas enviar un mensaje inmediatamente con una reelegibilidad de cero minutos, siempre intentaremos programarlo de inmediato, independientemente de cómo haya recibido los versiones anteriores de la campaña o Canvas el usuario.

#### Reelegibilidad con campañas desencadenadas por la API

El número de veces que un usuario recibe una campaña activada por la API puede limitarse mediante la configuración de la reelegibilidad. Esto significa que el usuario recibirá la campaña sólo una vez o una vez en una ventana determinada, independientemente de cuántas veces se dispare el activador de la API.

Por ejemplo, supongamos que utilizas una campaña desencadenada por API para enviar al usuario una campaña sobre un artículo que ha visto recientemente. En este caso, puedes limitar la campaña para enviar hasta un mensaje al día, independientemente del número de elementos que hayan visto, mientras se desencadena el disparador de la API para cada elemento. Por otro lado, si su campaña activada por API es transaccional, querrá asegurarse de que el usuario recibe la campaña cada vez que realiza la transacción estableciendo el retraso en cero minutos.
{% endtab %}

{% tab canvas %}

Para activar la posibilidad de volver a participar en un Canvas, selecciona **Permitir a los usuarios volver a entrar en este Canvas** en la sección **Controles de entrada**. Puedes elegir entre permitir que los usuarios vuelvan a entrar después de la duración máxima del Canvas o después de un intervalo de tiempo específico.

La posibilidad de volver a optar a las variantes de Canvas está vinculada a la entrada en Canvas y no a la recepción del mensaje. Los usuarios que entren en un lienzo y no reciban ningún mensaje no podrán volver a entrar en el lienzo a menos que se active la reelección.

Ten en cuenta que el usuario no necesita salir primero de Canvas para volver a entrar si la reelegibilidad se establece en cero segundos, lo que significa que el usuario puede volver a entrar en el mismo Canvas. Como otro ejemplo, si la duración del Canvas se establece en 7 días y el período de reelegibilidad se establece en 3 días, un usuario puede volver a entrar en el Canvas antes de completar tu primer recorrido por él.

Puedes añadir filtros adicionales para evitar que los usuarios reciban el mismo paso o mensaje varias veces. Sin embargo, cuando un usuario vuelve a entrar en un Canvas por segunda vez, los pasos que recibisteis la primera vez que entrasteis en el Canvas no son visibles para ti. Esto significa que el usuario puede seguir recibiendo el mismo mensaje. Para evitarlo, puedes configurar Canvas para impedir la reentrada o establecer la reelegibilidad para la duración máxima de Canvas.

También puedes utilizar un [paso de actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) para que el usuario que recibe el paso lo registre como un atributo personalizado, que se puede utilizar para filtrar a los usuarios que han recibido el paso durante su recorrido por Canvas.

### Ejemplo

Por ejemplo, supongamos que un usuario sin dirección de correo electrónico entra en un Canvas recurrente diario que contiene un paso en el recorrido del usuario. Este paso solo contiene un mensaje de correo electrónico, por lo que no se obtiene la interacción del usuario. Este usuario no podrá volver a entrar en Canvas a menos que se active la reelegibilidad en Canvas. 

Si tiene un lienzo activo recurrente o activado sin reelegibilidad, y desea que los usuarios vuelvan a entrar en el lienzo hasta que reciban un mensaje del mismo, puede considerar permitir que los usuarios vuelvan a ser elegibles para la entrada añadiendo un filtro a los criterios de entrada que excluya a los clientes que han recibido un mensaje del lienzo.

Si la reelegibilidad para un lienzo es inferior a la duración del lienzo, es posible que los usuarios entren en el lienzo más de una vez, lo que puede dar lugar a un comportamiento engañoso para los lienzos que utilizan mensajes dentro de la aplicación con retrasos especialmente largos. Dado que una misma sesión iniciada puede desencadenar varios mensajes dentro de la aplicación Canvas, es posible que el usuario reciba el mismo mensaje repetidamente si un componente específico se renderiza más rápido que otros.
{% endtab %}
{% endtabs %}

## Cálculo del plazo de readmisión

La reelegibilidad tanto para las campañas como para los lienzos se calcula en segundos, no en días del calendario. Esto significa que un día cuenta como 24 horas (u 86.400 segundos) a partir del momento en que el usuario recibe el mensaje, no como el siguiente día natural a medianoche. Del mismo modo, un mes cuenta exactamente como 2 592 000 segundos, lo que equivale aproximadamente a 30 días.

### Ejemplo

Considera el siguiente escenario:

* Se ha configurado una campaña para que se envíe mensualmente el día 15, con la posibilidad de volver a ser elegible establecida en 30 días.
* Hay menos de 30 días entre el 15 de febrero y el 15 de marzo. 

Esto significa que los usuarios que recibieron la campaña el 15 de febrero no podrán optar a la campaña que se enviará el 15 de marzo. Si la campaña está configurada para enviarse diariamente a las 8:00 a. m. con una reelegibilidad de 1 día, y hay una latencia en el envío del mensaje, los usuarios que recibieron la campaña a las 8:30 a. m. no serán elegibles al día siguiente a las 8:00 a. m.

## Pruebas multivariantes

Para las pruebas multivariante, Braze determina la reelegibilidad de las variantes para todas las campañas, los mensajes dentro de la aplicación desencadenados y los lienzos utilizando las siguientes reglas:

- Cuando los porcentajes de las variantes no se modifican, cada usuario introducirá siempre la misma variante de una campaña, mensaje in-app activado o entrada de Canvas cada vez que vuelva a ser elegible.
- Si los porcentajes de variantes cambian, los usuarios pueden redistribuirse a otras variantes.
- Los grupos de control seguirán siendo coherentes si el porcentaje de variantes no varía, y ningún usuario que haya recibido mensajes anteriormente entrará en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibirá nunca un mensaje.
