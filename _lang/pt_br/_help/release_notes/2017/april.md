---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão de abril de 2017."
---

# Abril de 2017

## Mensagens no navegador em HTML

Agora, oferecemos suporte a tipos de mensagens interativas no navegador, incluindo HTML personalizado e formatos de captura de e-mail, o que o capacita a alcançar seus clientes onde quer que eles estejam. Saiba mais sobre as [mensagens no app][48].

## Mensagem personalizada no app com conteúdo conectado

Adicionamos os blocos {% raw %} {%connected_content%} {% endraw %} nas mensagens no app disparadas, o que permite adicionar personalização avançada inserindo qualquer informação acessível via API diretamente em suas mensagens. Agora, você pode usar os conteúdos conectados dentro do seu app, além de push, e-mail e webhooks. Saiba mais sobre o [Connected Content][34].

## Navegação aprimorada para cartões do feed de notícias

Melhoramos a interface do usuário para a criação de cartões do Feed de notícias, facilitando a navegação e a criação de suas campanhas. Saiba mais sobre os [cartões do Feed de notícias][33].

## Prévia aprimorada das notificações Rich do iOS

Nossas notificações prévias no iOS agora exibem notificações Rich, oferecendo uma visão clara do que exatamente está sendo enviado aos seus clientes, até o tamanho da fonte. Saiba mais sobre as [notificações Rich do iOS][32].

## Adição de "aberturas por influência" às estatísticas de push

Adicionamos "aberturas por influência" à nossa lista de estatísticas padrão de campanha e canvas oferecidas no Braze, facilitando o conhecimento do detalhamento de aberturas influenciadas, diretas e totais de suas campanhas. Saiba mais sobre as [aberturas por influência][31].

## Fazer upgrade para grupos internos

Agora é possível criar vários grupos internos e atribuir propriedades que indicam se o grupo será usado para registro de SDK, registro de API REST ou teste de conteúdo de mensagens. Saiba mais sobre os [registros de usuários de eventos][30].

> Atualizar: Os grupos internos também podem ser usados para o [envio de e-mails de teste]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## Novas opções para URLs da Web

Agora você tem a opção de abrir URLs da Web em um navegador externo para mensagens push, mensagens no app e no navegador e cartões do Feed de notícias. A ação "Deep Link into App" agora também é compatível com deep links HTTP/HTTPS. Se estiver usando um parceiro como a Branch ou o Universal Links da Apple, você precisará personalizar o SDK. Saiba mais sobre o [deep linking][29].

## Novo canvas de evento "Conversão realizada"

Adicionamos um novo evento "Performed Conversion" (Conversão realizada) e um filtro "In Canva Control" (Controle na tela) para melhorar as opções de redirecionamento. Saiba mais sobre o uso de [filtros de redirecionamento][28].



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
