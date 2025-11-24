---
nav_title: Objetos anidados
article_title: Objetos anidados en eventos personalizados
page_order: 1
page_type: reference
description: "Este artículo describe cómo enviar datos JSON anidados como propiedades de eventos personalizados y compras, y cómo utilizar esos objetos anidados en tu mensajería."
---

# Objetos anidados en eventos personalizados

> Esta página explica cómo enviar datos JSON anidados como propiedades de eventos personalizados y compras, y cómo utilizar esos objetos anidados en tu mensajería.

Puedes utilizar objetos anidados -objetos que están dentro de otro objeto- para enviar datos JSON anidados como propiedades de eventos personalizados y compras. Estos datos anidados pueden utilizarse para plantillas de información personalizada en los mensajes, desencadenar envíos de mensajes y segmentar a los usuarios.

## Limitaciones

- Los datos anidados son compatibles con los [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) y [los eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), pero no con otros tipos de eventos.
- Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 100 KB.
- No se pueden generar esquemas de propiedades del evento para los eventos de compra.
- Los esquemas de propiedades de eventos se generan mediante el muestreo de eventos personalizados de las últimas 24 horas.

### Versiones mínimas del SDK

Las siguientes versiones del SDK admiten objetos anidados:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Paso 1: Generar un esquema

Puedes acceder a los datos anidados de tu evento personalizado generando un esquema para cada evento con propiedades de eventos anidados. Para generar un esquema:

1. Ve a **Configuración de datos** > Eventos personalizados.
2. Selecciona **Gestionar propiedades** para los eventos con propiedades anidadas.
3. Selecciona el botón <i class="fas fa-arrows-rotate"></i> para generar el esquema. Para ver el esquema, selecciona el botón <i class="fas fa-plus"></i> plus.

\![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Si se envían nuevas propiedades en el futuro, no estarán en el esquema hasta que se regenere. Los esquemas pueden regenerarse cada 24 horas.

## Paso 2: Utiliza el objeto anidado

Puedes hacer referencia a los datos anidados durante la segmentación y la personalización. Nota que no es necesario un esquema. Consulta las secciones siguientes para ver ejemplos de uso:

- [Cuerpo de la solicitud API](#api-request-body)
- [Plantilla líquida](#liquid-templating)
- [Desencadenar mensajes](#message-triggering)
- [Segmentación](#segmentation)
- [Personalización](#personalization)

### Cuerpo de la solicitud API

{% tabs %}
{% tab Music Example %}

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
{% tab Restaurant Example%}

A continuación se muestra un ejemplo de `/users/track` con un evento personalizado "Ordenado". Una vez completado un pedido, captura las propiedades de ese pedido enviando:
- Una solicitud a la API que enumera "r_details" como propiedad
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

### Plantilla líquida

A continuación se muestra cómo crear una plantilla Liquid que haga referencia a las propiedades anidadas solicitadas en la [petición API anterior](#api-request-body).

{% tabs %}
{% tab Music Example %}
Plantilla en Liquid en un mensaje desencadenado por el evento "Lista de reproducción creada":

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "No importa"<br>
`{{event_properties.${songs}[1].title}}`: "Mientras mi guitarra llora suavemente"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Plantilla en Liquid en un mensaje desencadenado por el evento "Ordenado":

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Desencadenar mensajes

Para utilizar estas propiedades para desencadenar una campaña, selecciona tu evento personalizado o compra y, a continuación, añade un filtro de **propiedades anidadas**. Ten en cuenta que la desencadenación de mensajes aún no es compatible con los mensajes dentro de la aplicación, pero las propiedades anidadas en la personalización de Liquid en los mensajes seguirán mostrándose.

{% tabs %}
{% tab Music Example %}

Desencadenar una campaña con propiedades anidadas del evento "Lista de reproducción creada":

\![Un usuario que elige una propiedad anidada para filtrar propiedades en un evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

La condición desencadenante `songs[].album.yearReleased` "es" "1968" coincidirá con un evento en el que cualquiera de las canciones tenga un álbum publicado en 1968. Utilizamos la notación de corchetes `[]` para recorrer matrices, y coincidimos si **algún** elemento de la matriz recorrida coincide con la propiedad del evento.

{% alert important %}
El filtro **no es igual** sólo coincide si ninguna de las propiedades de tu matriz es igual al valor proporcionado. <br><br>Por ejemplo, digamos que el Canvas A tiene el filtro de propiedades anidadas evento personalizado basado en acciones **igual a** "smartwatch", y el Canvas B tiene el filtro de propiedades anidadas evento personalizado basado en acciones **no igual a** "simphone". Si tienes "smartwatch" y "simphone" en tus propiedades, se desencadenarán ambos Lienzos. Pero si tienes "simphone" o "sólo sim" en alguna propiedad, no se desencadenará ningún Canvas.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Desencadenar una campaña con propiedades anidadas del evento "Ordenado":

\![Un usuario que añade el filtro de propiedades r_details.name es McDonalds para un evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Si tu propiedad de evento contiene los caracteres `[]` o `.`, escápalos encerrando el fragmento entre comillas dobles. Por ejemplo, `"songs[].album".yearReleased` coincidirá con un evento con la propiedad literal `"songs[].album"`.
{% endalert %}

### Segmentación

Para segmentar a los usuarios en función de las propiedades de eventos anidados, debes utilizar las [Extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Cuando hayas generado un esquema, aparecerá el explorador de objetos anidados en la sección de segmentación. 

\![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

La segmentación utiliza la misma notación que la desencadenación (ver [Desencadenación de mensajes](#message-triggering)).

Para editar o crear extensiones de segmento, necesitarás el permiso "Editar segmentos".

### Personalización

Utilizando el modal **Añadir personalización**, selecciona **Propiedades del evento avanzadas** como tipo de personalización. Permite añadir propiedades de eventos anidados después de generar un esquema.

\![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Preguntas más frecuentes

### ¿El uso de objetos anidados registra puntos de datos adicionales?

No hay ningún cambio en cómo registramos los puntos de datos como resultado de añadir esta capacidad. La segmentación basada en objetos anidados utiliza Extensiones de segmento, que no utilizan puntos de datos adicionales.

### ¿Cuántos datos anidados se pueden enviar?

Si una o más de las propiedades del evento contienen datos anidados, la carga útil máxima para todas las propiedades combinadas de un evento es de 100 KB. Cualquier solicitud que supere ese límite de tamaño será rechazada.

