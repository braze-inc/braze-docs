---
nav_title: Glosario
article_title: Diseño de glosario
page_order: 0
noindex: true
---

# Ejemplo de diseño: Glosario

> El diseño del glosario está en YAML. Requiere varios componentes y parámetros. Los diseños de glosario son buenos para contenido localizado que se puede buscar, como diccionarios y categorías específicas de contenidos.

## Componentes necesarios

1. Notación YAML de apertura y cierre. En otras palabras, `---` antes del contenido, y `---` después. 
2. Comillas alrededor del contenido de ciertos parámetros. (Parámetros de encabezado, parámetros de texto, contenido con guiones u otros caracteres especiales).
3. Notación de glosario de etiquetas (son etiquetas para filtrar)

## Parámetros requeridos

|Parámetro | Tipo de contenido | Detalles |
|---|---|---|
|`page_order`| numérico | Ordena la página dentro de la sección. Este orden se reflejará en la navegación de la izquierda. |
| `nav-title`| Alfanumérico | Título que aparecerá en la navegación de la izquierda. |
|`layout`| Alfanumérico - Sin espacios | Selecciona un diseño en la [sección de diseño](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentación. | 
|`glossary_top_header` | Alfanumérico | Requiere comillas dobles. El título aparece en la parte superior de la página. |
|`glossary_top_text`| Cadena, alfanumérico | Describe tu página de glosario. Aparecerá encima de la barra de búsqueda y de los filtros (si decides tenerlos). Esto está escrito esencialmente en HTML, por lo que puedes utilizar \`\`\`.<br> para crear saltos de línea. | 
|`glossary_tag_name` | Una palabra, alfanumérico | Pon nombre a tus filtros. Aparecerán en casillas de verificación debajo de la barra de búsqueda, así como en los datos de abajo. | 
|`glossary_filter_text`| Cadena, alfanumérico | Describe tus filtros. Suele utilizarse para instrucción. | 
|`glossary_tags`| Más contenido adicional YAML. | Formato como se muestra a continuación: <br> glossary_tags: <br>  \- nombre: Tarjetas de contenido <br>  \- nombre: Correo electrónico | 
| `glossaries`| Más contenido adicional YAML. | Ver [Parámetros de glosarios](#glossaries-parameters) más abajo. |

### Parámetros de glosarios

|Parámetro | Tipo de contenido | Detalles |
|---|---|---|
|`name`| Alfanumérico | Nombra tu elemento del glosario.| 
|`description`| Cadena, alfanumérico | Describe tu elemento del glosario. | 
|`calculation`| Cadena | (opcional) Describe cómo se calcula tu elemento del glosario (normalmente se utiliza cuando se describen datos o métricas. | 
|`tags`| Alfanumérico | Debe coincidir con lo que figura como `name` en `glossary_tags`. Enumera todos los que correspondan. Si escribes `All`, el elemento se incluirá en todos los filtros.|

## Ejemplo

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
