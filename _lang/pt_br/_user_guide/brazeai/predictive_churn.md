---
nav_title: Churn preditivo
article_title: Churn preditivo
description: "Esta página de destino aborda o Predictive Churn, uma ferramenta que permite definir o que a rotatividade significa para sua empresa, bem como os usuários que você gostaria de evitar."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Churn preditivo

> Com o Predictive Churn, você pode definir o que significa churn para a sua empresa e identificar os usuários que deseja reter. Quando você cria uma previsão, o Braze treina um modelo de aprendizado de máquina usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para reconhecer usuários em risco, analisando padrões de comportamento anterior, tanto de usuários que cancelaram quanto daqueles que não cancelaram.

{% alert tip %}
Para obter mais informações, consulte [Definição de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) e [audiência de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Sobre o Predictive Churn

Depois que o modelo de previsão for criado, os usuários do público-alvo da previsão receberão uma [pontuação de risco de rotatividade]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 e 100, indicando a probabilidade de rotatividade de acordo com a sua definição. Quanto maior for a pontuação, maior será a probabilidade de um usuário cancelar a assinatura. 

A atualização das pontuações de risco do público-alvo da previsão pode ser feita na [frequência que você escolher]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). Dessa forma, você pode entrar em contato com os usuários que correm o risco de se afastar antes que eles se afastem e evitar que isso aconteça. Usando até três previsões ativas, você pode aproveitar o Predictive Churn para adaptar modelos individuais para ajudar a evitar a rotatividade em segmentos específicos dos usuários que você considera mais valiosos.

\![Uma visão geral da rotatividade, que inclui um público de previsão anterior com treinamento com dados históricos. Isso contribui para prever o risco de rotatividade futura, medindo o público previsto hoje com uma pontuação de risco de rotatividade.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acesso à rotatividade preditiva

A página **Predictions (Previsões** ) está localizada na seção **Analytics**. Para obter acesso total, entre em contato com o gerente da sua conta.

Antes de comprar esse recurso, ele está disponível no modo de visualização. Isso permitirá que você veja uma demonstração de previsão de rotatividade com dados sintéticos e crie um modelo de previsão de rotatividade com base nos dados do usuário de cada vez. Essa visualização não permitirá que você direcione usuários para mensagens de acordo com o risco de rotatividade e não será atualizada regularmente após a criação.

Com a visualização, você também pode editar e reconstruir sua previsão ou arquivá-la e criar outras para testar a [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) esperada de diferentes [definições]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
