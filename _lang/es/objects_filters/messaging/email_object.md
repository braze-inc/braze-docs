---
nav_title: "Objeto de correo electrónico"
article_title: Objeto de mensajería de correo electrónico
page_order: 5
page_type: reference
channel: email
description: "Este artículo de referencia explica los diferentes componentes del objeto de correo electrónico Braze."

---

# Objeto de correo electrónico

> El objeto `email` le permite modificar o crear correos electrónicos a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

## Objeto de correo electrónico

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address will get added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)
  - Cualquier `app_id` válido de una aplicación configurada en tu espacio de trabajo funcionará para todos los usuarios de tu espacio de trabajo, independientemente de si el usuario tiene la aplicación específica en su perfil o no.
- Para más información y mejores prácticas sobre preencabezados, consulta nuestro artículo de ayuda sobre [el estilo del cuerpo del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling).

{% alert warning %}
Braze recomienda evitar el uso de enlaces de Google Drive para los archivos adjuntos `url`, ya que esto puede bloquear las llamadas de nuestros servidores para obtener el archivo y provocar que el mensaje de correo electrónico no se envíe.
{% endalert %}

Los tipos de archivos adjuntos válidos son: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` y `pkpass`.

Se puede recuperar un `email_template_id` de la parte inferior de cualquier plantilla de correo electrónico creada con el editor HTML. A continuación se muestra un ejemplo del aspecto de este ID:

![Sección del identificador de la API de una plantilla de correo electrónico HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"} 

## Ejemplo de objeto de correo electrónico con archivo adjunto

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

## Autenticación de archivos adjuntos por correo electrónico

1. Vaya a **Configuración** > **Contenido conectado** y haga clic en **Añadir credencial** para añadir sus credenciales de autenticación.
2. Introduzca un nombre y añada un nombre de usuario y una contraseña.
3. En el objeto de correo electrónico del punto final `/messages/send`, incluye una propiedad `basic_auth_credential` que especifique el nombre de la credencial en los detalles del archivo adjunto. Consulte el siguiente ejemplo con el nombre de credencial `company_basic_auth_credential_name`:

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachment test",
      "from": "mail <mail@e.company.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

