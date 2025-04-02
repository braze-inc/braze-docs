---
nav_title: "Grupos de suscripción de SMS"
article_title: Grupos de suscripción de SMS
page_order: 4
description: "Este artículo de referencia trata sobre los grupos de suscripción SMS, los estados de suscripción y el proceso de configuración de grupos de suscripción."
page_type: reference
channel:
  - SMS
  
---

# Grupos de suscripción SMS

> Los grupos de suscripción son la base para enviar SMS y MMS a través de Braze. Un grupo de suscripción es una colección de [números de teléfono de envío][2] (como códigos cortos, códigos largos y/o ID alfanuméricos de remitente) que se utilizan para un tipo específico de propósito de mensajería. Por ejemplo, si una marca tiene previsto enviar mensajes SMS transaccionales y promocionales, deberá configurar dos grupos de suscripción con grupos separados de números de teléfono de envío en el panel de control de Braze.

## Estados de suscripción a SMS

Existen dos estados de suscripción para los usuarios de SMS: `subscribed` y `unsubscribed`. El estado de suscripción de un usuario no se comparte entre grupos de suscripción, lo que significa que un usuario puede estar `subscribed` en un grupo de suscripción transaccional pero `unsubscribed` en uno promocional. Para las marcas, esta separación de estados garantiza que puedan seguir enviando mensajes SMS relevantes a sus usuarios.

| Estado | Definición |
| --------- | ---------- |
| Suscrito | El usuario ha confirmado explícitamente que desea recibir SMS de un grupo de suscripción específico. Un usuario puede suscribirse actualizando su estado de suscripción a través de la API de suscripción Braze o enviando un mensaje de texto con una respuesta de palabra clave. Un usuario debe estar suscrito a un grupo de suscripción SMS para poder recibir un SMS. |
| No suscrito | El usuario ha optado explícitamente por no recibir mensajes de su grupo de suscripción SMS y de los números de teléfono remitentes dentro del grupo de suscripción. Pueden cancelar la suscripción enviando un mensaje de texto con la palabra clave "opt-out"; alternativamente, una marca puede cancelar la suscripción de los usuarios a través de la [API de suscripción Braze][4]. Los usuarios que se den de baja de un grupo de suscripción SMS dejarán de recibir SMS de los números de teléfono de envío que pertenezcan al grupo de suscripción.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cómo se establecen los grupos de suscripción SMS de los usuarios 

- **API REST:** Los perfiles de usuario pueden establecerse mediante programación en [`/subscription/status/set` endpoint][4] utilizando la API REST de Braze.
- **Integración SDK** Los usuarios pueden añadirse a un grupo de suscripción por correo electrónico o SMS utilizando el método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web][11].
- **Se gestiona automáticamente cuando el usuario se da de alta o de baja:** Cuando los usuarios envían un mensaje de texto con una opción de inclusión o exclusión predeterminada [palabra clave][7], Braze establece y actualiza automáticamente el estado de suscripción de los usuarios.
- **Importación de usuarios**: Los usuarios pueden añadirse a grupos de suscripción por correo electrónico o SMS mediante **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debe tener estas dos columnas en su CSV: `subscription_group_id` y `subscription_state`. Consulte [Importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para obtener más información.

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), esta página se llama **Importación de usuarios** y se encuentra en **Usuarios**.
{% endalert %}

Cuando se actualiza un número de teléfono en un perfil de usuario, el nuevo número de teléfono hereda el estado del grupo de suscripción del usuario. Si el número de teléfono se actualiza a un número que ya existe en Braze, se hereda el estado de suscripción de ese número de teléfono existente.

Por ejemplo, si el usuario A tiene un número de teléfono que está suscrito a varios grupos de suscripción y ese número de teléfono se añade al usuario B, el usuario B estará suscrito a los mismos grupos de suscripción. Para evitar que un usuario herede las suscripciones existentes, puede restablecer los grupos de suscripción del número antiguo a través de la API REST cada vez que un usuario cambie de número. Si varios usuarios comparten este número de teléfono, todos serán dados de baja.

### Cómo comprobar el grupo de suscripción SMS de un usuario

- **Perfil del usuario:** Se puede acceder a los perfiles individuales de los usuarios a través del panel de control de Braze seleccionando Búsqueda de usuarios en la barra lateral. Aquí puede buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Dentro del perfil de un usuario, en la pestaña Compromiso, puede ver los grupos de suscripción a SMS de un usuario. 
- **API REST:** Los perfiles de usuario individuales del grupo de suscripción se pueden ver mediante el punto final [Listar grupos de suscripción del usuario][9] o el punto final [Listar estado del grupo de suscripción del usuario][8] utilizando la API REST de Braze. 

## Envío con un grupo de suscripción

Para lanzar una campaña de SMS a través de Braze, se debe seleccionar un grupo de suscripción en el desplegable, como se muestra en la siguiente imagen. Después de seleccionarlo, se añadirá automáticamente un filtro de audiencia a su campaña o Canvas, asegurando que sólo los usuarios `subscribed` al grupo de suscripción seleccionado estén en la audiencia objetivo. Para adherirse a las [normas y directrices internacionales de telecomunicaciones][3], Braze nunca enviará SMS a usuarios que no se hayan suscrito al grupo de suscripción seleccionado.  

![Compositor de SMS con el desplegable del grupo de suscripción abierto y "Servicio de mensajería A para SMS" resaltado por el usuario.][6]

## Proceso de configuración

Durante el proceso de integración de SMS, un gestor de integración de Braze creará grupos de suscripción para su cuenta de panel de control. Trabajarán con usted para determinar cuántos grupos de suscripción necesita y añadir los números de teléfono de envío adecuados a sus grupos de suscripción. Los plazos para configurar un grupo de suscripción dependerán del tipo de números de teléfono que estés añadiendo. Por ejemplo, las solicitudes de códigos cortos pueden tardar entre 8 y 12 semanas, mientras que los códigos largos pueden crearse en un día. Si tienes preguntas sobre la configuración de tu panel Braze, ponte en contacto con tu representante Braze para obtener ayuda.  

## Habilitación de MMS para grupos de suscripción

Para enviar un mensaje MMS, al menos un número de tu grupo de suscripción debe estar habilitado para enviar MMS. Esto se indica mediante una etiqueta situada junto al grupo de suscripción. 

![Grupo de suscripción desplegable con "Servicio de mensajería A para SMS" resaltado. La entrada va precedida de la etiqueta "MMS".][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
