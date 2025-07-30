---
nav_title: Análise de dados de eventos
article_title: Análises preditivas de eventos
description: "Este artigo de referência cobre os diferentes componentes incluídos na página de Análise de Eventos Preditivos e como eles podem ser usados para tomar decisões informadas."
page_order: 1.3

---

# Análises preditivas de eventos

> Depois que sua previsão for construída e treinada, você terá acesso à página de **análises de previsão**. Esta página ajuda você a decidir quais usuários você deve segmentar com base em sua pontuação de probabilidade ou categoria.

## Sobre análises preditivas de eventos

Assim que a previsão terminar de treinar e esta página estiver populada, você pode começar a usar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) em segmentos ou campanhas para começar a usar os resultados do modelo. Se você deseja ajuda para decidir quem direcionar e por quê, esta página pode ajudar com base na precisão histórica do modelo e nos seus próprios objetivos de negócios.

Esses são os componentes que compõem as análises preditivas de eventos:

- [Pontuação de Probabilidade](#purchase_score)
- [Qualidade da previsão](#prediction_quality)
- [Precisão estimada](#estimated_results)
- [Tabela de Correlação de Eventos](#correlation_table)

A distribuição dos escores de probabilidade para todo o público de previsão é exibida no topo da página. Usuários em {buckets} mais à direita têm pontuações mais altas e são mais propensos a realizar o evento. Usuários em buckets mais à esquerda são menos propensos a realizar o evento. O controle deslizante abaixo do gráfico permitirá que você selecione uma seção de usuários e estime quais seriam os resultados de direcionamento desses usuários.

À medida que você move os controles deslizantes para diferentes posições, a barra na metade esquerda do painel informará quantos usuários do público total de previsão seriam alvo usando a parte da população que você selecionou.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Pontuação de probabilidade {#purchase_score}

Usuários no público de previsão receberão uma pontuação de probabilidade entre 0 e 100. Quanto maior a pontuação, maior a probabilidade de realizar o evento. 

A seguir está como um usuário é categorizado dependendo de sua pontuação de probabilidade:

- **Baixo:** entre 0 e 50
- **Médio:** entre 50 e 75
- **Alto:** entre 75 e 100

As pontuações e as categorias correspondentes serão atualizadas de acordo com o cronograma que você escolheu na página de **Criação de Previsão**. O número de usuários com pontuações de probabilidade em cada um dos 20 intervalos de tamanho igual ou em cada uma das categorias de probabilidade é exibido no gráfico no topo da página.

## Precisão estimada {#estimated_results}

Na metade direita do painel abaixo do gráfico, mostramos estimativas da precisão esperada do direcionamento da parte do público de previsão que você selecionou de duas maneiras: quantos usuários selecionados devem realizar o evento e quantos não devem.

![O público selecionado e a precisão estimada mostrados no dashboard do Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Espera-se que tenha performance

É possível usar a precisão estimada para verificar quantos usuários selecionados devem executar o evento.

A previsão não é perfeitamente precisa, e nenhuma previsão jamais é, o que significa que a Braze não será capaz de identificar todos os futuros usuários para realizar o evento. As pontuações de probabilidade são como um conjunto de previsões informadas e confiáveis. A barra de progresso indica quantos dos "verdadeiros positivos" esperados no público de previsão serão alvejados com o público selecionado. Observe que esperamos que este número de usuários realize o evento mesmo que você não envie uma mensagem para eles.

### Não se espera que tenha performance

É possível usar a precisão estimada para verificar quantos usuários selecionados deverão não realizar o evento.

Todos os modelos de machine learning cometem erros. Pode haver usuários em sua seleção que tenham uma pontuação de alta probabilidade, mas que não acabem realmente realizando o evento. Eles não realizariam o evento se você não tomasse nenhuma ação. Eles serão segmentados de qualquer maneira, então isso é um erro ou "falso positivo." A largura total desta segunda barra de progresso representa o número esperado de usuários que não realizarão o evento, e a parte preenchida são aqueles que serão incorretamente alvejados usando a posição atual do controle deslizante.

Usando essas informações, incentivamos você a decidir quantos dos verdadeiros positivos você deseja capturar, quantos falsos positivos você pode aceitar serem direcionados e qual é o custo dos erros para o seu negócio. Se você está enviando uma promoção valiosa, pode querer direcionar apenas para não-compradores (falsos positivos) favorecendo o lado esquerdo do gráfico. Ou, você pode querer incentivar os compradores que frequentemente compram (verdadeiros positivos) a fazê-lo novamente, selecionando uma seção de usuários que favorece o lado direito do gráfico.

## Qualidade da previsão {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tabela de correlação de eventos {#correlation_table}

Esta análise exibe atributos ou comportamentos de usuários que estão correlacionados com eventos no público de previsão. Os atributos avaliados são Idade, País, Gênero e Idioma. Comportamentos que são analisados incluem sessões, compras, total de dólares gastos, eventos personalizados, e campanhas e passos de canva recebidos nos últimos 30 dias.

As tabelas são divididas em esquerda e direita para mais e menos propensas a realizar o evento, respectivamente. Para cada linha, a razão pela qual os usuários com o comportamento ou atributo na coluna da esquerda são mais ou menos propensos a realizar o evento é exibida na coluna da direita. Este número é a razão entre as pontuações de probabilidade de usuários com esse comportamento ou atributo dividida pela probabilidade de realizar o evento de todo o público de previsão.

Esta tabela é atualizada apenas quando a previsão é re-treinada e não quando as pontuações de probabilidade do usuário são atualizadas.

{% alert note %}
Os dados de correlação para prévia das previsões serão parcialmente ocultos. Uma compra é necessária para revelar esta informação. Entre em contato com o seu gerente de conta para saber mais.
{% endalert %}
