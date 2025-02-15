---
nav_title: Integración
article_title: Integración de mensajes dentro de la aplicación para Web
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "Este artículo incluye recursos sobre los tipos de mensajes dentro de la aplicación y el comportamiento de los mensajes para tu aplicación Web."
search_rank: 2
---

# Integración de mensajes dentro de la aplicación

> Este artículo explica cómo configurar mensajes dentro de la aplicación Web.

[Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) te ayudan a hacer llegar contenido a tus usuarios sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con varios diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca.

Consulta nuestros [casos de estudio](https://www.braze.com/customers) para ver ejemplos de mensajes dentro de la aplicación.

## Tipos de mensajes dentro de la aplicación

Braze ofrece actualmente los siguientes tipos predeterminados de mensajes dentro de la aplicación: 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

Cada tipo de mensaje dentro de la aplicación es personalizable en contenido, imágenes, iconos, acciones de clic, análisis, visualización y entrega.

Todos los mensajes dentro de la aplicación heredan su prototipo de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)que define el comportamiento básico y las características de todos los mensajes dentro de la aplicación. Las subclases prototípicas son [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)y [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

## Comportamientos esperados según el tipo de mensaje

Así es como se ven tus usuarios al abrir uno de nuestros tipos predeterminados de mensajes dentro de la aplicación.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) Los mensajes dentro de la aplicación se llaman así porque tradicionalmente, en las plataformas móviles, se "deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. En el SDK Web de Braze, estos mensajes se muestran más como una notificación estilo Growl o Toast para alinearse con el paradigma dominante en la Web. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje dentro de la aplicación que se desliza desde la parte inferior de la pantalla de un teléfono y que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en la esquina inferior de una página Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones de acción por clic y habilitados para análisis.

![Un mensaje modal dentro de la aplicación en el centro de una pantalla de teléfono que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en el centro de una página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. En ventanas de navegador estrechas (por ejemplo, la web móvil), los mensajes dentro de la aplicación `full` ocupan toda la ventana del navegador. En las ventanas más grandes del explorador, los mensajes dentro de la aplicación `full` aparecen de forma similar a los mensajes dentro de la aplicación `modal`. La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen, y la mitad inferior permite hasta ocho líneas de texto, así como hasta dos botones de acción de clic y habilitación de análisis.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono y que dice: "Los humanos somos complicados. La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en gran parte en el centro de una página Web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) Los mensajes dentro de la aplicación son útiles para crear contenido de usuario totalmente personalizado. El HTML definido por el usuario se muestra en un iFrame y puede contener contenido enriquecido, como imágenes, fuentes, videos y elementos interactivos, lo que permite un control total sobre la apariencia y funcionalidad del mensaje. Éstos admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK de la Web de Braze desde dentro de tu HTML, consulta nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) para más detalles.

{% alert important %}

Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, **debes** proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad. Los mensajes HTML dentro de la aplicación pueden ejecutar JavaScript, por lo que necesitamos que un mantenedor del sitio los habilite.

{% endalert %}

El siguiente ejemplo muestra un mensaje HTML paginado dentro de la aplicación:

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## Integración

Por predeterminado, los mensajes dentro de la aplicación se muestran automáticamente como parte de nuestras [instrucciones de integración] recomendadas ({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/). Se puede realizar una personalización adicional siguiendo los pasos de esta guía.

