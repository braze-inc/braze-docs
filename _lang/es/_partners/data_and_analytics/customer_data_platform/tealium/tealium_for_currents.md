---
nav_title: Tealium para corrientes
article_title: Tealium para corrientes
page_order: 3
alias: /partners/tealium_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Tealium, una plataforma de datos de clientes que recopila y encamina información entre fuentes de su pila de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium para corrientes

> [Tealium](https://www.tealium.com) es una plataforma de datos de clientes que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en su pila de marketing.

La integración de Braze y Tealium le permite controlar perfectamente el flujo de información entre los dos sistemas. Con Currents, también puedes conectar los datos a Tealium para que sean procesables en todo el stack de crecimiento. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Tealium EventStream o Tealium AudienceStream | Se necesita una [cuenta Tealium](https://my.tealiumiq.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar datos a Tealium, debe tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en su cuenta. |
| URL de Tealium | Puedes obtenerlos navegando a tu panel de Tealium y copiando la URL de ingesta.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crear una fuente de datos para Braze en Tealium

Las instrucciones para crear una fuente de datos se encuentran en el sitio de [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Una vez completado, Tealium te proporcionará una URL de origen de datos para copiar, que utilizarás en el siguiente paso.

### Paso 2: Crear corriente

En Braze, ve a **Currents** > **\+ Crear corriente** > **Exportar Tealium**. Proporcione un nombre de integración, un correo electrónico de contacto y su URL de Tealium. 

A continuación, seleccione lo que desea seguir de la lista de eventos disponibles. Por defecto, todos los eventos enviados a Tealium incluyen la dirección `external_user_id` del usuario. Sin embargo, puedes seleccionar la casilla **Incluir eventos de usuarios anónimos** para enviar también a Tealium los eventos que no tengan un `external_user_id`.

Después de configurar tu integración, selecciona **Lanzar Actual**.

{% alert important %}
Es importante mantener actualizada la URL de Tealium. Si la URL de su conector es incorrecta, Braze no podrá enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Detalles de la integración

Braze admite la exportación a Tealium de todos los datos enumerados en [los glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (incluidas todas las propiedades tanto de los eventos de [compromiso de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) como de [comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ).

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados, que puede consultarse en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).
