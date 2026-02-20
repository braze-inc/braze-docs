---
nav_title: Conectar orígenes de datos
article_title: Conectar orígenes de datos
page_order: 1
description: "Aprende a conectar los orígenes de datos de clientes a BrazeAI Decisioning Studio Pro para tomar decisiones personalizadas con IA."
---

# Conectar orígenes de datos

> Los agentes de BrazeAI Decisioning Studio™ Pro necesitan comprender plenamente el contexto del cliente para tomar decisiones eficaces. Este artículo explica cómo conectar fuentes de datos de clientes a Decisioning Studio Pro.

{% alert tip %}
Tu equipo de Servicios de Decisión sobre IA te ayudará a configurar las conexiones de datos para obtener un rendimiento óptimo.
{% endalert %}

## Modelos de integración admitidos

Decisioning Studio Pro admite múltiples patrones de integración para conectar datos de clientes:

| Modelo de integración | Lo mejor para | Complejidad de la instalación |
|---------------------|----------|------------------|
| **Plataforma de datos Braze** | Clientes que ya utilizan Braze | Baja |
| **Ingesta de datos en la nube Braze (CDI)** | Conexión de almacenes de datos externos | Media |
| **Almacenamiento en la nube (GCS, AWS, Azure)** | Exportación directa de datos desde otras plataformas | Media |
| **Integraciones CEP** | SFMC, extensiones de datos Klaviyo | Media |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Tipos de datos de clientes

Los siguientes activos de datos de clientes ayudan a los agentes a personalizar de forma más eficaz:

| Tipo de datos | Descripción | Ejemplos |
|-----------|-------------|----------|
| **Perfil del cliente** | Atributos estáticos y que cambian lentamente | Años como cliente, geografía, canal de adquisición, nivel de satisfacción, estimación del valor del ciclo de vida |
| **Comportamiento del cliente** | Patrones de actividad e interacción | Inicio de sesión de la cuenta, tipo de dispositivo, interacciones con el servicio de atención al cliente, uso del producto |
| **Historial de transacciones** | Datos de compra y conversión | Productos comprados, importes de las transacciones, métodos de pago, canales de compra |
| **Interacción en marketing** | Respuestas a las comunicaciones | Aperturas/clics de correo electrónico, interacción por SMS, actividad web y móvil, respuestas a cuestionarios |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Cuanta más información tengan los agentes sobre tus clientes, mejor rendimiento obtendrán. Considera la posibilidad de incluir datos sobre cualquier información que sea especialmente importante para tu empresa (por ejemplo, ¿quieres ver cómo la IA trata de forma diferente a tus clientes fidelizados? Asegúrate de que el estado de fidelización está en los datos de clientes).
{% endalert %}

## Conectar datos por plataforma

{% tabs %}
{% tab Braze %}

### Envía datos de clientes a través de Braze

BrazeAI Decisioning Studio puede utilizar todos los datos que ya estés enviando a la Plataforma de Datos Braze.

Si hay datos de clientes que quieras utilizar para Decisioning Studio que no estén almacenados actualmente en el perfil de usuario o en los atributos personalizados, lo recomendable es utilizar [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para ingesta de datos de otros orígenes.

El CDI admite integraciones directas con:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para ver la lista completa de fuentes admitidas, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Una vez que estés satisfecho con los datos que envías a la plataforma de datos Braze, ponte en contacto con tu equipo de servicios de toma de decisiones sobre IA para discutir qué campos del perfil de usuario o atributos personalizados deben utilizarse para la toma de decisiones sobre IA.

Para agilizar este proceso, crea una lista de atributos del perfil de usuario Braze que creas que representan mejor los comportamientos de tus clientes que deberían utilizarse en Decisioning Studio (consulta la [lista de campos disponibles]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Tu equipo de servicios también puede ayudarte a realizar sesiones de descubrimiento para decidir qué campos son los más apropiados para la toma de decisiones con IA.

Otras opciones para enviar datos son

- Envío de eventos personalizados Braze a través del SDK
- Envío de eventos mediante el punto final REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Estos patrones requieren un mayor esfuerzo de ingeniería, pero a veces son preferibles dependiendo de tu configuración actual de Braze. Ponte en contacto con el equipo de AI Decisioning Services para obtener más información.

{% endtab %}
{% tab SFMC %}

### Enviar datos de clientes a través de SFMC

Para integraciones de Salesforce Marketing Cloud:

1. Configura la(s) Extensión(es) de Datos SFMC para tus datos de clientes
2. Configura el paquete instalado de SFMC para la integración de la API con los permisos adecuados requeridos por Decisioning Studio
3. Asegúrate de que las extensiones de datos se actualizan diariamente, ya que Decisioning Studio tirará de los últimos datos incrementales disponibles

Proporciona el ID de extensión y la clave de API a tu equipo de Servicios de Decisión sobre IA. Ayudarán con los siguientes pasos en la ingesta de datos de clientes.

{% endtab %}
{% tab Klaviyo %}

### Envía datos de clientes a través de Klaviyo

Para las integraciones de Klaviyo:

1. Confirma que los datos de perfil de clientes están disponibles en los perfiles de Klaviyo
2. Generar una clave de API privada con acceso completo a los perfiles
3. Proporciona la clave de API a tu equipo de Servicios de Decisión sobre IA

Consulta la [documentación de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obtener más información sobre la configuración de la clave de API.

{% endtab %}
{% tab Cloud Storage %}

### Otras soluciones en la nube (Google Cloud Storage, Azure, AWS)

Si los datos de clientes no están almacenados actualmente en Braze, SFMC o Klaviyo, el siguiente mejor paso es configurar una exportación automatizada directamente a un contenedor de Google Cloud Storage controlado por Braze. También podemos exportar a AWS o Azure (aunque es preferible GCS). Para estas plataformas, exporta a su almacenamiento en la nube interno en esas plataformas en la nube y Braze podrá entonces extraer esos datos.

Para determinar si esto es factible, consulta la documentación de tu plataforma MarTech. Por ejemplo:

- mParticle ofrece una [integración nativa con Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Segmento Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma Adobe Experience](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Si esto es factible, podemos proporcionar un contenedor GCS al que exportar los datos de clientes y que esté aislado de Decisioning Studio.

{% endtab %}
{% endtabs %}

## Buenas prácticas

- **Nombres descriptivos de las columnas**: Los datos de clientes deben tener nombres de columna claros y descriptivos. Lo ideal sería proporcionar un diccionario de datos.
- **Actualizaciones incrementales**: Los archivos incrementales son preferibles a las instantáneas de todo el historial del cliente cada día
- **Identificadores coherentes**: Cada registro debe contener un identificador único de cliente que sea coherente en todos los activos de datos
- **Incluye marcas de tiempo**: Los registros deben tener marcas de tiempo asociadas para una atribución precisa y la formación de los agentes

## Integraciones personalizadas

Son posibles otras opciones o canalizaciones de datos totalmente personalizadas. Esto puede requerir un trabajo adicional de servicios o de ingeniería por parte de tu equipo. Para determinar qué es factible y óptimo, trabaja con tu equipo de Servicios de Decisión sobre IA.

{% alert important %}
Esta guía explica los modelos de integración más habituales. La Seguridad de la Información tendrá que examinar todos los puntos de conexión y los Consultores de Soluciones estarán disponibles para asesorar sobre la implantación.
{% endalert %}

## Próximos pasos

Tras conectar tus orígenes de datos, procede a configurar la orquestación:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

