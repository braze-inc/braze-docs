---
nav_title: Resumen
page_order: 0
noindex: true
---

# Ejemplo de diseño: Resumen

> El diseño de resumen es bueno para crear una opción de navegación específica en la parte superior de una página que permita a los usuarios hacer clic en un botón para viajar a una parte concreta de una página o a otra completamente distinta.

Ejemplos clásicos del diseño del SELECTOR son la página [de registros de cambios del SDK](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_changelogs/) o [la página de detalles creativos de mensajes dentro de la aplicación](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/).

## Componentes necesarios

1. Notación YAML de apertura y cierre. En otras palabras, --- antes del contenido, y --- después.
2. Comillas alrededor del contenido de ciertos parámetros. (Parámetros de encabezado, parámetros de texto, contenido con guiones u otros caracteres especiales).
3. Notación de glosario de etiquetas (son etiquetas para filtrar)

## Parámetros requeridos

|Parámetro | Tipo de contenido | Detalles |
|---|---|---|
|`page_order`| numérico | Ordena la página dentro de la sección. Este orden se reflejará en la navegación de la izquierda. |
| `nav-title`| Alfanumérico | Título que aparecerá en la navegación de la izquierda. |
|`layout`| Alfanumérico - Sin espacios | Selecciona un diseño en la [sección de diseño](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentación. | 
|`guide_top_header`|Alfanumérico | Titula tu página.|
|`guide_top_text`|Alfanumérico | Describe tu página, esto irá directamente encima de los botones y su título. Se requieren comillas alrededor del contenido. |
|`guide_featured_title`| Alfanumérico | Titula tus tarjetas. Esto irá directamente encima de los botones.
|`guide_featured_list`| Más YAML, Alfanumérico | Consulta el [Formato de la Lista de Guías](#guide-listing-format) más abajo. |

### Formato del listado de guías

|Parámetro | Tipo de contenido | Detalles |
|---|---|---|
|`name`| Alfanumérico | Ponle un nombre a la casilla. |
| `link`| URL o ruta | Enlace al lugar donde irá la casilla. Debe contener la URL completa o (si es un enlace interno) `/docs...`  |
|`image`| Recorrido | Enlace a la ubicación de la imagen. |

Ejemplo de formato:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## Ejemplo

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
