---
nav_title: Front
article_title: Front
description: "Aprende a integrar Front con Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> La integración de Front te habilita para aprovechar la transformación de datos Braze y los webhooks de cada plataforma para establecer un canal SMS conversacional bidireccional.

El webhook entrante de Front contendrá una carga útil que incluye el mensaje enviado por el agente en vivo. Será necesario reformatear la solicitud antes de que pueda ser aceptada por los puntos finales de Braze. La plantilla Front Data Transformation reformateará la carga útil y escribirá un evento personalizado en el perfil de usuario titulado **SMS saliente enviado,** pasando el cuerpo del mensaje como una propiedad del evento.

Antes de configurar una nueva transformación en Braze, recomendamos revisar la matriz de soporte para cada nivel en nuestra documentación de [Transformación de Datos]({{site.baseurl}}/user_guide/data/data_transformation/overview/). Nuestros niveles Free y Pro ofrecen un número diferente de transformaciones activas y solicitudes entrantes al mes. Confirma que el plan actual en el que estás puede admitir tu caso práctico.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo             | Descripción                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta de Front            | Se necesita una cuenta Front para beneficiarse de esta asociación.|
| URL Webhook de Transformación de datos Braze | [La Transformación de Datos Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/) se utilizará para reformatear el webhook entrante desde Front, de modo que pueda ser aceptado por el punto final Braze /users/track.|
| Una clave de API REST de Front         | Se utilizará una clave de API REST de Front para realizar una solicitud de webhook saliente de Braze a Front. |

## Ejemplos

- Agiliza tu proceso de generación de clientes potenciales utilizando la mensajería SMS automatizada Braze para identificar las preferencias de los usuarios y habilitar a los agentes de ventas en vivo para que realicen el seguimiento y cierren las ventas.
- Reactiva a los clientes que abandonaron sus carritos de la compra, impulsando las conversiones de ventas mediante respuestas automatizadas por SMS y asistencia por chat en vivo.

## Integración de Front

### Paso 1: Crear una transformación de datos

Primero, crearás una nueva transformación de datos en Braze. Los pasos siguientes son simplificados; para un recorrido completo, consulta [Crear una transformación]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

1. En Braze, ve a **Configuración de datos** > **Transformaciones de datos** y, a continuación, selecciona **Crear transformación**.
2. En **Editar experiencia**, selecciona **Empezar de cero**.
3. En **Seleccionar destino**, selecciona **POST: Seguimiento de usuarios**.
4. Copia y pega la siguiente plantilla de transformación, luego guárdala y activa el punto final.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Tu transformación debe ser similar a la siguiente

    ![Un ejemplo de transformación de datos.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
Puedes modificar esta plantilla para adaptarla a tus necesidades específicas. Por ejemplo, puedes personalizar el nombre preestablecido del evento personalizado. Para más información, consulta [Resumen de la transformación de datos]({{site.baseurl}}/user_guide/data/data_transformation/overview/).
{% endalert %}

### Paso 2: Crear una campaña de SMS salientes

A continuación, crearás una campaña de SMS que escuchará los webhooks de Front y dará una respuesta personalizada por SMS a tus clientes.

#### Paso 2.1: Redacta tu mensaje

En el cuadro de texto **Mensaje**, añade el siguiente código Liquid, junto con cualquier idioma de exclusión u otro contenido estático.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Tu mensaje debe ser similar al siguiente:

![Un mensaje de ejemplo utilizando código Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Programar la entrega

Para el tipo de entrega, selecciona **Entrega basada en acciones**; a continuación, para el desencadenante del evento personalizado, selecciona **SMS salientes enviados**.

![La página "Programar entrega".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Este evento personalizado es la Transformación de Datos que escribe en el perfil del usuario. Los mensajes del agente se guardarán como una propiedad del evento en este evento.
{% endalert %}

Por último, en **Controles de entrega**, habilita la posibilidad de volver a ser elegible.

![Re-elegibilidad habilitada en "Controles de entrega".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Paso 3: Crear un canal personalizado

En el panel frontal, ve a **Configuración** > **Canales** > **Añadir canales** y, a continuación, selecciona **Canal personalizado** e introduce un nombre para tu nuevo canal Braze.

![Un canal personalizado para Braze en el panel frontal.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Paso 4: Configura los ajustes

En el campo del punto final de la API de salida, introduce la URL del webhook de transformación de datos [que creaste anteriormente](#step-1-set-up-a-data-transformation-in-braze). Todos los mensajes salientes de los agentes en vivo de tu nuevo canal Braze se enviarán aquí. Este canal también proporciona una URL de punto final para que Braze reenvíe los mensajes SMS en el campo **URL entrante**.

Toma nota de esta URL, la necesitarás más adelante.

![La configuración del canal para el canal Braze recién creado en Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Paso 5: Configurar el reenvío de SMS entrantes

A continuación, crearás dos nuevas campañas webhook en Braze para poder reenviar los SMS entrantes de los clientes al buzón de entrada de Front.

|Número|Propósito|
|---|---|
|Campaña webhook 1|Señala a Front que se está solicitando una conversación de chat en vivo.|
|Campaña webhook 2|Reenvía todas las respuestas SMS conversacionales enviadas por el cliente al buzón de entrada de Front.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Paso 5.1: Crear una categoría de palabras clave SMS

En el panel de Braze, ve a **Audiencia**, elige tu **grupo de suscripción a SMS** y, a continuación, selecciona **Añadir palabra clave personalizada**. Para crear una categoría de palabras clave SMS exclusiva para Front, rellena los siguientes campos.

|Campo|Descripción|
|---|---|
|Categoría de palabra clave|El nombre de tu categoría de palabras clave, como `FrontSMS1`.|
|Palabras claves|Tus palabras clave personalizadas, como `TIMETOMOW`. Evita las palabras comunes para evitar que se desencadenen accidentalmente. Ten en cuenta que las palabras clave no distinguen entre mayúsculas y minúsculas, por lo que `lawn` coincidiría con `LAWN`.|
|Mensaje de respuesta|El mensaje que se enviará cuando se detecte una palabra clave, como "Un paisajista se pondrá en contacto contigo en breve".|
{: .reset-td-br-1 .reset-td-br-2 }

![Un ejemplo de categoría de palabras clave SMS en Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Paso 5.2: Crea tu primera campaña webhook

En el panel de Braze, crea tu primera campaña webhook utilizando la URL [que creaste anteriormente](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Un ejemplo de la primera campaña webhook que debe crearse en Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Añade lo siguiente al cuerpo de tu solicitud:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

En la pestaña Configuración, configura tus encabezados de solicitud `Authorization`, `content-type` y `accept`.

![Un ejemplo de solicitud con los tres encabezados requeridos.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Paso 5.3: Programar la primera entrega

Para **Programar entrega**, selecciona **Entrega basada en acciones** y, a continuación, elige **Enviar un mensaje SMS entrante** para tu tipo de desencadenante. Añade también el grupo de suscripción SMS y la categoría de palabras clave que [configuraste anteriormente](#step-51-create-an-sms-keyword-category).

![La página "Programar entrega" de la primera campaña webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

En **Controles de entrega**, habilita la posibilidad de volver a ser elegible.

![Reelegibilidad seleccionada en "Controles de entrega" para la primera campaña webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Paso 5.4: Crea tu segunda campaña webhook

Como tu segunda campaña webhook coincidirá con la primera, puedes [duplicar la primera y cambiarle el nombre]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns). Puedes hacerlo ahora.

#### Paso 5.5: Programar la segunda entrega

Para **programar la entrega**, establece el **desencadenante basado en acciones** y el **grupo de suscripción** SMS igual que [en tu primera entrega](#step-53-schedule-the-first-delivery). Sin embargo, para la **categoría de palabras clave**, elige **Otros**.

![La página "Entrega programada" de la segunda campaña webhook, con "Otros" elegida como categoría de palabras clave.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Paso 5.6: Añadir un filtro de audiencia

Tu campaña webhook ahora puede reenviar las respuestas SMS entrantes de tus clientes. Para filtrar las respuestas SMS de modo que solo se reenvíen los mensajes de las charlas en vivo, añade el filtro de segmentación **Último mensaje recibido de una campaña específica** al **paso Audiencias objetivo**.

![Un filtro de audiencia con "Último mensaje recibido de una campaña específica" seleccionado.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Después configura tu filtro:

1. En **Campaña**, selecciona la campaña de SMS [que creaste anteriormente](#step-2-create-an-outbound-sms-campaign).
2. Para **Operador**, selecciona **Menor que**.
3. En **Ventana de tiempo**, elige el tiempo que debe permanecer abierto un chat sin respuesta del cliente.

![Los ajustes de configuración del filtro de audiencia seleccionado.]({% image_buster /assets/img/front/front_target_audience.png %})

## Consideraciones

### Segmentos facturables

- Los mensajes SMS en Braze se cobran por segmento del mensaje. Entender qué define un segmento y cómo se dividirán estos mensajes es clave para comprender cómo se te facturarán los mensajes. Consulta más información en nuestra [documentación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- Las respuestas largas de los agentes consumirán más segmentos facturables.

### Consumo de puntos de datos

Actualmente, esta integración requiere que se escriba un evento personalizado en un perfil de usuario cada vez que un agente en vivo envía un SMS desde Front. Esto puede ser adecuado para intercambios rápidos que solo duren un par de mensajes, pero a medida que las conversaciones se alargan también lo hacen las implicaciones de los puntos de datos. Se consume un punto de datos por cada evento personalizado registrado en Braze.

### Incluir enlaces en mensajes SMS

El envío de un enlace desde el chat en vivo de Front se mostrará con etiquetas HTML adicionales.

### Adjuntar archivo de imagen desde Front

Los archivos de imagen en Front no se mostrarán en los mensajes SMS enviados desde Braze.

### Adhesión voluntaria 

Los mensajes conversacionales tienen un mayor riesgo de contener la palabra "stop" o expresiones vernáculas similares que pueden reconocerse como exclusiones difusas.
