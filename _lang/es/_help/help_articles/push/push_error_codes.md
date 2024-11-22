---
nav_title: Mensajes de error push comunes
article_title: Mensajes de error push comunes
page_order: 2

page_type: solution
description: "Este artículo de ayuda cubre los mensajes de error comunes relacionados con push para iOS y Android, y te guía a través de posibles soluciones."
channel: push
platform:
- iOS
- Android
---

# Mensajes comunes de error push

Consulta estos mensajes de error habituales en la mensajería push:

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

### El push rebotó: Error al enviar al token de notificaciones push malo

Este error puede producirse por varias razones:
- El token de notificaciones push no se nos envía correctamente en `[[Appboy sharedInstance] registerPushToken:]`
	- Comprueba el token en el **Registro de actividad de mensajes**. Por lo general, debería parecerse a una larga cadena de letras y números. (e.g `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`) Si no es así, comprueba el código implicado en el envío de errores del token de notificaciones push Braze.<br><br>
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

_Última actualización el 24 de enero de 2021_
