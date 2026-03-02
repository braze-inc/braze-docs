---
nav_title: Conectar orígenes de datos
article_title: Conectar orígenes de datos
page_order: 1
description: "Descubre cómo BrazeAI Decisioning Studio Go se conecta a los datos de tus clientes a través de tu plataforma de interacción con los clientes."
---

# Conectar orígenes de datos

> BrazeAI Decisioning Studio™ Go se conecta a tus datos de clientes a través de tu plataforma de interacción con los clientes (CEP). Este artículo explica qué datos se utilizan y cómo funciona la conexión.

## Cómo accede Go a los datos de clientes

A diferencia de Decisioning Studio Pro, que admite integraciones directas de datos con diversas fuentes, Decisioning Studio Go accede a los datos de clientes a través de tu CEP. Es decir:

- **Los datos de audiencia** se extraen directamente de segmentos o listas definidos en tu CEP (Braze o Salesforce Marketing Cloud) y sólo pueden incluir ciertos atributos predefinidos (no datos 1P)
- **Los datos de interacción** (aperturas, clics, envíos) se capturan mediante consultas automatizadas o integraciones nativas con tu CEP.
- **No** se requiere **ninguna configuración adicional de la canalización de** datos más allá de lo que configures en tu CEP

## Modelos de integración admitidos

Decisioning Studio Go admite los siguientes CEP para el acceso a los datos:

| CEP | Fuente de la audiencia | Datos de participación |
|-----|-----------------|-----------------|
| **Braze** | Segmentos | Exportación de Braze Currents |
| **Salesforce Marketing Cloud** | Extensiones de datos | Automatización de consultas SQL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Requisitos de datos por CEP

{% tabs %}
{% tab Braze %}

### Requisitos de los datos Braze

Para las integraciones Braze, Decisioning Studio Go requiere:

1. **Braze Currents**: Debes tener habilitado y configurado Braze Currents para exportar datos de interacción a Decisioning Studio Go. Esto permite al agente aprender de las respuestas de los clientes.

2. **Acceso a segmentos**: La clave de API que crees debe tener permisos para acceder a los segmentos que definen tu audiencia objetivo.

3. **Datos de perfil de usuario**: Cualquier atributo del perfil de usuario o atributo personalizado que quieras que tenga en cuenta el agente debe ser accesible a través de la API de Braze.

{% alert important %}
Asegúrate de que tu exportación Braze Currents incluye datos de cualquier campaña con la que quieras comparar (incluidas las campañas BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Requisitos de los datos del SFMC

Para las integraciones de Salesforce Marketing Cloud, Decisioning Studio Go requiere:

1. **Extensiones de datos**: Tu audiencia debe estar definida en una Extensión de Datos a la que Decisioning Studio Go pueda acceder. Utiliza el SubscriberKey como identificador principal del usuario.
2. **Seguimiento del acceso a los eventos**: Mientras el paquete de aplicación instalado admita la configuración automatizada de extremo a extremo, no será necesaria ninguna configuración adicional. 

Las extensiones de datos y las consultas SQL se configuran como parte de la [configuración de la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% endtabs %}

## Buenas prácticas

- **Mantén los datos actualizados**: Asegúrate de que tus segmentos de audiencia y datos de clientes se actualizan regularmente (como mínimo, a diario) para que el agente trabaje con información actual.
- **Incluye los atributos relevantes**: Piensa en qué características de los clientes pueden influir en la resonancia de los mensajes: los datos demográficos, el historial de interacción, el comportamiento de compra y la fase del ciclo de vida son señales valiosas.

## Próximos pasos

Ahora que ya sabes cómo se conecta Go a los datos, procede a configurar tu integración CEP:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

