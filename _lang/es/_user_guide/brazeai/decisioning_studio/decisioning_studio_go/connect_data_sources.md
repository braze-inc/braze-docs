---
nav_title: Conectar orígenes de datos
article_title: Conectar orígenes de datos
page_order: 1
description: "Descubre cómo BrazeAI Decisioning Studio Go se conecta a los datos de clientes a través de tu plataforma de interacción con los clientes."
---

# Conectar orígenes de datos

> BrazeAI Decisioning Studio™ Go se conecta a los datos de tus clientes a través de tu plataforma de interacción con los clientes (CEP). Este artículo explica qué datos se utilizan y cómo funciona la conexión.

## Cómo Go accede a los datos de clientes

A diferencia de Decisioning Studio Pro, que admite integraciones directas de datos con diversos orígenes de datos, Decisioning Studio Go accede a los datos de clientes a través de tu CEP. Esto significa:

<<<<<<< HEAD
- **Los datos de audiencia** se extraen directamente de segmentos o listas definidos en tu CEP (Braze o Salesforce Marketing Cloud) y sólo pueden incluir ciertos atributos predefinidos (no datos 1P)
- **Los datos de interacción** (aperturas, clics, envíos) se capturan mediante consultas automatizadas o integraciones nativas con tu CEP.
- **No** se requiere **ninguna configuración adicional de la canalización de** datos más allá de lo que configures en tu CEP
=======
- **Los datos de audiencia** se extraen directamente de los segmentos o listas definidos en tu CEP (Braze, Salesforce Marketing Cloud o Klaviyo) y solo pueden incluir determinados atributos predefinidos (no datos 1P).
- **Los datos de interacción** (aperturas, clics, envíos) se recopilan mediante consultas automatizadas o integraciones nativas con tu CEP.
- **No** es necesario **configurar ningún canal de datos adicional** más allá de lo que configures en tu CEP.
>>>>>>> develop

## Patrones de integración compatibles

Decisioning Studio Go admite los siguientes CEP para el acceso a datos:

| CEP | Fuente de audiencia | Datos de participación |
|-----|-----------------|-----------------|
| **Braze** | Segmentos | Exportación de Braze Currents |
| **Salesforce Marketing Cloud** | Extensiones de datos | Automatización de consultas SQL |
<<<<<<< HEAD
=======
| **Klaviyo** | Segmentos | Integración con API nativa |
>>>>>>> develop
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Requisitos de datos según el CEP

{% tabs %}
{% tab Braze %}

### Requisitos de datos de Braze

Para las integraciones de Braze, Decisioning Studio Go requiere:

1. **Braze Currents**: Debes tener Braze Currents habilitado y configurado para exportar datos de interacción a Decisioning Studio Go. Esto permite al agente aprender de las respuestas de los clientes.

2. **Acceso al segmento**: La clave de API que crees debe tener permisos para acceder a los segmentos que definen tu audiencia objetivo.

3. **Datos del perfil de usuario**: Cualquier atributo del perfil de usuario o atributo personalizado que desees que el agente tenga en cuenta debe ser accesible a través de la API de Braze.

{% alert important %}
Asegúrate de que tu exportación de Braze Currents incluya datos de todas las campañas con las que quieras comparar (incluidas las campañas BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Requisitos de datos de SFMC

Para las integraciones de Salesforce Marketing Cloud, Decisioning Studio Go requiere:

1. **Extensiones de datos**: Tu audiencia debe estar definida en una extensión de datos a la que Decisioning Studio Go pueda acceder. Utiliza la clave de suscriptor como identificador principal del usuario.
2. **Acceso al seguimiento de eventos**: Siempre que el paquete de aplicaciones instalado admita la automatización de la configuración de extremo a extremo, no se requiere ninguna configuración adicional. 

Las extensiones de datos y las consultas SQL se configuran como parte de la [configuración de la]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) [orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
<<<<<<< HEAD
=======
{% tab Klaviyo %}

### Requisitos de datos de Klaviyo

Para las integraciones de Klaviyo, Decisioning Studio Go requiere:

1. **Acceso al segmento**: Tu audiencia debe definirse como un segmento de Klaviyo al que pueda acceder la clave de API.
2. **Datos del perfil**: La clave de API debe tener acceso completo a los perfiles para leer los atributos de los clientes.
3. **Acceso a métricas**: La clave de API debe tener acceso completo a métricas y eventos para capturar datos de interacción.

{% endtab %}
>>>>>>> develop
{% endtabs %}

## Buenas prácticas

- **Mantén los datos actualizados**: Asegúrate de que tus segmentos de audiencia y datos de clientes se actualicen con regularidad (como mínimo, a diario) para que el agente trabaje con información actualizada.
- **Incluye los atributos relevantes**: Piensa en las características de los clientes que podrían influir en los mensajes que les llegan: los datos demográficos, el historial de interacción, el comportamiento de compra y la etapa del ciclo de vida son señales muy valiosas.

## Próximos pasos

Ahora que ya sabes cómo se conecta Go a los datos, continúa con la configuración de la integración CEP:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

