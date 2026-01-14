---
nav_title: Datos del Tesoro para Corrientes
article_title: Datos del Tesoro para Corrientes
description: "Este artículo de referencia describe la asociación entre Braze Currents y Treasure Data, una plataforma de datos de clientes empresariales que permite escribir resultados de trabajos directamente en Braze."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Datos del Tesoro para Corrientes

> [Treasure Data](https://www.treasuredata.com/) es una plataforma de datos de clientes (CDP) que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en su pila de marketing.

La integración de Braze y Treasure Data te permite controlar fácilmente el flujo de información entre ambos sistemas. Con Currents, también puedes conectar los datos a Treasure Data para que sean procesables en toda la stack de crecimiento.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Treasure Data | Se necesita una [cuenta de Treasure Data](https://console.treasuredata.com/users/sign_in) para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Treasure Data, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
| URL de datos del Tesoro | Esto se puede obtener navegando a tu panel de Treasure Data y copiando la URL de ingesta.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Treasure Data registra cada evento por lotes. Para más información sobre cómo consultar Treasure Data para obtener recuentos de eventos, consulta [Integración de Importación de Braze Currents](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration).
{% endalert %}

## Integración

El método recomendado para conectar con Treasure Data es a través de la API Postback. Este método no requiere un conector predeterminado y los datos pueden recibirse a través de un enfoque push. Todos los eventos enviados en un lote de datos están dentro de un campo de una fila en un array JSON, que necesita ser analizado para obtener los datos requeridos.

{% alert important %}
Actualmente, la ingesta en Treasure Data a través del recopilador de eventos no se produce en tiempo real y puede tardar hasta cinco minutos.
{% endalert %}

### Paso 1: Configurar la API Postback de Treasure Data con Braze

Puedes encontrar instrucciones para crear una API Postback en el [sitio web de Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). Braze enviará directamente los eventos actualizados a Treasure Data en tiempo real, a excepción de la ingesta a través del recolector de eventos. Una vez completado, Treasure Data proporcionará una URL de origen de datos que deberás copiar para utilizarla en el siguiente paso.

### Paso 2: Crear corriente

En Braze, vaya a **Corrientes** > **\+ Crear corriente** > **Exportar datos de tesorería**. Proporciona un nombre de integración, un correo electrónico de contacto y tu URL de Treasure Data. A continuación, seleccione lo que desea rastrear de la lista de eventos disponibles y haga clic en **Lanzar actual**.

Todos los eventos enviados a Treasure Data incluirán la dirección `external_user_id` del usuario. En este momento, Braze no envía datos de eventos a Treasure Data para los usuarios que no han configurado su `external_user_id`.

{% alert important %}
Mantén actualizada tu URL de Treasure Data. Si la URL de tu conector es incorrecta, Braze no podrá enviar eventos. Si esto persiste durante más de 48 horas, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

#### Ejemplo de valor de campo de evento
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Ejemplo de vista ingestada

![4]{: style="max-width:70%;"}

## Detalles de la integración

Braze admite la exportación a Treasure Data de todos los datos enumerados en [los glosarios de eventos Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (incluidas todas las propiedades tanto de los eventos de [compromiso de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) como de [comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ).

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados, que puede consultarse en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
