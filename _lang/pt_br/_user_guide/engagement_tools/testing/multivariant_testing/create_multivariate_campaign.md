---
nav_title: Criação de testes
article_title: Criação de testes multivariantes e A/B
page_order: 1
page_type: reference
description: "Este artigo explica como criar testes multivariantes e A/B com a Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Criação de testes multivariantes e A/B {#creating-tests}

> Você pode criar um [teste multivariante ou A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para qualquer campanha que tenha como direcionamento um único canal.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## Etapa 1: Crie sua campanha

Clique em **Criar campanha** e selecione um canal para a campanha na seção que permite testes multivariantes e Testes A/B. Para obter documentação detalhada sobre cada canal de envio de mensagens, consulte [Criar uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Etapa 2: Crie suas variantes

Você pode criar até 8 variantes de sua mensagem, diferenciando entre títulos, conteúdo, imagens e muito mais. O número de diferenças entre as mensagens determina se esse é um teste multivariante ou A/B. Um teste A/B examina o efeito da alteração de uma variável, enquanto um teste multivariante examina duas ou mais.

Para obter algumas ideias sobre como começar a diferenciar suas variantes, consulte [Dicas para diferentes canais](#tips-different-channels).

![][3]

## Etapa 3: Programe sua campanha

O agendamento de sua campanha multivariante funciona da mesma forma que o agendamento de qualquer outra campanha do Braze. Todos os tipos de entrega padrão [][4] ] estão disponíveis.

Após o início de um teste multivariante, não é possível fazer alterações na campanha. Se você alterar os parâmetros, como a linha de assunto ou o corpo do HTML, a Braze considerará o experimento comprometido e o desativará imediatamente.

{% alert important %}
Se quiser usar uma [otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponível para canais selecionados), programe sua campanha para ser entregue uma vez. As otimizações não estão disponíveis para campanhas que se repetem ou que têm a reelegibilidade ativada.
{% endalert %}

## Etapa 4: Escolha um segmento e distribua seus usuários entre as variantes

Selecione os segmentos a serem direcionados e, em seguida, distribua seus membros entre as variantes selecionadas e o [grupo de controle](#including-a-control-group) opcional. Para obter as práticas recomendadas sobre a escolha de um segmento para teste, consulte [Escolha de um segmento](#choosing-a-segment).

Para campanhas push, de e-mail e webhook programadas para serem enviadas uma vez, você também pode usar uma [otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Isso reservará uma parte de seu público-alvo do teste A/B e os manterá para um segundo envio otimizado com base nos resultados do primeiro teste.

### Grupo de controle {#including-a-control-group}

É possível reservar uma porcentagem do seu público-alvo para um grupo de controle randomizado. Os usuários do grupo de controle não recebem o teste, mas a Braze monitora sua taxa de conversão durante a campanha.

Ao visualizar seus resultados, é possível comparar as taxas de conversão de suas variantes com uma taxa de conversão de linha de base fornecida pelo grupo de controle. Isso permite comparar os efeitos de suas variantes e os efeitos de suas variantes com a taxa de conversão que resultaria se você não enviasse nenhuma mensagem.

![Painel Testes A/B que mostra o detalhamento percentual do Grupo de controle, Variante 1, Variante 2 e Variante 3 com 25% para cada grupo.][5]

{% alert important %}
Não é recomendado usar um grupo de controle ao determinar o vencedor por aberturas ou cliques. Como o grupo de controle não receberá a mensagem, esses usuários não poderão abrir ou clicar. Portanto, a taxa de conversão desse grupo é 0% por definição e não constitui uma comparação significativa com as variantes.
{% endalert %}

#### Grupos de controle com Testes A/B

Ao usar o limite de frequência com um Testes A/B, o limite de frequência não é aplicado ao grupo de controle da mesma forma que o grupo de teste, o que é uma fonte potencial de viés de tempo. Use janelas de conversão adequadas para evitar esse viés.

#### Grupos de controle com Intelligent Selection

O tamanho do grupo de controle de uma campanha com [Intelligent Selection][1] é baseado no número de variantes. Se cada variante for enviada a mais de 20% dos usuários, o grupo de controle será de 20% e as variantes serão divididas igualmente entre os 80% restantes. No entanto, se tiver variantes suficientes para que cada variante seja enviada a menos de 20% dos usuários, o grupo de controle deverá ser menor. Quando a Intelligent Selection começa a analisar a performance do seu teste, o grupo de controle aumenta ou diminui com base nos resultados.

## Etapa 5: Designar um evento de conversão (opcional)

A definição de um evento de conversão para uma campanha permite que você veja quantos destinatários dessa campanha realizaram uma determinada ação após recebê-la.

Isso só afeta o teste se você tiver escolhido **a Taxa de conversão primária** nas etapas anteriores. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). 

## Etapa 6: Revisão e lançamento

Na página de confirmação, revise os detalhes de sua campanha multivariante e inicie o teste! Em seguida, saiba como [entender os resultados de seus testes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Coisas para saber

{% alert important %}
Fazer edições nas mensagens após o início da experiência invalidará os resultados do teste.

- Se o seu experimento estiver no meio do envio e você editar a mensagem, o experimento será inutilizado e todos os resultados do experimento serão removidos.
- Se o experimento for concluído e você editar a mensagem após o envio, os resultados do experimento permanecerão disponíveis na página de análise de dados do dashboard. Se você relançar a campanha, os resultados do experimento serão removidos.
{% endalert %}

### Dicas para diferentes canais {#tips-different-channels}

Dependendo do canal que selecionar, você poderá testar diferentes componentes de sua mensagem. Tente criar variantes com uma ideia do que você deseja testar e do que espera provar.

Que alavancas você precisa acionar e quais são os efeitos desejados? Embora existam milhões de possibilidades que você pode investigar usando um teste multivariante e um teste A/B, temos algumas sugestões para você começar:

| Canal | Aspectos da mensagem que você pode mudar | Resultados a serem buscados |
| ---------------------| --------------- | ------------- |
| Push | Copiar <br> Uso de imagens e emojis <br> Deep links  <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%")  <br> Apresentação do tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| E-mail | Assunto <br> Nome de exibição <br> Saudação <br> Texto do corpo <br> Uso de imagens e emojis <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%") <br> Apresentação do tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| Mensagem no app | Aspectos listados para "push" (empurrar) <br> [Formato da mensagem][7] | Clique <br> Taxa de conversão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Ao executar Testes A/B, não se esqueça de gerar [relatórios de funil]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/) que lhe permitam entender como cada variante afetou seu funil de conversão, especialmente se a "conversão" para sua empresa envolver várias etapas ou ações.
{% endalert %}

Além disso, a duração ideal de seu teste também pode variar dependendo do canal. Tenha em mente o tempo médio que a maioria dos usuários pode precisar para se engajar em cada canal.

Por exemplo, se estiver testando um push, poderá obter resultados significativos mais rapidamente do que ao testar o envio de e-mail, pois os usuários veem os pushes imediatamente, mas pode levar dias até que vejam ou abram um e-mail. Se estiver testando mensagens no app, lembre-se de que os usuários devem abrir o aplicativo para ver a campanha, portanto, espere mais tempo para coletar resultados tanto dos usuários mais ativos que abrem o app quanto dos usuários mais comuns.

Se você não tiver certeza de quanto tempo seu teste deve durar, o recurso [seleção inteligente][6]] pode ser útil para encontrar uma variante vencedora de forma eficiente.

### Escolha de um segmento {#choosing-a-segment}

Como diferentes segmentos de seus usuários podem responder de forma diferente ao envio de mensagens, o sucesso de uma determinada mensagem diz algo sobre a própria mensagem e seu segmento de direcionamento. Portanto, tente projetar um teste tendo em mente seu segmento-alvo.

Por exemplo, embora os usuários ativos possam ter taxas de resposta iguais para "Esta oferta expira amanhã!" e "Esta oferta expira em 24 horas!", os usuários que não abrem o app há uma semana podem ser mais receptivos à última formulação, pois ela cria um maior senso de urgência.

Além disso, ao escolher em qual segmento executar seu teste, não se esqueça de considerar se o tamanho desse segmento será grande o suficiente para seu teste. Em geral, os testes multivariantes e A/B com mais variantes exigem um grupo de teste maior para obter resultados estatisticamente significativos. Isso ocorre porque mais variantes resultarão em menos usuários vendo cada variante individual.

{% alert tip %}
Como orientação, provavelmente serão necessários cerca de 15.000 usuários por variante (incluindo o controle) para obter 95% de confiança nos resultados do teste. No entanto, o número exato de usuários de que você precisa pode ser maior ou menor do que isso, dependendo do seu caso específico. Para obter orientações mais precisas sobre tamanhos de amostras variantes, considere consultar uma [calculadora de tamanho de amostra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Viés e randomização

Uma pergunta comum sobre as atribuições de grupos de controle e de teste é se eles podem introduzir viés nos seus testes. Outras pessoas às vezes se perguntam como sabemos se essas atribuições são realmente aleatórias.

Os usuários são atribuídos a variantes de mensagens, variantes do Canvas ou a seus respectivos grupos de controle concatenando sua ID de usuário (gerada aleatoriamente) com a ID da campanha ou do Canvas (gerada aleatoriamente), considerando o módulo desse valor com 100 e, em seguida, ordenando os usuários em fatias que correspondem às atribuições de porcentagem para variantes e controle opcional escolhidos no dashboard. Portanto, não há nenhuma maneira prática de que os comportamentos dos usuários antes da criação de uma determinada campanha ou Canva possam variar sistematicamente entre variantes e controle. Também não é prático ser mais aleatório (ou mais precisamente, pseudo-aleatório) do que essa implementação.

#### Erros a serem evitados

Há alguns erros comuns que devem ser evitados, criando a aparência de diferenças com base no canal de envio de mensagens se os públicos não forem filtrados corretamente.

Por exemplo, se você enviar uma mensagem push para um público amplo com um controle, o grupo de teste só enviará mensagens para usuários com um token por push. No entanto, o grupo de controle incluirá tanto os usuários que têm um token por push quanto os que não têm. Nesse caso, seu público inicial para a campanha ou o Canva deve filtrar por ter um token por push (`Push Enabled` é `true`). O mesmo deve ser feito para ser elegível para receber mensagens em outros canais: aceitação, ter um token por push, assinatura etc.

{% alert note %}
Se você usar números aleatórios para grupos de controle manualmente, consulte esta lista de [coisas a serem observadas]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) em seus grupos de controle.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
 [6]:{{site.baseurl}}/brazeai/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
