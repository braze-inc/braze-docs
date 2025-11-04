---
nav_title: Eventos preditivos
article_title: Eventos preditivos
description: "Este artigo aborda o Predictive Events (anteriormente Predictive Purchases), uma ferramenta que oferece aos profissionais de marketing a capacidade de identificar e enviar mensagens aos usuários com base na probabilidade de eles realizarem um evento."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Eventos preditivos

> Os Predictive Events oferecem aos profissionais de marketing uma ferramenta poderosa para identificar e enviar mensagens aos usuários com base na probabilidade de eles realizarem um evento. Quando você cria uma previsão de evento, o Braze treina um modelo de aprendizado de máquina usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender com a atividade anterior e prever a atividade futura.

## Sobre a Predictive Events

Depois que uma previsão é criada, os usuários recebem uma [pontuação de probabilidade]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) entre 0 e 100, indicando a probabilidade de eles realizarem o evento selecionado. Quanto maior a pontuação, maior a probabilidade de um usuário realizar esse evento. Os usuários também são classificados por categorias de probabilidade baixa, média e alta.

O valor real dos eventos preditivos está no uso dos resultados da previsão para criar um segmento ou uma campanha. Os profissionais de marketing podem criar campanhas direcionadas diretamente na página **Prediction** para obter resultados imediatos de aumento de receita ou salvar um segmento para uma futura campanha ou Canvas. Não tem certeza de quem deve ser o primeiro alvo? Leia nossas [considerações estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para enviar mensagens aos usuários com base em sua pontuação de probabilidade.

Gráfico intitulado "How Predictive Events Works" (Como funcionam os eventos preditivos), que mostra os dados do usuário sendo canalizados para o modelo de aprendizado de máquina. O rótulo diz: "Treine com dados históricos, compare o comportamento dos usuários que realizaram o evento em um determinado período com aqueles que não o fizeram". Ele também mostra os resultados do aprendizado de máquina, em que os usuários são classificados de menos propensos a mais propensos a realizar o evento. O rótulo diz: "Preveja a probabilidade de eventos futuros, atribua uma pontuação de probabilidade aos usuários para um direcionamento preciso e conveniente".]({% image_buster /assets/img/how_predictive_events_works.png %})

## Acesso a eventos preditivos

A página **Predictions (Previsões** ) está localizada na seção **Analytics**. Para obter acesso total, entre em contato com o gerente da sua conta.

Antes de comprar esse recurso, ele está disponível no modo de visualização. Isso permitirá que você veja uma previsão de demonstração com dados sintéticos, além de criar um modelo de previsão de visualização por vez. Essa previsão será criada com base nos dados reais do usuário, mas não permitirá que você direcione mensagens aos usuários de acordo com a pontuação de probabilidade deles. Ele também não será atualizado regularmente após a criação.

Com a visualização, você também pode editar e reconstruir essa previsão ou arquivá-la e criar outras para testar a [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) esperada de [diferentes públicos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) e se familiarizar com a análise.
