---
nav_title: Campañas de reorientación
article_title: Campañas de reorientación
page_order: 2
page_type: reference
description: "Este artículo de referencia repasa cómo y por qué deberías plantearte campañas de reorientación basadas en los mensajes que reciben tus usuarios."
tool:
  - Campaigns
  
---

# Campañas de reorientación

> Al reorientar las campañas basándote en las acciones anteriores del usuario, como si abrió o no un correo electrónico, puedes ayudar a reclasificar a tus usuarios, abriendo la puerta a un enfoque de marketing basado en datos eficaz.

Braze proporciona soporte para reorientar a los usuarios basándose en los mensajes que han recibido. Puedes reorientar a los usuarios en función de sus interacciones con tus campañas y Canvases. 

Cada uno de estos filtros de reorientación te ofrece varias opciones después de añadirlos. Para obtener más información sobre la segmentación de usuarios, ¡consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas!

\![Sección Detalles del segmento con el menú desplegable para los filtros disponibles.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Reorientar filtros

Puedes utilizar los filtros de reorientación de esta sección para tus usuarios dentro de tus campañas y Canvases.

### Campaña clicada/abierta

Utiliza este filtro para encontrar usuarios que tienen o no tienen:

- Has hecho clic en un correo electrónico
- Has hecho clic en un mensaje dentro de la aplicación
- Directamente abierta una notificación push
- Abrir un correo electrónico
- Visto un mensaje dentro de la aplicación

\![]({% image_buster /assets/img_archive/clickedopened.png %})

Esto se puede especificar aún más seleccionando qué campaña quieres reorientar.

### Has hecho clic o has abierto una campaña o Canvas con etiqueta

Utiliza este filtro para encontrar usuarios que hayan o no interactuado con campañas o Lienzos con una etiqueta determinada:

- Has hecho clic en un correo electrónico
- Has hecho clic en un mensaje dentro de la aplicación
- Directamente abierta una notificación push
- Abrir un correo electrónico
- Visto un mensaje dentro de la aplicación

\![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Convertido de campaña 

Utiliza este filtro para encontrar usuarios que se hayan convertido o no (en función de la conversión primaria) en tu campaña objetivo. 

Para las campañas recurrentes, este filtro se refiere a si los usuarios han convertido en el mensaje más reciente de la campaña.

\![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Convertido de Canvas 

Utiliza este filtro para encontrar usuarios que se hayan convertido o no (en función de la conversión primaria) en tu Canvas de destino.

Para los Canvas recurrentes, este filtro se refiere a si los usuarios se han convertido alguna vez que han pasado por el Canvas.

\![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### En Grupo de control de campaña 

Utiliza este filtro para encontrar usuarios que estén o no en el grupo de control de tu campaña objetivo.

\![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### En Canvas Grupo de control 

Utiliza este filtro para encontrar usuarios que estén o no en el grupo de control de tu Canvas de destino, que puedes seleccionar en el desplegable.

\![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Último mensaje recibido de una campaña específica 

Utiliza este filtro para encontrar usuarios que recibieron por última vez una campaña específica antes o después de una fecha o número de días especificados. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas.

\![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Último mensaje recibido de una campaña específica o Canvas con etiqueta 

Utiliza este filtro para encontrar usuarios que recibieron por última vez una campaña o Canvas específico con una etiqueta determinada antes o después de una fecha o número de días especificados. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas o Lienzos.

\![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Mensaje recibido de la campaña 

Utiliza este filtro para encontrar usuarios que han recibido o no tu campaña objetivo.

\![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Mensaje recibido de campaña o Canvas con etiqueta 

Utiliza este filtro para encontrar usuarios que hayan recibido o no una campaña o Canvas que tenga tu etiqueta objetivo.

\![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Ventajas de las campañas de reorientación

La reorientación es especialmente eficaz cuando el segmento original también incluía una acción específica que quieres que realicen los usuarios. Por ejemplo, supongamos que tienes una tarjeta dirigida a usuarios que nunca han hecho una compra. La tarjeta anuncia una promoción para una compra dentro de la aplicación con descuento. El segmento inicial tiene el siguiente aspecto:

- El dinero gastado en la aplicación es exactamente 0
- Última aplicación utilizada hace menos de 14 días

El número total de usuarios del segmento es de 100.000 y sabes por las estadísticas de la tarjeta de contenido que 60.000 usuarios únicos vieron la tarjeta y 20.000 usuarios únicos hicieron clic en ella. A través del segmentador podemos ver cuántos de esos usuarios que hicieron clic en la tarjeta realizaron realmente una compra:

- El dinero gastado en la aplicación es más de 0
- La tarjeta en la que has hecho clic es el nombre de la tarjeta

Tras examinar esas estadísticas, podemos hacer un segmento de usuarios que hicieron clic en la tarjeta, pero no realizaron ninguna compra:

- El dinero gastado en la aplicación es exactamente 0
- La tarjeta en la que has hecho clic es el nombre de la tarjeta

Podemos reorientar este segmento con mensajería adicional en torno a la promoción u otra compra dentro de la aplicación. La reorientación puede hacerse con una campaña de mensajería. Un enfoque multicanal te permite llegar a los usuarios allí donde es más probable que respondan, aumentando así la eficacia de tus campañas.

