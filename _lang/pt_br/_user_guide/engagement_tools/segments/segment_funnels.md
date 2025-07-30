---
nav_title: Funis de segmento
article_title: Funis de segmento
page_order: 3

page_type: reference
tool: Segments
description: "Este artigo de referência explica como usar os funis de segmento da Braze, suas práticas recomendadas e casos de uso."
search_rank: 1
---

# Funis de segmento

> Os funis de segmento são ótimos para restringir seu público para um caso de uso de campanha específico, aprender sobre esse público e suas interações e usar esse conhecimento para criar estratégias e desenvolver campanhas eficazes.

Os funis de segmento permitem que você veja como cada filtro adicionado afeta as estatísticas do segmento. Ao criar um segmento, uma linha de dados aparecerá sob cada filtro. Esses dados fornecerão as seguintes informações para os usuários que foram direcionados por todos os filtros até aquele momento:

- Número total de usuários direcionados e a porcentagem da sua base de público
- LTV e LTV para usuários pagantes  
- Número de usuários que podem enviar e-mail
- Número de usuários que aceitaram o envio de e-mail
- Número de usuários que estão ativados para push  
- Número de usuários que aceitaram o push

![][1]

## Práticas recomendadas

- Ao adicionar filtros que documentam o fluxo do usuário, você pode ver os pontos em que os usuários caem. Por instância do app, se você for um aplicativo de rede social e quiser ver onde pode estar perdendo usuários durante o processo de integração, talvez queira adicionar filtros de dados personalizados para inscrever-se, adicionar amigos e enviar a primeira mensagem. Se descobrir que 85% dos usuários estão inscrevendo-se e adicionando amigos, mas apenas 45% enviaram a primeira mensagem, então saberá que deve se concentrar em incentivar mais envios de mensagens durante suas campanhas de integração e marketing.

- Os funis de segmento permitem comparar a porcentagem de usuários que realizam ações diferentes. Por exemplo, os usuários ativos, ou aqueles com alto LTV, tendem a interagir mais com envios de e-mail ou push][4]? Para descobrir isso, crie um segmento de usuários ativos com um ou mais filtros e, em seguida, veja como as estatísticas mudam quando você adiciona um filtro para aceitação de push e quando adiciona um filtro para aceitação de envio de e-mail.

- Analise como o LTV muda à medida que você adiciona filtros. Para usuários ativos, aqueles que se conectam ao Facebook ou aqueles que se conectam ao X (antigo Twitter) têm um LTV mais alto? Ou o LTV é significativamente maior para aqueles que se conectaram a ambos? Se você descobrir, por exemplo, que a conexão com o X (antigo Twitter) tem muito pouco impacto sobre o LTV, mas a conexão com o Facebook tem um grande impacto, talvez queira que suas campanhas de marketing se concentrem em incentivar as conexões com o Facebook.

## Casos de uso

### Impacto de uma ação específica do usuário nas conversões {#push-email}

Ao analisar o impacto de uma determinada ação do usuário (como adicionar itens a uma lista de desejos) em uma conversão (como fazer compras), você pode responder às seguintes perguntas:

- A ação do usuário coincide com mais compras?
- Qual é a prevalência da ação do usuário? Você deve criar campanhas de marketing que incentivem mais essa ação?

Por exemplo, digamos que você tenha um grupo em que todos os usuários que adicionaram itens a uma lista de desejos também fizeram uma compra. Como apenas uma pequena porcentagem de usuários adicionou itens a uma lista de desejos, esse app pode querer incentivar mais esse comportamento por meio de campanhas de marketing.

![Exemplo de funil de segmento com os seguintes filtros: "Usou o app pela última vez há menos de 30 dias", "Item adicionado à lista de espera há menos de 30 dias" e "Última compra feita há menos de 30 dias" para alcançar 4.302 usuários.][3]

### Compare os canais de envio de mensagens

Crie um segmento de usuários ativos (ou usuários com as características desejadas) e compare suas interações com diferentes canais de engajamento, como envio de e-mail e notificações por push. Por exemplo, se mais usuários fiéis estiverem inscritos no push, talvez seja melhor dedicar mais tempo ao envio de campanhas de usuários ativos via push. No entanto, se descobrir que o LTV é maior para os assinantes de e-mail, convém solicitar que os usuários mais ativos assinem o e-mail.

![Funil de segmento para exemplo de e-mail com os seguintes filtros: "Last Made Purchase less than 30 days ago", "Last used these apps less than 30 days ago", "Push Enabled is true" e "Email Subscription Status is Opted In" para alcançar 2.799 usuários.][5]

### Aceitações push para iOS ou Android

Esse caso de uso aproveita o filtro "Push Enabled for App" para direcionamento a usuários de iOS ou Android que aceitaram o push.

![][11]

![][12]

### Público totalmente capacitado para push

Esse caso de uso aproveita o filtro "Push Enabled" para direcionar os usuários que aceitaram o push.

![][10]

### Grupo de controle global de público ativado por push

Esse caso de uso aproveita o filtro "Push Enabled" e "Random Bucket #" para direcionar os usuários que fazem parte do grupo de controle global que aceitaram o push.

![][9]

### Compradores recentes

Esse caso de uso aproveita o filtro "Last Made Purchase" (Última compra feita) para direcionar os usuários que fizeram uma compra pela última vez há menos de 7 dias.

![][8]

### Engajamento push

Esse caso de uso utiliza o filtro "Last Did Custom Event" (último evento personalizado), em que o evento personalizado é "opened any push" (abriu qualquer push), para direcionar os usuários que mostraram engajamento por push nos últimos 21 dias.

![][7]

### Dinheiro gasto no app

Esse caso de uso aproveita o filtro "Money Spent" (dinheiro gasto) para direcionamento a usuários que gastaram pelo menos 1.000 dólares.

![][6]


[1]: {% image_buster /assets/img_archive/segment_funnel_example.png %}
[3]: {% image_buster /assets/img_archive/Wish_List_2.png %}
[11]: {% image_buster /assets/img/seg_filter_examples/ios.png %}
[12]: {% image_buster /assets/img/seg_filter_examples/android.png %}
[6]: {% image_buster /assets/img/seg_filter_examples/moneyspent.png %}
[7]: {% image_buster /assets/img/seg_filter_examples/push_engagement.png %}
[8]: {% image_buster /assets/img/seg_filter_examples/recent_purchase.png %}
[9]: {% image_buster /assets/img/seg_filter_examples/global_control.png %}
[10]: {% image_buster /assets/img/seg_filter_examples/both.png %}
[4]: \#push-email
[5]: {% image_buster /assets/img_archive/Wish_List_Email.png %}
