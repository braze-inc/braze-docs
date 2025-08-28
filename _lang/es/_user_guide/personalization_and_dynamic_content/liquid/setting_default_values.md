---
nav_title: Establecer valores por defecto
article_title: Configuración de valores predeterminados de Liquid
page_order: 5
description: "En este artículo de referencia se explica cómo establecer valores de reserva predeterminados para cualquier atributo de personalización que utilices en tus mensajes."

---

# Establecer valores por defecto

{% raw %}

> Se pueden establecer valores por defecto para cualquier atributo de personalización que utilices en tus mensajes. Este artículo explica cómo funcionan los valores predeterminados, cómo configurarlos y cómo utilizarlos en tus mensajes.

## Cómo funcionan

Se pueden añadir valores por defecto especificando un filtro [Liquid](http://docs.shopify.com/themes/liquid-documentation/filters) (utilice `|` para distinguir el filtro en línea, como se muestra) con el nombre "default".

```
| default: 'Insert Your Desired Default Here'
```

Si no se proporciona un valor predeterminado y el campo falta o no está configurado en el usuario, el campo aparecerá en blanco en el mensaje.

El siguiente ejemplo muestra la sintaxis correcta para añadir un valor por defecto. En este caso, las palabras "Usuario valorado" sustituirán al atributo `{{ ${first_name} }}` si el campo `first_name` de un usuario está vacío o no está disponible.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

A un usuario llamado Janet Doe, el mensaje le aparecería como

```
Hi Janet, thanks for using the App!
```

O...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
El valor predeterminado se mostrará para los valores vacíos, pero no para los vacíos. Un valor vacío no contiene nada, mientras que un valor en blanco contiene caracteres de espacio en blanco (como espacios) y ningún otro carácter. Por ejemplo, una cadena vacía podría parecerse a `""` y una cadena en blanco a `" "`.
{% endalert %}

## Configuración de valores predeterminados para distintos tipos de datos

El ejemplo anterior muestra cómo establecer un valor predeterminado para una cadena. Puedes establecer valores predeterminados para cualquier tipo de dato Liquid que tenga el valor `empty`, `nil` (indefinido) o `false`, lo que incluye cadenas, booleanos, matrices, objetos y números.

### Casos de uso: Booleanos

Supongamos que tienes un atributo personalizado booleano llamado `premium_user` y quieres enviar un mensaje personalizado basado en el estado Premium del usuario. Algunos usuarios no tienen un estado Premium configurado, por lo que tendrás que establecer un valor predeterminado para capturar a esos usuarios.

1. Asignarás una variable llamada `is_premium_user` al atributo `premium_user` con un valor predeterminado de `false`. Esto significa que si `premium_user` es `nil`, el valor de `is_premium_user` será predeterminado a `false`. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\. A continuación, utiliza la lógica condicional para especificar el mensaje a enviar si `is_premium_user` es `true`. En otras palabras, qué enviar si `premium_user` es `true`. También asignarás un valor predeterminado al nombre del usuario, por si no tenemos su nombre.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\. Por último, especifica qué mensaje enviar si `is_premium_user` es `false` (lo que significa que `premium_user` es `false` o `nil`). Entonces cerrarás la lógica condicional.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Código completo de Liquid %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Casos de uso: Números

Supongamos que tienes un atributo personalizado numérico llamado `reward_points` y quieres enviar un mensaje con los puntos de recompensa del usuario. Algunos usuarios no tienen puntos de recompensa configurados, por lo que tendrás que establecer un valor predeterminado para tener en cuenta a esos usuarios.

1. Comienza el mensaje dirigiéndote al nombre de pila del usuario o con un valor predeterminado de `Valued User`, en caso de que no tengas su nombre.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Finaliza el mensaje con cuántos puntos de recompensa tiene el usuario utilizando el atributo personalizado llamado `reward_points` y utilizando el valor predeterminado de `0`. Todos los usuarios cuyo `reward_points` tenga un valor de `nil` tendrán `0` puntos de recompensa en el mensaje.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Casos de uso: Objetos

Digamos que tienes un objeto atributo personalizado anidado llamado `location` que contiene las propiedades `city` y `state`. Si alguna de estas propiedades no está configurada, debes animar al usuario a que te la proporcione.

1. Dirígete al usuario por su nombre e incluye un valor predeterminado, en caso de que no tengas su nombre.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. Escribe un mensaje que diga que te gustaría confirmar la ubicación del usuario.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\. Inserta la ubicación del usuario en el mensaje y asigna valores predeterminados para cuando la propiedad de dirección no esté establecida.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Código completo de Liquid %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Casos de uso: Matrices

Supongamos que tienes un atributo personalizado de matriz llamado `upcoming_trips` que contiene viajes con las propiedades `destination` y `departure_date`. Quieres enviar a los usuarios mensajes personalizados en función de si tienen viajes programados.

1. Escribe una lógica condicional para especificar que un mensaje no debe enviarse si `upcoming_trips` es `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\. Especifica qué mensaje enviar si `upcoming_trips` tiene contenido:<br><br>**2a.** Dirígete al usuario e incluye un valor predeterminado, en caso de que no tengas su nombre. <br>**2b.** Utiliza una etiqueta `for` para especificar que extraerás propiedades (o información) de cada viaje que esté contenido en `upcoming_trips`. <br>**2c.** Enumera las propiedades del mensaje e incluye un valor predeterminado por si el `departure_date` no está configurado. (Digamos que se requiere un `destination` para que se cree un viaje, por lo que no necesitas establecer un valor predeterminado para ello).<br>**2d.** Cierra la etiqueta `for` y, a continuación, cierra la lógica condicional.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Código completo de Liquid %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
