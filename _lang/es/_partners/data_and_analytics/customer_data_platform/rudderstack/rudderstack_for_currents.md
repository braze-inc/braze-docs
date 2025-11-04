---
nav_title: Rudderstack para Currents
article_title: Rudderstack para Currents
description: "Este artículo describe la asociación entre Braze Currents y Rudderstack, una infraestructura de datos de clientes de código abierto que ofrece una integración perfecta de Braze para tus aplicaciones Android, iOS y Web."
page_type: partner
tool: Currents
search_tag: Partner

---

# Rudderstack para Currents

> [Rudderstack](https://www.rudderstack.com/) te permite recopilar, transformar y activar los datos de clientes en toda tu pila, aprovechando tu almacén de datos en la nube como fuente central de la verdad. Este artículo ofrece un resumen de cómo establecer una conexión entre Braze Currents y Rudderstack.

La integración de Braze y Rudderstack te permite aprovechar Braze Currents para exportar tus eventos de Braze a Rudderstack para impulsar análisis más profundos.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta RudderStack | Se requiere una [cuenta Rudderstack](https://app.rudderstack.com/login) para beneficiarse de esta asociación. |
| Destino Braze | Te sugerimos que hayas configurado [Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) en Rudderstack. |
| Currents | Para volver a exportar datos a Rudderstack, necesitas tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crear un origen de datos para Braze dentro de Rudderstack

En primer lugar, debes crear una fuente Braze en la aplicación Web Rudderstack. Puedes encontrar instrucciones para crear un origen de datos en el sitio web [de Rudderstack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Una vez completado, Rudderstack proporcionará una URL de webhook, incluida la clave de escritura, que deberás utilizar en el siguiente paso. Puedes encontrar la URL del webhook en la pestaña **Configuración** de tu fuente Braze.

### Paso 2: Crear Current

En Braze, ve a **Current > + Crear Current > Exportar Rudderstack**. Proporciona el nombre de la integración, el correo electrónico de contacto, la URL del webhook de RudderStack (que va en el campo clave) y la región de RudderStack. 

### Paso 3: Exportar eventos

A continuación, selecciona los eventos que deseas exportar. Por último, haz clic en **Lanzar Current**

Todos los eventos enviados a Rudderstack incluirán la dirección `external_user_id` del usuario. En este momento, Braze no envía datos de eventos a Rudderstack para los usuarios que no tienen configurado su `external_user_id`.

## Detalles de la integración

Braze admite la exportación a Rudderstack de todos los datos incluidos en [los glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/braze_currents/).

La estructura de la carga útil para los datos exportados es la misma que la de los conectores HTTP personalizados, que puedes consultar en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).