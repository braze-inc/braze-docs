---
nav_title: Usuarios de mensajería
article_title: Mensajería Usuarios de LINE
page_order: 2
description: "Este artículo de referencia explica cómo chatear con los usuarios utilizando plantillas de campañas y Lienzos."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Mensajería Usuarios de LINE

> LINE es un canal de comunicación bidireccional. Puedes ir más allá del envío de mensajes a los usuarios y entablar conversaciones con ellos utilizando plantillas de campañas y Lienzos. Este artículo cubre los detalles de la mensajería a los usuarios, como por ejemplo cómo establecer palabras desencadenantes para mensajes entrantes y respuestas no reconocidas.

Existen varios métodos para conversar con los usuarios a través de LINE, como utilizar las palabras desencadenantes de LINE. También puedes utilizar llamadas a la acción (CTA) para fomentar la interacción del usuario con tu mensajería LINE.

## Desencadenantes basados en la acción

Puedes crear campañas y Lienzos que se inicien, ramifiquen y tengan cambios a mitad de camino cuando recibas un mensaje entrante de LINE (un mensaje enviado por un usuario) que contenga una palabra desencadenante. Asegúrate de elegir palabras desencadenantes que coincidan con lo que esperas que envíen los usuarios.

### Campaña

Configura tus palabras desencadenantes al programar una campaña de entrega basada en acciones.

\![Acción desencadenante de "Enviar esta campaña a los usuarios que enviaron LÍNEA de entrada al grupo de suscripción donde está el cuerpo del mensaje" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Configura tus palabras desencadenantes dentro de [las rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) de tu Canvas.

\![Ruta de acción con un desencadenante de "Enviar esta campaña a los usuarios que enviaron LÍNEA de entrada al grupo de suscripción donde está el cuerpo del mensaje" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requisitos

Cada letra de tu palabra desencadenante debe ir en mayúsculas al crear tu campaña o Canvas, aunque Braze no exige que las palabras desencadenantes entrantes vayan en mayúsculas. Por ejemplo, si tu palabra desencadenante es "JOIN2023", un mensaje entrante de "jOin2023" seguirá desencadenando el Canvas o la campaña.

Si no se especifica ninguna palabra desencadenante, la campaña o Canvas se ejecutará para *todos los* mensajes LINE entrantes. Esto incluye los mensajes que tienen frases coincidentes en campañas y Lienzos activos, en cuyo caso el usuario recibirá dos mensajes de LINE.

## Respuestas no reconocidas

Deberías incluir una opción para desencadenar respuestas no reconocidas en los Lienzos interactivos. Esto informa a los usuarios de las indicaciones disponibles (o palabras desencadenantes) y establece sus expectativas para el canal.

### Crear un desencadenante de respuestas no reconocidas

Después de crear grupos de acción para las frases de filtrado personalizadas, añade otro grupo de acción a la ruta de acción para **Enviar mensaje de LINE**, y no marques **Dónde está el cuerpo del mensaje**. Esto atrapará todas las respuestas de usuario no reconocidas, de forma similar a una cláusula "else".

Para este mensaje, debes enviar un mensaje LINE informando al usuario de que este canal no está supervisado por un humano y, si lo necesita, guiarle a un canal de soporte.

