---
nav_title: Utilizar las recomendaciones de artículos
article_title: Utilizar recomendaciones de artículos en tus mensajes
description: "Este artículo describe cómo utilizar las recomendaciones de elementos en tu mensaje."
page_order: 20
---

# Utilizar recomendaciones de artículos en tu mensajería

> Una vez formada tu recomendación, puedes utilizar Liquid para buscar y mostrar los elementos recomendados en tus mensajes. La clave aquí es trabajar directamente con el objeto `product_recommendation` Liquid. Este artículo trata del objeto `product_recommendation` Liquid e incluye un tutorial para ayudarte a poner en práctica esos conocimientos.

{% alert tip %}
Este artículo describe detalladamente la sintaxis del objeto Liquid. Sin embargo, puedes [insertar variables preformateadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) con valores predeterminados a través del modal **Añadir personalización** situado en la parte superior derecha de cualquier campo de texto de la plantilla.
{% endalert %}

Para obtener más orientación sobre el uso de recomendaciones de elementos de IA en Braze, consulta nuestro [curso de Braze Learning sobre Creación de experiencias personalizadas con IA][1]. Este curso cubre casos de uso del sector, instrucciones paso a paso y un caso de uso adicional para crear un mensaje dentro de la aplicación con recomendaciones basadas en IA.

## Anatomía del objeto de recomendación

El objeto `product_recommendation` representa el conjunto de elementos recomendados por el modelo. Proporciona datos directamente del catálogo asociado, estructurados como una matriz de objetos, donde cada objeto representa un elemento recomendado.

- **Estructura:** Se accede a cada elemento como `items[index]`, donde el índice empieza en 0 (para el primer elemento) y aumenta para los elementos siguientes.
- **Campos del catálogo:** Cada elemento de la matriz contiene pares clave-valor correspondientes a campos (columnas) del catálogo. Por ejemplo, los campos habituales del catálogo para recomendaciones de productos incluyen:
   - `name` o `title`
   - `price`
   - `image_url`

## Etiquetas de Liquid

El objeto `product_recommendation` contiene recomendaciones de productos generadas dinámicamente. Para acceder a ellos en Liquid, primero debes asignar los datos a una variable antes de utilizarlos en tu mensaje.

### Asignar datos de recomendación

Empieza siempre con la etiqueta asignar para obtener los datos de `product_recommendation` y almacenarlos en una variable.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`: Sustitúyelo por el nombre de la recomendación de IA que creaste en Braze.
- `items`: La variable que almacena la matriz de elementos recomendados.

### Acceder a elementos individuales

Una vez asignados los datos de recomendación, puedes hacer referencia a elementos concretos y a sus campos utilizando la indexación de matrices y la notación de puntos:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

Para incluir varios elementos, haz referencia a cada uno de ellos individualmente por su índice. `.name` y `.price` extraen el campo correspondiente del catálogo. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

Las recomendaciones de IA devuelven varios productos como una matriz, donde `items[0]` es el primer elemento, `items[1]` es el segundo, y así sucesivamente. Si una recomendación sólo devuelve un elemento, al intentar hacer referencia a `items[1]` aparecerá un campo vacío.

## Añadir imágenes

Si el catálogo que utiliza tu recomendación incluye enlaces de imágenes, puedes hacer referencia a esas imágenes en tu mensaje. 

{% tabs %}

{% tab Arrastrar y soltar%}
En compositores con campos de imagen, añade el siguiente Liquid al campo correspondiente en el compositor:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

Para el editor de arrastrar y soltar del correo electrónico:

1. Añade un bloque de imagen a tu correo electrónico.
2. Selecciona el bloque de la imagen (no el botón **Examinar** ) para abrir el panel de **propiedades de la imagen**.
3. Enciende **Imagen con Liquid**. 
4. Pega el fragmento de código Liquid en el campo **URL dinámico**.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![Panel de propiedades de la imagen en el editor de arrastrar y soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. Para incluir una imagen de marcador de posición en tus correos de vista previa y de prueba, pulsa **Elegir imagen** para añadir una imagen de marcador de posición de la biblioteca multimedia, o introduce una URL donde esté alojada tu imagen.

{% endtab %}

{% tab HTML %}

Para las referencias de imágenes HTML, establece el atributo de imagen `src` en el campo URL de la imagen en el catálogo. Puede que quieras utilizar otro campo, como el nombre o la descripción de un producto, como texto alternativo.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  Sustituye `MY_RECOMMENDATION_NAME` por el nombre de tu recomendación
- Sustituye `IMAGE_URL_FIELD` por el nombre del campo de tu catálogo que contiene las URL de las imágenes.


## Tutorial: Crear correo electrónico de carrito abandonado

En este tutorial, aprenderás a crear un correo electrónico dinámico que recomiende productos a los usuarios en función de sus preferencias o comportamiento utilizando las recomendaciones de artículos de la IA de Braze. 

Supongamos que eres especialista en marketing de "Flash & Thread", un comercio minorista de ropa online. Quieres reactivar la interacción con los clientes que han dejado artículos en sus carritos y vender productos adicionales. Tu objetivo es crear un correo electrónico que muestre los objetos abandonados y recomendaciones personalizadas.

### Paso 1: Prepara tu catálogo

Tu recomendación sacará artículos de un catálogo. Sigue los pasos para Crear un catálogo. Asegúrate de que tu catálogo incluye estos campos:

| Campo | Tipo de datos | Descripción |
| --- | --- | --- |
| ID | Cadena | Un identificador único para cada artículo de tu catálogo |
| nombre | Cadena | El nombre del producto, como "Suéter de punto a rayas". |
| precio | Número | El precio del producto, como "49,99". |
| URL_imagen | Cadena | Una URL que apunta a la imagen del producto. Debe ser seguro HTTPS. Si tus imágenes están alojadas en la biblioteca multimedia, pasa el ratón por encima de un activo para copiar su URL. |
| categoría | Cadena | La categoría del producto, como "Suéteres" o "Accesorios". |
| color | Cadena | Un color descriptivo del producto, como "Azul marino/gris". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### Ejemplo de catálogo

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>ID</th>
    <th>nombre</th>
    <th>precio</th>
    <th>URL_imagen</th>
    <th>categoría</th>
    <th>color</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>Jersey de punto a rayas</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>Jerseys</td>
    <td>Azul marino/gris</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>Zapatos Yacht Club personalizados</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>Calzado</td>
    <td>Marina</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>Zapatos de Vuelta al Trabajo</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>Calzado</td>
    <td>Rosa/Dorado</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>Sombrero de fin de verano</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>Accesorios</td>
    <td>Floral blanco</td>
  </tr>
</table>


### Paso 2: Configura tu recomendación

1. En tu catálogo, selecciona **Crear recomendación**.
2. Sigue los pasos para [Crear una recomendación de elemento AI][3]. 
3. Para el tipo de recomendación, selecciona **AI Personalizada**.
4. Utiliza el catálogo que acabas de crear para entrenar la recomendación. Esto puede llevar algún tiempo; recibirás un correo electrónico cuando la formación esté completa.

### Paso 3: Crear un correo electrónico

Cuando la recomendación haya terminado de formarse, podrás utilizarla en tu mensajería.

1. Crea un correo electrónico con el editor de arrastrar y soltar.
2. En el cuerpo del mensaje, añade un bloque de imagen donde quieras extraer una recomendación del catálogo. 
3. Selecciona el bloque de imagen y activa **Imagen con Liquid** en el panel de **propiedades de la imagen**. 
4. Pega este fragmento de código Liquid en el campo URL dinámico.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. Debajo de la imagen, añade un bloque de párrafo. Aquí es donde añadirás el nombre del producto y cualquier detalle complementario. 
6. Pega el siguiente fragmento de código Liquid en el bloque. Esto extrae el nombre, la categoría, el color y el precio de la primera recomendación del catálogo, y los añade como líneas separadas. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. Para ambos fragmentos de código, sustituye `abandoned_cart` por el nombre de tu recomendación en Braze.
8. Comprueba que los nombres de los campos de los artículos (`{{ items[0].field_name }}`) coinciden con los nombres de las columnas de tu catálogo.
9. Incrementa la matriz en uno cada vez que repitas el bloque para extraer el siguiente elemento recomendado del catálogo. Por ejemplo, la matriz comienza con `{{ items[0].name }}`, por lo que el siguiente elemento sería `{{ items[1].name }}`.

### Paso 4: Vista previa de tu mensaje

Para ver cómo se ve tu mensaje para un usuario real:

1. Ve a la pestaña **Vista previa y Prueba** de tu editor.
2. Selecciona **Usuario aleatorio** en el desplegable.
3. Selecciona **Obtener usuario aleatorio** para obtener un usuario de tu audiencia y obtener una vista previa de cómo aparecerá el correo electrónico con sus datos.

La vista previa mostrará Liquid por completo, incluidas las recomendaciones de IA, siempre que el usuario seleccionado tenga los atributos necesarios o los datos del evento vinculados a la recomendación.

Si la recomendación no aparece en la vista previa, comprueba lo siguiente:

- El usuario ha interactuado con productos o eventos relevantes que entrenaron el modelo de recomendación
- La propia recomendación ha sido entrenada con éxito
- El código Liquid hace referencia correctamente a la recomendación y los campos correctos



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation