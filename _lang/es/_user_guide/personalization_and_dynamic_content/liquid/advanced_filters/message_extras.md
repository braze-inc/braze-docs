---
nav_title: Etiqueta de extras para mensajes
article_title: Etiqueta de extras para mensajes
page_order: 1
description: "Este artículo explica cómo utilizar la etiqueta Liquid de extras de mensajes y cómo comprobar la sintaxis."
alias: "/message_extras_tag/"
---

# Etiqueta Liquid de extras para mensajes

> Utiliza la etiqueta de Liquid `message_extras` para anotar tus eventos de envío con datos dinámicos de Contenido conectado, Catálogos, atributos personalizados (como idioma, país), propiedades de entrada en Canvas u otras fuentes de datos.

La etiqueta de Liquid `message_extras` añade pares clave-valor al evento de envío correspondiente en Intercambio de datos de Currents y Snowflake. 

Para enviar datos dinámicos o adicionales a su evento de envío de intercambio de datos Currents o Snowflake, inserte la etiqueta Liquid adecuada en el cuerpo del mensaje. 

Aquí tienes un ejemplo del formato estándar de etiqueta de Liquid para `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Puede añadir estas etiquetas según sea necesario para sus pares clave-valor en el cuerpo del mensaje. Sin embargo, la longitud de todas las claves y valores no debe superar 1 KB. En el Intercambio de datos de Currents y Snowflake, verás un nuevo campo de evento llamado `message_extras` para tus eventos de envío. Esto generará una cadena serializada JSON en un campo.

## Canales admitidos

La etiqueta `message_extras` es compatible con todos los tipos de mensajes con un evento de envío, así como con los eventos de impresión de mensajes dentro de la aplicación. El uso de `message_extras` con mensajes dentro de la aplicación requiere que se cumplan ciertas [versiones mínimas del SDK](#iam-sdk).

## Cómo utilizar la etiqueta `message_extras` 

1. En el cuerpo del mensaje del canal, introduce la etiqueta de Liquid `message_extras`. O bien, puede utilizar el modal **Añadir Personalización** y seleccionar **Extras de Mensaje** para el tipo de personalización. 

![El modal Añadir personalización con la opción Extras de mensajes seleccionada como tipo de personalización.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Introduzca el [par clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para cada etiqueta `message_extras`. 

![Un ejemplo de pares clave-valor para la etiqueta de extras del mensaje. El campo del título dice "Tus nuevos favoritos". El mensaje lee pares clave-valor para la etiqueta de extras del mensaje y la siguiente frase: "Estamos encantados de ofrecerte una selección de productos frescos y emocionantes que seguro que se convertirán en tus nuevos favoritos"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Una vez enviada su campaña o Canvas, Braze adjuntará los datos dinámicos en el momento del envío a través de los eventos de envío Currents o Snowflake Data Sharing al campo `message_extras`.

## Comprobación de la sintaxis

Cualquier otra entrada que no se ajuste a la norma de etiquetas comentada anteriormente puede no pasar a Currents o Snowflake. Compruebe que su sintaxis o formato no incluye ninguno de los siguientes elementos:

- Delimitadores inexistentes, vacíos o mal escritos
- Claves duplicadas (Braze enviará por defecto el par clave-valor que se encuentre en primer lugar)
- Texto extra antes de definir claves o valores
- Claves y valores desordenados 
  - {% raw %}Por ejemplo, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Consideraciones

- Si los valores clave superan 1 KB, se truncarán. 
- Los espacios en blanco contarán para el recuento de caracteres. Tenga en cuenta que Braze omite los espacios en blanco iniciales y finales.
- El JSON resultante sólo mostrará valores de cadena.
- Puedes incluir variables Liquid como clave o valor, pero no puedes utilizar otras etiquetas de Liquid dentro de `message_extras`.
  - Por ejemplo, podrías utilizar el siguiente Liquid: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Preguntas más frecuentes

#### ¿Cómo puedo asociar el campo message_extras de los eventos de envío a mis eventos de compromiso, como aperturas y clics? 

En los eventos de envío se genera y proporciona un `dispatch_id`, que puede utilizarse como identificador único para vincularlo a eventos específicos de clic, apertura o entrega. Podrás utilizar y consultar este campo en Currents o Snowflake. Más información sobre el [comportamiento en`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### ¿Puedo utilizar message_extras con mensajes in-app? {#iam-sdk}

Sí, puedes utilizar `message_extras` en tus mensajes in-app siempre que los dispositivos de tus usuarios tengan las siguientes versiones mínimas del SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

