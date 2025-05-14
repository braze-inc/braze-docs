---
nav_title: Churn previsto
article_title: Churn previsto
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Churn previsto"
guide_top_text: "O churn de clientes, também conhecido como rotatividade de clientes ou perda de clientes, é uma das métricas mais importantes a serem consideradas pelas empresas em crescimento. Ter as ferramentas certas para lidar com o churn é crucial para minimizar a perda e maximizar a retenção de clientes. Para dar um salto nesses usuários potencialmente desistentes, a Braze oferece o Churn previsto, uma abordagem para tentar diminuir o churn."
description: "Essa landing page aborda o Predictive Churn, uma ferramenta que permite definir o que significa churn para sua empresa, bem como os usuários que você gostaria de evitar."

guide_featured_title: "Tópicos"
guide_featured_list:
- name: Criação de uma previsão de churn
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Análises de dados
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Usuários de envio de mensagens
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: Solução de problemas
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## Visão geral

![Uma visão geral do churn, que inclui um público de previsão passado com treinamento com dados históricos. Isso contribui para prever o risco de churn futuro, medindo o público previsto para hoje com uma pontuação de risco de churn.][1]

> Com o Churn previsto, é possível definir o que significa churn para a sua empresa[(definição de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) e os usuários que você gostaria de evitar que se tornem churn[(público de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Quando você cria uma previsão, a Braze treina um modelo de machine learning usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para identificar os usuários em risco de churn, aprendendo com os padrões de atividade de usuários anteriores que tiveram e não tiveram churn de acordo com a sua definição.

Depois que o modelo de previsão for criado, os usuários do público de previsão receberão uma [pontuação de risco de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) entre 0 e 100, indicando a probabilidade de churn de acordo com sua definição. Quanto maior a pontuação, maior a probabilidade de churn do usu'ario. 

A atualização das pontuações de risco do público de previsão pode ser feita com a [frequência que você escolher]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). Dessa forma, é possível entrar em contato com os usuários que correm o risco de churn antes que eles realmente o façam e evitar que isso aconteça. Usando até três previsões ativas, é possível aproveitar o Predictive Churn para adaptar modelos individuais para ajudar a evitar o churn em segmentos específicos dos usuários desistentes que você considera mais valiosos.

## Acesso ao churn previsto

A página **Previsões** está localizada na seção **Análises de dados**. Para obter acesso total, entre em contato com o gerente da sua conta.

Antes de comprar esse recurso, ele está disponível em modo de prévia. Isso permitirá ver uma previsão de churn de demonstração com dados sintéticos e criar um modelo de previsão de churn com base nos dados de usuários de cada vez. Essa prévia não permitirá o direcionamento de usuários para envio de mensagens de acordo com o risco de churn e não será atualizada regularmente após a criação.

Com a prévia, você também pode editar e reconstruir sua previsão ou arquivá-la e criar outras para testar a [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) esperada de diferentes [definições]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
