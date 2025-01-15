---
nav_title: As mensagens no app não estão sendo exibidas
article_title: As mensagens no app não estão sendo exibidas
page_order: 1

page_type: solution
description: "Este artigo de ajuda o orienta na solução de problemas com mensagens no app que não são exibidas ou renderizadas corretamente."
channel: in-app messages
---

# As mensagens no app não estão sendo exibidas

Se descobrir que as mensagens no app não estão sendo exibidas ou renderizadas corretamente, há várias abordagens a serem verificadas:

* [Eventos de gatilho](#event-triggers)
* [Impressões de mensagens](#message-impressions)
* [Testes](#run-tests)
* [Tempo limite da sessão](#session-timeout)
* [Intervalo de envio de mensagens](#minimum-interval)

## Eventos de gatilho

Se a campanha for disparada por um início de sessão ou por um evento personalizado, é preciso garantir que esse evento ou sessão esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique esses dados nas páginas [Overview (Visão geral)][1] (para dados de sessão) ou [Custom Events (Eventos personalizados)][2]:

![A página Eventos personalizados mostra um gráfico do número de vezes que o evento personalizado Adicionado aos favoritos ocorreu em um período de um mês][14]

## Impressões de mensagens

A personalização da interface do usuário de mensagens no app ou dos mecanismos de entrega no SDK pode exigir que os desenvolvedores utilizem nossos métodos para registrar manualmente as impressões de mensagens no app. Verifique com seus desenvolvedores se você usa a personalização de mensagens no app.

## Executar testes

É importante determinar se o evento de gatilho não está ocorrendo ou se a mensagem em si não está sendo exibida. Para testar, dispare a mensagem usando uma ação diferente (como o início de uma sessão ou outro evento personalizado) e verifique se ela é exibida. Isso ajudará a isolar se esse é um possível problema de dados.

Como alternativa, tente usar um tipo diferente de modelo de mensagem no app ou tamanho de imagem. Há [especificações para mensagens no app][15] que devem ser seguidas. Às vezes, se uma imagem for muito grande, ela impedirá a exibição da mensagem no app.

## Tempo limite da sessão

Descubra se você personalizou o tempo limite da sessão. Por padrão, a Braze recupera do servidor as mensagens no app no início de uma sessão.

Se o tempo limite da sessão tiver sido estendido, o período de tempo a partir do qual podemos atualizar as possíveis mensagens no app para as quais você é elegível será estendido. Além disso, se a sua campanha estiver configurada para disparar a partir do início de uma sessão, será necessário garantir que o tempo apropriado tenha passado para que uma nova sessão seja registrada. Por exemplo, o tempo limite da sessão pode ter sido personalizado para ser de 30 segundos. Se você abrir e fechar o app em menos de 30 segundos, não será elegível para receber outra mensagem no app disparada no início da sessão. 

Saiba mais sobre como personalizar os tempos limite da sessão para as seguintes plataformas:
* [iOS][16]
* [Android][17]
* [Web][18]

## Intervalo mínimo

Há um intervalo mínimo no qual permitiremos que mensagens no app sejam disparadas consecutivamente, portanto, você pode estar tentando dispará-las muito rapidamente. Saiba mais sobre o intervalo mínimo para as seguintes plataformas: 
* [iOS][19]
* [Android][20]
* [Web][21]

Embora os intervalos sejam personalizáveis, ainda os temos em vigor para evitar o envio excessivo de mensagens aos usuários.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 15 de julho de 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
