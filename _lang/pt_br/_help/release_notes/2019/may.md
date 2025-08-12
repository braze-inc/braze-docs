---
nav_title: Maio
page_order: 8
noindex: true
page_type: update
description: "Neste artigo você encontra as notas de versão de maio de 2019."
---

# Maio de 2019

## Cartões de conteúdo

Os Cartões de Conteúdo são conteúdos persistentes que aparecem nas experiências de app e web dos clientes.

Com os Cartões de Conteúdo, você pode enviar um fluxo altamente segmentado e dinâmico de conteúdo rico para seus clientes diretamente nos aplicativos que eles amam, sem interromper sua experiência. Ou, você pode emparelhar os Cartões de Conteúdo com outros canais, como e-mail ou notificações por push, para ativar estratégias de marketing coesas.

![Feed de Cartões de Conteúdo]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Além disso, os Cartões de Conteúdo suportam recursos mais personalizados, incluindo fixação de cartão, descarte de cartão, entrega baseada em API, tempos de expiração de cartão personalizados, análise de dados de cartão.

Use isso para criar centros de notificação, feeds de página inicial e feeds de promoção.

Você precisará atualizar para uma versão compatível do SDK da Braze:
- iOS: 3.8.0 ou posterior
- Android: 2.6.0 ou posterior
- Web: 2.2.0 ou posterior

[Saiba mais sobre os Cartões de Conteúdo aqui!]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)

{% alert update %}
Cartões de Conteúdo para Currents e nossa documentação da API para cartões de conteúdo serão lançados no final desta semana. Fique de olho!
{% endalert %}

## Adição da plataforma Roku

Braze adicionou um novo canal às nossas capacidades! Ao expandir para novos canais, podemos ativar nossos clientes a enriquecer seus dados ao entender o comportamento de visualização ou fornecer experiências significativas aos seus consumidores em todos os canais relevantes.

Agora você pode [recuperar dados de dispositivos Roku]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) para enriquecimento de dados e rastreamento de eventos personalizados.

## Preferências de notificação para canva ou atualizações de campanha

Esta [nova notificação]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) irá alertá-lo via e-mail quando uma campanha ou canva for ativada, atualizada, reativada ou desativada. Ative isso em **Preferências de Notificação** na sua conta Braze.

## Documentação do parceiro tecnológico da Jampp

A Jampp é uma plataforma de marketing de performance para aquisição e redirecionamento de clientes móveis. Combina dados comportamentais com tecnologia preditiva e programática para gerar receita para os anunciantes, mostrando anúncios pessoais e relevantes que inspiram os consumidores a comprar pela primeira vez ou com mais frequência.

Os clientes da Braze podem [integrar-se com a Jampp]({{site.baseurl}}/partners/jampp/) configurando o canal de webhook da Braze para transmitir eventos para a Jampp. Como resultado, os clientes conseguem adicionar conjuntos de dados mais ricos às suas iniciativas de redirecionamento com a Jampp dentro do ecossistema de publicidade móvel.

## Seletor de plataforma para mensagens no app

Tornamos mais fácil selecionar para onde suas mensagens no app estão indo e para quais plataformas elas são construídas com nosso seletor de plataforma, que enfatiza esta etapa no processo de criação da campanha.

![Selecionador de Plataforma]({% image_buster /assets/img/iam_platforms.gif %})

## Campo de Correntes de ID de despacho para e-mail

{% alert update %}
O comportamento para `dispatch_id` difere entre canva e campanhas porque a Braze trata as etapas do canva (exceto as etapas de entrada, que podem ser agendadas) como eventos acionados, mesmo quando estão "agendadas". Saiba mais sobre o [comportamento `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) no canva e nas campanhas.

_Atualização registrada em agosto de 2019._
{% endalert %}

No esforço para continuar aprimorando nossas capacidades de Currents, estamos adicionando `dispatch_id` como um campo para eventos de e-mail do Currents em todos os tipos de conector.

O `dispatch_id` é o ID único gerado para cada transmissão ou envio, enviado da plataforma Braze.

Embora todos os clientes que recebem uma mensagem agendada recebam o mesmo `dispatch_id`, os clientes que recebem mensagens baseadas em ações ou acionadas por API receberão um `dispatch_id` único por mensagem. O campo `dispatch_id` permite que você identifique qual instância de uma campanha recorrente é responsável pela conversão, fornecendo assim mais insights e informações sobre quais tipos de campanhas estão ajudando a push a agulha em seus objetivos de negócios.

## Recurso de classificação da campanha "Mostrar Apenas Minhas"

Quando um usuário marca a caixa de seleção `Only Show Mine` na grade da campanha, os resultados serão filtrados para mostrar apenas as campanhas criadas pelo usuário logado. Além disso, o usuário pode usar a barra de pesquisa inserindo `created_by_me:true`.

Além disso, a barra lateral da grade da campanha agora é redimensionável!

## Excluir usuários por alias

Agora você pode usar o endpoint `users/delete` para [excluir usuários por alias]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Cálculo único para cliques e aberturas de e-mail

Cliques Únicos e Aberturas Únicas para e-mail agora são capturados e exibidos em um período de 7 dias por usuário e incrementam uma contagem de 1 dentro dessa janela de 7 dias, por cada `dispatch_id`.

Usar `dispatch_id` permite que mensagens recorrentes reflitam a verdadeira contagem de abertura única ou clique único de cada mensagem. Será fácil para os clientes administrarem esses dados, agora que o `dispatch_id` está disponível no Currents.

Qualquer usuário que também use o Mailjet verá um aumento nesses números, já que o período de exclusividade anterior era superior a 30 dias. Deveriam ter informado você sobre essa mudança três (3) semanas atrás.  Os clientes do SendGrid não devem notar nenhuma diferença.

Você pode procurar por esses termos atualizados em nosso [glossário de métricas de relatórios]({{site.baseurl}}/user_guide/data/report_metrics/).

{% alert update %}
O comportamento para `dispatch_id` difere entre canva e campanhas porque a Braze trata as etapas do canva (exceto as Etapas de Entrada, que podem ser agendadas) como eventos disparados, mesmo quando estão "agendadas". [Saiba mais sobre o [comportamento `dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) em canvas e campanhas.

_Atualização registrada em agosto de 2019._
{% endalert %}


## Canal mais engajado

{% alert update %}
A partir do [lançamento do produto de novembro de 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite), "Canal mais engajado" foi renomeado para ["Canal inteligente"]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/).
{% endalert %}

O filtro de Canal Mais Engajado seleciona a parte do seu público para quem o canal de envio de mensagens selecionado é o seu "melhor" canal. Neste caso, "melhor" significa "tem a maior probabilidade de engajamento, dado o histórico do usuário". Você pode selecionar e-mail, web push ou push móvel (que inclui qualquer sistema operacional móvel ou dispositivo disponível) como um canal.

Confira este novo filtro em nossa [Biblioteca de Filtros de Segmentação]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

