---
nav_title: Constructor
article_title: Constructor
description: "Este artículo de referencia describe la asociación entre Braze y Constructor. Esta asociación te permite aprovechar el Descubrimiento de productos fuera del sitio de Constructor para generar y entregar dinámicamente recomendaciones personalizadas de productos en mensajes Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) es una plataforma de búsqueda y descubrimiento de productos que utiliza IA y aprendizaje automático para entregar experiencias personalizadas de búsqueda, recomendación y navegación para sitios web de comercio minorista y comercio electrónico.

Con la integración de Braze y Constructor, puedes utilizar el Descubrimiento de productos fuera del sitio de Constructor para generar y entregar dinámicamente recomendaciones de productos personalizadas en mensajes Braze.

## Ejemplos

- **Carrito abandonado y seguimiento posterior al pedido**: Genera recomendaciones de productos dinámicas basadas en el comportamiento del usuario y el contenido del carrito para enviar recordatorios personalizados de carritos abandonados o sugerencias posteriores al pedido.
- **Recomendaciones de productos similares para los artículos del carrito abandonado**: Sugiere productos similares a los artículos que se han quedado en el carrito de un usuario para mantener su interacción y ofrecerle alternativas.
- **Recordatorios de artículos vistos recientemente**: Notifica a los usuarios los artículos que han visto recientemente pero que aún no han comprado, animándoles a completar su compra.
- **Campañas de promoción**: Entrega mensajes promocionales personalizados con recomendaciones de productos seleccionadas y adaptadas a las preferencias del usuario para ventas de temporada u ofertas especiales.
- **Sugerencias de productos visualmente similares**: Recomienda artículos visualmente similares a los que un usuario ha visto recientemente, ayudándole a descubrir opciones relacionadas que podría preferir.

## Requisitos previos

| Requisito | Descripción |
|-------------|-------------|
| Cuenta del Constructor | Se necesita una cuenta Constructor con su servicio de Descubrimiento Externo habilitado para aprovechar esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Trabaja con tu equipo de incorporación de Constructor para completar el proceso de integración. Asegúrate de que los datos de comportamiento de tu sitio web u otros orígenes de datos relevantes están disponibles para habilitar las recomendaciones de productos personalizadas. Tu equipo de incorporación de Constructor también te ayudará a configurar los fragmentos de código HTML necesarios para su uso en mensajes Braze.

## URL de la API de descubrimiento externo del constructor

Puedes utilizar la URL de la API de descubrimiento externo de Constructor para mostrar imágenes de productos y dirigir a los usuarios a la página de detalles del producto correspondiente. A continuación encontrarás un desglose de la estructura del punto final y un ejemplo de cómo utilizarlo:

### Ejemplo

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### Parámetros

| Parámetros | Descripción |
|-------------|-------------|
| `position` | Se refiere a la clasificación del elemento concreto recomendado dentro de la lista sugerida (por ejemplo, `position = 2`). <br>![Clasificación de la posición del elemento.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Representa el identificador del usuario, crucial para personalizar los resultados de las recomendaciones. Configura el parámetro `ui` como `external_id` del cliente en Braze. Si se omite, el Constructor devolverá recomendaciones generales en lugar de específicas del usuario. |
| `pod_id` | Identificador del pod que contiene la estrategia y las reglas de búsqueda de recomendaciones (por ejemplo, un pod con una estrategia de bestsellers genera bestsellers personalizados). |
| `key` | La clave de índice del Constructor para este cliente. |
| `style_id` | Determina qué imágenes se muestran para la tarjeta de producto. Por ejemplo, diferentes `style_ids` muestran imágenes únicas de tarjetas de producto. |
| `campaign_id` | ID único para la campaña de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entradas opcionales

| Entrada de datos | Descripción |
|-------------|-------------|
| `item_id` | Representa el elemento semilla. Necesario para estrategias basadas en elementos, como paquetes alternativos, complementarios. Por ejemplo, el primer elemento de un correo electrónico es el elemento semilla, y los siguientes son alternativos. |
| `num_results` | Número de productos que se añadirán al correo electrónico. El valor predeterminado es 10, hasta 100. Por ejemplo, `num_results = 3` significa que se añaden tres recomendaciones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

