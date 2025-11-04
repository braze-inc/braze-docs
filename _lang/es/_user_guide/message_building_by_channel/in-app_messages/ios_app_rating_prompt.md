---
nav_title: Pregunta de valoración en la aplicación para iOS
article_title: Aviso de tasa en la aplicación para iOS
page_order: 6
description: "Este artículo describe los enfoques y las implicaciones de utilizar Braze para pedir a los usuarios que revisen tu aplicación."
channel:
  - in-app messages

---

# Aviso de tasa en la aplicación para iOS

> Este artículo describe los enfoques y las implicaciones de utilizar Braze para pedir a los usuarios que revisen tu aplicación. Para obtener consejos sobre cómo hacer una campaña eficaz de valoración de aplicaciones, consulta [Qué hacer y qué no hacer en las valoraciones de aplicaciones por parte de los clientes](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple ofrece un aviso nativo, introducido con iOS 10.3, que permite a los usuarios valorar las aplicaciones desde la propia aplicación. Si quieres solicitar valoraciones de la aplicación a los usuarios mediante un mensaje dentro de la aplicación en iOS, debes utilizar el mensaje nativo, ya que Apple no permite mensajes de valoración personalizados (consulta [las Directrices de valoración de la App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), sección 5.6.1).

Según las directrices de Apple, los avisos de revisión de aplicaciones pueden mostrarse a un usuario hasta tres veces al año, por lo que cualquier campaña de revisión de aplicaciones debe aprovechar la [limitación de tasas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Los usuarios también pueden optar por no ver los avisos de revisión de la aplicación en su configuración. Para más información sobre las tasas del App Store, consulta el artículo de Apple sobre [Valoraciones, reseñas y respuestas](https://developer.apple.com/app-store/ratings-and-reviews/).

## Utilizar Braze para pedir a los usuarios opiniones sobre la aplicación

Aunque Apple exige que utilices el indicador nativo, puedes aprovechar las campañas Braze para pedir a los usuarios que valoren y revisen tu aplicación en el momento adecuado. Hay dos enfoques principales que puedes adoptar.

### Enfoque 1: Vinculación en profundidad con la App Store

Con este enfoque, quieres animar a los usuarios a visitar la App Store para añadir una opinión. Para ello, crea una campaña de mensajería dentro de la aplicación que [enlace]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) en profundidad con el App Store.

Dos pantallas de móvil una al lado de la otra. El primero es un mensaje dentro de la aplicación que pide al usuario que valore la aplicación en la App Store. La segunda es la página de iOS App Store de esa aplicación.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Enfoque 2: Cebado suave

Si no quieres que los usuarios abandonen tu aplicación, puedes prepararles primero con un mensaje dentro de la aplicación. El cebado es una forma de pedir permiso a los usuarios antes de enviarles la solicitud de revisión nativa de la App Store. Para ello, crea una campaña de mensajería dentro de la aplicación y añade un vínculo profundo personalizado que llame al método `requestReview` cuando se haga clic en él. 

Para conocer los pasos detallados, consulta la [solicitud de revisión personalizada de la App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

Dos mensajes dentro de la aplicación uno al lado del otro. La primera prepara al usuario para valorar la aplicación preguntándole si tiene un momento para hacerlo. El segundo es el mensaje nativo de revisión de la App Store de iOS, que muestra una escala de cinco estrellas que el usuario puede seleccionar para valorar la aplicación.]({% image_buster /assets/img_archive/prime_app_review.png %})

Los usuarios enviarán una tasa a través de la solicitud de opinión nativa del App Store, y pueden escribir y enviar una opinión sin salir de la aplicación.

### Consideraciones

Como alternativa a la imprimación suave, también puedes mostrar directamente el aviso de valoración de la aplicación iOS sin que aparezca antes ningún mensaje de imprimación suave Braze. La ventaja de esto es que si el usuario opta por no recibir avisos de revisión de la aplicación, no se produciría la experiencia de usuario subóptima de intentar valorar la aplicación sin que aparezca ningún aviso para hacerlo.

{% alert important %}
No crees mensajes HTML personalizados dentro de la aplicación que imiten el aviso de tasa de una aplicación nativa de iOS, ya que esto infringe las directrices de Apple.
{% endalert %}

