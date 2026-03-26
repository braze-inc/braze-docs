---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre push
page_order: 25
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas push."
page_type: FAQ
channel:
  - Push
---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre el canal push.

### ¿Qué sucede cuando varios usuarios inician sesión en un solo dispositivo?

Cuando un usuario cierra sesión en un dispositivo o sitio web, seguirá estando disponible mediante notificaciones push hasta que otro usuario inicie sesión. En ese momento, el token de notificaciones push se reasigna al nuevo usuario. Esto se debe a que cada dispositivo solo puede tener una suscripción push activa por aplicación o sitio web.

Cuando se reasigna un token de notificaciones push, el cambio se refleja en el **registro de cambios push** del perfil de usuario. Puedes encontrarlo en la pestaña **Interacción** del perfil de usuario.

![El «Registro de cambios push» en la sección «Configuración de contacto».]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Cuando envío una notificación push de prueba, ¿se envía a todos mis dispositivos?

Sí. La notificación push de prueba se envía a todos los dispositivos con push habilitado asociados al perfil de usuario seleccionado. Si tienes varios teléfonos o tabletas con la sesión iniciada con el mismo usuario, cada dispositivo con un token de notificaciones push válido recibirá la notificación.

Para enviar la notificación push de prueba a un solo dispositivo, puedes eliminar los tokens de notificaciones push de los demás dispositivos del perfil de usuario antes de realizar la prueba. Alternativamente, si estás enviando con el [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), establece `send_to_most_recent_device_only` en `true` en el objeto `apple_push` o `android_push` para que solo el dispositivo activo más reciente reciba la notificación push.

### ¿Qué significa «Error al enviar la notificación push porque la carga útil no era válida»?

Este mensaje indica que APN rechazó la solicitud push debido a una carga útil no válida (por ejemplo, una carga útil vacía o una carga útil demasiado grande).

Para obtener más información y conocer los pasos siguientes, consulta [Mensajes de error comunes de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### ¿Por qué un usuario con adhesión voluntaria no tiene un token de notificaciones push?

Esto puede suceder si el token de notificaciones push del usuario se reasignó a otra persona que utilizó el mismo dispositivo.

1. Ve al **registro de cambios push** en la pestaña **Interacción** del perfil del usuario afectado.
2. Busca un mensaje que indique que el token de notificaciones push se trasladó a otro usuario.
3. Copia el token de notificaciones push y pégalo en la barra de búsqueda de usuarios. 
4. Si el token de notificaciones push aún existe, se te redirigirá al usuario que haya iniciado sesión más recientemente en el dispositivo.

Si deseas que el token de notificaciones push se reasigne al usuario original:

1. Pide al usuario original que inicie sesión en el perfil con el token de notificaciones push faltante.
2. Desencadena un nuevo envío push. Esto devolverá el token a la cuenta si todavía tiene habilitada la función push a nivel de dispositivo.

### ¿Cuál es la diferencia entre «Enviar a producción» y «Enviar a desarrollo» en los certificados push de iOS?

Al añadir un certificado push de Apple en Braze, las opciones **Enviar a producción** y **Enviar a desarrollo** determinan qué puerta de enlace de APN (servicio de notificaciones push de Apple) utiliza Braze para entregar las notificaciones push:

- **Enviar a desarrollo:** selecciona esta opción si la aplicación se compiló en modo de desarrollo en Xcode y se firmó con un perfil de aprovisionamiento de desarrollo. Las notificaciones push se enrutan a través de la puerta de enlace de desarrollo (sandbox) de Apple.
- **Enviar a producción:** selecciona esta opción si la aplicación se distribuye a través de TestFlight de Apple, App Store o distribución empresarial. Las notificaciones push se enrutan a través de la puerta de enlace de producción de Apple.

Si se selecciona la opción incorrecta, las notificaciones push fallan silenciosamente porque el tipo de token de notificaciones push no coincide con la puerta de enlace. Normalmente, las aplicaciones distribuidas a través de TestFlight o App Store deben usar **Enviar a producción**.