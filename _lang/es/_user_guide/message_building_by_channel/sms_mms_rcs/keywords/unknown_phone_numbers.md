---
nav_title: Tratamiento de números de teléfono desconocidos
article_title: Tratamiento de números de teléfono desconocidos
page_order: 4
description: "Este artículo de referencia explica cómo procesa Braze los números de teléfono desconocidos de nuevos usuarios."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Tratamiento de números de teléfono desconocidos - nuevos usuarios

> Puede que después de poner en marcha los SMS, MMS y RCS con Braze, recibas mensajes de usuarios desconocidos. Los siguientes pasos describen cómo se procesan un usuario y un número no identificados.

## Flujo de trabajo Opt-in/out y palabras clave personalizadas para números desconocidos

Braze se dirige automáticamente a un número desconocido de una de estas tres maneras:

1. Si se envía un mensaje de texto con una palabra clave:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Suscribe al usuario al grupo de suscripción correspondiente en función de la palabra clave de suscripción recibida por Braze.<br><br>
2. Si se envía una palabra clave de adhesión voluntaria:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Cancela la suscripción del usuario del grupo de suscripción correspondiente en función de la palabra clave de cancelación recibida por Braze.<br><br>
3. Si se escribe cualquier otra palabra clave personalizada:
  * Braze ignora el mensaje de texto y no hace nada.

