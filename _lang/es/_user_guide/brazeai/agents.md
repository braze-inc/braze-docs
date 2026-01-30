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

En la práctica, los agentes pueden crear automáticamente mensajes, como líneas del asunto o texto en el producto, para que cada cliente reciba una comunicación personalizada. También pueden adaptarse en tiempo real, dirigiendo a las personas por diferentes rutas de Canvas en función de sus preferencias, comportamientos u otros datos.

Más allá de la mensajería, los agentes pueden enriquecer tus catálogos calculando o generando valores de campos de producto y perfil, manteniendo tus datos frescos y dinámicos. Al encargarse de tareas repetitivas o complejas, liberan a tu equipo para que se centre en la estrategia y la creatividad en lugar de en la configuración manual. Los Agentes Braze actúan más como colaboradores que como procesos en segundo plano, ayudándote a resolver problemas y a entregar resultados a gran escala.

### Cuándo utilizar los Agentes Braze frente a otras características de BrazeAI

Utiliza agentes para personalizar el contenido sobre la marcha utilizando el contexto específico de un usuario. Por ejemplo, si un agente sabe que el sabor de helado favorito de un determinado usuario es el chocolate y su cobertura favorita son los ositos de gominola, puede crear una copia push específica de esa combinación para ese usuario a medida que pasa por el Canvas.

Sin embargo, el agente no aprende mediante el método de ensayo y error, y no tiene idea de un objetivo de marketing final que pretenda medir y maximizar. Aunque le digas que, en general, escriba copias que impulsen las conversiones, no tiene ningún mecanismo para "controlar" el impacto en la conversión de su escritura agéntica e integrar esos datos en futuras llamadas agénticas. Puedes pensar en esto como una toma de decisiones "vibrante", no como una toma de decisiones AI basada en recompensas.

En cambio, otras herramientas BrazeAI están diseñadas para maximizar las métricas que miden. Por ejemplo, los agentes son muy buenos evaluando cualitativamente cómo influyen las características de un usuario en su probabilidad o propensión a realizar un determinado evento o a que le guste un determinado producto. Sin embargo, como el agente no aprende mediante ensayo y error, no tiene ni idea de cómo medir su precisión en la predicción de probabilidades y en la mejora de la señal a lo largo del tiempo. Por ello, el uso de la Suite Predictiva supera al paso de Agente cuando se juzga por la precisión de sus predicciones y las mejoras a lo largo del tiempo.

## Características

Entre las características de los Agentes Braze se incluyen:

- **Configuración flexible:** Utiliza un LLM proporcionado por Braze o conecta tu propio proveedor de modelos (como OpenAI, Anthropic, Google Gemini o AWS Bedrock).
- **Integración perfecta:** Despliega agentes directamente en los pasos en Canvas o en los campos del catálogo.
- **Herramientas de prueba y registro:** Realiza una vista previa del resultado de tu agente probando con entradas de muestra antes de lanzarlo. Visualiza los registros de cada vez que se ejecuta el agente, incluyendo la entrada y la salida de esa ejecución.
- **Controles de uso:** Los límites diarios ayudan a gestionar el rendimiento y los costes.

## Acerca de Braze Agents

Los agentes se configuran con instrucciones (avisos del sistema) que definen cómo se comportan. Cuando un agente se ejecuta, utiliza tus instrucciones junto con los datos que le pasas para generar una respuesta. 

### Conceptos clave

| Plazo | Definición |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | El "cerebro" del agente, en este caso un gran modelo lingüístico (LLM). Interpreta las entradas, genera respuestas y realiza razonamientos. Un modelo más sólido (entrenado con más datos relevantes) hace que el agente sea más capaz y versátil. |
| [Instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | Las normas o directrices que des al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Unas instrucciones claras hacen que el agente sea más fiable y predecible. |
| Contexto | Datos que se pasan al agente en tiempo de ejecución allí donde se despliega, como campos de perfil de usuario o filas de catálogo. Esta entrada proporciona la información que el agente utiliza para generar salidas. |
| [Variable de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | La salida que produce el agente cuando se utiliza en pasos en Canvas. Las variables de salida almacenan el resultado del agente para personalizar el contenido o guiar las rutas del flujo de trabajo. Las variables de salida pueden ser de tipo cadena, número o booleano.  |
| [Ejecución](#limitations) | Una única ejecución del agente. Esto cuenta para tus límites diarios. |
| [Formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) | La estructura de datos predefinida de la respuesta del agente. |
| [Temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) | El nivel de desviación de la producción del agente. Esto define lo preciso o creativo que puede ser tu agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

Durante el periodo beta, se aplican las siguientes limitaciones:

- Cada agente tiene un límite predeterminado de ejecución diaria de 50.000 ejecuciones, que puede aumentarse hasta un máximo de 100.000 ejecuciones al día.
- Por defecto, cada ejecución debe completarse en 15 segundos. Transcurridos 15 segundos, el agente devuelve una respuesta `null` en la que se utiliza. 
    - Si a tus agentes se les acaba el tiempo de espera constantemente, ponte en contacto con tu director de cuentas Braze para aumentar este límite.
- Los datos de entrada están limitados a 25 KB por petición. Las entradas más largas se truncan.

## Próximos pasos

Ahora que conoces los Agentes Braze, estás preparado para los siguientes pasos:

- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Despliega agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

## Proveedores modelo como subprocesadores o proveedores terceros

Cuando el Cliente utilice una integración con modelos proporcionados por Braze a través de los Servicios Braze ("LLM proporcionados por Braze"), los proveedores de dichos LLM proporcionados por Braze estarán actuando como Subprocesadores de Braze, sujetos a los términos del Anexo de Procesamiento de Datos (DPA) entre el Cliente y Braze. 

Si el Cliente opta por aportar su propia clave de API para integrarse con la funcionalidad de Braze AI, el proveedor de la propia suscripción LLM del Cliente se considerará un Tercero Proveedor, tal y como se define en el contrato entre el Cliente y Braze. 

### ¿Cómo se utilizan mis datos y se envían a los LLM proporcionados por Braze?

Para generar resultados de IA a través de las características de IA de Braze que Braze identifique como aprovechando los LLM proporcionados por Braze ("Resultados"), Braze enviará la indicación de tu sistema o cualquier otra entrada, según corresponda ("Entrada") al LLM proporcionado por Braze. Los datos enviados al LLM aplicable proporcionado por Braze no se utilizan para entrenar o mejorar el LLM proporcionado por Braze. Entre tú y Braze, la Salida es tu propiedad intelectual. Braze no hará valer ninguna reclamación de propiedad de derechos de autor sobre dicha Salida. Braze no ofrece garantías de ningún tipo con respecto a ningún contenido generado por IA en general, incluida la Salida.

El LLM proporcionado por Braze para los agentes de Braze, identificado como "Auto", utiliza modelos de Google Gemini. Google conserva las Entradas y Salidas enviadas a través de Braze durante 55 días, tras los cuales se eliminan los datos.
