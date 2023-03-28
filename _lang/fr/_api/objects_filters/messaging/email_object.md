---
nav_title: "Objet E-mail"
article_title: Objet Messagerie e-mail
page_order: 5
page_type: reference
channel: email
description: "Cet article de référence explique les différents composants de l’objet E-mail de Braze."

---

# Spécification de l’objet E-mail

Le `email` vous permet de modifier ou de créer des e-mails via nos [endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging).

## Corps
```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) If provided and the BCC feature is enabled for your account, this address will get added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the App Group,
  "attachments": (optional, array), array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you would like to attach to your email, excluding the extension (e.g., ".pdf"). You can attach any number of files up to 2MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you would like to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [Identifiant d’application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)
- Pour plus d’informations et les meilleures pratiques sur les accroches, consultez notre article d’aide sur le [style des corps de message][46].

{% alert warning %}
Braze recommande d’éviter d’utiliser les liens Google Drive pour les `url` de pièces jointes, car cela peut bloquer les appels de nos serveurs pour obtenir le fichier ce qui empêche l’envoi d’e-mails.
{% endalert %}

Les types de fichiers joints valides comprennent : `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` et `pkpass`.

Un `email_template_id` peut être récupéré au bas des modèles d’e-mail créés avec l’éditeur HTML. Voici un exemple de ce à quoi ressemble cet ID :

![Section Identifiant API d’un modèle d’e-mail HTML][31]

## Exemple d’objet d’e-mail avec pièce jointe

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

[31]: {% image_buster /assets/img_archive/email_template_id.png %}
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling
