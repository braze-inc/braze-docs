---
nav_title: Olo
article_title: Olo
description: "Este artículo describe la asociación entre Braze y Olo, una plataforma SaaS abierta líder para restaurantes que habilita la hostelería en todos los puntos de intervención."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) es una plataforma SaaS abierta líder para restaurantes que habilita la hostelería en cada punto de intervención.

Integrando Olo y Braze, puedes:

- Actualizar los perfiles de usuario en Braze para que sean coherentes con los perfiles de usuario de Olo.
- Envía la mejor mensajería de Braze basada en eventos de Olo

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Olo | Se requiere una cuenta de Olo con acceso a webhooks para aprovechar esta asociación. Configure suscripciones a webhooks a través de la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dentro del Panel de control de Olo. |
| Transformación de datos Braze | Se necesita una [URL de transformación de datos]({{site.baseurl}}/data_transformation/) para recibir datos de Olo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Un webhook es una forma de que Olo envíe información basada en eventos a Braze sobre los usuarios y sus acciones, incluidos eventos como Pedido realizado, Invitado optado, Pedido recogido y más. El Webhook de Olo entrega el evento a Braze generalmente a los pocos segundos de realizarse la acción.

## Descargo de responsabilidad

En Olo, estás limitado a un webhook por entorno para cada marca aprobada, todos enviados a la misma **URL de destino**. Las distintas marcas pueden tener URL diferentes, pero los eventos de una misma marca deben compartir una URL. En Braze, esto significa que sólo puedes hacer una transformación para usar con Olo.

Para manejar múltiples eventos Olo dentro de esta única transformación, busca la cabecera `X-Olo-Event-Type` en cada webhook. Esta cabecera te permite procesar condicionalmente diferentes eventos de Olo.

## Integración

### Paso 1: Configurar la transformación de datos Braze para aceptar el evento de prueba de Olo {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### Paso 2: Configurar los webhooks de Olo

Utiliza la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) del panel de control de Olo para configurar webhooks y enviarlos a tu transformación de datos.

1. Elija qué eventos deben enviarse a Braze
2. Configure la **URL de destino**. Esta será la URL de Transformación de Datos creada en [el paso 1](#step-1).

{% alert note %}
`OAuth` y el secreto compartido de la cabecera `X-Olo-Signature` no son necesarios para la transformación.
{% endalert %}

{:start="3"}
3\. Verifique que el webhook está configurado correctamente enviando un [Evento de Prueba](https://developer.olo.com/docs/load/webhooks#operation/test) a su Transformación de Datos. Sólo los usuarios de Olo Dashboard con el [permiso de Herramientas para Desarrolladores](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) pueden enviar Eventos de Prueba.

Olo requiere una respuesta exitosa del webhook Evento de Prueba antes de que puedas completar el proceso de configuración del webhook de Olo.

### Paso 3: Escribir código de transformación para aceptar los eventos Olo elegidos

En este paso, transformará la carga útil del webhook que se enviará desde la plataforma de origen en un valor de retorno de objeto JavaScript.

1. Envía una solicitud a tu URL de Transformación de Datos con una muestra de la carga útil de un evento Olo que pretendas soportar. Consulta el [formato del cuerpo de](#request-body-format) la solicitud para obtener ayuda sobre el formato de tu solicitud.
2. Actualice su Transformación de Datos y asegúrese de que puede ver la carga útil del evento de muestra en los **Detalles del Webhook**.
3. Actualiza tu código de transformación de datos para que sea compatible con los eventos Olo elegidos.
4. Haga clic en **Validar** para obtener una vista previa de la salida de su código y comprobar si se trata de una solicitud aceptable de `/users/track`.
5. Guarda y activa tu Transformación de Datos.

#### Formato del cuerpo de la solicitud

Este valor de retorno debe ajustarse al formato del cuerpo de la solicitud de Braze `/users/track`:

- El código de transformación se acepta en el lenguaje de programación JavaScript. Se admite cualquier flujo de control estándar de JavaScript, como la lógica if/else.
- El código de transformación accede al cuerpo de la petición del webhook a través de la variable payload. Esta variable es un objeto poblado por el análisis del cuerpo de la solicitud JSON.
- Se admite cualquier característica de nuestro punto final `/users/track`, incluidos:
    - Objetos de atributos de usuario, objetos de evento y objetos de compra
    - Atributos anidados y propiedades anidadas de eventos personalizados
    - Actualizaciones de grupos de suscripción
    - Dirección de correo electrónico como identificador

## Ejemplo de transformaciones de datos para webhooks Olo

Esta sección contiene plantillas de ejemplo que pueden utilizarse como punto de partida. Siéntase libre de empezar desde cero, o de eliminar componentes específicos como mejor le parezca.

En cada plantilla, el código define una variable, `brazecall`, para construir una solicitud `/users/track`.

Después de asignar la petición `/users/track `a `brazecall`, devolverás explícitamente `brazecall` para crear una salida.

### Transformación de un solo evento

Si sólo quieres admitir un único evento Olo, no necesitarás utilizar el encabezado `X-Olo-Event-Type` para crear condicionalmente la carga útil de solicitud `/users/track`. Por ejemplo, registrar un evento de compra o un evento personalizado en el perfil del usuario cuando se envía un webhook de Olo Order Placed a Braze.

### Registrar cada producto como una compra

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Registro de un evento personalizado

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformación multievento

Olo envía el tipo de evento dentro de la cabecera `X-Olo-Event-Type` de cada webhook. Para admitir varios eventos de webhook de Olo en una única transformación, utilice lógica condicional para transformar la carga útil del webhook en función del valor de este tipo de encabezado.  

En el siguiente ejemplo de transformación, nuestro JavaScript crea una carga útil particular para los eventos de `UserSignedUp` y `OrderPlaced`. Además, una condición `else` gestiona una carga útil para cualquier evento Olo enviado a Braze sin el encabezado X-Olo-Event-Type de `UserSignedUp` y `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Paso 4: Publica tu webhook Olo

Después de haber activado su transformación de datos en Braze, utilice la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) en el panel de control de Olo para publicar su webhook. Cuando el webhook es publicado, la Transformación de Datos comenzará a recibir mensajes de eventos webhook de Olo.

## Lo que hay que saber

### Reintentos

Olo reintentará las llamadas de webhook que resulten en un código de estado de respuesta HTTP de `429 - Too Many Requests` o en el rango `5xx` (por ejemplo, debido a un tiempo de espera de la puerta de enlace o a un error del servidor), hasta 50 veces en un periodo de 24 horas antes de abandonar la solicitud.

### Al menos una entrega

Si una llamada webhook resulta en un código de estado de respuesta HTTP de `429 - Too Many Requests` o en el rango `5xx` (por ejemplo, debido a un tiempo de espera de la puerta de enlace o a un error del servidor), Olo reintentará el mensaje hasta 50 veces en un período de 24 horas antes de rendirse.

Por lo tanto, un suscriptor puede recibir los webhooks varias veces. Depende del suscriptor ignorar los duplicados comprobando la cabecera `X-Olo-Message-Id`.


