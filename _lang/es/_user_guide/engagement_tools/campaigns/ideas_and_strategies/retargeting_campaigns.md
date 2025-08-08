---
nav_title: Reorientación de campañas
article_title: Reorientación de campañas
page_order: 2
page_type: reference
description: "Este artículo de referencia repasa cómo y por qué debe considerar las campañas de retargeting basadas en los mensajes que reciben sus usuarios."
tool:
  - Campaigns
  
---

# Reorientación de campañas

> Al reorientar las campañas en función de las acciones anteriores del usuario, como si abrió o no un correo electrónico, puede ayudar a reclasificar a sus usuarios, abriendo la puerta a un enfoque de marketing eficaz y basado en datos.

Braze permite reorientar a los usuarios en función de los mensajes que han recibido. Puedes reorientar a los usuarios en función de sus interacciones con tus campañas y Lienzos. 

Cada uno de estos filtros de retargeting le ofrece varias opciones después de añadirlos. Para obtener más información sobre la segmentación de usuarios, consulte nuestro [curso Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

![Sección Detalles del segmento con el menú desplegable para los filtros disponibles.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtros de reorientación

Puedes utilizar los filtros de reorientación de esta sección para tus usuarios dentro de tus campañas y Canvases.

### Campaña que se abrió o a la que se hizo clic

Utilice este filtro para encontrar usuarios que lo hayan hecho o no:

- Hizo clic en un correo electrónico
- Has pulsado un mensaje de la aplicación
- Abrió directamente una notificación push
- Abrió un correo electrónico
- Has visto un mensaje en la aplicación

![]({% image_buster /assets/img_archive/clickedopened.png %})

Esto se puede especificar aún más seleccionando qué campaña quieres reorientar.

### Se ha hecho clic o se ha abierto la campaña o el lienzo con la etiqueta

Utilice este filtro para encontrar usuarios que hayan o no interactuado con campañas o lienzos con una etiqueta determinada:

- Hizo clic en un correo electrónico
- Has pulsado un mensaje de la aplicación
- Abrió directamente una notificación push
- Abrió un correo electrónico
- Has visto un mensaje en la aplicación

![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Convertido desde campaña 

Utilice este filtro para encontrar usuarios que se hayan convertido o no (en función de la conversión principal) en su campaña de destino. 

Para las campañas recurrentes, este filtro se refiere a si los usuarios han convertido en el mensaje más reciente de la campaña.

![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Convertido desde Canvas 

Utilice este filtro para encontrar usuarios que se hayan convertido o no (en función de la conversión principal) en su lienzo de destino.

Para los Canvas recurrentes este filtro se refiere a si los usuarios han convertido alguna vez que han pasado por el Canvas.

![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### Grupo de control en campaña 

Utilice este filtro para encontrar usuarios que pertenezcan o no al grupo de control de su campaña objetivo.

![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### Grupo de control en Canvas 

Utiliza este filtro para encontrar usuarios que estén o no en el grupo de control de tu Canvas de destino, que puedes seleccionar en el desplegable.

![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Último mensaje recibido de una campaña específica 

Utilice este filtro para encontrar usuarios que recibieron por última vez una campaña específica antes o después de una fecha o número de días especificados. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas.

![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Último mensaje recibido de una campaña específica o Canvas con etiqueta 

Utiliza este filtro para encontrar usuarios que recibieron por última vez una campaña o Canvas específicos con una etiqueta determinada antes o después de una fecha o número de días especificados. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas o Lienzos.

![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Mensaje recibido de la campaña 

Utilice este filtro para encontrar usuarios que han recibido o no su campaña objetivo.

![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Mensaje recibido de campaña o Canvas con etiqueta 

Utiliza este filtro para encontrar usuarios que han recibido o no una campaña o Canvas que tenga tu etiqueta objetivo.

![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Ventajas de las campañas de retargeting

El retargeting es especialmente eficaz cuando el segmento original también incluía una acción específica que desea que realicen los usuarios. Por ejemplo, supongamos que tiene una tarjeta dirigida a usuarios que nunca han realizado una compra. La tarjeta anuncia una promoción para una compra con descuento dentro de la aplicación. El segmento inicial tiene el siguiente aspecto:

- El dinero gastado en la aplicación es exactamente 0
- Usó la aplicación por última vez hace menos de 14 días

El número total de usuarios del segmento es de 100.000 y sabes por las estadísticas de la tarjeta de contenido que 60.000 usuarios únicos vieron la tarjeta y 20.000 usuarios únicos hicieron clic en ella. A través del segmentador podemos ver cuántos de esos usuarios que hicieron clic en la tarjeta realizaron realmente una compra:

- El dinero gastado en la aplicación es superior a 0
- La tarjeta seleccionada es el nombre de la tarjeta

Tras examinar esas estadísticas, podemos hacer un segmento de usuarios que hicieron clic en la tarjeta, pero no realizaron ninguna compra:

- El dinero gastado en la aplicación es exactamente 0
- La tarjeta seleccionada es el nombre de la tarjeta

Podemos volver a dirigirnos a este segmento con mensajes adicionales sobre la promoción u otra compra dentro de la aplicación. La reorientación puede hacerse con una campaña de mensajería. Un enfoque multicanal le permite llegar a los usuarios allí donde es más probable que respondan, aumentando así la eficacia de sus campañas.

