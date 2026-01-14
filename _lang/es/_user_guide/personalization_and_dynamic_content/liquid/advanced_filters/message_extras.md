---
nav_title: Etiqueta de extras para mensajes
article_title: Mensaje Etiqueta Extras
page_order: 1
description: "Este artículo explica cómo utilizar los extras de mensaje de la etiqueta de Liquid y cómo comprobar la sintaxis."
alias: "/message_extras_tag/"
---

# Extras de mensajes Etiqueta de Liquid

> Utiliza la etiqueta de Liquid `message_extras` para anotar tus eventos de envío con datos dinámicos de Contenido conectado, Catálogos, atributos personalizados (como idioma, país), propiedades de entrada en Canvas u otras fuentes de datos.

La etiqueta de Liquid `message_extras` añade pares clave-valor al evento de envío correspondiente en Compartir Datos de Currents y Snowflake. 

Para enviar datos dinámicos o adicionales a tu evento de envío de datos compartidos Currents o Snowflake, inserta la etiqueta de Liquid adecuada en el cuerpo de tu mensaje. 

Aquí tienes un ejemplo del formato estándar de etiqueta de Liquid para `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Puedes añadir estas etiquetas según necesites para tus pares clave-valor en el cuerpo del mensaje. Sin embargo, la longitud de todas las claves y valores no debe superar 1 KB. En Compartir Datos de Currents y Snowflake, verás un nuevo campo de evento llamado `message_extras` para tus eventos de envío. Esto generará una cadena JSON serializada en un campo.

## Canales admitidos

La etiqueta `message_extras` es compatible con todos los tipos de mensajes con un evento de envío, junto con los eventos de impresión de mensajes dentro de la aplicación. El uso de `message_extras` con mensajes dentro de la aplicación requiere que se cumplan ciertas [versiones mínimas del SDK](#iam-sdk).

## Cómo utilizar la etiqueta `message_extras` 

1. En el cuerpo del mensaje del canal, introduce la etiqueta de Liquid `message_extras`. O bien, puedes utilizar el modal **Añadir personalización** y seleccionar **Extras de mensajes** para el tipo de personalización. 

\![El modal Añadir personalización con la opción Extras de mensajes seleccionada como tipo de personalización.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Introduce el [par clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) de cada etiqueta `message_extras`. 

\![Un ejemplo de pares clave-valor para la etiqueta de extras del mensaje. El campo del título dice "Tus nuevos favoritos". El mensaje lee los pares clave-valor de la etiqueta de extras del mensaje y la frase siguiente: "Estamos encantados de ofrecerte una selección de productos frescos y emocionantes que seguro que se convertirán en tus nuevos favoritos".]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Una vez enviada tu campaña o Canvas, Braze adjuntará los datos dinámicos en el momento del envío a través de los eventos de envío de Compartir datos Currents o Snowflake al campo `message_extras`.

## Comprobar la sintaxis

Cualquier otra entrada que no se ajuste a la norma de etiquetas comentada anteriormente puede no pasar a Currents o Snowflake. Comprueba que tu sintaxis o formato no incluye nada de lo siguiente:

- Delimitadores inexistentes, vacíos o mal escritos
- Claves duplicadas (Braze enviará por defecto el par clave-valor que se encuentre primero)
- Texto extra antes de definir claves o valores
- Claves y valores desordenados 
  - {% raw %}Por ejemplo, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Envío de información sobre códigos promocionales a Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Consideraciones

- Si tus valores-clave superan 1 KB, los truncarán. 
- Los espacios en blanco contarán para el recuento de caracteres. Nota que Braze omite los espacios en blanco iniciales y finales.
- El JSON resultante sólo mostrará valores de cadena.
- Puedes incluir variables Liquid como clave o valor, pero no puedes utilizar otras etiquetas de Liquid dentro de `message_extras`.
  - Por ejemplo, podrías utilizar el siguiente Liquid: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Preguntas más frecuentes

#### ¿Cómo puedo asociar el campo message_extras de los eventos de envío a mis eventos de interacción, como aperturas y clics? 

En tus eventos de envío se genera y proporciona un `dispatch_id`, que puede utilizarse como identificador único para vincularlo a eventos específicos de clic, apertura o entrega. Podrás utilizar y consultar este campo en Currents o Snowflake. Más información sobre el [comportamiento`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### ¿Puedo utilizar message_extras con mensajes dentro de la aplicación? {#iam-sdk}

Sí, puedes utilizar `message_extras` en tus mensajes dentro de la aplicación siempre que los dispositivos de tus usuarios tengan las siguientes versiones mínimas del SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

