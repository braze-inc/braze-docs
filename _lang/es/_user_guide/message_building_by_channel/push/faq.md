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

Cuando se reasigna un token de notificaciones push, el cambio se refleja en el **registro de cambios de notificaciones** del perfil de usuario. Puedes encontrarlo en la pestaña **«Interacción»** del perfil de usuario.

![El «Registro de cambios» en la sección «Configuración de contacto».]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### ¿Qué significa «Error al enviar la notificación push porque la carga útil no era válida»?

Este mensaje indica que APN rechazó la solicitud push debido a una carga útil no válida (por ejemplo, una carga útil vacía o una carga útil demasiado grande).

Para obtener más información y conocer los pasos siguientes, consulta [Mensajes de error comunes de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### ¿Por qué un usuario que ha realizado la adhesión voluntaria no tiene un token de notificaciones push?

Esto puede suceder si el token de notificaciones push del usuario se reasignó a otra persona que utilizó el mismo dispositivo.

1. Ve al registro **de cambios** en la pestaña **«Interacción»** del perfil de usuario afectado.
2. Busca un mensaje que indique que el token de notificaciones push se ha trasladado a otro usuario.
3. Copia el token de notificaciones push y pégalo en la barra de búsqueda de usuarios. 
4. Si el token de notificaciones push aún existe, se te redirigirá al usuario que haya iniciado sesión más recientemente en el dispositivo.

Si deseas que el token de notificaciones push se reasigne al usuario original:

1. Pide al usuario original que inicie sesión en el perfil con el token de notificaciones push que falta.
2. Desencadena un nuevo envío push. Esto devolverá el token a la cuenta si todavía tienes habilitada la función push en el dispositivo.

