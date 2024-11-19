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

## Tokens de notificaciones push

Comprender los tokens de notificaciones push y lo que son es una pieza fundamental para entender cómo enviamos mensajes push aquí en Braze. Los tokens push son un identificador anónimo único generado por el dispositivo de un usuario y enviado a Braze para identificar dónde enviar la notificación de cada destinatario. Si un dispositivo no tiene un token de notificaciones push, no hay forma de enviarle push.

Los tokens push son generados por proveedores de servicios push. Braze se conecta con proveedores de servicios push como Firebase Cloud Messaging Service (FCMs) para Android y Apple Push Notification Service (APNs) para iOS, y esos proveedores envían tokens de dispositivo únicos que identifican tu aplicación. Cada dispositivo tiene un token único que se utiliza para la mensajería. Los tokens pueden [caducar](#push-token-expire) o actualizarse.

Hay dos formas de clasificar un [push token][push-tokens] que son esenciales para entender cómo se puede enviar una notificación push a sus usuarios.

1. **Foreground push** ofrece la posibilidad de enviar notificaciones push visibles de forma regular al primer plano del dispositivo de un usuario.
2. **Las notificaciones push en segundo plano** están disponibles independientemente de si un dispositivo concreto ha optado por recibir notificaciones push de esa marca. El push en segundo plano permite a las marcas enviar notificaciones push silenciosas -notificaciones que intencionadamente no se muestran- a los dispositivos para dar soporte a funcionalidades clave como el seguimiento de desinstalaciones.

Cuando un perfil de usuario tiene un token push válido en primer plano asociado a una aplicación, Braze considera que el usuario está "registrado push" para la aplicación en cuestión. Braze, entonces, proporciona un filtro de segmentación específico, `Push enabled for App,` para ayudar a identificar a estos usuarios.

{% alert note %}
El filtro `Push enabled for App` sólo tiene en cuenta la presencia de un token push válido en primer o segundo plano para la aplicación en cuestión. Sin embargo, el filtro más genérico `Push Enabled` segmenta a los usuarios que han activado explícitamente las notificaciones push para cualquier aplicación de su espacio de trabajo. Este recuento incluye sólo los push en primer plano y no incluye a los usuarios que se han dado de baja. Puede obtener más información sobre estos y otros filtros en [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).
{% endalert %}

### Varios usuarios en un dispositivo

Los tokens push son específicos tanto de un dispositivo como de una aplicación, por lo que no es posible utilizarlos para distinguir entre varios usuarios que utilicen el mismo dispositivo.

Por ejemplo, supongamos que tiene dos usuarios: Charlie y Kim. Si Charlie ha activado las notificaciones push para tu aplicación en su teléfono y Kim utiliza el teléfono de Charlie para salir del perfil de Charlie e iniciar sesión en el suyo, el token push se reasignará al perfil de Kim. El token push permanecerá asignado al perfil de Kim en ese dispositivo hasta que se desconecte y Charlie vuelva a conectarse.

Una aplicación o sitio web sólo puede tener una suscripción push por dispositivo. Así, cuando un usuario se desconecta de un dispositivo o sitio web y otro nuevo se conecta, el token push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario en la sección **Configuración de contactos** de la pestaña **Compromiso**:

![Registro de cambios del token de notificaciones push en la pestaña \*\*Interacción** del perfil de un usuario, que enumera cuándo se trasladó el token de notificaciones push a otro usuario, y de qué token se trataba.][4]

Dado que los proveedores de push (APN/FCM) no pueden distinguir entre varios usuarios en un mismo dispositivo, pasamos el token de push al último usuario que inició sesión para determinar a qué usuario se debe enviar el push en el dispositivo.

## Registro de token de notificaciones push

Las plataformas tratan el registro de token de notificaciones push y los permisos push de diferentes maneras:

- **Android**:
  - **Androide 13**:<br>El permiso push debe ser solicitado y concedido por el usuario. Recibe un token después de que el usuario conceda el permiso. Tu aplicación puede pedir permiso manualmente al usuario en los momentos oportunos, pero si no, se lo pedirá automáticamente después de que tu aplicación cree un [canal de notificación](https://developer.android.com/reference/android/app/NotificationChannel).
  - **Android 12 y anteriores**:<br>Todos los usuarios son considerados `Subscribed` en su primera sesión, cuando Braze solicita automáticamente un token de notificaciones push. En este punto, el usuario está **habilitado para push** con un token push válido para ese dispositivo y un estado de suscripción predeterminado de `Subscribed`.<br><br>
- **iOS**: No se registra automáticamente para push.
    - **iOS 12 (con autorización provisional)**: <br>Su aplicación puede solicitar [autorización provisional]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) o push autorizado. El push autorizado requiere el permiso explícito de un usuario antes de enviar cualquier notificación (recibe un token después de que el usuario conceda el permiso), mientras que [push provisional][provisional-blog] permite enviar notificaciones __silenciosamente__, directamente al centro de notificaciones sin ningún sonido o alerta.
    - **iOS 11 y posteriores e iOS 12 (sin autorización provisional)**: <br>Todos los usuarios deben optar explícitamente por recibir notificaciones push. Recibirá un token después de que los usuarios se hayan registrado.<br><br>
- **Web:** Debe solicitar el consentimiento explícito de los usuarios a través del cuadro de diálogo de permisos nativo del navegador. Recibirá un token después de que los usuarios hayan optado por la adhesión voluntaria.  A diferencia de iOS y Android, que permiten que tu aplicación muestre el aviso de permiso en cualquier momento, algunos navegadores modernos sólo lo muestran si se activa mediante un "gesto del usuario" (clic del ratón o pulsación de una tecla). Si tu sitio intenta solicitar permiso de notificación push al cargar la página, es probable que el navegador lo ignore o lo silencie.

| Obtener un token de notificaciones push | Enviar un token push |
| ---------------- | ----------------- |
| Las aplicaciones deben registrarse en un proveedor push para obtener un token de notificaciones push para un dispositivo. | A continuación, los desarrolladores pueden dirigirse al dispositivo utilizando el token de notificaciones push generado por FCM/APN.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comprobar el estado de la suscripción push del usuario

![Perfil de usuario de John Doe con su estado de suscripción push establecido en Suscrito.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de la suscripción push de un usuario con Braze:

1. **Perfil del usuario**: Puede acceder a perfiles de usuario individuales a través del panel de control de Braze en la página [Búsqueda de usuarios][5]. Después de encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID de usuario externo), puede seleccionar la pestaña **Compromiso** para ver y ajustar manualmente el estado de suscripción de un usuario. 
<br>
2. **Exportación de API REST**: Puede exportar perfiles de usuario individuales en formato JSON utilizando los puntos finales de exportación [Usuarios por segmento][segmento] o [Usuarios por identificador][identificador]. Braze devolverá un objeto de tokens push que contiene información de habilitación push por dispositivo.

### Comprobar el estado del registro push

En la pestaña **Participación** del perfil de un usuario, verá **Push Registered For** seguido del nombre de una aplicación. Si no existe información de la aplicación para ese dispositivo, verás dos guiones**(--**). Habrá una entrada para cada dispositivo que pertenezca al usuario.

Si el nombre de la aplicación de la entrada del dispositivo lleva el prefijo `Foreground:`, la aplicación está autorizada a recibir tanto notificaciones push en primer plano (visibles para el usuario) como notificaciones push en segundo plano (no visibles para el usuario) en ese dispositivo.

![Registro de cambios push con un token de notificaciones push de ejemplo.][2]{: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

Por otro lado, si el nombre de la aplicación de la entrada del dispositivo lleva el prefijo `Background:`, la aplicación sólo está autorizada a recibir [push en segundo plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/types/#background-push-notifications) y no puede mostrar notificaciones visibles para el usuario en ese dispositivo. Esto suele indicar que el usuario ha desactivado las notificaciones de la aplicación en ese dispositivo.

Si un token push se mueve a un usuario diferente en el mismo dispositivo, ese primer usuario ya no será registrado push.

## Tratamiento de token de notificaciones push

Consulte el siguiente gráfico para ver las acciones que provocan cambios en los tokens push o su eliminación de los perfiles de usuario. 

| Acción | Descripción |
| ------ | ----------- |
| `changeUser()` método llamado | El método Braze `changeUser()` cambia el ID de usuario al que los SDK asignan los datos de comportamiento del usuario. Este método suele llamarse cuando un usuario inicia sesión en una aplicación. Cuando se llama a `changeUser()` con un ID de usuario diferente o nuevo en un dispositivo específico, el token push de ese dispositivo se moverá al perfil Braze apropiado con el ID de usuario correspondiente. |
| Se produce un error de empuje | Algunos errores push comunes que llevan a la eliminación del token son `MismatchSenderId`, `InvalidRegistration`, y otros tipos de rebotes push. <br><br>Consulte nuestra lista completa de [errores push][errors] comunes. |
| El usuario desinstala | Cuando un usuario desinstale la aplicación de un dispositivo, Braze eliminará el token push del usuario del perfil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ¿Qué aspecto tiene esto a mayor escala?

Cuando un usuario abre una nueva aplicación y concede acceso push desde una solicitud push, se realiza una llamada desde el SDK de Braze a los proveedores push. Cuando se realiza esa llamada, el proveedor de push ejecuta una comprobación para ver si todo está configurado correctamente. Si es así, se pasa un token de notificaciones push a tu dispositivo. Cuando llega ese token, el SDK lo comunica a Braze. Después de que Braze haya recibido el token del proveedor de push, actualizamos o creamos un nuevo perfil de usuario. Estos usuarios se consideran ahora registrados.

Si queremos lanzar una campaña, creamos una campaña en Braze que genere una carga útil push para enviar al proveedor push. A partir de ahí, el proveedor entrega la carga útil push al dispositivo del usuario y el SDK pasa el estado de la mensajería a Braze.

![Un diagrama de flujo que mapea el proceso push antes mencionado entre Braze, el cliente y el servicio de notificaciones push de Apple o Firebase Cloud Messaging.][push-process]

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

[errors]: {{site.baseurl}}/help/help_articles/push/push_error_codes/#push-bounced-mismatchsenderid
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[push-process]: {% image_buster /assets/img/push_process.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[2]: {% image_buster /assets/img/push_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}


