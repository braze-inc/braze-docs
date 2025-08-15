---
nav_title: "Objeto e-mail"
article_title: Objeto envio de mensagens de e-mail
page_order: 5
page_type: reference
channel: email
description: "Este artigo de referência explica os diferentes componentes do objeto de e-mail do Braze."

---

# Objeto de e-mail

> O objeto `email` permite que você modifique ou crie e-mails através dos nossos endpoints de [envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

## Objeto de e-mail

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

- [Identificador do app]({{site.baseurl}}/api/identifier_types/)
  - Qualquer `app_id` válido de um app configurado no seu espaço de trabalho funcionará para todos os usuários no seu espaço de trabalho, independentemente de o usuário ter ou não o app específico em seu perfil.
- Para saber mais e melhores práticas sobre pré-cabeçalhos, consulte nosso artigo de ajuda sobre [estilização do corpo do e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling).

{% alert warning %}
A Braze recomenda que você evite usar links do Google Drive para os seus anexos `url`, pois isso pode bloquear as chamadas dos nossos servidores para obter o arquivo e resultar no não envio da mensagem de e-mail.
{% endalert %}

Tipos de anexos válidos incluem: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf` e `pkpass`.

Um `email_template_id` pode ser recuperado do rodapé de qualquer modelo de e-mail criado com o editor de HTML. O seguinte mostra um exemplo de como esse ID se parece:

![Seção do Identificador da API de um modelo de e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"} 

## Exemplo de objeto de e-mail com anexo

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

## Autenticação para anexos de arquivos de e-mail

{% alert important %}
A autenticação para anexos de arquivos de e-mail neste endpoint está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

1. Navegue para **Configurações** > **Conteúdo Conectado** e clique em **Adicionar Credencial** para adicionar suas credenciais de autenticação.
2. Digite um nome e adicione um nome de usuário e senha.
3. No objeto de e-mail do endpoint `/messages/send`, inclua uma propriedade `basic_auth_credential` especificando o nome da credencial nos detalhes do anexo. Consulte o seguinte exemplo com o nome da credencial `company_basic_auth_credential_name`:

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

