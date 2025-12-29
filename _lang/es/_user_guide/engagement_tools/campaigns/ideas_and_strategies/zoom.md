---
nav_title: Automatizar el registro de Zoom
article_title: Automatizar el registro de Zoom
page_order: 1
page_type: tutorial
description: "Este artículo describe cómo automatizar el registro de asistentes a Zoom en tus campañas de correo electrónico, push y mensajes dentro de la aplicación."
channel: 
  - email
  - push
  - in-app messages

---

# Automatizar el registro de Zoom

> Los seminarios web se han convertido en algo habitual para los clientes de Braze en los últimos años. Al organizar un seminario web de Zoom, los usuarios deben introducir sus datos en una página de destino de Zoom para registrarse. 

A continuación se expone un flujo de usuarios recomendado:
1. Programa un seminario web en Zoom y genera un `webinarId`.
2. Utiliza Braze para promocionar los seminarios web de Zoom a través de correo electrónico, push y canales de mensajería dentro de la aplicación. 
3. Incluye un botón de llamada a la acción en estas comunicaciones que añada automáticamente usuarios al seminario web.

Esto se puede conseguir utilizando [las API de Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) para añadir automáticamente a un usuario a un seminario web mediante un clic en un botón dentro de un correo electrónico, push o mensaje dentro de la aplicación. Utiliza el siguiente punto final, sustituyendo el ID del seminario web en la solicitud API. 

POST: `/meetings/{webinarId}/registrants`

Para más información, consulta el [punto final de](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) Zoom [Añadir participantes al seminario web](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate).<br><br>

{% tabs %}
{% tab Email %}

Crea una campaña de correo electrónico con un botón de llamada a la acción dentro del cuerpo del mensaje. Cuando un usuario haga clic en el botón, redirígele a la página de destino del seminario web (con los parámetros adecuados incluidos en el enlace de redirección). 

Utilizando los parámetros de la URL para pasar los datos de usuario, crea una llamada a la API que se dispare cuando se cargue la página para añadir al usuario al seminario web.

\![Mensaje de correo electrónico con plantilla Liquid utilizada para incluir nombre, apellidos, dirección de correo electrónico y ciudad.]({% image_buster /assets/img/zoom/zoom1.png %})

Los usuarios ya están registrados para el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% tab Push %}

1. Crear una campaña push<br><br>

	Establece el comportamiento del botón al hacer clic para enlazar con la página de inicio del seminario web.<br>

	Enlace al seminario web cuando se hace clic en un botón.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Un ejemplo sencillo de página de aterrizaje para usuarios que se registran a través de un clic de botón desde un push. Informa al usuario de para qué se ha registrado y confirma su inscripción:<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Crea una campaña webhook desencadenada por el mensaje dentro de la aplicación o el clic en un botón.<br><br>
 	Utilizando los datos de usuario existentes en su perfil de Braze, registra al usuario para el seminario web.<br>

	Una campaña basada en acciones que se enviará a los usuarios que hayan hecho clic en un botón de una campaña concreta.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Ejemplo de llamada webhook al endpoint Zoom.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Los usuarios ya están registrados para el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% tab In-app message %}

1. Crea una campaña de mensajes dentro de la aplicación<br><br>

	Configurar el comportamiento del botón al hacer clic para enlazar con la página de inicio del seminario web<br>

	Enlace al seminario web cuando se hace clic en un botón.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Un ejemplo sencillo de página de destino para usuarios que se registran haciendo clic en un botón desde un mensaje dentro de la aplicación. Informa al usuario de para qué se ha registrado y confirma su inscripción:<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Crea una campaña webhook desencadenada por el mensaje dentro de la aplicación o el clic en un botón.<br><br>
	Utilizando los datos de usuario existentes en su perfil de Braze, registra al usuario para el seminario web.<br>

	Una campaña basada en acciones que se enviará a los usuarios que hayan hecho clic en un botón de una campaña concreta.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Ejemplo de llamada webhook al endpoint Zoom.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Los usuarios ya están registrados para el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% endtabs %}
