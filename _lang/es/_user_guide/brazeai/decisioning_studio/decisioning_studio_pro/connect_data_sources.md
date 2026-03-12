---
nav_title: Conectar orígenes de datos
article_title: Conectar orígenes de datos
page_order: 1
description: "Aprende a conectar orígenes de datos de clientes a BrazeAI Decisioning Studio Pro para tomar decisiones personalizadas basadas en inteligencia artificial."
---

# Conectar orígenes de datos

> Los agentes de BrazeAI Decisioning Studio™ Pro deben comprender plenamente el contexto del cliente para poder tomar decisiones eficaces. Este artículo explica cómo conectar orígenes de datos de clientes a Decisioning Studio Pro.

{% alert tip %}
Tu equipo de servicios de toma de decisiones basadas en IA te ayudará a configurar las conexiones de datos para obtener un rendimiento óptimo.
{% endalert %}

## Patrones de integración compatibles

Decisioning Studio Pro admite múltiples patrones de integración para conectar los datos de clientes:

| Patrón de integración | Ideal para | Complejidad de la configuración |
|---------------------|----------|------------------|
| **Plataforma de datos Braze** | Clientes que ya utilizan Braze | Baja |
| **Ingesta de datos en la nube (CDI) de Braze** | Conexión de almacénes de datos externos | Media |
| **Almacenamiento en la nube (GCS, AWS, Azure)** | Exportación directa de datos desde otras plataformas | Media |
| **Integraciones CEP** | SFMC, extensiones de datos de Klaviyo | Media |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Tipos de datos de clientes

Los siguientes activos de datos de clientes ayudan a los agentes a realizar la personalización de forma más eficaz:

| Tipo de datos | Descripción | Ejemplos |
|-----------|-------------|----------|
| **Perfil del cliente** | Atributos estáticos y que cambian lentamente | Años como cliente, ubicación geográfica, canal de adquisición, nivel de satisfacción, estimación del valor de duración del ciclo de vida. |
| **Comportamiento del cliente** | Patrones de actividad y interacción | Inicios de sesión en la cuenta, tipo de dispositivo, interacciones con el servicio de atención al cliente, uso del producto. |
| **Historial de transacciones de transacciones** | Datos de compra y conversión | Productos adquiridos, importes de las transacciones, métodos de pago, canales de compra. |
| **Interacción con el marketing** | Respuestas a las comunicaciones | Aperturas/clics de correos electrónicos, interacción con SMS, actividad web y móvil, respuestas a cuestionarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Cuanta más información tengan los agentes sobre tus clientes, mejor será su rendimiento. Considera la posibilidad de incluir datos sobre cualquier información que sea especialmente importante para tu negocio (por ejemplo, ¿quieres ver cómo la IA trata de forma diferente a tus clientes de fidelización? Asegúrate de que el estado de fidelización figure en los datos de clientes.
{% endalert %}

## Conectando datos por plataforma

{% tabs %}
{% tab Braze %}

### Enviar datos de clientes a través de Braze

BrazeAI Decisioning Studio puede utilizar todos los datos que ya estás enviando a la plataforma de datos Braze.

Si hay datos de clientes que deseas utilizar para Decisioning Studio y que actualmente no están almacenados en el perfil de usuario ni en los atributos personalizados, lo más recomendable es utilizar [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para importar datos de otras fuentes.

CDI admite integraciones directas con:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para obtener la lista completa de orígenes de datos compatibles, consulta [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Una vez que estés satisfecho con los datos que envías a la plataforma de datos Braze, ponte en contacto con tu equipo de servicios de toma de decisiones basadas en IA para discutir qué campos del perfil de usuario o atributos personalizados deben utilizarse para la toma de decisiones basadas en IA.

Para agilizar este proceso, crea una lista de atributos del perfil de usuario de Braze que consideres que mejor representan los comportamientos de tus clientes y que deberían utilizarse en Decisioning Studio (consulta la [lista de campos disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Tu equipo de servicio también puede ayudarte a llevar a cabo sesiones de descubrimiento para decidir qué campos son los más adecuados para la toma de decisiones mediante IA.

Otras opciones para enviar datos incluyen:

- Envío de eventos personalizados de Braze a través del SDK
- Envío de eventos mediante el punto final REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Estos patrones requieren más esfuerzo de ingeniería, pero a veces son preferibles dependiendo de tu configuración actual de Braze. Ponte en contacto con el equipo de Servicios de toma de decisiones basados en IA para obtener más información.

{% endtab %}
{% tab SFMC %}

### Enviar datos de clientes a través de SFMC

Para integraciones de Salesforce Marketing Cloud:

1. Configura las extensiones de datos SFMC para los datos de clientes.
2. Configura el paquete instalado SFMC para la integración de la API con los permisos adecuados requeridos por Decisioning Studio.
3. Asegúrate de que las extensiones de datos se actualicen a diario, ya que Decisioning Studio extraerá los últimos datos incrementales disponibles.

Proporciona el ID de extensión y la clave de API a tu equipo de servicios de toma de decisiones basados en IA. Te ayudarán con los siguientes pasos en la ingesta de datos de clientes.

{% endtab %}
{% tab Klaviyo %}

### Enviar datos de clientes a través de Klaviyo

Para integraciones con Klaviyo:

1. Confirma que los datos del perfil del cliente están disponibles en los perfiles de Klaviyo.
2. Genera una clave de API privada con acceso completo a los perfiles.
3. Proporciona la clave de API a tu equipo de servicios de toma de decisiones basados en IA.

Consulta la [documentación de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obtener más información sobre la configuración de la clave de API.

{% endtab %}
{% tab Cloud Storage %}

### Otras soluciones en la nube (Google Cloud Storage, Azure, AWS)

Si los datos de clientes no están almacenados actualmente en Braze, SFMC o Klaviyo, el siguiente paso más adecuado es configurar una exportación automatizada directamente a un contenedor de Google Cloud Storage controlado por Braze. También podemos admitir la exportación a AWS o Azure (aunque es preferible GCS). Para estas plataformas, exporta a su almacenamiento en la nube en esas plataformas en la nube y Braze podrá extraer esos datos.

Para determinar si esto es factible, consulta la documentación de tu plataforma MarTech. Por ejemplo:

- mParticle ofrece una [integración nativa con Google Cloud Storage.](https://www.mparticle.com/integration/google-cloud-storage/)
- [Segmento Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma Adobe Experience](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si esto es factible, podemos proporcionar un contenedor GCS para exportar los datos de clientes que estén aislados en Decisioning Studio.

{% endtab %}
{% endtabs %}

## Buenas prácticas

- **Nombres descriptivos de las columnas**: Los datos de clientes deben tener nombres de columna claros y descriptivos. Lo ideal sería que se proporcionara un diccionario de datos.
- **Actualizaciones incrementales**: Los archivos incrementales son preferibles a las instantáneas diarias del historial completo de los clientes.
- **Identificadores consistentes**: Cada registro debe contener un identificador de cliente único que sea coherente en todos los activos de datos.
- **Incluir marcas de tiempo**: Los registros deben tener marcas de tiempo asociadas para una atribución precisa y la formación de los agentes.

## Integraciones personalizadas

Hay otras opciones disponibles, así como canales de datos totalmente personalizados. Esto puede requerir trabajo adicional por parte de tu equipo en materia de servicios o ingeniería. Para determinar qué es factible y óptimo, trabaja con tu equipo de Servicios de toma de decisiones de IA.

{% alert important %}
Esta guía explica los patrones de integración más comunes. El departamento de Seguridad de la Información seguirá teniendo que examinar todos los puntos de conexión y los consultores de soluciones estarán disponibles para asesorar sobre la implementación.
{% endalert %}

## Próximos pasos

Después de conectar tus orígenes de datos, procede a configurar la orquestación:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

