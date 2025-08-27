---
nav_title: Objetos anidados
article_title: Objetos anidados en eventos personalizados
page_order: 1
page_type: reference
description: "En este artículo se describe cómo enviar datos JSON anidados como propiedades de eventos y compras personalizados, y cómo utilizar esos objetos anidados en la mensajería."
---

# Objetos anidados en eventos personalizados

> Esta página explica cómo enviar datos JSON anidados como propiedades de eventos personalizados y compras, y cómo utilizar esos objetos anidados en tu mensajería.

Puede utilizar objetos anidados -objetos que están dentro de otro objeto- para enviar datos JSON anidados como propiedades de eventos y compras personalizados. Estos datos anidados pueden utilizarse para plantillas de información personalizada en los mensajes, desencadenar envíos de mensajes y segmentar a los usuarios.

## Limitaciones

- Los datos anidados son compatibles con los [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) y [los eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), pero no con otros tipos de eventos.
- Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 100 KB.
- No se pueden generar esquemas de propiedades de eventos para eventos de compra.
- Los esquemas de propiedades de eventos se generan mediante el muestreo de eventos personalizados de las últimas 24 horas.

### Versiones mínimas del SDK

Las siguientes versiones del SDK admiten objetos anidados:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Paso 1: Generar un esquema

Puedes acceder a los datos anidados de tu evento personalizado generando un esquema para cada evento con propiedades de eventos anidados. Para generar un esquema:

1. Vaya a **Configuración de datos** > **Eventos personalizados**.
2. Seleccione **Gestionar propiedades** para los eventos con propiedades anidadas.
3. Seleccione el botón <i class="fas fa-arrows-rotate"></i> para generar el esquema. Para ver el esquema, seleccione el botón <i class="fas fa-plus"></i> plus.

![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Si se envían nuevas propiedades en el futuro, no estarán en el esquema hasta que se regenere. Los esquemas pueden regenerarse cada 24 horas.

## Paso 2: Utilizar el objeto anidado

Puedes hacer referencia a los datos anidados durante la segmentación y la personalización. Nota que no es necesario un esquema. Consulte los siguientes apartados para ver ejemplos de uso:

- [Cuerpo de la solicitud API](#api-request-body)
- [Plantillas de Liquid](#liquid-templating)
- [Desencadenamiento de mensajes](#message-triggering)
- [Segmentación](#segmentation)
- [Personalización](#personalization)

### Cuerpo de la solicitud API

{% tabs %}
{% tab Ejemplo de música %}

A continuación se muestra un ejemplo de `/users/track` con un evento personalizado "Lista de reproducción creada". Una vez creada una lista de reproducción, captura las propiedades de la lista enviando:
- Una solicitud a la API que incluye "canciones" como propiedad
- Una matriz de las propiedades anidadas de las canciones

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Ejemplo de restaurante%}

A continuación se muestra un ejemplo de `/users/track` con un evento personalizado "Ordenado". Una vez completado un pedido, captura las propiedades de ese pedido enviando:
- Una solicitud a la API que incluye "r_detalles" como propiedad
- Las propiedades anidadas de ese orden

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para las propiedades de eventos personalizados anidados, si el año es menor que 0 o mayor que 3000, Braze no almacena estos valores en el usuario.
{% endalert %}

### Plantillas de Liquid

A continuación se muestra cómo crear una plantilla Liquid que haga referencia a las propiedades anidadas solicitadas en la [petición API anterior](#api-request-body).

{% tabs %}
{% tab Ejemplo de música %}
Plantillas en Liquid en un mensaje activado por el evento "Lista de reproducción creada":

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "Mientras mi guitarra llora suavemente"
{% endraw %}

{% endtab %}
{% tab Ejemplo de restaurante %}
Plantillas en Liquid en un mensaje activado por el evento "Ordenado":

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Desencadenamiento de mensajes

Para utilizar estas propiedades para desencadenar una campaña, selecciona tu evento personalizado o compra y, a continuación, añade un filtro de **propiedades anidadas**. Tenga en cuenta que la activación de mensajes aún no es compatible con los mensajes dentro de la aplicación, pero las propiedades anidadas en la personalización de Liquid en los mensajes seguirán mostrándose.

{% tabs %}
{% tab Ejemplo de música %}

Lanzamiento de una campaña con propiedades anidadas desde el evento "Lista de reproducción creada":

![Un usuario que elige una propiedad anidada para filtros de propiedades en un evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

La condición de activación `songs[].album.yearReleased` "is" "1968" coincidirá con un evento en el que cualquiera de las canciones tenga un álbum publicado en 1968. Utilizamos la notación de corchetes `[]` para recorrer matrices y comprobar si **algún** elemento de la matriz recorrida coincide con la propiedad del evento.

{% alert important %}
El filtro **no es igual** sólo coincide si ninguna de las propiedades de tu matriz es igual al valor proporcionado. <br><br>Por ejemplo, digamos que el Canvas A tiene el filtro de propiedades anidadas evento personalizado basado en acciones **igual a** "smartwatch", y el Canvas B tiene el filtro de propiedades anidadas evento personalizado basado en acciones **no igual a** "simphone". Si tienes "smartwatch" y "simphone" en tus propiedades, se desencadenarán ambos Lienzos. Pero si tienes "simphone" o "sólo sim" en alguna propiedad, no se desencadenará ningún Canvas.
{% endalert %}

{% endtab %}
{% tab Ejemplo de restaurante %}

Lanzamiento de una campaña con propiedades anidadas desde el evento "Ordenado":

![Un usuario que añade el filtro de propiedad r_details.name es McDonalds para un evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Si su propiedad de evento contiene los caracteres `[]` o `.`, escápelos envolviendo el trozo entre comillas dobles. Por ejemplo, `"songs[].album".yearReleased` coincidirá con un evento con la propiedad literal `"songs[].album"`.
{% endalert %}

### Segmentación

Para segmentar usuarios basándose en propiedades de eventos anidados, debe utilizar [Extensiones de Segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Una vez generado el esquema, aparecerá el explorador de objetos anidados en la sección de segmentación. 

![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

La segmentación utiliza la misma notación que la activación (véase [Activación de mensajes](#message-triggering)).

Para editar o crear extensiones de segmento, necesitarás el permiso "Editar segmentos".

### Personalización

Utilizando el modal **Añadir Personalización**, seleccione **Propiedades Avanzadas de Eventos** como tipo de personalización. Permite añadir propiedades de eventos anidados después de generar un esquema.

![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Preguntas más frecuentes

### ¿El uso de objetos anidados consume puntos de datos adicionales?

No hay ningún cambio en la forma de cobrar los puntos de datos como resultado de añadir esta capacidad. La segmentación basada en objetos anidados utiliza extensiones de segmento, que no incurren en un uso de punto de datos adicional.

### ¿Cuántos datos anidados se pueden enviar?

Si una o más de las propiedades del evento contienen datos anidados, la carga útil máxima para todas las propiedades combinadas de un evento es de 100 KB. Cualquier solicitud que supere ese límite de tamaño será rechazada.

