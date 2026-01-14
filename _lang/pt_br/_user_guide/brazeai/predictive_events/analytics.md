---
nav_title: Análise de eventos
article_title: Análise preditiva de eventos
description: "Este artigo de referência aborda os diferentes componentes incluídos na página Predictive Events Analytics e como eles podem ser usados para tomar decisões orientadas por insights."
page_order: 1.3

---

# Análise preditiva de eventos

> Depois que sua previsão tiver sido criada e treinada, você terá acesso à página **Prediction Analytics**. Essa página o ajuda a decidir quais usuários você deve segmentar com base na pontuação ou categoria de probabilidade.

## Sobre a análise preditiva de eventos

Assim que a previsão terminar o treinamento e essa página for preenchida, você poderá começar a usar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) em segmentos ou campanhas para começar a usar os resultados do modelo. Se você quiser ajuda para decidir quem segmentar e por quê, esta página pode ajudar com base na precisão histórica do modelo e em suas próprias metas de negócios.

Esses são os componentes que compõem a análise preditiva de eventos:

- [Pontuação de probabilidade](#purchase_score)
- [Qualidade da previsão](#prediction_quality)
- [Precisão estimada](#estimated_results)
- [Tabela de correlação de eventos](#correlation_table)

A distribuição das pontuações de probabilidade para todo o público da previsão é exibida na parte superior da página. Os usuários em grupos mais à direita têm pontuações mais altas e têm maior probabilidade de realizar o evento. Os usuários em grupos mais à esquerda têm menos probabilidade de realizar o evento. O controle deslizante abaixo do gráfico permitirá que você selecione uma seção de usuários e estime quais seriam os resultados da segmentação desses usuários.

À medida que você mover as alças do controle deslizante para diferentes posições, a barra na metade esquerda do painel informará quantos usuários de todo o público-alvo da previsão seriam direcionados usando a parte da população que você selecionou.

\![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Pontuação de probabilidade {#purchase_score}

Os usuários do público-alvo da previsão receberão uma pontuação de probabilidade entre 0 e 100. Quanto maior a pontuação, maior a probabilidade de realizar o evento. 

Veja a seguir como um usuário é categorizado de acordo com sua pontuação de probabilidade:

- **Baixa:** entre 0 e 50
- **Média:** entre 50 e 75
- **Alta:** entre 75 e 100

As pontuações e as categorias correspondentes serão atualizadas de acordo com a programação que você escolheu na página **Criação de previsão**. O número de usuários com pontuações de probabilidade em cada um dos 20 grupos de tamanho igual ou em cada uma das categorias de probabilidade é exibido no gráfico na parte superior da página.

## Precisão estimada {#estimated_results}

Na metade direita do painel abaixo do gráfico, mostramos estimativas da precisão esperada da segmentação da parte do público-alvo da previsão que você selecionou de duas maneiras: quantos usuários selecionados devem realizar o evento e quantos não devem.

\![O público selecionado e a precisão estimada mostrados no painel do Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Espera-se que o desempenho

Você pode usar a precisão estimada para verificar quantos usuários selecionados devem realizar o evento.

A previsão não é perfeitamente precisa, e nenhuma previsão é, o que significa que o Braze não conseguirá identificar todos os futuros usuários que realizarão o evento. As pontuações de probabilidade são como um conjunto de previsões informadas e confiáveis. A barra de progresso indica quantos dos "verdadeiros positivos" esperados no público-alvo da previsão serão direcionados com o público-alvo selecionado. Observe que esperamos que esse número de usuários realize o evento mesmo que você não envie uma mensagem a eles.

### Não se espera que tenha desempenho

Você pode usar a precisão estimada para verificar quantos usuários selecionados não devem realizar o evento.

Todos os modelos de aprendizado de máquina cometem erros. Pode haver usuários na sua seleção que tenham uma pontuação de probabilidade alta, mas que não acabem realizando o evento. Eles não realizariam o evento se você não tomasse nenhuma providência. Eles serão alvos de qualquer forma, portanto, isso é um erro ou "falso positivo". A largura total dessa segunda barra de progresso representa o número esperado de usuários que não realizarão o evento, e a parte preenchida representa aqueles que serão direcionados incorretamente usando a posição atual do controle deslizante.

Usando essas informações, recomendamos que você decida quantos dos verdadeiros positivos deseja capturar, quantos falsos positivos pode aceitar como alvo e qual é o custo dos erros para a sua empresa. Se você estiver enviando uma promoção valiosa, talvez queira segmentar apenas os que não compram (falsos positivos), favorecendo o lado esquerdo do gráfico. Ou, talvez você queira incentivar os compradores que compram com frequência (verdadeiros positivos) a fazê-lo novamente, selecionando uma seção de usuários que favoreça o lado direito do gráfico.

## Qualidade da previsão {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tabela de correlação de eventos {#correlation_table}

Essa análise exibe atributos ou comportamentos do usuário que estão correlacionados com eventos no público-alvo da previsão. Os atributos avaliados são Idade, País, Gênero e Idioma. Os comportamentos analisados incluem sessões, compras, total de dólares gastos, eventos personalizados e campanhas e etapas do Canvas recebidas nos últimos 30 dias.

As tabelas são divididas em esquerda e direita, para maior e menor probabilidade de realizar o evento, respectivamente. Para cada linha, a proporção pela qual os usuários com o comportamento ou atributo na coluna da esquerda têm maior ou menor probabilidade de realizar o evento é exibida na coluna da direita. Esse número é a proporção das pontuações de probabilidade dos usuários com esse comportamento ou atributo dividida pela probabilidade de realizar o evento em todo o público da previsão.

Essa tabela é atualizada somente quando a previsão é retreinada e não quando as pontuações de probabilidade do usuário são atualizadas.

{% alert note %}
Os dados de correlação das previsões de visualização ficarão parcialmente ocultos. É necessário fazer uma compra para revelar essas informações. Entre em contato com o gerente da sua conta para obter mais informações.
{% endalert %}
