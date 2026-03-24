---
nav_title: Notificaciones de bajada de precios
article_title: Notificaciones de bajada de precios
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artículo de referencia describe cómo crear notificaciones de bajada de precios en catálogos de Braze."
---

# Notificaciones de bajada de precios

> Esta página explica cómo funcionan las notificaciones de bajada de precios y cómo puedes configurarlas y utilizarlas. Con una combinación de notificaciones de bajada de precios a través de los catálogos de Braze y un Canvas, puedes notificar a los clientes cuando el precio de un artículo haya bajado.

## Cómo funciona

Cuando un usuario desencadene un evento personalizado para un artículo, le suscribiremos automáticamente para que reciba notificaciones de bajada de precio de ese artículo. Cuando el precio del artículo cumpla tu regla de inventario (como una caída superior al 50 %), todos los suscriptores serán elegibles para recibir notificaciones a través de una campaña o Canvas. Sin embargo, solo los usuarios que hayan optado por recibir notificaciones las recibirán. 

## Configuración de un evento personalizado para notificaciones de bajada de precio

Configurarás un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo un evento `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Recomendamos incluir un nombre de catálogo, pero no es obligatorio. También proporcionarás el nombre de un campo de precio, que debe ser de tipo de datos numérico. 

Puedes crear una suscripción a bajadas de precio para un usuario y un artículo del catálogo cuando se produzca alguna de las siguientes situaciones:

- Un usuario realiza un evento personalizado seleccionado
- El evento personalizado tiene una propiedad `type` que incluye `price_drop` (`type` debe ser una matriz)

Para configurar notificaciones tanto de bajada de precio como de reposición de existencias en el mismo evento, puedes utilizar la propiedad `type`, que debe ser una matriz. Cuando un artículo tenga un cambio de precio que cumpla tu regla de precios, buscaremos a todos tus usuarios suscritos a ese artículo (usuarios que realizaron el evento de suscripción) y enviaremos un evento personalizado de Braze que puedes utilizar para desencadenar una campaña o Canvas. 

Las propiedades del evento se envían junto con tu usuario, por lo que puedes incluir los detalles del artículo en la plantilla de la campaña o Canvas que lo envía.

## Configurar las notificaciones de bajada de precios

Sigue estos pasos para configurar las notificaciones de bajada de precios en un catálogo específico.

1. Ve a tu catálogo y selecciona la pestaña **Configuración**.
2. Selecciona el alternador **Bajada de precios**.
3. Si no se ha realizado la configuración global del catálogo, se te pedirá que configures los eventos y propiedades personalizados que se utilizarán para desencadenar las notificaciones. <br><br> ![Cajón de configuración del catálogo.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| Campo | Descripción |
| --- | --- |
| **Catálogo alternativo** | El catálogo utilizado para la suscripción si no hay una propiedad `catalog_name` en el evento personalizado. |
| **Evento personalizado para suscribirse** | El evento personalizado utilizado para suscribir a un usuario a las notificaciones del catálogo. Cuando se produzca este evento, se suscribirá al usuario que lo haya realizado. |
| **Evento personalizado para cancelar suscripción** | El evento personalizado utilizado para cancelar la suscripción de un usuario a las notificaciones. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de bajada de precio, lo que ocurra primero. |
| **Propiedad del evento de ID de artículo** | La propiedad en el evento personalizado anterior que se utiliza para determinar el artículo para una suscripción o cancelación de suscripción. Esta propiedad del evento personalizado debe contener un ID de artículo que exista en un catálogo. El evento personalizado debe contener una propiedad `catalog_name` para especificar en qué catálogo se encuentra este artículo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A continuación se muestra un ejemplo de evento personalizado:

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
4. Selecciona **Guardar** y continúa con la siguiente sección para configurar las reglas de notificación.

### Configuración de reglas de notificación

1. Ve a la página **Configuración** de tu catálogo. 
2. Para **Reglas de notificación**, selecciona una de las siguientes opciones:<br>

    - **Notificar a todos los usuarios suscritos:** Notifica a todos los clientes que están esperando cuando baje el precio del artículo.
    - **Establecer límites de notificación:** Notifica a un número específico de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar, o hasta que el precio del artículo vuelva a subir. La tasa de notificación no puede superar los 10.000 usuarios por minuto.<br>

2. Configura el **campo Precio en el catálogo**. Es el campo del catálogo que se utilizará para determinar el precio del artículo. Debe ser de tipo numérico.
3. Configura la **regla de bajada de precios**. Esta es la lógica utilizada para determinar si se debe enviar una notificación. Una bajada de precio se puede configurar como un cambio porcentual del precio o como un cambio en el valor del campo de precio.
4. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la función de bajada de precios activada. La regla de bajada de precios consiste en un cambio del tres por ciento sobre el precio original.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
Las reglas de notificación de esta configuración no sustituyen a los ajustes de notificación de Canvas, como las horas tranquilas.
{% endalert %}

## Uso de las notificaciones de bajada de precio en Canvas

Después de configurar las notificaciones de bajada de precios en un catálogo, sigue estos pasos para utilizar estas notificaciones en un Canvas.

1. Configura un Canvas basado en acciones.
2. Selecciona **Realizar evento de bajada de precio** como desencadenante.
3. Selecciona el nombre del catálogo con las notificaciones de bajada de precios.
4. Continúa [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) tu Canvas como lo harías normalmente.

Ahora, tus clientes recibirán una notificación cuando baje el precio de un artículo.

### Utilizar Liquid

Para incluir en la plantilla detalles sobre el artículo del catálogo que ha bajado de precio, puedes utilizar la etiqueta de Liquid `context` para acceder a `item_id`. 

Al usar {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} se devolverá el ID del artículo cuyo precio ha bajado. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} devolverá el valor del precio del artículo antes de la actualización, y {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} devolverá el nuevo valor del precio después de la actualización. 

Utiliza la etiqueta de Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} en la parte superior de tu mensaje y, a continuación, utiliza {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acceder a los datos sobre ese artículo a lo largo del mensaje.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Consideraciones

- Los usuarios se suscriben por 90 días. Si un artículo no baja de precio en 90 días, el usuario se da de baja de la suscripción.
- Cuando se utiliza la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 usuarios en 10 minutos.
- Braze admite hasta 50.000 artículos actualizados diariamente que son elegibles para desencadenar notificaciones de bajada de precios. Puedes tener hasta 100 millones de suscripciones activas en un momento dado, donde cada suscripción representa un perfil de usuario suscrito para seguir un artículo del catálogo.