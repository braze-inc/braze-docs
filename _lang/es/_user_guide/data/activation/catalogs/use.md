---
nav_title: Utilizar catálogos
article_title: Utilizar los catálogos
page_order: 1.5
description: "Este artículo de referencia explica cómo utilizar catálogos para hacer referencia a datos de no usuarios en tus campañas Braze a través de Liquid."
---

# Utilizar catálogos

> Después de crear un catálogo, puedes hacer referencia a datos de no usuarios en tus campañas Braze a través de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Puedes utilizar catálogos en todos tus canales de mensajería, incluso en cualquier lugar del editor de arrastrar y soltar donde se admita Liquid.

## Utilizar catálogos en un mensaje

### Paso 1: Añadir tipo de personalización {#step-one-personalization}

En el creador de mensajes de tu elección, selecciona el icono más <i class="fas fa-plus-circle"></i> para abrir el modal **Añadir personalización** y selecciona **Elementos del catálogo** para el **Tipo de personalización**. A continuación, selecciona el **Nombre de** tu **Catálogo**. Utilizando nuestro ejemplo anterior, seleccionaremos el catálogo "Juegos".

\![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver inmediatamente la siguiente vista previa de Liquid:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Paso 2: Selecciona artículos del catálogo

A continuación, ¡es hora de añadir los artículos de tu catálogo! Utilizando el desplegable, selecciona los elementos del catálogo y la información a mostrar. Esta información corresponde a las columnas de tu archivo CSV cargado, utilizado para generar tu catálogo.

Por ejemplo, para consultar el título y el precio de nuestro juego Tales, podríamos seleccionar `id` para Tales (1234) como elemento del catálogo y solicitar `title` y `price` para la información mostrada.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Esto se traduce en lo siguiente:

> Consigue Tales por sólo 7,49

## Exportar catálogos

Hay dos formas de exportar catálogos desde el panel: 

- Pasa el ratón por encima de la fila del catálogo en la sección **Catálogos**. A continuación, selecciona el botón **Exportar catálogo**.
- Selecciona tu catálogo. A continuación, selecciona el botón **Exportar catálogo** en la pestaña **Vista previa** del catálogo.

Recibirás un correo electrónico para descargar el archivo CSV después de iniciar la exportación. Tendrás hasta cuatro horas para recuperar este archivo.

## Casos de uso adicionales

### Varios artículos

No estás limitado a un solo elemento en un solo mensaje. Puedes utilizar el modal **Añadir personalización** para añadir hasta tres elementos del catálogo a la vez. Para añadir más elementos a tu mensaje, selecciona **Añadir personalización** en el creador de mensajes y selecciona los elementos adicionales del catálogo y la información que quieres mostrar.

Echa un vistazo a este ejemplo en el que añadimos el `id` de tres juegos, Tales, Teslagrad y Acaratus, para **Elementos del catálogo** y seleccionamos `title` para **Información a mostrar**.

\![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar aún más nuestro mensaje añadiendo algún texto alrededor de nuestro Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

El resultado es el siguiente:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
¡Comprueba [las selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para crear grupos de datos para una mensajería más personalizada!
{% endalert %}

### Utilizando las declaraciones de Liquid `if` 

Puedes utilizar elementos del catálogo para crear sentencias condicionales. Por ejemplo, puedes desencadenar que se muestre un determinado mensaje cuando se seleccione un elemento específico en tu campaña.

Para ello, utilizarás una declaración Liquid `if`, como en este ejemplo:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

En este ejemplo, se mostrarán mensajes diferentes si el atributo personalizado `venue_name` tiene más de 10 caracteres o menos de 10 caracteres. Si `venue_name` es `blank`, no se mostrará nada. 

Ten en cuenta que debes declarar la lista de catálogos y, si procede, la selección antes de utilizar las declaraciones `if`. En el ejemplo, `item-list` es la lista del catálogo, y `selections` es el nombre de la selección.

### Utilizar imágenes {#using-images}

También puedes hacer referencia a imágenes del catálogo para utilizarlas en tu mensajería. Para ello, utiliza la etiqueta `catalogs` y el objeto `item` en el campo Liquid para las imágenes.

Por ejemplo, para añadir el `image_link` de nuestro catálogo de Juegos a nuestro mensaje promocional para Cuentos, selecciona el `id` para el campo **Artículos del catálogo** y `image_link` para el campo **Información a mostrar**. Esto añade las siguientes etiquetas de Liquid a nuestro campo de imagen:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

\![Compositor de tarjetas de contenido con la etiqueta de Liquid del catálogo utilizada en el campo de imagen.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Esto es lo que parece cuando se representa el Liquid:

\![Ejemplo de tarjeta de contenido con etiquetas de Liquid en el catálogo.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Plantilla de elementos de catálogo

También puedes utilizar plantillas para extraer dinámicamente elementos del catálogo basándote en atributos personalizados. Por ejemplo, supongamos que un usuario tiene el atributo personalizado `wishlist`, que contiene una matriz de ID de juegos de tu catálogo.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Los objetos JSON de los catálogos sólo se ingieren a través de la API. No puedes subir un objeto JSON utilizando un archivo CSV.
{% endalert %}

Utilizando la plantilla Liquid, puedes extraer dinámicamente los ID de la lista de deseos y utilizarlos en tu mensaje. Para ello, [asigna una variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) a tu atributo personalizado y, a continuación, utiliza el modal **Añadir personalización** para extraer un elemento concreto de la matriz. Las variables a las que se hace referencia como ID del artículo del catálogo deben ir entre llaves para que se haga referencia a ellas correctamente, como `{{result}}`.

{% alert tip %}
Recuerda que las matrices empiezan en `0`, no en `1`.
{% endalert %}

Por ejemplo, para informar a un usuario de que Tales (un artículo de nuestro catálogo que ha deseado) está de oferta, podemos añadir lo siguiente a nuestro creador de mensajes:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Que se mostrará como sigue:
> Consigue Tales ahora, ¡por sólo 7,49!

Con la plantilla, puedes mostrar un elemento del catálogo diferente para cada usuario en función de sus atributos personalizados individuales, propiedades del evento o cualquier otro campo que se pueda planificar.

### Cargar un CSV

Puedes subir un CSV de nuevos elementos de catálogo para añadir o elementos de catálogo para actualizar. Para eliminar una lista de artículos, puedes subir un CSV con los ID de los artículos para eliminarlos.

### Utilizar Liquid

También puedes crear catálogos manualmente con la lógica de Liquid. Sin embargo, ten en cuenta que si escribes un ID que no existe, Braze seguirá devolviendo una matriz de objetos sin objetos. Te recomendamos que incluyas un tratamiento de errores, como comprobar el tamaño de la matriz y utilizar una sentencia `if` para tener en cuenta un caso de matriz vacía.

{% alert note %}
Liquid actualmente no se puede utilizar dentro de los catálogos. Si la personalización de Liquid aparece dentro de una celda de tu catálogo, el valor dinámico no se mostrará y sólo se mostrará el Liquid real.
{% endalert %}

#### Elementos del catálogo de plantillas, incluido Liquid

De forma similar al [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), debes utilizar la bandera `:rerender` en una etiqueta de Liquid para representar el contenido Liquid de un elemento del catálogo. Ten en cuenta que la bandera `:rerender` sólo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna llamada anidada a la etiqueta de Liquid.

Si un elemento del catálogo contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse en Liquid antes en el mensaje y antes de la plantilla para que Liquid se muestre correctamente. Si no se indica la bandera `:rerender`, se mostrará el contenido sin procesar de Liquid.

Por ejemplo, si un catálogo llamado "Mensajes" tiene un elemento con este Liquid:

\![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para representar el siguiente contenido Liquid:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Aparecerá lo siguiente:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Las etiquetas de Liquid no pueden utilizarse recursivamente dentro de los catálogos.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
