---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Este artículo de referencia describe la asociación entre Braze y Lob.com, que te permite enviar cartas, postales y cheques por correo directo."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) es un servicio online que te permite enviar correo directo a tus usuarios.

_Esta integración está mantenida por Lob._

## Sobre la integración

Con esta integración, puedes:

- Envía cartas, postales y cheques por correo utilizando los webhooks Braze y la API Lob.
- Comparte eventos de Lob con Braze como atributos y eventos personalizados utilizando la Transformación de Datos Braze y los webhooks de Lob.

## Requisitos previos

|Requisito| Descripción|
| ---| ---|
|Cuenta Lob | Se necesita una cuenta Lob para beneficiarse de esta asociación. |
| Clave de API Lob | Tu clave de API de Lob se encuentra en la sección de configuración, debajo de tu nombre, en el panel de Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Enviar correo utilizando webhooks Braze

### Paso 1: Elige un punto final Lob

Dependiendo de lo que quieras hacer en Lob, tendrás que utilizar el punto final correspondiente en la petición HTTP de tu webhook. Para obtener información detallada sobre cada punto final, consulta [la documentación de referencia de la API de Lob](https://lob.com/docs#intro).

| URL base | Puntos finales disponibles |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 2: Cree su plantilla de webhook Braze

Para crear una plantilla de webhook Lob para utilizarla en futuras campañas o Lienzos, ve a **Plantillas** > **Plantillas de webhook** en el panel de Braze. 

Si quieres hacer una campaña Lob webhook única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla Webhook, rellena los siguientes campos:

- **URL del webhook**: `<LOB_API_ENDPOINT>`
- **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Lob requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**, debes sustituir el `<LOB_API_KEY>` por tu clave API Lob. Esta clave debe incluir un ":" justo después de la clave y estar codificada en base 64. 

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: Básica `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Código del cuerpo de la solicitud y URL del webhook mostrados en la pestaña de composición del constructor de webhook Braze.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Cuerpo de la solicitud

A continuación se muestra un ejemplo de cuerpo de solicitud para el punto final de postales Lob. Aunque este cuerpo de solicitud se proporciona en la plantilla base Lob de Braze, si deseas utilizar otros puntos finales, deberás ajustar tus campos Liquid en consecuencia.

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### Paso 3: Vista previa de su solicitud

En este punto, tu campaña debería estar lista para probarla y enviarla. Comprueba el panel de Lob y los registros de mensajes de error de la consola para desarrolladores Braze si te encuentras con errores. Por ejemplo, el siguiente error fue causado por una cabecera de autenticación formateada incorrectamente. 

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

![Un registro de mensajes de error que muestra la hora, el nombre de la aplicación, el canal y el mensaje de error. El mensaje de error incluye la alerta de mensaje y el código de estado.]({% image_buster /assets/img_archive/error_log.png %})

## Compartir eventos mediante webhooks Lob 

[La Transformación de Datos Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview) te permite crear y administrar webhooks para automatizar el flujo de datos desde plataformas externas a Braze. A cada transformación se le asigna un punto final único, que otras plataformas pueden utilizar como destino de su webhook.

{% alert important %}
La plantilla de Transformación de Datos de Lob envía eventos utilizando tu [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que consume puntos de datos en Braze. Te recomendamos que establezcas un límite de velocidad en la configuración de tu webhook de Lob, para evitar un consumo excesivo de datos.
{% endalert %}

### Paso 1: Crear una transformación en Braze

1. En el panel de Braze, ve a **Configuración de datos** > **Transformaciones de datos** y, a continuación, selecciona **Crear transformación**.
2. Introduce un nombre corto y descriptivo para tu transformación.
3. En **Editar experiencia**, selecciona **Utilizar una plantilla**, busca Lob y marca la casilla.
4. Cuando hayas terminado, selecciona **Crear transformación**. Se te redirigirá al editor de transformaciones, que utilizarás en el siguiente paso.

### Paso 2: Rellena la plantilla Lob

Con esta plantilla, puedes transformar uno de tus eventos Lob en un evento personalizado o atributo que pueda utilizarse en Braze. Sigue los comentarios en línea para terminar de construir la plantilla.

{% alert tip %}
Para obtener información detallada sobre la estructura de la carga útil de los webhooks de Lob, consulta [Lob: Uso de webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Paso 3: Crear un webhook en Lob

1. Cuando hayas terminado de crear tu plantilla, selecciona **Activar** y, a continuación, copia la **URL del webhook** en el portapapeles.
2. En Lob, [crea un nuevo webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1) y utiliza la URL de tu webhook de Braze para recibir el webhook.
