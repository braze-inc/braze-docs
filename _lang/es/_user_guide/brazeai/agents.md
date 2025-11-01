---
nav_title: Agentes
article_title: Agentes de Braze
page_order: 0.5
description: "Los Agentes Braze pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas."
---

# Agentes de Braze

> Los Agentes Braze son ayudantes potenciados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas.

{% alert important %}
Los Agentes Braze están actualmente en fase beta. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## ¿Por qué utilizar Agentes Braze?

Los Agentes Braze ayudan a tu equipo a entregar experiencias más inteligentes y personalizadas, sin añadir trabajo extra. Actúan como asistentes inteligentes que no sólo responden a las indicaciones, sino que comprenden el contexto, toman decisiones y actúan para alcanzar un objetivo.

En la práctica, los agentes pueden crear automáticamente copias de mensajes -como líneas del asunto o texto en el producto- para que cada cliente reciba una comunicación personalizada. También pueden adaptarse en tiempo real, dirigiendo a las personas por diferentes rutas de Canvas en función de sus preferencias, comportamientos u otros datos.

Más allá de la mensajería, los agentes pueden enriquecer tus catálogos calculando o generando valores de campos de producto y perfil, manteniendo tus datos frescos y dinámicos. Al encargarse de tareas repetitivas o complejas, liberan a tu equipo para que se centre en la estrategia y la creatividad en lugar de en la configuración manual. Los Agentes Braze actúan más como colaboradores que como procesos en segundo plano, ayudándote a resolver problemas y a entregar resultados a gran escala.

## Características

Entre las características de los Agentes Braze se incluyen:

- **Configuración flexible:** Utiliza un LLM proporcionado por Braze o conecta tu propio proveedor de modelos (como OpenAI, Anthropic, Google Gemini o AWS Bedrock).
- **Integración perfecta:** Despliega agentes directamente en los pasos en Canvas o en los campos del catálogo.
- **Herramientas de prueba y registro:** Realiza una vista previa del resultado de tu agente probando con entradas de muestra antes de lanzarlo. Visualiza los registros de cada vez que se ejecuta el agente, incluyendo la entrada y la salida de esa ejecución.
- **Controles de uso:** Los límites de invocación y tamaño incorporados ayudan a gestionar el rendimiento y los costes.

## Acerca de Braze Agents

Los agentes se configuran con instrucciones (avisos del sistema) que definen cómo se comportan. Cuando un agente se ejecuta, utiliza tus instrucciones junto con los datos que le pasas para generar una respuesta. 

### Conceptos clave

| Plazo | Definición |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | El "cerebro" del agente, en este caso un gran modelo lingüístico (LLM). Interpreta las entradas, genera respuestas y realiza razonamientos. Un modelo más sólido (entrenado con más datos relevantes) hace que el agente sea más capaz y versátil. |
| [Instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Las normas o directrices que des al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Unas instrucciones claras hacen que el agente sea más fiable y predecible. |
| Contexto | Datos que se pasan al agente en tiempo de ejecución allí donde se despliega, como campos de perfil de usuario o filas de catálogo. Esta entrada proporciona la información que el agente utiliza para generar salidas. |
| [Variable de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | La salida que produce el agente cuando se utiliza en pasos en Canvas. Las variables de salida almacenan el resultado del agente para personalizar el contenido o guiar las rutas del flujo de trabajo. Las variables de salida pueden ser de tipo cadena, número o booleano.  |
| Invocación | Una única ejecución del agente. Esto cuenta para tus límites diarios y totales. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

Los agentes procesan las peticiones a unas 1.000 invocaciones por minuto. Cada espacio de trabajo puede admitir hasta 1.000 agentes. Si se alcanza este límite, tendrás que eliminar un agente existente antes de crear uno nuevo. 

Además, durante el periodo beta:

- La invocación está limitada a 50.000 ejecuciones diarias y 500.000 ejecuciones en total.
- Cada carrera debe completarse en 30 segundos. Transcurridos 30 segundos, el agente devolverá una respuesta nula cuando se utilice.
- Los datos de entrada están limitados a 10 KB por solicitud. Las entradas más largas se truncan.
- Para los catálogos, los campos agénticos sólo actualizan las 10.000 primeras filas.

## Próximos pasos

Ahora que conoces los Agentes Braze, estás preparado para los siguientes pasos:

- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Despliegue de agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
