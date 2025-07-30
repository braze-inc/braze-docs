---
nav_title: "Registro Push"
article_title: Registro Push
page_order: 2
page_type: reference
description: "Este artículo de referencia trata sobre lo que significa estar registrado para push y cómo enviamos mensajes push y tratamos los tokens push y el registro push en Braze."
channel:
 - push

---

# Registro push

> Este artículo cubre el proceso mediante el cual se asigna un token push a un usuario y cómo Braze envía mensajes push a sus usuarios.

## Acerca de los tokens de notificaciones push {#push-tokens}

Cuando una aplicación solicita permisos push a un dispositivo, el proveedor de servicios de notificaciones push del dispositivo generará un token de notificaciones push para esa aplicación. Cada aplicación recibe su propio token de notificaciones push, único y anónimo, que es como identifica el dispositivo y la instancia actual de la aplicación al enviar una notificación push.

Ten en cuenta que los tokens de notificaciones push no son identificadores estáticos que duren para siempre: pueden actualizarse y [caducar](#push-token-expire).

{% alert tip %}
Para detalles específicos de la plataforma, consulta [Registro de token de notificaciones push](#push-token-registration).
{% endalert %}

### Foreground vs. background push {#foreground-vs-background}

Los tokens de notificaciones push se utilizan para enviar notificaciones push tanto en primer plano como en segundo plano.

| Tipo       | ¿Requiere adhesión voluntaria? | Descripción                                                 |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Foreground push | Sí       | Se muestra una notificación visible al usuario mientras la aplicación está en primer plano.           |
| Push de fondo | No        | Una notificación se entrega silenciosamente en segundo plano sin mostrarse. A menudo se utiliza para funciones como el seguimiento de desinstalaciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario se adhiere voluntariamente a las notificaciones push de tu aplicación, se le considera "registrado push", lo que significa que ahora se le puede dirigir utilizando el filtro de segmentación `Push enabled for App` en Braze.

{% alert note %}
Esto es diferente del filtro de segmentación `Push Enabled`, que se utiliza para identificar a los usuarios que han optado por la adhesión voluntaria a al menos una de tus aplicaciones, no a una aplicación concreta. Para más información, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#push-enabled).
{% endalert %}

### Varios usuarios en un dispositivo

Los tokens de notificaciones push son únicos tanto para el dispositivo como para la aplicación, lo que significa que los tokens push no pueden utilizarse para dirigirse a usuarios concretos si varios usuarios utilizan el mismo dispositivo.

Por ejemplo, supongamos que tiene dos usuarios: Charlie y Kim. Si Charlie ha activado las notificaciones push para tu aplicación en su teléfono y Kim utiliza el teléfono de Charlie para salir del perfil de Charlie e iniciar sesión en el suyo, el token push se reasignará al perfil de Kim. El token push permanecerá asignado al perfil de Kim en ese dispositivo hasta que se desconecte y Charlie vuelva a conectarse.

Una aplicación o sitio web sólo puede tener una suscripción push por dispositivo. Así, cuando un usuario se desconecta de un dispositivo o sitio web y otro nuevo se conecta, el token push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario en la sección **Configuración de contactos** de la pestaña **Compromiso**:

![Registro de cambios del token de notificaciones push en la pestaña \*\*Interacción** del perfil de un usuario, que enumera cuándo se trasladó el token de notificaciones push a otro usuario, y cuál era el token.]({% image_buster /assets/img/push_token_changelog.png %})

Dado que los proveedores de push (APN/FCM) no pueden distinguir entre varios usuarios en un mismo dispositivo, pasamos el token de push al último usuario que inició sesión para determinar a qué usuario se debe enviar el push en el dispositivo.

## Registro de token de notificaciones push

Cada plataforma de dispositivos gestiona el registro de token de notificaciones push de forma diferente. Consulta a continuación los detalles específicos de cada plataforma:

{% tabs local %}
{% tab android %}
Cuando se instala tu aplicación, se genera automáticamente un token de notificaciones push; sin embargo, sólo puede utilizarse para [notificaciones push en segundo plano](#foreground-vs-background) hasta que el usuario acepte explícitamente. Además, el registro se gestiona de forma diferente en las distintas versiones de Android:

| Versión       | Detalles                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13**         | El permiso push debe ser solicitado y concedido por el usuario. Tu aplicación puede solicitar el permiso manualmente, o se pedirá permiso a los usuarios automáticamente después de crear un [canal de notificación](https://developer.android.com/reference/android/app/NotificationChannel). |
| **Android 12 y anteriores** | Todos los usuarios son considerados `Subscribed` después de su primera sesión. Braze solicita automáticamente un token de notificaciones push en este punto, haciendo que el usuario quede habilitado para push con un token válido y un estado de suscripción predeterminado de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab ios %}
iOS no genera automáticamente tokens de notificaciones push para una aplicación cuando se instala. Además, el registro se gestiona de forma diferente en las distintas versiones de iOS: 

| Versión                         | ¿Autorización provisional? | Detalles                                                                                                                                                     |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12**      | Sí                         | Cuando un usuario se adhiere voluntariamente a las notificaciones push, recibes una autorización estándar que te permite enviar [notificaciones push en primer plano](#foreground-vs-background). Sin embargo, también puedes solicitar [una autorización provisional]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), que te permite enviar [notificaciones push](#foreground-vs-background) silenciosas [en segundo plano](#foreground-vs-background) directamente al centro de notificaciones. |
| **iOS 11 y posteriores** | No                          | Todos los usuarios deben optar explícitamente por recibir notificaciones push. Sólo se genera un token de notificaciones push cuando se concede el permiso.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}

{% tab Web %}
Debe solicitar el consentimiento explícito de los usuarios a través del cuadro de diálogo de permisos nativo del navegador. Recibirá un token después de que los usuarios hayan optado por la adhesión voluntaria. A diferencia de iOS y Android, que permiten que tu aplicación muestre el aviso de permiso en cualquier momento, algunos navegadores modernos sólo lo muestran si se activa mediante un "gesto del usuario" (clic del ratón o pulsación de una tecla). Si tu sitio intenta solicitar permiso de notificación push al cargar la página, es probable que el navegador lo ignore o lo silencie.
{% endtab %}
{% endtabs %}

### Comprobación del estado de la suscripción push del usuario

![Perfil de usuario de John Doe con su estado de suscripción push establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de la suscripción push de un usuario con Braze:

- **Perfil del usuario**: Puedes acceder a perfiles de usuario individuales a través del panel de Braze en la página de [Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Después de encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID de usuario externo), puede seleccionar la pestaña **Compromiso** para ver y ajustar manualmente el estado de suscripción de un usuario.
- **Exportación de API REST**: Puedes exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales de exportación [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze devolverá un objeto de tokens push que contiene información de habilitación push por dispositivo.

### Comprobar el estado del registro push

En la pestaña **Participación** del perfil de un usuario, verá **Push Registered For** seguido del nombre de una aplicación. Si no existe información de la aplicación para ese dispositivo, verás dos guiones**(--**). Habrá una entrada para cada dispositivo que pertenezca al usuario.

Si el nombre de la aplicación de la entrada del dispositivo lleva el prefijo `Foreground:`, la aplicación está autorizada a recibir tanto notificaciones push en primer plano (visibles para el usuario) como notificaciones push en segundo plano (no visibles para el usuario) en ese dispositivo.

![Registro de cambios push con un token de notificaciones push de ejemplo.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por otro lado, si el nombre de la aplicación de la entrada del dispositivo lleva el prefijo `Background:`, la aplicación sólo está autorizada a recibir [push en segundo plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) y no puede mostrar notificaciones visibles para el usuario en ese dispositivo. Esto suele indicar que el usuario ha desactivado las notificaciones de la aplicación en ese dispositivo.

Si un token push se mueve a un usuario diferente en el mismo dispositivo, ese primer usuario ya no será registrado push.

## Tratamiento de token de notificaciones push

Consulte el siguiente gráfico para ver las acciones que provocan cambios en los tokens push o su eliminación de los perfiles de usuario. 

| Acción | Descripción |
| ------ | ----------- |
| `changeUser()` método llamado | El método Braze `changeUser()` cambia el ID de usuario al que los SDK asignan los datos de comportamiento del usuario. Este método suele llamarse cuando un usuario inicia sesión en una aplicación. Cuando se llama a `changeUser()` con un ID de usuario diferente o nuevo en un dispositivo específico, el token push de ese dispositivo se moverá al perfil Braze apropiado con el ID de usuario correspondiente. |
| Se produce un error de empuje | Algunos errores push comunes que llevan a la eliminación del token son `MismatchSenderId`, `InvalidRegistration`, y otros tipos de rebotes push. <br><br>Consulte nuestra lista completa de [errores push]({{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid) comunes. |
| El usuario desinstala | Cuando un usuario desinstale la aplicación de un dispositivo, Braze eliminará el token push del usuario del perfil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ¿Qué aspecto tiene esto a mayor escala?

Cuando un usuario abre una nueva aplicación y concede acceso push desde una solicitud push, se realiza una llamada desde el SDK de Braze a los proveedores push. Cuando se realiza esa llamada, el proveedor de push ejecuta una comprobación para ver si todo está configurado correctamente. Si es así, se pasa un token de notificaciones push a tu dispositivo. Cuando llega ese token, el SDK lo comunica a Braze. Después de que Braze haya recibido el token del proveedor de push, actualizamos o creamos un nuevo perfil de usuario. Estos usuarios se consideran ahora registrados.

Si queremos lanzar una campaña, creamos una campaña en Braze que genere una carga útil push para enviar al proveedor push. A partir de ahí, el proveedor entrega la carga útil push al dispositivo del usuario y el SDK pasa el estado de la mensajería a Braze.

![Un diagrama de flujo que mapea el mencionado proceso push entre Braze, el cliente, y el servicio de notificación push de Apple o la mensajería en la nube de Firebase.]({% image_buster /assets/img/push_process.png %})

| Pasos de la inscripción | Pasos de la mensajería |
| ------------------ | --------------- |
| 1\. El cliente (dispositivo) se registra en el proveedor de push<br>2\. El proveedor genera y entrega el token push<br>3\. Descartar tokens en Braze |1\. Braze envía la carga útil push al proveedor<br>2\. El proveedor entrega la carga útil push al dispositivo<br>3\. SDK pasa las estadísticas de mensajería a Braze |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

### ¿Qué ocurre cuando un usuario que ha dado su consentimiento borra y vuelve a descargar mi aplicación?

Supongamos que un usuario opta por la adhesión voluntaria push, recibe algunos mensajes de mensajería push y, más tarde, elimina la aplicación. Esto eliminará el consentimiento push a nivel de dispositivo. A partir de aquí, el primer mensaje push devuelto tras la desinstalación hará que el usuario quede automáticamente excluido de futuros mensajes push. Después de esto, si un usuario reinstala la aplicación pero no la inicia, Braze no podrá enviar un push al usuario porque los tokens push no se han vuelto a conceder para su aplicación.

Además, si un usuario volviera a activar la función push en primer plano, sería necesario iniciar una sesión para actualizar esta información en su perfil de usuario y empezar a recibir mensajes push.
 
### ¿Cuándo caducan los tokens push? {#push-token-expire}

Por desgracia, APN y FCM no lo definen realmente. Los tokens push pueden caducar cuando se actualiza una aplicación, cuando los usuarios transfieren sus datos a un nuevo dispositivo o cuando reinstalan un sistema operativo. En general, no tenemos información sobre por qué los proveedores de push caducan determinados tokens de notificaciones push.

Para tener en cuenta esta ambigüedad, nuestras integraciones push SDK siempre registran y descargan los tokens al inicio de la sesión para garantizar que tenemos el token más actualizado.
