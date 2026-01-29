---
nav_title: Caso de uso
article_title: Caso de uso Prever upgrades de inscrição
description: "Este exemplo mostra como uma marca fictícia usa o Braze Predictive Events para definir os resultados que importam para seus negócios - como fazer upgrade para uma associação profissional - e criar estratégias direcionadas que melhoram os resultados."
page_type: tutorial
---

# Caso de uso: Prever upgrades de inscrição com direcionamento mais inteligente

> Este exemplo mostra como uma marca fictícia usa o Braze Predictive Events para definir os resultados que importam para seus negócios - como fazer upgrade para uma associação profissional - e criar estratégias direcionadas que melhoram os resultados. 

Digamos que Jordan seja um estrategista de ciclo de vida na Steppington, um app de integridade e condicionamento físico com níveis gratuitos e pagos. A equipe de Jordan tem o objetivo de aumentar os upgrades do plano Pro sem bombardear toda a base de usuários gratuitos com envios de mensagens de desconto. Atualmente, eles enviam uma promoção "Try Pro for 50% off" para todos os usuários de nível gratuito após sete dias. Embora isso gere algumas conversões (cerca de 5% em 7 dias), também resulta em alcance excessivo - incluindo desconto para usuários que provavelmente fariam upgrade de qualquer forma.

Para melhorar o direcionamento e reduzir a fadiga do envio de mensagens, Jordan usa o Predictive Events para modelar a probabilidade de um usuário fazer upgrade para o Pro nos próximos 7 dias. Ele define um evento personalizado: `upgraded_to_pro` e usa isso para treinar um modelo de previsão e segmentar os usuários em grupos inteligentes e orientados para a ação. 

Este tutorial explica como Jordan criou:

- Um modelo de previsão para `upgraded_to_pro` em 7 dias
- Segmentos de mensagens que ajudam a aumentar as conversões e, ao mesmo tempo, enviam menos mensagens no total

## Etapa 1: Criar um modelo de previsão de upgrades

Jordan começa definindo o resultado mais importante para sua estratégia de fazer upgrade: um usuário que passa da camada gratuita para a Pro. Em vez de confiar em disparadores genéricos, como "tempo desde a inscrição", ele quer prever quais usuários têm probabilidade real de conversão. Dessa forma, sua equipe pode agir com base em sinais reais, e não apenas em suposições.

1. No dashboard do Braze, Jordan vai para **Analytics** > Predictive Events ( **Análises** de dados > Eventos preditivos).
2. Ele [cria uma nova previsão de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) e a nomeia como "Upgrade para Pro em 7 dias"
3. Como evento de direcionamento, ele seleciona seu evento personalizado: `upgraded_to_pro`.
4. Jordan define a janela de previsão para 7 dias, define uma programação de atualização e cria a previsão.

![Configurações de previsão mostrando a definição, a janela, o público e o cronograma de atualização da previsão.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Etapa 2: Segmentar usuários com base na probabilidade de fazer upgrade

Após a conclusão do treinamento, o Braze atribui um [Event Likelihood Score]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) a cada usuário elegível. Jordan usa essa pontuação para criar segmentos acionáveis - um para usuários de alta intenção que talvez não precisem de um desconto e outro para usuários que provavelmente não se converterão sem suporte.

1. Jordan navega até Segmentos no Braze.
2. Ele cria dois [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) usando o [filtro Event Likelihood Score]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) e seleciona a previsão que criou. Os dois segmentos são:
  - **É provável que faça upgrade:** Pontuação superior a 70
  - **Precisa de um empurrãozinho para fazer upgrade:** Pontuação maior que 40 e menor que 70

{% alert tip %}
Os filtros de previsão podem ser combinados com quaisquer outras atribuições ou comportamentos do usuário. Jordan planeja refinar ainda mais esses segmentos com base nos interesses dos usuários, como priorizar os usuários que usam frequentemente os recursos de rastreamento de condicionamento físico. Isso lhe dá quatro subgrupos para direcionamento mais preciso, permitindo que o conteúdo e o envio de mensagens correspondam às necessidades de cada usuário.
{% endalert %}

![Criador de segmentos com dois filtros para Event Likelihood Score.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Etapa 3: Personalize o envio de mensagens por nível de intenção

Agora que Jordan tem sinais claros de intenção de fazer upgrade - e subgrupos refinados com base no comportamento do usuário - ele cria uma estratégia de envio de mensagens que se adapta às necessidades de cada usuário. Não há mais blasts de tamanho único.

Ele escolhe o e-mail como o principal canal para essa campanha. Por quê? Porque Jordan quer explicar o valor do Pro para os usuários de alta intenção e apresentar um caso convincente para os usuários mais hesitantes, o que exige espaço, recursos visuais e uma CTA forte. O envio de e-mail oferece a flexibilidade de fazer isso bem, sem pressionar os usuários, e permite rastrear o desempenho por meio do comportamento dos cliques.

Jordan [cria um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) que divide a experiência com base nos segmentos que ele acabou de criar. Ele adiciona uma etapa de Jornada do Público ao direcionamento:

- Usuários com alta intenção e foco em condicionamento físico
- Alta intenção, outros usuários
- Usuários de baixa intenção e focados em condicionamento físico
- Baixa intenção, outros usuários

![Jornada do público do Canva com quatro jornadas para cada tipo de intenção.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Ele também define o evento de conversão do Canvas como o evento personalizado `upgraded_to_pro`, para que o Braze rastreie as conversões de upgrade automaticamente à medida que os usuários progridem no fluxo.

### Exemplo de mensagens por jornada

{% tabs %}
{% tab High intent, fitness %}

Esses usuários já são ativos e estão muito engajados com os recursos de rastreamento de condicionamento físico. É provável que eles façam upgrade sem incentivos extras, portanto, a mensagem se concentra em desbloquear insights mais profundos e ferramentas avançadas que se baseiam em seus hábitos existentes.

- **Linha de assunto:** Acesse suas metas de condicionamento físico
- **Cabeçalho:** Seu progresso merece Pro
- **Corpo:** Você já construiu uma rotina sólida. Com o Pro, você pode ir mais fundo - rastrear o progresso em todos os grupos musculares, definir metas de performance semanais e desbloquear análises de dados avançadas adaptadas à forma como você se movimenta.
- **CTA:** Inicie sua avaliação gratuita do Pro

{% endtab %}
{% tab High intent, other %}
Esses usuários mostram fortes sinais de engajamento - como navegação nos recursos do Pro ou atividade frequente no app - mas não estão especificamente focados no rastreamento de condicionamento físico. A mensagem destaca os benefícios mais amplos do Pro, como treinamento e personalização, para incentivá-los a ultrapassar a linha.

- **Linha de assunto:** Você está quase lá - o Pro está pronto quando você estiver
- **Cabeçalho:** Desbloqueie mais maneiras de se movimentar
- **Corpo:** Você está explorando o que o Pro tem a oferecer. Agora é a sua chance de acessar planos personalizados, conteúdo de treinamento individual e programas orientados criados para atender às suas metas exclusivas - seja força, equilíbrio ou manter a consistência.
- **CTA:** Inicie sua avaliação gratuita do Pro

{% endtab %}
{% tab Low intent, fitness %}
Esses usuários se interessam pelos recursos de condicionamento físico, mas não fizeram upgrade. A mensagem se baseia em seus interesses de condicionamento físico e, ao mesmo tempo, reduz o atrito com uma oferta por tempo limitado - ajudando-os a ver o Pro como uma forma de baixo risco para melhorar sua rotina.

- **Linha de assunto:** Pronto para treinar de forma mais inteligente? Experimente o Pro com 50% de desconto
- **Cabeçalho:** Seu upgrade de treino está esperando
- **Corpo:** Pro oferece tudo o que você precisa para começar forte - planos de exercícios fáceis de seguir, dicas de especialistas e rastreamento do progresso real. Experimente agora com 50% de desconto e cancele a qualquer momento.
- **CTA:** Ganhe 50% de desconto no Pro

{% endtab %}
{% tab Low intent, other %}

Esses usuários mostram um engajamento mínimo em geral. É improvável que eles façam upgrade sem um incentivo convincente, portanto, a mensagem adota uma abordagem simples, que prioriza os benefícios, com um desconto e uma linguagem suave para convidar à exploração sem pressão.

- **Linha de assunto:** 50% de desconto no Pro-just para este fim de semana
- **Cabeçalho:** Pronto quando você estiver
- **Corpo:** Crie seu primeiro plano de condicionamento físico personalizado, rastreie seu progresso e acesse exercícios exclusivos - tudo pela metade do preço. Experimente o Pro por menos e cancele a qualquer momento.
- **CTA:** Ganhe 50% de desconto no Pro

{% endtab %}
{% endtabs %}

## Etapa 4: Meça os resultados e otimize sua estratégia

Após a execução da campanha, Jordan analisa a performance no [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para entender o desempenho das jornadas personalizadas e se a combinação da intenção preditiva com sinais comportamentais melhorou as taxas de upgrade.

Performance de e-mail por jornada:

- **Alta intenção, condicionamento físico**
   - *Taxa de abertura:* 34%
   - *Taxa de cliques:* 20%
   - *Taxa de conversão:* 13%
   - Nenhum desconto utilizado
- **Alta intenção, outros**
   - *Taxa de abertura:* 30%
   - *Taxa de cliques:* 17%
   - *Taxa de conversão:* 11%
   - Nenhum desconto utilizado
- **Baixa intenção, condicionamento físico**
   - *Taxa de abertura:* 27%
   - *Taxa de cliques:* 12%
   - *Taxa de conversão:* 8%
   - Oferta de 50% de desconto incluída
- **Baixa intenção, outros**
   - *Taxa de abertura:* 23%
   - *Taxa de cliques:* 9%
   - *Taxa de conversão:* 6%
   - Oferta de 50% de desconto incluída

Em comparação com a campanha anterior de tamanho único da equipe (em que um desconto geral após 7 dias levou a apenas 5% de conversões e ao envio excessivo de mensagens), a abordagem direcionada mostra um aumento significativo em todos os grupos, com maior eficiência e menos descontos desnecessários.

O [relatório do funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) também mostra uma clara redução no abandono das etapas principais, especialmente para usuários de baixa intenção que receberam envio de mensagens personalizadas. Mais usuários estão abrindo, clicando e fazendo upgrade - o que comprova o valor do direcionamento baseado em intenção.

Jordan usa esses insights para:

- Explorar Testes A/B em linhas de assunto e frases de CTA
- Reavaliar o limite de desconto para usuários de intenção intermediária
- Continue refinando os segmentos com base em comportamentos adicionais, como visualizações de conteúdo ou uso de recursos do app

Com o Predictive Events e a segmentação em camadas, sua equipe agora tem uma estratégia dimensionável que adapta o envio de mensagens com base na intenção e no comportamento do usuário, gerando mais upgrades e preservando a confiança na marca.
