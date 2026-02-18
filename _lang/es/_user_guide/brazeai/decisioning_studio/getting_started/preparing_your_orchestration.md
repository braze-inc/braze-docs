---
nav_title: Preparar tu orquestación
article_title: Preparar tu orquestación
page_order: 3
page_type: reference
description: "Este artículo de referencia explica lo que tienes que preparar antes de configurar la orquestación para BrazeAI Decisioning Studio, incluida la elección de tu CEP y la recopilación de las credenciales y activos necesarios."
---

# Preparar tu orquestación

> Este artículo de referencia explica lo que tienes que preparar antes de configurar la orquestación para BrazeAI Decisioning Studio™, incluida la elección de tu plataforma de interacción con los clientes (CEP) y la recopilación de las credenciales y activos necesarios.

## ¿Qué es la orquestación?

La orquestación es la conexión entre Decisioning Studio y tu plataforma de interacción con los clientes (CEP). Una vez que tu agente de toma de decisiones determina la acción óptima para cada cliente, la orquestación lleva a cabo esas decisiones desencadenando comunicaciones personalizadas a través de tu CEP.

Piénsalo de este modo:

- **Decisioning Studio** decide *qué* enviar y *cuándo* enviarlo
- **Tu CEP** se encarga de *cómo* enviarlo

## Elegir tu CEP

El primer paso es determinar qué plataforma de interacción con los clientes utilizarás con Decisioning Studio. Tu elección afecta a la complejidad de la configuración y a las características disponibles.

### PEC apoyados

| CEP | Estudio de decisión Go | Estudio de decisiones Pro | Tipo de integración |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Integración API nativa (recomendada) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Eventos API + Constructor de Viajes |
| **Klaviyo** | ✓ | ✓ | Eventos API + Flujos |
| **Otros PEC** | - | ✓ | Personalizado (archivo de recomendación) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Si ya utilizas Braze como CEP, te recomendamos que utilices la integración nativa de Braze para que la configuración sea lo más sencilla posible.
{% endalert %}

## Qué necesitarás para prepararte

Antes de configurar la orquestación, reúne los siguientes elementos en función del CEP que hayas elegido.

{% tabs %}
{% tab Braze %}

| Elemento | Descripción |
|------|-------------|
| **Clave de API REST** | Una nueva clave de API con permisos para datos de usuario, mensajes, campañas, Canvas, segmentos y plantillas. |
| **URL del panel de Braze** | La URL de tu instancia de Braze (por ejemplo, `https://dashboard-01.braze.com`). |
| **ID de la aplicación** | La clave de API asociada a la aplicación que quieres seguir (se encuentra en **Configuración** > **Configuración de la aplicación**). |
| **Nombre y dirección de correo electrónico para mostrar** | La información del remitente que utilizarás para tus campañas (se encuentra en **Configuración** > **Preferencias de correo electrónico**). |
| **Plantillas base** | Las plantillas de mensajes que utilizará tu agente para la orquestación. Crearás campañas desencadenadas por la API para cada plantilla. |
| **ID de usuario de prueba** | Un ID de usuario para probar la integración antes del lanzamiento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Elemento | Descripción |
|------|-------------|
| **Credenciales del paquete de la aplicación** | ID de cliente, secreto de cliente, URI base de autenticación, URI base REST y URI base SOAP de un paquete instalado con integración API de servidor a servidor. |
| **Permisos API** | Ámbitos para canales, activos, automatizaciones, viajes, contactos, extensiones de datos y eventos de seguimiento. |
| **Extensiones de datos** | Necesitarás extensiones de datos para datos de suscriptores, datos de interacción y recomendaciones. |
| **Plantillas de correo electrónico** | Las plantillas que quieres que utilice Decisioning Studio, con los ID de plantilla de cada una. |
| **Acceso al Constructor de Viajes** | Acceso para crear y activar trayectos de varios pasos con fuentes de entrada de eventos API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Elemento | Descripción |
|------|-------------|
| **Clave de API privada** | Una nueva clave de API con permisos de acceso completo para eventos, flujos, listas, métricas, perfiles y plantillas. |
| **Plantillas de correo electrónico** | Las plantillas que quieres que utilice Decisioning Studio. Las plantillas deben estar asociadas a un flujo (para ello puedes crear un flujo marcador de posición). |
| **Información del remitente** | El nombre del remitente y la dirección de correo electrónico que utilizarás para tus campañas. |
| **Flujo de acceso** | Acceso para crear y activar flujos con desencadenadores métricos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Las integraciones CEP personalizadas sólo están disponibles con Decisioning Studio Pro.
{% endalert %}

Si utilizas un CEP distinto de Braze, SFMC o Klaviyo, Decisioning Studio Pro puede integrarse mediante un enfoque de archivos de recomendación:

| Elemento | Descripción |
|------|-------------|
| **Capacidad de ingesta de datos** | Tu CEP debe ser capaz de ingerir archivos de recomendaciones (normalmente CSV o JSON) que contengan decisiones personalizadas para cada cliente. |
| **Soporte de contenido dinámico** | Tus campañas deben permitir rellenar campos dinámicamente en función de los datos de recomendación. |
| **Recursos de ingeniería personalizados** | Tu equipo tendrá que construir la integración para leer los archivos de recomendaciones y desencadenar las comunicaciones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planifica tus campañas

Antes de configurar la orquestación, ten en cuenta los siguientes detalles:

### Plantillas base

Una plantilla base es cualquier plantilla de mensaje que pueda utilizar tu agente decisor. Considéralo:

- **¿Cuántas plantillas?** Tu agente puede trabajar con una plantilla o con varias. Si son múltiples, el agente puede personalizar qué plantilla recibe cada cliente.
- **¿Qué canales?** Correo electrónico, push, SMS o una combinación. Cada canal puede requerir plantillas y campañas distintas.
- **¿Qué elementos dinámicos?** Identifica qué partes de tu mensaje personalizará el agente (líneas del asunto, CTA, ofertas, plazos, etc.). Se convertirán en propiedades desencadenantes de la API o en marcadores de posición dinámicos.

### Configuraciones de reeligibilidad

Tus campañas deben permitir a los usuarios recibir mensajes varias veces:

- Para las pruebas, querrás enviar la misma campaña al mismo usuario repetidamente
- En producción, el agente puede determinar que la misma campaña es óptima para un usuario en días consecutivos

{% alert note %}
Al configurar la reelegibilidad para las pruebas, los agentes de Decisioning Studio están diseñados para respetar los límites de frecuencia y no enviarán la misma campaña a un usuario más de una vez al día en producción.
{% endalert %}

### Propiedades de la API desencadenante

Para las integraciones Braze, planifica qué dimensiones optimizará tu agente. Se convierten en propiedades desencadenantes de la API que pasan valores dinámicos a tus campañas:

| Ejemplo de dimensión | Propiedad API desencadenante |
|-------------------|---------------------|
| Línea del asunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Llamada a la acción | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Importe del descuento | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Buenas prácticas

Ten en cuenta estas buenas prácticas cuando te prepares para la orquestación:

1. **Empieza de forma sencilla.** Empieza con un canal y una o dos plantillas. Puedes ampliarlo más adelante a medida que aprendas lo que funciona.
2. **Prueba a fondo.** Antes de poner en marcha la integración, pruébala con un pequeño grupo de usuarios para comprobar que el contenido dinámico se rellena correctamente.
3. **Documenta tu configuración.** Haz un seguimiento de los ID de campaña, los ID de plantilla, las claves de API y otros identificadores. Tendrás que hacer referencia a ellos en el portal Decisioning Studio.
4. **Coordínate con tu equipo.** La configuración de la orquestación puede implicar a equipos de marketing, ingeniería y datos. Asegúrate de que todos comprenden su papel en el proceso.
5. **Planifica los datos de respuesta.** La orquestación no consiste sólo en enviar mensajes, sino también en recopilar los datos de interacción y conversión que ayudan a tu agente a aprender. Consulta [Preparar tus orígenes de datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/) para más detalles.

## Próximos pasos

Una vez que hayas reunido tus credenciales y planificado tus campañas, estarás listo para configurar la orquestación:

- [Estudio de decisión Go: Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

