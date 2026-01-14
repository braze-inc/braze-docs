---
nav_title: Notificaciones de bajada de precios
article_title: Notificaciones de bajada de precios
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artículo de referencia describe cómo crear notificaciones de bajada de precios en los catálogos de Braze."
---

# Notificaciones de bajada de precios

> Esta página explica cómo funcionan las notificaciones de bajada de precios y cómo puedes configurarlas y utilizarlas. Con una combinación de notificaciones de bajada de precios a través de los catálogos Braze y un Canvas, puedes notificar a los clientes cuando el precio de un artículo ha bajado.

## Cómo funciona

Cuando un usuario desencadene un evento personalizado para un artículo, le suscribiremos automáticamente para que reciba notificaciones de bajada de precio de ese artículo. Cuando el precio del artículo cumpla tu norma de inventario (como una caída superior al 50%), todos los suscriptores serán elegibles para recibir notificaciones a través de una campaña o Canvas. Sin embargo, sólo los usuarios que hayan optado por las notificaciones recibirán notificaciones. 

## Configuración de un evento personalizado para las notificaciones de bajada de precios

Configurarás un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Recomendamos incluir un nombre de catálogo, pero no es obligatorio. También proporcionarás el nombre de un campo de precio, que debe ser un tipo de dato numérico. 

Puedes crear una suscripción de caída de precio para un usuario y un artículo de catálogo cuando ocurra lo siguiente:

- Un usuario realiza un evento personalizado seleccionado
- El evento personalizado tiene una propiedad `type` que incluye `price_drop` (`type` debe ser una matriz)

Para establecer notificaciones tanto de bajada de precio como de reposición de existencias en el mismo evento, puedes utilizar la propiedad `type`, que debe ser una matriz. Cuando un artículo tenga un cambio de precio que cumpla tu regla de precios, buscaremos a todos tus usuarios suscritos a ese artículo (usuarios que hicieron el evento de suscripción) y enviaremos un evento personalizado Braze que puedes utilizar para desencadenar una campaña o Canvas. 

Las propiedades del evento se envían junto con tu usuario, por lo que puedes introducir la plantilla con los detalles del elemento en la campaña o Canvas que envía.

## Configuración de las notificaciones de bajada de precios

Sigue estos pasos para configurar las notificaciones de bajada de precios en un catálogo concreto.

1. Ve a tu catálogo y selecciona la pestaña **Configuración**.
2. Selecciona el botón alternativo **Caída de precios**.
3. Si no se han configurado los ajustes globales del catálogo, se te pedirá que configures los eventos personalizados y las propiedades que se utilizarán para desencadenar las notificaciones. <br><br> Cajón de configuración del catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Campo | Descripción |
| --- | --- |
| **Catálogo alternativo** | El catálogo utilizado para la suscripción si no hay una propiedad `catalog_name` en el evento personalizado. |
| **Evento personalizado para suscriptores** | El evento personalizado utilizado para suscribir a un usuario a las notificaciones del catálogo. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado. |
| **Evento personalizado para cancelar suscripción** | El evento personalizado utilizado para cancelar la suscripción de un usuario a las notificaciones. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de bajada de precio, lo que ocurra primero. |
| **Propiedad del evento ID de elemento** | La propiedad del evento personalizado anterior que se utiliza para determinar el elemento de una suscripción o desuscripción. Esta propiedad del evento personalizado debe contener un ID de artículo que exista en un catálogo. El evento personalizado debe contener una propiedad `catalog_name` para especificar en qué catálogo está este artículo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Aquí tienes un ejemplo de evento personalizado:

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
                "type": ["price_drop", "back_in_stock"]
            }
        }
    ]
}
```

{: start="4"}
4\. Selecciona **Guardar** y continúa con la siguiente sección para configurar las reglas de notificación.

### Configuración de las reglas de notificación

1. Ve a la página de **configuración** de tu catálogo. 
2. Para **las reglas de notificación**, selecciona una de las siguientes opciones:<br>

    - **Notifica a todos los usuarios suscritos:** Avisa a todos los clientes que estén esperando cuando baje el precio del artículo.
    - **Configura los límites de notificación:** Notifica a un número determinado de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar, o hasta que el precio del artículo vuelva a subir. Tu tasa de notificación no puede superar la notificación a 10.000 usuarios por minuto.<br>

2. Configura el **campo Precio en el catálogo**. Es el campo del catálogo que se utilizará para determinar el precio del artículo. Debe ser de tipo numérico.
3. Configura la **regla de caída de precios**. Es la lógica utilizada para determinar si debe enviarse una notificación. Una bajada de precio puede configurarse como un cambio de precio porcentual o por el cambio de valor del campo de precio.
4. Selecciona **Guardar configuración**.

\![Configuración del catálogo que muestra la característica de bajada de precios activada. La regla de la bajada de precios es un cambio del tres por ciento del precio original.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
Las reglas de notificación de estas configuraciones no sustituyen a las configuraciones de notificación de Canvas, como Horas tranquilas.
{% endalert %}

## Utilizar notificaciones de bajada de precios en un Canvas

Después de configurar las notificaciones de bajada de precios en un catálogo, sigue estos pasos para utilizar estas notificaciones para un Canvas.

1. Configura un Canvas basado en acciones.
2. Selecciona **Realizar Evento de Caída de Precio** como desencadenante.
3. Selecciona el nombre del catálogo con las notificaciones de bajada de precios.
4. Continúa [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) tu Canvas como lo harías.

Ahora, tus clientes recibirán una notificación cuando baje el precio de un artículo.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que ha bajado de precio, puedes utilizar la etiqueta de Liquid `canvas_entry_properties` para acceder a `item_id`. 

Si utilizas {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%}, obtendrás el ID del artículo cuyo precio ha bajado. Si utilizas {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%}, obtendrás el valor del precio del artículo antes de la actualización, y si utilizas {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%}, obtendrás el nuevo valor del precio después de la actualización. 

Utiliza esta etiqueta de Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en la parte superior de tu mensaje, y luego utiliza {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acceder a los datos sobre ese elemento a lo largo de todo el mensaje.

## Consideraciones

- Los usuarios están suscritos durante 90 días. Si un artículo no baja de precio en 90 días, el usuario es dado de baja de la suscripción.
- Al utilizar la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 usuarios en 10 minutos.
- Braze procesará 10 solicitudes de actualización de elementos del catálogo por minuto. Los puntos finales de actualización permiten 50 actualizaciones de artículos por solicitud, soportando hasta 500 actualizaciones de artículos por minuto que pueden desencadenar notificaciones de reposición de existencias

