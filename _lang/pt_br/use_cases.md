---
nav_title: Casos de uso da API
article_title: Casos de uso da API
description: "Seja você um desenvolvedor experiente ou um profissional de marketing com recursos mínimos de desenvolvimento, este artigo de referência foi criado para ajudá-lo a entender como aproveitar o poder da Braze REST API para realizar várias tarefas e aprimorar sua estratégia de engajamento do cliente."
page_type: reference
page_order: 4.8
---

# Casos de uso da API

> A [Braze REST API]({{site.baseurl}}/api/basics/) fornece uma ampla gama de endpoints projetados para ajudar a gerenciar e otimizar sua estratégia de engajamento do cliente. Neste artigo, exploraremos vários casos de uso para cada coleção de endpoints: catálogos, listas e endereços de e-mail, exportação, mensagens, Central de Preferências, SMS, grupos de inscrições, modelos e dados de usuários.<br><br>Cada seção apresenta um cenário com um guia passo a passo, exemplo de código e resultado esperado. Ao final deste artigo, você entenderá melhor como usar a REST API da Braze para aprimorar seus esforços de engajamento do cliente.

## Exclusão de vários itens em um catálogo

Um novo ano traz lançamentos de novos produtos na Kitchenerie, uma marca de varejo especializada em utensílios de cozinha. No painel do Braze, a Kitchenerie tem um catálogo configurado para sua coleção de louças chamado "Dishware". Esse novo ano também significa a remoção dos seguintes produtos de sua coleção de louças.

* Bisque simples
* Porcelana Pérola
* Rosa cintilante

Para remover esses produtos de seu catálogo, a Kitchener pode usar o [endpoint`/catalogs/{catalog_name}/items` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) para passar os IDs dos itens.

Aqui está o exemplo de solicitação:

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

Depois de enviar essa carga útil, a resposta a seguir confirma que as três coleções foram removidas com êxito do catálogo de louças da Kitchenerie.

```json
{
  "message": "success"
}
```

## Remoção de e-mails da lista de spam do Braze

Na MovieCanon, uma empresa de serviços de streaming, a equipe de desenvolvedores é responsável por auditar periodicamente suas listas de e-mail para identificar e manter os usuários que estão inscritos em suas campanhas de e-mail. Como parte dessa auditoria, a MovieCanon deseja remover essa lista de e-mails de sua lista de spam:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

Para realizar essa tarefa, a equipe de desenvolvedores precisará de uma chave de API com a permissão `email.spam.remove` para usar o endpoint `/email/spam/remove`. Esse endpoint remove endereços de e-mail da lista de spam do Braze e da lista de spam mantida pelo provedor de e-mail do MovieCanon.

Para enviar essa solicitação, inclua um endereço de e-mail string ou um vetor de até 50 endereços de e-mail para modificar. Como a lista de e-mails a serem removidos é inferior a 50, o MovieCanon pode realizar essa tarefa com o seguinte corpo de solicitação:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

Depois de enviar essa carga útil com êxito, essa resposta confirma que os e-mails foram removidos da lista de spam do MovieCanon.

```json
{
  "message": "success"
}
```

## Auditoria de todas as telas

O Siege Valley Health é um sistema hospitalar que inclui 10 hospitais em funcionamento e centros de pesquisa com milhares de pacientes. Sua equipe de marketing quer comparar as telas enviadas aos pacientes para lembrá-los de marcar uma consulta para vacinação contra a gripe nos últimos três anos de uso do Braze. A equipe de marketing da Siege Valley Health também quer uma maneira rápida e eficiente de ver a lista de telas e o resumo da análise de dados.

Vamos nos aprofundar em como a Siege Valley Health pode realizar essas duas tarefas usando uma combinação de endpoints em vez de filtrar pelo dashboard do Braze.

Para a primeira tarefa de auditoria de Canvas, use o [ponto de extremidade`/canvas/list` ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) para exportar uma lista de Canvas que inclua o nome e as tags. Aqui está um exemplo de solicitação:

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

Vamos passar para a próxima tarefa de visualizar o resumo da análise de dados do primeiro Canvas da lista de Canvas do Siege Valley Health. Para isso, usaríamos o [ponto de extremidade`/canvas/data_summary` ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) com os seguintes parâmetros de solicitação:

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

Aqui está um exemplo de solicitação:

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Verificação das próximas campanhas e telas programadas

A época mais movimentada do ano está se aproximando rapidamente para a Flash & Thread, uma marca de varejo que vende roupas e produtos de beleza on-line e em lojas. Sua equipe de marketing deseja verificar as próximas campanhas e canvas no dashboard do Braze antes de 31 de março de 2024, às 12 horas. Isso pode ser feito usando o [endpoint`/messages/scheduled_broadcasts` ]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/). 

Aqui está o exemplo de solicitação:

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

Esse endpoint retornará a lista de campanhas e canvas futuras. A partir daqui, a equipe de marketing pode confirmar sua lista de mensagens consultando o campo `name` para as campanhas e Canvas na resposta.

## Visualização de uma Central de Preferências antiga

A PoliterWeekly é uma revista digital cujos assinantes podem ser contatados por e-mail. Em um esforço para entender melhor a jornada do usuário de seus assinantes, a equipe de marketing deseja revisar os detalhes da Central de Preferências do PoliterWeekly para verificar quando ela foi criada e atualizada pela última vez.

Usando o [ponto de extremidade`/preference_center/v1/{preferenceCenterExternalID}` ]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), a equipe de marketing só precisa inserir a ID externa da Central de Preferências como parâmetro de jornada, que teria a seguinte aparência:

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

Com base nessa resposta, a equipe de marketing pode ver que a Central de Preferências foi criada 3 anos antes de sua atualização mais recente. Com essas informações em mente, a equipe de marketing poderia criar e lançar uma nova Central de Preferências.

{% enddetails %}

## Remoção de números de telefone inválidos

Na CashBlastr, o objetivo principal é simplificar a forma como as pessoas podem enviar e receber pagamentos rápidos. Como uma empresa de serviços financeiros, a CashBlastr deseja manter a lista de números de telefone dos clientes atualizada e precisa. A equipe de desenvolvedores foi encarregada de remover a seguinte lista de números de telefone marcados como "inválidos" para que as mensagens por SMS da equipe de marketing possam alcançar os clientes apropriados da CashBlastr.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

Para enviar uma solicitação com o [endpoint`/sms/invalid_phone_numbers/remove` ]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/), os números de telefone precisam estar em um vetor de strings no [formatoe.164 ](https://en.wikipedia.org/wiki/E.164), com até 50 números de telefone por solicitação. Como a lista não ultrapassa 50 números de telefone, aqui está um exemplo do corpo da solicitação que a equipe de desenvolvedores da CashBlastr enviaria:

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

Depois de enviar essa carga útil, a resposta a seguir confirma que os números de telefone inválidos da CashBlastr foram removidos da lista de inválidos do Braze.

```json
{
  "message": "success"
}
```

## Visualização do status do grupo de inscrições de um usuário

A SandwichEmperor é uma cadeia de restaurantes de serviço rápido nos Estados Unidos, e sua equipe de marketing deseja verificar os status do grupo de inscrições de uma lista aleatória de seus usuários por SMS. Usando o [endpoint`/subscription/status/get` ]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), o SandwichEmperor pode realizar essa tarefa para um usuário individual com o seguinte exemplo de solicitação:

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

Esse ponto de extremidade também lista os status do grupo de inscrições para e-mail de um usuário e pode ser usado para ver o status do grupo de inscrições de vários usuários.

## Verificação de um modelo HTML para envio de mensagens por e-mail

Na WorkFriends, uma rede social que ajuda a criar conexões entre trabalhadores de diferentes setores, sua equipe de marketing é responsável pelo envio de campanhas de e-mail para seus usuários. Essas campanhas geralmente incluem lembretes de eventos no local, boletins informativos semanais e destaques de atividades de perfil.

Nesse cenário, a WorkFriends tem usado historicamente um modelo HTML Singular com sua marca antiga. Em um esforço para alinhar a identidade de sua marca, a WorkFriends deseja verificar se há alguma informação útil nesse modelo HTML para aproveitar antes de fazer a transição para um novo modelo.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

Depois de revisar essas informações de modelo, a WorkFriends também pode usar o [endpoint`/templates/email/update` ]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) para atualizar o modelo de e-mail por meio da API. O modelo de e-mail no dashboard do Braze refletirá essas edições.
