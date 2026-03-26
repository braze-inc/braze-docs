---
nav_title: Notificaciones de existencias
article_title: Configurar notificaciones de reposición de existencias
page_order: 2
description: "Aprende a configurar notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible."
---

# Notificaciones de existencias

> Aprende a configurar notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible. Ten en cuenta que esto solo se aplica a los usuarios que han realizado una adhesión voluntaria para recibir notificaciones.

## Cómo funciona

Puedes configurar un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo un`product_clicked`evento . Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Le sugerimos que incluya un nombre de catálogo, pero no es obligatorio. También deberás proporcionar el nombre de un campo de cantidad de inventario, que debe ser de tipo de datos numérico. 

Ten en cuenta que el stock de un artículo del catálogo debe ser cero para que un usuario pueda suscribirse a él correctamente. Cuando un artículo tiene una cantidad en inventario superior a cero, Braze buscará todos los usuarios suscriptos a ese artículo y enviará un evento personalizado que podrás utilizar para desencadenar una campaña o Canvas.

Las propiedades del evento se envían junto con tu usuario, por lo que puedes crear una plantilla con los detalles del elemento en la campaña o Canvas que lo envía.

## Configurar las notificaciones de reposición de existencias

Siga estos pasos para configurar las notificaciones de agotado en un catálogo específico.

1. Vaya a su catálogo y seleccione la pestaña **Configuración**.
2. Seleccione la opción **Volver a existencias**.
3. Si no se han configurado los ajustes globales de reposición de existencias, se le pedirá que configure los eventos y propiedades personalizados que se utilizarán para activar las notificaciones de reposición de existencias:
    <br> ![Cajón de configuración del catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Catálogo alternativo** Éste es el catálogo que se utilizará para la suscripción de reserva, si no hay ninguna propiedad `catalog_name` presente en el evento personalizado.
    - **El evento personalizado para suscripciones** es el evento personalizado de Braze que se utilizará para suscribir a un usuario a las notificaciones de reposición de existencias. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado.
    - **Evento personalizado para darse de baja** es el evento personalizado Braze que se utilizará para dar de baja a un usuario de las notificaciones de reposición de existencias. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de reposición de existencias, lo que ocurra primero.
    - **La propiedad del evento ID del artículo** es la propiedad del evento personalizado anterior que se utilizará para determinar el artículo para una suscripción o desuscripción de nuevo en stock. Esta propiedad del evento personalizado debe contener un ID de elemento (`id`) que esté presente en un catálogo. El ID del elemento debe enviarse como una cadena para que coincida con el tipo`id` de datos almacenado en el catálogo de destino. El evento personalizado también debe contener una`catalog_name`propiedad para especificar en qué catálogo se encuentra este elemento.
    
    - Un ejemplo de evento personalizado sería el siguiente:
    
```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

{% alert note %}
Los desencadenantes de reposición de existencias y bajada de precios utilizan el mismo evento para suscribir al usuario a la notificación, por lo que puedes utilizar la`type`propiedad para configurar las notificaciones de bajada de precios y reposición de existencias en el mismo evento. Ten en cuenta que la`type`propiedad debe ser una matriz.
{% endalert %}

{: start="4"}
4\. Seleccione **Guardar** y continúe en la página **Configuración** del catálogo.
5\. Establezca su regla de notificación. Hay dos opciones:
    - **Notificar a todos los usuarios suscritos** notifica a todos los clientes que están esperando cuando el artículo vuelve a estar disponible.
    - **Establecer límites de notificación** notifica a un número determinado de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes por incrementos hasta que no haya más clientes a los que notificar o hasta que el artículo se agote. El ritmo de notificación no puede superar los 10.000 usuarios por minuto.
6\. Establezca el **campo Inventario en el catálogo**. Este campo del catálogo se utilizará para determinar si el artículo está agotado. El campo debe ser de tipo numérico.
7\. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la función de reposición de existencias activada. Las reglas de notificación consisten en notificar a mil usuarios cada diez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Las reglas de notificación de estos ajustes no sustituyen a los ajustes de notificación de Canvas, como Horas de silencio.
{% endalert %}

## Utilizar las notificaciones de agotado en un lienzo

Después de configurar la característica «De nuevo en stock» en un catálogo, sigue estos pasos para utilizarla con Canvas.

1. Establezca un lienzo basado en acciones.
2. Seleccione **Volver a existencias** como desencadenante.
3. Seleccione el nombre del catálogo con las notificaciones de reposición de existencias.
4. Continúe [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) su lienzo como lo haría.

Ahora, sus clientes pueden recibir una notificación cuando un artículo vuelva a estar disponible.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que vuelve a estar disponible, puedes utilizar la etiqueta de Liquid `context` para acceder a `item_id`. 

El uso de {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} devolverá el ID del artículo que volvió a estar en stock. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} devolverá el valor de inventario del artículo antes de la actualización, y {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} devolverá el nuevo valor de inventario después de la actualización.

Utiliza la etiqueta de Liquid{%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} en la parte superior de tu mensaje y, a continuación, utiliza{%raw%}``{{ items[0].<field_name> }}``{%endraw%}  para acceder a los datos sobre ese elemento a lo largo del mensaje.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Consideraciones

- Los usuarios sólo están suscritos durante 90 días. Si el artículo no vuelve a estar disponible en 90 días, el usuario se da de baja.
- Cuando se utiliza la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 usuarios en 10 minutos.
- El soporte de Braze admite hasta 50 000 artículos actualizados al día que son elegibles para desencadenar notificaciones de reposición de existencias. Puedes tener hasta 100 millones de suscripciones activas en un momento dado, donde cada suscripción representa un perfil de usuario suscrito para ver un elemento del catálogo.

