---
nav_title: Código Liquid
article_title: Generar código Liquid con BrazeAI
description: "Este artículo explicará cómo funciona el Asistente AI Liquid y cómo puedes utilizarlo para generar fragmentos de código Liquid para tu mensajería."
page_type: reference
page_order: 0.0
---

# Generar código Liquid con <sup>BrazeAITM</sup>

> El Asistente Líquido <sup>BrazeAITM</sup> es un asistente de chat impulsado por <sup>BrazeAITM</sup> que te ayuda a generar el Líquido que necesitas para personalizar el contenido de los mensajes.

## Acerca del asistente <sup>BrazeAITM</sup> Liquid

El Asistente para Liquid <sup>BrazeAITM</sup> está diseñado para ayudarte a escribir código Liquid eficaz y adaptado a tus necesidades de marketing. Formada tanto en la sintaxis de Liquid como en la forma en que los especialistas en marketing utilizan Liquid en sus mensajes, nuestra IA comprende los matices de la elaboración de contenidos personalizados.

Además, al proporcionar al Asistente de Liquid BrazeAI<sup>TM</sup> tus nombres de atributos personalizados (como "color_favorito") y tipos de datos (como booleano y cadena), nuestro Asistente de Liquid BrazeAI<sup>TM</sup> garantiza que tus mensajes estén orientados con precisión y alineados con tus objetivos. Además, si creas Directrices de Marca, el Asistente Líquido <sup>BrazeAITM</sup> puede utilizar las Directrices de Marca para personalizar mejor los resultados generados y adaptar el contenido a nuestra propia voz de marca. Las directrices de marca que crees sólo se utilizarán para personalizar contenido para tu propio uso.

## Canales admitidos

Puedes utilizar el Asistente Líquido <sup>BrazeAITM</sup> al crear: 
- Mensajes SMS
- Notificaciones push
- Mensajes de correo electrónico HTML
- Canvas

{% alert note %}
El asistente funciona con mensajes de correo electrónico y no con plantillas. Funciona mejor con mensajes de correo electrónico ya creados.
{% endalert %}

## Generar código Liquid

Para iniciar el asistente <sup>BrazeAITM</sup> Liquid, selecciona el icono del asistente de IA en el creador de mensajes.

![Creador de mensajes con el asistente de inteligencia artificial.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Puedes elegir una de las indicaciones incluidas o introducir la tuya propia en el cuadro de texto.

{% tabs local %}
{% tab utilizar la actividad de la aplicación %}
El aviso **Utilizar actividad de la aplicación** genera código Liquid para ayudarte a enviar mensajes diferentes en función de cuándo se utilizó tu aplicación por última vez. Es posible que te hagan preguntas de seguimiento para que el asistente pueda generar un resultado más preciso.

![Ejemplo de salida de la consulta "Usar actividad de aplicación".]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab añadir cuenta atrás %}
Este aviso generará código Liquid que envía un mensaje con el tiempo que falta para que se produzca un evento. Te pedirá que proporciones detalles sobre la fecha y hora del evento.

![Ejemplo de salida de la consulta "Añadir cuenta atrás".]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspírame %}
Este mensaje aparece cuando hay contenido en tu buzón de mensajes. Genera una lista de opciones que puedes elegir para personalizar tu mensaje con Liquid. 

![Ejemplo de salida de la consulta "Inspírame".]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab mejorar mi Liquid %}
Este mensaje aparece cuando hay contenido en tu creador de mensajes. Selecciónala cuando quieras que el asistente haga tu código más eficaz y fácil de leer.

![Ejemplo de salida de la consulta "Mejorar mi Liquid".]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Para generar tu código Liquid, selecciona **Actualizar compositor**.

![Ventana del asistente de IA con indicaciones proporcionadas.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
Puedes generar otro mensaje utilizando el mismo aviso seleccionando **Regenerar**. Para eliminar el mensaje y volver al anterior, selecciona **Deshacer actualización**.

## Atributos líquidos {#supported-attributes}

Los siguientes atributos están actualmente en fase beta para el Asistente de Líquidos <sup>BrazeAITM</sup>:

| Criterio Tipo de conocimiento
| - | - |
| Liquid (incluyendo `for` bucles, `if` declaraciones, matemáticas y otros) | Codificación |
| Atributos de usuario predeterminados y estándar | Atributos | Atributos
| Atributos personalizados que tengan cualquiera de estos tipos de datos: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Cadenas</li><li>Matrices</li><li>Tiempo</li></ul>{:/} | Atributos
| Contenido conectado | Codificación | Codificación
{: .reset-td-br-1 .reset-td-br-2 }

## Buenas prácticas

Si necesitas ayuda para escribir instrucciones eficaces para el Asistente Líquido <sup>BrazeAITM</sup>, consulta nuestras mejores prácticas:

### Utiliza el lenguaje natural

El Asistente Líquido <sup>BrazeAITM</sup> está entrenado para entender el lenguaje natural. Habla con él como lo harías con un compañero de trabajo cuando le pides ayuda. Esto facilita que el asistente comprenda tus necesidades y te proporcione una asistencia precisa.

### Dar contexto

Proporcionar contexto ayuda al Asistente Líquido <sup>BrazeAITM</sup> a comprender el panorama general que rodea a tu proyecto. Es útil incluir contextos como:

- Nombre y sector de tu empresa
- Una campaña en la que estés trabajando, como el Black Friday o las rebajas navideñas
- Tu objetivo, como aumentar tu tasa de click-through
- Atributos personalizados específicos que quieres incluir en tu mensaje

Incluir el contexto en tu consulta ayuda al asistente a adaptar sus respuestas para que se ajusten mejor a tus necesidades. También puedes incluir detalles de tu campaña, un resumen del mensaje o un documento de lluvia de ideas para poner al día al asistente.

### Sé concreto

El Asistente Líquido <sup>BrazeAITM</sup> puede hacer preguntas de seguimiento, pero proporcionar detalles por adelantado puede conducir a resultados más precisos antes. Considera la posibilidad de incluir detalles como

- Cualquier preferencia o requisito conocido para el mensaje
- Instrucciones sobre cómo manejar situaciones, como la falta de respuestas del destinatario del mensaje o las opciones de mensajes alternativos.
- Cuando pidas Liquid que utiliza contenido conectado, documentación para el punto final de la API, una respuesta de muestra de la API, o ambas cosas

### Sé creativo

Piensa de forma innovadora con tus mensajes para ver cómo el Asistente Líquido <sup>BrazeAITM</sup> puede mejorar tu mensajería. Experimenta con diferentes ideas y estímulos, ya que la creatividad puede dar lugar a resultados más atractivos.

## Ejemplos de indicaciones

Aquí tienes algunos ejemplos que te ayudarán a empezar:

{% tabs local %}
{% tab adquirir conocimientos %}
- ¿Qué es Liquid y cómo puede ayudarme a mejorar la personalización de mis campañas de marketing en Braze?
- ¿Qué tipos de datos puedo utilizar en Liquid para personalizar mis mensajes de marketing, como información demográfica o compras anteriores?
{% endtab %}

{% tab personalización de contenidos dinámicos %}
- Crear un mensaje que muestre un contenido diferente en función del estado de fidelización de mi cliente. Si no conocemos su estado de fidelización, envía un mensaje de alternativa.
- Escribe un mensaje dinámico que incluya el producto favorito de un usuario y su última fecha de compra. Si no hay última compra, aborta el mensaje.
- Escríbeme Liquid para animar a alguien a hacer clic en mi mensaje que incluye una cuenta atrás con el tiempo que queda. Si la oferta ha caducado, aborta el mensaje.
- Ayúdame a escribir un mensaje para animar a los usuarios a volver y pasar por caja si les quedan artículos en la cesta.
- Escribe Liquid para personalizar un mensaje en función del país del cliente. Quiero rellenar el mensaje con el nombre del país. Si no tenemos ninguno de los dos, sugiéreles que hagan clic en un enlace para actualizar su perfil.
- ¿Cómo puedo personalizar un mensaje de bienvenida con el nombre de pila de un usuario y escribir un texto diferente en función del sexo del usuario?
- Escribe Liquid para mostrar diferentes mensajes en función de un atributo personalizado, "CUSTOM_ATTRIBUTE_NAME" y su valor. Hay seis opciones diferentes que podría enviar. Si no hay valor para el atributo personalizado, quiero enviar un mensaje de marcador de posición.
{% endtab %}

{% tab manejo de valores atípicos %}
- ¿Puedes darme algunos ejemplos de cómo se utiliza Liquid en campañas de marketing para aumentar las tasas de interacción y conversión?
- ¿Cuáles son algunos casos comunes de uso de Liquid en mensajes de texto para las rebajas de verano, como recordatorios de carrito abandonado o promociones personalizadas?
{% endtab %}
{% endtabs %}

{% alert tip %}
Haznos saber si tuviste alguna sugerencia o experiencia interesante reservando una [sesión de comentarios](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) con nosotros.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
