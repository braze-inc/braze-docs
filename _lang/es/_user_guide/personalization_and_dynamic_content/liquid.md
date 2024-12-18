---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "Personalización mediante etiquetas líquidas"
guide_top_text: "Braze puede sustituir automáticamente los valores de un usuario determinado en tus mensajes. Coloque la expresión dentro de dos conjuntos de llaves para notificar a Braze que utilizará un valor interpolado. Dentro de estos corchetes, cualquier valor de usuario que desee sustituir debe ir rodeado de un conjunto adicional de corchetes con un signo de dólar delante.<br><br>Para más información sobre Liquid, consulta nuestra ruta guiada de <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Personalización dinámica con Liquid</a></b> de Braze Learning."
description: "Esta página de destino cubre todos los aspectos de Liquid, como las etiquetas de personalización compatibles, los filtros, la configuración de valores predeterminados y mucho más."

guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Utilizar Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Etiquetas de personalización admitidas
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Operadores
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filtros
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtros avanzados
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Establecer valores por defecto
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Lógica de mensajería condicional
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Anular mensajes
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Casos de uso de Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: Tutoriales
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Preguntas frecuentes
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## Acerca de Liquid

> Liquid es un lenguaje de plantillas de código abierto desarrollado por Shopify y escrito en Ruby. En Braze, Liquid se utiliza para incorporar datos del perfil de un usuario a los mensajes. 

Por ejemplo, puede recuperar un atributo personalizado de un perfil de usuario que sea un tipo de datos entero y redondear ese valor al número entero más cercano. Para obtener más información sobre la sintaxis y el uso de Liquid, consulte [**Etiquetas de personalización compatibles**][1].

El lenguaje de plantillas Liquid admite el uso de objetos, etiquetas y filtros.

- [**Los objetos**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) le permiten insertar atributos personalizados en sus mensajes.
- [**Etiquetas**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) te permiten insertar datos en la mensajería y utilizar la lógica condicional para enviar mensajes si se cumplen determinadas condiciones. Por ejemplo, puede utilizar etiquetas para incluir lógica inteligente, como sentencias "if", en sus campañas.
- [**Los filtros**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) permiten reformatear atributos personalizados y contenidos dinámicos. Por ejemplo, puedes utilizar el [filtro`date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) para convertir una marca de tiempo, como *2016-09-07 08:43:50 UTC*, en una fecha, como *7 de septiembre de 2016*.

{% alert warning %}
Actualmente, Braze no es compatible con el 100% de Liquid de Shopify, sólo con ciertas partes que hemos intentado describir en nuestra documentación. Recomendamos encarecidamente probar todos los mensajes con Liquid antes de enviarlos para reducir el riesgo de errores o de utilizar Liquid no compatible.
{% endalert %}

### Soporte Liquid 5

Braze es compatible con Liquid, incluido **Liquid 5 de Shopify**. La implementación de Liquid admite tipos de etiquetas de personalización de sintaxis y control de espacios en blanco. Para más información sobre etiquetas concretas, consulta las [etiquetas de sintaxis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Los siguientes nuevos filtros de matrices y matemáticas están disponibles para su uso en su Liquid a medida que construye su mensajería.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consulta las definiciones en [Filtros]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/).

### Actualizaciones líquidas

#### Etiquetas de color

Cada elemento Liquid se corresponde con un color, lo que te permite diferenciar tu Liquid de un vistazo en tu editor Liquid.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### Predicción Liquid

También puedes aprovechar la predicción Liquid para atributos personalizados, nombres de atributos y mucho más, a medida que construyes tus mensajes personalizados.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Términos que debe conocer

Estos términos se reinterpretan a partir de [**documentación de Shopify**](https://shopify.github.io/liquid/basics/introduction/) en función de nuestro nivel de soporte.

{% raw %}

| Plazo | Definición | Ejemplo |  
|---|---|---|
| Liquid | Un lenguaje de plantillas de uso común y orientado al cliente, creado por Shopify y escrito en Ruby, que se utiliza para cargar y extraer contenido dinámico. | `{{${first_name}}}` insertará el nombre de pila de un usuario en un mensaje. |
| Objeto | Denotación de una variable y ubicación del nombre de la variable prevista que indica a Liquid dónde mostrar el contenido en el mensaje. | `{{${city}}}` insertará la ciudad de un usuario en un mensaje. |
| Etiqueta de lógica condicional | Se utiliza para crear la lógica y controlar el flujo del contenido de los mensajes. En Braze, las etiquetas de lógica condicional se utilizan para crear excepciones y variaciones en los mensajes en función de determinados criterios predefinidos. | ```{% if ${language} == 'en' %}``` activará su mensaje de la forma designada en caso de que un usuario haya designado el "inglés" como su idioma. |
| Filtros | Se utiliza para cambiar, reducir o reformatear la salida del objeto Líquido. Suele utilizarse para crear operaciones matemáticas. | ```{{"Big Sale" | upcase}}``` hará que las palabras "Gran Venta" aparezcan como "GRAN VENTA" en el mensaje. |
| Operadores | Se utiliza en los mensajes para crear dependencias o criterios que pueden afectar al mensaje que recibe el usuario. | Si un usuario cumple los criterios definidos en un mensaje etiquetado con `{% custom_attribute.${Total_Revenue} > 0%}`, recibirá el mensaje. Si no, recibirán otro mensaje designado (o no), dependiendo de lo que hayas establecido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
