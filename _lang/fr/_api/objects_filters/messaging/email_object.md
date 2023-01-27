---
nav_title: "Objet E-mail"
article_title: Objet d’e-mail
page_order: 5
page_type: reference
channel: email
description: "Cet article explique les différents composants de l’objet E-mail de Braze."

---

# Spécification de l’objet E-mail

L’objet `email` vous permet de modifier ou de créer des e-mails via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Corps
```json
{
  "app_id": (required, string), voir identifiant de l’application,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set) - utilisez « NO_REPLY_TO » pour définir l’adresse de réponse sur « Vide »,
  "bcc": (optional, one of the BCC addresses defined in your app group's email settings) S’il est fourni et que la fonctionnalité BCC est activée pour votre compte, cette adresse sera ajoutée à votre message émis en tant qu’adresse CCI.,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) Longueur recommandée entre 50 et 100 caractères,
  "email_template_id": (optional, string) Si elle est fournie, elle utilisera les valeurs subject/body/should_inline_css du modèle d’e-mail donné SAUF si elles sont spécifiées ici, auquel cas nous substituerons le modèle fourni.,
  "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi,
  "extras": (optional, valid Key-Value Hash), hachage supplémentaire ; pour les clients SendGrid, il sera transmis à SendGrid en tant qu’arguments uniques,
  "headers": (optional, valid Key-Value Hash), hachage des en-têtes des extensions personnalisées. Pris en charge uniquement pour les clients SendGrid actuellement.,
  "should_inline_css": (optional, boolean), si du CSS doit être inséré dans le corps. S’il n’est pas fourni, il revient sur la valeur d’insertion du CSS par défaut pour le groupe d’apps.,
  "attachments": (optional, array), array d’objets JSON qui définit les fichiers que vous devez attacher, définis par « file_name » et « url »,
    "file_name": (required, string) le nom du fichier que vous désirez attacher à votre e-mail sans son extension (par ex., « .pdf »). Vous pouvez attacher autant de fichiers que vous désirez jusqu’à 2 MB. Ceci est obligatoire si vous utilisez des « pièces jointes »,
    "url": (required, string) l’URL correspondante du fichier que vous désirez joindre à votre e-mail. L’extension du nom de fichier sera détectée automatiquement à partir de l’URL défini, ce qui devrait renvoyer le « Content-Type » adéquat en tant qu’en-tête de réponse. Ceci est obligatoire si vous utilisez des « pièces jointes »,
}
```

- [Identifiant d’application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)
- Pour plus d’informations et les meilleures pratiques sur les accroches, consultez notre article d’aide sur le [style des corps de l’e-mail][46].

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
            "file_name":"LeNomDeVotreFichier",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

[31]: {% image_buster /assets/img_archive/email_template_id.png %}
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling
