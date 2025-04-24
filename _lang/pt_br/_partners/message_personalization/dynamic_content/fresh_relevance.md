---
nav_title: Nova relevância
article_title: Nova relevância
description: "Este artigo de referência descreve a parceria entre o Braze e a Fresh Relevance, uma plataforma de personalização versátil que permite incluir produtos relevantes em suas campanhas e telas do Braze."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Nova relevância

> [O Fresh Relevance][1] é uma solução de personalização versátil que capacita as empresas orientadas para o comércio a criar experiências personalizadas entre canais com facilidade. A plataforma economiza seu tempo, integra-se à sua pilha de tecnologia e permite que você ofereça experiências personalizadas de clientes que aumentam a conversão em seu site, app, e-mails, SMS e anúncios, sem depender de sua equipe de TI.

A integração entre a Braze e o Fresh Relevance permite que você:
* Envie campanhas avançadas de e-mail disparadas, como queda de preço, volta ao estoque, navegação em várias etapas ou mensagens de abandono de carrinho.
* Inclua conteúdo personalizado nos e-mails disparados, como recomendações do produto com base no produto pesquisado pelo cliente ou em itens da mesma categoria.
* Personalize as campanhas de envio de e-mail em massa com recomendações orientadas por IA, tempos de contagem regressiva, previsões do tempo em tempo real, feeds de redes sociais e muito mais.
* Aumente o banco de dados de e-mail com novos contatos coletados por meio de pop-ups de captura de dados.
* Identifique os visitantes do site que chegam por meio de um link de e-mail do Braze.

## Pré-requisitos

| Requisito | Descrição |
|-------------| ----------- |
| Conta Fresh Relevance  | É necessário ter uma conta Fresh Relevance para aproveitar essa parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões suficientes para os endpoints listados abaixo. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][3]. Seu endpoint dependerá da URL do Braze para sua instância. |
| ID da campanha do Braze | A campanha padrão do Braze que você deseja usar para enviar e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para configurar a integração no Fresh Relevance, você deve criar um canal do Braze em **Canais de envio de mensagens** e usar o canal em disparadores ou conteúdo apropriados do Fresh Relevance, conforme necessário. 

Para obter instruções passo a passo, faça login no no Fresh Relevance e siga [a documentação][2].

O sistema Fresh Relevance se comunicará com a Braze usando a chave de API fornecida. Uma integração completa faz uso dos seguintes pontos de extremidade da Braze API:

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/