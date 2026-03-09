---
nav_title: Bloques de producto
article_title: Bloques de productos arrastrar y soltar
page_order: 9
description: "Este artículo de referencia trata sobre los bloques de productos de arrastrar y soltar, que permiten a los usuarios añadir y configurar rápidamente escaparates dinámicos o estáticos de artículos del catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Bloques de productos arrastrar y soltar 

> El editor de arrastrar y soltar te permite añadir y configurar rápidamente bloques de productos en tus mensajes para mostrar los productos fácilmente, sin necesidad de crear código Liquid personalizado. 

{% alert important %}
La característica de arrastrar y soltar bloques de productos se encuentra en fase de acceso anticipado y, por el momento, solo está disponible para el correo electrónico. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos 

| Requisito | Descripción |
| --- | --- |
| Eventos recomendados para el comercio electrónico | [Los eventos recomendados para el comercio electrónico]({{site.baseurl}}/ecommerce_events/) proporcionan esquemas de datos estandarizados para eventos de comportamiento clave que se producen antes y después de realizar un pedido. Estos eventos acabarán sustituyendo al antiguo evento de compra de Braze y se convertirán en el estándar para el seguimiento del comportamiento relacionado con el comercio. <br><br> Los eventos recomendados de comercio electrónico son necesarios para los bloques de productos dinámicos.<br><br> Los eventos recomendados para el comercio electrónico se encuentran actualmente en fase de acceso anticipado. Si estás interesado en participar en este acceso anticipado, ponte en contacto con tu administrador del éxito del cliente de Braze. |
| Plantillas de Canvas para comercio electrónico | Los eventos recomendados para comercio electrónico admiten plantillas prediseñadas, incluidas las plantillas de Canvas de comercio electrónico diseñadas para casos de uso esenciales, como navegación abandonada, abandono del carrito de compras y confirmaciones de pedidos. <br><br>Si tienes previsto implementar cualquiera de estos casos de uso esenciales del comercio electrónico utilizando las [plantillas de eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/), debes utilizar o seguir la plantilla Canvas proporcionada. |
| Catálogo de Braze | Debes crear un catálogo Braze que incluya los siguientes campos, que utilizarás en la configuración del bloque de productos:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Selección del catálogo | Para los bloques de productos estáticos, debes crear una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar qué productos incluir en tu bloque de productos. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Tipos de bloques de productos de arrastrar y soltar

| Bloque de productos | Propósito | Ejemplos | Disponibilidad |
| --- | --- | --- | --- |
| Dinámico | Personaliza tu mensajería con una muestra de productos basada en las interacciones de los clientes utilizando [los eventos]({{site.baseurl}}/ecommerce_events/) y catálogos [recomendados para comercio electrónico]({{site.baseurl}}/ecommerce_events/) dentro de nuestras [plantillas de eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navegación abandonada</li><li>Carrito abandonado</li><li>Compra abandonada</li><li>Confirmaciones de pedido</li></ul>{:/} | Disponible solo en Canvas. |
| Estático | Personaliza los productos utilizando los datos almacenados en un catálogo de Braze. Debes utilizar una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar qué productos incluir. | Perfecto para presentar lanzamientos de nuevos productos u ofertas específicas de una categoría.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Configuración del contenido del bloque de productos

Cada tipo de bloque de contenido tiene diferentes configuraciones de contenido. 

### Campos de producto

En la sección **Campos del producto**, selecciona el tipo de bloque de producto y, a continuación, alterna los campos que deseas incluir para cada producto. Cada campo se extrae de diferentes fuentes en función del tipo de bloque de producto que selecciones.

#### Bloque de producto dinámico

| Campo del producto | Fuente |
| --- | --- | 
| Imagen variante | Catálogos | 
| Título del producto | Catálogos | 
| Botón para la URL del producto | Catálogos |
| Precio | Propiedad recomendada para eventos de comercio electrónico|
| Cantidad | Propiedad recomendada para eventos de comercio electrónico| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Campos de producto para un bloque de productos dinámico, que se dividen en datos de catálogo y datos de eventos.]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloque de productos estáticos

| Campo del producto | Fuente |
| --- | --- | --- |
| Imagen variante | Catálogos |
| Título del producto | Catálogos |
| Botón para la URL del producto | Catálogos |
| Precio | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![Campos de producto para un bloque de productos estático, todos ellos clasificados como datos de catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opciones de diseño

Utiliza las opciones de diseño para hacer que tus productos se muestren de manera personalizada dentro del bloque de productos.

| Opción | Descripción |
| --- | --- |
| Orientación de productos | Elige cómo se orientarán los campos de imagen y producto dentro del bloque. |
| Alineación | Ajusta la alineación de los campos de texto y el botón dentro del bloque. |
| Máximo de productos por fila | Muestra hasta tres productos por fila, hasta 12 productos en total para bloques de productos estáticos y hasta 24 productos en total para bloques de productos dinámicos. |
| Espacio entre productos | Establece el espacio entre los productos. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Opciones de diseño para la orientación de los productos, la alineación, el número máximo de productos por fila y el espaciado entre productos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configuración global del estilo del correo electrónico 

[La configuración global del estilo del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) te permite aplicar un estilo coherente a tus correos electrónicos dentro de Braze. Esto significa que puedes definir estilos específicos, como fuentes, colores y diseños de botones, que se aplicarán automáticamente a todos tus correos electrónicos.

#### Cómo funciona la configuración global de estilo del correo electrónico con los bloques de productos

Los estilos existentes para párrafos y botones se aplican automáticamente a los elementos de texto y botones dentro del bloque de productos. Esto significa que tu bloque de producto utiliza de forma coherente cualquier formato que hayas establecido para los párrafos y botones, manteniendo un aspecto uniforme en todo tu correo electrónico.

## Configuración de bloques de productos

### Configuración del catálogo 

{% alert important %}
Si utilizas la integración de Braze y Shopify para [sincronizar productos]({{site.baseurl}}/shopify_catalogs/), no es necesario que realices ningún paso adicional para utilizar los bloques de productos de arrastrar y soltar.<br><br> Si no dispones de información sobre las variantes de los productos, debes duplicar la información de los productos de nivel superior tanto en los campos de productos como en los de variantes de productos dentro de las cargas útiles y los catálogos de eventos. Esto significa que debes proporcionar los mismos detalles del producto para ambos identificadores a fin de mantener la coherencia y que el bloque del producto funcione correctamente.
{% endalert %}

Para utilizar bloques de productos de arrastrar y soltar, debes configurar un catálogo de Braze que incluya valores de campo específicos. Utilizas estos campos en la configuración del bloque de productos. Asegúrate de que tu catálogo incluya los siguientes campos:

| Campo | Descripción |
| --- | --- |
|`product_title` | El título del producto.|
|`product_url` | La URL donde los clientes pueden ver o comprar el producto. |
|`variant_image_url` | La URL de la imagen variante. |

Empieza con buen pie trabajando con este [catálogo de productos de muestra]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), que incluye los campos obligatorios. 

![Un archivo CSV de muestra con los campos obligatorios, además de otros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mapeado a campos del catálogo

En la pestaña **Configuración** de tu catálogo, puedes alternar los **Bloques de productos** para realizar el mapeo de campos e información específicos de tu catálogo. Esto te permite seleccionar qué campos utilizar como título del producto, URL del producto y URL de la imagen. Ten en cuenta que los campos del catálogo de Shopify están mapeados de forma predeterminada y no se pueden cambiar.

{% alert note %}
Si no utilizas Shopify, puedes ponerte en contacto con tu director de cuentas para activar el mapeado de campos, lo que te permitirá conectar cualquier catálogo a bloques de productos y asignar sus campos a `product_title`,`product_url` , y `variant_image_url`.
{% endalert %}

## Creación de bloques de productos

Esta guía te explicará los pasos para crear, probar y garantizar la funcionalidad de un bloque de productos dinámico o estático utilizando nuestro editor de arrastrar y soltar de correo electrónico.

### Paso 1: Crear una campaña de correo electrónico o un paso en Canvas

#### Bloque de producto dinámico

{% alert note %}
Los bloques de productos dinámicos requieren [eventos recomendados para comercio electrónico]({{site.baseurl}}/ecommerce_events/) y solo se pueden utilizar dentro de [lienzos]({{site.baseurl}}/ecommerce_use_cases). Para los usuarios de Braze Shopify, estos eventos se incluyen automáticamente como parte de la integración. Si no utilizas Shopify, deberás trabajar con tus desarrolladores para transferir estos eventos a Braze y asegurarte de que el identificador principal del producto dentro de los eventos se añada como ID del artículo del catálogo.
{% endalert %}

Crea un nuevo Canvas que utilice una de las plantillas disponibles de Braze para tu caso de uso específico:
- Navegación abandonada
- Carrito abandonado
- Finalización de compra abandonada
- Confirmaciones de pedidos

Para obtener instrucciones detalladas sobre cómo crear tus lienzos de comercio electrónico, consulta [los casos de uso]({{site.baseurl}}/ecommerce_use_cases/) de [comercio electrónico.]({{site.baseurl}}/ecommerce_use_cases/)

#### Bloque de productos estáticos

Crea una campaña de correo electrónico de arrastrar y soltar, un lienzo basado en acciones o una plantilla que tenga un paso de mensaje de correo electrónico de arrastrar y soltar.

### Paso 2: Añadir un bloque de productos

{% tabs %}
{% tab Dynamic product block %}

En el paso del mensaje, crea un correo electrónico o modifica la plantilla existente utilizando el editor de correo electrónico de arrastrar y soltar.
Arrastra un bloque de producto a tu mensaje de correo electrónico.
Confirma que el tipo de bloque dinámico está seleccionado.
Selecciona el catálogo de productos que deseas utilizar para la personalización. Asegúrate de que se ajuste a los productos de los eventos entrantes a los que te diriges.

{% endtab %}
{% tab Static product block %}

Arrastra un bloque de producto a tu mensaje de correo electrónico y selecciona el tipo de bloque estático.
Selecciona el catálogo que deseas utilizar para tu bloque de productos. Debes seleccionar una selección de catálogo para especificar qué productos se muestran en tu bloque de productos.

{% endtab %}
{% endtabs %}

![La pestaña «Contenido», que contiene bloques de editor, como bloques de productos.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Paso 3: Configurar campos de producto

Selecciona [los campos del producto](#product-fields) que deben mostrarse en el bloque de productos. Selecciona **Aplicar configuración** después de cada cambio para ver las actualizaciones en el editor. 

También puedes personalizar el texto que precede a tus etiquetas de Liquid. Por ejemplo, puedes anteponer el signo del dólar ($) al precio de un artículo o cambiar el término «cantidad» por «importe» u otra etiqueta que prefieras.

![Bloque de productos con el precio del producto precedido por el símbolo del dólar.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Paso 4: Configurar la configuración de diseño

Cambia las [opciones de diseño](#layout-options) para actualizar la forma en que se muestran los productos dentro de tu bloque de productos y asegúrate de seleccionar **Aplicar configuración** después de cada cambio.

### Paso 5: Vista previa y prueba de tu mensaje

{% tabs %}
{% tab Dynamic product block %}

1. En la sección **Vista previa&de la prueba**, previsualiza el mensaje como un usuario personalizado.
2. Especifica cuántos elementos deseas mostrar en la vista previa.
3. Confirma que aparece el número correcto de elementos y que tus opciones de diseño se aplican correctamente. Nota: Los elementos que aparecen se seleccionan al azar.

![Pestaña «Vista previa como usuario» con una sección desplegable «Bloque de productos dinámico» que especifica mostrar 4 artículos.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

Se generará una vista previa en el editor de arrastrar y soltar cuando apliques cambios al bloque de tu producto. 

![Editor de correo electrónico de arrastrar y soltar que muestra un bloque de productos generados con diferentes mosaicos de artículos.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Una vez que hayas terminado de crear tu mensaje y hayas confirmado que se ve como esperabas, ¡ya estás listo para enviarlo!