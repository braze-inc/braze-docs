---
nav_title: Vista de carrusel
article_title: Vista de carrusel de tarjetas de contenido para iOS
platform: iOS
page_order: 5
description: "Este artículo explica cómo implementar un caso de uso de vista de carrusel de tarjetas de contenido para aplicaciones iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Casos de uso: Vista de carrusel

![Ejemplo de aplicación de noticias que muestra un carrusel de tarjetas de contenido en un artículo.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Esta sección explica cómo implementar una fuente de carrusel de varias tarjetas en la que el usuario puede deslizar horizontalmente el dedo para ver más tarjetas destacadas. Para integrar una vista de carrusel, tendrás que utilizar una implementación de tarjeta de contenido totalmente personalizada: la fase "correr" del [enfoque "rastrear, caminar, correr"]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches).

Con este enfoque, no utilizarás las vistas Braze ni la lógica predeterminada, sino que mostrarás las tarjetas de contenido de forma totalmente personalizada utilizando tus propias vistas pobladas con datos de los modelos Braze.

En términos de nivel de esfuerzo de desarrollo, las diferencias clave entre la implementación básica y la implementación de carrusel incluyen:

- Construir tus propias vistas
- Registro de análisis de tarjeta de contenido
- Introducir lógica adicional en el lado del cliente para dictar cuántas y qué tarjetas mostrar en el carrusel.

## Aplicación

### Paso 1: Crear un controlador de vista personalizado

Para crear el carrusel de tarjetas de contenido, crea tu propio controlador de vista personalizado (como `UICollectionViewController`) y [suscríbete para recibir actualizaciones de datos]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data). Ten en cuenta que no podrás ampliar o subclasificar nuestro `ABKContentCardTableViewController` predeterminado, ya que sólo puede gestionar los tipos de tarjeta de contenido predeterminados.

### Paso 2: Implementar análisis

Al crear un controlador de vista totalmente personalizado, las impresiones, los clics y los rechazos de la tarjeta de contenido no se registran automáticamente. Debes implementar los métodos de análisis respectivos para asegurarte de que las impresiones, los eventos de rechazo y los clics se registran correctamente en los análisis del panel de Braze.

Para obtener información sobre los métodos de análisis, consulta [Métodos de tarjeta]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods). 

{% alert note %}
En la misma página también se detallan las distintas propiedades heredadas de nuestra clase modelo genérica Tarjeta de contenido, que pueden resultarte útiles durante la implementación de tu vista.
{% endalert %}

### Paso 3: Crear un observador de tarjetas de contenido

Crea un [observador de tarjetas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) de contenido que se encargue de gestionar la llegada de tarjetas de contenido, e implementa una lógica condicional para mostrar un número específico de tarjetas en el carrusel en un momento dado. Por defecto, las tarjetas de contenido se ordenan por fecha de creación (la más reciente primero), y un usuario ve todas las tarjetas para las que es elegible.

Dicho esto, podrías ordenar y aplicar lógica de visualización adicional de varias formas. Por ejemplo, podrías seleccionar los cinco primeros objetos de la tarjeta de contenido de la matriz o introducir pares clave-valor (la propiedad `extras` en el modelo de datos) para construir una lógica condicional en torno a ellos.

Si estás implementando un carrusel como fuente secundaria de tarjetas de contenido, consulta [Utilizar múltiples fuentes de tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/) para asegurarte de que ordenas las tarjetas en la fuente correcta basándote en los pares clave-valor.

{% alert important %}
Es importante asegurarse de que tus equipos de marketing y desarrolladores se coordinan para decidir qué pares clave-valor se utilizarán (por ejemplo, `feed_type = brand_homepage`), ya que cualquier par clave-valor que los especialistas en marketing introduzcan en el panel Braze debe coincidir exactamente con los pares clave-valor que los desarrolladores incorporen a la lógica de la aplicación.
{% endalert %}

Para obtener documentación específica para desarrolladores de iOS sobre la clase, los métodos y los atributos de las tarjetas de contenido, consulta la [referencia de la clase`ABKContentCard` ](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) de iOS.

## Consideraciones

- Al utilizar vistas completamente personalizadas, no podrás ampliar ni subclasificar los métodos utilizados en `ABKContentCardsController`. En su lugar, tendrás que integrar tú mismo los métodos y propiedades del modelo de datos.
- La lógica y la implementación de la vista de carrusel no es un tipo predeterminado de tarjeta de contenido en Braze, y por lo tanto la lógica para lograr el caso de uso debe ser suministrada y soportada por tu equipo de desarrollo.
- Tendrás que implementar la lógica del lado del cliente para mostrar un número específico de tarjetas en el carrusel en un momento dado.

