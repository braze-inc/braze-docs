---
nav_title: "Grupos de suscripción"
article_title: Grupos de suscripción de WhatsApp
page_order: 1
description: "En este artículo se describen los grupos de suscripción de WhatsApp, qué estados de suscripción se ofrecen y cómo se configuran los grupos de suscripción."
page_type: reference
channel:
  - WhatsApp
 
---

# Grupos de suscripción

> Los grupos de suscripción de WhatsApp se crean al integrar WhatsApp con su aplicación a través del **Portal de Socios Tecnológicos**.

## Estados de suscripción a WhatsApp

Existen dos estados de suscripción para los usuarios de WhatsApp: `subscribed` y `unsubscribed`.

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario ha confirmado explícitamente que desea recibir mensajes de WhatsApp de una empresa concreta. Los usuarios pueden suscribirse actualizando su estado de suscripción a través de la API de suscripción Braze o desplegando una estrategia de opt-in, según las directrices de WhatsApp. |
| No suscrito | El usuario no ha dado explícitamente su consentimiento para la adhesión voluntaria o se ha eliminado explícitamente su estado de adhesión voluntaria. <br><br> Los usuarios que se den de baja de un grupo de suscripción de WhatsApp dejarán de recibir mensajes de WhatsApp de los números de teléfono remitentes que pertenezcan al grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Cómo configurar los grupos de suscripción de WhatsApp de los usuarios

- **API REST:** Los perfiles de usuario se pueden configurar mediante programación en el [punto final`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) utilizando la API REST de Braze.
- **SDK Web:** Los usuarios pueden añadirse a un grupo de suscripción por correo electrónico, SMS o WhatsApp utilizando el método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importación de usuarios**: Los usuarios pueden añadirse a grupos de suscripción por correo electrónico o SMS mediante **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debe tener estas dos columnas en su CSV: `subscription_group_id` y `subscription_state`. Consulte [Importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para obtener más información.

### Cómo comprobar el grupo de suscripción de WhatsApp de un usuario

- **Perfil del usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel Braze desde **Audiencia** > **Buscar usuarios**. Aquí puede buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Cuando estás dentro del perfil de un usuario, en la pestaña **Compromiso**, puedes ver el grupo de suscripción de WhatsApp de un usuario y su estado.

- **API REST:** Los perfiles de usuario individuales del grupo de suscripción pueden verse mediante el [punto final Listar]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) [grupos de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o el [punto final Listar estado del grupo de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) utilizando la API REST de Braze. 

## Proceso de adhesión voluntaria y exclusión voluntaria de WhatsApp

Actualmente, los usuarios pueden suscribirse y darse de [alta o baja]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) en la mensajería de WhatsApp de varias formas, como [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), a través de un sitio web, un hilo de WhatsApp, por teléfono o en persona. Ten en cuenta que la adhesión voluntaria es obligatoria.

Actualmente no se admiten palabras clave de suscripción para el canal WhatsApp, por lo que dependerá de usted mantener una lista de usuarios. WhatsApp tiene un enfoque retrospectivo para los opt-ins y los límites de tarifa, donde si los usuarios empiezan a reportarte o bloquearte, tu límite de tarifa se reducirá. 

## Actualizar el estado de suscripción de un usuario a un Canvas de WhatsApp {#update-subscription-status}

Independientemente de los métodos de adhesión voluntaria y de cancelación que utilices, puedes actualizar el estado de suscripción de los perfiles de usuario con uno de los siguientes métodos de actualización:

- Cree un [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) que actualice el estado de la suscripción a través de REST API, como en el ejemplo siguiente:

![Webhook compositor de un mensaje utilizando el método POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Para evitar condiciones de carrera, cualquier mensaje de seguimiento después del webhook debe estar contenido en un segundo Canvas que se active por los resultados del primer Canvas (como que un usuario haya entrado en una variación del Canvas y esté en un grupo de suscripción de WhatsApp).

- Utilice el editor JSON avanzado para actualizar el perfil de usuario con la siguiente plantilla: 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Paso de actualización de usuario con un paso avanzado de editor JSON.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
La actualización del estado de suscripción de un usuario puede tardar hasta 60 segundos.
{% endalert %}

