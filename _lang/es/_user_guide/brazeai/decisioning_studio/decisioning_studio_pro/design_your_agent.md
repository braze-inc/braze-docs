---
nav_title: Diseña tu agente
article_title: Diseña tu agente
page_order: 3
description: "Aprende a diseñar tu agente Decisioning Studio Pro con el equipo de servicios de toma de decisiones basados en IA, incluyendo la definición de la audiencia, las métricas de éxito y las dimensiones."
---

# Diseña tu agente

> El primer paso para configurar tu agente es trabajar con nuestro equipo de Servicios de toma de decisiones con IA para diseñar tu agente. Este artículo trata sobre las decisiones clave de diseño y cómo definir tu audiencia.

Para conocer los conceptos básicos sobre los agentes de toma de decisiones, incluidas las métricas de éxito, las dimensiones, los bancos de acciones y las restricciones, consulta [Diseño de agentes de toma de decisiones]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Decisiones clave de diseño

En colaboración con el equipo de Servicios de toma de decisiones basadas en IA, tomarás las siguientes decisiones:

| Decisión | Descripción | Ejemplos |
|----------|-------------|----------|
| **Métrica de éxito** | ¿Qué maximizará el agente al realizar la personalización de la interacción con los clientes? | Ingresos, LTV, ARPU, conversiones, retención |
| **Audiencia** | ¿Para quién tomará decisiones sobre la interacción con los clientes el agente de Decisioning Studio? | Todos los clientes, miembros del programa de fidelización y suscriptores en riesgo. |
| **Grupos experimentales** | ¿Cómo deben estructurarse los ensayos controlados aleatorios de Decisioning Studio? | Estudio de toma de decisiones, control aleatorio, BAU, retención |
| **Dimensiones:** | ¿Qué decisiones debe personalizar el agente? | Hora del día, línea del asunto, frecuencia, ofertas, canal |
| **Opciones** | ¿Con qué opciones cuenta el agente para trabajar? | Plantillas específicas, ofertas, ventanas de tiempo |
| **Restricciones** | ¿Qué decisiones no debes tomar *nunca*? | Restricciones geográficas, límites presupuestarios, normas de elegibilidad. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cada una de estas decisiones tiene implicaciones en cuanto al aumento incremental que el agente puede generar y la rapidez con la que puede hacerlo. Nuestro equipo de servicios de toma de decisiones basados en inteligencia artificial trabajará contigo para diseñar un agente que genere el máximo valor respetando todas tus reglas de negocio.

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Definir tu audiencia

Las audiencias de casos de uso suelen definirse en una plataforma de interacción con los clientes (como Braze o Salesforce Marketing Cloud) y, a continuación, se envían al agente de Decisioning Studio. A continuación, el agente divide a los clientes en grupos de tratamiento con el fin de realizar ensayos controlados aleatorios.

### Grupos de tratamiento

| Grupo | Descripción |
|-------|-------------|
| **Estudio de toma de decisiones** | Clientes que reciben recomendaciones personalizadas por IA. |
| **Control aleatorio** | Clientes que reciben opciones seleccionadas al azar (comparación con la línea de base) |
| **Sin cambios (opcional)** | Clientes que reciben el recorrido de marketing actual (para compararlo con el rendimiento existente) |
| **Reserva (opcional)** | Clientes que no reciben comunicaciones (para medir el impacto global de la campaña) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configuración de tu audiencia

{% tabs %}
{% tab Braze %}

**Configura la audiencia en Braze:**

1. Crea un segmento para la audiencia a la que deseas dirigirte.
2. Proporciona el ID del segmento a tu equipo de servicios de toma de decisiones basados en inteligencia artificial.

{% alert note %}
En el caso de Braze, podemos incorporar múltiples segmentos y combinarlos para crear la audiencia. Decisioning Studio puede incorporar un segmento para una campaña comparativa de «negocio habitual». Todos estos patrones son aceptables.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configura la audiencia en Salesforce Marketing Cloud:**

1. Configura una o varias extensiones de datos SFMC para tu audiencia y proporciona el ID de la extensión de datos.
2. Configura el paquete instalado SFMC para la integración de la API con los permisos adecuados requeridos por Decisioning Studio.
3. Asegúrate de que esta extensión de datos se actualice diariamente, ya que Decisioning Studio extraerá los últimos datos incrementales disponibles.

Proporciona el ID de extensión y la clave de API al equipo de servicios de Braze. Te ayudarán con los siguientes pasos en la ingesta de datos de clientes.

{% endtab %}
{% tab Klaviyo %}

**Define la audiencia en Klaviyo:**

1. Crear un segmento de audiencia
2. Genera una clave de API privada y facilítala al equipo de Braze AI Decisioning.
3. Proporciona el ID del segmento y la clave de API al equipo de servicios de Braze.

Consulta la [documentación de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obtener más información sobre cómo seguir estos pasos.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Si la audiencia no está almacenada actualmente en Braze, SFMC o Klaviyo, el siguiente paso más adecuado es configurar una exportación de automatización directamente a un contenedor de Google Cloud Services controlado por Braze.

Para determinar si esto es factible, consulta la documentación de tu plataforma MarTech. Por ejemplo, mParticle ofrece una [integración nativa con Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Si este es el caso, podemos proporcionar un contenedor de GCS para exportar los datos de la audiencia.

Hay páginas similares para:
- [Segmento Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma Adobe Experience](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Funciones profesionales

Decisioning Studio Pro ofrece toda la potencia de la toma de decisiones basada en IA:

| Capacidad | Detalles |
|------------|---------|
| **Cualquier métrica de éxito** | Optimiza los ingresos, las conversiones, el ARPU, el LTV o cualquier KPI empresarial. |
| **Dimensiones ilimitadas** | Personaliza la oferta, el canal, el momento, la frecuencia, la creatividad y mucho más. |
| **Cualquier CEP** | Integraciones nativas con Braze, SFMC, Klaviyo + integraciones personalizadas para cualquier plataforma. |
| **Servicios de toma de decisiones basados en IA** | Asistencia dedicada del equipo de ciencia de datos de Braze. |
| **Diseño avanzado de experimentos** | Grupos de tratamiento y grupos de control totalmente personalizables |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Buenas prácticas

Algunas prácticas recomendadas para diseñar agentes de Decisioning Studio:

1. **Maximiza la riqueza de los datos**: Cuanta más información tengan los agentes sobre tus clientes, mejor será su rendimiento.
2. **Diversificar las acciones**: Cuanto más diverso sea el conjunto de acciones que el agente puede realizar, más podrá personalizar su estrategia para cada usuario.
3. **Minimizar las restricciones**: Cuantas menos restricciones tengan tus agentes, mejor. Las restricciones deben diseñarse de manera que respeten las reglas empresariales y, al mismo tiempo, permitan la mayor libertad posible para la experimentación dirigida por los agentes.

## Próximos pasos

Una vez tomadas las decisiones clave de diseño, podemos proceder al lanzamiento:

- [Inicia tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)