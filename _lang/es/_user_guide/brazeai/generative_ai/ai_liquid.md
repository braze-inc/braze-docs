---
nav_title: Asistente Líquido BrazeAI
article_title: Asistente Líquido BrazeAI
description: "Este artículo explicará cómo funciona el Asistente AI Liquid y cómo puedes utilizarlo para generar fragmentos de código Liquid para tu mensajería."
page_type: reference
page_order: 5
---

# <sup>BrazeAITM</sup> Asistente líquido

> El Asistente Líquido <sup>BrazeAITM</sup> es un asistente de chat impulsado por <sup>BrazeAITM</sup> que te ayuda a generar el Líquido que necesitas para personalizar el contenido de los mensajes.

Con el Asistente para Líquidos <sup>BrazeAITM</sup>, puedes generar Líquidos a partir de plantillas, recibir sugerencias personalizadas de Líquidos y optimizar los Líquidos existentes con la ayuda de <sup>BrazeAITM</sup>. El asistente también proporciona anotaciones que explican el Liquid utilizado, para que puedas aumentar tu comprensión de Liquid y aprender a escribir el tuyo propio.

## Canales admitidos

Puedes utilizar el Asistente Líquido <sup>BrazeAITM</sup> al crear: 
- Mensajes SMS
- Notificaciones push
- Mensajes de correo electrónico HTML
    - El asistente funciona con mensajes de correo electrónico y no con plantillas, y funciona mejor con mensajes de correo electrónico ya creados.
- Canvas

## Cómo funciona

El Asistente para Liquid <sup>BrazeAITM</sup> está diseñado para ayudarte a escribir código Liquid eficaz y adaptado a tus necesidades de marketing. Formada tanto en la sintaxis de Liquid como en la forma en que los especialistas en marketing utilizan Liquid en sus mensajes, nuestra IA comprende los matices de la elaboración de contenidos personalizados. Además, al proporcionar al Asistente de Liquid BrazeAI<sup>TM</sup> tus nombres de atributos personalizados (como "color_favorito") y tipos de datos (como booleano y cadena), nuestro Asistente de Liquid BrazeAI<sup>TM</sup> garantiza que tus mensajes estén orientados con precisión y alineados con tus objetivos. Además, si creas Directrices de Marca, el Asistente Líquido <sup>BrazeAITM</sup> puede utilizar las Directrices de Marca para personalizar mejor los resultados generados y adaptar el contenido a nuestra propia voz de marca. Las directrices de marca que crees sólo se utilizarán para personalizar contenido para tu propio uso. 

## Generar código Liquid

Para iniciar el asistente <sup>BrazeAITM</sup> Liquid, selecciona el icono del asistente de IA en el creador de mensajes.

![Creador de mensajes con el asistente de IA.][1]{: style="max-width:50%;"}

Puedes elegir uno [de los que se te proporcionan](#provided-prompts) o introducir el tuyo propio en el cuadro de texto. Para generar tu código Liquid, selecciona **Actualizar compositor**.

![Ventana del asistente de IA con las indicaciones proporcionadas.][2]{: style="max-width:50%;"}
 
Puedes generar otro mensaje utilizando el mismo aviso seleccionando **Regenerar**. Para eliminar el mensaje y volver al anterior, selecciona **Deshacer actualización**.

### Indicaciones proporcionadas

Mientras utilizas el Asistente Líquido <sup>BrazeAITM</sup>, es posible que veas una serie de indicaciones que te ayudarán a empezar a utilizar Liquid. A continuación se enumeran algunas de ellas.

#### Utiliza la actividad de la aplicación

El aviso **Utilizar actividad de la aplicación** genera código Liquid para ayudarte a enviar mensajes diferentes en función de cuándo se utilizó tu aplicación por última vez. Es posible que te hagan preguntas de seguimiento para que el asistente pueda generar un resultado más preciso.

![Ejemplo de salida de la consulta "Utilizar actividad de aplicación".][3]{: style="max-width:45%;"}

#### Añadir cuenta atrás

Este aviso generará código Liquid que envía un mensaje con el tiempo que falta para que se produzca un evento. Te pedirá que proporciones detalles sobre la fecha y hora del evento.

![Ejemplo de salida de la consulta "Añadir cuenta atrás".][4]{: style="max-width:45%;"}

#### Inspírame

Este mensaje aparece cuando hay contenido en tu buzón de mensajes. Genera una lista de opciones que puedes elegir para personalizar tu mensaje con Liquid. 

![Ejemplo de salida de la consulta "Inspírame".][5]{: style="max-width:45%;"}

#### Mejorar mi Liquid

Este mensaje aparece cuando hay contenido en tu creador de mensajes. Selecciónala cuando quieras que el asistente haga tu código más eficaz y fácil de leer.

![Ejemplo de salida de la consulta "Mejorar mi Liquid".][6]{: style="max-width:45%;"}

## Atributos compatibles en beta

| Criterio Tipo de conocimiento
| - | - |
| Liquid (incluyendo `for` bucles, `if` declaraciones, matemáticas y otros) | Codificación |
| Atributos de usuario predeterminados y estándar | Atributos | Atributos
| Atributos personalizados que tengan cualquiera de estos tipos de datos: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Cadenas</li><li>Matrices</li><li>Tiempo</li></ul>{:/} | Atributos
| Contenido conectado | Codificación | Codificación
{: .reset-td-br-1 .reset-td-br-2 }

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para modificar o crear el contenido de tus mensajes, Braze enviará a la Plataforma API de OpenAI las indicaciones, el contenido de tus mensajes y/o las directrices de tu marca (si decides crearlas) enviados al asistente de IA <sup>BrazeAITM</sup>. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que incluyas información identificadora única en el contenido que proporciones. Como se detalla en [los compromisos de la plataforma API de Open](https://openai.com/policies/api-data-usage-policies)AI, los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Asegúrate de que cumples las políticas de OpenAI relevantes para ti, que pueden incluir sus [políticas de Uso](https://openai.com/policies/usage-policies) y su [política de Compartir y publicar](https://openai.com/policies/sharing-publication-policy). Braze no ofrece garantías de ningún tipo con respecto a cualquier contenido generado por IA.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
