---
nav_title: Integración
article_title: Resumen de mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 0
description: "En este artículo se cubren los tipos de mensajería dentro de la aplicación de iOS, los comportamientos esperados y varios casos de uso para el SDK Swift."
channel:
  - in-app messages

---

# Integración de mensajes dentro de la aplicación

> [Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) te ayudan a hacer llegar contenido a tu usuario sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una gran variedad de diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca.

Consulta nuestros [casos de estudio](https://www.braze.com/customers) para ver ejemplos de mensajes dentro de la aplicación.

## Tipos de mensajes dentro de la aplicación

Braze ofrece actualmente los siguientes tipos predeterminados de mensajes dentro de la aplicación: 

- deslizamiento hacia arriba
- Modal
- Imagen modal
- Completo
- Imagen completa
- HTML personalizado
- Control

Cada tipo de mensaje dentro de la aplicación es altamente personalizable en cuanto a contenido, imágenes, iconos, acciones de clic, análisis, visualización y entrega.

Para obtener una lista completa de las propiedades y el uso de los mensajes dentro de la aplicación, consulta la [documentación de la clase`InAppMessage` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Todos los mensajes dentro de la aplicación son tipos enumerados de `Braze.InAppMessage`, que define el comportamiento básico y los rasgos de todos los mensajes dentro de la aplicación. Cada tipo de mensaje dentro de la aplicación y sus detalles correspondientes se enumeran en las pestañas de abajo.

### Comportamientos esperados por tipos de mensajes

Así es como se ven tus usuarios al abrir uno de nuestros tipos predeterminados de mensajes dentro de la aplicación.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) Los mensajes dentro de la aplicación se llaman así porque "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje deslizamiento hacia arriba dentro de la aplicación en la parte inferior y superior de la pantalla del teléfono.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones habilitados para análisis.

![Un mensaje modal dentro de la aplicación en el centro de la pantalla del teléfono.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Imagen modal %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Estos mensajes son similares a los del tipo `Modal`, excepto que no tienen cabecera ni texto de mensaje. Útiles para una mensajería más crítica, pueden equiparse con hasta dos botones habilitados para análisis.

![Un mensaje dentro de la aplicación con una imagen modal en el centro de la pantalla del teléfono.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Pantalla completa %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. La mitad superior de un mensaje dentro de la aplicación `Full` contiene una imagen, y la mitad inferior muestra texto y hasta dos botones habilitados para el análisis.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Imagen en pantalla completa %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) Los mensajes dentro de la aplicación son similares a los mensajes dentro de la aplicación `Full`, excepto que no tienen cabecera ni texto de mensaje. Este tipo de mensaje es útil para maximizar el contenido y el impacto de tu comunicación con el usuario. Un mensaje dentro de la aplicación `Full Image` contiene una imagen que abarca toda la pantalla, con la opción de mostrar hasta dos botones habilitados para el análisis.

![Un mensaje dentro de la aplicación con una imagen a pantalla completa que se muestra en toda la pantalla del teléfono.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) Los mensajes dentro de la aplicación son útiles para crear contenido de usuario totalmente personalizado. El contenido HTML completo de los mensajes dentro de la aplicación, definido por el usuario, se muestra en `WKWebView`y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. <br><br>Los mensajes dentro de la aplicación de iOS admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK de la Web de Braze desde dentro de tu HTML, consulta nuestras [mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) para obtener más detalles.

El siguiente ejemplo muestra un mensaje HTML completo paginado dentro de la aplicación:

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Ten en cuenta que actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) Los mensajes dentro de la aplicación no contienen un componente de interfaz de usuario y se utilizan principalmente con fines de análisis. Este tipo se utiliza para verificar la recepción de un mensaje dentro de la aplicación enviado a un grupo de control.

Para más detalles sobre Intelligent Selection y los grupos de control, consulta [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endtab %}
{% endtabs %}


{% alert important %}
La integración de SDK estándar incluye pasos que activan los mensajes dentro de la aplicación, incluida la compatibilidad con GIF. Para más detalles sobre la compatibilidad con GIF, consulta este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}


