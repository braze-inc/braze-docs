---
nav_title: Sincronización de colecciones de Shopify
article_title: Sincronización de colecciones de Shopify
permalink: "/shopify_collections_sync/"
description: "Este artículo de referencia explica cómo configurar la sincronización de colecciones de Shopify, que te permite agrupar tus productos en colecciones para que los clientes puedan encontrar tus productos por categorías."
hidden: true
---

# Sincronización de colecciones de Shopify beta

> La sincronización de colecciones de Shopify te permite agrupar tus productos en colecciones para que los clientes puedan encontrar tus productos por categorías. Para una experiencia de compra más fluida, puedes incorporar artículos de las colecciones de tu tienda en tu mensajería Braze.

{% alert important %}
La sincronización de colecciones de Shopify está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si quieres participar en la beta.
{% endalert %}

## Configuración de la sincronización de colecciones de Shopify

Para sincronizar los productos de tu tienda Shopify con Braze, selecciona la casilla **Sincronizar colecciones de Shopify** en el paso **Sincronizar productos** de la [integración de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Paso 4 de la sincronización de productos de Shopify con la casilla "Sincronizar colecciones de Shopify" seleccionada.][1]

Una vez sincronizados tus productos, puedes ver qué productos están asociados a tus colecciones consultando tu catálogo de Shopify. <br><br>![Fila de la tabla del catálogo que muestra un producto en las colecciones de "más vendidos" y "portada".][2]

Desde tu catálogo de Shopify, puedes ver tu colección de Shopify en la pestaña **Selecciones**. <br><br>![La pestaña Selecciones muestra una lista de dos colecciones: "best-sellers" y "portada".][3]

### Funcionalidad beta

- Braze admitirá hasta 30 colecciones
- El orden de clasificación de tu colección no se mantiene ni se admite en este momento. Por ahora, el orden de clasificación que se basa en lo siguiente:
    - Los objetos más recientes añadidos a tu colección.
    - El orden en que se actualizan los elementos durante las sincronizaciones continuas.
    - El orden que selecciones en la pestaña de selección de tu colección de Shopify.

## Utilizar las colecciones de Shopify

Utiliza tus colecciones de Shopify para personalizar un mensaje para cada usuario de tu campaña, de forma similar a como utilizarías una [selección de Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Ten en cuenta el siguiente comportamiento en la beta: <br><br>Si actualizas la descripción de la colección de Shopify o la configuración de filtrar, romperás la sincronización de tu colección de Shopify. Como resultado, tu colección de Shopify no funcionará como esperabas.
{% endalert %}

### Paso 1: Configura el orden de clasificación de tu colección de Shopify

1. Especifica el orden en el que se devuelven los resultados de tu colección de Shopify seleccionando el **Orden de clasificación** en la pestaña de selección de tu colección de Shopify. Incluye una opción para aleatorizar el orden de clasificación.
2. Introduce el número máximo de resultados (hasta 50) para el **número límite**.
3. Selecciona **Actualizar selección**.

![La página Editar selección, donde puedes seleccionar la configuración para filtrar, el tipo de ordenación y el límite de resultados.][4]

### Paso 2: Utiliza la colección en una campaña

1. Crea una campaña y, a continuación, selecciona **\+ Personalización** en el creador de mensajes.
2. Selecciona lo siguiente:<br>- **Elementos** del catálogo como **tipo de personalización**<br>\- El nombre del catálogo<br>\- El método de selección de elementos<br>\- El nombre de la selección (el nombre de tu colección de Shopify) <br>\- La información a mostrar en tu mensaje

{: start="3"}
3\. Copia y pega el fragmento de código de Liquid donde quieras que aparezca la información en tu mensaje.

![La sección "Añadir personalización" con campos para seleccionar tu catálogo, el método de selección de artículos y la información a mostrar.][5]{: style="max-width:30%;"}

#### Liquid en los resultados de la selección

Utilizar cualquier resultado de los catálogos, como atributos personalizados y eventos personalizados, puede hacer que aparezcan resultados diferentes para cada usuario de tu selección.

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
