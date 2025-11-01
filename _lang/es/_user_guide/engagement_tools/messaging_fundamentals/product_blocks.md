---
nav_title: Bloques de productos
article_title: Bloques de producto arrastrar y soltar
page_order: 7.5
description: "Este artículo de referencia trata de los bloques de producto de arrastrar y soltar, que permiten a los usuarios añadir y configurar rápidamente escaparates dinámicos o estáticos de artículos del catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Arrastrar y soltar bloques de producto 

> El editor de arrastrar y soltar te permite añadir y configurar rápidamente bloques de producto a tus mensajes para mostrar los productos fácilmente, sin necesidad de crear código Liquid personalizado. 

{% alert important %}
La característica de arrastrar y soltar bloques de productos está en acceso temprano y actualmente sólo está disponible para correo electrónico. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisitos 

| Requisito | Descripción |
| --- | --- |
| Eventos recomendados en eCommerce | [Los eventos recomendados por eCommerce]({{site.baseurl}}/ecommerce_events/) proporcionan esquemas de datos estandarizados para eventos clave de comportamiento que ocurren antes y después de realizar un pedido. Estos eventos acabarán sustituyendo al evento de compra heredado de Braze y se convertirán en la norma para el seguimiento del comportamiento relacionado con el comercio. <br><br> Los eventos recomendados de eCommerce son necesarios para los bloques de productos dinámicos.<br><br> Los eventos recomendados por eCommerce están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. |
| Plantillas Canvas para comercio electrónico | Los eventos recomendados de eCommerce admiten plantillas preconstruidas, incluidas las plantillas de eCommerce Canvas diseñadas para casos de uso esenciales, como navegación abandonada, carritos abandonados y confirmaciones de pedidos. <br><br>Si piensas poner en práctica alguno de estos casos de uso esenciales del comercio electrónico utilizando [las plantillas del Canvas de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases/), debes utilizar o seguir la plantilla Canvas proporcionada. |
| Catálogo Braze | Tienes que crear un catálogo Braze que incluya los siguientes campos, que se utilizarán en la configuración de tu bloque de productos:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Selección del catálogo | Para los bloques de producto estáticos, debes crear una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar qué productos incluir en tu bloque de producto. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Tipos de bloques de producto arrastrar y soltar

| Bloque de productos | Propósito | Casos de uso | Disponibilidad |
| --- | --- | --- | --- |
| Dinámico | Personaliza tu mensajería con un escaparate de productos basado en las interacciones con los clientes utilizando [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events/) y catálogos dentro de nuestras [plantillas Canvas de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navegar abandonada</li><li>Carrito abandonado</li><li>Caja abandonada</li><li>Confirmaciones de pedido</li></ul>{:/} | Disponible sólo en Canvas. |
| Estática | Personaliza productos utilizando datos almacenados en un catálogo Braze. Debes utilizar una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar qué productos incluir. | Perfecto para mostrar el lanzamiento de nuevos productos u ofertas de categorías específicas.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Configuración del bloque de contenido del producto

Cada tipo de bloque tiene diferentes configuraciones de contenido. 

### Campos de producto

En la sección **Campos de producto**, selecciona tu tipo de bloque de producto y, a continuación, alterna los campos que quieras incluir para cada producto. Cada campo se extrae de fuentes diferentes en función del tipo de bloque de producto que selecciones.

#### Bloque de producto dinámico

| Campo del producto | Fuente |
| --- | --- | 
| Imagen variante | Catálogos | 
| Título del producto | Catálogos | 
| Botón para la URL del producto | Catálogos |
| Precio | eCommerce Propiedad de evento recomendada|
| Cantidad | eCommerce Propiedad de evento recomendada| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

\![Campos de producto para un bloque de producto dinámico, que se dividen en datos de catálogo y datos de evento]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloque estático de producto

| Campo del producto | Fuente |
| --- | --- | --- |
| Imagen variante | Catálogos |
| Título del producto | Catálogos |
| Botón para la URL del producto | Catálogos |
| Precio | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

\![Campos de producto para un bloque de producto estático, que están todos categorizados como datos de catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opciones de diseño

Utiliza las opciones de diseño para personalizar cómo se muestran tus productos dentro de tu bloque de productos.

| Opción | Descripción |
| --- | --- |
| Orientación al producto | Elige cómo se orientan los campos de imagen y producto dentro del bloque. |
| Alineación | Ajusta la alineación de los campos de texto y del botón dentro del bloque. |
| Máximo de productos por fila | Muestra hasta tres productos por fila, hasta 12 productos en total para bloques de productos estáticos y hasta 24 productos en total para bloques de productos dinámicos. |
| Espacio entre productos | Configura el espaciado entre productos. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

\![Opciones de diseño para la orientación de los productos, la alineación, el número máximo de productos por fila y el espaciado entre productos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configuración global del estilo de correo electrónico 

[La configuración global del estilo de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) te permite aplicar un estilo coherente a tus correos electrónicos dentro de Braze. Esto significa que puedes definir estilos específicos -como fuentes, colores y diseños de botones- que se aplicarán automáticamente a todos tus correos electrónicos.

#### Cómo funcionan las configuraciones globales de estilo de correo electrónico con los bloques de producto

Los estilos existentes para párrafos y botones se aplicarán automáticamente a los elementos de texto y botón dentro del bloque de producto. Esto significa que cualquier formato que hayas establecido para párrafos y botones se utilizará de forma coherente en tu bloque de producto, manteniendo un aspecto cohesivo en todo tu correo electrónico.

## Configuración de bloques de producto

### Configuración del catálogo 

{% alert important %}
Si utilizas la integración de Braze y Shopify para [sincronizar productos]({{site.baseurl}}/shopify_catalogs/), no necesitas dar ningún paso adicional para utilizar bloques de productos de arrastrar y soltar.<br><br> Si no tienes información sobre la variante del producto, tienes que duplicar su información de producto de nivel superior tanto en el campo del producto como en el de la variante del producto dentro de las cargas útiles y los catálogos de eventos. Esto significa que tienes que proporcionar los mismos detalles del producto para ambos identificadores a fin de mantener la coherencia para que el bloque de producto funcione correctamente.
{% endalert %}

Para utilizar bloques de producto de arrastrar y soltar, tienes que configurar un catálogo Braze que incluya valores de campo específicos. Estos campos se utilizarán en la configuración de tu bloque de producto. Asegúrate de que tu catálogo incluye los siguientes campos:

| Campo | Descripción |
| --- | --- |
|`product_title` | El título del producto.|
|`product_url` | La URL donde los clientes pueden ver o comprar el producto. |
|`variant_image_url` | La URL de la imagen variante. |

Empieza trabajando con este [Catálogo de productos de muestra]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), que incluye los campos obligatorios. 

\![Un archivo CSV de muestra con los campos obligatorios además de otros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## Crear bloques de producto

Esta guía te guiará a través de los pasos para crear, probar y garantizar la funcionalidad de un bloque de producto dinámico o estático utilizando nuestro editor de arrastrar y soltar de correo electrónico.

### Paso 1: Crear una campaña de correo electrónico o paso en Canvas

#### Bloque de producto dinámico

{% alert note %}
Los bloques dinámicos de producto requieren [eventos recomendados por eCommerce]({{site.baseurl}}/ecommerce_events/) y sólo pueden utilizarse dentro de [Canvases]({{site.baseurl}}/ecommerce_use_cases). Para los usuarios de Braze Shopify, estos eventos se incluyen automáticamente como parte de la integración. Para los usuarios que no son de Shopify, tienes que trabajar con tus desarrolladores para pasar estos eventos a Braze y asegurarte de que el identificador principal del producto dentro de los eventos se añade como ID del artículo del catálogo.
{% endalert %}

Crea un nuevo Canvas que utilice una de las plantillas Braze disponibles para tu caso de uso específico:
- Exploración abandonada
- Carrito abandonado
- Pago abandonado
- Confirmaciones de pedido

Para obtener instrucciones detalladas sobre la creación de tus Lienzos de Comercio Electrónico, consulta los [casos de uso de Comercio Electrónico]({{site.baseurl}}/ecommerce_use_cases/).

#### Bloque estático de producto

Crea una campaña de correo electrónico de arrastrar y soltar, un Canvas basado en acciones o una plantilla que tenga un paso de mensaje de correo electrónico de arrastrar y soltar.

### Paso 2: Añadir un bloque de producto

{% tabs %}
{% tab Dynamic product block %}

Dentro del paso de mensajes, crea un mensaje de correo electrónico o modifica la plantilla existente utilizando el creador de mensajes de arrastrar y soltar.
Arrastra un bloque de producto a tu mensaje de correo electrónico.
Confirma que se ha seleccionado el tipo de bloque dinámico.
Selecciona el catálogo de productos que quieres utilizar para la personalización. Asegúrate de que concuerda con los productos de los eventos entrantes a los que te diriges.

{% endtab %}
{% tab Static product block %}

Arrastra un bloque de producto a tu mensaje de correo electrónico y selecciona el tipo de bloque estático.
Selecciona el catálogo que quieres utilizar para tu bloque de productos. Debes elegir una selección de catálogo para especificar qué productos se muestran en tu bloque de productos.

{% endtab %}
{% endtabs %}

\![La pestaña "Contenido" que contiene bloques de editor, como los bloques de producto.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Paso 3: Configurar los campos del producto

Selecciona qué [campos de producto](#product-fields) deben mostrarse en el bloque de producto. Selecciona **Aplicar configuración** después de cada cambio para ver las actualizaciones en el editor. 

También puedes personalizar el texto que precede a tus etiquetas de Liquid. Por ejemplo, puedes anteponer un signo de dólar ($) al precio de un artículo o actualizar el término de cantidad a "cantidad" u otra etiqueta preferida.

Bloque de producto con un dólar añadido al precio del artículo.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Paso 4: Configurar los ajustes de diseño

Cambia las [opciones de diseño](#layout-options) para actualizar cómo se muestran los productos dentro de tu bloque de productos, y asegúrate de seleccionar **Aplicar configuración** después de cada cambio.

### Paso 5: Vista previa y prueba de tu mensaje

{% tabs %}
{% tab Dynamic product block %}

1. En la sección **Vista previa & Prueba**, previsualiza el mensaje como usuario personalizado.
2. Especifica cuántos elementos quieres mostrar en la vista previa.
3. Confirma que aparece el número correcto de elementos y que tus opciones de diseño se aplican correctamente. Ten en cuenta que los elementos que aparecen se seleccionan al azar.

\!["Vista previa como usuario" pestaña con una sección desplegable "Bloque de productos dinámicos" que especifica que se muestren 4 elementos.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

Se generará una vista previa dentro del compositor arrastrar y soltar cuando apliques cambios a tu bloque de producto. 

\![Compositor de arrastrar y soltar por correo electrónico que muestra un bloque de producto generado con diferentes mosaicos de artículos.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Cuando hayas terminado de crear tu mensaje y de confirmar que tiene el aspecto esperado, ¡estás listo para enviarlo!