---
nav_title: Utilizar Liquid
article_title: Caso de uso y resumen de Liquid
page_order: 0
description: "Este artículo de referencia ofrece una visión general de los casos de uso habituales de Liquid y de cómo incluir etiquetas Liquid en su mensajería."
search_rank: 2
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Utilización de líquido

> Este artículo mostrará cómo puedes utilizar diversos atributos de usuario para insertar dinámicamente información personal en tu mensajería.

Liquid es un lenguaje de plantillas de código abierto desarrollado por Shopify y escrito en Ruby. Puedes utilizarlo en Braze para introducir datos de perfil de usuario en tus mensajes y personalizar esos datos. Por ejemplo, puedes utilizar etiquetas de Liquid para crear mensajes condicionales, como enviar ofertas diferentes en función de la fecha de aniversario de la suscripción de un usuario. Además, los filtros pueden manipular datos, como formatear la fecha de registro de un usuario de una marca de tiempo a un formato más legible, como "15 de enero de 2022". Para más detalles sobre la sintaxis de Liquid y sus capacidades, consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Cómo funciona

Las etiquetas líquidas actúan como marcadores de posición en sus mensajes que pueden extraer información consentida de la cuenta de su usuario y permitir la personalización y las prácticas de mensajería relevantes.

En el siguiente bloque, se puede ver el doble uso de una etiqueta Liquid para llamar al nombre de pila del usuario, así como una etiqueta por defecto en caso de que un usuario no tuviera registrado su nombre de pila.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

A un usuario llamado Janet Doe, el mensaje le aparecería como

```
Hi Janet, thanks for using the App!
```

O...

```
Hi Valued User, thanks for using the App!
```

## Valores admitidos para sustituir

Los siguientes valores pueden sustituirse en un mensaje, en función de su disponibilidad:

- [Información básica del usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (por ejemplo, `first_name`, `last_name`, `email_address`)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [Propiedades personalizadas de los eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [Información sobre el dispositivo utilizado más recientemente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Información del dispositivo de destino]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

También puedes extraer contenido directamente de un servidor Web a través de [Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) Braze.

{% alert important %}
Actualmente, Braze es compatible con Liquid, incluido Liquid 5 de Shopify.
{% endalert %}

## Utilizar Liquid

Con [las etiquetas de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), puedes elevar la calidad de tus mensajes enriqueciéndolos con un toque personal. 

### Sintaxis líquida

Liquid sigue una estructura o sintaxis específica que deberá tener en cuenta a la hora de crear una personalización dinámica. Aquí tienes unas cuantas normas básicas que debes tener en cuenta:

1. **Utilice comillas rectas en Braze:** Existe una diferencia entre las comillas rizadas ('**')** y las rectas ('**')**. Utilice comillas rectas ('**')** en su Líquido en Braze. Es posible que vea comillas rizadas al copiar y pegar desde ciertos editores de texto, lo que puede causar problemas en su Liquid. Si introduces las cotizaciones directamente en el panel de control de Braze, todo irá bien.
2. **Los corchetes vienen en pares:** Cada corchete debe abrir y cerrar **{ }**. ¡Asegúrate de utilizar llaves!
3. **Las afirmaciones If vienen en pares:** Por cada `if`, se necesita un `endif` para indicar que la afirmación `if` ha terminado.

#### Atributos predeterminados y atributos personalizados

{% raw %}

Si incluye el siguiente texto en su mensaje: `{{${first_name}}}`, el nombre de pila del usuario (extraído de su perfil) será sustituido cuando se envíe el mensaje. Puedes utilizar el mismo formato con otros atributos predeterminados de usuario.

Si desea utilizar el valor de un atributo personalizado, debe añadir el espacio de nombres "custom_attribute" a la variable. Por ejemplo, para utilizar un atributo personalizado denominado "código postal", deberá incluir `{{custom_attribute.${zip code}}}` en su mensaje.

### Insertar etiquetas

Puedes insertar etiquetas escribiendo dos llaves abiertas `{{` en cualquier mensaje, lo que activará una función de autocompletado que se irá actualizando a medida que escribas. Incluso puede seleccionar una variable entre las opciones que aparecen a medida que escribe.

Si utilizas una etiqueta personalizada, puedes copiarla y pegarla en el mensaje que desees.

{% endraw %}

{% alert note %}

Si utilizas Liquid en tus mensajes de correo electrónico, asegúrate de:

1. Insértelo utilizando el editor HTML en lugar del editor clásico. El editor clásico puede parsear el Liquid como texto plano. Por ejemplo, Liquid parsearía como {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} en lugar de introducir como plantilla el nombre del usuario.
2. Coloque el código Liquid únicamente dentro de la etiqueta `<body>`. Colocarlo fuera de esta etiqueta puede provocar una representación incoherente en el momento de la entrega.

{% endalert %}

### Insertar variables preformateadas

Puedes insertar variables preformateadas con valores predeterminados a través del modal **Añadir personalización**, situado cerca de cualquier campo de texto de la plantilla.

![El modal Añadir personalización que aparece tras seleccionar insertar personalización. El modal tiene campos para el tipo de personalización, atributo, valor predeterminado opcional y muestra una vista previa de la sintaxis de Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

El modal insertará Liquid con el valor predeterminado que hayas especificado en el punto donde estaba el cursor. El punto de inserción también se especifica mediante el cuadro de vista previa, que tiene el texto anterior y posterior. Si se resalta un bloque de texto, se sustituirá el texto resaltado.

![Un GIF del modal Añadir personalización que muestra al usuario insertando "compañero de viaje" como valor predeterminado, y al modal sustituyendo el texto resaltado "nombre" en el compositor por el fragmento de código de Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### Asignación de variables

{% raw %}
Algunas operaciones en Liquid requieren que almacene el valor que desea manipular como una variable. Este suele ser el caso si su declaración Liquid incluye múltiples atributos, propiedades de eventos o filtros.

Por ejemplo, supongamos que desea sumar dos enteros de datos personalizados. 

#### Ejemplo de Liquid incorrecto

No puedes utilizar:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Este Liquid no funciona porque no puedes hacer referencia a varios atributos en una línea; tienes que asignar una variable al menos a uno de estos valores antes de que tengan lugar las funciones matemáticas. Añadir dos atributos personalizados requeriría dos líneas de Liquid: una para asignar el atributo personalizado a una variable y otra para realizar la adición.

#### Ejemplo correcto de Liquid

Puedes utilizar:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutorial: Utilización de variables para calcular un saldo

Calculemos el saldo actual de un usuario sumando el saldo de su tarjeta regalo y el saldo de recompensas:

En primer lugar, utilice la etiqueta `assign` para sustituir el atributo personalizado de `current_rewards_balance` por el término "balance". Esto significa que ahora tienes una variable llamada `balance`, que puedes manipular.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

A continuación, utilizaremos el filtro `plus` para combinar el saldo de la tarjeta regalo de cada usuario con su saldo de recompensas, indicado por `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
¿Te encuentras asignando las mismas variables en todos los mensajes? En lugar de escribir la etiqueta `assign` una y otra vez, puedes guardarla como Bloque de contenido y colocarla en la parte superior del mensaje.

1. [Crear un bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Asigne un nombre al bloque de contenido (sin espacios ni caracteres especiales).
3. Selecciona **Editar** en la parte inferior de la página.
4. Introduce tus etiquetas `assign`.

Mientras el bloque de contenido esté en la parte superior del mensaje, cada vez que la variable se inserte en el mensaje como un objeto, hará referencia al atributo personalizado que hayas elegido.
{% endalert %}

