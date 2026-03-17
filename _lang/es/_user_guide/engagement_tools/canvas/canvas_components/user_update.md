---
nav_title: Actualización del usuario
article_title: Actualización de usuario 
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Este artículo de referencia cubre el componente Actualización de usuario y cómo utilizarlo en sus lienzos."
tool: Canvas
---

# Actualización de usuario 

> El componente Actualización de usuario te permite actualizar los atributos, eventos y compras de un usuario en un editor JSON, por lo que no es necesario incluir información confidencial como claves de API.

## Cómo funciona este componente

![Un paso de actualización de usuario denominado «Actualizar fidelización» que actualiza el atributo «Es miembro Premium» a «verdadero».]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Cuando utilices este componente en tu Canvas, las actualizaciones no se tendrán en cuenta para el `/users/track`límite de velocidad. En su lugar, estas actualizaciones se agrupan por lotes para que Braze pueda procesarlas con mayor eficacia que un webhook de Braze a Braze. Ten en cuenta que este componente no registra [puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) cuando se utiliza para actualizar puntos de datos no facturables (como grupos de suscripción).

Una vez que los usuarios entran en el paso Actualización de usuario y se completa el procesamiento, avanzan al siguiente paso. Esto significa que cualquier mensaje de mensajería posterior que se base en estas actualizaciones de los usuarios estará actualizado cuando se ejecute el siguiente paso.

## Creación de una actualización de usuario

Arrastrar y soltar el componente desde la barra lateral, o selecciona el botón<i class="fas fa-plus-circle"></i> más situado en la parte inferior de la variante o el paso y selecciona **Actualización de usuario**. 

Hay tres opciones que te permiten actualizar la información del perfil de usuario existente, añadir nueva información o eliminar información del perfil de usuario. En conjunto, los pasos de actualización de usuarios en un espacio de trabajo pueden actualizar hasta 200.000 perfiles de usuario por minuto.

{% alert tip %}
También puede probar los cambios realizados con este componente buscando un usuario y aplicándole el cambio. Esto actualizará el usuario.
{% endalert %}

## Actualización de atributos personalizados

Para actualizar o eliminar un atributo personalizado, selecciona un nombre de atributo de la lista de atributos e introduce el valor.

![Paso de actualización de usuario que actualiza los dos atributos «Miembro del programa de fidelización» y «Programa de fidelización» a «verdadero».]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Eliminar atributos personalizados

Para eliminar un atributo personalizado, seleccione un nombre de atributo utilizando el desplegable. Puedes cambiar al [editor JSON avanzado](#advanced-json-editor) para seguir editando. 

![Paso de actualización de usuario que elimina el atributo «Miembro de fidelización».]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valores crecientes y decrecientes

El paso Actualización del usuario puede aumentar o disminuir el valor de un atributo. Seleccione el atributo, elija **Incrementar por** o **Disminuir por** e introduzca un número. 

#### Hacer un seguimiento semanal

Incrementando un atributo personalizado que rastrea un evento, puede rastrear el número de clases que un usuario ha tomado en una semana. Utilizando este componente, el recuento de clases puede reiniciarse al comienzo de la semana y comenzar el seguimiento de nuevo. 

![Paso de actualización del usuario que incrementa el atributo"class_count"en uno.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Actualizar una matriz de objetos

Una [matriz de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) es un atributo personalizado rico en datos que se almacena en el perfil de usuario. Puedes utilizarlo para crear un historial de las interacciones del usuario con tu marca y para crear segmentos basados en un campo calculado, como el historial de compras o el valor de duración del ciclo de vida.

Con la opción **Editor JSON avanzado**, puedes insertar JSON para añadir o eliminar elementos de esta matriz de objetos.

#### Casos de uso: Actualizar la lista de deseos de un usuario

Realiza un seguimiento de la lista de deseos de los usuarios para poder realizar segmentación o personalización en función de los artículos que hayan guardado.

1. Crea un atributo personalizado que sea una matriz de objetos, por ejemplo `wishlist`. Cada objeto puede incluir campos como `product_id`, `product_name`, y `added_at`.
2. En el paso Actualización de usuario, selecciona **Editor JSON avanzado**. A continuación, en la sección **Componer**, utiliza la`$add`operación  para añadir un elemento o la`$remove`operación  para eliminar un elemento por su valor.

A continuación se muestra un ejemplo de cómo añadir un artículo a la lista de deseos:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Para eliminar un elemento, utiliza`"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }`  con la misma estructura de objeto para que Braze pueda encontrarlo y eliminarlo.

#### Casos de uso: Calcular el total de la cesta de la compra

Realice un seguimiento de cuándo un usuario tiene artículos en su cesta de la compra, cuándo añade nuevos artículos o los elimina, y cuál es el valor total de la cesta de la compra. 

1. Crea una matriz de objetos personalizada llamada `shopping_cart`. El siguiente ejemplo muestra el aspecto que puede tener este atributo. Cada elemento tiene un  único`product_id`que contiene datos adicionales en su propia matriz anidada de objetos, incluyendo `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\. Crear un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) llamado `add_item_to_cart` que se registra cuando un usuario añade un artículo a la cesta.
3\. Crea un Canvas dirigido a los usuarios que realizan este evento personalizado. Ahora, cuando un usuario añade un artículo a su cesta, se activa este Canvas. A continuación, puede dirigir mensajes directamente a ese usuario, ofreciéndole códigos de cupón cuando haya alcanzado un determinado nivel de gasto, haya abandonado su cesta durante un determinado periodo de tiempo o cualquier otra cosa que se ajuste a su caso de uso. 

El atributo `shopping_cart` lleva el total de muchos eventos personalizados: el coste total de todos los artículos, el número total de artículos en el carrito, si el carrito contiene un regalo, etc. Esto puede parecerse a lo siguiente:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Establecer la propiedad de entrada Canvas como atributo

Puedes utilizar el paso de actualización de usuario para persistir un `canvas_entry_property`. Digamos que tienes un evento que se dispara cuando se añade un artículo al carrito. Puede almacenar el ID del último artículo añadido al carrito y utilizarlo para una campaña de remarketing. Utilice la función de personalización para recuperar una propiedad de entrada de Canvas y almacenarla en un atributo.

![Paso de actualización de usuario que actualiza el atributo"most_recent_cart_item"  con un ID de elemento.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalización

Para almacenar la propiedad del evento desencadenante de un Canvas como atributo, utilice el modal de personalización para extraer y almacenar la propiedad de entrada del Canvas. La actualización de usuarios también admite las siguientes funciones de personalización:

* [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propiedades de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Lógica líquida (incluidos los [mensajes de cancelación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Múltiples actualizaciones de atributos o eventos por objeto

{% alert warning %}
Recomendamos un uso cuidadoso de la personalización de Connected Content Liquid en los pasos de actualización de usuarios, ya que este tipo de paso tiene un límite de tasa de 200.000 solicitudes por minuto. Este límite de tarifa anula el límite de tarifa del Lienzo.
{% endalert %}

## Editor JSON avanzado

Añade un atributo, evento u objeto JSON de compra de hasta 65 536 caracteres al editor JSON. También se puede establecer el estado de la [suscripción global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) y del [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) de un usuario.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Con el editor JSON, también puedes obtener una vista previa y comprobar que el perfil de usuario se actualiza con los cambios realizados en la pestaña **Vista previa y prueba**. Puede seleccionar un usuario al azar o buscar un usuario concreto. A continuación, tras enviar una prueba a un usuario, visualice el perfil del usuario utilizando el enlace generado.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Consideraciones

No es necesario que incluyas datos confidenciales, como tu clave de API, al utilizar el editor JSON, ya que la plataforma los proporciona automáticamente. Los siguientes campos no deben incluirse en el editor JSON:
* ID de usuario externo
* Clave de API
* URL del clúster Braze
* Campos relacionados con la importación de fichas push

{% alert important %}
Las propiedades de Canvas (como las etiquetas`canvas_id` ,`canvas_name`  y`canvas_variant_name`  de Liquid) no son compatibles con los pasos de actualización de usuario.
{% endalert %}

{% raw %}
### Registrar eventos personalizados

Con el editor JSON, también puedes registrar eventos personalizados. Nota: Esto requiere una marca de tiempo en formato ISO, por lo que es necesario asignar una hora y una fecha con Liquid al principio. Considere este ejemplo que registra un evento con una hora.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

El siguiente ejemplo vincula un evento a una aplicación específica utilizando un evento personalizado con propiedades opcionales y la dirección `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Editar el estado de la suscripción

Dentro del editor JSON, también puedes editar el estado de la suscripción de un usuario. Por ejemplo, a continuación se muestra el estado de suscripción de un usuario actualizado a `opted_in`. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Actualizar los grupos de suscripción 

También puede actualizar los grupos de suscripción mediante este paso de Canvas. El siguiente ejemplo muestra cómo actualizar uno o varios grupos de suscripción.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

