---
nav_title: análises de previsão
article_title: análises de previsão
description: "Este artigo de referência cobre os diferentes componentes incluídos na página de análises de previsão de churn e como eles podem ser usados para tomar decisões perspicazes e orientadas."
page_order: 2

---

# análises de previsão

> Depois que sua previsão for construída e treinada, você terá acesso à página de **análises de previsão**. Esta página ajuda você a decidir quais usuários deve segmentar com base em seu _Pontução de risco de churn_ ou categoria. 

Assim que a previsão estiver concluída e esta página estiver populada, você pode começar a usar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) em segmentos ou campanhas para começar a usar os resultados do modelo. Mas, se você quiser ajuda para decidir quem direcionar e por quê, esta página pode ajudar com base na precisão histórica do modelo e nos seus próprios objetivos de negócios. 

**Componentes de análise de dados**<br>
- [Pontuação de churn e categoria](#churn_score)<br>
- [Qualidade da Previsão](#prediction_quality)<br>
[Resultados estimados](#estimated_results)<br>
[Tabela de correlação de churn](#correlation_table)

## Visão geral

A distribuição das pontuações para todo o público de previsão é exibida no topo da página em um gráfico que você pode visualizar, por categoria ou por pontuação. Usuários em grupos mais à direita têm pontuações mais altas e são mais propensos a churn. Usuários em grupos mais à esquerda são menos propensos a churn. O controle deslizante abaixo do gráfico permitirá que você selecione um grupo de usuários e estime quais seriam os resultados do direcionamento de usuários na faixa selecionada de _Pontuação de Risco de Churn_ ou categoria.

![][4]{: style="max-width:90%"}

À medida que você move o controle deslizante, a barra na metade esquerda do painel inferior informará quantos usuários do público total de previsão seriam alvo.

## Pontuação e categoria de churn {#churn_score}

Os usuários no público de previsão receberão uma _pontuação de risco de churn_ entre 0 e 100. Quanto maior a pontuação, maior a probabilidade de churn. 
- Usuários com pontuações entre 0 e 50 serão rotulados na categoria _Baixo Risco_. 
- Usuários com pontuações entre 50 e 75, e 75 e 100 serão rotulados nas categorias _Médio Risco_ e _Alto Risco_, respectivamente. 

As pontuações e as categorias correspondentes serão atualizadas de acordo com o cronograma que você escolheu na página de criação do modelo. O número de usuários com pontuações de churn em cada um dos 20 grupos de tamanho igual é exibido no gráfico no topo da página. Isso pode ajudar você a determinar como é o risco de churn em toda a população de acordo com esta previsão.

## Direcionamento de usuários para reduzir churn

### Qualidade da previsão {#prediction_quality}

Para medir a precisão do seu modelo, a métrica de _Qualidade da Previsão_ mostrará quão eficaz este modelo específico de machine learning parece ser quando testado em dados históricos. Consulte a [Qualidade da Previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) para saber mais sobre a métrica.

Aqui está o que recomendamos para vários intervalos de _Qualidade da Previsão_:

| Qualidade da Previsão Faixa (%) | Recomendação |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisão exemplar. É improvável que a alteração das definições de público traga mais benefícios. |
| 40 - 60 | Bom. Este modelo produzirá previsões precisas, mas pode valer a pena testar outras configurações de público para tentar obter resultados melhores. |
| 20 - 40| Justo. Este modelo pode proporcionar precisão e benefícios, mas experimente diferentes definições de público para ver se a performance melhora. |
| 0 - 20 | Pobre. Recomendamos alterar suas definições de público e tentar novamente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A previsão será treinada novamente a cada duas semanas e atualizada juntamente com a métrica de qualidade da previsão para manter suas previsões atualizadas com os padrões de comportamento mais recentes dos usuários. A última vez que esse re-treinamento ocorreu será exibida na página de lista de previsões, bem como na página de análise de dados da sua previsão.

## Resultados estimados {#estimated_results}

![][6]{: style="float:right;max-width:30%;margin-left:15px;"}

Na metade direita do painel abaixo do gráfico, mostramos estimativas da precisão esperada do direcionamento deste segmento do público de previsão. Com base em dados sobre usuários no público de previsão no passado, e a aparente precisão do modelo para discriminar entre usuários que desistem e não desistem nesses dados passados, essas barras de progresso estimam para uma mensagem potencial futura usando o público destacado com o controle deslizante:

1. Uma estimativa de quantos canceladores reais serão corretamente direcionados <br><br> Claro, não conhecemos o futuro perfeitamente, então não sabemos exatamente quais usuários do público de previsão irão sofrer churn no futuro. Mas a previsão é uma inferência confiável. Com base na performance passada, esta barra de progresso indica quantos do total de "churners" "atuais" ou "verdadeiros" esperados no público de previsão (com base nas taxas de churn anteriores) serão direcionados com a seleção de direcionamento atual. Esperaríamos esse número de usuários com churn se você não os direcionar com qualquer envio de mensagens extra ou incomum. <br><br>

2. Uma estimativa de quantos usuários que na verdade não teriam desistido serão incorretamente segmentados<br><br>Todos os modelos de machine learning cometem erros. Pode haver usuários em sua seleção que tenham uma alta _pontuação de risco de churn_, mas que não acabem com churn. Eles não sofrerão churn mesmo que você não faça nada. Eles serão segmentados de qualquer maneira, então isso é um erro ou "falso positivo." A largura total desta segunda barra de progresso representa o número esperado de usuários que não irão churn, e a parte preenchida são aqueles que serão incorretamente alvo usando a posição atual do controle deslizante.

Usando essas informações, incentivamos você a decidir quantos dos clientes que cancelaram você deseja capturar e qual é o custo de um erro falso positivo para o seu negócio. Se você está enviando uma promoção importante, pode querer manter os não-desistentes direcionados ao mínimo enquanto obtém o máximo de desistentes verdadeiros esperados que o modelo permitir. Ou, se você for menos sensível a falsos positivos e os usuários receberem envio de mensagens extra, você pode enviar mensagens para mais do público para capturar mais churners esperados e ignorar os prováveis erros.

## Tabela de correlação de churn {#correlation_table}

Esta análise exibe quaisquer atributos ou comportamentos de usuário que estão correlacionados com o churn de usuário no público de previsão histórica. As tabelas são divididas em esquerda e direita para mais e menos propensos a churn, respectivamente. Para cada linha, a razão pela qual os usuários com o comportamento ou atributo na coluna da esquerda são mais ou menos propensos a churn é exibida na coluna da direita. Este número é a razão da probabilidade de churn de usuários com este comportamento ou atributo dividida pela probabilidade de churn de todo o público de previsão.

Esta tabela é atualizada apenas quando a previsão é re-treinada e não quando os _Scores de Risco de Churn_ do usuário são atualizados.

{% alert note %}
Os dados de correlação para prévia das previsões serão parcialmente ocultos. Uma compra é necessária para revelar esta informação. Entre em contato com o seu gerente de conta para saber mais.
{% endalert %}

[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}
[4]: {% image_buster /assets/img/churn/churnTargeting.gif %}