---
nav_title: Lógica de mensajería condicional
article_title: Lógica de mensajería líquida condicional
page_order: 6
description: "Este artículo de referencia explica cómo pueden y deben utilizarse las etiquetas en sus campañas."

---

# Lógica de mensajería condicional

> [Etiquetas][7] te permiten incluir lógica de programación en tus campañas de mensajería. Las etiquetas pueden utilizarse para ejecutar sentencias condicionales, así como para casos de uso avanzados, como la asignación de variables o la iteración a través de un bloque de código. <br><br>En esta página se explica cómo pueden y deben utilizarse las etiquetas, por ejemplo, cómo tener en cuenta los valores de atributo nulo, nulo y vacío, y cómo hacer referencia a atributos personalizados.

## Etiquetas de formato

{% raw %}
Una etiqueta debe ir envuelta en `{% %}`.
{% endraw %}

{% alert tip %}
Para hacerte la vida un poco más fácil, Braze ha incluido un formateo por colores que se activará en verde y morado si has formateado correctamente tu sintaxis Liquid. El formato verde puede ayudar a identificar las etiquetas, mientras que el formato morado destaca las áreas que contienen personalización.
<br><br>
Si le resulta difícil utilizar la mensajería condicional, intente escribir la sintaxis condicional antes de insertar sus atributos personalizados y otros elementos Liquid.
<br><br>
Por ejemplo, añada primero lo siguiente en el campo de mensaje:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Asegúrese de que resalta en verde y, a continuación, sustituya el `X` por el Líquido o Contenido Conectado que haya elegido utilizando el `+` azul de la esquina del campo de mensaje, y el `0` por el valor que desee.
<br><br>
A continuación, añada las variaciones del mensaje que necesite entre las condiciones de `else`:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}
{% endalert %}

## Lógica condicional

Puedes incluir muchos tipos de [lógica inteligente dentro de los mensajes][1], como una declaración condicional. Mira el siguiente ejemplo que utiliza [condicionales][8] para internacionalizar una campaña:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Ejemplo paso a paso

En este ejemplo, utilizamos etiquetas con sentencias "if", "elsif" y "else" para entregar contenido internacionalizado.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
Si el idioma del usuario es el inglés, se cumple la primera condición y el usuario recibirá un mensaje en inglés.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Puede especificar tantas sentencias condicionales como desee. Las condiciones posteriores se comprobarán si no se cumplen las anteriores. En este ejemplo, si el dispositivo de un usuario no está configurado en inglés, este código comprobará si el dispositivo del usuario está configurado en español o chino. Si el dispositivo del usuario cumple una de estas condiciones, el usuario recibirá un mensaje en el idioma correspondiente.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who didn't match the other specified languages!
```

Tienes la opción de incluir una declaración `{% else %}` en tu lógica condicional. Si no se cumple ninguna de las condiciones establecidas, la sentencia `{% else %}` especifica el mensaje que debe enviarse. En este caso, predeterminamos el inglés si el idioma del usuario no es inglés, español o chino.

```liquid
{% endif %}
```

La etiqueta `{% endif %}` indica que has terminado tu lógica condicional. Debes incluir la etiqueta `{% endif %}` en cualquier mensaje con lógica condicional. Si no incluyes una etiqueta `{% endif %}` en tu lógica condicional, obtendrás un error, ya que Braze no podrá analizar tu mensaje.

{% endraw %}

## Contabilización de valores de atributos null, nil y blank

La lógica condicional es una forma útil de tener en cuenta los valores de atributos que no se establecen en los perfiles de usuario.

### Valores de atributo nulos y sin valor

Se produce un valor nulo o cero cuando no se ha establecido el valor de un atributo personalizado. Por ejemplo, un usuario que aún no haya configurado su nombre de pila no tendrá un nombre de pila registrado en Braze.

En algunas circunstancias, puede que desees enviar un mensaje completamente diferente a los usuarios que tienen un nombre de pila establecido y a los usuarios que no tienen un nombre de pila establecido.

La siguiente etiqueta permite especificar un mensaje para los usuarios con un atributo "nombre" nulo:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![Un mensaje de ejemplo en el panel de Braze, utilizando un atributo "nombre" nulo.][36]{: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Tenga en cuenta que un valor de atributo nulo no está estrictamente asociado a un tipo de valor (por ejemplo, una cadena "nula" es lo mismo que una matriz "nula"), por lo que en el ejemplo anterior, el valor de atributo nulo hace referencia a un nombre no establecido, que sería una cadena.

{% endraw %}

### Valores de atributo en blanco

Se produce un valor en blanco cuando el atributo de un perfil de usuario no está configurado, está configurado con una cadena de espacios en blanco (` `) o está configurado como `false`. Los valores en blanco deben comprobarse antes que otras variables para evitar un error de procesamiento de Liquid.

La siguiente etiqueta permite especificar un mensaje para los usuarios que tienen el atributo "nombre" en blanco.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Referencia a atributos personalizados

Una vez [creados los atributos personalizados][2], puede hacer referencia a estos atributos personalizados en su mensajería Liquid.

Cuando utilice lógica condicional, necesitará conocer el tipo de datos del atributo personalizado para asegurarse de que está utilizando la sintaxis correcta. En la página **Atributos personalizados** del cuadro de mandos, busque el tipo de datos asociado a su atributo personalizado y, a continuación, consulte los siguientes ejemplos enumerados para cada tipo de datos.

![Selección de un tipo de datos para un atributo personalizado. El ejemplo muestra un atributo Favorite_Category con un tipo de datos de cadena.][20]{: style="max-width:80%;"}

{% alert tip %}
Las cadenas y las matrices deben ir rodeadas de apóstrofos rectos, mientras que los booleanos y los enteros nunca llevan apóstrofos.
{% endalert %}

#### Booleano

[Los booleanos][9] son valores binarios, y pueden ajustarse a `true` o `false`, como `registration_complete: true`. Los valores booleanos no llevan apóstrofes.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Número

[Números][10] son valores numéricos, que pueden ser enteros o flotantes. Por ejemplo, un usuario puede tener `shoe_size: 10` o `levels_completed: 287`. Los valores numéricos no llevan apóstrofes.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

También puede utilizar otros [operadores básicos](https://shopify.dev/docs/themes/liquid/reference/basics/operators) como menor que (<) o mayor que (>) para números enteros:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### Cadena

Una [cadena][11] está formada por caracteres alfanuméricos y almacena un dato sobre su usuario. Por ejemplo, puede tener `favorite_color: red` o `phone_number: 3025981329`. Los valores de cadena deben ir rodeados de apóstrofes.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para las cadenas, puede utilizar tanto "==" como "contains" en su Liquid.

#### Matriz

Un [array][12] es una lista de información sobre su usuario. Por ejemplo, un usuario puede tener `last_viewed_shows: stranger things, planet earth, westworld`. Los valores de las matrices deben ir rodeados de apóstrofes.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para las matrices, debe utilizar "contains" y no puede utilizar "==". 

#### Tiempo

Una marca de tiempo de cuando un evento tuvo lugar. [Hora][13] valores deben tener un [filtro matemático][5] en ellos para ser utilizado en la lógica condicional.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Etiquetas de flujo de control"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
