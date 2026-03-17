---
nav_title: Caso de uso
article_title: "Caso de uso: Reduza o churn com conteúdo oportuno"
description: "Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente a perda de usuários."
page_type: tutorial
---

# Caso de uso: Reduza o churn com o engajamento oportuno do conteúdo

> Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente a perda de usuários. Em vez de esperar que o churn aconteça, faça a previsão de quais usuários estão em risco e envie mensagens personalizadas enquanto eles ainda estão ativos.

Digamos que Camila é gerente de CRM na MovieCanon, uma plataforma de streaming para filmes independentes, documentários e séries internacionais.

A equipe de Camila identificou uma tendência preocupante: os usuários se inscrevem, assistem a um ou dois filmes e depois desaparecem. Historicamente, eles tentaram enviar um e-mail genérico dizendo “Sentimos sua falta” uma semana depois, mas com uma taxa de conversão de apenas 3%, isso foi muito pouco e muito tarde. A maioria dos usuários não volta ao engajamento, e o churn se torna inevitável.

Camila quer mudar isso. Em vez de reagir à rotatividade depois que ela ocorre, ela usa o Predictive Churn para identificar usuários que provavelmente ficarão inativos nos próximos 14 dias, dando à sua equipe a oportunidade de promover o engajamento das pessoas enquanto elas ainda estão ativas.

Este tutorial mostra como Camila:

- Cria um modelo de previsão de churn com base no comportamento do usuário.
- Segmenta os usuários por nível de risco
- Cria uma campanha de engajamento personalizada para aqueles que estão em maior risco
- Avalia o impacto usando a análise de dados de campanha

## Etapa 1: Crie um modelo de previsão de churn

Camila começa modelando o resultado que deseja evitar: usuários se tornando inativos. Para MovieCanon, churn significa não iniciar uma transmissão dentro de 14 dias — então esse é o comportamento que ela deseja prever.

1. No dashboard do Braze, Camila acessa **Análise de Dados** > **Previsão de churn**.
2. Ela cria uma nova previsão de churn e nomeia-a “Risco de churn em duas semanas”.
3. Para definir a churn, ela seleciona`do not`  e o evento personalizado`stream_started` , que indica engajamento ativo.
4. Ela define uma janela de previsão para 14 dias, o que significa que o modelo identificará usuários que provavelmente ficarão 14 dias sem iniciar uma nova transmissão.

![Definição de rotatividade mostrando a rotatividade definida como um usuário que não realizou um evento personalizado"stream_started" nos últimos 14 dias.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Ela seleciona um público de previsão que inclui todos os usuários que dispararam eventos relevantes nos últimos 30 dias, fornecendo ao modelo comportamento recente suficiente para aprender.
6\. Ela define a programação de atualização das previsões para semanalmente, para que as pontuações permaneçam atualizadas.
7\. Ela seleciona **Criar previsão**.

O modelo então inicia o treinamento, analisando comportamentos como sessões recentes, frequência de visualização e interações com o conteúdo para revelar padrões que fazem a previsão do abandono. Uma hora depois, Camila recebe um e-mail informando que sua previsão concluiu o treinamento, então ela a abre no Braze e verifica a pontuação [de qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Está classificado como “Bom”, o que significa que as previsões do modelo são provavelmente precisas e confiáveis. Confiante na performance do modelo, ela segue em frente.

## Etapa 2: Segmente os usuários por risco de churn

Após o modelo concluir o treinamento, a Braze atribui a cada usuário elegível uma [pontuação de risco de cancelamento]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) entre 0 e 100. 

Para determinar um limite inicial para o direcionamento, Camila usa o controle deslizante de público-alvo da previsão para obter uma prévia de quantos usuários se enquadram em cada faixa de pontuação e qual é a precisão da previsão nesse nível. Ela equilibra a cobertura e a precisão com base nos verdadeiros positivos esperados. Com base nisso, ela decide realizar o direcionamento para pontuações de risco superiores a 70. 

1. Camila navega até Segments no Braze.
2. Ela cria um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) usando o [filtro Pontuação de risco de churn]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) e seleciona a previsão de churn que criou:
   - **Provável churn:** Pontuação superior a 70

![Filtragem de segmento para usuários com pontuação de risco de churn superior a 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Etapa 3: Direcione usuários em risco com conteúdo recorrente para engajamento

Com sua previsão e segmento prontos, Camila configura uma campanha recorrente que alcança automaticamente os usuários que se tornam vulneráveis a cada semana.

1. Camila cria uma campanha recorrente e ativa [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), para que cada mensagem seja entregue quando cada usuário individual estiver mais propenso a realizar engajamento, em vez de depender de um dia e horário fixos.
2. Ela realiza o direcionamento para o grupo “Prováveis desistentes” que acabou de criar.
3. Ela define o evento de conversão da campanha como evento personalizado`stream_started`, para realizar o rastreamento de quantos usuários realmente retornam para visualizar o conteúdo.
4. Camila escolhe o e-mail como seu canal principal, pois ele lhe dá espaço para destacar várias opções de conteúdo personalizado em um formato visualmente rico, sem muita pressão. O e-mail inclui:
   - Uma lista de observação personalizada alimentada por [recomendações de itens com IA]({{site.baseurl}}/user_guide/brazeai/recommendations/), selecionadas dinamicamente a partir do catálogo da MovieCanon.
   - Uma chamada à ação que os leva diretamente para o app.

Isso garante que, a cada semana, o MovieCanon alcance apenas os usuários que precisam de um empurrãozinho — sem excesso de envio de mensagens, sem suposições.

### Exemplo de e-mail

- **Assunto:** Não deixe esses títulos pendentes
- **Cabeçalho:** O seu próximo relógio fantástico está à sua espera
- **Corpo:** Não aperta o play há algum tempo? Não se preocupe, selecionamos algumas opções especialmente para você. De thrillers de suspense a documentários premiados, há algo aqui com o seu nome escrito.
- **CTA:** Ver mais sugestões

## Etapa 4: Meça o desempenho

Após algumas semanas, Camila verifica [a análise de dados]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) [da campanha]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) para avaliar a performance da estratégia. 

Ela vê:

- *Taxa de abertura:* 31%
- *Taxa de cliques:* 15%
- *Taxa de conversão* (transmissão iniciada em 48 horas): 11%

Em comparação com a antiga campanha “Sentimos sua falta” (onde as taxas de conversão oscilavam em torno de 3%), esse novo fluxo reduz o churn no grupo-alvo em 28%. Ela analisa o [relatório do funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para identificar onde os usuários abandonam o processo. Embora as taxas de abertura e cliques sejam altas, ela percebe um leve atrito entre o clique e a conversão, o que a leva a considerar testar o texto da CTA ou experimentar um novo layout.

Para entender o impacto a longo prazo, Camila também realiza o rastreamento do volume de usuários que entram no segmento “Provável churn” semana após semana. Isso a ajuda a avaliar a integridade geral do ciclo de vida e a informar a estratégia de retenção em um nível mais amplo. Por fim, ela revisita a página [de análises de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) para sua previsão de rotatividade, a fim de comparar os clientes que abandonaram o serviço previstos com os reais — uma verificação útil para garantir que o modelo esteja funcionando conforme o esperado.

Com base nesses insights, Camila planeja fazer testes A/B com linhas de assunto, testar diferentes janelas de tempo e experimentar formatos de conteúdo, como recomendações em estilo carrossel em uma mensagem no app.

Com a previsão de churn, Intelligent Timing e a personalização baseada em IA, a equipe de Camila não está apenas reagindo ao churn, mas se antecipando a ele. E sua campanha é executada discretamente em segundo plano, alcançando as pessoas certas, no momento certo, com conteúdo que realmente lhes interessa.
