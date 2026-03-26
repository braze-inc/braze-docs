---
nav_title: Consola de agentes
article_title: Agentes de Braze
page_order: 1
description: "Los agentes de Braze pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas."
---

# Agentes de Braze en la consola de agentes

> Los agentes de Braze son asistentes basados en inteligencia artificial que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas.

{% alert important %}
Se necesitan créditos de mensajes para acceder y utilizar Braze Agents. Si actualmente no tienes créditos de mensajes y deseas utilizar Braze Agents, ponte en contacto con tu director de cuentas para conocer los pasos a seguir.
{% endalert %}

## ¿Por qué utilizar Braze Agents?

Los agentes de Braze ayudan a tu equipo a entregar experiencias más inteligentes y de personalización, sin añadir trabajo adicional. Actúan como agentes autónomos que no solo responden a indicaciones, sino que comprenden el contexto, toman decisiones y actúan para alcanzar un objetivo.

En la práctica, los agentes pueden crear automáticamente copias de mensajes, como líneas del asunto o texto dentro del producto, para que cada cliente reciba una comunicación que parezca personalizada. También pueden adaptarse en tiempo real, dirigiendo a las personas por diferentes rutas de Canvas en función de sus preferencias, comportamientos u otros datos.

Más allá de la mensajería, los agentes pueden enriquecer tus catálogos calculando o generando valores de campos de productos y perfiles, lo que mantiene tus datos actualizados y dinámicos. Al encargarse de tareas repetitivas o complejas, liberan a tu equipo para que pueda centrarse en la estrategia y la creatividad, en lugar de en la configuración manual. Los agentes de Braze actúan más como colaboradores que como procesos en segundo plano, ayudándote a resolver problemas y a entregar un impacto a gran escala.

### Cuándo utilizar Braze Agents frente a otras características de BrazeAI

Utiliza agentes para realizar la personalización del contenido sobre la marcha utilizando el contexto específico del usuario. Por ejemplo, si un agente sabe que el sabor de helado favorito de un usuario en particular es el chocolate y que su ingrediente favorito son las gominolas, puede crear un mensaje específico para esa combinación para ese usuario cuando pase por el Canvas.

Sin embargo, el agente no aprende mediante ensayo y error, y no tiene ni idea del objetivo de marketing final que busca medir y maximizar. Aunque le indiques que, en general, redacte textos que impulsen las conversiones, no dispone de ningún mecanismo para «supervisar» el impacto de sus textos en las conversiones e integrar esos datos en futuras llamadas. Puedes pensar en esto como una toma de decisiones basada en «vibraciones», no en una toma de decisiones basada en recompensas por parte de la IA.

Por el contrario, otras herramientas de BrazeAI están diseñadas para maximizar las métricas que miden. Por ejemplo, los agentes son muy buenos a la hora de evaluar cualitativamente cómo las características de un usuario influyen en tu probabilidad o propensión a realizar una determinada acción o a gustarte un determinado producto. Sin embargo, dado que el agente no aprende mediante ensayo y error, no tiene ni idea de cómo medir su precisión a la hora de realizar predicciones de probabilidades y mejorar la señal con el tiempo. Por lo tanto, el uso de Predictive Suite supera al paso del agente cuando se evalúa la precisión de sus predicciones y las mejoras a lo largo del tiempo.

## Características

Las características para los agentes de Braze incluyen:

- **Configuración flexible:** Utiliza un LLM proporcionado por Braze o conecta tus propios [proveedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers) (como OpenAI, Anthropic o Google Gemini).
- **Integración fácil:** Implementa agentes directamente en los pasos en Canvas o en los campos del catálogo.
- **Herramientas de prueba y registro:** Realiza una vista previa del resultado de tu agente probando con entradas de muestra antes de lanzarlo. Ver los registros de cada vez que se ejecuta el agente, incluyendo la entrada y salida de esa ejecución.
- **Controles de uso:** Los límites diarios ayudan a administrar el rendimiento y los costes.

## Acerca de los agentes de Braze

Los agentes se configuran con instrucciones (indicaciones del sistema) que definen cómo deben comportarse. Cuando un agente se ejecuta, utiliza tus instrucciones junto con los datos que le pasas para generar una respuesta.

### Conceptos clave

| Plazo | Definición |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | El «cerebro» del agente, en este caso un modelo de lenguaje grande (LLM). Interpreta las entradas, genera respuestas y realiza razonamientos. Un modelo más sólido (entrenado con datos más relevantes) hace que el agente sea más capaz y versátil. |
| [Instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | Las reglas o directrices que le das al agente (solicitud del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones claras hacen que el agente sea más fiable y predecible. |
| Contexto | Datos que se transmiten al agente en tiempo de ejecución, independientemente de dónde se implemente, como campos de perfil de usuario o filas de catálogo. Esta entrada proporciona la información que tú utilizas para generar salidas. |
| [Variable de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#define-the-output-variable) | El resultado que produce el agente cuando se utiliza en los pasos en Canvas. Las variables de salida almacenan el resultado del agente para realizar la personalización del contenido o guiar las rutas del flujo de trabajo. Las variables de salida pueden ser una cadena, un número o un tipo de datos booleano.  |
| [Ejecución](#limitations) | Una sola ejecución del agente. Esto cuenta para tus límites diarios. |
| [Formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | La estructura de datos predefinida de la respuesta del agente. |
| [Temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) | El nivel de desviación del rendimiento del agente. Esto define el grado de precisión o creatividad que puede alcanzar tu agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

Se aplican las siguientes limitaciones:

- Cada agente tiene un límite de ejecución diario predeterminado de 250 000 ejecuciones, que se puede aumentar hasta un máximo de 1 000 000 de ejecuciones por día. Si estás interesado en aumentar este límite, ponte en contacto con tu administrador del éxito del cliente.
- Predeterminadamente, cada ejecución debe completarse en un plazo de 15 segundos. Después de 15 segundos, el agente devuelve una`null`respuesta donde se utiliza.
    - Si tus agentes agotan constantemente el tiempo de espera, ponte en contacto con tu director de cuentas de Braze para aumentar este límite.
- Los datos de entrada están limitados a 25 KB por solicitud. Las entradas más largas se truncan.

## ¿Cómo se utilizan tus datos y cómo se envían a los LLM proporcionados por Braze?

Con el fin de generar resultados de IA a través de las características de IA de Braze que Braze identifica como aprovechar los LLM proporcionados por Braze («Resultados»), Braze enviará tu solicitud al sistema o cualquier otra entrada, según corresponda («Entrada»), al LLM proporcionado por Braze. Los datos enviados al LLM proporcionado por Braze no se utilizan para entrenar o mejorar el LLM proporcionado por Braze. Entre tú y Braze, Output es tu propiedad intelectual. Braze no reclamará ningún derecho de propiedad intelectual sobre dichos Resultados. Braze no ofrece garantía alguna con respecto a cualquier contenido generado por IA en general, incluido el Resultado.

El LLM proporcionado por Braze para Braze Agents, con el identificador «Auto», utiliza modelos Google Gemini. Google conserva las entradas y salidas enviadas a través de Braze durante 55 días, tras los cuales los datos se eliminan.

## Próximos pasos

Ahora que ya conoces Braze Agents, estás listo para los siguientes pasos:

- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Implementar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
