---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes
page_order: 12
description: "Este artículo responde a las preguntas más frecuentes sobre Liquid."

---

# Preguntas más frecuentes

> En esta página encontrarás respuestas a algunas preguntas frecuentes sobre Liquid.<br><br>Braze no es compatible actualmente con el 100% de Liquid de Shopify, sólo con ciertas partes que hemos intentado describir en nuestra documentación. Recomendamos encarecidamente probar todos los mensajes utilizando Liquid antes de enviarlos para reducir el riesgo de errores o de utilizar Liquid no compatible.

### ¿Cómo se utilizan los fragmentos de código Liquid en Braze?

En muchos casos, puedes incorporar fragmentos de código Liquid navegando a tus campañas o Lienzos, e insertando Liquid en el modal de personalización en áreas como el cuerpo del mensaje de correo electrónico o en tus segmentos. 

#### ¿Dónde puedo obtener más información?

Para saber más sobre Liquid, ¡consulta nuestra ruta guiada de [personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learning! También puedes consultar la [biblioteca de casos de uso de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) Liquid para inspirarte y ver una serie de ejemplos de personalización con Liquid.

### ¿Cuál es la diferencia entre utilizar Liquid y Contenido conectado para la personalización?

El Contenido Conectado Braze es un ejemplo de etiqueta de Liquid. También se utiliza para la personalización, pero estos datos proceden de un punto final externo y no de datos almacenados dentro de Braze. Consulta nuestra sección dedicada [al Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para saber más sobre cómo puedes personalizar tus mensajes.

### ¿Qué es la plantilla Liquid?

Ésta es la forma más habitual de utilizar Liquid en Braze. La plantilla Liquid consiste en introducir datos del perfil de un usuario en un mensaje. Estos datos pueden ir desde el nombre de pila de un usuario hasta eventos personalizados de un mensaje desencadenado por un evento.

Consulta la sección [Etiquetas de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) admitidas para obtener una lista completa de las etiquetas de Liquid admitidas.

### ¿Cómo asigno variables con Liquid?

Puedes crear y asignar variables utilizando la etiqueta `assign`. Esto crea una variable en el creador de mensajes a la que también se puede hacer referencia a lo largo de tu mensaje.

### ¿El uso de Liquid registra puntos de datos?

No.

### ¿Cómo puedo utilizar Liquid para enviar una felicitación personalizada?

Para un saludo personalizado utilizando el nombre de pila de un usuario, puedes recurrir a los atributos estándar del perfil de usuario, como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

También puedes utilizar una sentencia Liquid `{% if X %}` {% endraw %}para hacer una representación condicional basada en cualquier cosa, como el día de la semana o atributos personalizados. Para más información sobre los operadores Liquid admitidos que pueden utilizarse en sentencias condicionales, consulta [Operadores]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### ¿Cómo puedo personalizar un mensaje en función de la ubicación de un cliente?

{% raw %}
Existe un atributo predeterminado para la ubicación del usuario: `{{${most_recent_location}}}`.

### ¿Cuál es la diferencia entre {{campaign.${name}}} y {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` como `{{campaign.${message_name}}}` admiten etiquetas de personalización de Liquid. Ambas etiquetas hacen referencia a atributos de campaña. `{{campaign.${name}}}` indica el nombre de tu campaña, y `{{campaign.${message_name}}}` es el nombre de tu variante de mensaje.
{% endraw %}

### ¿Cómo utilizo Liquid con objetos anidados?

Braze tiene una característica integrada que genera código Liquid para los segmentos que pueden utilizarse en un mensaje. Concretamente, puedes crear un segmento que coincida con varios criterios de un objeto.

Para más información, consulta [Segmentación multicriterio]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### ¿Cómo utilizo los atributos de los eventos para personalizar un mensaje desencadenado por un evento?

{% raw %}
Puedes acceder a las propiedades de los eventos desencadenados por la API con la etiqueta `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### ¿Qué es la lógica de abortar y cómo puedo utilizarla?

La lógica de abortar te permite detener el envío de un mensaje si se cumplen las condiciones. Esto es especialmente útil para evitar que se envíen mensajes incompletos a tus usuarios. Para ver ejemplos de cómo abortar la lógica en tus campañas de marketing, lee más en [Cómo abortar mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### ¿Qué es la lógica del bucle for y cómo puedo utilizarla?

Los bucles For también se conocen como [etiquetas de iteración](https://shopify.github.io/liquid/tags/iteration/). Utilizar la lógica de bucle for en tus fragmentos de código de Liquid te permite recorrer bloques de Liquid hasta que se cumpla una condición. 

En Braze, esto podría utilizarse para comprobar elementos en un atributo personalizado de matriz, o una lista de valores y objetos devueltos por una respuesta de [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) o llamada a [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). En concreto, puedes utilizar la lógica del bucle for como parte de tu mensajería para comprobar si un producto está en stock, o si un producto tiene una tasa mínima. 

Por ejemplo, digamos que tienes un catálogo llamado "Juegos" que tiene una selección llamada "cheap_games".. Para obtener los títulos de los juegos en "cheap_games", podrías utilizar este fragmento de código de Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Una vez cumplidas las condiciones establecidas, tu mensaje puede continuar. Utilizar esta lógica es una forma útil de ahorrar tiempo, en lugar de repetir bloques Liquid para diferentes condiciones.
