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
- [ID de remitente]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) incorrecto
- Registro múltiple si se registran en otro servicio push con un senderID diferente

### El push rebotó: InvalidRegistration
`InvalidRegistration` puede ocurrir cuando un token de notificaciones push está malformado. Los fallos más comunes pueden ser:
- La gente pasa tokens de registro de Braze manualmente, pero no llama a `getToken()`. Por ejemplo, pueden pasar el ID de instancia completo. El token que aparece en el mensaje de error es similar a `&#124;ID&#124;1&#124;:[regular token]`.  
- La gente se registra en varios servicios. Actualmente esperamos que las intenciones de registro push lleguen al estilo antiguo, así que si la gente se registra en varios sitios y captamos intenciones de otros servicios, podemos obtener tokens de notificaciones push malformados.

### El push rebotó: NotRegistered {#notregistered}
`NotRegistered` suele significar que la aplicación se ha eliminado del dispositivo (como nuestra señal de desinstalación). Esto también puede ocurrir si se produce un registro múltiple y un segundo registro invalida el token de notificaciones push que recibe Braze.

### DEVICE_UNREGISTERED {#device-unregistered}

Este error aparece en el registro de actividad de mensajes como:

`Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Esto suele ocurrir por alguna de las siguientes razones:

- El usuario desinstaló la aplicación. Esta es la causa más común. Cuando la aplicación se elimina de un dispositivo, el token de notificaciones push deja de ser válido.
- Se actualizaron las credenciales push en la aplicación. Si tu equipo cambió las credenciales o certificados de FCM incluidos en la aplicación, los usuarios que se registraron con las credenciales anteriores tienen tokens no válidos hasta que la aplicación los vuelva a registrar.
- Una lógica personalizada está cancelando el registro de los usuarios de push. Esto es poco frecuente, pero es técnicamente posible cancelar programáticamente el registro de un dispositivo de push usando el SDK de Firebase/Android.

{% alert note %}
Este error no significa que el usuario tenga push deshabilitado, solo que un token específico fue eliminado de su perfil. Esto es habitual en usuarios que están probando funcionalidades e instalan y desinstalan la aplicación con frecuencia. Para comprobar si el usuario aún tiene tokens válidos, ve a **Búsqueda de usuarios** y revisa la sección **Configuración de contacto** en la pestaña **Interacción**.
{% endalert %}

{% endtab %}
{% tab iOS %}

### Error al enviar la notificación push porque la carga útil no era válida

Este mensaje puede aparecer en la pestaña **Interacción** del perfil de usuario, en **Configuración de contacto** > **Registro de cambios push**, cuando el servicio de notificaciones push de Apple (APN) rechaza la solicitud push debido a una carga útil no válida.

En Braze, este mensaje del dashboard puede corresponder a uno de los siguientes motivos de error de APN:

- `PayloadEmpty`: La carga útil carecía del contenido necesario para el tipo de push que se estaba enviando.
- `PayloadTooLarge`: La carga útil superó el tamaño máximo de carga útil de APN.

Las causas más comunes incluyen:

- Las claves personalizadas (y sus valores) hacen que la carga útil sea demasiado grande (esto puede incluir valores renderizados por Liquid inesperadamente grandes).
- Una alerta o un cuerpo vacío o faltante donde sea necesario (o una carga útil `aps` malformada).

Próximos pasos:

- Reduce el tamaño de la carga útil recortando las claves personalizadas y acortando los valores dinámicos grandes.
- Si envías a través de la API, valida la carga útil JSON final (incluido el tamaño) antes de enviarla.

### El push rebotó: BadToken

El error `BadToken` puede producirse por varias razones:
- El token de notificaciones push no se envía correctamente a Braze (por ejemplo, en `registerDeviceToken:` o el equivalente de tu plataforma).
	- Comprueba el token en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Por lo general, debería tener el aspecto de una larga cadena de letras y números (como `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si no es así, comprueba el código relacionado con el envío del token de notificaciones push a Braze.<br><br>
- Entorno de aprovisionamiento no coincidente:
	- Si te registras con un certificado de desarrollo e intentas enviar con uno de producción, puedes ver este error.  
	- Braze solo admite certificados universales para entornos de producción. Probar push en entornos de desarrollo con un certificado universal no funcionará. 
	- Este tipo de notificación rebota en producción, pero no en desarrollo.<br><br>
- Perfil de aprovisionamiento no coincidente:
	- Esto puede ocurrir si tu certificado no coincide con el que se utilizó para obtener el token. Si sospechas que este es el caso, los próximos pasos son:
		- Asegúrate de que el certificado push que se utiliza para enviar push desde el panel de Braze y el perfil de aprovisionamiento están configurados correctamente.
		- Vuelve a crear el certificado de APN y, a continuación, vuelve a crear el perfil de aprovisionamiento después de configurar el certificado de APN en `app_id`. Esto a veces puede resolver algunos problemas más visibles.

### ID de paquete no permitido

El error `TopicDisallowed` significa que APN rechazó la notificación push porque el tema (ID de paquete) en la solicitud no está permitido para las credenciales de autenticación que se están utilizando. Para resolverlo:

1. **Verifica el ID de paquete.** Confirma que el ID de paquete configurado en los ajustes de tu aplicación en Braze coincide exactamente con el ID de paquete de tu aplicación. Esto incluye cualquier variación de sufijo (por ejemplo, `.debug`, `.staging`).
2. **Comprueba tu configuración de autenticación de APN.** Confirma que tu aplicación está configurada con la clave `.p8` de APN correcta y que la clave está asociada al mismo equipo de desarrollador de Apple que la aplicación a la que estás enviando.
3. **Confirma el entorno de la aplicación.** Si tienes ID de aplicación separados en Braze para compilaciones de desarrollo y producción, verifica que cada uno esté configurado con las credenciales push y el entorno correctos.

### Unregistered {#ios-unregistered}

Este error aparece en el registro de actividad de mensajes como:

`Received 'Unregistered' sending to '[Token String]'`

Este es el equivalente en iOS del error [DEVICE_UNREGISTERED](#device-unregistered) de Android. Suele ocurrir por alguna de las siguientes razones:

- El usuario desinstaló la aplicación. Esta es la causa más común.
- Se actualizaron los certificados push. Si tu equipo cambió o renovó los certificados de APN, los usuarios que se registraron con los certificados anteriores pueden tener tokens no válidos hasta que la aplicación los vuelva a registrar.
- Una lógica personalizada está cancelando el registro de los usuarios de push. Esto es poco frecuente, pero es técnicamente posible cancelar programáticamente el registro de notificaciones remotas usando el SDK de iOS.

{% alert note %}
Este error no significa que el usuario tenga push deshabilitado, solo que un token específico fue eliminado de su perfil. Para comprobar si el usuario aún tiene tokens válidos, ve a **Búsqueda de usuarios** y revisa la sección **Configuración de contacto** en la pestaña **Interacción**.
{% endalert %}

### InvalidProviderToken

El error `InvalidProviderToken` significa que APN rechazó la solicitud porque el token de autenticación (de una clave `.p8`) o el certificado push (`.p12`) no coincide con el ID de paquete o el ID de equipo de la aplicación. Para resolverlo:

1. **Verifica tu ID de equipo y tu ID de clave:** Si estás usando una clave de autenticación `.p8`, confirma que el **ID de equipo** y el **ID de clave** configurados en el panel de Braze (**Configuración** > **Configuración de la aplicación** > selecciona tu aplicación iOS) coinciden con los valores de tu cuenta de desarrollador de Apple.
2. **Comprueba el ID de paquete:** Asegúrate de que el ID de paquete registrado en Braze coincide con el ID de paquete de tu aplicación. Una discrepancia, como una diferencia en mayúsculas o un sufijo `.debug`, causa este error.
3. **Vuelve a cargar la clave o el certificado:** Si la clave `.p8` o el certificado `.p12` se regeneró o revocó recientemente, carga la nueva clave en Braze y elimina la anterior.
4. **Confirma el entorno de APN:** Si estás usando un certificado `.p12`, verifica que seleccionaste el entorno correcto (desarrollo frente a producción) al cargarlo. Para las claves `.p8`, esto se gestiona automáticamente.

### El push rebotó: Se eliminó del servicio de retroalimentación de APN

Esto suele ocurrir cuando alguien desinstala la aplicación. Braze consulta cada noche el servicio de retroalimentación de APN para obtener una lista de tokens no válidos. Para más información, consulta [Comunicación con APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) de Apple.

{% endtab %}
{% endtabs %}