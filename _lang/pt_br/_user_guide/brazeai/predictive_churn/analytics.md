---
nav_title: Análise de rotatividade
article_title: Análise preditiva de rotatividade
description: "Este artigo de referência aborda os diferentes componentes incluídos na página Churn Prediction Analytics e como eles podem ser usados para tomar decisões criteriosas e orientadas."
page_order: 1.5

---

# Análise preditiva de churn

> Depois que sua previsão tiver sido criada e treinada, você terá acesso à página **Prediction Analytics**. Esta página o ajuda a decidir quais usuários você deve segmentar com base em sua _Churn Risk Score_ ou categoria. 

## Sobre a análise preditiva de rotatividade

Assim que a previsão terminar de ser treinada e essa página for preenchida, você poderá simplesmente usar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) em segmentos ou campanhas para começar a usar os resultados do modelo. Mas, se você quiser ajuda para decidir quem e por que segmentar, esta página pode ajudar com base na precisão histórica do modelo e em suas próprias metas de negócios. 

Esses são os componentes que compõem a análise preditiva de rotatividade:

- [Churn Score e categoria](#churn_score)
- [Qualidade da previsão](#prediction_quality)
- [Precisão estimada](#estimated_results)
- [Tabela de correlação de rotatividade](#correlation_table)

A distribuição das pontuações para todo o público da previsão é exibida na parte superior da página em um gráfico que pode ser visualizado por categoria ou por pontuação. Os usuários em compartimentos mais à direita têm pontuações mais altas e são mais propensos a cancelar. Os usuários em compartimentos mais à esquerda têm menos probabilidade de mudar. O controle deslizante abaixo do gráfico permitirá que você selecione uma faixa de usuários e estime quais seriam os resultados da segmentação de usuários no intervalo selecionado de _Churn Risk Score_ ou categoria.

À medida que você mover o controle deslizante, a barra na metade esquerda do painel inferior informará quantos usuários de todo o público-alvo da previsão serão direcionados.

\![]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Pontuação e categoria de rotatividade {#churn_score}

Os usuários do público-alvo da previsão receberão um _Churn Risk Score_ entre 0 e 100. Quanto maior a pontuação, maior a probabilidade de rotatividade. 
- Os usuários com pontuações entre 0 e 50 serão rotulados na categoria de _baixo risco_. 
- Os usuários com pontuações entre 50 e 75 e entre 75 e 100 serão rotulados nas categorias _Médio Risco_ e _Alto Risco_, respectivamente. 

As pontuações e as categorias correspondentes serão atualizadas de acordo com a programação que você escolheu na página de criação do modelo. O número de usuários com pontuações de rotatividade em cada um dos 20 grupos de tamanho igual é exibido no gráfico na parte superior da página. Isso pode ajudá-lo a determinar como é o risco de rotatividade na população de acordo com essa previsão.

## Qualidade da previsão {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Precisão estimada {#estimated_results}

Na metade direita do painel abaixo do gráfico, mostramos estimativas da precisão esperada da segmentação dessa faixa do público-alvo da previsão. Com base nos dados sobre os usuários do público-alvo da previsão no passado e na precisão aparente do modelo para discriminar entre usuários que cancelam e não cancelam com base nesses dados anteriores, essas barras de progresso estimam uma mensagem potencial futura usando o público-alvo destacado com o controle deslizante:

\![]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Quantos usuários selecionados deverão se desligar
- Quantos usuários selecionados **não** devem se desligar

Com base nessas informações, recomendamos que você decida quantos churners deseja capturar e qual é o custo de um erro falso positivo para a sua empresa. Se estiver enviando uma promoção valiosa, convém manter o mínimo de não-churners direcionados e, ao mesmo tempo, obter o máximo de churners verdadeiros esperados que o modelo permitir. Ou, se você for menos sensível a falsos positivos e os usuários receberem mensagens adicionais, poderá enviar mais mensagens ao público-alvo para capturar mais churners esperados e ignorar os erros prováveis.

### Espera-se que os usuários mudem

Essa é uma estimativa de quantos churners reais serão direcionados corretamente. É claro que não conhecemos o futuro perfeitamente, portanto, não sabemos exatamente quais usuários do público-alvo da previsão serão desativados no futuro. Mas a previsão é uma inferência confiável. Com base no desempenho anterior, essa barra de progresso indica quantos do total de churners "reais" ou "verdadeiros" esperados no público-alvo de previsão (com base em taxas de churn anteriores) serão direcionados com a seleção de direcionamento atual. Esperamos que esse número de usuários se desfaça se você não os direcionar com nenhuma mensagem extra ou incomum.

### Espera-se que os usuários não se afastem 

Essa é uma estimativa de quantos usuários que não teriam feito churn serão incorretamente direcionados. Todos os modelos de aprendizado de máquina cometem erros. Pode haver usuários em sua seleção que tenham um _Churn Risk Score_ alto, mas que não acabem se desligando. Eles não se afastariam mesmo que você não tomasse nenhuma medida. Eles serão alvos de qualquer forma, portanto, isso é um erro ou "falso positivo". A largura total dessa segunda barra de progresso representa o número esperado de usuários que não se desligarão, e a parte preenchida representa aqueles que serão direcionados incorretamente usando a posição atual do controle deslizante.

## Tabela de correlação de rotatividade {#correlation_table}

Essa análise exibe todos os atributos ou comportamentos do usuário que estão correlacionados com a rotatividade de usuários no público-alvo da previsão histórica. As tabelas são divididas em esquerda e direita para maior e menor probabilidade de rotatividade, respectivamente. Para cada linha, a proporção pela qual os usuários com o comportamento ou o atributo na coluna da esquerda têm maior ou menor probabilidade de rotatividade é exibida na coluna da direita. Esse número é a proporção da probabilidade de rotatividade de usuários com esse comportamento ou atributo dividida pela probabilidade de rotatividade de todo o público-alvo da previsão.

Essa tabela é atualizada somente quando a previsão é treinada novamente e não quando _os Churn Risk Scores_ do usuário são atualizados.

{% alert note %}
Os dados de correlação das previsões de visualização ficarão parcialmente ocultos. É necessário fazer uma compra para revelar essas informações. Entre em contato com o gerente da sua conta para obter mais informações.
{% endalert %}
