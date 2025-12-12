---
nav_title: Notificaciones de existencias remanentes
article_title: Configuración de las notificaciones de agotamiento de existencias
page_order: 2
description: "Aprende a configurar las notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible."
---

# Notificaciones de existencias remanentes

> Aprende a configurar las notificaciones de reposición de existencias utilizando tu catálogo y eventos personalizados, para que puedas suscribir automáticamente a los clientes para que reciban notificaciones cuando un artículo vuelva a estar disponible. Ten en cuenta que esto sólo se aplica a los usuarios que ya han optado por la adhesión voluntaria a las notificaciones.

## Cómo funciona

Puedes configurar un evento personalizado para utilizarlo como evento de suscripción, como un evento de `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Te sugerimos que incluyas un nombre de catálogo, pero no es obligatorio. También proporcionarás el nombre de un campo de cantidad de inventario, que debe ser de tipo dato numérico. 

Ten en cuenta que el stock de un artículo del catálogo debe estar a cero para que un usuario pueda suscribirse a él con éxito. Cuando un artículo tenga una cantidad de inventario superior a cero, Braze buscará a todos los usuarios suscritos a ese artículo y enviará un evento personalizado que puedes utilizar para desencadenar una campaña o Canvas.

Las propiedades del evento se envían junto con tu usuario, por lo que puedes introducir la plantilla con los detalles del elemento en la campaña o Canvas que envía.

## Configuración de las notificaciones de agotamiento de existencias

Sigue estos pasos para configurar las notificaciones de agotado en un catálogo concreto.

1. Ve a tu catálogo y selecciona la pestaña **Configuración**.
2. Selecciona el botón alternativo **Disponible**.
3. Si no se han configurado los ajustes globales de existencias remanentes, se te pedirá que configures los eventos personalizados y las propiedades que se utilizarán para desencadenar las notificaciones de existencias remanentes:
    <br> Cajón de configuración del catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Catálogo alternativo** Éste es el catálogo que se utilizará para la suscripción de reserva, si no hay ninguna propiedad `catalog_name` presente en el evento personalizado.
    - El **evento personalizado para suscripciones** es el evento personalizado de Braze que se utilizará para suscribir a un usuario a las notificaciones de reposición de existencias. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado.
    - El **evento personalizado para cancelar suscripción** es el evento personalizado de Braze que se utilizará para cancelar la suscripción de un usuario a las notificaciones de reposición de existencias. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de reposición de existencias, lo que ocurra primero.
    - **La propiedad del evento ID del artículo** es la propiedad del evento personalizado anterior que se utilizará para determinar el artículo para una suscripción o desuscripción de nuevo en stock. Esta propiedad del evento personalizado debe contener un ID de artículo (`id`) que esté presente en un catálogo. El ID del artículo debe enviarse como una cadena para que coincida con el tipo de datos `id` almacenado en el catálogo de destino. El evento personalizado también debe contener una propiedad `catalog_name`, para especificar en qué catálogo se encuentra este artículo.
    
    - Un ejemplo de evento personalizado tendría el siguiente aspecto
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
Los desencadenantes de reposición de existencias y de bajada de precios utilizan el mismo evento para suscribir al usuario a la notificación, por lo que puedes utilizar la propiedad `type` para establecer tanto las notificaciones de bajada de precios como las de reposición de existencias en el mismo evento. Nota que la propiedad `type` debe ser una matriz.
{% endalert %}

{: start="4"}
4\. Selecciona **Guardar** y continúa a la página **Configuración** del catálogo.
5\. Configura tu regla de notificación. Hay dos opciones:
    - **Notificar a todos los usuarios suscritos** notifica a todos los clientes que están esperando cuando el artículo vuelve a estar disponible.
    - **Establecer límites de notificación** notifica a un número determinado de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar o hasta que el artículo se agote. Tu tasa de notificación no puede superar la notificación a 10.000 usuarios por minuto.
6\. Configura el **campo Inventario en el catálogo**. Este campo del catálogo se utilizará para determinar si el artículo está agotado. El campo debe ser de tipo numérico.
7\. Selecciona **Guardar configuración**.

\![Configuración del catálogo que muestra la característica de reserva activada. Las reglas de notificación consisten en notificar a mil usuarios cada diez minutos.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Las reglas de notificación de estas configuraciones no sustituyen a las configuraciones de notificación de Canvas, como Horas tranquilas.
{% endalert %}

## Utilizar notificaciones de agotamiento de existencias en un Canvas

Después de configurar la característica de reserva de existencias en un catálogo, sigue estos pasos para utilizarla con Canvas.

1. Configura un Canvas basado en acciones.
2. Selecciona **Volver a existencias** como desencadenante.
3. Selecciona el nombre del catálogo con las notificaciones de agotado.
4. Continúa [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) tu Canvas como lo harías.

Ahora, tus clientes pueden recibir una notificación cuando un artículo vuelva a estar disponible.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que vuelve a estar disponible, puedes utilizar la etiqueta de Liquid `canvas_entry_properties` para acceder a `item_id`. 

Si utilizas {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%}, obtendrás el ID del artículo que se ha vuelto a almacenar. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} obtendrás el valor de inventario del artículo antes de la actualización, y {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} obtendrás el nuevo valor de inventario después de la actualización.

Utiliza esta etiqueta de Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} en la parte superior de tu mensaje, y luego utiliza {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acceder a los datos sobre ese elemento a lo largo de todo el mensaje.

## Consideraciones

- Los usuarios sólo están suscritos durante 90 días. Si el artículo no vuelve a estar disponible en 90 días, se cancela la suscripción del usuario.
- Al utilizar la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 en 10 minutos.
- Braze procesará como máximo 10 actualizaciones de elementos en un minuto. Si actualizas 11 artículos en un minuto, sólo los 10 primeros pueden desencadenar una notificación de reposición de existencias.

