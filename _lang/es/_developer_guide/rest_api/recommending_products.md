---
nav_title: Recomendar productos a los usuarios
article_title: Recomendar productos a los usuarios
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo usar la API REST de Braze, los catálogos y el contenido conectado para recomendar productos a los usuarios a través de los canales de mensajería."
---

# Recomendar productos a los usuarios

> Usa la API REST de Braze junto con los [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) o el [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) para mostrar recomendaciones de productos personalizadas en tus mensajes. Este enfoque te permite conectar tu propia herramienta de recomendaciones al ecosistema de mensajería de Braze, para que los usuarios no técnicos puedan gestionar el contenido y la mensajería en torno a cada recomendación.

Con este enfoque, puedes:

- Almacenar recomendaciones de productos en los perfiles de usuario desde tu backend usando la API REST.
- Recuperar metadatos de productos en el momento del envío usando catálogos o contenido conectado.
- Mostrar recomendaciones personalizadas en cualquier canal de mensajería, incluyendo correo electrónico, push, mensajes dentro de la aplicación y más.

## Requisitos previos

Para completar esta guía, necesitas:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST de Braze | Una clave con el permiso `users.track` y, si gestionas catálogos a través de la API, los permisos de catálogos correspondientes. Para crear una, ve a **Configuración** > **Claves de API**. |
| Catálogo de Braze | Un catálogo que contenga los metadatos de tus productos (como nombre, categoría, precio y URL de imagen). Para crear uno, consulta [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/). |
| Conocimiento de Liquid | Familiaridad intermedia con [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para crear plantillas con variables personalizadas y usar contenido conectado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Almacenar recomendaciones en los perfiles de usuario

Para empezar, almacena las recomendaciones de productos generadas por tu herramienta de recomendaciones en los perfiles de usuario de Braze como atributos personalizados. Esto te permite hacer referencia a los productos recomendados de cada usuario en el momento del envío del mensaje.

1. Determina qué datos de recomendación almacenar, como IDs de productos o categorías preferidas.
2. Usa el punto de conexión [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para escribir la recomendación como un atributo personalizado en el perfil de usuario.

### Ejemplo de solicitud

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Reemplaza `YOUR_REST_ENDPOINT` con la [URL del punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints) de tu espacio de trabajo.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Usa nombres de atributos significativos (como `recommended_product_id`) para que sean fáciles de referenciar en las plantillas de Liquid más adelante. Mantén las recomendaciones precisas actualizándolas regularmente a medida que tu herramienta de recomendaciones produce nuevos resultados.

## Paso 2: Recuperar metadatos de productos

Después de almacenar un identificador de recomendación en cada perfil de usuario, necesitas recuperar los metadatos completos del producto (nombre, precio, imagen, etc.) para incluirlos en tu mensaje. Tienes dos opciones:

- **Opción A:** [Catálogos de Braze](#option-a-braze-catalogs) — almacena la información de productos directamente en Braze para consultas rápidas e integradas.
- **Opción B:** [Contenido conectado](#option-b-connected-content) — obtén la información de productos desde una API externa en el momento del envío.

### Opción A: Catálogos de Braze

Si has creado un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) con tu inventario de productos, puedes buscar artículos directamente en tu mensaje usando Liquid. Para una guía completa, consulta [Uso de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).

#### Recomendar un artículo específico del catálogo

{% raw %}
Para hacer referencia a un producto específico por ID, usa la etiqueta de Liquid `catalog_items`. Por ejemplo, para recomendar el producto `1001` de un catálogo llamado `retail_products`:

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Recomendar múltiples artículos del catálogo

{% raw %}
También puedes hacer referencia a múltiples artículos en una sola etiqueta. Por ejemplo, para destacar tres productos:

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Crear plantillas de artículos usando la recomendación de un usuario

{% raw %}
Combina el atributo personalizado del [Paso 1](#step-1-store-recommendations-on-user-profiles) con una consulta al catálogo para personalizar la recomendación para cada usuario:

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Opción B: Contenido conectado

Si los metadatos de tus productos se encuentran en un servicio externo en lugar de un catálogo de Braze, usa el [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para obtenerlos en el momento del envío.

{% raw %}
Por ejemplo, si tu API interna devuelve detalles del producto por ID:

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Para más detalles sobre cómo hacer llamadas a la API desde tus mensajes, consulta [Hacer una llamada a la API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

{% alert warning %}
Evita usar contenido conectado para obtener una lista grande de productos y luego iterar a través de esa lista en Liquid en el momento del envío. Las cargas útiles de respuesta grandes aumentan la latencia del envío y pueden causar tiempos de espera en los mensajes o fallos en la entrega a gran escala. En su lugar, almacena solo los IDs de productos específicos que un usuario necesita en su perfil (consulta el [Paso 1](#step-1-store-recommendations-on-user-profiles)), y obtén los metadatos de esos artículos individuales o usa [catálogos](#option-a-braze-catalogs), que están optimizados para consultas rápidas.
{% endalert %}

## Paso 3: Verificar tu integración

Después de completar la configuración, verifica tu integración:

1. Usa el punto de conexión [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para escribir una recomendación de prueba en tu propio perfil de usuario.
2. Envía un mensaje de prueba que haga referencia al producto recomendado usando catálogos o contenido conectado.
3. Confirma que los detalles del producto se muestran correctamente en el mensaje entregado.
4. En el dashboard de Braze, ve a la página de resultados de la campaña o Canvas y confirma que el envío se ha registrado.

## Consideraciones

- Mantén los datos de recomendación precisos actualizando los atributos personalizados regularmente a medida que tu herramienta de recomendaciones produce nuevos resultados.
- Usa las [características de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze para adaptar aún más los mensajes, como incorporar datos específicos del usuario junto con los detalles del producto.
- Considera usar la [entrega activada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) para desencadenar mensajes desde tu backend usando plantillas definidas en el dashboard de Braze.