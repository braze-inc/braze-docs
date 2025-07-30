---
nav_title: Mensajería de usuarios
article_title: Mensajería de usuarios de LINE
page_order: 2
description: "Este artículo de referencia explica cómo chatear con los usuarios utilizando campañas con plantillas y Canvases."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Mensajería de usuarios de LINE

> LINE es un canal de comunicación bidireccional. Puedes ir más allá de enviar mensajes a los usuarios y entablar conversaciones con ellos utilizando campañas con plantillas y Canvases. Este artículo cubre los detalles de la mensajería a los usuarios, como por ejemplo cómo establecer palabras desencadenantes para mensajes entrantes y respuestas no reconocidas.

Existen varios métodos para conversar con los usuarios a través de LINE, como el uso de palabras activadoras de LINE. También puede utilizar llamadas a la acción (CTA) para fomentar el compromiso del usuario con su mensaje LINE.

## Activadores basados en acciones

Puede crear campañas y lienzos que comiencen, se ramifiquen y tengan cambios a mitad de camino cuando reciba un mensaje LINE entrante (un mensaje enviado por un usuario) que contenga una palabra desencadenante. Asegúrese de elegir palabras desencadenantes que coincidan con lo que espera que envíen los usuarios.

### Campaña

Configura tus palabras desencadenantes al programar una campaña de entrega basada en acciones.

![Acción desencadenante de "Enviar esta campaña a los usuarios que enviaron LÍNEA de entrada al grupo de suscripción donde está el cuerpo del mensaje" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Establezca sus palabras desencadenantes dentro de [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) en su Canvas.

![Ruta de acción con un desencadenante de "Enviar esta campaña a los usuarios que enviaron LÍNEA de entrada al grupo de suscripción donde está el cuerpo del mensaje" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requisitos

Cada letra de su palabra desencadenante debe ir en mayúscula al crear su campaña o Canvas, aunque Braze no exige que las palabras desencadenantes entrantes vayan en mayúscula. Por ejemplo, si su palabra desencadenante es "JOIN2023", un mensaje entrante de "jOin2023" seguirá desencadenando el Canvas o la campaña.

Si no se especifica ninguna palabra desencadenante, la campaña o el lienzo se ejecutarán para *todos los* mensajes LINE entrantes. Esto incluye los mensajes que tienen frases coincidentes en campañas activas y Lienzos, en cuyo caso el usuario recibirá dos mensajes LINE.

## Respuestas no reconocidas

Debe incluir una opción de activación para las respuestas no reconocidas en los lienzos interactivos. Esto informa a los usuarios de las indicaciones disponibles (o palabras desencadenantes) y establece sus expectativas para el canal.

### Creación de un disparador para respuestas no reconocidas

Después de crear grupos de acciones para las frases de filtro personalizadas, añada otro grupo de acciones a la ruta de acción para **Enviar mensaje de LÍNEA**, y no marque **Donde el cuerpo del mensaje**. Esto atrapará todas las respuestas de usuario no reconocidas, similar a una cláusula "else".

Para este mensaje, debe enviar un mensaje LINE informando al usuario de que este canal no está supervisado por un humano y, si es necesario, guiarle a un canal de soporte.

