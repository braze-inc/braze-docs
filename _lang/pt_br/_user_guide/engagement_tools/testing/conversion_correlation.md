---
nav_title: Correlação de conversão
article_title: Correlação de conversão
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Este artigo de referência explica a análise de correlação de conversão na página do Campaign Analytics."
tool: 
  - Reports
  
---

# Correlação de conversão

> A análise de correlação de conversão na página **Campaign Analytics** fornece informações sobre quais atributos e comportamentos do usuário ajudam ou prejudicam os resultados definidos para as campanhas. 

## Visão geral

Para cada campanha, o Braze verifica uma lista de atributos e comportamentos do usuário e calcula se os usuários estão associados de forma estatisticamente significativa a aumentos ou reduções em cada um dos [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) que você escolheu para a campanha. Também calculamos a probabilidade maior ou menor de conversão dos usuários com determinado atributo ou comportamento e, se for significativo, exibimos isso no lado correspondente da tabela. Os usuários com cada atributo ou comportamento de interesse são comparados com as taxas de todo o público da campanha como um todo. Os comportamentos e atributos que não têm correlação significativa com a conversão não são mostrados na tabela.

Para executar uma análise de correlação de conversão, selecione o evento de conversão de interesse no menu suspenso.

Painel Conversion Correlation (Correlação de conversões) que mostra um exemplo com "Select a conversion event" (Selecionar um evento de conversão) definido como "Primary Conversion Event - A" (Evento de conversão primário - A) com a configuração de evento como "Made Purchase within 12 hours (Any product)" (Compra efetuada em 12 horas (Qualquer produto)).]({% image_buster /assets/img/convcorr.png %})

## O que é verificado?

Verificamos os seguintes atributos tratando-os como variáveis categóricas. Em outras palavras, um usuário tem ou não tem cada valor possível desses atributos, e testamos se eles afetam a taxa de conversão.

-  País
-  Idioma
-  Gênero

Também verificamos se os itens a seguir afetam a taxa de conversão:

- Realização de quaisquer eventos personalizados
- Campanhas e telas recebidas nos últimos 30 dias (que não sejam a campanha que está sendo avaliada no momento)

Por fim, verificamos diversas variáveis comportamentais que podem assumir vários valores. Dividimos o seguinte em quatro grupos ou quartis e medimos a associação de estar nesse quartil com aumentos ou reduções na conversão:

- Idade
- Total de dólares gastos
- Número de sessões

## Quando posso verificar essa análise?

Essa análise fica disponível pelo menos 24 horas após o início do envio de uma campanha e analisa apenas os envios ocorridos nos últimos 30 dias. Se nenhum comportamento ou atributo se correlacionar significativamente com qualquer evento de conversão da campanha, o menu suspenso será desativado e uma mensagem será exibida informando que esse é o caso.

## Como o Braze verifica a significância

Verificamos a significância estatística usando o [intervalo de confiança de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Determinamos com 95% de confiança a taxa de conversão de todo o público da campanha. Essa é a chamada taxa básica. 

Em seguida, para cada uma das variáveis, também calculamos a taxa na qual os usuários com esse atributo específico ou comportamento de interesse converteram com 95% de confiança. Ao dividir esse valor pela taxa básica, podemos medir a proporção. Se for muito maior que 1, os usuários com o atributo ou comportamento têm maior probabilidade de conversão. Se for muito menor, é menos provável. Exibimos o valor da própria proporção na tabela. O valor só é exibido se estiver longe o suficiente de 1 para ser significativo no nível de confiança de 95%.

