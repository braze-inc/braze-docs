---
nav_title: Actualización de usuario 
article_title: Actualización de usuario 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre el componente Actualización de usuario y cómo utilizarlo en sus lienzos."
tool: Canvas
---

# Actualización de usuario 

> El componente Actualización de usuario permite actualizar los atributos, eventos y compras de un usuario en un compositor JSON, por lo que no es necesario incluir información confidencial como claves API.

## Cómo funciona este componente

![Un paso de actualización de usuario llamado "Actualizar fidelización" que actualiza un atributo "Es miembro Premium" a "true".]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Cuando utilices este componente en tu Canvas, las actualizaciones no cuentan para el límite de velocidad de `/users/track` peticiones por minuto. En su lugar, estas actualizaciones se agrupan por lotes para que Braze pueda procesarlas con mayor eficacia que un webhook de Braze a Braze. Tenga en cuenta que este componente no consume [puntos de datos]({{site.baseurl}}/user_guide/data/data_points/) cuando se utiliza para actualizar puntos de datos no facturables (como grupos de suscripción).

Los usuarios sólo avanzarán a los siguientes pasos de Canvas una vez que hayan completado las actualizaciones de usuario pertinentes. Esto significa que cualquier mensajería posterior que dependa de estas actualizaciones del usuario estará actualizada cuando se ejecute el siguiente paso.

## Creación de una actualización de usuario

Arrastre y suelte el componente desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de la variante o paso y seleccione **Actualización de usuario**. 

Hay tres opciones que le permiten actualizar la información del perfil de usuario existente, añadir nueva o eliminarla. En conjunto, los pasos de actualización de usuarios en un espacio de trabajo pueden actualizar hasta 200.000 perfiles de usuario por minuto.

{% alert tip %}
También puede probar los cambios realizados con este componente buscando un usuario y aplicándole el cambio. Esto actualizará el usuario.
{% endalert %}

### Actualización de atributos personalizados

Para añadir o actualizar un atributo personalizado, seleccione un nombre de atributo de su lista de atributos e introduzca el valor clave.

![Paso de actualización de usuario que actualiza los dos atributos "Miembro de fidelización" y "Programa de fidelización" a "verdadero".]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Eliminar atributos personalizados

Para eliminar un atributo personalizado, seleccione un nombre de atributo utilizando el desplegable. Puede cambiar al [compositor JSON avanzado](#advanced-json-composer) para seguir editando. 

![Paso de actualización de usuario que elimina un atributo "Miembro fidelizado".]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Valores crecientes y decrecientes

El paso de actualización del usuario puede aumentar o disminuir el valor de un atributo. Seleccione el atributo, elija **Incrementar por** o **Disminuir por** e introduzca un número. 

#### Hacer un seguimiento semanal

Incrementando un atributo personalizado que rastrea un evento, puede rastrear el número de clases que un usuario ha tomado en una semana. Utilizando este componente, el recuento de clases puede reiniciarse al comienzo de la semana y comenzar el seguimiento de nuevo. 

![Paso de actualización del usuario que incrementa en uno el atributo "class_count".]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Actualizar una matriz de objetos

Un [array de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) es un atributo personalizado almacenado en el perfil de un usuario que es rico en datos. Esto le permite crear un historial de las interacciones del usuario con su marca. Esto le permite crear segmentos basados en un atributo personalizado que es un campo calculado, como el historial de compras o el valor total del tiempo de vida.

El paso de actualización de usuario puede añadir o eliminar atributos a esta matriz de objetos. Para actualizar una matriz, seleccione el nombre del atributo de la matriz en su lista de atributos e introduzca el valor de la clave.

#### Caso de uso: Actualizar la lista de deseos de un usuario

Al añadir o eliminar un elemento de una matriz se actualiza la lista de deseos del usuario.

![Paso de actualización de usuario que añade un elemento "bloqueador solar" al atributo "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Caso de uso: Calcular el total de la cesta de la compra

Realice un seguimiento de cuándo un usuario tiene artículos en su cesta de la compra, cuándo añade nuevos artículos o los elimina, y cuál es el valor total de la cesta de la compra. 

1. Cree una matriz personalizada de objetos llamada `shopping_cart`. El siguiente ejemplo muestra el aspecto que puede tener este atributo. Cada elemento tiene un único `product_id` que tiene datos más complejos en su propia matriz anidada de objetos, incluyendo `price`.

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
3\. Crea un Canvas con un público objetivo de usuarios con este evento personalizado. Ahora, cuando un usuario añade un artículo a su cesta, se activa este Canvas. A continuación, puede dirigir mensajes directamente a ese usuario, ofreciéndole códigos de cupón cuando haya alcanzado un determinado nivel de gasto, haya abandonado su cesta durante un determinado periodo de tiempo o cualquier otra cosa que se ajuste a su caso de uso. 

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
         "product_id": ["1001", "1002"]
         "gift": yes,
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

![Paso de actualización de usuario que actualiza el atributo "most_recent_cart_item" con un ID de artículo.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

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

## Compositor JSON avanzado

Añade un objeto JSON de atributo, evento o compra de hasta 65 536 caracteres al compositor JSON. También se puede establecer el estado de la [suscripción global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) y del [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) de un usuario.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Mediante el compositor avanzado, también puede previsualizar y probar que el perfil de usuario se actualiza con los cambios con la pestaña **Previsualizar y probar**. Puede seleccionar un usuario al azar o buscar un usuario concreto. A continuación, tras enviar una prueba a un usuario, visualice el perfil del usuario utilizando el enlace generado.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Consideraciones

No es necesario que incluyas datos confidenciales como tu clave de API al utilizar el compositor JSON, ya que la plataforma los proporciona automáticamente. Por lo tanto, los siguientes campos no son necesarios y no deben utilizarse en el compositor JSON:
* ID de usuario externo
* Clave de API
* URL del clúster Braze
* Campos relacionados con la importación de fichas push

{% raw %}
### Registrar eventos personalizados

Utilizando el compositor JSON, también puedes registrar eventos personalizados. Tenga en cuenta que esto requiere una marca de tiempo en formato ISO, por lo que es necesario asignar una hora y una fecha con Liquid al principio. Considere este ejemplo que registra un evento con una hora.

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

Dentro del compositor JSON, también puede editar el estado de suscripción de su usuario. Por ejemplo, a continuación se muestra el estado de suscripción de un usuario actualizado a `opted_in`. 

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

También puede actualizar los grupos de suscripción mediante este paso de Canvas. El siguiente ejemplo muestra una actualización de los grupos de suscripción. Puede realizar una o varias actualizaciones de grupos de suscripción.

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

