---
nav_title: Dixa
article_title: Dixa
description: "Este artículo describe la asociación entre Braze y Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) es una plataforma de servicio al cliente diseñada para mejorar las experiencias de asistencia unificando canales de comunicación como el chat, el correo electrónico, el teléfono y las redes sociales en una única interfaz. Ayuda a las empresas a mejorar la satisfacción del cliente y la eficiencia mediante el enrutamiento inteligente, la automatización y la información sobre el rendimiento en tiempo real.

La integración de Braze y Dixa ofrece una mejor visión de todos tus usuarios, proporcionando a los agentes de atención al cliente datos Braze en tiempo real.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta Dixa        | Se necesita una cuenta de administrador Dixa para beneficiarse de esta asociación.                                                                                           |
| Una clave de API REST Braze  | Una clave de API REST Braze con permisos `users.export.ids` y `email.status`.<br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

Supervisa los datos de Braze en la vista de agente de servicio al cliente mientras te comunicas con tus usuarios en diferentes canales de comunicación, como correo electrónico, mensajería o chat.

## Integración

Debes ser administrador de Dixa para configurar integraciones dentro de Dixa. Para la integración Braze, en Dixa, ve a **Configuración** > **Integraciones** > **Braze**.

![]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Paso 1: Crea la integración en Dixa

En la página **Crear widget de Braze**, rellena los siguientes campos obligatorios para crear la integración:

- **Nombre del widget:** Este es el nombre de la integración que se utilizará posteriormente en la barra lateral de conversación como título.
- **URL DE LA API:** Esta es la URL del punto final de la API REST de Braze para tu instancia.
- **Clave de API:** Esta es la clave de API de Braze que creaste en los requisitos previos.

### Paso 2: Configura la integración

A continuación, configura la integración de Braze y Dixa. Elige entre las siguientes opciones para ajustar la vista del widget Braze en la barra lateral de conversación.

#### Mostrar el widget en la barra lateral de conversación

Esta configuración muestra u oculta toda la integración dentro de la barra lateral de conversación en Dixa. 

Si estás configurando activamente la integración, te recomendamos que desactives esta opción mientras rellenas los campos obligatorios. Cuando hayas terminado de configurarlo, puedes volver a activarlo y los agentes de Dixa podrán utilizar la integración.

#### Mostrar datos del cliente

Elige mostrar u ocultar los datos del usuario. Los detalles contienen datos sobre ubicación, correo electrónico, número de teléfono, estado de suscripción por correo electrónico, estado de suscripción por notificación push y duración de la suscripción en Braze. 

#### Mostrar el botón para cambiar el estado de suscripción al correo electrónico

Los botones se basan en uno de los tres estados de suscripción de Braze: `subscribed`, `opted-in` y `unsubscribed`. Si un usuario es `subscribed`, el agente puede elegir entre `opt-in` o `unsubscribe`. Cuando un usuario es `opted-in` o `unsubscribed`, sólo es posible cambiar entre los dos.

#### Mostrar una lista de atributos personalizados

Elige mostrar u ocultar los atributos personalizados Braze del usuario.

#### Mostrar una lista de eventos personalizados

Elige mostrar u ocultar los eventos personalizados Braze del usuario.

#### Mostrar una lista de compras

Elige mostrar u ocultar una lista de productos comprados por el usuario. Aquí puedes ver cuántas veces se ha comprado. Para ver la primera y la última fecha de compra, pasa el ratón por encima del artículo. 

### Ejemplo de integración

A continuación se muestra un ejemplo de integración:

![La integración de Braze y Dixa en Dixa que muestra el estado de suscripción por correo electrónico, los atributos personalizados, los eventos personalizados y las compras de un usuario.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

