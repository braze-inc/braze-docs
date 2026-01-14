# Creación de agentes

> Aprende a crear un agente para BrazeAI Decisioning Studio™, para que puedas automatizar la experimentación personalizada y optimizar resultados como conversiones, retención o ingresos, sin pruebas A/B manuales.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Sobre los agentes

Un agente de toma de decisiones de IA es una configuración personalizada para el motor de toma de decisiones BrazeAI™, hecha a medida para cumplir un objetivo de negocio específico.

Por ejemplo, podrías crear un agente de repetición de compra para aumentar las conversiones de seguimiento tras una venta inicial. Tú defines la audiencia y el mensaje en Braze, mientras tus agentes decisores ejecutan experimentos diarios y prueban automáticamente distintas combinaciones de ofertas de productos, tiempo de envío de mensajes y frecuencia para cada cliente. Con el tiempo, BrazeAI™ aprende lo que funciona mejor y orquesta envíos personalizados a través de Braze para maximizar las tasas de recompra.

Para crear un buen agente, deberás hacer lo siguiente:

- Elegir una métrica de éxito para que BrazeAI™ la optimice, como ingresos, conversiones o ARPU.
- Definir qué dimensiones probar, como la oferta, la línea del asunto, la creatividad, el canal o la hora de envío.
- Seleccionar las opciones para cada dimensión, como correo electrónico frente a SMS, o frecuencia diaria frente a semanal.

![Ejemplo de diagrama de un agente de estudio de decisiones para correos electrónicos referidos.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Agentes de muestra

Aquí tienes algunos ejemplos de agentes que puedes construir con BrazeAI Decisioning Studio™. Tus agentes de decisión con IA aprenderán de cada interacción con el cliente y aplicarán esas informaciones a las acciones del día siguiente.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Construir un agente

### Requisitos previos

Antes de crear un agente, tendrás que [integrar BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration).

### Paso 1: Contacta con Servicios Expertos en IA

El equipo de Servicios Expertos en IA trabajará estrechamente contigo para determinar el alcance, diseñar y crear tu agente de toma de decisiones. Si aún no lo has hecho, ponte en [contacto](https://www.braze.com/get-started/) para empezar.

Completarán juntos los siguientes pasos para crear un agente personalizado adecuado para ti.

### Paso 2: Diseña tu agente

Junto con el equipo de Servicios Expertos en IA, definirás:

- una audiencia objetivo, 
- la métrica empresarial a optimizar, 
- las acciones para el agente decisor BrazeAI™, y 
- cualquier dato de clientes propio que el agente deba aprovechar para impulsar tus resultados empresariales. 

Con el diseño en la mano, el equipo trabajará contigo para identificar y completar cualquier requisito de integración adicional.

### Paso 3: Configura tu plataforma de entrega

A continuación, el equipo de Servicios Expertos en IA te ayudará a configurar tu plataforma de automatización del marketing. Aunque Decisioning Studio funciona mejor con Braze, es compatible con otras plataformas: ponte en contacto con tu equipo de Servicios Expertos en IA para obtener más recursos.

{% tabs local %}
{% tab Braze %}
Para configurar Braze:

1. Crea una [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) o [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ utilizará este método de entrega para enviar eventos de activación personalizados 1:1 a los usuarios de tu audiencia definida.
2. Asegúrate de no incluir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze, para que BrazeAI™ pueda ser el grupo de control dedicado en su lugar.
3. Dependiendo de tus dimensiones, puedes configurar etiquetas de Liquid en tu contenido creativo para rellenar dinámicamente tu mensajería con recomendaciones de BrazeAI™. BrazeAI™ pasará contenido específico del cliente a las etiquetas de Liquid de tus plantillas utilizando la API de Braze.
{% endtab %}
{% endtabs %}

### Paso 4: Iniciar y controlar

Después de poner en marcha tu agente, tu equipo de Servicios Expertos en IA continuará supervisándolo y ajustándolo al diseño acordado. También te ayudarán a hacer ajustes, ampliaciones o modificaciones en el agente, si es necesario.
