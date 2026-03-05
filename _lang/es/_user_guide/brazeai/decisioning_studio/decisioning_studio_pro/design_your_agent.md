---
nav_title: Diseña tu agente
article_title: Diseña tu agente
page_order: 3
description: "Aprende a diseñar tu agente de Decisioning Studio Pro con el equipo de servicios de Decisioning AI, incluyendo la definición de la audiencia, las métricas de éxito y las dimensiones."
---

# Diseña tu agente

> El primer paso de la configuración del agente es trabajar con nuestro equipo de Servicios de Decisión de IA para diseñar tu agente. Este artículo trata de las decisiones clave de diseño y de cómo definir tu audiencia.

Para conocer los conceptos básicos sobre los [agentes de decisión]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)-incluidas las métricas de éxito, las dimensiones, los bancos de acciones y las restricciones-, consulta [Diseñar agentes de decisión]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/).

## Decisiones clave de diseño

Trabajando con el equipo de Servicios de Decisión de IA, tomarás las siguientes decisiones:

| Decisión | Descripción | Ejemplos |
|----------|-------------|----------|
| **Métrica del éxito** | ¿Qué maximizará el agente al personalizar la interacción con los clientes? | Ingresos, LTV, ARPU, conversiones, retención |
| **Audiencia** | ¿Para quién tomará decisiones de interacción con los clientes el agente de Decisioning Studio? | Todos los clientes, miembros de fidelización, suscriptores de riesgo |
| **Grupos experimentales** | ¿Cómo deben estructurarse los ensayos controlados aleatorios de Decisioning Studio? | Estudio de decisión, Control aleatorio, BAU, Holdout |
| **Dimensiones:** | ¿Qué decisiones debe personalizar el agente? | Hora del día, línea del asunto, frecuencia, ofertas, canal |
| **Opciones** | ¿Qué opciones tiene el agente para trabajar? | Plantillas específicas, ofertas, ventanas de tiempo |
| **Restricciones** | ¿Qué decisiones *no* debe tomar *nunca* el agente? | Restricciones geográficas, límites presupuestarios, normas de elegibilidad |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cada una de estas decisiones tiene implicaciones sobre la cantidad de aumento que el agente puede ser capaz de generar, y con qué rapidez. Nuestro equipo de Servicios de Decisión de IA trabajará contigo para diseñar un agente que genere el máximo valor respetando todas tus normas empresariales.

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Definir tu audiencia

Las audiencias de los casos de uso suelen definirse en una plataforma de interacción con los clientes (como Braze o Salesforce Marketing Cloud), y luego se envían al agente de Decisioning Studio. A continuación, el agente divide a los clientes en grupos de tratamiento para realizar ensayos controlados aleatorios.

### Grupos de tratamiento

| Grupo | Descripción |
|-------|-------------|
| **Estudio de decisiones** | Clientes que reciben recomendaciones optimizadas por IA |
| **Control aleatorio** | Clientes que reciben opciones seleccionadas al azar (comparación de referencia) |
| **Business-as-Usual (opcional)** | Clientes que reciben el recorrido de marketing actual (para comparar con el rendimiento existente) |
| **Retención (opcional)** | Clientes que no reciben comunicaciones (para medir el impacto global de la campaña) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configurar tu audiencia

{% tabs %}
{% tab Braze %}

**Configura la audiencia en Braze:**

1. Crea un segmento para la audiencia a la que te gustaría dirigirte.
2. Proporciona el ID del segmento a tu equipo de servicios de toma de decisiones de IA.

{% alert note %}
En el caso de Braze, podemos ingerir varios segmentos y combinarlos para crear la audiencia. Decisioning Studio puede ingerir un segmento para una campaña de comparador Business-as-Usual. Todas estas pautas son aceptables.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configura la audiencia en Salesforce Marketing Cloud:**

1. Configura una(s) Extensión(es) de Datos SFMC para tu audiencia y proporciona el ID de la extensión de datos
2. Configura el paquete instalado de SFMC para la integración de la API con los permisos adecuados requeridos por Decisioning Studio
3. Asegúrate de que esta extensión de datos se actualiza diariamente, ya que Decisioning Studio tirará de los últimos datos incrementales disponibles

Proporciona el ID de extensión y la clave de API al equipo de servicios Braze. Ayudarán con los siguientes pasos en la ingesta de datos de clientes.

{% endtab %}
{% tab Klaviyo %}

**Define la audiencia en Klaviyo:**

1. Crear un segmento de audiencia
2. Genera una clave de API privada y proporciónala al equipo de Braze AI Decisioning
3. Proporciona el ID del segmento y la clave de API al equipo de servicios Braze

Consulta la [documentación de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obtener más información sobre cómo seguir estos pasos.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Si la audiencia no está almacenada actualmente en Braze, SFMC o Klaviyo, el siguiente mejor paso es configurar una exportación automatizada directamente a un contenedor de Google Cloud Services controlado por Braze.

Para determinar si esto es factible, consulta la documentación de tu plataforma MarTech. Por ejemplo, mParticle ofrece una [integración nativa con Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Si es así, podemos proporcionar un contenedor GCS al que exportar los datos de audiencia.

Hay páginas similares para:
- [Segmento Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma Adobe Experience](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Capacidades Pro

Decisioning Studio Pro ofrece toda la potencia de la toma de decisiones con IA:

| Capacidad | Detalles |
|------------|---------|
| **Cualquier métrica de éxito** | Optimiza para ingresos, conversiones, ARPU, LTV o cualquier KPI empresarial |
| **Dimensiones ilimitadas** | Personalización a través de la oferta, el canal, el momento, la frecuencia, la creatividad, etc. |
| **Cualquier CEP** | Integraciones nativas con Braze, SFMC, Klaviyo + integraciones personalizadas para cualquier plataforma |
| **Servicios de toma de decisiones AI** | Soporte dedicado del equipo de ciencia de datos de Braze |
| **Diseño avanzado de experimentos** | Grupos de tratamiento y retenciones totalmente personalizables |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Buenas prácticas

Algunas buenas prácticas para diseñar agentes de Decisioning Studio:

1. **Maximiza la riqueza de datos**: Cuanta más información tengan los agentes sobre tus clientes, mejor rendimiento obtendrán.
2. **Diversifica las acciones**: Cuanto más diverso sea el conjunto de acciones que puede realizar el agente, más podrá personalizar su estrategia para cada usuario.
3. **Minimiza las restricciones**: Cuantas menos limitaciones tengan tus agentes, mejor. Las restricciones deben diseñarse de forma que respeten las normas empresariales, al tiempo que liberan al máximo la experimentación dirigida por agentes.

## Próximos pasos

Una vez tomadas las decisiones clave sobre el diseño, podemos proceder al lanzamiento:

- [Lanza tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)