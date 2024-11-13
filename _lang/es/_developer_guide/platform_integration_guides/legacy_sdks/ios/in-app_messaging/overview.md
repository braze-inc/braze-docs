---
nav_title: Resumen
article_title: Resumen de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 0
description: "En este artículo de referencia se cubren los tipos de mensajería dentro de la aplicación de iOS, los comportamientos esperados y varios ejemplos."
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Mensajes dentro de la aplicación

[Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) te ayudan a hacer llegar contenido a tu usuario sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una gran variedad de diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca.

Consulta nuestros [casos de estudio](https://www.braze.com/customers) para ver ejemplos de mensajes dentro de la aplicación.

## Tipos de mensajes dentro de la aplicación

Braze ofrece actualmente los siguientes tipos predeterminados de mensajes dentro de la aplicación: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Cada tipo de mensaje dentro de la aplicación es altamente personalizable en cuanto a contenido, imágenes, iconos, acciones de clic, análisis, visualización y entrega.

Todos los mensajes dentro de la aplicación son subclases de `ABKInAppMessage`, que define el comportamiento básico y los rasgos de todos los mensajes dentro de la aplicación. Las estructuras de las clases de mensajes dentro de la aplicación son las siguientes:

![Un gráfico que muestra que la clase ABKInAppMessage es la clase raíz de las clases ABKInAppMessageSlideup, ABKInAppMessageImmersive y ABKInAppMessageHTML. El ABKInAppMessage incluye propiedades personalizables como mensaje, extras, duración, acción de clic, URI, acción de descartar, orientación del icono y alineación del texto. El ABKInAppMessageSlideup incluye propiedades personalizables como el chevron y el ancla deslizante. El ABKInAppMessageImmersive incluye propiedades personalizables como la cabecera, el botón de cierre, el marco y los botones de mensajes dentro de la aplicación. ABKInAppMessageHTML te permite registrar manualmente los clics en el botón HTML de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
Por defecto, los mensajes dentro de la aplicación se habilitan tras completar la integración de SDK estándar, incluida la compatibilidad con GIF.
<br><br>
Ten en cuenta que la integración de `SDWebImage` es necesaria si piensas utilizar nuestra interfaz de usuario Braze para mostrar imágenes en los mensajes dentro de la aplicación iOS o en las tarjetas de contenido.
{% endalert %}

### Comportamientos esperados por tipos de mensajes

Así es como se ven tus usuarios al abrir uno de nuestros tipos predeterminados de mensajes dentro de la aplicación.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) Los mensajes dentro de la aplicación se llaman así porque "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje dentro de la aplicación que se desliza desde la parte inferior de la pantalla de un teléfono y que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en la esquina inferior de una página Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones de acción por clic y habilitados para análisis.

![Un mensaje modal dentro de la aplicación en el centro de una pantalla de teléfono que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en el centro de una página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen, y la mitad inferior muestra texto y hasta dos botones de acción de clic y habilitación de análisis.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono y que dice: "Los humanos somos complicados. La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en gran parte en el centro de una página Web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) Los mensajes dentro de la aplicación son útiles para crear contenido de usuario totalmente personalizado. El contenido HTML completo de los mensajes dentro de la aplicación, definido por el usuario, se muestra en `WKWebView`y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. <br><br>Los mensajes dentro de la aplicación de iOS admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK de la Web de Braze desde dentro de tu HTML, consulta nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) para obtener más detalles.

El siguiente ejemplo muestra un mensaje HTML completo paginado dentro de la aplicación:

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

El contenido completo de los mensajes dentro de la aplicación se muestra en `WKWebView` y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. Ten en cuenta que actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.

{% alert note %}
A partir de la versión 3.19.0 del SDK de iOS, los siguientes métodos JavaScript no funcionan en los mensajes HTML dentro de la aplicación: `alert`, `confirm`, `prompt`.
{% endalert %}

{% endtab %}
{% endtabs %}

