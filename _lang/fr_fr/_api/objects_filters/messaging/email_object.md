---
nav_title: "Objet E-mail"
article_title: Objet Messagerie e-mail
page_order: 5
page_type: reference
channel: email
description: "Cet article de référence explique les différents composants de l’objet E-mail de Braze."

---

# Objet E-mail

> L'objet `email` vous permet de modifier ou de créer des e-mails par l'intermédiaire de nos [points d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging)

## Objet E-mail

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

- [Identifiant d’application]({{site.baseurl}}/api/identifier_types/)
  - Toute adresse `app_id` valide provenant d'une application configurée dans votre espace de travail fonctionnera pour tous les utilisateurs de votre espace de travail, que l'utilisateur ait ou non l'application spécifique sur son profil.
- Pour plus d'informations et de bonnes pratiques sur les accroches, consultez notre article d'aide sur le [style du corps de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling)

{% alert warning %}
Braze recommande d’éviter d’utiliser les liens Google Drive pour les `url` de pièces jointes, car cela peut bloquer les appels de nos serveurs pour obtenir le fichier ce qui empêche l’envoi d’e-mails.
{% endalert %}

Les types de fichiers joints valides comprennent : `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` et `pkpass`.

Un `email_template_id` peut être récupéré au bas des modèles d’e-mail créés avec l’éditeur HTML. Voici un exemple de ce à quoi ressemble cet ID :

![Section de l'identifiant API d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"} 

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

## Authentification des pièces jointes aux e-mails

{% alert important %}
L'authentification des pièces jointes aux e-mails dans cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

1. Naviguez vers **Paramètres** > **Contenu connecté** et cliquez sur **Ajouter un justificatif** pour ajouter vos justificatifs d'authentification.
2. Entrez un nom, puis ajoutez un nom d'utilisateur et un mot de passe.
3. Dans l'objet E-mail de l’endpoint `/messages/send`, incluez une propriété `basic_auth_credential` spécifiant le nom de l’identifiant dans les détails de la pièce jointe. Reportez-vous à l'exemple suivant avec le nom d’identifiant `company_basic_auth_credential_name` :

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachement test",
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

