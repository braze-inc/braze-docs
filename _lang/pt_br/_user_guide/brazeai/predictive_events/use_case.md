---
nav_title: Caso de uso
article_title: Caso de uso Prever upgrades de assinatura
description: "Este exemplo mostra como uma marca fictícia usa o Braze Predictive Events para definir os resultados que importam para seus negócios - como o upgrade para uma associação profissional - e criar estratégias direcionadas que melhoram os resultados."
page_type: tutorial
---

# Caso de uso: Preveja upgrades de assinaturas com um direcionamento mais inteligente

> Este exemplo mostra como uma marca fictícia usa o Braze Predictive Events para definir os resultados que importam para seus negócios - como o upgrade para uma associação profissional - e criar estratégias direcionadas que melhoram os resultados. 

Digamos que Jordan seja um estrategista de ciclo de vida na Steppington, um aplicativo de saúde e condicionamento físico com níveis gratuitos e pagos. A equipe de Jordan tem a meta de aumentar os upgrades do plano Pro sem bombardear toda a base de usuários gratuitos com mensagens de desconto. Atualmente, eles enviam uma promoção "Try Pro for 50% off" para todos os usuários de nível gratuito após sete dias. Embora isso gere algumas conversões (cerca de 5% em 7 dias), também resulta em alcance excessivo, incluindo desconto para usuários que provavelmente fariam upgrade de qualquer maneira.

Para melhorar a segmentação e reduzir a fadiga de mensagens, Jordan usa o Predictive Events para modelar a probabilidade de um usuário fazer upgrade para o Pro nos próximos 7 dias. Ele define um evento personalizado: `upgraded_to_pro` e usa isso para treinar um modelo de previsão e segmentar os usuários em grupos inteligentes e orientados para a ação. 

Este tutorial explica como Jordan criou:

- Um modelo preditivo para `upgraded_to_pro` em 7 dias
- Segmentos que ajudam a aumentar as conversões, enviando menos mensagens no total

## Etapa 1: Criar um modelo preditivo para upgrades

Jordan começa definindo o resultado mais importante para sua estratégia de upgrade: um usuário que passa do nível gratuito para o Pro. Em vez de confiar em acionadores genéricos, como "tempo desde a inscrição", ele quer prever quais usuários têm probabilidade real de conversão. Dessa forma, sua equipe pode agir com base em sinais reais, e não apenas em suposições.

1. No painel do Braze, Jordan vai para **Analytics** > **Predictive Events**.
2. Ele [cria uma nova previsão de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) e a nomeia como "Upgrade to Pro in 7 days"
3. Como evento de destino, ele seleciona seu evento personalizado: `upgraded_to_pro`.
4. Jordan define a janela de previsão para 7 dias, define um cronograma de atualização e cria a previsão.

\![Configurações de previsão que mostram a definição, a janela, o público e o cronograma de atualização da previsão.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Etapa 2: Segmentar usuários com base na probabilidade de upgrade

Após a conclusão do treinamento, o Braze atribui um [Event Likelihood Score]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) a cada usuário qualificado. Jordan usa essa pontuação para criar segmentos acionáveis - um para usuários de alta intenção que talvez não precisem de um desconto e outro para usuários que provavelmente não se converterão sem suporte.

1. Jordan navega até Segmentos no Braze.
2. Ele cria dois [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) usando o [filtro Event Likelihood Score]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) e seleciona a previsão que criou. Os dois segmentos são:
  - **É provável que faça upgrade:** Pontuação superior a 70
  - **Precisa de um empurrãozinho para ser atualizado:** Pontuação maior que 40 e menor que 70

{% alert tip %}
Os filtros preditivos podem ser combinados com quaisquer outros atributos ou comportamentos do usuário. Jordan planeja refinar ainda mais esses segmentos com base nos interesses dos usuários, como priorizar os usuários que usam com frequência os recursos de rastreamento de condicionamento físico. Com isso, ele tem quatro subgrupos para segmentar com mais precisão, permitindo que o conteúdo e as mensagens correspondam às necessidades de cada usuário.
{% endalert %}

Criador de segmentos com dois filtros para Event Likelihood Score.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Etapa 3: Personalize as mensagens por nível de intenção

Agora que Jordan tem sinais claros de intenção de upgrade - e subgrupos refinados com base no comportamento do usuário - ele cria uma estratégia de mensagens que se adapta às necessidades de cada usuário. Não há mais blasts de tamanho único.

Ele escolhe o e-mail como o principal canal para essa campanha. Por quê? Porque Jordan quer explicar o valor do Pro para os usuários de alta intenção e apresentar um caso convincente para os usuários mais hesitantes, o que exige espaço, recursos visuais e uma CTA forte. O e-mail dá a ele a flexibilidade de fazer isso bem, sem pressionar os usuários, e permite que ele acompanhe o desempenho por meio do comportamento dos cliques.

Jordan [cria um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) que divide a experiência com base nos segmentos que ele acabou de criar. Ele adiciona uma etapa de Caminhos do Público ao alvo:

- Usuários com alta intenção e foco em condicionamento físico
- Alta intenção, outros usuários
- Usuários de baixa intenção e focados em condicionamento físico
- Baixa intenção, outros usuários

Caminho do público-alvo do Canvas com quatro caminhos para cada tipo de intenção.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Ele também define o evento de conversão do Canvas para o evento personalizado `upgraded_to_pro`, para que o Braze rastreie automaticamente as conversões de upgrade à medida que os usuários progridem no fluxo.

### Exemplo de mensagens por caminho

{% tabs %}
{% tab High intent, fitness %}

Esses usuários já são ativos e estão muito envolvidos com os recursos de rastreamento de condicionamento físico. É provável que eles façam o upgrade sem incentivos extras, portanto, a mensagem se concentra em desbloquear insights mais profundos e ferramentas avançadas que se baseiam em seus hábitos existentes.

- **Linha de assunto:** Vá mais longe com suas metas de condicionamento físico
- **Cabeçalho:** Seu progresso merece Pro
- **Corpo:** Você já construiu uma rotina sólida. Com o Pro, você pode ir mais fundo - acompanhe o progresso em todos os grupos musculares, defina metas de desempenho semanais e desbloqueie análises avançadas adaptadas à forma como você se movimenta.
- **CTA:** Inicie sua avaliação gratuita do Pro

{% endtab %}
{% tab High intent, other %}
Esses usuários mostram fortes sinais de engajamento - como navegar pelos recursos do Pro ou atividade frequente no aplicativo - mas não estão especificamente focados no monitoramento de condicionamento físico. A mensagem destaca os benefícios mais amplos do Pro, como treinamento e personalização, para incentivá-los a ultrapassar a linha.

- **Linha de assunto:** Você está quase lá - o Pro está pronto quando você estiver
- **Cabeçalho:** Desbloqueie mais maneiras de se movimentar
- **Corpo:** Você está explorando o que o Pro tem a oferecer. Agora é a sua chance de acessar planos personalizados, conteúdo de treinamento individual e programas orientados criados para atender às suas metas exclusivas - seja força, equilíbrio ou manter a consistência.
- **CTA:** Inicie sua avaliação gratuita do Pro

{% endtab %}
{% tab Low intent, fitness %}
Esses usuários experimentam os recursos de condicionamento físico, mas não tomaram medidas para fazer a atualização. A mensagem se baseia em seus interesses de condicionamento físico e, ao mesmo tempo, reduz o atrito com uma oferta por tempo limitado - ajudando-os a ver o Pro como uma forma de baixo risco para melhorar sua rotina.

- **Linha de assunto:** Pronto para treinar de forma mais inteligente? Experimente o Pro com 50% de desconto
- **Cabeçalho:** Sua atualização de treino está esperando
- **Corpo:** Pro oferece tudo o que você precisa para começar forte - planos de exercícios fáceis de seguir, dicas de especialistas e acompanhamento real do progresso. Experimente agora com 50% de desconto e cancele a qualquer momento.
- **CTA:** Ganhe 50% de desconto no Pro

{% endtab %}
{% tab Low intent, other %}

Esses usuários mostram um envolvimento mínimo em geral. É improvável que eles façam o upgrade sem um incentivo convincente, portanto, a mensagem adota uma abordagem simples, que prioriza os benefícios, com um desconto e uma linguagem suave para convidar à exploração sem pressão.

- **Linha de assunto:** 50% de desconto no Pro-just para este fim de semana
- **Cabeçalho:** Pronto quando você estiver
- **Corpo:** Crie seu primeiro plano de condicionamento físico personalizado, acompanhe seu progresso e acesse exercícios exclusivos - tudo pela metade do preço. Experimente o Pro por menos e cancele a qualquer momento.
- **CTA:** Ganhe 50% de desconto no Pro

{% endtab %}
{% endtabs %}

## Etapa 4: Meça os resultados e otimize sua estratégia

Após a execução da campanha, Jordan analisa o desempenho no [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para entender o desempenho dos caminhos personalizados e se a combinação da intenção preditiva com sinais comportamentais melhorou as taxas de upgrade.

Desempenho de e-mail por caminho:

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

Em comparação com a campanha anterior de tamanho único da equipe (em que um desconto geral após 7 dias resultou em apenas 5% de conversões e excesso de mensagens), a abordagem direcionada mostra um aumento significativo em todos os grupos, com maior eficiência e menos descontos desnecessários.

O [relatório do funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) também mostra uma clara redução no abandono das etapas principais, especialmente para usuários de baixa intenção que receberam mensagens personalizadas. Mais usuários estão abrindo, clicando e fazendo upgrades - o que comprova o valor da segmentação baseada em intenção.

Jordan usa essas percepções para:

- Explore testes A/B em linhas de assunto e frases de CTA
- Reavaliar o limite de desconto para usuários de intenção intermediária
- Continue refinando os segmentos com base em comportamentos adicionais, como visualizações de conteúdo ou uso de recursos do aplicativo

Com o Predictive Events e a segmentação em camadas, sua equipe agora tem uma estratégia dimensionável que adapta as mensagens com base na intenção e no comportamento do usuário, gerando mais upgrades e preservando a confiança na marca.
