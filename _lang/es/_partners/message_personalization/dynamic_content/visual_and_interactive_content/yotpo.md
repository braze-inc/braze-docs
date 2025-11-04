---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Este artículo de referencia describe la asociación entre Braze y Yotpo, una plataforma líder de marketing de comercio electrónico que ayuda a miles de marcas con visión de futuro a acelerar el crecimiento directo al consumidor."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), la plataforma líder en marketing de comercio electrónico, ayuda a miles de marcas con visión de futuro a acelerar el crecimiento directo al consumidor. El enfoque de plataforma única de Yotpo integra soluciones basadas en datos para reseñas, fidelización, marketing por SMS y mucho más, capacitando a las marcas para crear experiencias de cliente más inteligentes y de mayor conversión.

_Esta integración está mantenida por Yotpo._

## Sobre la integración

Con la integración de Braze y Yotpo, puedes extraer y mostrar dinámicamente las puntuaciones con estrellas, las mejores opiniones y el contenido visual generado por el usuario (CGU) sobre productos en correos electrónicos y otros canales de comunicación dentro de Braze. También puedes incluir datos de fidelización a nivel de cliente en correos electrónicos y otros métodos de comunicación para crear una interacción más personalizada, impulsando las ventas y la fidelización.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Yotpo | Se necesita una cuenta de Yotpo para beneficiarse de esta asociación. |
| Yotpo revisa la clave de API | Esta API se implementará dentro del fragmento de código Contenido conectado.<br><br>Para más información, consulta [cómo encontrar la clave de tu aplicación de Yotpo y la clave secreta](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Clave de API de fidelización de Yotpo | Esta clave de API y GUID se implementarán dentro del fragmento de código de Contenido conectado.<br><br>Para más información, consulta [cómo encontrar tu clave de API y GUID de fidelización y referidos](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Antes de continuar, confirma que el ID de producto de Yotpo es el mismo que el de `product_id` que se extraerá dinámicamente de Braze. Esto es obligatorio para que la integración funcione. 

Para encontrar tu ID de producto de Yotpo, sigue estos pasos:

1. Ve al sitio web de tu tienda.
2. Abre la página del producto.
3. Haz clic con el botón derecho y selecciona **Inspeccionar**.
4. Pulsa <kbd>Control</kbd> + <kbd>F</kbd> y busca `yotpo-main` en el código. La variable `data-product ID` y su valor aparecen en el div de Yotpo.

![Inspecciona y busca yotpo-main para encontrar la variable ID del producto]({% image_buster /assets/img/yotpo/image1.png %})

## Integración

Para integrar Yotpo y Braze, realiza los siguientes pasos:

1. Ve a tu panel de Braze.
2. En la página **Campañas**, haz clic en **Crear campaña** y selecciona **Correo electrónico**.
3. Selecciona la plantilla que prefieras.
4. Haz clic en **Editar cuerpo del correo electrónico** y añade el fragmento de código de [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) correspondiente a tu caso de uso:
    - [Mostrar la tasa de estrellas y el recuento de opiniones de un producto](#star-review-count)
    - [Mostrar una opinión reciente de 5 estrellas sobre un producto](#five-star-review)
    - [Mostrar CGU visual por producto](#visual-ugc)
    - [Mostrar el saldo de fidelización de un cliente en un correo electrónico](#loyalty-balance)

### Mostrar la tasa de estrellas y el recuento de opiniones de un producto {#star-review-count}

Utiliza este fragmento de código para proporcionar la puntuación media pública y el número de opiniones totales de un producto incluido en el correo electrónico:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

Sustituye `<YOTPO-API-KEY>` por tu clave de API de reseñas de Yotpo. La dirección `product_id` se extraerá dinámicamente de Braze. Para que la integración funcione, el `product_id` en Braze debe coincidir con el ID del producto en Yotpo (normalmente el ID del producto padre de eCommerce).

![Sustituye YOTPO-API-KEY por tu clave de API de Yotpo Reviews]({% image_buster /assets/img/yotpo/image2.png %})

### Mostrar una opinión reciente de 5 estrellas sobre un producto {#five-star-review}

Utiliza este fragmento de código para proporcionar una opinión destacada (publicada) de un producto específico que se incluye en el correo electrónico:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Sustituye `<YOTPO-API-KEY>` por tu clave de API de reseñas de Yotpo. La dirección `product_id` se extraerá dinámicamente de Braze. Para que la integración funcione, el `product_id` en Braze debe coincidir con el ID del producto en Yotpo (normalmente el ID del producto padre de eCommerce).

Este es el aspecto que tendrá el fragmento de código en tu editor de correo electrónico:

![Ejemplo de editor de correo electrónico que muestra un fragmento de código para opiniones recientes de 5 estrellas]({% image_buster /assets/img/yotpo/image3.png %})

### Mostrar CGU visual por producto {#visual-ugc}

Utiliza este fragmento de código para recuperar imágenes de Yotpo etiquetadas y publicadas y añadirlas a tus correos electrónicos en lugar de la imagen de archivo o como una galería adicional:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Sustituye `<YOTPO-API-KEY>` por tu clave de API de reseñas de Yotpo. La dirección `product_id` se extraerá dinámicamente de Braze. Para que la integración funcione, el `product_id` en Braze debe coincidir con el ID del producto en Yotpo (normalmente el ID del producto padre de eCommerce).

El fragmento de código tendrá el siguiente aspecto:

![Ejemplo de editor de correo electrónico que muestra un fragmento de código de imágenes publicadas en Yotpo]({% image_buster /assets/img/yotpo/image4.png %})

### Mostrar el saldo de fidelización de un cliente en un correo electrónico {#loyalty-balance}

Utiliza este fragmento de código para recuperar el saldo de puntos de fidelización de un cliente y utilizarlo en tu mensajería por correo electrónico:

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Sustituye `<YOTPO-LOYALTY-GUID>` y `<YOTPO-LOYALTY-API-KEY>` por tus credenciales de fidelización de Yotpo. La página `email_address` se extrae dinámicamente de Braze. Para que la integración funcione, el correo electrónico debe ser la dirección de correo electrónico del cliente que recibe el correo.

El fragmento de código tendrá el siguiente aspecto:

![Ejemplo de editor de correo electrónico que muestra un fragmento de saldo de fidelización de clientes]({% image_buster /assets/img/yotpo/image5.png %})

## Preguntas más frecuentes {#faq}

#### ¿Qué pasa si no tengo una opinión de 5 estrellas?

Si no tienes ninguna reseña de 5 estrellas (por ejemplo, si la respuesta del punto final devuelve NULL para la reseña de 5 estrellas), no se mostrará ningún contenido.

#### ¿Qué pasa si no tengo una imagen publicada para un producto?

Si no tienes ninguna imagen para un producto (por ejemplo, si la respuesta del punto final devuelve NULL para la imagen del producto), no se mostrará ningún contenido.

#### ¿Puedo personalizar el aspecto o extraer otros campos de datos de Yotpo?

Sí. Para descubrir otros puntos de datos y opciones de personalización disponibles, consulta [Realizar una llamada a la API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Puede que necesites la ayuda de un desarrollador front-end para hacerlo.

{% alert note %}
Yotpo no admite requisitos personalizados más allá de lo descrito en esta guía.
{% endalert %}


