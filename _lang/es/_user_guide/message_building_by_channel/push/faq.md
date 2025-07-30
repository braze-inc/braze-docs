---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre push
page_order: 80
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas push."
page_type: FAQ
channel:
  - Push
---

# Preguntas más frecuentes

> Este artículo responde a algunas preguntas frecuentes sobre el canal push.

### ¿Qué ocurre cuando varios usuarios inician sesión en un mismo dispositivo?

Cuando un usuario se desconecta de un dispositivo o sitio web, permanecerá accesible mediante push hasta que otro usuario se conecte. En ese momento, el token de notificaciones push se reasigna al nuevo usuario. Esto se debe a que cada dispositivo sólo puede tener una suscripción push activa por aplicación o sitio web.

Cuando se reasigna un token de notificaciones push, el cambio se refleja en el registro de cambios push del perfil de usuario. Puedes encontrarlo yendo a la pestaña **"Interacción"** del perfil de usuario.

![El "Registro de cambios push" en la sección "Configuración de contactos".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### ¿Por qué un usuario con adhesión voluntaria no tiene un token de notificaciones push?

Esto puede ocurrir si el token de notificaciones push del usuario fue reasignado a otra persona que utilizó el mismo dispositivo.

1. Ve **al registro de cambios push** en la pestaña de **interacción** del perfil del usuario afectado.
2. Busca un mensaje que diga que el token de notificaciones push se ha movido a otro usuario.
3. Copia el token de notificaciones push y pégalo en la barra de búsqueda de usuarios. 
4. Si el token de notificaciones push sigue existiendo, se te dirigirá al usuario que haya iniciado sesión más recientemente en el dispositivo.

Si quieres que el token de notificaciones push se reasigne al usuario original:

1. Haz que el usuario original inicie sesión en el perfil con el token de notificaciones push que falta.
2. Desencadena un nuevo envío push. Esto devolverá el token a la cuenta si todavía tiene habilitada la función push en el dispositivo.

