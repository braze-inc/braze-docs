---
nav_title: Churn previsto
article_title: Churn previsto
description: "Essa landing page aborda o Predictive Churn, uma ferramenta que permite definir o que significa churn para sua empresa, bem como os usuários que você gostaria de evitar."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Churn previsto

> Com o Predictive Churn, é possível definir o que significa churn para a sua empresa e identificar os usuários que deseja reter. Quando você cria uma previsão, o Braze treina um modelo de machine learning usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para reconhecer usuários em risco, analisando padrões de comportamento passado, tanto de usuários desistentes quanto daqueles que não o fizeram.

{% alert tip %}
Para saber mais, consulte [Definição de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) e [público de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Sobre a previsão de churn

Depois que o modelo de previsão for criado, os usuários do público de previsão receberão uma [pontuação de risco de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 e 100, indicando a probabilidade de churn de acordo com sua definição. Quanto maior a pontuação, maior a probabilidade de churn do usu'ario. 

A atualização das pontuações de risco do público de previsão pode ser feita com a [frequência que você escolher]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). Dessa forma, é possível entrar em contato com os usuários que correm o risco de churn antes que eles realmente o façam e evitar que isso aconteça. Usando até três previsões ativas, é possível aproveitar o Predictive Churn para adaptar modelos individuais para ajudar a evitar o churn em segmentos específicos dos usuários desistentes que você considera mais valiosos.

![Uma visão geral do churn, que inclui um público de previsão passado com treinamento com dados históricos. Isso contribui para prever o risco de churn futuro, medindo o público previsto para hoje com uma pontuação de risco de churn.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acesso à previsão de churn

A página **Previsões** está localizada na seção **Análises de dados**. Para obter acesso total, entre em contato com o gerente da sua conta.

Antes de comprar esse recurso, ele está disponível em modo de prévia. Isso permitirá ver uma previsão de churn de demonstração com dados sintéticos e criar um modelo de previsão de churn com base nos dados de usuários de cada vez. Essa prévia não permitirá o direcionamento de usuários para envio de mensagens de acordo com o risco de churn e não será atualizada regularmente após a criação.

Com a prévia, você também pode editar e reconstruir sua previsão ou arquivá-la e criar outras para testar a [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) esperada de diferentes [definições]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
