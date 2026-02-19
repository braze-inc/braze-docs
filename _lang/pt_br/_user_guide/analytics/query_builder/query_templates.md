---
nav_title: Modelos de consulta
article_title: Modelos do Query Builder
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência lista os tipos de relatórios que você pode criar usando os dados do Braze do Snowflake no Query Builder."
tool: Reports
---

# Modelos do Query Builder

> Acesse os modelos [do Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) selecionando **Query Template** ao criar um relatório. Todos os modelos apresentam dados até os últimos 60 dias, mas você pode editar diretamente esse e outros valores no editor.<br><br>Para obter definições das métricas que podem aparecer em seus relatórios do Query Builder, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics/) e filtre pelo respectivo canal.

## Modelos de canal

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nome da consulta | Descrição | 
| --- | --- | 
| Engajamento e receita do canal | Esse relatório mostra, para cada canal, todas as métricas de engajamento (como aberturas e cliques), receita, número de transações e preço médio. {::nomarkdown} <ul> <li> <i>Número de transações:</i> Número de eventos de compra </li> <li> <i>Preço médio:</i> Receita dividida por transações </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Compras e receita por segmento | Esse relatório mostra as métricas das mensagens enviadas para um segmento específico. <br><br> As métricas de compra são únicas durante todo o período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Compras e receita de variantes ou etapas por segmento | Esse relatório mostra métricas para as variantes ou etapas do canva das mensagens enviadas a cada segmento de mensagem. <br><br> As métricas de compra são únicas durante todo o período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Mensagens de compras com melhor/pior performance | Esse relatório mostra as métricas de compra para as campanhas superiores ou inferiores, Canvas ou etapas do Canva. Cada linha é uma campanha, um Canvas ou uma etapa do Canva. Você deve especificar se deseja exibir os melhores ou os piores desempenhos e a métrica específica para a qual deseja executar essa análise (como *compras únicas no recebimento*, *receita no recebimento*, *destinatários únicos*). <br><br> As linhas dos relatórios de melhor desempenho serão ordenadas da melhor para a pior, enquanto as linhas dos relatórios de desempenho inferior serão ordenadas da pior para a melhor. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de campanha

| Nome da consulta | Descrição | 
| --- | --- | 
| Receita da campanha por país | Esse relatório mostra a receita por país para uma campanha específica. Para executar esse relatório, você deve especificar o identificador API de uma campanha. Você pode encontrar o identificador de API de uma campanha na parte inferior da página de detalhes da campanha. <br><br> Esse relatório mostra, para cada país, o valor da receita gerada, o número de pedidos, o número de devoluções, a receita líquida e a receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de canva

| Nome da consulta | Descrição | 
| --- | --- | 
| Receita do canva por país | Esse relatório mostra a receita por país para uma determinada tela. Para executar esse relatório, você deve especificar o identificador de API de um Canva. Você pode encontrar o identificador da API do Canva em **Analyze Variants (Analisar variantes**). <br><br> Esse relatório mostra, para cada país, o valor da receita gerada, o número de pedidos, o número de devoluções, a receita líquida e a receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de e-mail

| Nome da consulta | Descrição | 
| --- | --- | 
| Bounces de e-mails por domínio | O número de bounces por domínio de e-mail, dividido em total de bounces, hard bounces e soft bounces. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Métricas de entrega de e-mails por dia | Esse relatório mostra métricas para as mensagens enviadas em cada dia, como quantos e-mails foram enviados, entregues, soft bounce e hard bounce. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> para 21 de novembro aumenta em um.</li><li> A métrica de <i>soft bounces</i> de 22 de novembro não foi afetada. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
|  Métricas de engajamento de e-mails por segmento | Esse relatório mostra métricas para as mensagens enviadas a cada segmento de mensagem, como quantos e-mails foram enviados, entregues, soft bounce e hard bounce. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> para 21 de novembro aumenta em um. </li><li> A métrica de <i>soft bounces</i> de 22 de novembro não foi afetada.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Métricas de engajamento de e-mail para variantes ou etapas, por segmento | Esse relatório mostra métricas para as variantes ou etapas do canva das mensagens enviadas a cada segmento de mensagem. Essas métricas incluem quantos e-mails foram enviados, entregues, soft bounce e hard bounce. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> para 21 de novembro aumenta em um. </li> <li> A métrica de <i>soft bounces</i> de 22 de novembro não foi afetada.</li></ul> {:/} |
| Performance de e-mail por país | Esse relatório mostra as seguintes métricas para cada país: envios, taxa de abertura indireta e taxa de abertura direta. País é o país do usuário no momento do envio do push. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Changelogs de assinatura de e-mail | Esse relatório mostra as métricas que foram registradas sobre a alteração da inscrição de cada usuário, como endereço de e-mail, status da inscrição, hora em que o status foi alterado e o Canva ou campanha associada. |
| Grupo de inscrições para e-mail com aceitação e recusa | Esse relatório mostra o número de aceitações e exclusões de usuários únicos de qualquer grupo de inscrições para e-mail em cada semana. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| Cliques em URLs de e-mails | Esse relatório mostra o número de cliques em cada link de um e-mail. Para executar esse relatório, você precisará especificar o identificador da API para uma campanha ou canva. Você pode encontrar o identificador de API de uma campanha na parte inferior da página de detalhes dessa campanha e o identificador de API do Canva em **Analisar variantes**. <br><br> Esse relatório mostra links não personalizados e uma contagem de cliques para cada link. O download do CSV incluirá os IDs de todos os usuários que clicaram, o link em que clicaram e um registro de data e hora de quando clicaram. <br><br> *URLs despersonalizados:* URLs que não contêm tags Liquid. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Mensagens para engajamento de e-mail com melhor/pior performance | Esse relatório mostra as métricas de engajamento de e-mail para as campanhas superiores ou inferiores, Canvas ou etapas do Canva. Você deve especificar se deseja exibir os melhores ou os piores desempenhos e a métrica específica para a qual executar essa análise (como *Enviados*, *Soft Bounces* e *Aberturas únicas*). <br><br> As linhas dos relatórios de melhor desempenho serão ordenadas da melhor para a pior, enquanto as linhas dos relatórios de desempenho inferior serão ordenadas da pior para a melhor. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos para celular

| Nome da consulta | Descrição | 
| --- | --- | 
| Operadoras dos dispositivos | O número de usuários por operadora de dispositivo, como a Verizon e a T-Mobile. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modelos dos dispositivos | O número de usuários por modelo de dispositivo, como o iPhone 15 Pro e o Pixel 7. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Sistemas operacionais dos dispositivos | O número de usuários por sistema operacional, como o 17.4 e o Android 14. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Resoluções de tela dos dispositivos | O número de usuários por resolução de tela do dispositivo, como 1179x2556 e 750x1334. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Códigos de erro de SMS | Esse relatório mostra o tipo de erro e o número de erros para cada código de erro de SMS. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| Erros do provedor de SMS por usuário | Esse relatório mostra os códigos de erro de SMS para um usuário específico. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos push

| Nome da consulta | Descrição | 
| --- | --- | 
| Performance de push por país | Esse relatório mostra as seguintes métricas para cada país: entregas, taxa de abertura e taxa de cliques. País é o país do usuário no momento do envio do e-mail. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Detalhamento do segmento

| Nome da consulta | Descrição |
| -- | -- |
| Métricas de engajamento de e-mails por segmento | Esse relatório mostra as métricas de performance de e-mail divididas por segmento no nível da campanha ou do Canva. |
| Compras e receita por segmento | Esse relatório mostra as métricas de compra e receita divididas por segmento para uma campanha ou uma tela específica. |
| Mensagens para engajamento de e-mail com melhor/pior performance | Esse relatório mostra as campanhas, Canvas ou etapas do Canvas que tiveram a melhor ou a pior performance para uma métrica de engajamento de e-mail especificada.|
| Mensagens de compras com melhor/pior performance | Esse relatório mostra as campanhas, Canvas ou etapas do Canvas que tiveram a melhor ou a pior performance em uma métrica de compra ou receita especificada. |
| Performance de push por segmento | Esse relatório mostra as métricas de push divididas por segmentos.|
{: .reset-td-br-1 .reset-td-br-2 }