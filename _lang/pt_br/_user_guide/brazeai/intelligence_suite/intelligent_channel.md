---
nav_title: Filtro de canal
article_title: Filtro Intelligent Channel
page_order: 1.5
description: "Este artigo descreve o filtro Intelligent Channel, que seleciona a parte do seu público para a qual o canal de mensagem selecionado é o canal 'melhor'. Aqui, 'melhor' significa a maior probabilidade de engajamento com base no histórico do usuário."
search_rank: 11
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtro Intelligent Channel

> O filtro **Intelligent Channel** (anteriormente **Most Engaged**) seleciona a parte do seu público para a qual o canal de mensagem selecionado é o canal "melhor".

## Sobre o filtro de canal

![O filtro Intelligent Channel com um menu suspenso dos diferentes canais que podem ser selecionados.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Aqui, "melhor" significa o canal com a maior probabilidade de engajamento com base no histórico do usuário. Você pode selecionar e-mail, SMS, WhatsApp, push web ou push móvel (incluindo qualquer OS ou dispositivo móvel disponível) como canal.

O Intelligent Channel calcula a taxa de engajamento por usuário e por canal como a proporção de interações com mensagens (aberturas ou cliques) para mensagens recebidas nos últimos seis meses. Os canais são classificados por suas taxas de engajamento e o canal com a taxa mais alta é o "Most Engaged" para esse usuário.

Sempre que uma mensagem é enviada a um usuário ou um usuário interage com uma mensagem, a taxa de engajamento é recalculada em segundos. Um usuário só conta como tendo interagido com uma mensagem uma vez (por exemplo, abrir e clicar no mesmo e-mail conta como uma interação).

Para ativar o filtro Intelligent Channel, selecione o filtro **Intelligent Channel** na página **Público-alvo** ao criar uma campanha de e-mail, push web ou push móvel.

{% alert important %}
Para calcular a taxa de engajamento do canal SMS, ative o [encurtamento de links SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) com rastreamento avançado e de cliques. Sem esse rastreamento, o SMS pode ser selecionado como Intelligent Channel com taxa de engajamento de 0% devido ao nosso [comportamento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#tie-breaking).
{% endalert %}

## Opção "Dados insuficientes"

Para que a Braze determine qual canal é o "melhor", são necessários dados suficientes: um usuário deve ter recebido pelo menos três mensagens por canal em pelo menos dois dos três canais disponíveis (não é necessário ter aberto as mensagens).

Usuários que não receberam mensagens suficientes nos canais entram na opção "Dados insuficientes" deste filtro. Você pode usar qualquer um dos três canais para direcionar a esses usuários.

Por exemplo, para enviar push a usuários que preferem push e o mesmo push a usuários sem dados suficientes: configure o filtro Intelligent Channel em **Push móvel** e adicione com **OR** um segundo filtro Intelligent Channel configurado em **Dados insuficientes**. Uma campanha separada com o filtro Intelligent Channel em e-mail pode direcionar a usuários que preferem e-mail.

![Filtros Intelligent Channel para push móvel ou dados insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Campanhas e passos de Canvas que ignoram a [limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) não são considerados pelo Intelligent Channel e não contribuem para os requisitos de dados.
{% endalert %}

Para melhores práticas sobre desempate, canais inalcançáveis e tamanho do público, consulte a versão completa deste artigo no índice à esquerda ou na ajuda do dashboard da Braze.
