---
nav_title: Mensajes comunes de error push
article_title: Mensajes de error push comunes
page_order: 22
page_type: reference
description: "Este artículo trata sobre los mensajes de error más comunes relacionados con las notificaciones push para iOS y Android, y te guía a través de las posibles soluciones."
channel: push
platform:
- iOS
- Android
---

# Mensajes comunes de error push

> Esta página recoge los mensajes de error más comunes relacionados con la mensajería push.

{% tabs %}
{% tab Android %} 
### El push rebotó: MismatchSenderId
`MismatchSenderId` indica un fallo de autenticación. Firebase Cloud Messaging (FCM) se autentica con un par de datos clave: el ID del remitente y la clave de API de FCM.  Ambos deben validarse para comprobar su exactitud. Para más información, consulta la [documentación de Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sobre este tema.

Los fallos más comunes pueden ser:
- [Identificación de remitente]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) incorrecta
- Registro múltiple si se registran en otro servicio push con un senderID diferente

### El push rebotó: InvalidRegistration
`InvalidRegistration` puede ocurrir cuando un token de notificaciones push está malformado. Los fallos más comunes pueden ser
- La gente está pasando tokens de registro Braze manualmente, pero no llaman a `getToken()`. Por ejemplo, pueden pasar el ID de instancia completo. El token que aparece en el mensaje de error es similar a `&#124;ID&#124;1&#124;:[regular token]`.  
- La gente se registra en varios servicios. Actualmente esperamos que las intenciones de registro push lleguen al estilo antiguo, así que si la gente se registra en varios sitios y captamos intenciones de otros servicios, podemos obtener tokens de notificaciones push malformados.

### El push rebotó: NoRegistrado
`NotRegistered` suele significar que la aplicación se ha eliminado del dispositivo (como nuestra señal de Desinstalar). Esto también puede ocurrir si se produce un registro múltiple y un segundo registro invalida el token de notificaciones push que recibe Braze.

{% endtab %}
{% tab iOS %}

### Error al enviar la notificación push porque la carga útil no era válida.

Este mensaje puede aparecer en la pestaña **Interacción** del perfil de usuario, en **Configuración de contacto** > **Registro de cambios push,** cuando el servicio de notificaciones push de Apple (APN) rechaza la solicitud push debido a una carga útil no válida.

En Braze, este mensaje del panel de control puede ser mapeado a uno de los siguientes motivos de error de APN:

- `PayloadEmpty`: La carga útil carecía del contenido necesario para el tipo de push que se estaba realizando.
- `PayloadTooLarge`: La carga útil superó el tamaño máximo de carga útil de APN.

Las causas más comunes incluyen:

- Las claves personalizadas (y sus valores) hacen que la carga útil sea demasiado grande (esto puede incluir valores renderizados por Liquid inesperadamente grandes).
- Una alerta o un cuerpo vacío o faltante donde sea necesario (o una carga útil mal`aps` formada).

Próximos pasos:

- Reduce el tamaño de la carga útil recortando las claves personalizadas y acortando los valores dinámicos grandes.
- Si envías a través de la API, valida la carga útil JSON final (incluido el tamaño) antes de enviarla.

### El push rebotó: BadToken

El`BadToken`error puede producirse por varias razones:
- El token de notificaciones push no se nos envía correctamente en `[[Appboy sharedInstance] registerPushToken:]`
	- Comprueba el token en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Por lo general, debería tener el aspecto de una larga cadena de letras y números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si no es así, comprueba el código relacionado con el envío de errores de tokens de notificaciones push de Braze.<br><br>
- Entorno de aprovisionamiento desajustado:
	- Si te registras con un certificado de desarrollador e intentas enviar con uno de producción, puedes ver este error.  
	- Braze sólo admite certificados universales para entornos de producción. Probar push en entornos de desarrollo con un certificado universal no funcionará. 
	- Este tipo de notificación rebota en producción, pero no en desarrollo.<br><br>
- Perfil de aprovisionamiento no coincidente:
	- Esto puede ocurrir si tu certificado no coincide con el que se utilizó para obtener el token. Si se sospecha de ello, estos son los próximos pasos:
		- Asegúrate de que el certificado push que se utiliza para enviar push desde el panel de Braze y el perfil de aprovisionamiento están configurados correctamente.
		- Vuelve a crear el certificado APNS y, a continuación, vuelve a crear el perfil de aprovisionamiento después de configurar el certificado APNS en `app_id`. Esto a veces puede resolver algunos problemas más visibles.

### El push rebotó: Se eliminó el servicio de respuesta APNS

Esto suele ocurrir cuando alguien desinstala. Braze consulta cada noche el servicio de retroalimentación APNS para obtener una lista de tokens no válidos. Para más información, consulta [Comunicación con APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) de Apple.

{% endtab %}
{% endtabs %}
