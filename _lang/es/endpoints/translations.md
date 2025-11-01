---
nav_title: Traducciones
article_title: Puntos finales de traducción
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta página de destino enumera los puntos finales de traducción de Braze."
page_type: landing

guide_top_header: "Puntos finales de traducción"
guide_top_text: "Utiliza los puntos finales de traducción Braze para gestionar y actualizar las traducciones en tus campañas y Lienzos."

guide_featured_title: "Puntos finales de la campaña"
guide_featured_list:
  - name: "GET: Ver la traducción de una campaña"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver todas las traducciones de una campaña"
    link: /docs/api/endpoints/translations/campaigns/get_bulk_translations_campaigns/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "COLOCAR: Actualizar la traducción en una campaña"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "GET: Ver la traducción de un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver todas las traducciones de un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_bulk_translations_canvases/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "COLOCAR: Actualizar la traducción en un lienzo"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  
guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "GET: Ver la traducción original"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver traducción y localización específicas"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver todas las traducciones y localizaciones"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "COLOCAR: Actualizar traducciones en una plantilla de correo electrónico"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
Los puntos finales de traducción de Braze se encuentran actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Cómo funcionan nuestros puntos finales de traducción

Nuestros puntos finales de traducción trabajan con [composición multilingüe]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), en la que un mensaje puede tener diferentes versiones que se pueden renderizar dependiendo del usuario que reciba el mensaje.

### Requisitos previos

Antes de utilizar estos puntos finales, debes [añadir tus localizaciones]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### Cómo comprobar tus traducciones

Hay dos formas de validar el soporte de traducción mediante la API y el panel de Braze en las campañas, los lienzos (incluidos los pasos individuales) y las plantillas de correo electrónico:

- Durante la composición (antes del lanzamiento)
- Después del lanzamiento (utilizando borradores posteriores al lanzamiento)

Antes de probar la actualización de las traducciones, debes

1. [Añade tus localizaciones]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Crea un mensaje y utiliza etiquetas de traducción cuando proceda.
3. Guarda el mensaje.
4. Selecciona las localizaciones que quieres incluir.
