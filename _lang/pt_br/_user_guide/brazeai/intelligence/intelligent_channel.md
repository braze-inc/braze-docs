---
nav_title: Filtro de canal
article_title: Filtro de canal inteligente
page_order: 1.5
description: "Este artigo aborda o filtro O canal inteligente, um filtro que seleciona a parte do seu público-alvo para a qual o canal de mensagens selecionado é o melhor canal. Nesse caso, o melhor meio tem a maior probabilidade de engajamento, considerando o histórico do usuário."
search_rank: 11
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtro de canal inteligente

> O filtro `Intelligent Channel` (anteriormente `Most Engaged`) seleciona a parte do seu público para a qual o canal de mensagens selecionado é o "melhor" canal. 

## Sobre o filtro de canal

O filtro Intelligent Channel (Canal inteligente) com um menu suspenso para os diferentes canais que podem ser selecionados.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Nesse caso, melhor significa o canal que tem a maior probabilidade de engajamento, considerando o histórico do usuário. Você pode selecionar e-mail, SMS, WhatsApp, web push ou mobile push (incluindo qualquer sistema operacional ou dispositivo móvel disponível) como um canal.

O Intelligent Channel calcula a taxa de envolvimento de cada usuário para cada um dos três canais, considerando a proporção de interações de mensagens (aberturas ou cliques) em relação ao número de mensagens recebidas nos últimos seis meses de atividade. Os canais disponíveis são classificados de acordo com suas respectivas taxas de envolvimento, e o canal com a maior taxa é o "Mais envolvido" para esse usuário. 

Toda vez que uma mensagem é enviada a um usuário ou que um usuário interage com uma mensagem, a taxa de envolvimento é recalculada em segundos. Um usuário só pode ser contado como tendo interagido com uma mensagem uma vez (por exemplo, uma abertura e um clique no mesmo e-mail farão com que essa mensagem seja marcada como tendo sido engajada apenas uma vez, não duas). 

Para ativar o filtro Intelligent Channel, selecione o filtro **Intelligent Channel** na página **Target Audiences** ao criar uma campanha de e-mail, web push ou mobile push.

{% alert important %}
Para calcular a taxa de envolvimento do canal de SMS, ative o [encurtamento de links de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) com rastreamento avançado e rastreamento de cliques. Sem esse rastreamento, o SMS pode ser selecionado como o Canal Inteligente para uma taxa de engajamento de 0% devido ao nosso [comportamento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## A opção "Dados insuficientes"

Para que a Braze determine qual é o "melhor" canal, é necessário que haja dados suficientes. Isso significa que um usuário deve ter recebido pelo menos três ou mais mensagens por canal em pelo menos dois dos três canais disponíveis. As mensagens não precisam necessariamente ter sido abertas. 

Se os usuários não tiverem recebido mensagens suficientes em todos os canais, eles serão enquadrados na opção "Not Enough Data" (Dados insuficientes) desse filtro. Isso permite que você use qualquer um dos três canais de mensagens disponíveis para atingir esses usuários.

Por exemplo, digamos que você queira que os usuários que preferem mensagens push recebam um push e que os usuários que não têm dados suficientes recebam a mesma mensagem push. Nesse caso, você poderia definir o filtro do canal inteligente como **Mobile push** e usar a **opção OU** para adicionar um segundo filtro de canal inteligente definido como **Not Enough Data (Dados insuficientes**). Uma campanha separada com o filtro Intelligent Channel definido como e-mail poderia abordar os usuários que preferem e-mail.

\![Filtros de canal inteligentes para push móvel ou dados insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
As campanhas e as etapas do Canvas que ignoram [o limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) não serão contabilizadas pelo Intelligent Channel e não poderão contribuir para os requisitos de dados.
{% endalert %}

## A opção "Mobile push

O push móvel incorpora Android, iOS, Kindle e outros canais de dispositivos móveis disponíveis no Braze. Ao calcular o Canal Inteligente, o Braze analisa cada tipo de dispositivo móvel separadamente e, em seguida, escolhe a maior taxa de engajamento entre eles para representar a categoria "Mobile Push" na comparação com e-mail e Web Push. 

Por exemplo, se um usuário tiver vários dispositivos móveis, sua taxa de envolvimento móvel será representada pela taxa mais alta exibida em todos os dispositivos. No entanto, isso não forçaria o usuário a receber notificações push exclusivamente nesse dispositivo. Essa taxa é usada somente quando se comparam as taxas em relação ao envio por e-mail e pela Web.

## Canais individuais

Em vez de deixar o Braze escolher o melhor canal para um usuário, você também pode filtrar os usuários com base na probabilidade de eles abrirem ou não uma mensagem em um canal específico que você escolher. Para isso, você pode usar o filtro Message Open Likelihood nos [filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Práticas recomendadas e estratégia de uso eficaz

### Desempate

Como alguns usuários terão um número baixo de mensagens recebidas, não é incomum haver empates nas taxas de envolvimento entre os canais disponíveis para um determinado usuário (por exemplo, um único usuário tem uma taxa de envolvimento de 0,2 para e-mail e push móvel). Nesses casos, os empates serão desfeitos priorizando (dando uma classificação mais alta) o canal com os eventos abertos mais recentes.

### Canais inacessíveis

Quando o usuário tiver dados suficientes para que uma classificação seja determinada, mas se tornar inacessível em seu canal mais engajado, ele "cairá fora" e não receberá nenhuma mensagem. Os usuários que não podem ser contatados em canais específicos devem ser direcionados separadamente.

### Dimensionamento do público

O Canal Inteligente permite segmentar antecipadamente e de forma seletiva a fração de usuários que têm uma probabilidade muito maior de se envolver com uma mensagem do que o restante do seu público. Não é provável que isso represente a maioria dos usuários em um público típico. Em vez disso, você pode esperar que esse filtro encontre de 5% a 20% do seu público habitual que tenha um histórico estabelecido de envolvimento em um determinado canal.


