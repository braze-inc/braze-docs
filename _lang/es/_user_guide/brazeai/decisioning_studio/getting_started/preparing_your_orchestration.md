---
nav_title: Preparación de tu orquestación
article_title: Preparación de tu orquestación
page_order: 3
page_type: reference
description: "Este artículo de referencia explica lo que debes preparar antes de configurar la orquestación para BrazeAI Decisioning Studio, incluyendo la elección de tu CEP y la recopilación de las credenciales y los activos necesarios."
---

# Preparación de tu orquestación

> Este artículo de referencia explica lo que debes preparar antes de configurar la orquestación para BrazeAI Decisioning Studio™, incluyendo la elección de tu plataforma de interacción con los clientes (CEP) y la recopilación de las credenciales y los activos necesarios.

## ¿Qué es la orquestación?

La orquestación es la conexión entre Decisioning Studio y tu plataforma de interacción con los clientes (CEP). Una vez que tu agente de toma de decisiones determina la acción óptima para cada cliente, la orquestación lleva a cabo esas decisiones desencadenando comunicaciones personalizadas a través de tu CEP.

Piénsalo de esta manera:

- **Decisioning Studio** decide *qué* enviar y *cuándo* enviarlo.
- **Tu CEP** se encarga de *cómo* enviarlo.

## Elegir tu CEP

El primer paso es determinar qué plataforma de interacción con los clientes vas a utilizar con Decisioning Studio. Tu elección afecta a la complejidad de la configuración y a las características disponibles.

### CEP compatibles

| CEP | Estudio de toma de decisiones Go | Decisioning Studio Pro | Tipo de integración |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Integración con API nativa (recomendado) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Eventos API + Journey Builder |
| **Klaviyo** | ✓ | ✓ | Eventos API + Flujos |
| **Otros CEP** | — | ✓ | Personalizado (archivo de recomendaciones) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Si ya utilizas Braze como tu CEP, te recomendamos utilizar la integración nativa de Braze para disfrutar de una experiencia de configuración más fluida.
{% endalert %}

## Lo que necesitarás preparar

Antes de configurar la orquestación, reúne los siguientes elementos en función del CEP que hayas elegido.

{% tabs %}
{% tab Braze %}

| Elemento | Descripción |
|------|-------------|
| **Clave de API REST** | Una nueva clave de API con permisos para datos de usuario, mensajes, campañas, Canvas, segmentos y plantillas. |
| **URL del panel de Braze** | La URL de tu instancia de Braze (por ejemplo, `https://dashboard-01.braze.com`). |
| **ID de la aplicación** | La clave de API asociada a la aplicación que deseas seguir (se encuentra en **Configuración** > **Configuración de la aplicación**). |
| **Nombre y dirección de correo electrónico que aparecerán en la pantalla** | La información del remitente que se utilizará en tus campañas (se encuentra en **Configuración** > **Preferencias de correo electrónico**). |
| **Plantillas base** | Las plantillas de mensajes que tu agente utilizará para la orquestación. Crearás campañas activadas por API para cada plantilla. |
| **ID de usuario de prueba** | Un ID de usuario para probar la integración antes del lanzamiento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Elemento | Descripción |
|------|-------------|
| **Credenciales del paquete de aplicaciones** | ID de cliente, secreto de cliente, URI base de autenticación, URI base REST y URI base SOAP de un paquete instalado con integración de API de servidor a servidor. |
| **Permisos de API** | Ámbitos para canales, activos, automatizaciones, recorridos, contactos, extensiones de datos y eventos de seguimiento. |
| **Extensiones de datos** | Necesitarás extensiones de datos para los datos de los suscriptores, los datos de interacción y las recomendaciones. |
| **Plantillas de correo electrónico** | Las plantillas que deseas que utilice Decisioning Studio, con los ID de plantilla correspondientes a cada una. |
| **Acceso a Journey Builder** | Acceso para crear y activar recorridos de varios pasos con fuentes de entrada de eventos API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Elemento | Descripción |
|------|-------------|
| **Clave de API privada** | Una nueva clave de API con permisos de acceso completo para eventos, flujos, listas, métricas, perfiles y plantillas. |
| **Plantillas de correo electrónico** | Las plantillas que deseas que utilice Decisioning Studio. Las plantillas deben estar asociadas a un flujo (puedes crear un flujo marcador de posición para este fin). |
| **Información del remitente** | El nombre y la dirección de correo electrónico del remitente que se utilizarán en tus campañas. |
| **Acceso al flujo** | Acceso para crear y activar flujos con desencadenantes métricos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Las integraciones CEP personalizadas solo están disponibles con Decisioning Studio Pro.
{% endalert %}

Si utilizas un CEP distinto de Braze, SFMC o Klaviyo, Decisioning Studio Pro puede realizar la integración mediante un archivo de recomendaciones:

| Elemento | Descripción |
|------|-------------|
| **Capacidad de ingesta de datos** | Tu CEP debe ser capaz de incorporar archivos de recomendaciones (normalmente CSV o JSON) que contengan decisiones personalizadas para cada cliente. |
| **Compatibilidad con contenido dinámico** | Tus campañas deben admitir el rellenado dinámico de campos basándose en datos de recomendación. |
| **Recursos de ingeniería personalizados** | Tu equipo deberá crear la integración para leer los archivos de recomendaciones y desencadenar las comunicaciones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planificación de tus campañas

Antes de configurar la orquestación, ten en cuenta los siguientes detalles:

### Plantillas base

Una plantilla base es cualquier plantilla de mensaje que pueda utilizar tu agente de toma de decisiones. Considera lo siguiente:

- **¿Cuántas plantillas?** Tu agente puede trabajar con una o varias plantillas. Si hay varias, el agente puede realizar la personalización de la plantilla que recibe cada cliente.
- **¿Qué canales?** Correo electrónico, notificaciones push, SMS o una combinación de todos ellos. Cada canal puede requerir plantillas y campañas independientes.
- **¿Qué elementos dinámicos?** Identifica qué partes de tu mensaje serán objeto de personalización por parte del agente (línea del asunto, llamadas a la acción, ofertas, momento, etc.). Estos se convertirán en propiedades de activación de API o marcadores de posición dinámicos.

### Configuración de reelegibilidad

Tus campañas deben permitir que los usuarios reciban mensajes varias veces:

- Para realizar pruebas, es recomendable enviar la misma campaña al mismo usuario repetidamente.
- En la producción, el agente puede determinar que la misma campaña es óptima para un usuario en días consecutivos.

{% alert note %}
Al configurar la reelegibilidad para las pruebas, los agentes de Decisioning Studio están diseñados para respetar las limitaciones de frecuencia y no enviarán la misma campaña a un usuario más de una vez al día en producción.
{% endalert %}

### Propiedades del activador API

Para las integraciones de Braze, planifica qué dimensiones optimizará tu agente. Estas se convierten en propiedades de activación de API que pasan valores dinámicos a tus campañas:

| Ejemplo de dimensión | Propiedad de desencadenamiento de API |
|-------------------|---------------------|
| Línea de asunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Llamada a la acción | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Importe del descuento | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Buenas prácticas

Ten en cuenta estas prácticas recomendadas mientras te preparas para la orquestación:

1. **Empieza por lo sencillo.** Empieza con un canal y una o dos plantillas. Puedes ampliarlo más adelante, a medida que aprendas qué es lo que funciona.
2. **Prueba a fondo.** Antes del lanzamiento, prueba la integración con un pequeño grupo de usuarios para verificar que el contenido dinámico se rellene correctamente.
3. **Documenta tu configuración.** Realiza un seguimiento de los ID de campaña, los ID de plantilla, las claves de API y otros identificadores. Tendrás que hacer referencia a ellos en el portal Decisioning Studio.
4. **Coordínate con tu equipo.** La configuración de la orquestación puede involucrar a los equipos de marketing, ingeniería y datos. Asegúrate de que todos comprendan su función en el proceso.
5. **Planifica los datos de retroalimentación.** La orquestación no consiste solo en enviar mensajes, sino también en recopilar datos sobre la interacción y la conversión que ayudan a tus agentes a aprender. Consulta [Preparación de los orígenes de datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/) para obtener más información.

## Próximos pasos

Una vez que hayas recopilado tus credenciales y planificado tus campañas, estarás listo para configurar la orquestación:

- [Decisioning Studio Go: Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

