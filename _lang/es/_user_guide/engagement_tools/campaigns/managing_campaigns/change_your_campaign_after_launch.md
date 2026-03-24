---
nav_title: Edita tu campaña después de su lanzamiento
article_title: Edita tu campaña después del lanzamiento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artículo de referencia ofrece una visión general del resultado de editar determinados aspectos de una campaña tras su lanzamiento."

---

# Edita tu campaña después de su lanzamiento

> Este artículo ofrece una visión general del resultado de editar ciertos aspectos de una campaña tras su lanzamiento.

## Detener tu campaña

Para detener una campaña, abre la página **Detalles de la campaña** y selecciona **Detener campaña**. Cuando se detiene una campaña:

- Los mensajes programados para ser enviados serán cancelados.
- Las pruebas A/B en las que ya se haya enviado la prueba inicial se cancelarán de forma permanente.
- Los eventos relacionados con mensajes que ya se han enviado (por ejemplo, clics de apertura) seguirán siendo objeto de seguimiento.

Para reiniciar tu campaña, selecciona **Reanudar**. Tu campaña seguirá enviando mensajes y pruebas A/B, pero los mensajes no entregados no se volverán a enviar ni se reprogramarán.

## Campañas activadas

Todos los cambios en las campañas de entrega basadas en acciones y en las campañas de entrega activadas por API surten efecto inmediatamente en los envíos futuros. 

Si estas campañas se han desencadenado pero aún no se han enviado (por ejemplo, una campaña de entrega basada en acciones con un retraso de 1 día se edita durante el periodo de retraso de 1 día), consulta las siguientes instrucciones para campañas programadas.

### Campañas programadas

Si necesita realizar cambios en una campaña después de su lanzamiento, tenga en cuenta los siguientes puntos cuando edite su campaña para comprobar que sus cambios tienen los efectos deseados.

### Contenido del mensaje

Cualquier cambio en el contenido de los mensajes (incluidos los títulos, los cuerpos y las imágenes) se aplica inmediatamente al guardarlos para todos los mensajes que se envíen en adelante. No es posible modificar el contenido de los mensajes que ya han sido enviados.

### Programación y audiencia

Si modifica la hora de envío programada de su campaña o su público, esos cambios se reflejarán inmediatamente en la campaña real.

#### Consideraciones

Si tu campaña utiliza la función Intelligent Timing o la entrega según la zona horaria local, los cambios realizados en la hora de envío programada no se reflejarán si se realizan en las 24 horas anteriores a la hora de envío original. Esto se debe a que:

- **Intelligent Timing** Braze comienza a calcular la hora óptima de envío a medianoche, hora de Samoa. Si este tiempo ya ha transcurrido, el mensaje habrá comenzado a procesarse. Para obtener más información, consulta [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Entrega según la zona horaria local:** La edición de una campaña de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Para obtener más información, consulta [¿Cómo programo una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign) con [zona horaria local?]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign)

### Tasa de envío

Cuando se utiliza un límite de velocidad de envío, Braze "programa" los mensajes en franjas horarias de minutos, por lo que si desea cambiar la velocidad de envío de mensajes, siga el siguiente proceso para realizar cambios inmediatos.

## Hacer cambios inmediatos

Si necesitas que los cambios surtan efecto inmediatamente, haz lo siguiente:

1. Detener la campaña de afectados.
2. Duplica la campaña.
3. Edite la campaña duplicada.

{% alert important %}
Esto restablece la elegibilidad de las personas que ya recibieron la campaña original, por lo que es posible que tenga que filtrar la campaña duplicada para las personas que no recibieron la original.
{% endalert %}

## Guardar borradores de campañas activas {#campaign-drafts}

Los borradores son ideales para realizar cambios a gran escala en campañas activas. Al crear un borrador, puedes probar los cambios planificados antes del próximo lanzamiento.

{% alert note %}
Una campaña sólo puede tener un borrador a la vez. Además, los análisis no están disponibles, ya que los cambios propuestos aún no se han implementado.
{% endalert %}

Para crear un borrador, haz lo siguiente

1. Ve a tu campaña activa.
2. Haz tus cambios.
3. Selecciona **Guardar como borrador**. Ten en cuenta que, después de crear un borrador, no podrás editar la campaña activa hasta que la lances o la descartes.

![Un borrador de una campaña activa con una opción para ver la campaña activa.]({% image_buster /assets/img/campaign_draft.png %})

Mientras editas el borrador, también puedes consultar la campaña activa en el encabezado del borrador de la campaña o en el pie de página de los análisis de la campaña. 

Para volver a una campaña activa, selecciona **Editar borrador** en la vista de análisis o en la vista de campaña activa.

### Priorización de mensajes dentro de la aplicación

La prioridad de los mensajes dentro de la aplicación se actualizará inmediatamente (antes de que se lance el borrador) cuando selecciones **Establecer prioridad exacta** y especifiques la prioridad en relación con otras campañas o Lienzos.
