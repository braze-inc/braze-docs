---
nav_title: Primeros pasos
article_title: Primeros pasos con BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Aprende a acceder y usar BrazeAI Operator<sup>TM</sup>, el asistente de IA de Braze integrado en el dashboard, incluidas sus funciones y mejores prácticas."
---

# Primeros pasos con BrazeAI Operator

> Aprende a acceder y usar BrazeAI Operator<sup>TM</sup>, tu asistente de IA integrado en el dashboard, incluidas sus funciones y mejores prácticas.

## Acceder a Operator

Abre Operator desde cualquier página del dashboard de Braze.

1. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario.

![El icono de BrazeAI Operator junto a un perfil de usuario.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. El panel de chat de Operator se abrirá en el lado derecho de la pantalla.

![El panel de chat de Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximiza el panel para leer mejor o minimízalo para mantener Operator disponible mientras trabajas.
{% endalert %}

## Usar Operator

Describe lo que intentas hacer en lenguaje natural. Las solicitudes pueden ir desde preguntas simples hasta solicitudes complejas:

- **Simple:** ¿Por qué no se renderiza mi Liquid?
- **Complejo:** ¿Cómo puedo hacer que la etiqueta `abort_message` de mi mensaje incluya el atributo de usuario que causó la cancelación?

Operator puede proporcionar instrucciones paso a paso, enlaces a la documentación de Braze y explicaciones en lenguaje claro. Las preguntas claras y específicas generan respuestas más útiles. Operator utiliza [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que ofrece un razonamiento sólido y es adecuado para tareas complejas de varios pasos.

## Mejores prácticas

Trata a Operator como una conversación, no como un motor de búsqueda. Las solicitudes breves y naturales funcionan mejor.

- **Sé específico:** En lugar de "Cuéntame sobre Canvas", prueba "¿Cómo uso las rutas de acción en Canvas?".
- **Haz preguntas de seguimiento:** Si la primera respuesta no cubre tu necesidad, pide aclaraciones o detalles adicionales.
- **Usa el contexto de la página:** Operator entiende tu ubicación en Braze. Abre Operator mientras ves la página relevante para obtener los resultados más precisos.

## Personalizar tu experiencia

### Aplicar directrices de marca

Añade las directrices de marca como contexto a las consultas de Operator para que las respuestas coincidan con la voz, el tono y la personalidad de tu marca. Operator utiliza las directrices de marca configuradas en tu espacio de trabajo, lo que ayuda a garantizar una mensajería coherente cuando sugiere texto o explica funciones.

Para configurar las directrices de marca, ve a **Configuración** > **Directrices de marca**. Para más información, consulta [Directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Selección de directrices de marca en el panel de chat de Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aprovechar el contexto de la página

Operator entiende automáticamente tu ubicación en Braze y adapta las respuestas en consecuencia. Por ejemplo, cuando abres Operator mientras creas un Canvas, puede sugerir pasos relevantes o ofrecer orientación sobre las funciones de Canvas sin que tengas que explicar en qué parte del flujo de trabajo estás.

Así puedes hacer preguntas más cortas y naturales como "¿Cómo añado un retraso?" en lugar de "¿Cómo añado un paso de retraso en un flujo de trabajo de Canvas?".

## Trabajar con las respuestas de Operator

### Empezar con las solicitudes sugeridas

Cuando abres Operator, aparecen solicitudes sugeridas según las tareas habituales y tu página actual. Selecciona una para empezar rápido o escribe tu propia pregunta.

### Entender cómo piensa Operator

Operator muestra sus pasos de razonamiento en secciones plegables etiquetadas **Reasoned**. Selecciona el desplegable para expandir estas secciones y ver cómo Operator determinó una respuesta.

![El desplegable "Reasoned" colapsado en una respuesta de Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Actuar con Operator

Operator puede proponer y ejecutar cambios directamente en el dashboard de Braze, como rellenar campos de formulario, actualizar configuraciones o generar contenido. Cada cambio propuesto se presenta como una tarjeta de acción para que la revises y apruebes antes de que surta efecto. Para más información, consulta [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gestionar tu sesión

### Detener una respuesta

Mientras Operator genera una respuesta, el botón **Enviar** pasa a ser **Detener**. Selecciona **Detener** para terminar la respuesta antes de tiempo si necesitas reformular tu pregunta o si la respuesta va en la dirección equivocada.

### Borrar el historial

Para empezar de cero o eliminar información sensible de la conversación, selecciona **Borrar historial del chat**. Esto elimina todo el contenido actual y restablece el contexto de la conversación.

### Enviar comentarios

En la parte inferior de cada respuesta, usa los botones de pulgar arriba o abajo para enviar comentarios rápidos. Tus comentarios ayudan a mejorar las respuestas de Operator con el tiempo.

## Próximos pasos

- [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) – Aprende a revisar y aprobar los cambios propuestos por Operator
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) – Problemas habituales y soluciones
