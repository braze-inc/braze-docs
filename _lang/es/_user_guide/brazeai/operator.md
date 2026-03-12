---
nav_title: Operador
article_title: Operador de BrazeAI
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprende a acceder y utilizar BrazeAI Operator<sup>TM</sup>, un asistente basado en inteligencia artificial integrado en el panel de Braze, incluidas sus características y mejores prácticas."
---

# Operador de BrazeAI

> BrazeAI Operator<sup>TM</sup> es un asistente basado en inteligencia artificial integrado en el panel. El operador ayuda a realizar tareas: responde preguntas, guía en la configuración, realiza la solución de problemas y aporta ideas.

## Operador de acceso

Abre Operator desde cualquier página del panel de Braze.  

1. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario.

![El icono de BrazeAI Operator junto al perfil de usuario.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2\. El panel de chat del operador se abre en la parte derecha de la pantalla.

![El panel de chat del operador.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximiza para ampliar el panel y facilitar la lectura, o minimiza para mantener el Operador disponible mientras trabajas.  
{% endalert %} 

## Utilizar operador

Describe lo que intentas lograr utilizando un lenguaje natural. Las indicaciones pueden variar desde preguntas sencillas hasta solicitudes complejas:

- **Simple:** ¿Por qué no se renderiza Liquid?
- **Complejo:** ¿Cómo puedo hacer que la`abort_message`etiqueta de tu mensaje incluya el atributo de usuario que provocó la interrupción?

El operador puede proporcionar instrucciones paso a paso, enlaces a la documentación de Braze y explicaciones en lenguaje sencillo. Las preguntas claras y específicas dan lugar a respuestas más útiles. El operador utiliza [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que ofrece un razonamiento sólido y es adecuado para tareas complejas de varios pasos. 

## Buenas prácticas

Trata al operador como una conversación, no como un motor de búsqueda. Las indicaciones breves y naturales son las que mejor funcionan.

- **Sé específico:** En lugar de «Cuéntame sobre Canvas», prueba con «¿Cómo utilizo las rutas de acción en Canvas?».  
- **Haz preguntas de seguimiento:** Si la primera respuesta no satisface tus necesidades, solicita aclaraciones o detalles adicionales.
- **Utiliza el contexto consciente de la página:** El operador conoce tu ubicación en Braze. Abre Operator mientras visualizas la página correspondiente para obtener resultados más precisos.

## Personaliza tu experiencia

### Aplicar las directrices de marca

Añade directrices de marca como contexto a las consultas del operador para que las respuestas coincidan con la voz, el tono y la personalidad de tu marca. El operador utiliza las directrices de marca configuradas en tu espacio de trabajo, lo que ayuda a garantizar la coherencia de la mensajería cuando sugiere textos o explica características.

Para configurar las directrices de marca, ve a **Configuración** > **Directrices de marca**. Para más información, consulta [las Directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Seleccionar las directrices de marca en el panel de chat del operador.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aprovecha el contexto consciente de la página

El operador comprende automáticamente tu ubicación en Braze y adapta las respuestas en función de ese contexto. Por ejemplo, cuando abres Operator mientras creas un Canvas, puede sugerirte pasos relevantes u ofrecerte orientación sobre las características del Canvas sin que tengas que explicar en qué punto del flujo de trabajo te encuentras.

Esta conciencia del contexto significa que puedes formular preguntas más cortas y naturales, como «¿Cómo añado un retraso?», en lugar de «¿Cómo añado un paso de retraso en un flujo de trabajo de Canvas?».

## Trabajar con las respuestas del operador

### Empieza con las sugerencias propuestas.

Al abrir Operator, aparecen sugerencias basadas en tareas comunes y en la página en la que te encuentras. Selecciona una para empezar rápidamente o escribe tu propia pregunta personalizada.

### Comprender cómo piensa el operador

El operador muestra sus pasos de razonamiento en secciones plegables etiquetadas como **«Razonado**». Selecciona el menú desplegable para ampliar estas secciones y ver cómo el operador determinó una respuesta. Esto resulta útil cuando quieres comprender la lógica que hay detrás de una sugerencia o verificar el enfoque.

![El menú desplegable «Razonado» colapsado en una respuesta del operador.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Actúa con el operador

El operador puede proponer y ejecutar cambios directamente en el panel de Braze, como rellenar campos de formularios, actualizar configuraciones o generar contenido. Cada cambio propuesto se presenta como una tarjeta de acción para que lo revises y apruebes antes de que entre en vigor. Para obtener más información sobre cómo funciona esto, consulta [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gestiona tu sesión

### Detener una respuesta

Mientras el operador genera una respuesta, el botón **Enviar** se convierte en un botón **Detener**. Selecciona **Detener** para finalizar la respuesta antes de tiempo si necesitas reformular tu pregunta o si la respuesta va por mal camino.

### Borrar tu historial

Para empezar de cero o eliminar información confidencial de la conversación, selecciona **Borrar historial de chat**. Esto elimina todo el contenido actual y restablece el contexto de la conversación.

### Enviar comentarios

En la parte inferior de cada respuesta, utiliza los botones de pulgar hacia arriba o pulgar hacia abajo para proporcionar comentarios rápidos. Tus comentarios ayudan a mejorar las respuestas del operador con el tiempo.

## Privacidad de datos y seguridad de los datos

### Cumplimiento de la HIPAA

AI Operator utiliza tecnología de conversación multiturno que actualmente no cumple con la política de retención cero de datos de OpenAI. AI Operator utiliza la política de retención de datos modificada de OpenAI para la supervisión de abusos, pero AI Operator no está cubierto por el acuerdo de socio comercial (BAA) entre Braze y OpenAI. Los usuarios no deben solicitar al operador de IA que acceda a la información médica protegida (PHI) almacenada en Braze ni enviar PHI a esta característica.

### Proveedores de modelos como subencargados del tratamiento o proveedores externos

Cuando utilizas una integración con un proveedor de LLM proporcionado por Braze a través de los Servicios de Braze («LLM proporcionado por Braze»), los proveedores de dicho LLM proporcionado por Braze actúan como subencargados del tratamiento de Braze, con sujeción a los términos del Anexo de tratamiento de datos (DPA) entre tú y Braze. BrazeAI Operator<sup>TM</sup> tiene integración con OpenAI.

### Cómo se utilizan los datos con OpenAI

Para generar resultados de IA a través de las características de BrazeAI que aprovechan OpenAI («Resultados»), Braze enviará cierta información («Datos de entrada») a OpenAI. La entrada consiste en tus indicaciones, el contenido que se muestra en el panel y los datos del espacio de trabajo relevantes para tus consultas. De acuerdo con [los compromisos de la plataforma API de OpenAI](https://openai.com/enterprise-privacy/), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar los modelos de OpenAI. Entre tú y Braze, Output es tu propiedad intelectual. Braze no reclamará ningún derecho de propiedad intelectual sobre dichos Resultados. Braze no ofrece garantía alguna con respecto a cualquier contenido generado por IA, incluido el Resultado.

## Próximos pasos

- [Revisión de acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Aprende a revisar y aprobar los cambios propuestos por el operador.
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Problemas comunes y soluciones de referencia
