---
nav_title: Notificaciones de bajada de precios
article_title: Notificaciones de bajada de precios
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artículo de referencia describe cómo crear notificaciones de bajada de precios en catálogos Braze."
---

# Notificaciones de bajada de precios

> Utiliza una combinación de notificaciones de bajada de precios a través de los catálogos Braze y un Canvas para notificar a los clientes cuando el precio de un artículo ha bajado. Cada vez que un cliente realiza un evento personalizado seleccionado, puede suscribirse automáticamente para recibir una notificación cuando se reduzca el precio del artículo.<br><br>Esta página explica cómo funcionan las notificaciones de bajada de precios y cómo puedes configurarlas y utilizarlas.

Cuando un usuario active un evento personalizado para un artículo, le suscribiremos automáticamente para que reciba notificaciones de bajadas de precio de ese artículo. Cuando el precio del artículo cumpla tu regla de inventario (como una caída superior al 50 %), todos los suscriptores serán elegibles para recibir notificaciones a través de una campaña o Canvas. Sin embargo, sólo los usuarios que hayan optado por recibir notificaciones las recibirán. 

## Cómo funcionan las notificaciones de bajada de precios

Configurará un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Le sugerimos que incluya un nombre de catálogo, pero no es obligatorio. También proporcionará el nombre de un campo de precio, que debe ser de tipo dato numérico. 

Cuando un usuario realiza un evento personalizado seleccionado y tiene una propiedad `type` que incluye `price_drop`, se puede utilizar para crear una suscripción de caída de precio para un usuario y un artículo de catálogo para el que se produjo. También puedes utilizar esta matriz `type` para establecer notificaciones tanto de bajada de precio como de reposición de existencias en el mismo evento.

Cuando un artículo tenga un cambio de precio que cumpla su regla de precios, buscaremos a todos sus usuarios suscritos a ese artículo (usuarios que realizaron el evento de suscripción) y enviaremos un evento personalizado Braze que puede utilizar para activar una campaña o Canvas.

Las propiedades del evento se envían junto con el usuario, por lo que puede introducir los detalles del elemento en la campaña o el lienzo que envía.

## Configurar las notificaciones de bajada de precios

Siga estos pasos para configurar las notificaciones de bajada de precios en un catálogo específico.

1. Vaya a su catálogo y seleccione la pestaña **Configuración**.<br>
2. Selecciona el botón alternativo **Caída de precios**.<br>
3. Si no se han configurado los ajustes globales del catálogo, se le pedirá que configure los eventos y propiedades personalizados que se utilizarán para activar las notificaciones:
    <br> ![Cajón de configuración del catálogo.][2]{: style="max-width:70%;"}
    - **Catálogo de alternativas:** El catálogo utilizado para la suscripción si no hay una propiedad `catalog_name` en el evento personalizado.
    - **Evento personalizado para suscribirse:** El evento personalizado Braze utilizado para suscribir a un usuario a las notificaciones de catálogo. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado.
    - **Evento personalizado para cancelar suscripción:** El evento personalizado Braze utilizado para dar de baja a un usuario de las notificaciones. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de bajada de precio, lo que ocurra primero.
    - **Propiedad del evento ID del elemento:** La propiedad en el evento personalizado anterior que se utiliza para determinar el elemento para una suscripción o desuscripción. Esta propiedad del evento personalizado debe contener un ID de artículo que exista en un catálogo. El evento personalizado debe contener una propiedad `catalog_name` para especificar en qué catálogo se encuentra este artículo.
   
    - Un ejemplo de evento personalizado sería el siguiente
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
4\. Seleccione **Guardar** y continúe en la página **Configuración** del catálogo.
5\. Establezca su regla de notificación. Hay dos opciones:
    - **Notificar a todos los usuarios suscritos** notifica a todos los clientes que están esperando cuando el precio del artículo baja.
    - **Establecer límites de notificación** notifica a un número determinado de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar, o hasta que el precio del artículo vuelva a subir. El ritmo de notificación no puede superar los 10.000 usuarios por minuto.
6\. Configura el **campo Precio en el catálogo**. Es el campo del catálogo que se utilizará para determinar el precio del artículo. Debe ser de tipo numérico.<br>
7\. Configura la **regla de caída de precios**. Esta es la lógica utilizada para determinar si se debe enviar una notificación. Una bajada de precio puede configurarse como un cambio de precio porcentual o en cuánto ha cambiado el valor del campo de precio.<br>
8\. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la función de bajada de precios activada. La regla de la bajada de precios es una modificación del 3% del precio original.][1]{:style="max-width:60%;"}

{% alert important %}
Las reglas de notificación de estos ajustes no sustituyen a los ajustes de notificación de Canvas, como Horas de silencio.
{% endalert %}

## Uso de las notificaciones de bajada de precios en Canvas

Después de configurar las notificaciones de bajada de precios en un catálogo, siga estos pasos para utilizar estas notificaciones en un Canvas.

1. Establezca un lienzo basado en acciones.
2. Seleccione **Realizar evento de caída de precio** como desencadenante.
3. Seleccione el nombre del catálogo con las notificaciones de bajada de precios.
4. Continúe [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) su lienzo como lo haría.

Ahora, sus clientes recibirán una notificación cuando baje el precio de un artículo.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que ha bajado de precio, puedes utilizar la etiqueta de Liquid `canvas_entry_properties` para acceder a `item_id`. 

El uso de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} devolverá el ID del artículo que ha bajado de precio. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} devolverá el valor del precio del artículo antes de la actualización, y {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} devolverá el nuevo valor del precio después de la actualización. 

Utilice esta etiqueta Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en la parte superior de su mensaje y, a continuación, utilice {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acceder a los datos sobre ese elemento a lo largo de todo el mensaje.

## Consideraciones

- Los usuarios se suscriben por 90 días. Si un artículo no baja de precio en 90 días, el usuario se da de baja de la suscripción.
- Cuando se utiliza la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 usuarios en 10 minutos.
- Braze procesará hasta 10 actualizaciones de artículos por minuto. Esto significa que si actualizas 11 artículos en un minuto, solo los 10 primeros pueden desencadenar una notificación de bajada de precio.

[1]: {% image_buster /assets/img/price_drop_notifications.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
