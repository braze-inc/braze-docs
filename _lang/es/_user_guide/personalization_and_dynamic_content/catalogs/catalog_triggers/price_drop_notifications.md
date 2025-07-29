---
nav_title: Notificaciones de bajada de precios
article_title: Notificaciones de bajada de precios
page_order: 3
alias: "/price_drop_notifications/"
description: "Este artículo de referencia describe cómo crear notificaciones de bajada de precios en catálogos Braze."
---

# Notificaciones de bajada de precios

> Esta página explica cómo funcionan las notificaciones de bajada de precios y cómo puedes configurarlas y utilizarlas. Con una combinación de notificaciones de bajada de precios a través de los catálogos Braze y un Canvas, puedes notificar a los clientes cuando el precio de un artículo ha bajado.

## Cómo funciona

Cuando un usuario active un evento personalizado para un artículo, le suscribiremos automáticamente para que reciba notificaciones de bajadas de precio de ese artículo. Cuando el precio del artículo cumpla tu regla de inventario (como una caída superior al 50 %), todos los suscriptores serán elegibles para recibir notificaciones a través de una campaña o Canvas. Sin embargo, sólo los usuarios que hayan optado por recibir notificaciones las recibirán. 

## Configuración de un evento personalizado para notificaciones de bajada de precios

Configurará un evento personalizado para utilizarlo como evento de suscripción, como por ejemplo `product_clicked`. Este evento debe contener una propiedad del ID del artículo (ID de artículos del catálogo). Recomendamos incluir un nombre de catálogo, pero no es obligatorio. También proporcionarás el nombre de un campo de precio, que debe ser un tipo de dato numérico. 



- Un usuario realiza un evento personalizado seleccionado
- El evento personalizado tiene una propiedad `type` que incluye `price_drop` (`type` debe ser una matriz)

 Cuando un artículo tenga un cambio de precio que cumpla su regla de precios, buscaremos a todos sus usuarios suscritos a ese artículo (usuarios que realizaron el evento de suscripción) y enviaremos un evento personalizado Braze que puede utilizar para activar una campaña o Canvas. 

Las propiedades del evento se envían junto con tu usuario, por lo que puedes introducir la plantilla con los detalles del elemento en la campaña o Canvas que envía.

## Configurar las notificaciones de bajada de precios

Siga estos pasos para configurar las notificaciones de bajada de precios en un catálogo específico.

1. Vaya a su catálogo y seleccione la pestaña **Configuración**.
2. Selecciona el botón alternativo **Caída de precios**.
3. Si no se han configurado los ajustes globales del catálogo, se te pedirá que configures los eventos personalizados y las propiedades que se utilizarán para desencadenar las notificaciones. <br><br> 

| Campo | Descripción |
| --- | --- |
| **Catálogo alternativo** | El catálogo utilizado para la suscripción si no hay una propiedad `catalog_name` en el evento personalizado. |
| **Evento personalizado para suscriptores** | El evento personalizado utilizado para suscribir a un usuario a las notificaciones del catálogo. Cuando se produzca este evento, se suscribirá el usuario que lo haya realizado. |
| **Evento personalizado para cancelar suscripciones** | El evento personalizado utilizado para cancelar la suscripción de un usuario a las notificaciones. Este evento es opcional. Si el usuario no realiza este evento, se le cancelará la suscripción transcurridos 90 días o cuando se desencadene el evento de bajada de precio, lo que ocurra primero. |
| **Propiedad del evento de ID de elemento** | La propiedad en el evento personalizado anterior que se utiliza para determinar el elemento para una suscripción o desuscripción. Esta propiedad del evento personalizado debe contener un ID de artículo que exista en un catálogo. El evento personalizado debe contener una propiedad `catalog_name` para especificar en qué catálogo se encuentra este artículo. |
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
    - **Configura los límites de notificación:** Notifica a un número determinado de clientes según el periodo de notificación que hayas configurado. Braze notificará al número especificado de clientes en incrementos hasta que no haya más clientes a los que notificar, o hasta que el precio del artículo vuelva a subir. El ritmo de notificación no puede superar los 10.000 usuarios por minuto.<br>

2. Configura el **campo Precio en el catálogo**. Es el campo del catálogo que se utilizará para determinar el precio del artículo. Debe ser de tipo numérico.
3. Configura la **regla de caída de precios**. Esta es la lógica utilizada para determinar si se debe enviar una notificación. 
4. Selecciona **Guardar configuración**.

![Configuración del catálogo que muestra la función de bajada de precios activada. 

{% alert important %}
Las reglas de notificación de estos ajustes no sustituyen a los ajustes de notificación de Canvas, como Horas de silencio.
{% endalert %}

## 



1. Establezca un lienzo basado en acciones.
2. Seleccione **Realizar evento de caída de precio** como desencadenante.
3. Seleccione el nombre del catálogo con las notificaciones de bajada de precios.
4. Continúe [configurando]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) su lienzo como lo haría.

Ahora, sus clientes recibirán una notificación cuando baje el precio de un artículo.

### Utilizar Liquid

Para crear una plantilla con detalles sobre el artículo del catálogo que ha bajado de precio, puedes utilizar la etiqueta de Liquid `canvas_entry_properties` para acceder a `item_id`. 

 

Utilice esta etiqueta Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%} en la parte superior de su mensaje y, a continuación, utilice {%raw%}`{{items[0].<field_name>}}`{%endraw%} para acceder a los datos sobre ese elemento a lo largo de todo el mensaje.

## Consideraciones

- Los usuarios se suscriben por 90 días. Si un artículo no baja de precio en 90 días, el usuario se da de baja de la suscripción.
- Cuando se utiliza la regla de notificación **Notificar a todos los usuarios suscritos**, Braze notificará a 100.000 usuarios en 10 minutos.
-  

