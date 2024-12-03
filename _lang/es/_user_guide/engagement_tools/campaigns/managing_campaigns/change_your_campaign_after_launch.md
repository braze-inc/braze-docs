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

Para detener una campaña, abra la página **Detalles de la campaña** y seleccione el botón **Detener campaña** en la parte inferior derecha de la página. Cuando se detiene una campaña:
- Los mensajes programados para ser enviados serán cancelados
- Las pruebas A/B en las que ya se haya enviado la prueba inicial se cancelarán permanentemente
- Los eventos de los mensajes ya enviados (por ejemplo, los clics de apertura) seguirán siendo objeto de seguimiento.
- Las campañas pueden reanudarse haciendo clic en **Reanudar**

Una vez reanudada, esta campaña seguirá enviando mensajes y pruebas A/B, pero los mensajes perdidos no se volverán a enviar ni a programar.

## Campañas activadas

Todos los cambios en las campañas de entrega basada en acciones y en las campañas de entrega desencadenada por API entran en vigor inmediatamente para los envíos directos.

Si estas campañas se han activado pero aún no se han enviado (por ejemplo, una campaña de Entrega en función de la acción con un retraso de 1 día se edita durante el periodo de retraso de 1 día), consulte la siguiente guía para campañas programadas.

## Campañas programadas

Si necesita realizar cambios en una campaña después de su lanzamiento, tenga en cuenta los siguientes puntos cuando edite su campaña para comprobar que sus cambios tienen los efectos deseados.

### Contenido del mensaje

Cualquier cambio en el contenido del mensaje (incluyendo títulos, cuerpos, imágenes, etc.) surtirá efecto inmediatamente al guardarlo para todos los envíos de mensajes en adelante. No es posible modificar el contenido de los mensajes que ya han sido enviados.

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
