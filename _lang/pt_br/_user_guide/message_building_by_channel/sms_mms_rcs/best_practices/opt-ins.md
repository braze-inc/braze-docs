---
nav_title: "Coleta de aceitações de usuários"
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

Peça aos usuários para enviar uma mensagem de texto com "START", "UNSTOP", "YES" ou uma palavra-chave de aceitação personalizada para o seu número, adicionando-os automaticamente ao seu grupo de inscrições. No seu site, app móvel ou até mesmo em anúncios, você pode solicitar que os usuários façam isso para dar a aceitação e oferecer um incentivo, se for útil.

## Opção 2: Os usuários aceitam via mensagem no app

Para permitir que os usuários aceitem receber SMS a partir de uma mensagem no app, use o [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) fornecido pela Braze para criar um formulário personalizado com a sua marca que permite coletar números de telefone e aumentar sua lista de SMS.

![Criador de mensagens no app com um modelo para captura de número de telefone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

A Braze recomenda que você também use o recurso de [aceitação dupla por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Esse recurso funciona automaticamente com o formulário de captura de número de telefone da mensagem no app, solicitando que os usuários confirmem sua intenção após enviar seu número de telefone pelo formulário.

## Opção 3: Fluxo de inscrição

Quando um novo usuário se inscrever ou registrar no site ou app, peça o número de telefone e o e-mail. Inclua uma caixa de seleção para receber e-mails e SMS promocionais. 

Depois que o usuário se inscrever, faça o seguinte:

1. Use o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para criar o usuário e salvar seus atributos.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para inscrever o usuário em SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
Para inserir os usuários no fluxo de [aceitação dupla por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) ao inscrevê-los pela API REST, defina o parâmetro `use_double_opt_in_logic` como `true` na sua requisição. Se você omitir esse parâmetro, os usuários serão inscritos sem receber uma confirmação de aceitação dupla.

Esse parâmetro é compatível com os seguintes endpoints:<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}