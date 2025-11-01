---
nav_title: "Coleta de opt-ins de usuários"
article_title: Práticas recomendadas para a coleta de opt-ins de SMS de usuários
page_order: 7
description: "Este artigo de referência aborda três práticas recomendadas para coletar opt-ins de usuários."
page_type: reference
channel:
  - SMS
  
---

# Coleta de opt-ins de usuários

> O artigo a seguir lista alguns métodos comuns de opt-in de SMS.

## Opção 1: Peça aos usuários que enviem um texto com seu código curto ou longo

Peça aos usuários que enviem uma mensagem de texto com "START", "UNSTOP", "YES" ou uma palavra-chave personalizada de opt-in para o seu número para adicioná-los automaticamente ao seu grupo de assinatura. Em seu site, aplicativo móvel ou até mesmo em anúncios, você pode solicitar que os usuários façam isso para optar por participar, e pode oferecer um incentivo se isso for útil.

## Opção 2: Usuários optam por participar por meio de mensagem no aplicativo

Para permitir que os usuários optem pelo SMS a partir de uma mensagem no aplicativo, use o [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) fornecido pelo Braze para criar um formulário de marca que lhe permita coletar números de telefone e aumentar sua lista de SMS.

Compositor de mensagens no aplicativo com um modelo para captura de número de telefone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

A Braze recomenda que você também use o recurso de [double opt-in do SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Esse recurso funciona automaticamente com o formulário de captura de número de telefone de mensagem in-app, solicitando que os usuários confirmem sua intenção depois de enviar o número de telefone por meio do formulário.

## Opção 3: Fluxo de registro

Quando um novo usuário se inscrever ou se registrar no site ou aplicativo, solicite o número de telefone e o e-mail dele. Inclua uma caixa de seleção para receber e-mails promocionais e SMS. 

Depois que o usuário se inscrever, faça o seguinte:

1. Use o [ponto de extremidade`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para criar o usuário e salvar seus atributos.

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
2\. Use o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para inscrever o usuário no SMS.

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

