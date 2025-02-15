---
nav_title: Poucas impressões de mensagens no app
article_title: Poucas impressões de mensagens no app
page_order: 2

page_type: solution
description: "Este artigo de ajuda aborda as ações que podem ser tomadas se as impressões de mensagens no app forem menores do que você gostaria."
channel: in-app messages
---
# Poucas impressões de mensagens no app

Se suas impressões forem mais baixas do que você gostaria, recomendamos que verifique:
* [Tamanho do segmento](#segment-size)
* [Changelogs](#segment-changelogs)
* [Executar testes](#run-tests)
* [Eventos de gatilho](#event-triggers)
* [Impressões de mensagens](#message-impressions)

## Tamanho do segmento

É importante garantir que o tamanho de seu segmento na campanha reflita o público-alvo. Pode haver filtros aplicados que estejam limitando seu público e fazendo com que sua campanha tenha menos impressões.

## Changelogs de segmentos

Se a contagem de impressões estiver baixa em comparação com o que era antes, verifique se ninguém alterou involuntariamente o segmento ou a campanha desde o lançamento. Nossos changelogs de segmentos e campanhas lhe darão insights sobre as alterações feitas, quem fez a alteração e quando ela ocorreu.

![Link para visualizar o changelog na página Detalhes da campanha com sete alterações desde que o usuário visualizou a campanha pela última vez][10]

## Executar testes

Uma maneira rápida de identificar problemas óbvios é clonar a campanha, direcionar seu próprio ID de usuário ou e-mail e lançar a campanha. Depois de disparar a mensagem (início da sessão, evento personalizado, etc.), verifique se você recebeu a mensagem corretamente. Em seguida, navegue até o dashboard e atualize a página para ver se a sua impressão foi registrada corretamente. Se não for, então o problema provavelmente está em sua implementação.

## Eventos de gatilho

Se a campanha for disparada por um início de sessão ou por um evento personalizado, é preciso garantir que esse evento ou sessão esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique esses dados nas páginas [Overview (Visão geral)][1] (para dados de sessão) ou [Custom Events (Eventos personalizados)][2]:

![A página Eventos personalizados mostra um gráfico do número de vezes que o evento personalizado Adicionado aos favoritos ocorreu em um período de um mês][11]

## Impressões de mensagens

A personalização da interface do usuário de mensagens no app ou dos mecanismos de entrega no SDK pode exigir que os desenvolvedores utilizem nossos métodos para registrar manualmente as impressões de mensagens no app. Verifique com seus desenvolvedores se você usa a personalização de mensagens no app para:
  * [iOS][12] 
  * [Android][13] 

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 6 de maio de 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
