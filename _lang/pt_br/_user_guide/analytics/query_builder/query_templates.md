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
| Engajamento e receita do canal | Esse relatório mostra, para cada canal, todas as métricas de engajamento (como aberturas e cliques), receita, número de transações e preço médio. {::nomarkdown} <ul> <li> <i>Número de transações:</i> Número de eventos de compra </li> <li> <i>Preço médio:</i> Receita dividida por transações </li> </ul> {:/} \![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Compras e receita por segmento | Esse relatório mostra as métricas das mensagens enviadas para um segmento específico. <br><br> As métricas de compra são únicas em todo o período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Compras e receita de variantes ou etapas, por segmento | Esse relatório mostra métricas para as variantes ou etapas do Canvas das mensagens enviadas a cada segmento. <br><br> As métricas de compra são únicas em todo o período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Mensagens superiores/inferiores para compras | Esse relatório mostra as métricas de compra para as campanhas superiores ou inferiores, Canvases ou etapas do Canvas. Cada linha é uma campanha, um Canvas ou uma etapa do Canvas. Você deve especificar se deseja exibir os melhores ou piores desempenhos e a métrica específica para a qual deseja executar essa análise (como *compras únicas no recebimento*, *receita no recebimento*, *destinatários únicos*). <br><br> As linhas nos relatórios de melhor desempenho serão ordenadas da melhor para a pior, enquanto as linhas nos relatórios de desempenho inferior serão ordenadas da pior para a melhor. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de campanha

| Nome da consulta | Descrição | 
| --- | --- | 
| Receita da campanha por país | Esse relatório mostra a receita por país para uma campanha específica. Para executar esse relatório, você deve especificar o identificador de API de uma campanha. Você pode encontrar o identificador de API de uma campanha na parte inferior da página de detalhes da campanha. <br><br> Esse relatório mostra, para cada país, o valor da receita gerada, o número de pedidos, o número de devoluções, a receita líquida e a receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} \![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de tela

| Nome da consulta | Descrição | 
| --- | --- | 
| Receita do Canvas por país | Esse relatório mostra a receita por país para um Canvas específico. Para executar esse relatório, você deve especificar o identificador de API de um Canvas. Você pode encontrar o identificador da API do Canvas em **Analyze Variants**. <br><br> Esse relatório mostra, para cada país, o valor da receita gerada, o número de pedidos, o número de devoluções, a receita líquida e a receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} \![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos de e-mail

| Nome da consulta | Descrição | 
| --- | --- | 
| Rejeições de e-mail por domínio | O número de rejeições por domínio de e-mail, dividido em total de rejeições, rejeições graves e rejeições leves. <br> \![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Métricas de entrega de e-mail por dia | Esse relatório mostra métricas para as mensagens enviadas em cada dia, como quantos e-mails foram enviados, entregues, soft bounced e hard bounced. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi devolvido uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica <i>Soft Bounces</i> para 21 de novembro aumenta em um.</li><li> A métrica <i>Soft Bounces</i> de 22 de novembro não foi afetada. </li></ul>{:/} \![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
|  Métricas de engajamento de e-mail por segmento | Esse relatório mostra métricas para as mensagens enviadas a cada segmento, como quantos e-mails foram enviados, entregues, soft bounced e hard bounced. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi devolvido uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica <i>Soft Bounces</i> para 21 de novembro aumenta em um. </li><li> A métrica <i>Soft Bounces</i> de 22 de novembro não foi afetada.</li></ul>{:/} \![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Métricas de engajamento de e-mail para variantes ou etapas, por segmento | Esse relatório mostra métricas para as variantes ou etapas do Canvas das mensagens enviadas a cada segmento. Essas métricas incluem quantos e-mails foram enviados, entregues, soft bounced e hard bounced. <br><br> Todas as métricas são únicas durante todo o período do relatório. Por exemplo, se um e-mail de boas-vindas foi devolvido uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica <i>Soft Bounces</i> para 21 de novembro aumenta em um. </li> <li> A métrica <i>Soft Bounces</i> de 22 de novembro não foi afetada.</li></ul> {:/} |
| Desempenho de e-mail por país | Esse relatório mostra as seguintes métricas para cada país: envios, taxa de abertura indireta e taxa de abertura direta. Country é o país do usuário no momento do envio por push. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Registros de alteração de assinatura de e-mail | Esse relatório mostra as métricas que foram registradas sobre a alteração da assinatura de cada usuário, como endereço de e-mail, status da assinatura, a hora em que o status foi alterado e o Canvas ou a campanha associada. |
| Assinatura de e-mail para grupos de opt-ins e opt-outs | Esse relatório mostra o número de opt-ins e opt-outs de usuários únicos de qualquer grupo de assinatura de e-mail para cada semana. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URLs de e-mail clicados | Esse relatório mostra o número de cliques de cada link em um e-mail. Para executar esse relatório, você precisará especificar o identificador de API para uma campanha ou Canvas. Você pode encontrar o identificador de API de uma campanha na parte inferior da página de detalhes dessa campanha e o identificador de API do Canvas em **Analisar variantes**. <br><br> Esse relatório mostra links não personalizados e uma contagem de cliques para cada link. O download do CSV incluirá os IDs de usuário de todos os usuários que clicaram, o link em que clicaram e um registro de data e hora de quando clicaram. <br><br> *URLs despersonalizados:* URLs que não contêm tags Liquid. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Mensagens superiores/inferiores para engajamento por e-mail | Esse relatório mostra as métricas de envolvimento de e-mail para as campanhas, Canvases ou etapas do Canvas superiores ou inferiores. Você deve especificar se deseja exibir os melhores ou os piores desempenhos e a métrica específica para a qual deseja executar essa análise (como *Enviados*, *Soft Bounces* e *Aberturas únicas*). <br><br> As linhas nos relatórios de melhor desempenho serão ordenadas da melhor para a pior, enquanto as linhas nos relatórios de desempenho inferior serão ordenadas da pior para a melhor. <br><br> \![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos móveis

| Nome da consulta | Descrição | 
| --- | --- | 
| Portadores de dispositivos | O número de usuários por operadora de dispositivo, como a Verizon e a T-Mobile. <br><br> \![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modelos de dispositivos | O número de usuários por modelo de dispositivo, como o iPhone 15 Pro e o Pixel 7. <br><br> \![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Sistemas operacionais de dispositivos | O número de usuários por sistema operacional, como o 17.4 e o Android 14. <br><br> \![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Resoluções de tela do dispositivo | O número de usuários por resolução de tela do dispositivo, como 1179x2556 e 750x1334. <br><br> \![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Códigos de erro de SMS | Esse relatório mostra o tipo de erro e o número de erros para cada código de erro de SMS. <br><br>\![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| Erros de fornecimento de SMS por usuário | Esse relatório mostra os códigos de erro de SMS para um usuário específico. |
{: .reset-td-br-1 .reset-td-br-2 }

## Modelos push

| Nome da consulta | Descrição | 
| --- | --- | 
| Desempenho do push por país | Esse relatório mostra as seguintes métricas para cada país: entregas, taxa de abertura e taxa de cliques. Country é o país do usuário no momento do envio do e-mail. <br><br> \![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Detalhamento do segmento

| Nome da consulta | Descrição |
| -- | -- |
| Métricas de engajamento de e-mail por segmento | Esse relatório mostra as métricas de desempenho de e-mail divididas por segmento no nível da campanha ou do Canvas. |
| Compras e receita por segmento | Esse relatório mostra métricas de compra e receita divididas por segmento para uma campanha ou tela específica. |
| Mensagens superiores/inferiores para engajamento por e-mail | Esse relatório mostra as campanhas, Canvases ou etapas do Canvas que tiveram o melhor ou o pior desempenho para uma métrica de envolvimento de e-mail especificada.|
| Mensagens superiores/inferiores para compras | Esse relatório mostra as campanhas, Canvases ou etapas do Canvas que tiveram o melhor ou o pior desempenho em uma métrica de compra ou receita especificada. |
| Desempenho do impulso por segmento | Esse relatório mostra as métricas de push divididas por segmentos.|
{: .reset-td-br-1 .reset-td-br-2 }