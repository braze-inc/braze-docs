---
nav_title: Filtro de canal
article_title: Filtro Canal Inteligente
page_order: 1.5
description: "Este artigo aborda o filtro Canal Inteligente, que seleciona a parte de seu público para a qual o canal de envio de mensagens selecionado é o melhor canal. Neste caso, \"melhor\" significa \"tem a maior probabilidade de engajamento, dado o histórico do usuário\"."
search_rank: 11
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtro Canal Inteligente

> O filtro `Intelligent Channel` (anteriormente `Most Engaged`) seleciona a parte de seu público para a qual o canal de envio de mensagens selecionado é o "melhor" canal. 

## Sobre o filtro de canal

![O filtro Intelligent Channel (Canal inteligente) com um menu suspenso para os diferentes canais que podem ser selecionados.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Neste caso, "melhor" significa que o canal "tem a maior probabilidade de engajamento, dado o histórico do usuário". Você pode selecionar o envio de e-mail, SMS, WhatsApp, web push ou mobile push (incluindo qualquer sistema operacional ou dispositivo móvel disponível) como um canal.

O Canal Inteligente calcula a taxa de engajamento de cada usuário para cada um dos três canais, considerando a proporção de interações com mensagens (aberturas ou cliques) em relação ao número de mensagens recebidas nos últimos seis meses de atividade. Os canais disponíveis são classificados de acordo com suas respectivas taxas de engajamento, e o canal com a maior taxa é o "Mais engajado" para esse usuário. 

Toda vez que uma mensagem é enviada a um usuário, ou que um usuário interage com uma mensagem, a taxa de engajamento é recalculada em segundos. Um usuário só pode ser contado como tendo interagido com uma mensagem uma vez (por exemplo, uma abertura e um clique no mesmo e-mail farão com que essa mensagem seja marcada como tendo sido engajada apenas uma vez, não duas). 

Para ativar o filtro Intelligent Channel, selecione o filtro **Intelligent Channel** na página **Target Audiences (Públicos-alvo** ) ao criar uma campanha de envio de e-mail, web push ou mobile push.

{% alert important %}
Para calcular a taxa de engajamento do canal de SMS, ative o [encurtamento de links de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) com rastreamento avançado e rastreamento de cliques. Sem esse rastreamento, o SMS pode ser selecionado como o Canal Inteligente para uma taxa de engajamento de 0% devido ao nosso [comportamento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## A opção "Dados insuficientes"

Para que a Braze determine qual é o "melhor" canal, é necessário que haja dados suficientes. Isso significa que um usuário deve ter recebido pelo menos três ou mais mensagens em pelo menos dois dos três canais disponíveis. As mensagens não precisam necessariamente ter sido abertas. 

Se os usuários não tiverem recebido mensagens suficientes em todos os canais, eles serão enquadrados na opção "Dados insuficientes" desse filtro. Isso permite que você use qualquer um dos três canais de envio de mensagens disponíveis para direcionar esses usuários.

Por exemplo, suponha que você queira que os usuários que preferem o envio de mensagens recebam um push e que os usuários que não têm dados suficientes recebam a mesma mensagem push. Nesse caso, você poderia definir o filtro do canal inteligente como **Mobile push** e usar a opção** OR** para adicionar um segundo filtro de canal inteligente definido como **Not Enough Data (Dados insuficientes)**. Uma campanha separada com o filtro de Canal Inteligente definido como e-mail poderia abordar os usuários que preferem e-mail.

![Filtros de canal inteligentes para push móvel ou dados insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
As campanhas e etapas do canva que ignoram [o limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) não serão contabilizadas pelo Canal Inteligente e não poderão contribuir para os requisitos de dados.
{% endalert %}

## A opção "Mobile push"

O push móvel incorpora Android, iOS, Kindle e outros canais de dispositivos móveis disponíveis na Braze. Ao calcular o Canal Inteligente, a Braze analisa cada tipo de dispositivo móvel separadamente e, em seguida, escolhe a taxa de engajamento mais alta entre eles para representar a categoria "Mobile Push" na comparação com o envio de e-mail e web push. 

Por exemplo, se um usuário tiver vários dispositivos móveis, sua taxa de engajamento móvel será representada pela taxa mais alta exibida em todos os dispositivos. Isso, no entanto, não forçaria o usuário a receber notificações por push exclusivamente nesse dispositivo. Essa taxa é usada somente na comparação de taxas com envio de e-mail e web push.

## Canais individuais

Em vez de deixar a Braze escolher o melhor canal para um usuário, você também pode filtrar os usuários com base na probabilidade de eles abrirem ou não uma mensagem em um canal específico que você escolher. Para isso, você pode usar o filtro Probabilidade de abertura de mensagens nos [filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Práticas recomendadas e estratégia de uso eficaz

### Desempate

Como alguns usuários terão um baixo número de mensagens recebidas, não é incomum haver empates nas taxas de engajamento entre os canais disponíveis para um determinado usuário (por exemplo, um único usuário tem uma taxa de engajamento de 0,2 **tanto** para o envio de e-mail quanto para o push móvel). Nesses casos, os empates serão desfeitos priorizando (dando uma classificação mais alta) o canal com os eventos abertos mais recentes.

### Canais inacessíveis

Quando o usuário tiver dados suficientes para que uma classificação seja determinada, mas se tornar inacessível em seu canal de maior engajamento, o usuário "cairá fora" e não receberá nenhuma mensagem. Os usuários que não podem ser acessados em canais específicos devem ser direcionados separadamente.

### Dimensionamento do público

O Canal Inteligente permite o direcionamento antecipado e seletivo da fração de usuários que têm uma probabilidade muito maior de engajamento com uma mensagem do que o restante do seu público. Não é provável que isso represente a maioria dos usuários de um público típico. Em vez disso, espere que esse filtro encontre os 5 a 20% do seu público habitual que têm um histórico estabelecido de engajamento em um determinado canal.


