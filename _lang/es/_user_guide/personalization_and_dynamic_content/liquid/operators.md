---
nav_title: Operadores
article_title: Operadores de Liquid
page_order: 2
description: "En esta página de referencia se anotan los operadores que admite Liquid, así como ejemplos relevantes."

---

# Operadores

> Liquid admite muchos [operadores][25] que pueden utilizarse en sus sentencias condicionales. Esta página cubre los operadores que admite Liquid y proporciona casos de uso de cómo puedes utilizarlos en tus mensajes.

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

## Ejemplos

He aquí algunos casos de uso de cómo estos operadores podrían ser útiles para tus campañas de marketing:

### Elegir mensaje con un atributo personalizado entero

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

En este caso de uso, si el atributo personalizado "Gasto total" de un cliente es superior a `0`, recibirá el mensaje:

```
Thanks for purchasing! Here's another 10% off!
```
Si el atributo personalizado "Gasto total" de un cliente no existe o es igual a `0`, recibirá el siguiente mensaje:

```
Buy now! Would 5% off convince you?
```

### Elige un mensaje con un atributo personalizado de cadena

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

En este caso de uso, si has jugado a un determinado juego, recibirás el siguiente mensaje:

```
You played our Game! We're so happy!
```

Si has jugado a otro juego especificado:

```
You played our other Game! Woop!
```

Si no has jugado a ningún juego, o ese atributo personalizado no existe en tu perfil, recibirás el siguiente mensaje:

```
Hey! Get in here and play this Game!
```

### Mensaje de cancelación basado en la ubicación

Puedes abortar un mensaje basándote en casi cualquier cosa. El siguiente ejemplo muestra cómo puede abortar un mensaje si un usuario no se encuentra en un área especificada, ya que podría no cumplir los requisitos para la promoción, espectáculo o entrega.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

También puede [abortar mensajes][1] basados en Contenido conectado.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
