---
nav_title: Utilizar las recomendaciones
article_title: Utilizar recomendaciones de artículos en tu mensajería
description: "Este artículo describe cómo utilizar las recomendaciones de elementos en tu mensaje."
page_order: 1.2
---

# Utilizar recomendaciones de artículos en tu mensajería

> Una vez entrenada tu recomendación, puedes utilizar Liquid para obtener y mostrar los elementos recomendados en tus mensajes trabajando directamente con el objeto `product_recommendation` Liquid.

{% alert tip %}
Para un recorrido paso a paso, consulta nuestro curso de Braze Learning: [Crear experiencias personalizadas con IA](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Requisitos previos

Antes de poder utilizar recomendaciones en tus mensajes, tendrás que [crear y entrenar una herramienta de recomendaciones]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). La formación puede durar entre 10 minutos y 36 horas; recibirás un correo electrónico cuando haya terminado o si se ha producido un error.

## Utilizar recomendaciones en tu mensajería

### Paso 1: Añadir código Liquid

Una vez finalizada la formación de tu recomendación, puedes personalizar tus mensajes con Liquid para insertar los productos más populares de ese catálogo.

{% tabs local %}
{% tab pre-formatted code %}
\!["Añadir personalización" modal con la recomendación de artículos como tipo de personalización.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Puedes generar Liquid desde la sección **Añadir personalización** de tu creador de mensajes:

1. En cualquier creador de mensajes que admita la personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Tipo de personalización**, selecciona **Recomendación de artículos**.
3. En **Nombre de la** recomendación, selecciona la recomendación que acabas de crear.
4. En **Número de artículos predichos**, introduce cuántos productos principales quieres que se inserten. Por ejemplo, puedes mostrar los tres artículos más comprados.
5. En **Información a mostrar**, selecciona qué campos del catálogo deben incluirse para cada artículo. Los valores de estos campos para cada artículo se extraerán del catálogo asociado a esta recomendación.
6. Selecciona el icono **Copiar** y pega el Liquid donde sea necesario en tu mensaje.
{% endtab %}

{% tab custom code %}
Puedes escribir código Liquid personalizado haciendo referencia al objeto `product_recommendation` de un catálogo. Contiene todos los datos de recomendación de productos generados dinámicamente para ese catálogo, estructurados como una matriz de objetos, donde cada objeto representa un artículo recomendado.

|Especificación|Detalles|
|-------------|-------|
|**Estructura**|Se accede a cada elemento como `items[index]`, donde el índice empieza en 0 (para el primer elemento) y aumenta para los elementos siguientes.|
|**Campos del catálogo**|Cada elemento de la matriz contiene pares clave-valor correspondientes a campos (columnas) del catálogo. Por ejemplo, los campos habituales del catálogo para recomendaciones de productos incluyen:<br>- `name` o `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Utiliza la etiqueta `assign` para obtener los datos de `product_recommendation` y asignarlos a una variable.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Sustituye lo siguiente:

|Marcador de posición|Descripción|
|-----------|-----------|
|`recommendation_name`|El nombre de la recomendación de IA que creaste en Braze.|
|`items`|La variable que almacena la matriz de elementos recomendados.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

A continuación, haz referencia a elementos concretos y a sus campos utilizando la indexación de matrices y la notación con puntos:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Para incluir varios artículos, haz referencia a cada artículo individualmente por su índice. `.name` y `.price` extraen el campo correspondiente del catálogo. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

Las recomendaciones de IA devuelven varios productos como una matriz, donde `items[0]` es el primer elemento, `items[1]` es el segundo, y así sucesivamente. Si una recomendación sólo devuelve un elemento, al intentar hacer referencia a `items[1]` aparecerá un campo vacío.
{% endtab %}
{% endtabs %}

### Paso 2: Haz referencia a una imagen (opcional)

Si el catálogo que recomiendas incluye enlaces de imágenes, puedes hacer referencia a ellos en tu mensaje. 

{% tabs %}
{% tab Drag-and-drop%}
En el editor de arrastrar y soltar del correo electrónico, añade un bloque de imagen a tu correo electrónico y, a continuación, selecciona el bloque de imagen para abrir **Propiedades de imagen**.

\![Panel de propiedades de la imagen en el editor de arrastrar y soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Alterna **Imagen con Liquid** y, a continuación, añade lo siguiente al campo **URL dinámico**:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

Sustituye lo siguiente:

|Marcador de posición|Descripción|
|-----------|-----------|
|`recommendation_name`|El nombre de tu recomendación.|
|`image_url_field`|El nombre del campo de tu catálogo que contiene las URL de las imágenes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para incluir una imagen de marcador de posición en tus correos de vista previa y de prueba, selecciona **Elegir imagen** y, a continuación, elige una imagen de tu biblioteca multimedia o introduce la URL de una imagen de tu sitio de alojamiento.
{% endtab %}

{% tab HTML %}
Para las referencias de imágenes HTML, establece el atributo de imagen `src` en el campo URL de la imagen en el catálogo. Puede que quieras utilizar otro campo, como el nombre o la descripción de un producto, como texto alternativo.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Sustituye lo siguiente:

|Marcador de posición|Descripción|
|-----------|-----------|
|`recommendation_name`|El nombre de tu recomendación.|
|`image_url_field`|El nombre del campo de tu catálogo que contiene las URL de las imágenes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
