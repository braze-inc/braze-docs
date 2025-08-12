---
nav_title: Asociación con Twilio
alias: /partners/twilio/

description: "Este artículo describe la asociación entre Braze y Twilio."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Ten en cuenta que la compatibilidad con la integración de Twilio Webhook se interrumpirá el 31 de enero de 2020. Si deseas seguir accediendo a los servicios SMS con Braze, consulta nuestra [documentación sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).
{% endalert %}

En este ejemplo, configuraremos el canal webhook Braze para enviar SMS y MMS a tus usuarios, a través de la [API de envío de mensajes](https://www.twilio.com/docs/api/rest/sending-messages) de Twilio. Para tu comodidad, en el panel se incluye una plantilla de webhook de Twilio.

## HTTP URL

Twilio proporciona la URL del webhook en tu panel. Esta URL es única para tu cuenta Twilio, ya que contiene el ID de tu cuenta Twilio (`TWILIO_ACCOUNT_SID`).

En nuestro ejemplo de Twilio, la URL del webhook es `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Puedes encontrar esta URL en la sección *Primeros pasos* de la consola de Twilio.

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Cuerpo de la solicitud

La API de Twilio espera que el cuerpo de la solicitud esté codificado como URL, así que tenemos que empezar por cambiar el tipo de solicitud en el compositor del webhook Braze a `Raw Text`. Los parámetros necesarios para el cuerpo de la petición son *A*, *De* y *Cuerpo*.

La siguiente captura de pantalla es un ejemplo del aspecto que podría tener tu solicitud si estás enviando un SMS al número de teléfono de cada usuario, con el cuerpo "¡Hola de Braze!".

- Necesitarás tener números de teléfono válidos en cada perfil de usuario de tu audiencia objetivo.
- Para cumplir con el formato de solicitud de Twilio, utiliza el filtro `url_param_escape` de Liquid en el contenido de tus mensajes. Este filtro codifica una cadena para que todos los caracteres estén permitidos en una petición HTML; por ejemplo, el carácter más (`+`) en el número de teléfono `+12125551212` está prohibido en los datos codificados en URL y se convertirá en `%2B12125551212`.

![Cuerpo del webhook]({% image_buster /assets/img_archive/Webhook_Body.png %})

## Encabezados de solicitud y método

Twilio requiere dos encabezados de solicitud, el tipo de contenido de la solicitud y un encabezado de [autenticación básica HTTP](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Añádelos a tu webhook haciendo clic en el icono de engranaje situado junto al compositor del webhook y, a continuación, haciendo clic dos veces en *Añadir nuevo par*.

Nombre de la cabecera | Valor de cabecera
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Autorización | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Asegúrate de sustituir `TWILIO_ACCOUNT_SID` y `TWILIO_AUTH_TOKEN` por los valores de tu panel de Twilio. Por último, el punto final de la API de Twilio espera una solicitud HTTP POST, así que elige esa opción en el desplegable de *Método HTTP*.

![Método webhook]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Vista previa de tu solicitud

Utiliza el compositor del webhook para obtener una vista previa de la solicitud para un usuario aleatorio, o para un usuario con unas credenciales concretas, para asegurarte de que la solicitud se procesa correctamente.

![Vista previa del webhook]({% image_buster /assets/img_archive/Webhook_Preview.png %})

