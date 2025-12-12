---
nav_title: Painel de desempenho do canal
article_title: Painel de desempenho do canal
page_order: 2
page_type: reference
description: "Este artigo de referência aborda o Channel Performance Dashboard (Painel de desempenho do canal), que permite que você visualize as métricas de desempenho de canais inteiros em campanhas e Canvases."
tool: 
  - Reports

---

# Painel de desempenho do canal

> Os painéis de desempenho do canal mostram as métricas de desempenho agregadas de um canal inteiro, tanto das campanhas quanto dos Canvases. Atualmente, esses painéis estão disponíveis para e-mail e SMS.

Painel de desempenho de e-mail que exibe o envolvimento do canal de e-mail nos últimos trinta dias.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

Você pode visualizar os seguintes painéis:
- [Painel de desempenho de e-mail](#email-performance-dashboard)
- [Painel de insights de e-mail](#email-insights-dashboard)
- [Painel de desempenho de SMS](#sms-performance-dashboard)

## Painel de desempenho de e-mail

Visualize seu painel de desempenho de e-mail acessando **Analytics** > **Email Performance** e selecionando o intervalo de datas para o período em que deseja visualizar os dados. Seu intervalo de datas pode ser de até um ano no passado.

### Como as métricas são calculadas

\![Um exemplo de campanha de e-mail com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Os cálculos para diferentes métricas no painel de desempenho de e-mail são os mesmos que aqueles em um nível de mensagem individual (como a análise de campanha). Nesse painel, as métricas são agregadas em todas as campanhas e Canvases para o intervalo de datas que você selecionou. Para saber mais sobre essas definições, consulte [Métricas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Cada bloco mostra primeiro a métrica de taxa, seguida pela métrica de contagem (com exceção de *Envios*, que exibe a métrica de contagem seguida pela média por dia). Por exemplo, o bloco de cliques exclusivos contém a *taxa de cliques exclusivos* do período de tempo selecionado e a contagem do número total de cliques exclusivos desse período de tempo. Cada bloco também mostra a [comparação com o último período](#comparing-time-periods).

| Métrico | Tipo | Cálculo |
| --- | --- | ---- |
| Envia | Contagem | Número total de envios em cada dia no intervalo de datas |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de rejeição | Taxa | (Número total de devoluções em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de cancelamento de inscrição | Taxa | (Número total de cancelamentos exclusivos em cada dia no intervalo de datas) / (Número total de entregas em um intervalo de datas)<br><br>Isso usa cancelamentos de assinatura exclusivos, que também são usados em Campaign Analytics, Overview e Report Builder. Esses cancelamentos de assinatura são registrados em todas as fontes (como SDK, API REST, importações de CSV, e-mails e cancelamentos de lista). As taxas de cancelamento de assinatura no Campaign e no Canvas Analytics são cancelamentos de assinatura que ocorrem como resultado de um clique de cancelamento de assinatura em um e-mail entregue pelo Braze.  |
| Taxa de abertura exclusiva | Taxa | (Número total de aberturas exclusivas em cada dia no intervalo de datas) / (Número total de entregas em um intervalo de datas) |
| Outras taxas de abertura | Taxa | (Número total de outras aberturas em cada dia no intervalo de datas) / (Número total de entregas no intervalo de datas)<br><br>Outras aberturas incluem e-mails que não foram identificados como aberturas de máquina, como quando um usuário abre um e-mail. Essa métrica não é exclusiva e é uma submétrica do total de aberturas.  |
| Taxa de cliques únicos | Taxa | (Número total de cliques exclusivos em cada dia no intervalo de datas) / (Número total de entregas em um intervalo de datas) |
| Taxa única de cliques para abertura | Taxa | (Número total de cliques únicos em cada dia do intervalo de datas) / (Número total de aberturas únicas em cada dia do intervalo de datas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Painel de insights de e-mail 

O painel de insights de e-mail rastreia onde e quando seus clientes estão interagindo com seus e-mails. Esses relatórios podem fornecer dados ricos e granulares sobre como otimizar seus e-mails para gerar maior envolvimento. O painel de insights de e-mail inclui até os últimos seis meses de dados. Para acessar o painel, vá para **Analytics** > **Email Performance** > **Email Insights**.

### Engajamento por dispositivo

O relatório **Envolvimento por dispositivo** fornece um detalhamento dos dispositivos que seus usuários estão usando para interagir com seu e-mail. Esses dados rastreiam o envolvimento de e-mail em dispositivos móveis, desktops, tablets e outros tipos de dispositivos. Esses dados são baseados na string do agente do usuário passada pelos dispositivos dos usuários.

{% alert note %}
Se você usar o CloudFront como CDN, certifique-se de que o agente de usuário dos seus usuários seja transmitido ao ESP. Caso contrário, todo agente de usuário será "Amazon Cloudfront".
{% endalert %}

A categoria "Outros" inclui qualquer string de usuário que não possa ser identificada como desktop, celular ou tablet. Por exemplo, televisão, carro, console de videogame, OTT (over-the-top ou streaming) e similares. Isso também pode incluir valores nulos ou vazios.

Para entender melhor o que está nessa categoria "Outros", você pode extrair os agentes de usuário usando uma dessas opções:

1. [O Currents]({{site.baseurl}}/user_guide/data/braze_currents) enviará a string exata do agente do usuário que foi recuperada dos dispositivos dos seus usuários.
2. Aproveite nosso [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) para usar SQL ou nosso [AI Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) para visualizar os agentes de usuário.

Relatório de engajamento por dispositivo que mostra o número de cliques para celular, desktop, tablet e outros dispositivos. O maior número de cliques ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para abrir e-mails, o Braze separará o Google Image Proxy, o Apple Image Proxy e o Yahoo Mail Proxy. Esses serviços armazenam em cache e carregam todas as imagens incorporadas em um e-mail antes que ele seja entregue ao destinatário. Como resultado, isso acionará uma abertura de e-mail dos servidores do provedor de caixa de correio em vez do servidor do destinatário, o que pode levar a aberturas de e-mail inflacionadas. Esses serviços têm o objetivo de aumentar a privacidade, a segurança, o desempenho e a eficiência no carregamento de imagens. Isso também pode conter aberturas reais de destinatários, pois esses serviços de proxy mascaram o agente do usuário, e nós categorizamos os dados de proxy usando o agente do usuário.

Relatório de envolvimento por dispositivo que mostra o número de cliques para celular, desktop, tablet, proxy de privacidade da Apple, proxy de imagem do Google, proxy de e-mail do Yahoo e outros. O maior número de aberturas ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Engajamento por provedor de caixa postal

O relatório **Envolvimento por provedor de caixa de correio** exibe os principais provedores de caixa de correio que contribuem para seus cliques ou aberturas. Você pode clicar em provedores de caixa de correio principais específicos para detalhar domínios de recebimento específicos. Por exemplo, se a Microsoft estiver listada nesse relatório como uma das principais métricas do seu provedor de caixa de correio, você poderá ver mais detalhes dos domínios de recebimento, como "outlook.com", "hotmail.com", "live.com", entre outros.

\![Um exemplo de relatório de Engajamento por provedor de caixa de correio com Google, Apple iCloud, Yahoo, Microsoft e Mail.Ru Group e o número de cliques correspondente.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Tempo de engajamento

O relatório **Time of Engagement** exibe dados sobre quando os usuários estão interagindo com seus e-mails. Isso pode ajudar a responder a perguntas como, por exemplo, em que dia da semana ou em que horário há o maior envolvimento de seus clientes. Com esses insights, você pode experimentar o melhor dia ou horário para enviar suas mensagens para aumentar o envolvimento. Observe que esses horários são baseados no fuso horário de sua empresa.

O relatório de engajamento **do dia da semana** divide as aberturas ou os cliques por dia da semana. 

\![Um exemplo de relatório de engajamento do dia da semana com o maior número de cliques na segunda e na quarta-feira.]({% image_buster /assets/img_archive/time_engagement.png %})

O relatório de engajamento **Hora do dia** divide as aberturas ou os cliques por hora em um período de 24 horas.

\![Um exemplo de relatório de engajamento de Hora do dia com as aberturas ou cliques das 12 às 23 horas.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para obter mais informações sobre a análise de seus e-mails, consulte [Relatórios de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

## Painel de desempenho de SMS

Para usar o painel de desempenho de SMS, vá para **Analytics** > **SMS Performance** e selecione o intervalo de datas para o período em que deseja visualizar os dados. Seu intervalo de datas pode ser de até um ano no passado.

### Como as métricas são calculadas

\![Um exemplo de campanha de SMS com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Os cálculos para diferentes métricas no painel de desempenho de SMS são os mesmos que aqueles em um nível de mensagem individual (como a análise de campanha). Nesse painel, as métricas são agregadas em todas as campanhas e Canvases para o intervalo de datas que você selecionou. Para saber mais sobre essas definições, consulte [Métricas de SMS]({{site.baseurl}}/sms_mms_rcs_reporting/).

Cada bloco mostra primeiro a métrica de taxa, seguida pela métrica de contagem (com exceção de _Envios_, que exibe a métrica de contagem seguida pela média por dia). Cada bloco também mostra a [comparação com o último período](#comparison-to-last-period-change-in-totals-or-rates).

| Métrico | Tipo | Cálculo |
| --- | --- | ---- |
| Envia | Contagem | Número total de envios em cada dia no intervalo de datas |
| Taxa de entregas confirmadas | Taxa | (Número total de entregas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de falhas de entrega | Taxa | (Número total de falhas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de rejeição | Taxa | (Número total de rejeições em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de cliques | Taxa | (Número total de cliques em cada dia no intervalo de datas) / (Número total de entregas em cada dia no intervalo de datas) |
| Total de opt-ins | Taxa | Número total de opt-ins de mensagens recebidas em cada dia do intervalo de datas |
| Total de opt-outs | Taxa | Número total de opt-outs de mensagens recebidas em cada dia do intervalo de datas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros do painel

Você pode filtrar os dados em seu painel usando as seguintes opções de filtro:

- **Etiqueta:** Escolha uma etiqueta. Quando aplicado, seu painel mostrará métricas apenas para a tag selecionada.
- **Tela:** Escolha até 10 telas. Quando aplicado, seu painel mostrará métricas apenas para os Canvases selecionados. Se você selecionar um filtro de tag primeiro, suas opções de filtros de tela incluirão apenas telas que tenham a tag selecionada.
- **Campanha:** Escolha até 10 campanhas. Quando aplicado, seu painel mostrará métricas apenas para as campanhas selecionadas. Se você selecionar um filtro de tag primeiro, suas opções de filtros de campanha incluirão apenas campanhas que tenham a tag selecionada.

Opções de filtro no Painel de desempenho do canal, onde você pode selecionar uma tag e uma lista de Canvases para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparação de períodos de tempo

O painel de desempenho do canal compara automaticamente o período de tempo que você selecionou no intervalo de datas com o período de tempo anterior, totalizando o mesmo número de dias. Por exemplo, se você escolher "Last 7 Days" (Últimos 7 dias) como seu intervalo de datas no painel, a comparação com o último período comparará as métricas dos últimos sete dias com as dos sete dias anteriores. Se você selecionar um intervalo de datas personalizado, por exemplo, de 10 a 15 de maio, que corresponde a seis dias de dados, o painel comparará as métricas desses dias com as métricas de 4 a 9 de maio.

A comparação é a mudança percentual entre o último período e o atual, calculada pela diferença entre os dois períodos e dividida pela métrica do último período.

### Visualização de alterações nas contagens e taxas totais

Você pode alternar entre **Show Change in Totals (Mostrar alteração nos totais), que**compara as contagens totais (como o número de e-mails entregues) entre os dois períodos, e **Show Change in Rates (Mostrar alteração nas taxas), que**compara as taxas (como a taxa de entrega).

Botões de rádio para alternar entre mostrar a alteração nos totais ou a alteração nas taxas do Channel Performance Dashboard (Painel de desempenho do canal).]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Perguntas frequentes

### Por que meu painel está exibindo valores vazios?

Há alguns cenários que podem levar a valores vazios para uma métrica:

- O Braze registrou zeros para essa métrica específica no intervalo de datas selecionado.
- Você não enviou nenhuma mensagem durante o intervalo de datas selecionado.
- Embora houvesse métricas como aberturas, cliques ou cancelamentos de assinatura para um intervalo de datas selecionado, não havia entregas ou envios. Nesse caso, o Braze não calculará uma métrica de taxa.

Para ver mais métricas, tente expandir o intervalo de datas.

### Por que meu painel de e-mail exibe mais Outras aberturas do que Aberturas exclusivas?

Para a métrica de aberturas _exclusivas_, o Braze desduplicará todas as aberturas repetidas registradas por um determinado usuário (independentemente de incluírem _aberturas de máquina_ ou _outras aberturas_) para que apenas uma única _abertura exclusiva_ seja incrementada se um usuário abrir várias vezes. Para _Outras aberturas_, o Braze não desduplica.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

