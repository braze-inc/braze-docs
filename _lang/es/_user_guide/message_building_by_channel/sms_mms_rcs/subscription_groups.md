---
nav_title: "Grupos de suscripción"
article_title: Grupos de suscripción a SMS y RCS
page_order: 1
description: "Este artículo de referencia cubre los grupos de suscripción, los estados de suscripción y el proceso de configuración de grupos de suscripción para canales SMS, MMS y RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Grupos de suscripción SMS y RCS

> Los grupos de suscripción son la base para enviar mensajes SMS, MMS y RCS a través de Braze. Un grupo de suscripción es un conjunto de [entidades remitentes]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (como remitentes verificados por RCS, códigos abreviados SMS, códigos largos SMS o ID alfanuméricos de remitente SMS) que se utilizan para un tipo específico de mensajería. Por ejemplo, si una marca tiene previsto enviar mensajes SMS transaccionales y promocionales, tendrá que configurar dos grupos de suscripción con grupos separados de números de teléfono de envío en su panel de Braze.

## Estados del grupo de suscripción

Hay dos estados de suscripción para los usuarios de SMS y RCS: `subscribed` y `unsubscribed`. El estado de suscripción de un usuario reside en el nivel del grupo de suscripción y no se comparte entre grupos de suscripción, lo que significa que un usuario puede estar `subscribed` en un grupo de suscripción transaccional pero `unsubscribed` en uno promocional. Para las marcas, esta separación de estados garantiza que puedan seguir enviando mensajes SMS y RCS relevantes a sus usuarios.

| Estado | Definición |
| --------- | ---------- |
| Suscrito | El usuario ha confirmado explícitamente que desea recibir SMS y RCS de un grupo de suscripción específico. Un usuario puede suscribirse actualizando su estado de suscripción a través de la API de suscripción de Braze o enviando un mensaje de texto con una respuesta de palabra clave de adhesión voluntaria. Un usuario debe estar suscrito a un grupo de suscripción SMS o RCS para recibir SMS, RCS o ambos. |
| Cancelar suscripción | El usuario ha optado explícitamente por no recibir mensajería de tu grupo de suscripción a SMS y RCS y de los números de teléfono de envío dentro del grupo de suscripción. Pueden cancelar la suscripción enviando un mensaje de texto con una respuesta de palabra clave de exclusión o una marca puede dar de baja a los usuarios a través de la [API de suscripción de Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Los usuarios que se den de baja de un grupo de suscripción a SMS y RCS dejarán de recibir SMS y RCS de los números de teléfono de envío que pertenezcan al grupo de suscripción.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Configuración del estado de un usuario

Cuando se actualiza un número de teléfono en un perfil de usuario, el nuevo número de teléfono hereda el estado del grupo de suscripción del usuario. Si el número de teléfono se actualiza a un número que ya existe en Braze, se hereda el estado de suscripción de ese número de teléfono existente.

Por ejemplo, si el usuario A tiene un número de teléfono que está suscrito a varios grupos de suscripción y ese número de teléfono se añade al usuario B, el usuario B estará suscrito a los mismos grupos de suscripción. Para evitar que un usuario herede las suscripciones existentes, puedes restablecer los grupos de suscripción del número antiguo a través de la API REST de Braze cada vez que un usuario cambie de número. Si varios usuarios comparten este número de teléfono, se cancelará la suscripción de todos ellos.

Para establecer el estado del grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **API REST:** Los perfiles de usuario se pueden configurar mediante programación a través del punto final [\`/subscription/status/set\`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) utilizando la API REST de Braze.
- **Integración de SDK** Los usuarios pueden añadirse a un grupo de suscripción por correo electrónico o SMS y RCS utilizando el método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Se gestiona automáticamente con la adhesión/exclusión voluntaria del usuario:** Cuando los usuarios envían un mensaje de texto con una [palabra clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) predeterminada de adhesión voluntaria o de exclusión voluntaria, Braze establece y actualiza automáticamente el estado de suscripción de los usuarios.
- **Importación de usuarios**: Los usuarios pueden añadirse a grupos de suscripción por correo electrónico o SMS y RCS a través de **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debes tener estas dos columnas en tu CSV: `subscription_group_id` y `subscription_state`. Consulta [Importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para más información.

### Comprobar el grupo de un usuario

Para comprobar el grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze seleccionando **Búsqueda de usuarios** en la barra lateral. Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID externo de usuario. Dentro del perfil de usuario, en la pestaña Interacción, puedes ver los grupos de suscripción SMS y RCS de un usuario. 
- **API REST:** Los perfiles de usuario individuales del grupo de suscripción pueden verse mediante el [punto final Listar]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) [grupos de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o el [punto final Listar estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) utilizando la API REST de Braze. 

## Envío de mensajes con un grupo de suscripción

Para lanzar una campaña SMS o RCS a través de Braze, selecciona un grupo de suscripción en el desplegable **Variantes SMS/MMS/RCS**. Una vez seleccionado, se añadirá automáticamente un filtro de audiencia a tu campaña o Canvas, que garantizará que sólo los usuarios `subscribed` del grupo de suscripción seleccionado estén en la audiencia objetivo.

{% alert important %}
En cumplimiento [de las normas y directrices]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) internacionales [de telecomunicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze nunca enviará SMS o RCS a usuarios que no se hayan suscrito al grupo de suscripción seleccionado.  
{% endalert %}

\![Creador de mensajes SMS con el desplegable del grupo de suscripción abierto y "Servicio de mensajería A para SMS" resaltado por el usuario.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Habilitación de grupos de suscripción

Para habilitar grupos de suscripción para SMS, MMS o RCS, consulta lo siguiente:

{% tabs local %}
{% tab SMS %}
Durante tu proceso de incorporación de SMS, un administrador de incorporación de Braze establecerá grupos de suscripciones para tu cuenta del panel. Trabajarán contigo para determinar cuántos grupos de suscripción necesitas y añadirán los números de teléfono de envío adecuados a tus grupos de suscripción. Los plazos para configurar un grupo de suscripción dependerán del tipo de números de teléfono que estés añadiendo. Por ejemplo, las solicitudes de código abreviado pueden tardar entre 8 y 12 semanas, mientras que los códigos largos pueden configurarse en un día. Si tienes preguntas sobre la configuración de tu panel Braze, ponte en contacto con tu representante Braze para obtener ayuda.  
{% endtab %}

{% tab MMS %}
Para enviar un mensaje MMS, al menos un número de tu grupo de suscripción tiene que estar habilitado para enviar MMS. Esto se indica mediante una etiqueta situada junto al grupo de suscripción. 

\![Desplegable del grupo de suscripción con "Servicio de mensajería A para SMS" resaltado. La entrada va precedida de la etiqueta "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un remitente verificado por RCS debe estar presente en tu grupo de suscripción antes de que puedas enviar un mensaje RCS. 

Hay dos formas de añadir un remitente verificado por RCS:
- Añádelo a un grupo de suscripción existente
- Crear un nuevo grupo de suscripción RCS
La elección depende en gran medida de los casos de uso de RCS que te interesen. 

Dependiendo de tu integración, Braze puede añadir remitentes verificados por RCS a tus grupos de suscripción SMS existentes o configurar nuevos grupos de suscripción para ti. En cualquiera de los casos, tu administrador del éxito del cliente te guiará a través de una actualización del tráfico de SMS eficaz y sin complicaciones.
{% endtab %}
{% endtabs %}

## Migración del tráfico SMS a RCS

Si tienes grupos de suscripción SMS y RCS separados, puedes migrar usuarios de SMS a RCS utilizando un Canvas de un solo paso. 

Braze recomienda que pruebes a enviar RCS a volúmenes más pequeños de usuarios inicialmente y que migres más usuarios al grupo de suscripción RCS con el tiempo. Por ejemplo, si tienes 1.000.000 de usuarios suscritos a un grupo de suscripción de SMS, esto podría ser como migrar primero a todos los usuarios al nuevo grupo de suscripción y luego segmentar en una audiencia más pequeña de 50.000 a 100.000 (5-10%) para probar los mensajes RCS.

### Paso 1: Crea un Canvas y rellena el Calendario de Entrada

Crea un Canvas y ponle un nombre fácilmente identificable (como "Transferencia de usuario del grupo de suscripción SMS-RCS"). Después, programa la campaña cuando te venga bien.

### Paso 2: Define tu audiencia

Define tu audiencia utilizando uno de los siguientes métodos. A continuación, ve al paso **Configuración de envío** y selecciona **Usuarios suscritos o con adhesión voluntaria**.

| Método                          | Descripción                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Crear un segmento**         | Construye un segmento que incluya a todos los usuarios de un grupo de suscripción o un subconjunto utilizando filtros de segmentación (e.g., un 5-10% aleatorio). Los segmentos se actualizan antes de cada envío para reflejar tu base de usuarios actual.        |
| **Aplicar filtros de campaña o Canvas** | Afina la audiencia en el paso **Audiencia objetivo** de tu campaña o Canvas. Ajusta las opciones de orientación sin salir de la página para una mayor flexibilidad.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Paso 3: Configurar un paso de actualización de usuario

Añade un paso de actualización de usuario a tu Canvas. En el paso, abre el **Editor JSON Avanzado** e introduce lo siguiente (para el campo identificador único de usuario, recomendamos utilizar el campo `braze_id` ):

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

\!["Objeto de actualización del usuario" que contiene el código JSON indicado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Paso 4: Prueba el Canvas

Te recomendamos encarecidamente que [pruebes tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para confirmar que funciona como esperas antes de enviarlo a tu audiencia más amplia.

### Paso 5: Lanza tu Canvas

Cuando hayas probado con éxito tu Canvas, ¡lánzalo para tu subconjunto de usuarios!

Para confirmar que tus usuarios han migrado correctamente, te recomendamos que compruebes algunos perfiles de usuario individuales que se hayan actualizado. En la pestaña **Interacción**, busca **Configuración de contacto** y desplázate para ver los grupos de suscripción a los que está suscrito el usuario. Ahora debería estar activado el alternador del grupo de suscripción RCS.
