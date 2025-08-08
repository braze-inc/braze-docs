---
nav_title: Influenced Opens
article_title: Influenced Opens
page_order: 7
page_type: reference
description: "Este artículo de referencia explica las aperturas influidas y cómo puede realizar un seguimiento de las mismas para proporcionar un mayor nivel de detalle a sus campañas push."
channel: push

---

# Influenced Opens

> Cuando un usuario selecciona una notificación push y es enviado a tu aplicación, Braze lo registra como una apertura directa. Cuando los usuarios no seleccionan la notificación pero aún así pueden verse influidos por la notificación push, Braze la registra como una apertura influida. Esto proporciona un mayor nivel de detalle sobre el efecto de sus campañas push.

## Cómo funciona

En su base, las aperturas influidas miden el número de usuarios que abren la aplicación tras recibir una notificación sin seleccionarla. Como no hay una acción directa que vincule la notificación con la apertura de la aplicación, se registra una apertura influida si el usuario abre la aplicación menos de treinta minutos después de recibir la notificación push o menos de la mitad del tiempo medio transcurrido desde la última sesión de ese usuario.

Por ejemplo, supongamos que envías una notificación push a los usuarios de tu aplicación. Si un usuario que normalmente abre la aplicación 30 veces al día abre tu aplicación seis horas después de recibir el push, el push recibe poco o ningún crédito por influir en la apertura. Sin embargo, si un usuario que normalmente utiliza la aplicación una vez al mes la abre seis horas después de recibir el push, la apertura tiene muchas más posibilidades de contabilizarse como una apertura influida. 

Esto difiere de establecer las aperturas de aplicaciones como un evento de conversión para una campaña push. Para las conversiones, todas las aperturas dentro de la ventana de conversión se atribuirán a la campaña. Influenced Opens configura una ventana de tiempo y crédito de atribución basados en el comportamiento de un usuario individual.

## Ver las aperturas influidas por una campaña

Las aperturas influidas se suman a las aperturas directas de una campaña para obtener un número de aperturas totales. Se muestra en la página **de análisis de campaña** de una campaña push. Las aperturas totales y las aperturas directas se muestran en las secciones Rendimiento de los mensajes y **Rendimiento histórico**. Las Influenced Opens son la diferencia entre las dos medidas.

![Influenced Opens abre las estadísticas en la página Detalles de campaña de una campaña]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Para más información sobre el seguimiento de aperturas, consulta la sección de seguimiento de conversiones de nuestras [mejores prácticas para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

