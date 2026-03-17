---
nav_title: Operadores
article_title: Operadores de Liquid
page_order: 2
description: "En esta página de referencia se anotan los operadores que admite Liquid, así como ejemplos relevantes."

---

# Operadores

> Liquid admite muchos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que se pueden utilizar en tus sentencias condicionales. Esta página cubre los operadores que admite Liquid y proporciona casos de uso de cómo puedes utilizarlos en tus mensajes.

Esta tabla enumera los operadores compatibles. Ten en cuenta que los paréntesis son caracteres no válidos en Liquid e impiden que tus etiquetas funcionen.

|   Sintaxis| Descripción del operador|
|---------|-----------|
| ==  | equivale a        |
| !=  | no equivale a|
|  >  | superior a  |
| <   | menos de     |
| >=| mayor o igual que|
| <= | inferior o igual a |
| o | condición A o condición B|
| y | condición A y condición B|
| contiene | comprueba si una cadena o matriz de cadenas contiene una cadena|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Los operadores se pueden utilizar en sentencias condicionales (`if`, `elsif`, `unless`), pero no en`assign`sentencias ,`for`bucles, sentencias`case``when` / ni corchetes de acceso a matrices. Para obtener información detallada, consulta [Dónde utilizar operadores y filtros para filtrar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Agrupación de condiciones sin paréntesis

Liquid no admite paréntesis para agrupar expresiones. Para evaluar lógicas booleanas complejas como `(a and b) or c`, utiliza sentencias `if`anidadas  o variables intermedias.

Por ejemplo, para comprobar si un valor cumple una condición compuesta, asigna una variable intermedia:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriales

Veamos algunos tutoriales para aprender a utilizar estos operadores en tus campañas de marketing:

### Elige un mensaje con un atributo personalizado entero.

Enviemos notificaciones push con descuentos promocionales personalizados a los usuarios que hayan o no realizado compras. La notificación push utilizará un atributo personalizado entero llamado `total_spend` para comprobar el gasto total de un usuario.

1. Escribe una sentencia condicional utilizando el operador mayor que (`>`) para comprobar si el gasto total de un usuario es mayor que `0`, lo que indica que ha realizado una compra. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Añade la etiqueta {% raw %}`{% else %}`{% endraw %} para capturar a los usuarios cuyo gasto total sea igual a `0` o no exista. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. Cierra la lógica condicional con la etiqueta {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Un compositor de notificaciones push con el código completo de Liquid del tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Ahora, si el atributo personalizado «Gasto total» de un usuario es superior a `0`, recibirás el mensaje:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Si el atributo personalizado "Gasto total" de un usuario no existe o es igual a `0`, recibirá el siguiente mensaje:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Elige un mensaje con un atributo personalizado de cadena.

Enviemos notificaciones push a los usuarios y personalicemos el mensaje en función del juego más reciente de cada usuario. Esto utilizará un atributo personalizado de cadena llamado `recent_game` para comprobar a qué juego ha jugado por última vez un usuario.

1. Escribe una sentencia condicional utilizando el operador igual (`==`) para comprobar si el juego más reciente de un usuario es *Awkward Dinner Party*. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Utiliza la etiqueta `elsif` con el operador igual (`==`) para comprobar si el juego más reciente del usuario es *Proxy War 3: Guerra de sed*. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. Utiliza la`elsif`etiqueta  con los operadores «no es igual a» (`!=`) y «y» (`and`) para comprobar si el usuario tiene un juego reciente (es decir, si el valor no está en blanco) y si el juego no es *Awkward Dinner Party* o *Proxy War 3: Guerra de sed*. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Añade la etiqueta {% raw %}`{% else %}`{% endraw %} para capturar a los usuarios que no tienen un juego reciente. A continuación, crea un mensaje para enviarlo a esos usuarios.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. Cierra la lógica condicional con la etiqueta {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositor de notificaciones push con el código completo de Liquid del tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Ahora, si un usuario ha jugado por última vez *a Awkward Dinner Party*, recibirá este mensaje:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Si el juego más reciente de un usuario es *Proxy War 3: Guerra de Sed*, recibirán este mensaje:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Si un usuario ha jugado recientemente a un juego que no fuera *Awkward Dinner Party* o *Proxy War 3: Guerra de sed*, recibirán este mensaje:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Si un usuario no ha jugado a ningún juego o ese atributo personalizado no existe en su perfil, recibirá este mensaje:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Mensaje de cancelación basado en la ubicación

Puedes abortar un mensaje basándote en casi cualquier cosa. Abortemos un mensaje si un usuario no reside en una zona especificada, ya que podría no cumplir los requisitos para la promoción, el espectáculo o la entrega.

1. Escribe una sentencia condicional utilizando el operador igual (`==`) para comprobar si la zona horaria del usuario es `America/Los_Angeles`, y luego crea un mensaje para enviar a esos usuarios. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. Para evitar enviar mensajes a usuarios fuera de la zona horaria `America/Los_Angeles`, envuelve las etiquetas {% raw %}`{% else %}`{% endraw %} y {% raw %}`{% endif %}`{% endraw %} alrededor de una etiqueta {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositor de notificaciones push con el código completo de Liquid del tutorial.]({% image_buster /assets/img/abort-if.png %})

También puede [abortar mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) basados en Contenido conectado.

## Solución de problemas

### La vista previa puede forzar incorrectamente los tipos de propiedades. 

Al realizar la vista previa de un mensaje en el panel, la mayoría de las variables (como los atributos personalizados) se convierten al tipo correcto. Sin embargo, algunas variables no tienen un tipo definido que la vista previa pueda buscar:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Para estas propiedades, la vista previa intenta deducir el tipo a partir del valor. Esto significa que un valor que pretendes que sea una **cadena** podría interpretarse erróneamente como un **número**. Por ejemplo, si el valor de una propiedad es una cadena `"3"`, la vista previa puede convertirlo en un entero `3`, lo que puede provocar un comportamiento inesperado en operaciones con cadenas como`contains`  o `split`.

Si observas resultados de vista previa inesperados al utilizar estos tipos de propiedades, ten en cuenta que la inferencia de tipos de la vista previa puede no coincidir con lo que ocurre en el momento del envío. En el momento del envío, se conservan los tipos de datos reales del evento que desencadena o de la llamada a la API.

Para forzar un tipo específico en la vista previa, puedes convertir explícitamente el valor:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}