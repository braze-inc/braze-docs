---
nav_title: Operario
article_title: Operador BrazeAI
page_order: 0.7
alias: /operator/
description: "Este artículo de referencia trata sobre BrazeAI Operator, un asistente potenciado por IA integrado en el panel de Braze."
---

# Operador <sup>BrazeAITM</sup> 

> <sup>BrazeAITM</sup> Operator es un asistente basado en IA integrado en el panel de Braze. Operator te ayuda a encontrar respuestas, solucionar problemas y aprender las mejores prácticas sin abandonar tu flujo de trabajo.

{% alert important %}
El Operador <sup>BrazeAITM</sup> está actualmente en una beta privada con funcionalidad limitada. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Acerca del Operador

Operador es tu asistente de IA integrado en el panel de Braze. Te ayuda a avanzar más rápido respondiendo a tus preguntas, sugiriéndote los siguientes pasos y guiándote a través de las tareas, todo ello sin abandonar tu flujo de trabajo.

Durante la beta, Operador sólo admite el modo **Preguntar**. Puedes hacerlo:

- Obtén respuestas de la documentación de Braze
- Solución de problemas utilizando [el contexto consciente de la página](#page-aware-context)
- Aprende las mejores prácticas y orientaciones para la incorporación

## Cómo acceder a Operador

Puedes abrir Operador desde cualquier página del panel de Braze.  

1. Selecciona **Operador <sup>BrazeAITM</sup>**, junto a tu perfil de usuario.

\![El icono del Operador BrazeAI junto a un perfil de usuario.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"}
2\. Se abrirá el panel de chat del Operador en la parte derecha de la pantalla.

El panel de chat del Operador.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Prueba a maximizar para ampliar el panel y facilitar la lectura, o a minimizarlo para mantener disponible el Operador mientras sigues trabajando.  
{% endalert %}

## Cómo hablar con el Operador

Utiliza indicaciones para comunicarte con el Operador. Lo mejor es hablar con naturalidad, como lo harías con un compañero de trabajo o un amigo. Tus indicaciones pueden ir desde preguntas sencillas a peticiones complejas:

- **Sencillo:** ¿Cómo puedo asegurarme de que los usuarios no reciben correos electrónicos de abandono del carrito mientras todavía están en el sitio comprando?
- **Complejo:** ¿Cómo puedo hacer que la etiqueta `abort_message` de mi mensaje incluya el atributo del usuario que provocó el aborto?

El operador puede proporcionar instrucciones paso a paso, enlaces a documentos de Braze y explicaciones en lenguaje sencillo. Cuanto más clara y concreta sea tu pregunta, más útil será la respuesta. 

### Buenas prácticas

Piensa en la Operadora como en una conversación, no como en un motor de búsqueda. Los estímulos breves y naturales suelen funcionar mejor.

- **Sé concreto:** En lugar de "Háblame de Canvas", prueba con "¿Cómo utilizo las rutas de acción en Canvas?".  
- **Utiliza seguimientos:** Si la primera respuesta no es la que necesitas, haz preguntas aclaratorias. El operador puede afinar las respuestas.
- **Apóyate en el contexto:** El operador sabe en qué página estás en Braze. Abre Operator mientras estás en la página con la que estás trabajando para obtener los resultados más relevantes.

## Características

El operador incluye las siguientes características durante la versión beta:

### Contexto de página

El operador entiende la página en la que estás trabajando en Braze y puede adaptar las respuestas en función de ese contexto. Por ejemplo, si abres Operator mientras construyes un Canvas, puede sugerirte pasos o proporcionarte orientación relevante para Canvas, sin que tengas que explicarle dónde te encuentras. 

### Sugerencias

Cuando abras Operator, verás algunas sugerencias que te ayudarán a empezar. Selecciona una para empezar o escribe tu propia pregunta.

### Razonamiento visual

El Operador muestra sus pasos de razonamiento en secciones plegables etiquetadas como **Razonado**. Selecciona el desplegable para ampliar estas secciones y ver cómo el Operador llegó a una respuesta.

\![Desplegable para "Razonado" ampliado con más detalles sobre cómo respondió el Operador.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:60%"}

### Acciones sugeridas

En algunos casos, el Operador te recomendará los siguientes pasos y te proporcionará enlaces directos a las páginas pertinentes de tu panel Braze. Por ejemplo, si preguntas por las tasas de rebote del correo electrónico, Operator puede enlazarte a la página de tu **Centro de capacidad de entrega**. Estos atajos te ayudan a actuar más rápidamente sin necesidad de navegar manualmente.

### Detener la generación

Mientras el Operador está generando una respuesta, el botón **Enviar** se convierte en un botón **Detener**. Si quieres terminar la respuesta antes de tiempo, selecciona **Detener**.

### Borrar el historial de chat

Para restablecer tu conversación, selecciona **Borrar historial de chat**. Esto elimina el contenido actual para que puedas empezar de cero.

### Maximizar y minimizar el panel

Puedes utilizar el botón **de maximizar** para ampliar el Operador y facilitar su lectura, o **minimizarlo** para mantener el panel oculto mientras sigues trabajando en Braze.

### Enviar comentarios

En la parte inferior de cada respuesta, utiliza los botones de pulgar hacia arriba o pulgar hacia abajo para dar una respuesta rápida. Esto ayuda a mejorar las respuestas del Operador.

## Solución de problemas

| Edición | Solución de problemas |
| --- | --- |
| Sin respuesta | Prueba a actualizar la página y a volver a abrir el panel del Operador. |
| Respuestas fuera de tema | Reformula tu pregunta de forma más específica. Menciona la característica o el flujo de trabajo sobre el que preguntas. |
| Mensajes de error | Si Operator no puede transmitirte contenidos, es posible que aparezca el mensaje "Inténtalo de nuevo". Puede que el operador no esté disponible temporalmente o que se haya interrumpido tu conexión. Vuelve a intentarlo pasados unos minutos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

El Operador está diseñado para ayudarte a navegar por Braze y hacer el trabajo de forma más eficiente, pero hay algunos límites de corriente que debes tener en cuenta:

### Sin acceso a tus datos

Aunque Operator tiene acceso al contexto del trabajo que estás haciendo en Braze, Operator no puede consultar ni devolver respuestas sobre los datos de tu empresa almacenados en Braze. Por ejemplo, **no puede** responder a peticiones como:

- "Dame una lista de todas mis campañas de correo electrónico del año pasado".
- "Muéstrame qué segmentos tuvieron mayor interacción el último trimestre".
- "Analizar mi rendimiento en Canvas y sugerir mejoras".

### Estabilidad beta

Como beta privada, Operador puede tener errores ocasionales, interrupciones o características incompletas.

Si no estás seguro de si una pregunta es compatible, intenta formularla en términos de cómo Operator puede ayudarte a navegar o realizar acciones dentro del panel Braze, en lugar de recurrir a análisis o datos históricos.
