---
nav_title: "E-Mail-Objekt"
article_title: E-Mail Messaging Objekt
page_order: 5
page_type: reference
channel: email
description: "In diesem referenzierten Artikel werden die verschiedenen Komponenten des E-Mail-Objekts von Braze erläutert."

---

# E-Mail Objekt

> Mit dem Objekt `email` können Sie über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) E-Mails ändern oder erstellen.

## E-Mail Objekt

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

- [Bezeichner der App]({{site.baseurl}}/api/identifier_types/)
  - Jede gültige `app_id` von einer App, die in Ihrem Workspace konfiguriert ist, funktioniert für alle Nutzer:innen in Ihrem Workspace, unabhängig davon, ob der Nutzer die spezifische App in seinem Profil hat oder nicht.
- Weitere Informationen und bewährte Verfahren für Preheader finden Sie in unserem Hilfeartikel zur [Gestaltung von E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling).

{% alert warning %}
Braze empfiehlt, die Verwendung von Google Drive-Links für Ihre Anhänge `url` zu vermeiden, da dies die Aufrufe unserer Server zum Abrufen der Datei blockieren und dazu führen kann, dass die Nachricht nicht gesendet wird.
{% endalert %}

Gültige Anhangstypen sind: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` und `pkpass`.

Eine `email_template_id` kann am Ende jeder mit dem HTML-Editor erstellten E-Mail-Vorlage abgerufen werden. Im Folgenden sehen Sie ein Beispiel dafür, wie diese ID aussieht:

![API Bezeichner Abschnitt einer HTML E-Mail Vorlage.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"} 

## Beispiel für ein E-Mail-Objekt mit Anhang

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

## Authentifizierung für E-Mail Dateianhänge

1. Navigieren Sie zu **Einstellungen** > **Connected-Content** und klicken Sie auf **Zugangsdaten hinzufügen**, um Ihre Zugangsdaten hinzuzufügen.
2. Geben Sie einen Namen ein, und fügen Sie einen Benutzernamen und ein Passwort hinzu.
3. Fügen Sie in das E-Mail-Objekt des Endpunkts `/messages/send` eine Eigenschaft `basic_auth_credential` ein, die den Namen der Zugangsdaten in den Anlagedetails angibt. Referenzieren Sie auf das folgende Beispiel mit dem Zugangsdaten-Namen `company_basic_auth_credential_name`:

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

