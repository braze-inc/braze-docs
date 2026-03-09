---
nav_title: Caso de uso
article_title: Use Case Prever Upgrades de Inscrição
description: "Este exemplo mostra como uma marca fictícia usa os Eventos Preditivos da Braze para definir os resultados que importam para seus negócios—como fazer upgrade para uma assinatura pro—e construir estratégias direcionadas que melhoram os resultados."
page_type: tutorial
---

# Caso de uso: Prever upgrades de inscrição com direcionamento mais inteligente

> Este exemplo mostra como uma marca fictícia usa os Eventos Preditivos da Braze para definir os resultados que importam para seus negócios—como fazer upgrade para uma assinatura pro—e construir estratégias direcionadas que melhoram os resultados. 

Vamos supor que Jordan é um estrategista de ciclo de vida na Steppington, um app de saúde e fitness com níveis gratuito e pago. A equipe de Jordan tem como objetivo aumentar os upgrades do plano Pro sem bombardear toda a sua base de usuários gratuitos com mensagens de desconto. Atualmente, eles enviam uma promoção "Experimente o Pro com 50% de desconto" para cada usuário do nível gratuito após sete dias. Embora isso gere algumas conversões (cerca de 5% em 7 dias), também resulta em um contato excessivo—incluindo descontos para usuários que provavelmente fariam upgrade de qualquer forma.

Para melhorar o direcionamento e reduzir a fadiga de mensagens, Jordan usa Eventos Preditivos para modelar a probabilidade de que um usuário faça upgrade para Pro nos próximos 7 dias. Ele define um evento personalizado: `upgraded_to_pro`, e então usa isso para treinar um modelo de previsão e segmentar usuários em grupos inteligentes e orientados para a ação. 

Este tutorial explica como Jordan criou:

- Um modelo preditivo para `upgraded_to_pro` em 7 dias
- Segmentos que ajudam a aumentar as conversões enquanto enviam menos mensagens no total

## Etapa 1: Criar um modelo preditivo para upgrades

Jordan começa definindo o resultado que mais importa para sua estratégia de upgrade: um usuário passando do nível gratuito para o Pro. Em vez de depender de gatilhos genéricos como "tempo desde a inscrição", ele quer prever quais usuários estão realmente propensos a converter. Dessa forma, sua equipe pode agir com base em sinais reais, não apenas suposições.

1. No dashboard da Braze, Jordan vai para **análise de dados** > **Eventos Preditivos**.
2. Ele [cria uma nova previsão de evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) e a nomeia "Upgrade para Pro em 7 dias"
3. Como evento alvo, ele seleciona seu evento personalizado: `upgraded_to_pro`.
4. Jordan define a janela de previsão para 7 dias, define um cronograma de atualização e cria a previsão.

![Configurações de Previsão mostrando a definição, janela, público e cronograma de atualização para a previsão.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Etapa 2: Segmentar usuários com base na probabilidade de upgrade

Após a conclusão do treinamento, a Braze atribui um [Score de Probabilidade de Evento]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100) a cada usuário elegível. Jordan usa essa pontuação para criar segmentos acionáveis—um para usuários com alta intenção que podem não precisar de desconto, e outro para usuários que provavelmente não converterão sem suporte.

1. Jordan navega até Segmentos na Braze.
2. Ele cria dois [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) usando o [filtro de Score de Probabilidade de Evento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) e seleciona a previsão que ele criou. Os dois segmentos são:
  - **Provável de fazer upgrade:** Pontuação maior que 70
  - **Precisa de um empurrão para fazer upgrade:** Pontuação maior que 40 e menor que 70

{% alert tip %}
Filtros preditivos podem ser combinados com quaisquer outros atributos ou comportamentos do usuário. Jordan planeja refinar ainda mais esses segmentos com base nos interesses dos usuários—como priorizar usuários que usam frequentemente recursos de rastreamento de fitness. Isso lhe dá quatro subgrupos para segmentar de forma mais precisa, permitindo que o conteúdo e o envio de mensagens correspondam às necessidades de cada usuário.
{% endalert %}

![Criador de segmentos com dois filtros para Score de Probabilidade de Evento.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Etapa 3: Personalizar o envio de mensagens por nível de intenção

Agora que Jordan tem sinais claros de intenção de upgrade—e subgrupos refinados com base no comportamento do usuário—ele constrói uma estratégia de envio de mensagens que se adapta ao que cada usuário precisa. Chega de envios em massa que servem para todos.

Ele escolhe e-mail como o canal principal para esta campanha. Por quê? Porque Jordan quer explicar o valor do Pro para usuários com alta intenção e fazer um caso convincente para usuários mais hesitantes—ambos os quais requerem espaço, visuais e um forte CTA. O e-mail dá a ele a flexibilidade de fazer isso bem, sem pressionar os usuários, e permite que ele rastreie a performance através do comportamento de cliques.

Jordan [cria um canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) que divide a experiência com base nos segmentos que ele acabou de construir. Ele adiciona uma etapa de Jornada do Público para segmentar:

- Usuários com alta intenção, focados em fitness
- Usuários com alta intenção, outros
- Usuários com baixa intenção, focados em fitness
- Usuários com baixa intenção, outros

![Jornada do Público do Canvas com quatro caminhos para cada tipo de intenção.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Ele também define o evento de conversão do Canvas para o evento personalizado `upgraded_to_pro`, para que o Braze rastreie automaticamente as conversões de upgrade à medida que os usuários progridem no fluxo.

### Mensagens de exemplo por caminho

{% tabs %}
{% tab High intent, fitness %}

Esses usuários já estão ativos e muito engajados com os recursos de rastreamento de fitness. Eles provavelmente farão upgrade sem incentivos extras, então a mensagem foca em desbloquear insights mais profundos e ferramentas avançadas que se baseiam em seus hábitos existentes.

- **Linha de assunto:** Vá mais longe com seus objetivos de fitness
- **Cabeçalho:** Seu progresso merece Pro
- **Corpo:** Você já construiu uma rotina forte. Com o Pro, você pode ir mais fundo—rastrear o progresso entre grupos musculares, definir metas de performance semanais e desbloquear análises avançadas adaptadas ao seu movimento.
- **CTA:** Comece seu teste gratuito do Pro

{% endtab %}
{% tab High intent, other %}
Esses usuários estão mostrando sinais fortes de engajamento—como navegar por recursos do Pro ou atividade frequente no app—mas não estão especificamente focados no rastreamento de fitness. A mensagem destaca os benefícios mais amplos do Pro, como coaching e personalização, para incentivá-los a ultrapassar a linha.

- **Linha de assunto:** Você está quase lá—o Pro está pronto quando você estiver
- **Cabeçalho:** Desbloqueie mais maneiras de se mover
- **Corpo:** Você tem explorado o que o Pro tem a oferecer. Agora é sua chance de acessar planos personalizados, conteúdo de coaching 1:1 e programas guiados feitos para corresponder aos seus objetivos únicos—seja força, equilíbrio ou manter a consistência.
- **CTA:** Comece seu teste gratuito do Pro

{% endtab %}
{% tab Low intent, fitness %}
Esses usuários experimentam recursos de fitness, mas não deram passos em direção ao upgrade. A mensagem se concentra em seus interesses de fitness enquanto reduz a fricção com uma oferta por tempo limitado—ajudando-os a ver o Pro como uma maneira de baixo risco para melhorar sua rotina.

- **Linha de assunto:** Pronto para treinar de forma mais inteligente? Experimente o Pro com 50% de desconto
- **Cabeçalho:** Seu upgrade de treino está esperando
- **Corpo:** O Pro oferece tudo que você precisa para começar forte—planos de treino fáceis de seguir, dicas de especialistas e rastreamento de progresso real. Experimente agora com 50% de desconto e cancele a qualquer momento.
- **CTA:** Obtenha 50% de desconto no Pro

{% endtab %}
{% tab Low intent, other %}

Esses usuários mostram engajamento mínimo no geral. É improvável que eles façam upgrade sem um incentivo convincente, então a mensagem adota uma abordagem simples, focada nos benefícios, com um desconto e uma linguagem suave para convidar à exploração sem pressão.

- **Linha de assunto:** 50% de desconto no Pro—apenas neste fim de semana
- **Cabeçalho:** Pronto quando você estiver
- **Corpo:** Crie seu primeiro plano de fitness personalizado, rastreie seu progresso e acesse treinos exclusivos—tudo pela metade do preço. Experimente o Pro por menos e cancele a qualquer momento.
- **CTA:** Obtenha 50% de desconto no Pro

{% endtab %}
{% endtabs %}

## Etapa 4: Meça os resultados e otimize sua estratégia

Após a campanha, Jordan revisa a performance na [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para entender como os caminhos personalizados se saíram—e se a combinação de intenção preditiva com sinais comportamentais melhorou as taxas de upgrade.

Performance de e-mail por caminho:

- **Alta intenção, fitness**
   - *Taxa de abertura:* 34%
   - *Taxa de Clique:* 20%
   - *Taxa de conversão:* 13%
   - Nenhum desconto utilizado
- **Alta intenção, outros**
   - *Taxa de abertura:* 30%
   - *Taxa de Clique:* 17%
   - *Taxa de conversão:* 11%
   - Nenhum desconto utilizado
- **Baixa intenção, fitness**
   - *Taxa de abertura:* 27%
   - *Taxa de Clique:* 12%
   - *Taxa de conversão:* 8%
   - Oferta de 50% de desconto incluída
- **Baixa intenção, outros**
   - *Taxa de abertura:* 23%
   - *Taxa de Clique:* 9%
   - *Taxa de conversão:* 6%
   - Oferta de 50% de desconto incluída

Comparado à campanha anterior da equipe, que era uma abordagem única para todos (onde um desconto geral após 7 dias levou a apenas 5% de conversões e excesso de mensagens), a abordagem direcionada mostra um aumento significativo em todos os grupos, com eficiência melhorada e menos descontos desnecessários.

O [relatório de funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) também mostra uma clara redução na desistência em etapas-chave, particularmente para usuários de baixa intenção que receberam mensagens personalizadas. Mais usuários estão abrindo, clicando e fazendo upgrade—provando o valor do direcionamento baseado em intenção.

Jordan usa essas percepções para:

- Explorar testes A/B em linhas de assunto e formulação de CTA
- Reavaliar o limite de desconto para usuários de média intenção
- Continuar refinando segmentos com base em comportamentos adicionais, como visualizações de conteúdo ou uso de recursos do app

Com Eventos Preditivos e segmentação em camadas, sua equipe agora tem uma estratégia escalável que adapta o envio de mensagens com base na intenção e comportamento do usuário—impulsionando mais upgrades enquanto preserva a confiança na marca.
