---
nav_title: "Grupos de suscripción"
article_title: Grupos de suscripción a SMS y RCS
page_order: 1
description: "Este artículo de referencia trata sobre los grupos de suscripción, los estados de suscripción y el proceso de configuración de grupos de suscripción para los canales SMS, MMS y RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Grupos de suscripción a SMS y RCS

> Los grupos de suscripción son la base para enviar mensajes SMS, MMS y RCS a través de Braze. Un grupo de suscripción es un conjunto de [entidades emisoras]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (como remitentes verificados por RCS, códigos abreviados SMS, códigos largos SMS o ID de remitente alfanuméricos SMS) que se utilizan para un tipo específico de mensajería. Por ejemplo, si una marca tiene previsto enviar mensajes SMS transaccionales y promocionales, deberá configurar dos grupos de suscripción con grupos separados de números de teléfono de envío en el panel de control de Braze.

## Estados del grupo de suscripción

Hay dos estados de suscripción para los usuarios de SMS y RCS:`subscribed`  y `unsubscribed`. El estado de suscripción de un usuario reside en el nivel del grupo de suscripción y no se comparte entre grupos de suscripción, lo que significa que un usuario puede pertenecer`subscribed`a un grupo de suscripción transaccional pero`unsubscribed`no a uno promocional. Para las marcas, esta separación de estados garantiza que puedan seguir enviando mensajes SMS y RCS relevantes a sus usuarios.

| Estado | Definición |
| --------- | ---------- |
| Suscrito | El usuario ha confirmado explícitamente que deseas recibir SMS y RCS de un grupo de suscripción específico. Un usuario puede suscribirse actualizando su estado de suscripción a través de la API de suscripción Braze o enviando un mensaje de texto con una respuesta de palabra clave. El usuario debe estar suscrito a un grupo de suscripción SMS o RCS para poder recibir SMS, RCS o ambos. |
| No suscrito | El usuario ha optado explícitamente por no recibir mensajes de tu grupo de suscripción SMS y RCS ni de los números de teléfono que envían mensajes dentro del grupo de suscripción. Pueden cancelar la suscripción enviando un mensaje de texto con la palabra clave "opt-out"; alternativamente, una marca puede cancelar la suscripción de los usuarios a través de la [API de suscripción Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Los usuarios que hayan cancelado la suscripción a un grupo de suscripción SMS y RCS ya no recibirán ningún SMS o RCS de los números de teléfono remitentes que pertenezcan al grupo de suscripción.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Configuración del estado de un usuario

Cuando se actualiza un número de teléfono en un perfil de usuario, el nuevo número de teléfono hereda el estado del grupo de suscripción del usuario. Si el número de teléfono se actualiza a un número que ya existe en Braze, se hereda el estado de suscripción de ese número de teléfono existente.

Por ejemplo, si el usuario A tiene un número de teléfono que está suscrito a varios grupos de suscripción y ese número de teléfono se añade al usuario B, el usuario B estará suscrito a los mismos grupos de suscripción. Para evitar que un usuario herede las suscripciones existentes, puedes restablecer los grupos de suscripción del número antiguo a través de la API REST de Braze cada vez que un usuario cambie su número. Si varios usuarios comparten este número de teléfono, todos serán dados de baja.

Para establecer el estado del grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **API REST:** Los perfiles de usuario se pueden configurar mediante programación en el punto final [\`/suscripción/estado/set]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)\` utilizando la API REST de Braze.
- **Integración de SDK** Se puede añadir usuarios a un grupo de suscripción por correo electrónico, SMS o RCS utilizando el`addToSubscriptionGroup`método para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Se gestiona automáticamente cuando el usuario se da de alta o de baja:** Cuando los usuarios envían por mensaje de texto una [palabra clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) predeterminada para la adhesión voluntaria o la baja, Braze configura y actualiza automáticamente el estado de la suscripción de los usuarios.
- **Importación de usuarios**: Se puede añadir usuarios a grupos de suscripción por correo electrónico, SMS y RCS a través de **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debe tener estas dos columnas en su CSV: `subscription_group_id` y `subscription_state`. Consulte [Importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para obtener más información.

### Comprobación del grupo del usuario

Para comprobar el grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **Perfil del usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze seleccionando **«Búsqueda de usuarios»** en la barra lateral. Aquí puede buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Cuando estés dentro del perfil de usuario, en la pestaña Interacción, podrás ver los grupos de suscripción SMS y RCS del usuario. 
- **API REST:** El grupo de suscripción de perfiles de usuario individuales se puede ver mediante el [punto final Listar grupos de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o [Listar estado de grupo de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) mediante la API REST de Braze. 

## Envío de mensajes con un grupo de suscripción

Para lanzar una campaña SMS o RCS a través de Braze, selecciona un grupo de suscripción en el menú desplegable **Variantes SMS/MMS/RCS**. Después de seleccionarlo, se añadirá automáticamente un filtro de audiencia a su campaña o Canvas, asegurando que sólo los usuarios `subscribed` al grupo de suscripción seleccionado estén en la audiencia objetivo.

{% alert important %}
En cumplimiento de [las normas y directrices]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) internacionales [en materia de telecomunicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze nunca enviará SMS o RCS a usuarios que no se hayan suscrito al grupo de suscripción seleccionado.  
{% endalert %}

![Compositor de SMS con el desplegable del grupo de suscripción abierto y "Servicio de mensajería A para SMS" resaltado por el usuario.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Habilitar grupos de suscripción

Para habilitar grupos de suscripción para SMS, MMS o RCS, consulta lo siguiente:

{% tabs local %}
{% tab SMS %}
Durante el proceso de integración de SMS, un gestor de integración de Braze creará grupos de suscripción para su cuenta de panel de control. Trabajarán con usted para determinar cuántos grupos de suscripción necesita y añadir los números de teléfono de envío adecuados a sus grupos de suscripción. Los plazos para configurar un grupo de suscripción dependerán del tipo de números de teléfono que estés añadiendo. Por ejemplo, las solicitudes de códigos cortos pueden tardar entre 8 y 12 semanas, mientras que los códigos largos pueden crearse en un día. Si tienes alguna pregunta sobre la configuración del panel de Braze, ponte en contacto con tu representante de Braze para obtener ayuda.  
{% endtab %}

{% tab MMS %}
Para enviar un mensaje MMS, al menos un número de tu grupo de suscripción debe estar habilitado para enviar MMS. Esto se indica mediante una etiqueta situada junto al grupo de suscripción. 

![Grupo de suscripción desplegable con "Servicio de mensajería A para SMS" resaltado. La entrada va precedida de la etiqueta "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Para poder enviar un mensaje RCS, debe haber un remitente verificado por RCS en tu grupo de suscripción. 

Hay dos formas de añadir un remitente verificado por RCS:
- Añadirlo a un grupo de suscripción existente
- Crear un nuevo grupo de suscripción RCS
La elección depende en gran medida de los casos de uso de RCS que te interesen. 

Dependiendo de tu integración, Braze puede añadir remitentes verificados por RCS a tus grupos de suscripción SMS existentes o configurar nuevos grupos de suscripción para ti. En cualquier caso, tu administrador del éxito del cliente te guiará fácilmente y de manera eficiente a través de la actualización del tráfico SMS.
{% endtab %}
{% endtabs %}

## Migración del tráfico SMS a RCS

Si tienes grupos de suscripción SMS y RCS separados, puedes realizar la migración de usuarios de SMS a RCS utilizando un Canvas de un solo paso. 

Braze recomienda que pruebes el envío de RCS a un volumen reducido de usuarios inicialmente y que vayas realizando la migración de más usuarios al grupo de suscripción RCS con el tiempo. Por ejemplo, si tienes 1 000 000 de usuarios suscritos a un grupo de suscripción por SMS, esto podría consistir en realizar primero la migración de todos los usuarios al nuevo grupo de suscripción y, a continuación, realizar la segmentación de una audiencia más pequeña de entre 50 000 y 100 000 (5-10 %) para probar los mensajes RCS.

### Paso 1: Crea un Canvas y rellena el calendario de entradas.

Crea un Canvas y ponle un nombre que sea fácil de identificar (por ejemplo, «Transferencia de usuarios del grupo de suscripción SMS-RCS»). A continuación, programa la campaña cuando te resulte más conveniente.

### Paso 2: Define tu audiencia

Define tu audiencia utilizando uno de los siguientes métodos. A continuación, ve al paso **Configuración de** **envío** y selecciona **Usuarios suscriptores o que han realizado una adhesión voluntaria**.

| Método                          | Descripción                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Crear un segmento**         | Crea un segmento que incluya a todos los usuarios de un grupo de suscripción o un subconjunto utilizando filtros de segmentación (por ejemplo, un 5-10 % aleatorio). Los segmentos se actualizan antes de cada envío para reflejar tu base de usuarios actual.        |
| **Aplicar filtros de campaña o Canvas** | Refina la audiencia en el paso **Audiencia objetivo** de tu campaña o Canvas. Adjust las opciones de segmentación sin salir de la página para mayor flexibilidad.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Paso 3: Configura un paso de actualización de usuario.

Añade un paso de actualización de usuario a tu Canvas. En el paso, abre el **Editor JSON avanzado** e introduce lo siguiente (para el campo de identificador único de usuario, recomendamos utilizar el`braze_id`campo  ):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![«Objeto de actualización de usuario» que contiene el código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Paso 4: Prueba el Canvas

Te recomendamos encarecidamente [que]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) [pruebes tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para confirmar que funciona según lo previsto antes de enviarlo a una audiencia más amplia.

### Paso 5: Lanza tu Canvas

Una vez que hayas probado con éxito tu Canvas, ¡adelante, lánzalo para tu subconjunto de usuarios!

Para confirmar que tus usuarios se han migrado correctamente, te recomendamos que compruebes algunos perfiles de usuario individuales que se hayan actualizado. En la pestaña **Interacción**, busca **Configuración** de **contacto** y desplázate para ver los grupos de suscripción a los que estás suscrito. Ahora debería alternarse el botón del grupo de suscripción RCS.
