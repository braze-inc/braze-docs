---
nav_title: Uso de catálogos
article_title: Usar catálogos
page_order: 1.5
description: "En este artículo de referencia se explica cómo utilizar catálogos para hacer referencia a datos de no usuarios en tus campañas de Braze a través de Liquid."
---

# Uso de catálogos

> Después de crear un catálogo, puedes hacer referencia a datos de no usuarios en tus campañas de Braze a través de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Puedes utilizar catálogos en todos tus canales de mensajería, incluso en cualquier parte del editor de arrastrar y soltar donde se admita Liquid.

## Utilización de catálogos en un mensaje

### Paso 1: Añadir tipo de personalización {#step-one-personalization}

En el creador de mensajes que elijas, selecciona el icono <i class="fas fa-plus-circle"></i> más para abrir el modal **Añadir personalización** y selecciona **Elementos del catálogo** como **tipo de personalización**. A continuación, selecciona el nombre de tu catálogo. Utilizando nuestro ejemplo anterior, seleccionaremos el catálogo "Games".

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver inmediatamente la siguiente vista previa de Liquid:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Paso 2: Selecciona elementos del catálogo

A continuación, ¡es hora de añadir los elementos de tu catálogo! Utiliza el menú desplegable para seleccionar los elementos del catálogo y la información que deseas mostrar. Esta información corresponde a las columnas del archivo CSV cargado para generar el catálogo.

Por ejemplo, para consultar el título y el precio de nuestro juego Tales, podríamos seleccionar el `id` de Tales (1234) como elemento del catálogo y solicitar `title` y `price` para la información mostrada.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Esto se muestra de la siguiente manera:

> ¡Consigue Tales por solo 7,49!

## Exportación de catálogos

Hay dos formas de exportar catálogos desde el dashboard: 

- Coloca el cursor sobre la fila del catálogo en la sección **Catálogos**. A continuación, selecciona el botón **Exportar catálogo**.
- Selecciona tu catálogo. A continuación, selecciona el botón **Exportar catálogo** en la pestaña **Vista previa** del catálogo.

Recibirás un correo electrónico para descargar el archivo CSV después de iniciar la exportación. Tendrás hasta cuatro horas para recuperar este archivo.

## Casos de uso adicionales

### Varios elementos

No estás limitado a un solo elemento por mensaje. Utiliza el modal **Añadir personalización** para añadir hasta tres elementos del catálogo a la vez. Para añadir más, selecciona de nuevo **Añadir personalización** en el compositor y selecciona los elementos adicionales del catálogo y la información que deseas mostrar.

Echa un vistazo a este ejemplo en el que añadimos el `id` de tres juegos, Tales, Teslagrad y Acaratus, para **Elementos del catálogo** y seleccionamos `title` para **Información a mostrar**.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar aún más nuestro mensaje añadiendo algo de texto alrededor de nuestro Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

El resultado es el siguiente:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

En este ejemplo, la etiqueta `catalog_items` obtiene el elemento `1234` del catálogo `Games`, y luego la sentencia `if` comprueba el campo `on_sale` para mostrar diferentes mensajes.

#### Con selecciones de catálogo

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer. 
{% else %} 
{% abort_message('no venue_name') %} 
{% endif %}
```
{% endraw %}

En este ejemplo, se muestran diferentes mensajes en función de si el campo `venue_name` tiene más o menos de 10 caracteres. Si `venue_name` está en blanco, el mensaje se cancela.

{% alert tip %}
Para evitar errores de sintaxis de Liquid, selecciona el botón **+** más en el creador de mensajes para insertar automáticamente las etiquetas de Liquid del catálogo.
{% endalert %}

### Utilizar imágenes {#using-images}

También puedes hacer referencia a imágenes del catálogo para utilizarlas en tus mensajes. Para ello, utiliza la etiqueta `catalogs` y el objeto `item` en el campo de Liquid para imágenes.

Por ejemplo, para añadir el `image_link` de nuestro catálogo de Games a nuestro mensaje promocional para Tales, selecciona el `id` para el campo **Elementos del catálogo** y `image_link` para el campo **Información a mostrar**. Esto añade las siguientes etiquetas de Liquid a nuestro campo de imagen:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Compositor de tarjetas de contenido con la etiqueta de Liquid del catálogo utilizada en el campo de imagen.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Esto es lo que se ve cuando se renderiza el Liquid:

![Ejemplo de tarjeta de contenido con etiquetas de Liquid del catálogo renderizadas.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Plantillas de elementos de catálogo

También puedes utilizar plantillas para extraer dinámicamente elementos del catálogo en función de atributos personalizados. Por ejemplo, supongamos que un usuario tiene el atributo personalizado `wishlist`, que contiene una matriz de ID de juegos de tu catálogo.

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
Los objetos JSON de los catálogos solo se ingieren a través de la API. No puedes cargar un objeto JSON utilizando un archivo CSV.
{% endalert %}

Utilizando plantillas de Liquid, puedes extraer dinámicamente los ID de la lista de deseos y utilizarlos en tu mensaje. Para ello, [asigna una variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) a tu atributo personalizado y, a continuación, utiliza el modal **Añadir personalización** para extraer un elemento específico de la matriz. Las variables a las que se hace referencia como ID de elemento del catálogo deben escribirse entre llaves para que se puedan referenciar correctamente, como por ejemplo `{{result}}`.

{% alert tip %}
Recuerda que las matrices empiezan en `0`, no en `1`.
{% endalert %}

Por ejemplo, para avisar a un usuario de que Tales (un elemento de nuestro catálogo que ha deseado) está en oferta, podemos añadir lo siguiente a nuestro creador de mensajes:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Que se mostrará de la siguiente manera:
> ¡Consigue Tales ahora por solo 7,49!

Con las plantillas, puedes renderizar un elemento de catálogo diferente para cada usuario en función de sus atributos personalizados, propiedades del evento o cualquier otro campo que admita plantillas.

### Cargar un CSV

Puedes cargar un CSV de nuevos elementos de catálogo para añadir o elementos de catálogo para actualizar. Para eliminar una lista de elementos, puedes cargar un CSV con los ID de los elementos para eliminarlos.

### Utilizar Liquid

También puedes crear catálogos manualmente con lógica de Liquid. Sin embargo, ten en cuenta que si escribes un ID que no existe, Braze seguirá devolviendo una matriz de elementos sin objetos. Te recomendamos que incluyas gestión de errores, como la comprobación del tamaño de la matriz y el uso de una sentencia `if` para tener en cuenta un caso de matriz vacía.

#### Elementos del catálogo con plantillas que incluyen Liquid

De forma similar al [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), debes utilizar la marca `:rerender` en una etiqueta de Liquid para renderizar el contenido Liquid de un elemento del catálogo. Ten en cuenta que la marca `:rerender` solo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna llamada anidada de etiquetas de Liquid.

Si un elemento del catálogo contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse en Liquid antes en el mensaje y antes de la plantilla para que el Liquid se renderice correctamente. Si no se proporciona la marca `:rerender`, se mostrará el contenido sin procesar de Liquid.

Por ejemplo, si un catálogo llamado "Messages" tiene un elemento con este Liquid:

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para renderizar el siguiente contenido Liquid:

{% raw %}
```liquid
Hi ${first_name},

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
Las etiquetas de Liquid de catálogos no pueden utilizarse recursivamente dentro de los catálogos.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}