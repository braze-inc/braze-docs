---
nav_title: Uso de recomendaciones
article_title: Utiliza recomendaciones de artículos en tu mensajería
description: "Este artículo describe cómo utilizar las recomendaciones de artículos en tus mensajes."
page_order: 1.2
---

# Utiliza recomendaciones de artículos en tu mensajería.

> Una vez que se haya entrenado tu recomendación, puedes utilizar Liquid para recuperar y mostrar los artículos recomendados en tus mensajes trabajando directamente con el objeto`product_recommendation` Liquid.

{% alert tip %}
Para obtener una guía paso a paso, consulta nuestro curso de Braze Learning: [Creación de experiencias de personalización con IA](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Requisitos previos

Antes de poder utilizar recomendaciones en tu mensajería, deberás [crear y entrenar una herramienta de recomendaciones]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). La formación puede durar entre 10 minutos y 36 horas. Recibirás un correo electrónico cuando haya finalizado o si se ha producido un error.

## Uso de recomendaciones en tu mensajería

### Paso 1: Añadir código Liquid

Una vez que tu recomendación haya terminado la formación, podrás personalizar tus mensajes con Liquid para insertar los productos más populares de ese catálogo.

{% tabs local %}
{% tab pre-formatted code %}
![Modalidad "Añadir personalización" con la recomendación de artículos como tipo de personalización.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Puedes generar Liquid desde la sección **Añadir personalización** del creador de mensajes:

1. En cualquier creador de mensajes que admita la personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Tipo de personalización**, selecciona **Recomendación de artículos**.
3. En **Nombre de la** recomendación, selecciona la recomendación que acabas de crear.
4. En **Número de artículos predichos**, introduce cuántos productos principales quieres que se inserten. Por ejemplo, puedes mostrar los tres artículos más comprados.
5. En **Información a mostrar**, selecciona qué campos del catálogo deben incluirse para cada artículo. Los valores de estos campos para cada artículo se extraerán del catálogo asociado a esta recomendación.
6. Selecciona el icono **Copiar** y pega el Liquid donde sea necesario en tu mensaje.
{% endtab %}

{% tab custom code %}
Puedes escribir código Liquid personalizado haciendo referencia al objeto `product_recommendation`de un catálogo. Contiene todos los datos de recomendaciones de productos generados de manera dinámica para ese catálogo, estructurados como una matriz de objetos, donde cada objeto representa un artículo recomendado.

|Especificaciones|Detalles|
|-------------|-------|
|**Estructura**|Se accede a cada elemento como `items[index]`, donde el índice comienza en 0 (para el primer elemento) y se incrementa para los elementos siguientes.|
|**Campos del catálogo**|Cada elemento de la matriz contiene pares clave-valor correspondientes a campos (columnas) del catálogo. Por ejemplo, los campos habituales del catálogo para recomendaciones de productos incluyen:<br>-`name`o `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Utiliza la`assign`etiqueta  para obtener los`product_recommendation`datos  y asignarlos a una variable.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Sustituye lo siguiente:

|Marcador de posición|Descripción|
|-----------|-----------|
|`recommendation_name`|El nombre de la recomendación de IA que creaste en Braze.|
|`items`|La variable que almacena la matriz de artículos recomendados.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

A continuación, haced referencia a elementos específicos y sus campos utilizando el índice de la matriz y la notación de puntos:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Para incluir varios elementos, haz referencia a cada uno de ellos individualmente por su índice.`.name`  y`.price`  extrae el campo correspondiente del catálogo. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

Las recomendaciones de IA devuelven varios productos como una matriz, donde`items[0]`  es el primer elemento,`items[1]`  es el segundo, y así sucesivamente. Si una recomendación solo devuelve un elemento, intentar hacer referencia a`items[1]`  dará como resultado un campo vacío.
{% endtab %}
{% endtabs %}

### Paso 2: Referencia una imagen (opcional)

Si el catálogo que recomiendas incluye enlaces a imágenes, puedes hacer referencia a ellos en tu mensaje. 

{% tabs %}
{% tab Drag-and-drop%}
En el editor de arrastrar y soltar del correo electrónico, añade un bloque de imagen a tu correo electrónico y, a continuación, selecciona el bloque de imagen para abrir **las propiedades de la imagen**.

![Panel de propiedades de imagen en el editor de arrastrar y soltar]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Alternar **la opción Imagen con Liquid** y, a continuación, añade lo siguiente al campo **URL dinámico**:

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

Para incluir una imagen de marcador de posición en tus correos electrónicos de vista previa y prueba, selecciona **Elegir imagen** y, a continuación, elige una imagen de tu biblioteca multimedia o introduce la URL de una imagen de tu sitio de alojamiento.
{% endtab %}

{% tab HTML %}
Para las referencias de imágenes HTML, configura el atributo `src`de imagen en el campo URL de la imagen del catálogo. Puede que quieras utilizar otro campo, como el nombre o la descripción de un producto, como texto alternativo.

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
