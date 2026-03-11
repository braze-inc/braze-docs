---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 12
description: "Este artículo responde a las preguntas más frecuentes sobre Liquid."

---

# Preguntas más frecuentes

> En esta página encontrará respuestas a algunas preguntas frecuentes sobre Liquid.<br><br>Braze no es compatible actualmente con el 100 % de Liquid en Shopify, solo con ciertas partes que hemos intentado describir en nuestra documentación. Recomendamos encarecidamente probar todos los mensajes con Liquid antes de enviarlos para reducir el riesgo de errores o de utilizar Liquid no compatible.

### ¿Cómo se utilizan los fragmentos de código Liquid en Braze?

En muchos casos, puede incorporar fragmentos de Liquid navegando a sus campañas o Canvases, e insertando Liquid en el modal de personalización en áreas como el cuerpo del mensaje de correo electrónico o en sus segmentos. 

#### ¿Dónde puedo obtener más información?

Para más información sobre Liquid, consulta nuestra ruta guiada de [Personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) de Braze Learning. También puedes consultar la [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) para inspirarte y ver una serie de ejemplos de personalización con Liquid.

### ¿Cuál es la diferencia entre utilizar Liquid y Connected Content para la personalización?

Braze Connected Content es un ejemplo de etiqueta Liquid. También se utiliza para la personalización, pero estos datos proceden de un punto final externo y no de datos almacenados dentro de Braze. Echa un vistazo a nuestra sección dedicada [al Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para saber más sobre cómo personalizar tus mensajes.

### ¿Qué son las plantillas de Liquid?

Esta es la forma más común de utilizar líquido en soldadura fuerte. La plantilla líquida consiste en introducir datos del perfil de un usuario en un mensaje. Estos datos pueden ir desde el nombre de pila de un usuario hasta eventos personalizados de un mensaje activado por un evento.

Consulte [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para obtener una lista completa de las etiquetas Liquid compatibles.

### ¿Cómo asigno variables con Liquid?

Puede crear y asignar variables utilizando la etiqueta `assign`. Esto crea una variable en el compositor del mensaje a la que también se puede hacer referencia en todo el mensaje.

### ¿El uso de Liquid registra puntos de datos?

No.

### ¿Cómo puedo utilizar Liquid para enviar una felicitación personalizada?

Para un saludo personalizado utilizando el nombre de pila de un usuario, puede recurrir a los atributos estándar del perfil de usuario, como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

También puede utilizar una sentencia Liquid `{% if X %}` {% endraw %}para realizar una renderización condicional basada en cualquier cosa, como el día de la semana o atributos personalizados. Para obtener más información sobre los operadores Liquid admitidos que pueden utilizarse en sentencias condicionales, consulte [Operadores]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### ¿Cómo puedo personalizar un mensaje en función de la ubicación de un cliente?

{% raw %}
Existe un atributo por defecto para la ubicación del usuario: `{{${most_recent_location}}}`.

### ¿Cuál es la diferencia entre {{campaign.${name}}} y {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` como `{{campaign.${message_name}}}` admiten etiquetas de personalización líquida. Ambas etiquetas hacen referencia a atributos de campaña. `{{campaign.${name}}}` denota el nombre de su campaña, y `{{campaign.${message_name}}}` es el nombre de la variante de su mensaje.
{% endraw %}

### ¿Cómo se utiliza Liquid con objetos anidados?

Braze incorpora una función que genera código Liquid para segmentos que pueden utilizarse en un mensaje. En concreto, puede crear un segmento que coincida con varios criterios de un objeto.

Para más información, consulte [Segmentación multicriterio]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### ¿Cómo puedo utilizar los atributos de los eventos para personalizar el mensaje que desencadena un evento?

{% raw %}
Puede acceder a las propiedades de los eventos activados por la API con la etiqueta `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### ¿Qué es la lógica de aborto y cómo puedo utilizarla?

La lógica de abortar permite detener el envío de un mensaje si se cumplen las condiciones. Esto es especialmente útil para evitar que se envíen mensajes incompletos a sus usuarios. Para ver ejemplos de lógica de cancelación en sus campañas de marketing, lea más en [Cancelación de mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### ¿Qué es la lógica del bucle for y cómo puedo utilizarla?

Los bucles For también se conocen como [etiquetas de iteración](https://shopify.github.io/liquid/tags/iteration/). El uso de la lógica de bucle for en sus fragmentos de Liquid le permite recorrer bloques de Liquid hasta que se cumpla una condición. 

En Braze, esto podría utilizarse para comprobar elementos en un atributo personalizado de matriz, o una lista de valores y objetos devueltos por una respuesta de [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) o llamada a [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). En concreto, puede utilizar la lógica del bucle for como parte de su mensajería para comprobar si un producto está en stock, o si un producto tiene una valoración mínima. 

Por ejemplo, supongamos que tienes un catálogo llamado «Juegos» que contiene una selección llamada"cheap_games".  Para extraer los títulos de los juegos,"cheap_games",  puedes utilizar este fragmento de código de Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Una vez cumplidas las condiciones establecidas, su mensaje puede continuar. Utilizar esta lógica es una forma útil de ahorrar tiempo, en lugar de repetir bloques Líquidos para diferentes condiciones.

### ¿Por qué hay un espacio adicional en los mensajes que utilizan bloques de contenido?

Si observas un espaciado adicional en los mensajes enviados que utilizan bloques de contenido con Liquid, es posible que haya saltos de párrafo o de línea innecesarios dentro de tus declaraciones condicionales. Escribe tus sentencias condicionales en una sola línea en lugar de en varias líneas.

#### Ejemplo

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}
