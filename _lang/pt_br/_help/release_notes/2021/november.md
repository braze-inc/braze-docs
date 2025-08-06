---
nav_title: Novembro
page_order: 1
noindex: true
page_type: update
description: "Este artigo contém notas de versão para novembro de 2021."
---
# Novembro de 2021

## métrica de relatório de taxa de clique para abertura
Braze adicionou uma nova métrica de e-mail, taxa de cliques por abertura, disponível no [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). Esta métrica representa a porcentagem de e-mails abertos que foram clicados.

## Métrica de abertura por máquina

Uma nova métrica de e-mail, [Máquina Abre]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), está disponível nas páginas de Canva e Análise de Dados de campanhas para e-mails. Esta métrica identifica aberturas de e-mail que não são humanas (como as abertas pelos servidores da Apple), exibidas como um subconjunto do total de aberturas.

## Variável do Liquid random_bucket_number
Uma variável `random_bucket_number` foi adicionada à lista de [variáveis Liquid suportadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) para personalização de mensagens. 

## Diretrizes de notificação por Rich Push do iOS 15
Novas [diretrizes de notificação por push do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) foram adicionadas aos documentos ricos do iOS, incluindo informações sobre estados de notificação e uma análise das variáveis de truncamento de texto.

## IPs para lista de permissões na UE para webhooks e conteúdo conectado
IPs extras para adicionar à lista de permissões na UE para webhooks e conteúdo conectado foram adicionados ao nosso artigo de [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) e [conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Estes novos IPs incluem `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` e `3.70.107.88`.

## Ponto de extremidade de exportação de compras
Um novo [`/purchases/product_list` endpoint]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) foi adicionado ao Braze. Este endpoint retorna listas paginadas de IDs de produtos.

## Novas parcerias Braze

### Adobe - plataforma de dados do cliente
A integração Braze e [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permite que as marcas conectem e mapeiem seus dados Adobe (atributos personalizados e segmentos) ao Braze em tempo real. As marcas podem então agir com base nesses dados, oferecendo experiências personalizadas e direcionadas a esses usuários. 

### BlueConic - plataforma de dados do cliente
Com [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), os usuários do Braze podem unificar dados em perfis individuais persistentes e, em seguida, sincronizá-los em pontos de contato e sistemas de clientes para apoiar uma ampla gama de iniciativas focadas no crescimento, incluindo orquestração do ciclo de vida do cliente, modelagem e análise de dados, produtos e experiências digitais, monetização baseada em público e mais.

### Digno - conteúdo dinâmico
A integração da Braze e [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) permite que você crie facilmente experiências personalizadas e ricas no app usando o editor de conteúdo dinâmico de arrastar e soltar do Worthy e as entregue através da Braze.

### Judo - Conteúdo dinâmico
A integração entre [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) e Braze permite que você substitua componentes de sua campanha e os substitua por experiências Judo. Os dados da Braze podem ser usados para apoiar conteúdo personalizado em uma experiência de Judo. Eventos do usuário e dados da experiência podem ser retroalimentados na Braze para atribuição e direcionamento.

### LINE - envio de mensagens
A integração [LINE]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) e Braze permite que você aproveite os webhooks, segmentação avançada, personalização e recursos de disparo da Braze para enviar mensagens aos seus usuários no LINE através da [API de envio de mensagens do LINE](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Pagamentos
A integração [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) e Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição do seu cliente em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição de seus clientes, como engajar com clientes que optaram por sair durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento.

### Punchh - Fidelidade
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) fez parceria com Braze para sincronizar dados entre as duas plataformas para fins de presentes e fidelidade. Os dados publicados no Braze estarão disponíveis para segmentação e podem sincronizar dados de usuários de volta ao Punchh por meio de templates de webhook configurados no Braze.  