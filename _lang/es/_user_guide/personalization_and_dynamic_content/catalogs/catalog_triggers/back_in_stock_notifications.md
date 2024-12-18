---
nav_title: Notificaciones de existencias
article_title: Notificaciones de existencias
page_order: 2
description: "Este artículo de referencia describe cómo crear notificaciones de falta de existencias en los catálogos Braze."
---

# Notificaciones de existencias

> Mediante una combinación de notificaciones de reposición de existencias a través de los catálogos Braze y un Canvas, puede notificar a los clientes cuándo un artículo vuelve a estar disponible. Cada vez que un cliente realiza un evento personalizado seleccionado, puede suscribirse automáticamente para recibir una notificación cuando se reponga el artículo.

{% alert important %}
Las notificaciones de agotamiento de existencias de los catálogos se encuentran actualmente en fase de acceso anticipado. Póngase en contacto con su gestor de cuenta si está interesado en participar en este acceso anticipado.
{% endalert %}

Cuando un usuario active un evento personalizado para un artículo, lo suscribiremos automáticamente para que reciba notificaciones de reposición de existencias de ese artículo. Cuando la cantidad de inventario del artículo cumpla tu regla de inventario (como un inventario superior a 100), todos los suscriptores serán elegibles para recibir notificaciones a través de una campaña o Canvas. Sin embargo, sólo los usuarios que hayan optado por recibir notificaciones las recibirán. 

## Cómo funcionan las notificaciones de reposición de existencias

Configurará un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Le sugerimos que incluya un nombre de catálogo, pero no es obligatorio. También proporcionará el nombre de un campo de cantidad de inventario, que debe ser de tipo dato numérico.

Cuando un artículo tiene una cantidad de inventario que cumple su regla de inventario, buscaremos a todos sus usuarios suscritos a ese artículo (usuarios que realizaron el evento de suscripción) y enviaremos un evento personalizado Braze que puede utilizar para activar una campaña o Canvas.

Las propiedades del evento se envían junto con el usuario, por lo que puede introducir los detalles del elemento en la campaña o el lienzo que envía.

## Configurar las notificaciones de reposición de existencias

Siga estos pasos para configurar las notificaciones de agotado en un catálogo específico.

1. Vaya a su catálogo y seleccione la pestaña **Configuración**.
2. Seleccione la opción **Volver a existencias**.
3. Si no se han configurado los ajustes globales de reposición de existencias, se le pedirá que configure los eventos y propiedades personalizados que se utilizarán para activar las notificaciones de reposición de existencias:
    <br> ![Cajón de configuración del catálogo.][2]{: style="max-width:70%;"}
    - **Evento personalizado para suscripciones** es el evento personalizado Braze que se utilizará para suscribir a un usuario a las notificaciones de reposición de existencias. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado.
    - **Evento personalizado para darse de baja** es el evento personalizado Braze que se utilizará para dar de baja a un usuario de las notificaciones de reposición de existencias.
    - **La propiedad del evento ID del artículo** es la propiedad del evento personalizado anterior que se utilizará para determinar el artículo para una suscripción o desuscripción de nuevo en stock. Esta propiedad del evento personalizado debe contener un ID de artículo, que esté presente en un catálogo. El evento personalizado también debe contener una propiedad `catalog_name`, para especificar en qué catálogo se encuentra este artículo.
    - **Catálogo alternativo** Éste es el catálogo que se utilizará para la suscripción de reserva, si no hay ninguna propiedad `catalog_name` presente en el evento personalizado.
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
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
Los desencadenadores de reserva y de bajada de precio utilizan el mismo evento para suscribir al usuario a la notificación. Crea una notificación de bajada de precio configurando `type` en `back-in-stock`. No puedes establecer tanto una notificación de bajada de precio como de reabastecimiento.
{% endalert %}

{: start="4"}
4\. Seleccione **Guardar** y continúe en la página **Configuración** del catálogo.
5\. Establezca su regla de notificación. Hay dos opciones:
    - **Notificar a todos los usuarios suscritos** notifica a todos los clientes que están esperando cuando el artículo vuelve a estar disponible.
    - **Notificar a un número determinado de usuarios por un número determinado de minutos** notifica a un número determinado de clientes por tu periodo de notificación configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar o hasta que el artículo se agote. El ritmo de notificación no puede superar los 10.000 usuarios por minuto.
6\. Establezca el **campo Inventario en el catálogo**. Este campo del catálogo se utilizará para determinar si el artículo está agotado. El campo debe ser de tipo numérico.
7\. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la función de reposición de existencias activada. Las reglas de notificación consisten en notificar a mil usuarios cada diez minutos.][1]

{% alert important %}
Las reglas de notificación de estos ajustes no sustituyen a los ajustes de notificación de Canvas, como Horas de silencio.
{% endalert %}

## Utilizar las notificaciones de agotado en un lienzo

Después de configurar la función de reserva de existencias en un catálogo, siga estos pasos para utilizarla con Canvas.

1. Establezca un lienzo basado en acciones.
2. Seleccione **Volver a existencias** como desencadenante.
3. Seleccione el nombre del catálogo con las notificaciones de reposición de existencias.
4. Continúe [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) su lienzo como lo haría.

Ahora, sus clientes pueden recibir una notificación cuando un artículo vuelva a estar disponible.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que vuelve a estar disponible, puedes utilizar la etiqueta de Liquid `canvas_entry_properties` para acceder a `item_id`. 

El uso de {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} devolverá el ID del artículo que volvió a estar en stock. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} devolverá el valor de inventario del artículo antes de la actualización, y {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} devolverá el nuevo valor de inventario después de la actualización.

Utilice esta etiqueta Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en la parte superior de su mensaje y, a continuación, utilice {%raw%}``{{ items[0].<field_name> }}``{%endraw%} para acceder a los datos sobre ese elemento a lo largo de todo el mensaje.

## Consideraciones

- Los usuarios sólo están suscritos durante 90 días. Si el artículo no vuelve a estar disponible en 90 días, el usuario se da de baja.
- Cuando se utiliza la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 en 10 minutos.
- Braze procesará como máximo 10 actualizaciones de elementos en un minuto. Si actualizas 11 artículos en un minuto, solo los 10 primeros pueden desencadenar una notificación de reposición de existencias.

[1]: {% image_buster /assets/img/back_in_stock_settings.png %}
[2]: {% image_buster /assets/img/catalog_settings_drawer.png %}
