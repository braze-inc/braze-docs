---
nav_title: "Coletando Opt-Ins do Usuário"
article_title: Melhores Práticas para Coletar Opt-Ins de SMS de Usuários
page_order: 7
description: "Este artigo de referência abrange três melhores práticas para coletar aceitações de usuários."
page_type: reference
channel:
  - SMS
  
---

# Coleta de aceitações de usuários

> O artigo a seguir lista alguns métodos comuns de aceitação de SMS.

## Opção 1: Peça aos usuários para enviar uma mensagem de texto para seu código curto ou longo

Peça aos usuários para enviar uma mensagem de texto com "START", "UNSTOP", "YES" ou uma palavra-chave de aceitação personalizada para o seu número para adicioná-los automaticamente ao seu grupo de inscrições. No seu site, app móvel ou até mesmo anúncios, é possível solicitar que os usuários façam isso para dar a aceitação, e você pode oferecer um incentivo se for útil.

## Opção 2: Os usuários aceitam via mensagem no app

Para permitir que os usuários optem por SMS a partir de uma mensagem no app, use o [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) fornecido pela Braze para criar um formulário com a marca que permite coletar números de telefone e aumentar sua lista de SMS.

![Criador de mensagens no app com um modelo para captura de número de telefone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recomenda que você também use o recurso de [aceitação dupla por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Este recurso funciona automaticamente com o formulário de captura de número de telefone {mensagem no app}, solicitando que os usuários confirmem sua intenção após enviar seu número de telefone através do formulário.

## Opção 3: Fluxo de inscrição

Quando um novo usuário se inscrever ou registrar no site ou app, peça seu número de telefone e e-mail. Incluir uma caixa de seleção para receber e-mails e SMS promocionais. 

Depois que o usuário se inscrever, faça o seguinte:

1. Use o [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para criar o usuário e salvar seus atributos.

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\. Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para inscrever o usuário em SMS.

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

