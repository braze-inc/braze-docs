---
nav_title: Race conditions
article_title: Race conditions
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artículo cubre las mejores prácticas para evitar que las condiciones de carrera afecten a sus campañas de mensajería."

---

# Condiciones de la carrera

> Una condición de carrera es un concepto en el que un resultado depende de la secuencia o sincronización de otros eventos. 

Por ejemplo, si la secuencia deseada de eventos es "Evento A" y luego "Evento B", pero a veces el "Evento A" llega primero y otras veces el "Evento B" llega primero, eso se conoce como una condición de carrera.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Segmentar a nuevos usuarios

En Braze, una de las condiciones de carrera más comunes se produce con los mensajes dirigidos a usuarios recién creados. Aquí, el orden esperado de los acontecimientos es:

1. Se crea un usuario;
2. El mismo usuario recibe inmediatamente un mensaje, realiza un evento personalizado o registra un atributo personalizado.

Sin embargo, en algunos casos, el segundo evento se activará primero. Esto significa que se está intentando enviar un mensaje a un usuario que aún no ha sido creado, y como resultado, el usuario nunca lo recibe. Lo mismo ocurre con los eventos o atributos, cuando el evento o atributo intenta registrarse en un perfil de usuario que aún no existe.

## Uso de varios puntos finales de API

Hay algunas situaciones en las que varios puntos finales de la API también pueden dar lugar a esta condición de carrera, como cuando:

- Utilizar puntos finales de API separados para crear usuarios y desencadenar Canvas o campañas
- Hacer varias llamadas separadas al punto final `/users/track` para actualizar atributos personalizados, eventos o compras.

Cuando la información del usuario se envía a Braze a través del endpoint `/users/track`, ocasionalmente puede tardar unos segundos en procesarse. Como resultado, cuando se realizan solicitudes a los puntos finales `/users/track` y [Mensajería][4] al mismo tiempo, actualmente no hay garantía de que la información del usuario se actualice antes de que se envíe un mensaje.

En los dos casos anteriores, si estas solicitudes se realizan en la misma solicitud de API, no habrá ningún problema.

{% alert note %}
Si se envían atributos de usuario y eventos en la misma solicitud (ya sea desde `/users/track` o desde el SDK), Braze procesará los atributos antes que los eventos o que intentar enviar cualquier mensaje.
{% endalert %}

Tenga en cuenta que si está enviando una solicitud de API de mensajes programados, estas solicitudes deben estar separadas y se debe crear un usuario antes de enviar la solicitud de API programada.

### Evitar la condición de carrera

Una forma de evitar esta condición de carrera es añadiendo un retardo -alrededor de un minuto- entre la creación de un usuario y la selección de ese usuario por parte de su Canvas o campaña, o intentando registrar un atributo o evento en ese perfil de usuario.

Del mismo modo, puedes utilizar el objeto [`Attributes`][1] para añadir, crear o actualizar un usuario, y luego dirigirte a él utilizando [el punto final `/canvas/trigger/send`][2] o [el punto final `/campaign/trigger/send`][3]. Esta solicitud de API procesará el objeto `attributes` antes de dirigirse a los usuarios.

Los atributos incluidos en este objeto se procesarán antes de que Braze comience a enviar la campaña. Si el indicador `send_to_existing_only` tiene el valor falso y no existe un `external_user_id` en la base de datos de Braze, crearemos un perfil de usuario para el `external_user_id` y procesaremos los atributos asociados al perfil de usuario antes de que Braze comience a enviar la campaña. Tenga en cuenta también que, si el indicador `send_to_existing_only` está establecido en false, se debe incluir el objeto de atributos para crear el usuario. El indicador `send_to_existing_only` no puede utilizarse con alias de usuario.

## Combinación de desencadenantes basados en acciones y filtros de audiencia

Otra condición de carrera común puede ocurrir si configura una campaña basada en acciones o Canvas con el mismo disparador que el filtro de audiencia (como un atributo cambiado o realizado un evento personalizado). Es posible que el usuario no se encuentre entre el público en el momento de realizar el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas. En este caso, Braze te recomienda que evites configurar tu activador para que coincida con tu filtro de audiencia. 

### Evitar la condición de carrera

Una forma de evitar esta condición de carrera puede ser añadir un retraso de más de un minuto para dar a los usuarios tiempo suficiente para entrar en el Canvas.

[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
