---
nav_title: Visão geral da Shopify (legado)
article_title: "Visão geral da Shopify (legado)"
description: "Este artigo de referência descreve a parceria com a Braze e a Shopify, uma empresa de comércio global, que permite conectar sua loja da Shopify com a Braze para passar webhooks selecionados da Shopify para a Braze. Aproveite as estratégias de mensagens integradas entre canais da Braze e o canva para incentivar os clientes a completarem suas compras ou redirecionar os usuários com base nas compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Visão geral da Shopify (legado)

> A [Shopify](https://www.shopify.com/) é uma empresa de comércio global líder que fornece ferramentas confiáveis para abrir, expandir, comercializar e gerenciar um negócio de varejo de qualquer tamanho. A Shopify torna o comércio melhor para todo mundo com uma plataforma e serviços projetados para confiabilidade, enquanto oferece uma melhor experiência de compra para consumidores em todos os lugares.

A integração da Shopify e da Braze permite que você conecte sua loja da Shopify para transferir seus dados do Shopify para a Braze com praticidade. Você pode aproveitar estratégias multicanal e canva no Braze para engajar novos leads, enviar mensagens para novos clientes ou redirecionar seus usuários com envio de mensagens de carrinho abandonado para incentivá-los a concluir suas compras.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Recursos suportados

- Monitorar o comportamento no site e usuários anônimos via SDK para Web da Braze
- Ajudar na sincronização e reconciliação de clientes da Shopify na Braze via SDK para Web da Braze
- Sincronizar dados de cliente do Shopify
- Coletar os estados de aceitação de inscrição de e-mail e SMS da Shopify
- Preencher dados históricos de compras da Shopify 
- sincronização de catálogo do Shopify 
- Use mensagens no app como um canal 

## Casos de uso suportados 

- Campanhas de jornada de compra e jornadas de usuário do canva, incluindo: 
  - Abandono de navegação 
  - Carrinho abandonado 
  - Checkout abandonado 
- Campanhas pós-compra e jornadas do usuário na canva, incluindo:
  - Confirmações de pedidos 
  - Atualizações de cumprimento 
  - Cancelamentos de pedidos 
  - Reembolsos de pedidos
- Recomendações de produtos
- Venda cruzada e upsell
- [De volta ao estoque]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Loja da Shopify | Você tem uma loja [Shopify](https://www.shopify.com/) ativa.<br><br>Você pode conectar uma loja Shopify por espaço de trabalho. Se você estiver interessado em conectar várias lojas a um único espaço de trabalho, entre em contato com seu gerente de sucesso do cliente para participar do beta de Múltiplas Lojas do Shopify. |
| Permissões de usuário do Shopify | Você tem uma das seguintes permissões para sua loja da Shopify:{::nomarkdown}<ul><li>Proprietário da loja</li><li>Equipe</li><li>Membro com todas as configurações Gerais e da Loja Online, bem como estas permissões adicionais de administrador:<ul><li>Pedidos</li><li>Ver (localizado em <b>Produtos</b>)</li><li>Clientes</li><li>Gerenciar configurações</li><li>Ver aplicativos desenvolvidos por funcionários e colaboradores</li><li>Gerencie e instale aplicativos e canais</li></ul></li></ul>{:/} |
| Implementação do Braze Web SDK | Para rastrear o comportamento no site e usuários anônimos, você deve implementar o Braze Web SDK através da nossa integração padrão com o Shopify ou manualmente. <br><br>Para saber mais sobre suas opções de implementação, consulte [Como implementar o SDK para Web no seu site da Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify). |
| Segmentação de propriedade de evento ativada | Para confirmar que você pode segmentar as propriedades dos eventos do Shopify, trabalhe com seu gerente de sucesso do cliente ou [suporte da Braze]({{site.baseurl}}/braze_support/) para confirmar que a segmentação de propriedades de eventos está ativada no seu dashboard da Braze. |
{: .reset-td-br-1 .reset-td-br-2 }

## Regulamento Geral sobre a Proteção de Dados (GDPR)

Com relação aos dados pessoais enviados aos serviços da Braze por seus clientes ou em nome deles, a Braze é a processadora de dados, e nossos clientes são os controladores de dados. Assim sendo, a Braze processa esses dados pessoais exclusivamente sob a instrução de nossos clientes e, quando aplicável, notifica nossos clientes sobre solicitações de titulares de dados. Como controladores de dados, nossos clientes respondem diretamente às solicitações dos titulares dos dados. Como parte da integração do Shopify na plataforma Braze, a Braze recebe automaticamente [os webhooks de GDPR do Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). No entanto, os clientes da Braze são, em última instância, responsáveis por responder às solicitações de titulares de dados de seus clientes do Shopify através do uso de [SDKs da Braze]({{site.baseurl}}/developer_guide/home/) ou [APIs REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) de acordo com nossas políticas de [conformidade com o GDPR]({{site.baseurl}}/dp-technical-assistance/).
