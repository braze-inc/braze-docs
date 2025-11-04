---
nav_title: Configuración de la LÍNEA
article_title: Configuración de la LÍNEA
description: "Este artículo explica cómo configurar el canal Braze LINE, incluidos los requisitos previos y los pasos siguientes sugeridos."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuración de la LÍNEA

> Este artículo explica cómo configurar el canal LINE en Braze, incluyendo cómo configurar usuarios, conciliar ID de usuario y crear usuarios de prueba LINE en Braze.

## Requisitos previos

Necesitarás lo siguiente para integrar LINE con Braze:

- [Cuenta de empresa LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Estado de cuenta Premium o verificada (necesario para sincronizar los seguidores existentes)
   - Ver [las directrices de la cuenta de LINE](https://terms2.line.me/official_account_guideline_oth)
- [Cuenta de desarrollador de LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de mensajería API de LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Al enviar mensajes de LINE desde Braze, se utilizarán los créditos de mensajes de tu cuenta.

## Tipos de cuentas LINE

| Tipo de cuenta | Descripción |
| --- | --- |
| Cuenta no verificada | Una cuenta no revisada que puede obtener cualquiera (particular o empresa). Esta cuenta está representada con una señal gris y no aparecerá en los resultados de búsqueda dentro de la aplicación LINE. |
| Cuenta verificada | Una cuenta que ha superado el control de LINE Yahoo. Esta cuenta está representada con una señal azul y aparecerá en los resultados de búsqueda dentro de la aplicación LINE.<br><br>Esta cuenta sólo está disponible para cuentas con sede en Japón, Taiwán, Tailandia e Indonesia.  |
| Cuenta Premium | Una cuenta que ha superado el control de LINE Yahoo. Esta cuenta está representada con una señal verde y aparecerá en los resultados de búsqueda dentro de la aplicación LINE. Este tipo de cuenta se concede automáticamente durante la selección a discreción de LINE. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipo de cuenta requerido

Para sincronizar seguidores en Braze, tu cuenta de LINE debe estar verificada o ser premium. Cuando crees una cuenta, su estado predeterminado será sin verificar. Tendrás que solicitar la verificación de la cuenta.

### Solicitar una cuenta LINE verificada

{% alert important %}
Las cuentas verificadas sólo están disponibles para cuentas con sede en Japón, Taiwán, Tailandia e Indonesia.
{% endalert %}

1. En la página de la **Cuenta Oficial** de LINE, selecciona **Configuración**.
2. En **Estado de verificación de la divulgación de información**, selecciona **Solicitar verificación de cuenta**.
3. Introduce la información requerida.
4. Espera una notificación con los resultados de la revisión.

## Integración de LINE

Para configurar actualizaciones de usuario coherentes, traslada los ID de LINE de los usuarios existentes y sincronízalos todos con los estados de suscripción de LINE:

1. [Importar o actualizar usuarios conocidos existentes](#step-1-import-or-update-existing-line-users)
2. [Integrar el canal LINE](#step-2-integrate-line-channel)
3. [Conciliar ID de usuario](#step-3-reconcile-user-ids)
4. [Cambiar los métodos de actualización del usuario](#step-4-change-your-user-update-methods)
5. [(Opcional) Fusionar perfiles de usuario](#step-5-merge-profiles-optional)

## Paso 1: Importar o actualizar usuarios existentes de LINE

Este paso es necesario si tienes un usuario de LINE existente e identificado, ya que Braze extraerá después automáticamente su estado de suscripción y actualizará el perfil de usuario correcto. Si no has conciliado previamente a los usuarios con su ID de LINE, omite este paso. 

Puedes importar o actualizar usuarios utilizando cualquiera de los métodos que admite Braze, incluido el punto final [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) punto final, la [importación CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) o [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Independientemente del método que utilices, actualiza el `native_line_id` para proporcionar el ID de LÍNEA del usuario. Para saber más sobre `native_line_id`, consulta [Configuración del usuario](#user-setup).

{% alert note %}
El estado del grupo de suscripción no debe especificarse, y será ignorado. LINE es la fuente de verdad del estado de suscripción del usuario, que se sincronizará con Braze mediante la herramienta de sincronización de suscripciones o mediante actualizaciones de eventos.
{% endalert %}

## Paso 2: Integra el canal LINE

Una vez completado el proceso de integración, Braze incorporará automáticamente a Braze los seguidores de LINE de ese canal. Para los ID de LINE que ya estén asociados a un perfil de usuario de Braze, cada perfil se actualizará con el estado "suscrito", y los ID de LINE restantes generarán usuarios anónimos. Además, a los nuevos seguidores de tu canal de LINE se les crearán perfiles de usuario no identificados cuando sigan el canal.

### Paso 2.1: Editar configuración del webhook

1. En LINE, ve a la pestaña **API de mensajería** y edita la **configuración de** tu **webhook**:
   - Configura la **URL del webhook** en `https://anna.braze.com/line/events`.
      - Braze cambiará esto automáticamente a una URL diferente al realizar la integración, basándose en el grupo de tu panel.
   - Activa **Usar webhook** y **Reenviar webhook**. <br><br> \![Página de configuración del webhook para verificar o editar la URL del webhook, alternando entre "Usar webhook", "Reenvío de webhook" y "Agregación de estadísticas de errores".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Toma nota de la siguiente información en la pestaña **Proveedores**:

| Tipo de información | Ubicación |
| --- | --- |
| ID del proveedor | Selecciona tu proveedor y ve a **\*Configuración** > **Información básica** |
| ID del canal | Selecciona tu proveedor y ve a **Canales** > tu canal > **Configuración básica** |
| Secreto del canal | Selecciona tu proveedor y luego ve a **Canales** > tu canal > **Configuración básica**. |
| Token de acceso al canal | Selecciona tu proveedor y luego ve a **Canales** > tu canal > **API de mensajería**. Si no hay un token de acceso al canal, selecciona **Emitir**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. Ve a tu página **Configuración** > **Configuración de respuesta** y haz lo siguiente:
   - Desactiva el **mensaje de saludo**. Esto puede gestionarse en Braze mediante desencadenar al seguir.
   - Desactiva **los mensajes de respuesta automática**. Todos los mensajes desencadenados deben enviarse a través de Braze. Esto no te impedirá enviar directamente desde la consola LINE.
   - Activa **los webhooks**.

\![Página de configuración de la respuesta con alternadores para saber cómo tu cuenta gestionará los chats.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Paso 2.2: Generar grupos de suscripción LINE en Braze

1. Ve a la página de socios tecnológicos de Braze para LINE e introduce la información que hayas anotado en tu pestaña de **proveedores de** LINE:
   - ID del proveedor
   - ID del canal
   - Secreto del canal
   - Token de acceso al canal

Si quieres añadir una lista blanca de IP en tu cuenta de LINE, añade a tu lista de permitidas todas las direcciones IP que aparecen para tu clúster en la [lista de permitidas de IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting).

{% alert important %}
Durante la integración, asegúrate de que el secreto de tu canal es correcto. Si es incorrecto, puede haber incoherencias en el estado de la suscripción.
{% endalert %}

Página de integración de la mensajería LINE con la sección de integración de LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Tras la conexión, Braze generará automáticamente un grupo de suscripción Braze para cada integración LINE que se añada correctamente a tu espacio de trabajo. <br><br> Cualquier cambio en tu lista de seguidores (como nuevos seguidores o dejar de seguirlos) se empujará automáticamente a Braze.

\![Sección de grupos de suscripción LINE que muestra un grupo de suscripción para el canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Paso 3: Conciliar ID de usuario

Combina los ID de LINE de tus usuarios con sus perfiles de usuario Braze existentes siguiendo los pasos de [Reconciliación de ID de usuario](#user-id-reconciliation).

## Paso 4: Cambia tus métodos de actualización de usuario 

Suponiendo que ya tengas un método para proporcionar actualizaciones de usuario a Braze, tendrás que actualizarlo para que incluya el nuevo campo `native_line_id`, de modo que las actualizaciones de usuario posteriores que se envíen a Braze incluyan ese campo.

Pueden existir perfiles de usuario no identificados con un `native_line_id` en Braze que se crearon como parte del proceso de sincronización del estado de suscripción, o cuando un nuevo seguidor siguió tu canal. 

Cuando un usuario de LINE se identifica en tu aplicación a través de [la conciliación de usuarios](#user-id-reconciliation) u otros medios, puedes dirigirte a un perfil de usuario potencial no identificado en Braze utilizando el punto final [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) punto final. Cada perfil de usuario no identificado con un `native_line_id` también tiene un alias de usuario `line_id` que puede utilizarse para seleccionar el perfil de usuario a identificar.

He aquí un ejemplo de carga útil para `/users/identify` que se dirige a un perfil de usuario no identificado mediante el alias de usuario `line_id`: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Si no existe ningún perfil de usuario para tu `external_id` facilitado, se añadirá al perfil de usuario no identificado, convirtiéndolo en identificado. Si existe un perfil de usuario para `external_id`, todos los atributos exclusivos del perfil de usuario no identificado se copiarán en el perfil de usuario conocido, incluidos `native_line_id` y el estado de suscripción del usuario.

Puedes actualizar los usuarios de LINE conocidos en tu aplicación a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pasando sus identificadores externos y `native_line_id`. Si ya existe un perfil de usuario no identificado para un usuario y el mismo `native_line_id` se añade a un perfil de usuario diferente a través de `/users/track`, heredará todos los estados de suscripción del perfil de usuario no identificado. Sin embargo, existirán perfiles de usuario duplicados con el mismo `native_line_id`. Cualquier actualización posterior de la suscripción a partir de actualizaciones de eventos actualizará todos los perfiles en consecuencia. 

Aquí tienes un ejemplo de carga útil para `/users/track` que actualiza un perfil de usuario mediante el ID externo de usuario para añadir un `native_line_id`: 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Paso 5: Fusionar perfiles (opcional)

Como se ha descrito anteriormente, existe la posibilidad de que existan varios perfiles de usuario con el mismo `native_line_id`. Si tus métodos de actualización crean perfiles de usuario duplicados, puedes fusionar perfiles de usuario no identificados con perfiles de usuario identificados con el punto final `/user/merge`. 

He aquí un ejemplo de carga útil para `/users/merge` que se dirige a un perfil de usuario no identificado por el alias de usuario `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Para obtener más información sobre la gestión de usuarios duplicados en Braze, consulta [Usuarios duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## Configuración de usuario

LINE es la fuente de la verdad para los estados de suscripción de los usuarios. Aunque tengas el ID de LINE de un usuario (`native_line_id`), si ese usuario no ha seguido el canal de LINE desde el que estás enviando, LINE no le entregará mensajes.

Para ayudar a gestionar esto, Braze ofrece herramientas y lógica que dan soporte a una base de usuarios bien integrada, incluyendo la sincronización de suscripciones y las actualizaciones de eventos para los seguidores y no seguidores de LINE.

### Sincronización de suscripciones y lógica de eventos

1. **Herramienta de sincronización de suscripciones:** Esta herramienta se despliega automáticamente tras una integración satisfactoria del canal LINE. Utilízala para actualizar perfiles existentes y crear perfiles nuevos.<br><br>Todos los perfiles de usuario de Braze que tengan un `native_line_id` que siga el canal LINE se actualizarán para tener un estado del grupo de suscripción de `subscribed`. Cualquier seguidor del canal LINE que no tenga un perfil de usuario Braze con el `native_line_id` lo tendrá:<br><br>\- Un perfil de usuario anónimo creado con `native_line_id` configurado con el ID de LÍNEA del usuario siguiente al canal <br>\- Un alias de usuario `line_id` ajustado al ID de LÍNEA del usuario que sigue al canal <br>\- Un estado del grupo de suscripción de `subscribed`

{: start="2"}
2\. **Actualizaciones del evento:** Se utilizan para actualizar el estado de suscripción de un usuario. Cuando Braze recibe actualizaciones de eventos de usuario para el canal LINE integrado y el evento es un seguimiento, el perfil de usuario tendrá un estado del grupo de suscripción de `subscribed`. Si el evento es un unfollow, el perfil de usuario tendrá un estado del grupo de suscripción de `unsubscribed`.<br><br>\- Todos los perfiles de usuario de Braze que coincidan con `native_line_id` se actualizarán automáticamente. <br>\- Si no existe un perfil de usuario coincidente para un evento, Braze [creará un usuario anónimo]({{site.baseurl}}/line/user_management/).

## Casos de uso

Estos son casos de uso de cómo se pueden actualizar los usuarios después de seguir los pasos de configuración anteriores.

##### El perfil de usuario Braze existente ya sigue el canal LINE

1. El perfil de usuario de Braze se actualiza con un atributo `native_line_id`. Su estado de suscripción predeterminado es `unsubscribed`.
2. Se ejecuta la herramienta de sincronización de suscripciones, comprueba que el usuario sigue el canal LINE y, a continuación, actualiza el perfil de usuario con el estado de la suscripción `subscribed`.
3. Si se produce algún cambio en el estado de la suscripción (por ejemplo, si el usuario bloquea el canal, se da de baja como amigo o lo vuelve a seguir), Braze recibe la actualización de LINE y actualiza el perfil de usuario con la dirección `native_line_id` en consecuencia.

##### El perfil de usuario existente ha bloqueado, eliminado de la lista de amigos o del canal LINE 

1. El perfil de usuario de Braze se actualiza con un atributo `native_line_id`. Su estado de suscripción predeterminado es `unsubscribed`.
2. La herramienta de sincronización de suscripciones no encuentra que el usuario esté siguiendo el canal LINE y el estado de suscripción del usuario permanece como `unsubscribed`.
3. Si el usuario sigue posteriormente el canal, Braze recibe la actualización de LINE y actualiza el perfil de usuario con el estado de suscripción `subscribed`.

##### La creación del perfil de usuario se produce después de seguir la LÍNEA

1. El canal consigue un nuevo seguidor LINE.
2. Braze crea un perfil de usuario anónimo con el atributo `native_line_id` configurado para que sea el ID de LÍNEA del seguidor, y un alias de usuario de `line_id` configurado para que sea el ID de LÍNEA del seguidor. El perfil tiene un estado de suscripción de `subscribed`.
3. El usuario se identifica como poseedor del ID de LINE a través de [la conciliación de usuario](#user-id-reconciliation).
  - El perfil de usuario anónimo puede identificarse mediante el punto final [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) punto final. Las actualizaciones posteriores (a través del [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) punto final, [importación de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) o [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) a este perfil de usuario pueden dirigirse al usuario mediante este `external_id` conocido.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Se puede crear un nuevo perfil de usuario (a través del punto final [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) punto final, la [importación de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) o [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) configurando `native_line_id`. Este nuevo perfil heredará el estado de suscripción del perfil de usuario anónimo existente. Nota que esto hará que varios perfiles compartan el mismo `native_line_id`. Se pueden fusionar en cualquier momento utilizando el punto final `/users/merge` en el proceso descrito en el [Paso 5](#step-5-merge-profiles-optional).

##### La creación del perfil de usuario se produce antes de seguir la LÍNEA

1. Adquieres un nuevo usuario y envías la información a Braze. Se crea un nuevo perfil de usuario (perfil 1).
2. El usuario sigue tu cuenta de LINE.
3. Braze recibe un evento de seguimiento y crea un perfil de usuario anónimo (perfil 2).
4. El usuario se identifica como poseedor del ID de LINE a través de [la conciliación de usuario](#user-id-reconciliation).
5. Actualiza el perfil 1 para establecer el atributo `native_line_id`. Este perfil hereda el estado de suscripción del perfil 2.
  - Ahora hay dos perfiles de usuario con el mismo `native_line_id`. Se pueden fusionar en cualquier momento utilizando el punto final `/users/merge` en el proceso descrito en el [Paso 5](#step-5-merge-profiles-optional).

## Conciliación de ID de usuario 

Los ID de LINE son recibidos automáticamente por Braze cuando un usuario sigue tu canal, o cuando utilizas el flujo de trabajo único "sincronizar seguidores". Los ID de LINE también son específicos del canal que siguen los usuarios, por lo que es poco probable que los usuarios puedan proporcionar sus ID de LINE.

Hay dos formas de combinar un ID de LINE con un perfil de usuario Braze existente:

- [Iniciar sesión en LINE](#line-login)
- [Vinculación de cuentas de usuario](#user-account-linking)

### Iniciar sesión en LINE

Este método utiliza las redes sociales para iniciar sesión. Cuando un usuario inicia sesión en tu aplicación, tiene la opción de utilizar [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) para crear una cuenta de usuario o iniciar sesión.

{% alert note %}
Para obtener el ID de LINE correcto para cada usuario, inicia sesión en LINE con el mismo proveedor que tu cuenta oficial o canal de LINE integrado en Braze.
{% endalert %}

1. Ve a la consola para desarrolladores de LINE y [solicita permiso para obtener las direcciones de correo electrónico de los usuarios](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) que inicien sesión en tu aplicación a través de LINE Login.

2. Sigue los pasos adecuados proporcionados por LINE para iniciar sesión en LINE:<br><br>
  - [Instrucciones para la aplicación Web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Indicaciones para aplicaciones nativas](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Asegúrate de incluir `email` en el [ámbito configurado](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) para las solicitudes de verificación. 

{: start="3"}
3\. Utiliza la [llamada al token Verificar ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) para obtener el correo electrónico del usuario. 

4. Guarda el ID de LINE del usuario (`native_line_id`) en el perfil de usuario con un correo electrónico coincidente en tu base de datos, o crea un nuevo perfil de usuario con el correo electrónico y el ID de LINE del usuario.

5. Envía la información nueva o actualizada del usuario a Braze utilizando el [punto final`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), la [importación CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) o [la ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Flujos de trabajo

##### Seguidor existente utiliza LINE Iniciar sesión

**Escenario:** Se ha creado un usuario anónimo durante la sincronización inicial del suscriptor o después de la integración mediante un evento "seguir".

1. El usuario inicia sesión en tu aplicación utilizando LINE Login.
2. LINE te proporciona el correo electrónico del usuario.
3. Envías a Braze el usuario actualizado (el perfil de usuario existente con ese correo electrónico para añadir el ID de LINE) o actualizas el usuario anónimo con el correo electrónico.

##### Nuevo seguidor utiliza LINE Iniciar sesión

**Escenario:** No existe ningún perfil de usuario en Braze con el ID de LÍNEA del usuario.

1. El usuario inicia sesión en tu aplicación utilizando LINE Login.
2. LINE te proporciona el correo electrónico del usuario.
3. O bien
  - Actualiza un perfil de usuario existente con ese correo electrónico para que también tenga el ID de LÍNEA del usuario.
  - Crea un nuevo perfil de usuario con el correo electrónico y el ID de LINE.
4. Cuando el usuario sigue tu Cuenta Oficial de LINE, Braze recibe un evento de seguimiento y actualiza el estado de suscripción del usuario a `subscribed`.

### Vinculación de cuentas de usuario 

Este método permite a los usuarios vincular su cuenta de LINE a la cuenta de usuario de tu aplicación. A continuación, puedes utilizar Liquid en Braze, como {% raw %}`{{line_id}}`{% endraw %}, para crear una URL personalizada para el usuario que devuelva el ID de LINE del usuario a tu sitio web o aplicación, que podrá asociarse a un usuario conocido.

1. Crea un Canvas basado en acciones que se base en un cambio de estado de suscripción y se desencadene cuando un usuario se suscriba a tu canal de LINE.<br>Canvas que se desencadena cuando un usuario se suscribe al canal LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Crea un mensaje que incentive a los usuarios a iniciar sesión en tu sitio web o aplicación, pasando el ID de LINE del usuario como parámetro de consulta (a través de Liquid), como por ejemplo

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. Crea un mensaje de seguimiento que entregue el código del cupón.
4\. (Opcional) Crea una campaña basada en acciones o Canvas que se desencadene cuando se identifique al usuario de LINE para enviarle su código de cupón. <br>Campaña basada en acciones que se desencadena cuando se identifica al usuario de LINE.]({% image_buster /assets/img/line/account_link_2.png %})

#### Cómo funciona

Después de que el usuario inicie sesión, se realiza un cambio en tu sitio web o aplicación para que el ID de usuario se envíe de nuevo a Braze para asociarlo con el ID de LINE que se pasó como parte de la URL, con un código de ejemplo como el siguiente:

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Flujos de trabajo

##### El usuario existente sigue tu canal LINE

**Escenario:** Un usuario existente en Braze sigue tu canal en LINE.

1. LINE envía a Braze un evento de seguimiento.
2. Braze crea un perfil de usuario anónimo con el ID de LINE, el alias de usuario de `line_id` y el estado del grupo de suscripción de LINE de `subscribed`.
3. El usuario recibe un mensaje de LINE con un enlace a tu sitio web y aplicación e inicia sesión. Ahora se conoce su perfil de usuario.
4. El perfil de usuario anónimo que se creó se identifica y se fusiona a través del [ punto final /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) en el perfil de usuario conocido del usuario. El perfil de usuario conocido contiene ahora el ID de LINE y tiene un estado de suscripción de `subscribed`.
5. (Opcional) El usuario recibe un mensaje LINE con el código del cupón y Braze registra el envío en el perfil de usuario de Braze.

## Creación de usuarios de prueba LINE en Braze

Puedes probar tu canal LINE antes de configurar [la conciliación de usuarios](#user-id-reconciliation) creando un Canvas o campaña "Quién soy".

1. Configura un Canvas que devuelva el ID de usuario Braze de un usuario en una palabra desencadenante específica. <br><br>Ejemplo de desencadenante <br><br>\![Desencadenar el envío de la campaña a los usuarios que enviaron una LÍNEA de entrada a un grupo de suscripción concreto.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Ejemplo de mensaje<br><br>\![Mensaje de LINE indicando el ID de usuario de Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. En Braze, puedes utilizar el ID de Braze para buscar usuarios concretos y modificarlos según sea necesario.

{% alert important %}
Asegúrate de que el Canvas no tiene control global o grupos de control que impidan los envíos.
{% endalert %}


