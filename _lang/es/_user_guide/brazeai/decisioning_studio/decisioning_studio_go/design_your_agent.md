---
nav_title: Diseña tu agente
article_title: Diseña tu agente
page_order: 3
description: "Aprende a diseñar un agente BrazeAI Decisioning Studio Go, incluyendo la definición de la audiencia, las dimensiones y las limitaciones específicas de Go."
---

# Diseña tu agente

> Este artículo explica cómo diseñar tu agente Go de Decisioning Studio, incluyendo la definición de tu audiencia, la selección de dimensiones y la comprensión de las capacidades y limitaciones específicas de Go.

Para conocer los conceptos básicos sobre los [agentes de decisión]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)-incluidas las métricas de éxito, las dimensiones, los bancos de acciones y las restricciones-, consulta [Diseñar agentes de decisión]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Capacidades Go versus Pro

Decisioning Studio Go es una plataforma de autoservicio con funciones simplificadas en comparación con Decisioning Studio Pro. Comprender estas diferencias te ayuda a diseñar un agente eficaz dentro del ámbito de Go.

| Capacidad | Estudio de decisión Go | Estudio de decisiones Pro |
|-----------|----------------------|------------------------|
| **Métrica del éxito** | Sólo clics | Cualquier métrica empresarial (ingresos, conversiones o ARPU) |
| **Dimensiones:** | Banco de acción limitada | Dimensiones ilimitadas |
| **PEC apoyados** | Braze, SFMC, Klaviyo | Cualquier CEP (nativo y personalizado) |
| **Datos del cliente** | Sólo interacción | Todos los datos 1P |
| **Configurar** | Autoservicio | Apoyo a los servicios de toma de decisiones AI |
| **Grupos experimentales** | Ir + Control aleatorio + BAU opcional | Totalmente personalizable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Diseñar tu agente Go

Al diseñar un agente de Decisioning Studio Go, tomarás decisiones en las siguientes áreas:

### Paso 1: Define tu audiencia

Tu audiencia es el conjunto de clientes con los que se relacionará el agente. En Go, las audiencias se definen en tu CEP:

{% tabs %}
{% tab Braze %}

**Definir la audiencia en Braze:**

1. Crea un segmento en Braze que defina los clientes a los que quieres que se dirija el agente.
2. Cuando configures tu experimentador en el portal Decisioning Studio Go, selecciona este segmento como tu audiencia objetivo.

{% alert tip %}
Considera la posibilidad de crear un segmento dedicado a tu experimentador de Decisioning Studio Go para mantener tus pruebas aisladas y medibles.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definir la audiencia en SFMC:**

1. Configura una Extensión de Datos que contenga tu audiencia objetivo.
2. Asegúrate de que esta Extensión de datos se actualiza diariamente con los datos de clientes más recientes.
3. Haz referencia a esta Extensión de Datos en el portal Decisioning Studio Go cuando configures tu experimentador.

{% endtab %}
{% tab Klaviyo %}

**Definir la audiencia en Klaviyo:**

1. Crea un segmento en Klaviyo que defina tu audiencia objetivo.
2. Cuando configures tu experimentador en el portal Decisioning Studio Go, selecciona este segmento.

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tus dimensiones

Las dimensiones son las "palancas" de las que puede tirar el agente para personalizar la experiencia del cliente. Incluyen dimensiones creativas como la línea del asunto y la imagen principal, así como dimensiones de tipo de envío como la frecuencia de los correos electrónicos o la hora del día. 

{% alert note %}
Las dimensiones específicas disponibles dependen de tu CEP y de cómo estén configuradas tus campañas. Trabaja con las plantillas y el contenido que hayas configurado en tu CEP.
{% endalert %}

### Paso 3: Configura tu banco de acciones

El banco de acciones define las opciones concretas que el agente puede elegir para cada dimensión. Por ejemplo:

- **Plantillas de correo electrónico**: Selecciona qué plantillas puede utilizar el agente (primero deben estar configuradas en tu CEP)
- **Línea del asunto**: Define las variantes de línea del asunto que el agente puede probar
- **Enviar horas**: Especifica las ventanas de tiempo que el agente puede elegir

### Paso 4: Configurar grupos de experimentación

Decisioning Studio Go crea automáticamente grupos de experimentos para medir el rendimiento:

| Grupo | Descripción |
|-------|-------------|
| **Estudio de decisión Go** | Clientes que reciben recomendaciones optimizadas por IA |
| **Control aleatorio** | Clientes que reciben opciones seleccionadas al azar (comparación de referencia) |
| **Como siempre (opcional)** | Clientes que reciben tu campaña actual (si se compara con el rendimiento actual) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Para que la comparación sea exacta, asegúrate de que ningún cliente pueda pertenecer a más de un grupo del experimento, y de que los clientes se asignen aleatoriamente a los grupos sin sesgos.
{% endalert %}

## Limitaciones a tener en cuenta

Cuando diseñes tu agente Go, ten en cuenta estas limitaciones:

- **Sólo clics**: Go optimiza las tasas de click-through. Si necesitas optimizar los ingresos, las conversiones u otras métricas empresariales, considera Decisioning Studio Pro.
- **Dimensiones limitadas**: Go admite un conjunto predefinido de dimensiones. Para dimensiones personalizadas o personalizaciones complejas, considera Decisioning Studio Pro.
- **Tres CEPs**: Go sólo se integra con Braze, Salesforce Marketing Cloud y Klaviyo. Para otras plataformas, considera Decisioning Studio Pro.

## Buenas prácticas

- **Empieza de forma sencilla**: Empieza con 2-3 plantillas o variantes de línea del asunto. Esto da al agente suficientes opciones para aprender, a la vez que mantiene el experimento manejable.
- **Dale tiempo**: El agente necesita datos suficientes para aprender. Deja pasar al menos 2-4 semanas antes de sacar conclusiones sobre el rendimiento.
- **Haz que el contenido sea variado**: Asegúrate de que tus opciones son significativamente diferentes. Probar variaciones menores puede no aportar información significativa.
- **Vigila regularmente**: Consulta el portal Decisioning Studio Go para controlar el progreso del experimento y las métricas de interacción.

## Próximos pasos

Una vez que hayas diseñado tu agente y lo hayas configurado en el portal Decisioning Studio Go, estarás listo para lanzarlo:

- [Lanza tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
