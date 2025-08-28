---
nav_title: Regal
article_title: Regal
description: "Este artículo de referencia describe la asociación entre Braze y Regal, una solución de ventas por teléfono y SMS que le permite utilizar datos de ambas fuentes para crear experiencias personalizadas para sus clientes."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) es la solución de ventas por teléfono y SMS creada para impulsar más conversaciones y que puedas alcanzar tus objetivos de crecimiento mucho más rápido.

Al integrar Regal y Braze, puede crear una experiencia más coherente y personalizada en todos los puntos de contacto con el cliente.
- Envía el siguiente mejor correo electrónico o notificación push de Braze basándote en lo que se dice en una conversación telefónica en Regal.
- Active una llamada en Regal cuando un cliente de alto valor haga clic en un correo electrónico de marketing de Braze pero no se convierta.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Regal | Se necesita una cuenta Regal para beneficiarse de esta asociación. |
| Clave API de Regal | Una clave API de Regal permitirá enviar eventos de Braze a Regal.<br><br>Envía un correo electrónico a [support@regal.io](mailto:support@regal.io) para obtener esta clave. |
| Transformación de datos Braze | La transformación de datos se encuentra actualmente en fase de acceso anticipado. Póngase en contacto con su gestor de éxito de clientes de Braze si está interesado en participar en el acceso anticipado. Esto es necesario para recibir datos del Regal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración: Envío de datos de Braze a Regal

La siguiente sección describe cómo utilizar Braze como fuente para enviar el perfil de su cliente y datos de eventos a Regal utilizando Braze Canvas o webhooks de campaña.

### Paso 1: Crear nuevos contactos en Regal

Cree un Canvas o campaña que se conecte a Regal cada vez que se cree un nuevo contacto en Braze que desee que esté disponible para llamadas y mensajes de texto en Regal. 

1. Cree un lienzo o campaña con el título "Crear nuevo contacto para Regal" y seleccione **Basado en acciones** como tipo de entrada.

2. Establezca la lógica de activación como **Evento personalizado** y seleccione el evento que se dispara cuando se crea un contacto con un número de teléfono. Regal también recomienda añadir un filtro adicional en el campo del teléfono que garantice que está configurado.

3. En su nueva plantilla de webhook, rellene los siguientes campos:
   - **URL del webhook**: <https://events.regalvoice.com/events>
   - **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Regal.io también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor en la pestaña **Configuración**:
{% raw %}
- **Método HTTP**: POST
- **Encabezados de solicitud**:
    - **Autorización**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

El único campo obligatorio a continuación es la propiedad `traits.phone`. El resto es opcional. Sin embargo, si incluyes `optIn`, debes incluir `optIn.channel` y `optIn.subscribed`.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

El ejemplo de carga útil anterior supone que todos tus contactos han aceptado la adhesión voluntaria para voz y SMS. Si no es así, puedes eliminar la propiedad `optIn` de lo anterior y configurar un Canvas o campaña independiente para actualizar un contacto en Regal cuando se recopile `optIn`.

### Paso 2: Actualizar la información de registro 

Si la adhesión voluntaria y la exclusión pueden producirse en diferentes partes de la experiencia del usuario en tu aplicación, es importante actualizar Regal a medida que los usuarios se adhieren o se excluyen. A continuación encontrarás un Canvas recomendado sobre cómo enviar información actualizada de adhesión voluntaria a Regal. Se supone que lo guarda como un campo de perfil de Braze, pero si no es así, el desencadenante puede ser fácilmente un evento de su cuenta de Braze que represente a un usuario que se suscribe o se da de baja. (El ejemplo de abajo es para la adhesión voluntaria por teléfono, pero puedes configurar un Canvas o campaña similar para la adhesión voluntaria por SMS si los recoges por separado).

1. Crea un nuevo Canvas o campaña titulado "Enviar adhesión voluntaria o baja en Regal".

2. Selecciona una de las siguientes opciones de desencadenamiento y selecciona el campo que represente el estado de adhesión voluntaria del usuario. Si envía un evento a Braze para representar la aceptación o rechazo, utilice ese evento como disparador.
    - Campo de perfil de usuario actualizado
    - Actualizar el estado del grupo de suscripción
    - Estado de la suscripción

3. En tu nueva plantilla Webhook, rellena los siguientes campos:
   - **URL del webhook**: <https://events.regalvoice.com/events>
   - **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Regal.io también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**:
{% raw %}
- **Método HTTP**: POST
- **Encabezados de solicitud**:
    - **Autorización**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

Puede añadir más atributos de perfil de usuario en esta carga útil si desea asegurarse de que más atributos están actualizados simultáneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Paso 3: Enviar eventos personalizados

Por último, configura un Canvas o campaña para cada uno de los eventos clave que quieras enviar a Regal. Regal recomienda enviar cualquier evento que sea importante para desencadenar SMS y Llamadas en Regal (como un evento en cada paso del flujo de registro o compra) o que se utilice como criterio de salida para que los contactos se salgan de las campañas de Regal.

Por ejemplo, a continuación se muestra un flujo de trabajo para enviar a Regal un evento cuando un usuario completa el primer paso de una Aplicación.

1. Crea un nuevo Canvas o campaña titulado "Enviar Solicitud Paso 1 Evento Completado a Regal".

2. Establezca la lógica del nodo disparador como **Evento Personalizado** y seleccione el nombre del evento que desea enviar a Regal, como por ejemplo "Paso 1 de la aplicación completado".

3. En tu nueva plantilla Webhook, rellena los siguientes campos:
   - **URL del webhook**: <https://events.regalvoice.com/events>
   - **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Regal.io también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**:
{% raw %}
- **Método HTTP**: POST
- **Encabezados de solicitud**:
    - **Autorización**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

Puede añadir más atributos de perfil de usuario en esta carga útil si desea asegurarse de que más atributos están actualizados simultáneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Atributos de contacto actualizados

Aunque no es necesario, Regal recomienda enviar también cualquier campo de datos de perfil de usuario clave en las cargas útiles de eventos de sus flujos de trabajo de eventos para garantizar que Regal tenga acceso a los atributos de contacto más actualizados en el momento en que los eventos clave estén disponibles.

{% alert note %}
Si tienes preguntas sobre qué eventos es importante enviar a Regal o sobre la mejor manera de configurar estos Lienzos y campañas, ponte en contacto con support@regal.io.
{% endalert %}

## Integración: Envío de datos de Regal a Braze

Esta sección describe cómo obtener eventos de informes Regal como `SMS.sent` y `call.completed` en Braze para que aparezcan en sus perfiles Braze y estén disponibles en la herramienta de segmentación Braze, Canvas y campañas. Esta integración utiliza Regal Reporting Webhooks y Braze Data Transformation para automatizar el flujo de datos.

### Paso 1: Crear una transformación de datos en Braze

{% alert important %}
La transformación de datos se encuentra actualmente en fase de acceso anticipado. Póngase en contacto con su gestor de éxito de clientes de Braze si está interesado en participar en el acceso anticipado.
{% endalert %}

Braze recomienda crear una transformación por el webhook Regal que planea enviar a Braze. 

Para crear una Transformación de Datos:
1. Vaya a la página **Transformaciones** del panel de control de Braze.
2. Dale un nombre a tu transformación y haz clic en **Crear transformación**.
3. En la lista de transformaciones, haga clic en <i class="fa-solid fa-ellipsis-vertical" title="Ver acciones"></i> y seleccione **Copiar URL de webhook**.

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### Paso 2: Habilitar webhooks de informes en Regal

Para configurar webhooks de informes:
1. Ve a la aplicación Regal y abre la página de **Configuración**.

2. En la sección **Reporting Webhooks**, haga clic en **Create Webhooks**.

3. En la entrada del punto final del webhook, añade la URL del webhook de Transformación de Datos Braze para la Transformación de Datos asociada.

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### Actualización de un punto final
Cuando editas un punto final, la caché puede tardar hasta 5 minutos en actualizarse y enviar eventos a tu nuevo punto final en su lugar.
#### Reintentos
Actualmente, no hay reintentos en estos eventos. Si no se recibe una respuesta en 5 segundos, el evento se abandona y no se vuelve a intentar. Regal añadirá reintentos en una futura versión.
#### Eventos
[La guía de Webhooks de Reporting](https://developer.regal.io/docs/reporting-webhooks#events) de Regal incluye la lista completa de eventos de Reporting que publican. Allí puedes ver definiciones de propiedades y también ejemplos de cargas útiles.

### Paso 3: Transforme los eventos Regal en eventos Braze

La característica [Transformación de datos]({{site.baseurl}}/data_transformation) Braze te permite mapear los eventos Regal entrantes en el formato necesario para añadirlos como atributos, eventos o compras en Braze.

1. Asigne un nombre a su transformación de datos. Se recomienda configurar una Transformación de Datos por webhook de evento.

2. Para probar la conexión, cree una llamada saliente desde el Escritorio del Agente Regal a su teléfono móvil y envíe el formulario de Resumen de Conversación para crear un evento call.completed.

3. Determine qué identificadores utilizará para asignar sus contactos Regal a sus perfiles Braze. Los identificadores disponibles en los eventos Regal incluyen:
   - `userId` - sólo se activa en eventos si previamente se ha enviado este identificador para un contacto
   - `traits.phone`
   - `traits.email` - sólo se activa en eventos si previamente se ha enviado este identificador para un contacto

#### Identificadores soportados por Braze
- Braze no admite números de teléfono como identificador. Para utilizarlo como identificador, el número de teléfono puede configurarse como [alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) en Braze.
- Al utilizar la transformación de datos Braze, la dirección de correo electrónico puede utilizarse como identificador. Si la dirección de correo electrónico existe como perfil en Braze, se actualizará el perfil existente. Si la dirección de correo electrónico aún no existe en Braze, se creará un perfil sólo para correo electrónico.

## Casos prácticos

{% tabs %}
{% tab Desencadenar un correo electrónico %}

**Activar un correo electrónico de Braze basado en una disposición de llamada en Regal**

A continuación se muestra un ejemplo de carga útil para un evento `call.completed` en Regal. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de transformación de datos para asignar esto a un evento personalizado en Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Actualizar los atributos del perfil %}

**Actualiza los atributos del perfil en Braze basándote en los eventos de `contact.attribute.edited` desde Regal.**

A continuación se muestra un ejemplo de carga útil para un evento `contact.attribute.edited` en Regal. Este evento se dispara cada vez que uno de tus agentes se entera de algo nuevo en una conversación y actualiza un atributo en el perfil del contacto.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de transformación de datos para asignar los nuevos valores de propiedades personalizadas a los atributos pertinentes de sus perfiles Braze:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Sincronice sus experimentos %}

**Mantén sincronizados tus experimentos en Braze y Regal mediante eventos `contact.experiment.assigned` **

A continuación se muestra un ejemplo de carga útil para un evento `contact.experiment.assigned` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de transformación de datos para asignar esto a un evento personalizado en Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Cancelar la suscripción de un contacto %}

**Cancelar suscripción de un contacto en Braze basado en un `contact.unsubscribed` de Regal**

A continuación se muestra un ejemplo de carga útil para un evento `contact.unsubscribed` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de transformación de datos para dar de baja el contacto en Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

