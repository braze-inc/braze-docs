---
nav_title: Dixa
article_title: Dixa
description: "Este artículo describe la asociación entre Braze y Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) es una plataforma de atención al cliente diseñada para mejorar las experiencias de soporte unificando canales de comunicación como el chat, el correo electrónico, el teléfono y las redes sociales en una única interfaz. Ayuda a las empresas a mejorar la satisfacción del cliente y la eficiencia mediante el enrutamiento inteligente, la automatización y la información sobre el rendimiento en tiempo real.

La integración de Braze y Dixa ofrece una mejor visión de todos tus usuarios, proporcionando a los agentes de atención al cliente datos de Braze en tiempo real.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta de Dixa        | Se necesita una cuenta de administrador de Dixa para beneficiarse de esta asociación.                                                                                           |
| Una clave de API REST de Braze  | Una clave de API REST de Braze con permisos `users.export.ids` y `email.status`.<br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Un punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Muestra los datos de Braze en la vista del agente de atención al cliente mientras te comunicas con tus usuarios en diferentes canales de comunicación, como correo electrónico, Messenger o chat. Además, utiliza la transformación de datos de Braze para enviar datos de Dixa a Braze y pausar el marketing mientras resuelves el problema de un usuario.

## Integración

Debes ser administrador de Dixa para configurar integraciones dentro de Dixa. Para la integración de Braze, en Dixa, ve a **Configuración** > **Integraciones** > **Braze**.

![La página Crear widget de Braze en Dixa donde introduces el nombre del widget, la URL de la API y la clave de API.]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Paso 1: Crea la integración en Dixa

En la página **Crear widget de Braze**, rellena los siguientes campos obligatorios para crear la integración:

- **Nombre del widget:** Este es el nombre de la integración que se utilizará posteriormente en la barra lateral de conversación como título.
- **URL de la API:** Esta es la URL del punto de conexión de la API REST de Braze para tu instancia.
- **Clave de API:** Esta es la clave de API de Braze que creaste en los requisitos previos.

### Paso 2: Configura la integración

A continuación, configura la integración de Braze y Dixa. Elige entre las siguientes opciones para ajustar la vista del widget de Braze en la barra lateral de conversación.

#### Mostrar el widget en la barra lateral de conversación

Esta configuración muestra u oculta toda la integración dentro de la barra lateral de conversación en Dixa. 

Si estás configurando activamente la integración, te recomendamos que desactives esta opción mientras rellenas los campos obligatorios. Cuando hayas terminado de configurar, puedes volver a activarla y los agentes de Dixa podrán utilizar la integración.

#### Mostrar datos del cliente

Elige mostrar u ocultar los datos del usuario. Los detalles contienen datos sobre ubicación, correo electrónico, número de teléfono, estado de suscripción por correo electrónico, estado de suscripción de notificación push y la duración de la membresía en Braze. 

#### Mostrar el botón para cambiar el estado de suscripción al correo electrónico

Los botones se basan en uno de los tres estados de suscripción de Braze: `subscribed`, `opted-in` y `unsubscribed`. Si un usuario es `subscribed`, el agente puede elegir entre `opt-in` o `unsubscribe`. Cuando un usuario es `opted-in` o `unsubscribed`, el agente solo puede alternar entre los dos.

#### Mostrar una lista de atributos personalizados

Elige mostrar u ocultar los atributos personalizados de Braze del usuario.

#### Mostrar una lista de eventos personalizados

Elige mostrar u ocultar los eventos personalizados de Braze del usuario.

#### Mostrar una lista de compras

Elige mostrar u ocultar una lista de productos que el usuario ha comprado. Aquí puedes ver cuántas veces compró el usuario el producto. Para ver la primera y la última fecha de compra, pasa el cursor por encima del artículo. 

### Ejemplo de integración

A continuación se muestra un ejemplo de la integración:

![La integración de Braze y Dixa en Dixa que muestra el estado de suscripción por correo electrónico de un usuario, atributos personalizados, eventos personalizados y compras.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## Herramienta de transformación de datos

Dixa utiliza webhooks para enviar datos a Braze. Debes ser administrador de Dixa para configurar webhooks.

El primer paso es crear una transformación de datos en Braze. 

1. Ve a **Configuración de datos** > **Transformaciones de datos** > **Crear transformación**.
2. Selecciona **Empezar desde cero**, selecciona el destino **POST: Track Users** y selecciona **Crear transformación**.
3. En el editor de transformación, copia el código de ejemplo de **Ejemplo de herramienta de transformación** a continuación e insértalo en el campo **Código de transformación**. Selecciona **Guardar**, copia la **URL del webhook** y abre Dixa.
4. En Dixa, ve a **Configuración** > **Integraciones** > **Webhooks** > **+ Webhook saliente**.
5. En la página de configuración del webhook, pega la URL de Braze y activa los eventos que quieras rastrear. **Conversación creada** es un buen punto de partida para rastrear las conversaciones de los clientes. 
6. Selecciona **Guardar** para finalizar la configuración de Dixa.

### Ejemplo de herramienta de transformación

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```
