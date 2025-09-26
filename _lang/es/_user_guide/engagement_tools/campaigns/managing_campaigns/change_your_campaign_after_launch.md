---
nav_title: Editar la campaña después del lanzamiento
article_title: Editar la campaña después del lanzamiento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artículo de referencia ofrece una visión general del resultado de editar determinados aspectos de una campaña tras su lanzamiento."

---

# Editar la campaña después del lanzamiento

> Este artículo ofrece una visión general del resultado de editar ciertos aspectos de una campaña tras su lanzamiento.

## Detener tu campaña

Para detener una campaña, abre tu página **Detalles de campaña** y selecciona **Detener campaña**. Cuando se detiene una campaña:

- Los mensajes programados para ser enviados serán cancelados.
- Las pruebas A/B en las que ya se haya enviado la prueba inicial se cancelarán permanentemente.
- Los eventos de los mensajes que ya se han enviado (por ejemplo, los clics de apertura) seguirán siendo objeto de seguimiento.

Para reiniciar tu campaña, selecciona **Reanudar**. Tu campaña seguirá enviando mensajes y pruebas A/B, pero los mensajes perdidos no se volverán a enviar ni a programar.

## Campañas activadas

Todos los cambios en las campañas de entrega basada en acciones y en las campañas de entrega desencadenadas por la API entran en vigor inmediatamente para los envíos en adelante. 

Si estas campañas se han desencadenado pero aún no se han enviado (por ejemplo, una campaña de entrega basada en acciones con un retraso de 1 día se edita durante el periodo de retraso de 1 día), consulta la siguiente guía para campañas programadas.

### Campañas programadas

Si necesita realizar cambios en una campaña después de su lanzamiento, tenga en cuenta los siguientes puntos cuando edite su campaña para comprobar que sus cambios tienen los efectos deseados.

### Contenido del mensaje

Cualquier cambio en el contenido de los mensajes (incluidos títulos, cuerpos e imágenes) surtirá efecto inmediatamente al guardarlos para todos los envíos de mensajes en adelante. No es posible modificar el contenido de los mensajes que ya han sido enviados.

### Programación y audiencia

Si modifica la hora de envío programada de su campaña o su público, esos cambios se reflejarán inmediatamente en la campaña real.

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

Los borradores son estupendos para hacer cambios a gran escala en campañas activas. Al crear un borrador, puedes pilotar los cambios previstos antes de tu próximo lanzamiento.

{% alert note %}
Una campaña sólo puede tener un borrador a la vez. Además, los análisis no están disponibles, ya que los cambios redactados aún no se han puesto en marcha.
{% endalert %}

Para crear un borrador, haz lo siguiente

1. Ve a tu campaña activa.
2. Haz tus cambios.
3. Selecciona **Guardar como borrador**. Ten en cuenta que después de crear un borrador, no puedes editar la campaña activa hasta que lances o descartes tu borrador.

![Un borrador de una campaña activa con una opción para ver la campaña activa.]({% image_buster /assets/img/campaign_draft.png %})

Mientras editas el borrador, también puedes hacer referencia a la campaña activa en la cabecera del borrador de la campaña o en el pie de página de los análisis de la campaña. 

Para volver a una campaña activa, selecciona **Editar borrador** en la vista de análisis o en la vista de campaña activa.

### Priorización de mensajes dentro de la aplicación

La prioridad de los mensajes dentro de la aplicación se actualizará inmediatamente (antes de que se lance el borrador) cuando selecciones **Establecer prioridad exacta** y especifiques la prioridad en relación con otras campañas o Lienzos.
