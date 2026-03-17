---
nav_title: Churn previsto
article_title: Churn previsto
description: "Esta landing page aborda o Predictive Churn, uma ferramenta do pacote preditivo da Braze que permite definir o que significa churn para sua empresa, bem como os usuários que você gostaria de evitar que abandonassem sua marca."
page_order: 8
alias: /predictive_churn/
search_rank: 2
---

# Churn previsto

> Com o Predictive Churn, uma ferramenta do pacote preditivo da Braze, você pode definir o que significa rotatividade para o seu negócio e identificar os usuários que deseja manter. Quando você cria uma previsão, a Braze treina um modelo de machine learning usando [árvores de decisão com reforço de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para reconhecer usuários em risco, analisando padrões de comportamento passado — tanto de usuários desistentes quanto daqueles que permaneceram.

{% alert tip %}
Para saber mais, consulte [Definição de churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) e [Público-alvo da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Sobre o churn preditivo

Após a construção do modelo de previsão, os usuários do público-alvo da previsão receberão uma [pontuação de risco de cancelamento]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) entre 0 e 100, indicando a probabilidade de cancelamento de acordo com sua definição. Quanto maior a pontuação, maior a probabilidade de churn do usu'ario. 

A atualização das pontuações de risco do público de previsão pode ser feita com a [frequência que você escolher]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction). Dessa forma, você pode entrar em contato com usuários que correm o risco de churn antes que isso aconteça e evitar que isso ocorra. Usando até três previsões ativas, é possível aproveitar o Predictive Churn para adaptar modelos individuais para ajudar a evitar o churn em segmentos específicos dos usuários desistentes que você considera mais valiosos.

![Uma visão geral do churn, que inclui um público de previsão passado com treinamento com dados históricos. Isso contribui para prever o risco de churn futuro, medindo o público previsto para hoje com uma pontuação de risco de churn.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acessando a previsão de churn

{% multi_lang_include brazeai/predictions_page_access.md %}

Antes de comprar esse recurso, ele está disponível em modo de prévia. Isso permitirá ver uma previsão de churn de demonstração com dados sintéticos e criar um modelo de previsão de churn com base nos dados de usuários de cada vez. Essa prévia não permitirá o direcionamento de usuários para envio de mensagens de acordo com o risco de churn e não será atualizada regularmente após a criação.

Com a prévia, você também pode editar e reconstruir sua previsão ou arquivá-la e criar outras para testar a [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) esperada de diferentes [definições]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
