---
nav_title: Embudos de segmentos
permalink: /segment_funnels/
hidden: true
page_type: reference
---

# Embudos de segmentos

> Los embudos de segmentos son ideales para delimitar la audiencia para un caso de uso de campaña específico, aprender sobre esa audiencia y sus interacciones, y utilizar ese conocimiento para crear estrategias y desarrollar campañas eficaces.

Los embudos de segmento le permiten ver cómo afecta cada filtro añadido a las estadísticas de su segmento. Al crear un segmento, aparecerá una fila de datos debajo de cada filtro. Estos datos proporcionarán la siguiente información para los usuarios a los que se dirigen todos los filtros hasta ese momento:

- Número total de usuarios objetivo y porcentaje de tu base de audiencia
- LTV y LTV para usuarios de pago  
- Número de usuarios que pueden enviar correos electrónicos
- Número de usuarios que han optado por la adhesión voluntaria por correo electrónico
- Número de usuarios con push activado  
- Número de usuarios que han optado por la adhesión voluntaria por push

![]({% image_buster /assets/img_archive/segment_funnel_example.png %})

## Buenas prácticas

- Si añade filtros que documenten su flujo de usuarios, podrá ver los puntos en los que los usuarios se caen. Por ejemplo, si eres una aplicación de redes sociales y quieres ver dónde puedes estar perdiendo usuarios durante el proceso de incorporación, puedes añadir filtros de datos personalizados para registrarse, añadir amigos y enviar el primer mensaje. Si descubres que el 85% de los usuarios se registran y añaden amigos, pero sólo el 45% envía el primer mensaje, sabrás que debes centrarte en fomentar más envíos de mensajes durante tus campañas de incorporación y marketing.

- Los embudos de segmentos le permiten comparar el porcentaje de usuarios que realizan diferentes acciones. Por ejemplo, ¿los usuarios activos, o los que tienen un alto LTV, [tienden a interactuar más con push o correo electrónico](#push-email)? Para averiguarlo, cree un segmento de usuarios activos con uno o varios filtros y, a continuación, vea cómo cambian las estadísticas cuando añade un filtro para optar por el push y cuando añade un filtro para optar por el correo electrónico.

- Analiza cómo cambia el LTV a medida que añades filtros. En el caso de los usuarios activos, ¿tienen mayor LTV los que se conectan a Facebook o los que se conectan a X (antes Twitter)? ¿O es el LTV significativamente mayor para quienes se han conectado a ambos? Si descubres, por ejemplo, que conectarse a X (antes Twitter) tiene muy poco impacto en el LTV, pero conectarse a Facebook tiene un gran impacto, puede que quieras que tus campañas de marketing se centren en incentivar las conexiones a Facebook.

## Ejemplos

### Impacto de una acción específica del usuario en las conversiones {#push-email}

Analizando el impacto de una determinada acción del usuario (como añadir artículos a una lista de deseos) en una conversión (como realizar compras), puede responder a las siguientes preguntas:

- ¿Coincide la acción del usuario con más compras?
- ¿Cuál es la prevalencia de la acción del usuario? ¿Debería crear campañas de marketing que fomenten más esa acción?

Por ejemplo, supongamos que tiene un grupo en el que todos los usuarios que han añadido artículos a una lista de deseos también han realizado una compra. Dado que sólo un pequeño porcentaje de usuarios añadió artículos a una lista de deseos, esta aplicación podría incentivar más este comportamiento mediante campañas de marketing.

![Ejemplo de embudo de segmentos con los siguientes filtros: "Último uso de estas aplicaciones hace menos de 30 días", "Último artículo añadido a la lista de espera hace menos de 30 días" y "Última compra realizada hace menos de 30 días" para llegar a 4.302 usuarios.]({% image_buster /assets/img_archive/Wish_List_2.png %})

### Comparar canales de mensajería

Cree un segmento de usuarios activos (o usuarios con rasgos deseados) y compare sus interacciones con diferentes canales de compromiso, como el correo electrónico y las notificaciones push. Por ejemplo, si los usuarios más fieles están suscritos a push, es posible que desee dedicar más tiempo a enviar campañas de usuarios activos a través de push. Sin embargo, si observa que el LTV es mayor para los que están suscritos al correo electrónico, puede que desee incitar a los usuarios más activos a suscribirse al correo electrónico.

![Ejemplo de embudo de segmentación para correo electrónico con los siguientes filtros: "Última compra realizada hace menos de 30 días", "Último uso de estas aplicaciones hace menos de 30 días", "La habilitación push es verdadera" y "El estado de la suscripción por correo electrónico es habilitado" para llegar a 2.799 usuarios.]({% image_buster /assets/img_archive/Wish_List_Email.png %})

### Inscripciones push en iOS o Android

Este caso de uso aprovecha el filtro "Push Enabled for App" para dirigirse a los usuarios de iOS o Android que han optado por recibir push.

![]({% image_buster /assets/img/seg_filter_examples/ios.png %})

![]({% image_buster /assets/img/seg_filter_examples/android.png %})

### Audiencia total habilitada para push

Este caso de uso aprovecha el filtro "Push Enabled" para dirigirse a los usuarios que han optado por recibir push.

![]({% image_buster /assets/img/seg_filter_examples/both.png %})

### Grupo de control global de audiencia habilitada para push

Este caso de uso aprovecha el filtro "Push Enabled" y "Random Bucket #" para dirigirse a los usuarios que forman parte del grupo de control global que han optado por push.

![]({% image_buster /assets/img/seg_filter_examples/global_control.png %})

### Compradores recientes

Este caso de uso aprovecha el filtro "Última compra realizada" para dirigirse a los usuarios que realizaron su última compra hace menos de 7 días.

![]({% image_buster /assets/img/seg_filter_examples/recent_purchase.png %})

### Empujar el compromiso

Este caso de uso aprovecha el filtro "Último evento personalizado" en el que el evento personalizado es "abrió cualquier push" para dirigirse a los usuarios que han mostrado interacción push en los últimos 21 días.

![]({% image_buster /assets/img/seg_filter_examples/push_engagement.png %})

### Dinero gastado en la aplicación

Este caso de uso aprovecha el filtro "Dinero gastado" para dirigirse a los usuarios que han gastado al menos 1.000 dólares.

![]({% image_buster /assets/img/seg_filter_examples/moneyspent.png %})


