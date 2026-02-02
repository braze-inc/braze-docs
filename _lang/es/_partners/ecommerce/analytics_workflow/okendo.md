---
nav_title: Okendo
article_title: "Okendo"
description: "Aprende a integrar Okendo con Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) es una plataforma unificada de marketing del cliente que proporciona herramientas para cultivar la promoción, ampliar el boca a boca y maximizar el valor de duración para movilizar a tus clientes y conseguir un crecimiento más rápido y eficiente.

*Esta integración está mantenida por Okendo.*

## Sobre la integración

La integración de Braze con Okendo funciona en múltiples productos de la plataforma de Okendo, incluyendo Opiniones, Fidelización, Referidos, Encuestas y Cuestionarios. Okendo envía eventos personalizados y atributos del usuario a Braze, que pueden utilizarse para personalizar y desencadenar mensajes.  

## Requisitos previos

| Requisito            | Descripción                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Cuenta Okendo         | Se necesita una cuenta Okendo para beneficiarse de esta asociación.        |
| Clave de API REST de Braze     | Una clave de API REST de Braze con permisos `users.track`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze    | [La URL de tu punto final REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Configuración del conector Braze en Okendo

1. En Okendo, ve a **Configuración** > **Integraciones** > **Correo electrónico & SMS** > **Braze**
2. Añade el punto final de la API y la clave de API a la configuración de **integración**.

### Paso 2: Configura tu identificador

El campo `external_id` se utiliza para identificar al usuario asociado a cada suceso. Alterna en **Usar el ID de cliente de Shopify para la identificación del usuario de Braze** para asociar el campo con los ID de cliente de Shopify. Si no, altérnalo para asociarlo a la dirección de correo electrónico de cada usuario.

## Sincronización de eventos y atributos de Okendo con Braze

### Eventos personalizados

{% alert note %}
Para ver ejemplos de datos de eventos, consulta [la documentación de Okendo.](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)
{% endalert %}

#### Eventos de revisión

- Revisión de Okendo Creada
- Solicitud de revisión Okendo

#### Actos referidos

- Enviado Okendo Referidos
- Adhesión voluntaria a Okendo Referidos
- Invitación a referidos Okendo
- Recibido el cupón de referidos de Okendo
- Cupón de referidos Okendo canjeado
- Okendo Referidos Rechazados

#### Actos de fidelización

- Inscrito en Okendo Fidelización
- Puntos de fidelización Okendo concedidos
- Puntos de fidelización Okendo canjeados
- Cambio del nivel de fidelización de Okendo
- Puntos de fidelización Okendo Adjusted

#### Cuestionario

- Encuesta enviada a Okendo

#### Concurso

- Presentado Okendo Quiz

### Atributos personalizados

Okendo envía datos de perfil de usuario como atributos personalizados en Braze, que pueden utilizarse para crear segmentos de audiencia. Algunos ejemplos son:

- Preguntas de perfil realizadas en cuestionarios y durante el envío de una revisión, como la edad, la fecha de nacimiento, el tipo de piel y el color del pelo.
- Métricas de revisión como _la tasa media de revisión_ y el _sentimiento medio de revisión_.
- Métricas de fidelización como _Saldo de Puntos_ y _Nivel VIP_
- Métricas de referidos, como el _número de referidos con éxito_ y los _ingresos totales por referidos_.  
- Puntuación NPS obtenida de un cuestionario

## Utilizar Braze con productos Okendo

Dependiendo del producto Okendo, deberás completar pasos adicionales para utilizar Braze y Okendo juntos. Consulta los siguientes artículos para más detalles:

- [Integración de Reseñas con Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integración de la fidelización con Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integración de referidos con Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integración de cuestionarios con Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integración de cuestionarios con Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Si necesitas ayuda para configurar la integración, ponte en contacto con el equipo de soporte de Okendo.
{% endalert %}
