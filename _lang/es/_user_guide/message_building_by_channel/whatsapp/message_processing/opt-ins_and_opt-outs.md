---
nav_title: Adhesiones voluntarias y cancelaciones
article_title: Adhesiones voluntarias y cancelaciones de WhatsApp
description: "Este artículo de referencia trata de los diferentes métodos de inclusión y exclusión de WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Adhesión voluntaria y cancelación

> La gestión de las altas y bajas de WhatsApp es crucial, ya que WhatsApp controla [la valoración de la calidad de tu número de teléfono](https://www.facebook.com/business/help/896873687365001), y las valoraciones bajas pueden hacer que se reduzcan tus límites de mensajes. <br><br>Una forma de construir una tasa de alta calidad es evitar que los usuarios bloqueen o denuncien tu negocio. Esto puede hacerse proporcionando [mensajes de alta calidad](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como valor para sus usuarios), controlando la frecuencia de los mensajes y permitiendo a los clientes optar por no recibir futuras comunicaciones. <br><br>Esta página explica cómo configurar las adhesiones voluntarias y las exclusiones voluntarias, y las diferencias entre los modificadores "regex" y "is".

Las adhesiones voluntarias pueden proceder de fuentes externas o de métodos Braze, como SMS o mensajes dentro de la aplicación y en el explorador. Las cancelaciones se pueden gestionar mediante palabras clave configuradas en Braze y botones de marketing de WhatsApp. Consulta los siguientes métodos para obtener orientación sobre la configuración de la adhesión voluntaria y la cancelación.

#### Métodos de inscripción
- [Métodos de opt-in externos a Braze](#external-to-braze-opt-in-methods)
  - [Lista de adhesión voluntaria creada externamente](#externally-built-opt-in-list)
  - [Mensaje saliente en el canal WhatsApp de atención al cliente](#outbound-message-in-customer-support-whatsapp-channel)
  - [Mensaje entrante de WhatsApp](#inbound-whatsapp-message)
- [Métodos de opt-in potenciados por Braze](#braze-powered-opt-in-methods)

#### Métodos de exclusión voluntaria
- [Palabras clave generales de exclusión](#general-opt-out-keywords)
- [Selección de la cancelación de marketing](#marketing-opt-out-selection)

## Configura adhesiones voluntarias para tu canal de WhatsApp Braze

Para las adhesiones voluntarias de WhatsApp, debes cumplir [los requisitos de WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). También deberá facilitar a Braze la siguiente información:
- Un `external_id`, un [número de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) y un estado de suscripción actualizado para cada usuario. Esto puede hacerse utilizando el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) o a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el número de teléfono y el estado de la suscripción.

{% alert note %}
Braze ha publicado una mejora en el punto final `/users/track` que permite actualizar el estado de la suscripción que puede conocer en [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). Sin embargo, si ya has creado protocolos de adhesión voluntaria utilizando el [punto final `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), puedes seguir haciéndolo allí.
{% endalert %}

### Métodos de opt-in externos a Braze

Su aplicación o sitio web (registro de cuenta, página de pago, configuración de cuenta, terminal de tarjeta de crédito) a Braze.

Si ya dispone de un consentimiento de marketing para el correo electrónico o los mensajes de texto, incluya una sección adicional para WhatsApp. Cuando un usuario se registra, necesita una dirección `external_id`, un [número de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) y un estado de suscripción actualizado. Para ello, dependiendo de cómo esté configurada tu instalación de Braze, aprovecha el [punto final `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) o utiliza el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de adhesión voluntaria creada externamente

Si ha utilizado WhatsApp anteriormente, es posible que ya haya creado una lista de usuarios con opt-ins según los requisitos de WhatsApp. En este caso, cargue un CSV o utilice la API con la [siguiente información]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) en Braze.

#### Mensaje saliente en el canal WhatsApp de atención al cliente

En su canal de atención al cliente, haga un seguimiento de los problemas resueltos con un mensaje automático en el que se les pregunte si desean recibir mensajes de marketing. La funcionalidad aquí depende de la disponibilidad de funciones en la herramienta de atención al cliente de su elección y de dónde guarde la información del usuario.

1. Proporcione un [enlace de mensaje](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) desde su número de teléfono de WhatsApp Business.
2. Proporcionar [acciones de respuesta rápida]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) en las que el cliente responda "Sí" para indicar su adhesión voluntaria.
3. Configurar disparador de palabras clave personalizado.
4. Para cualquiera de esas ideas, probablemente necesitarás terminar el camino con lo siguiente:
	- Llama al [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar o crear un usuario
	- Aprovecha el [punto final `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) o utiliza el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Mensaje entrante de WhatsApp 

Haga que los clientes envíen un mensaje entrante al número de WhatsApp.

Esto puede configurarse como un Canvas o una campaña, dependiendo de si desea que el usuario reciba un mensaje de confirmación en el nuevo canal.

1. Cree una campaña con el desencadenante de entrega basado en la acción de un mensaje entrante.
2. Crea una campaña webhook. Para ver un ejemplo de webhook, consulte [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Ten en cuenta que puedes crear una URL o un código QR para unirte a un canal de WhatsApp desde el [gestor de WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/), en **Número de teléfono** > **Enlaces de mensajes**.<br>![Compositor del código QR de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de opt-in potenciados por Braze 

#### Mensaje SMS

En Canvas, configure una campaña que pregunte a los clientes si desean optar por recibir mensajes de WhatsApp utilizando uno de los siguientes métodos:
- Segmento de clientes: grupo de marketing suscrito fuera de EE. UU.
- Configuración personalizada del activador de palabras clave

Obtenga información sobre cómo actualizar el estado de suscripción de los perfiles de usuario consultando [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### Mensaje en la aplicación o en el navegador

Cree un mensaje en la aplicación o una ventana emergente en el navegador para pedir a los clientes que acepten utilizar WhatsApp.

Utiliza [mensajes HTML dentro de la aplicación](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) con [un "puente" JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) para interactuar con el SDK Braze. Asegúrate de utilizar el ID del grupo de suscripción de WhatsApp. 

#### Formulario de captura de números de teléfono

Utilice la plantilla de [formulario de captura de números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) en el editor de arrastrar y soltar para mensajes in-app para recopilar números de teléfono de usuarios y hacer crecer sus grupos de suscripción de WhatsApp.

## Configure las exclusiones voluntarias para su canal de WhatsApp Braze

### Palabras clave generales de exclusión

Puedes configurar una campaña o Canvas que permita a los usuarios que envíen mensajes con determinadas palabras excluirse de futuros mensajes. Los Canvas pueden ser especialmente beneficiosos, ya que te permiten incluir un mensaje de seguimiento que confirme el éxito de la adhesión voluntaria. 

#### Paso 1: Crear un lienzo con el desencadenante "Mensaje de WhatsApp entrante"
 
![Paso en Canvas basado en acciones que da entrada a los usuarios que envían un mensaje entrante de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Cuando selecciones palabras clave desencadenantes, incluye palabras como "Detener" o "Sin mensaje". Si eliges este método, asegúrate de que tus clientes conocen tus palabras de cancelación. Por ejemplo, después de recibir la adhesión voluntaria inicial, incluye una respuesta de seguimiento como "Para cancelar estos mensajes, envía el mensaje "Detener" en cualquier momento". 

![Paso de mensaje para enviar un mensaje entrante de WhatsApp en el que el cuerpo del mensaje es "STOP" o "SIN MENSAJE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Paso 2: Actualizar el perfil del usuario

Actualice el perfil del usuario utilizando uno de los métodos descritos en [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Selección de la cancelación de marketing

Dentro del creador de plantillas de mensajes de WhatsApp, puedes incluir la opción de "exclusión de marketing". Cada vez que incluya esto, asegúrese de que la plantilla se utiliza en un Canvas con un paso posterior para un cambio de grupo de suscripción. 

1. Cree una plantilla de mensaje con la respuesta rápida "marketing opt-out".<br>![Plantilla de mensaje con una opción de pie de página de "Exclusión voluntaria de marketing"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Sección para configurar un botón de salida de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crea un Canvas que utilice esta plantilla de mensaje.<br><br>
3. Sigue los pasos del ejemplo anterior pero con el texto desencadenante "DETENER PROMOCIONES".<br><br>
4. Actualice el estado de suscripción del usuario utilizando uno de los métodos descritos en [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Establecer flujos de trabajo de inclusión y exclusión voluntarias

Puede configurar flujos de trabajo de respuesta de palabra clave "START" y "STOP" para WhatsApp con estos dos métodos:

- [Paso de actualización de usuario](#user-update-step)
- [Campaña Webhook para activar una segunda campaña WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Paso de actualización de usuario

El [paso Actualizar usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) puede añadir el número de teléfono del usuario al grupo de suscripción de WhatsApp cuando el usuario envía una palabra clave al número de teléfono del grupo de suscripción.

El paso Actualización de usuario evita condiciones de carrera porque el usuario no avanzará al siguiente paso en el Canvas antes de que su número de teléfono se añada al grupo de suscripción. También tiene menos pasos de configuración que los otros métodos, por lo que Braze suele recomendar este método.

1. Crea un Canvas con el paso basado en acciones **Enviar un mensaje entrante de WhatsApp**. Seleccione **Donde el cuerpo del mensaje** e introduzca "START" para **Is.**

{% alert important %}
Para los mensajes "STOP", invierta el paso del mensaje que confirma la exclusión y el paso de actualización del usuario. Si no lo hace, el usuario será excluido primero del grupo de suscripción y después no podrá recibir el mensaje de confirmación.
{% endalert %}

![Paso de un mensaje de WhatsApp en el que el cuerpo del mensaje es "INICIO".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. En el Lienzo, cree un paso **Configurar Actualización de Usuario** y para **Acción** seleccione **Editor JSON Avanzado**. <br><br>![Paso de actualización de usuario con una acción de "Editor JSON avanzado".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. Rellene el **objeto Actualización de usuario** con la siguiente carga útil JSON, sustituyendo `XXXXXXXXXXX` por el ID de su grupo de suscripción:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\. Añade un paso de mensaje de WhatsApp posterior. <br><br>![Paso de actualización de usuario en Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Consideraciones

La actualización puede completarse a velocidades variables porque Braze agrupa por lotes las solicitudes de [pasos de actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

### Campaña Webhook para activar una segunda campaña WhatsApp

Una campaña Webhook puede activar la entrada en una segunda campaña después de añadir el número de teléfono del usuario al grupo de suscripción de WhatsApp cuando el usuario envía una palabra clave al número de teléfono del grupo de suscripción.

{% alert important %}
No es necesario utilizar este método para los mensajes STOP. El mensaje de confirmación se enviará antes de que el usuario se elimine del grupo de suscripción, por lo que puede utilizar uno de los otros dos pasos.
{% endalert %}

1. Crear una campaña o Canvas con un paso basado en una acción **Enviar un mensaje entrante de WhatsApp**. Seleccione **Donde el cuerpo del mensaje** e introduzca "START" para **Is.**

![Paso de mensaje de WhatsApp en el que el cuerpo del mensaje es "INICIO".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. En la campaña o Canvas, crea un paso de Mensaje de webhook y cambia el **Cuerpo de la solicitud** a **Texto sin procesar**.

![Paso de mensaje para un webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Introduce la [URL del]({{site.baseurl}}/api/basics/) punto final del cliente en la **URL del Webhook**, seguida del enlace del punto final `campaigns/trigger/send`. Por ejemplo, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Campo URL del webhook en la sección "Componer webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. En el texto sin formato, introduzca la siguiente carga útil JSON y sustituya `XXXXXXXXXXX` por el ID de su grupo de suscripción. Tendrá que sustituir `campaign_id` después de crear su segunda campaña.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5\. Cree una campaña de WhatsApp (su segunda campaña) y establezca el activador en API. Asegúrese de copiar este `campaign_id` en la carga JSON de su primera campaña.

#### Consideraciones

- Las actualizaciones de atributos desde la carga JSON del activador de la API de Canvas aún no son compatibles, por lo que solo puede activar una campaña de WhatsApp para el mensaje de respuesta de WhatsApp (como en el paso 2).
- Una plantilla de WhatsApp debe estar aprobada para poder enviarla como mensaje de respuesta. Esto se debe a que una respuesta rápida requiere que el desencadenante del mensaje entrante esté dentro de la misma campaña o Canvas. Si utiliza un [paso de Actualización de usuario](#user-update-step), puede enviar un mensaje de respuesta rápida sin la aprobación de Meta.

## Comprender la diferencia entre los modificadores "regex" e "is

En esta tabla, `STOP` se utiliza como palabra desencadenante de ejemplo para demostrar cómo funcionan los modificadores.

| Modificador | Palabra desencadenante | Acción |
| --- | --- | --- |
| `Is` | `STOP` | Capta cualquier uso de "stop" en toda la palabra, independientemente del caso. Por ejemplo, esto capta "para" pero no "por favor, para". |
| `Matches regex` | `STOP` | Captura cualquier uso de "STOP" en ese caso. Por ejemplo, esto capta "detente" pero no "POR FAVOR, DETENTE". |
| `Matches regex` | `(?i)STOP(?-i)` | Captura cualquier uso de "STOP" en cualquier caso. Por ejemplo, esto capta "para", "por favor, para" y "nunca dejes de enviarme mensajes". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

