---
nav_title: "Anuncios que hacen clic en WhatsApp"
article_title: Anuncios que hacen clic en WhatsApp
page_order: 1
description: "Este artículo de referencia proporciona una guía paso a paso para configurar y utilizar Anuncios que hacen clic en WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Anuncios que hacen clic en WhatsApp

> Esta página proporciona una guía paso a paso para configurar y utilizar Ads That Click para WhatsApp, para que tú y tu equipo podáis elevar vuestro programa de WhatsApp.

Los anuncios que hacen clic en WhatsApp son una forma eficaz de atraer tanto a clientes nuevos como a los ya existentes a partir de Meta anuncios en Facebook, Instagram u otras plataformas. Utiliza estos anuncios para promocionar tus productos y servicios a la vez que haces que los usuarios conozcan tu presencia en WhatsApp.

\![Un anuncio de Facebook de Calorie Rocket que anuncia la entrega gratuita, y la conversación de WhatsApp correspondiente que se produce cuando un usuario selecciona el botón del anuncio.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configuración de anuncios que hacen clic en WhatsApp

1. En el administrador de Meta Ads, crea un anuncio en Facebook, Instagram u otras plataformas siguiendo la guía paso a paso [Cómo crear anuncios que hacen clic en WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **No** configures respuestas automatizadas; en su lugar, configurarás las respuestas en Braze.

\![Administrador de anuncios con un compositor para crear un anuncio de interacción.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Cuando configures el mensaje precargado, que el usuario enviará a tu cuenta de WhatsApp Business, incluye una palabra o frase específica que utilizarás para desencadenar una respuesta específica al anuncio concreto. En este ejemplo, una aplicación de entrega de comida utiliza "entrega gratuita" porque así se promociona en su anuncio. 

\![Compositor de plantillas del administrador de anuncios con un mensaje precargado de "Quiero entrega gratuita".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Deja claro en la descripción del anuncio que al hacer clic en él se iniciará una conversación con tu marca, utilizando frases como "Chatea ahora por WhatsApp".
{% endalert %}

{: start="2"}
2\. En Braze, configura un Canvas basado en acciones donde la opción basada en acciones sea **Enviar un mensaje entrante de WhatsApp** y el cuerpo del mensaje sea “YOUR_TRIGGER_WORD”.. En este ejemplo, una aplicación de entrega de comida está utilizando "entrega gratuita".

Programa de entrada para un Canvas de Braze basado en acciones, con el evento desencadenante "Enviar un mensaje entrante de WhatsApp" y un cuerpo de mensaje que coincide con el regex de "entrega gratuita".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\. Configura un mensaje de respuesta en el Canvas que se envíe inmediatamente después de que el cliente entre en el Canvas (por ejemplo, sin retraso). Aunque hacer clic en el anuncio constituye técnicamente una adhesión voluntaria, te recomendamos que configures tu mensaje de respuesta para preguntar al usuario si desea recibir futuros mensajes de marketing tuyos por WhatsApp. 

{% alert tip %}
Configura tu mensaje de respuesta con respuestas rápidas (como "Sí" o "No, gracias") para que los usuarios puedan indicar rápidamente si desean la adhesión voluntaria.
{% endalert %}

No olvides proporcionar también cualquier código de descuento, oferta u otra información prometida en el anuncio.

\![Creador de mensajes de WhatsApp con botones de respuesta "Sí" y "No, gracias".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

\![Paso en Canvas con un grupo de "Adhesión voluntaria" con un evento desencadenante de "Enviado WhatsApp entrante al grupo de suscripción" y una palabra desencadenante de "SÍ".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\. Consigue la adhesión voluntaria de los usuarios actualizando el estado de suscripción de los perfiles de usuario con uno de los siguientes métodos de actualización:
    \- Crea un webhook Braze to Braze que actualice el estado de la suscripción a través de la API REST.  
    \- Utiliza el editor JSON avanzado para actualizar el perfil de usuario con la plantilla para [actualizar el estado de suscripción de un usuario a un Canvas de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process).

\![Paso en Canvas de actualización de usuario que utiliza el editor JSON avanzado para actualizar el perfil de usuario.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

\![Canvas que muestra el flujo de trabajo para enviar Anuncios que hacen clic a WhatsApp, incluyendo tres rutas de acción: Adhesión voluntaria, exclusión voluntaria y todos los demás.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Consideraciones

Las conversaciones que se inician a partir de un anuncio que hace clic en WhatsApp son gratuitas si se cumplen las siguientes condiciones:

- Si un usuario te envía un mensaje a través de un [punto de entrada gratuito](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), como un anuncio que hace clic en WhatsApp, se abre una [ventana de servicio al cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) de 24 horas en la que puedes enviar a ese usuario cualquier tipo de mensaje.
- Si respondes dentro de la ventana de servicio al cliente (en 24 horas), se abre un punto de entrada libre durante 72 horas, y todos los mensajes dentro de la ventana de 72 horas serán gratuitos.
- La mensajería de respuesta es gratuita.