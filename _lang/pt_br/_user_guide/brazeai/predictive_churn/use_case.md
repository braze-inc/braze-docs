---
nav_title: Caso de uso
article_title: Caso de uso Reduzir a rotatividade com conteúdo oportuno
description: "Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente o abandono de usuários."
page_type: tutorial
---

# Caso de uso: Reduzir a rotatividade com o reengajamento oportuno de conteúdo

> Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente o abandono de usuários. Em vez de esperar que a rotatividade ocorra, preveja quais usuários estão em risco e envie mensagens personalizadas enquanto eles ainda estão ativos.

Digamos que Camila seja gerente de CRM da MovieCanon, uma plataforma de streaming de filmes independentes, documentários e séries internacionais.

A equipe de Camila detectou uma tendência preocupante: os usuários se inscrevem, transmitem um ou dois filmes e depois desaparecem. Historicamente, eles tentaram enviar um e-mail genérico "Sentimos sua falta" uma semana depois, mas com uma taxa de conversão de apenas 3%, é muito pouco e muito tarde. A maioria dos usuários não se envolve novamente, e a rotatividade se torna inevitável.

Camila quer mudar isso. Em vez de reagir à rotatividade depois que ela acontece, ela usa o Predictive Churn para identificar os usuários que provavelmente ficarão inativos nos próximos 14 dias, dando à sua equipe a oportunidade de reengajar as pessoas enquanto elas ainda estão ativas.

Este tutorial explica como a Camila:

- Cria um modelo de previsão de rotatividade com base no comportamento do usuário
- Segmenta os usuários por nível de risco
- Cria uma campanha de reengajamento adaptada às pessoas em maior risco
- Avalia o impacto usando a análise da campanha

## Etapa 1: Criar um modelo de previsão de rotatividade

Camila começa modelando o resultado que deseja evitar: usuários que se tornam inativos. Para a MovieCanon, a rotatividade significa não iniciar um fluxo dentro de 14 dias - portanto, esse é o comportamento que ela deseja prever.

1. No painel do Braze, Camila vai para **Analytics** > **Predictive Churn**.
2. Ela cria uma nova previsão de rotatividade e a nomeia "Risco de rotatividade em 2 semanas".
3. Para definir a rotatividade, ela seleciona `do not` e o evento personalizado `stream_started`, que indica envolvimento ativo.
4. Ela define a janela de previsão para 14 dias, o que significa que o modelo identificará os usuários que provavelmente passarão 14 dias sem iniciar um novo fluxo.

Definição de rotatividade mostrando a rotatividade definida como um usuário que não realiza um evento personalizado "stream_started" nos últimos 14 dias.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Ela seleciona um público-alvo de previsão que inclui todos os usuários que acionaram eventos relevantes nos últimos 30 dias - dando ao modelo um comportamento recente suficiente para aprender.
6\. Ela define o cronograma de atualização da previsão como semanal para que as pontuações permaneçam atualizadas.
7\. Ela seleciona **Criar previsão**.

Em seguida, o modelo começa a ser treinado, analisando comportamentos como sessões recentes, frequência de visualização e interações com o conteúdo para revelar padrões que preveem o abandono. Uma hora depois, Camila recebe um e-mail informando que sua previsão terminou o treinamento, então ela o abre no Braze e verifica a pontuação de [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Ele é rotulado como "Bom", o que significa que as previsões do modelo provavelmente serão precisas e confiáveis. Confiante no desempenho do modelo, ela segue em frente.

## Etapa 2: Segmentar usuários por risco de rotatividade

Depois que o modelo termina o treinamento, o Braze atribui a cada usuário qualificado um [Churn Risk Score]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) entre 0 e 100. 

Para determinar um limite inicial para a segmentação, Camila usa o controle deslizante de público-alvo da previsão para visualizar quantos usuários se enquadram em cada faixa de pontuação e qual é a precisão da previsão nesse nível. Ela equilibra a cobertura e a precisão com base nos verdadeiros positivos esperados. Com base nisso, ela decide visar pontuações de risco superiores a 70. 

1. Camila navega até Segmentos no Braze.
2. Ela cria um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) usando o [filtro Churn Risk Score]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) e seleciona a previsão de rotatividade que criou:
   - **Probabilidade de rotatividade:** Pontuação superior a 70

Filtragem de segmentos para usuários com uma pontuação de risco de rotatividade superior a 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Etapa 3: Direcione os usuários em risco com conteúdo recorrente de reengajamento

Com a previsão e o segmento prontos, Camila configura uma campanha recorrente que atinge automaticamente os usuários em risco a cada semana.

1. Camila cria uma campanha recorrente e ativa o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), de modo que cada mensagem é entregue quando cada usuário individual tem maior probabilidade de se envolver, em vez de depender de um dia e horário fixos.
2. Ela tem como alvo o segmento "Likely to churn" que acabou de criar.
3. Ela define o evento de conversão da campanha como o evento personalizado `stream_started`, para rastrear quantos usuários realmente retornam para visualizar o conteúdo.
4. Camila escolhe o e-mail como seu canal principal - ele lhe dá espaço para destacar várias opções de conteúdo personalizado em um formato visualmente rico, sem muita pressão. O e-mail inclui:
   - Uma lista de observação personalizada com base em [recomendações de itens de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/), selecionada dinamicamente no catálogo do MovieCanon
   - Uma chamada para ação que os leve diretamente para o aplicativo.

Isso garante que, a cada semana, o MovieCanon alcance apenas os usuários que precisam de um empurrãozinho - sem excesso de mensagens, sem adivinhações.

### Exemplo de e-mail

- **Linha de assunto:** Não deixe esses títulos pendentes
- **Cabeçalho:** Seu próximo grande relógio está esperando
- **Corpo:** Não está tocando no play há algum tempo? Não se preocupe, nós preparamos algumas opções só para você. De thrillers de ritmo lento a documentários premiados, há algo aqui com o seu nome.
- **CTA:** Ver mais opções

## Etapa 4: Medir o desempenho

Depois de algumas semanas, Camila verifica [as análises da campanha]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) para avaliar o desempenho da estratégia. 

Ela está vendo:

- *Taxa de abertura:* 31%
- *Taxa de cliques:* 15%
- *Taxa de conversão* (fluxo iniciado em 48 horas): 11%

Em comparação com a antiga campanha "Sentimos sua falta" (em que as taxas de conversão giravam em torno de 3%), esse novo fluxo reduz a rotatividade no grupo-alvo em 28%. Ela se aprofunda no [relatório do funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para identificar onde os usuários caem. Embora as taxas de abertura e de cliques sejam altas, ela percebe um pequeno atrito entre o clique e a conversão, o que a leva a considerar a possibilidade de testar o texto da CTA ou fazer experiências com o layout.

Para entender o impacto a longo prazo, a Camila também acompanha o volume de usuários que entram no segmento "Likely to churn" semana a semana. Isso a ajuda a avaliar a saúde geral do ciclo de vida e a informar a estratégia de retenção em um nível mais amplo. Por fim, ela revisita a página [Prediction Analytics]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) da previsão de rotatividade para comparar a rotatividade prevista com a real - uma verificação útil para garantir que o modelo esteja funcionando conforme o esperado.

Com base nesses insights, Camila planeja fazer testes A/B nas linhas de assunto, testar diferentes janelas de tempo e experimentar formatos de conteúdo como recomendações em estilo carrossel em uma mensagem no aplicativo.

Com o Predictive Churn, o Intelligent Timing e a personalização com tecnologia de IA, a equipe de Camila não está apenas reagindo ao churn - está se antecipando a ele. E sua campanha é executada discretamente em segundo plano, atingindo as pessoas certas, no momento certo, com conteúdo que realmente lhes interessa.
