---
nav_title: Eventos previstos
article_title: Eventos previstos
description: "Este artigo aborda os Predictive Events (anteriormente Predictive Purchases), uma ferramenta que oferece aos profissionais de marketing a capacidade de identificar e enviar mensagens aos usuários com base na probabilidade de realizarem um evento."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Eventos previstos

> Os eventos de previsão oferecem aos profissionais de marketing uma ferramenta poderosa para identificar e enviar mensagens privadas aos usuários com base na probabilidade de realizarem um evento. Quando você cria uma previsão de evento, o Braze treina um modelo de machine learning usando [árvores de decisão com aumento de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender com a atividade anterior e prever a atividade futura.

## Sobre os eventos preditivos

Depois que uma previsão é criada, é atribuída aos usuários uma [pontuação de probabilidade]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) entre 0 e 100, indicando a probabilidade de eles realizarem o evento selecionado. Quanto maior a pontuação, maior a probabilidade de um usuário realizar esse evento. Os usuários também são classificados por categorias de probabilidade baixa, média e alta.

O valor real dos eventos preditivos está no uso dos resultados da previsão para criar um segmento ou uma campanha. Os profissionais de marketing podem criar campanhas direcionadas diretamente na página de **previsão** para obter resultados imediatos de aumento de receita ou salvar um segmento para uma futura campanha ou Canvas. Não tem certeza de quem deve ser o primeiro alvo? Leia nossas [considerações estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para o envio de mensagens aos usuários com base em sua pontuação de probabilidade.

![Gráfico intitulado "Como Funciona a Previsão de Eventos", exibindo dados de usuários sendo canalizados para o modelo de machine learning. O rótulo diz "Treine com dados históricos, compare o comportamento dos usuários que realizaram o evento em um determinado período com aqueles que não o fizeram". São mostrados também os resultados do machine learning, em que os usuários são classificados de menos propensos a mais propensos a realizar o evento. O rótulo diz: "Preveja a probabilidade de eventos futuros, atribua uma pontuação de probabilidade aos usuários para um direcionamento preciso e conveniente."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Acesso a eventos de previsão

A página **Previsões** está localizada na seção **Análises de dados**. Para obter acesso total, entre em contato com o gerente da sua conta.

Antes de comprar esse recurso, ele está disponível em modo de prévia. Isso lhe permitirá ver uma previsão de demonstração com dados sintéticos, bem como criar um modelo de previsão prévia por vez. Essa previsão será criada com base nos dados reais do usuário, mas não permitirá o direcionamento de mensagens para os usuários de acordo com a pontuação de probabilidade deles. Ele também não será atualizado regularmente após a criação.

Com a Prévia, você também pode editar e reconstruir essa previsão ou arquivá-la e criar outras para testar a [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) esperada de [diferentes públicos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) e se familiarizar com as análises preditivas.
