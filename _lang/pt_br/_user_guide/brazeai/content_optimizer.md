---
nav_title: Otimizador de conteúdo
article_title: Otimizador de conteúdo
alias: "/content_optimizer/"
description: "O Content Optimizer é um agente que ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo."
page_type: reference
page_order: 3
---

# Otimizador de conteúdo

> O Content Optimizer é um agente que ajuda você a testar e otimizar o conteúdo das mensagens em grande escala, usando IA para gerar e avaliar automaticamente altos volumes de variantes de conteúdo.

{% alert important %}
O Content Optimizer está atualmente em beta e disponível apenas para mensagens de e-mail. Para obter ajuda para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Sobre o Content Optimizer

O Content Optimizer é um agente que funciona em uma etapa do canva. Ele ajuda você a definir os componentes da mensagem a serem testados, gerar variantes usando IA Generativa ou entrada manual, e otimizar automaticamente quais combinações de conteúdo são enviadas aos usuários. Este recurso ajuda você a:

- Otimizar linhas de assunto, cabeçalho do corpo, conteúdo do corpo ou CTA principal para e-mails.
- Melhorar continuamente o desempenho das mensagens sem a configuração manual de testes A/B.
- Testar rapidamente altos volumes de variantes de conteúdo, aproveitando a IA para ideação.
- Descontinuar automaticamente conteúdos com baixo desempenho e escalar os vencedores.

Saiba como criar uma [etapa do Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Casos de uso

### E-mail

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações de linha de assunto | Aumentar a taxa de abertura | Testar tom, urgência, personalização e uso de emojis. |
| Estilos de mensagens de cabeçalho | Aumentar o engajamento | Comparar mensagens emocionais, orientadas a valores e claras no cabeçalho do corpo. | 
| Formato do conteúdo do corpo | Melhore a legibilidade e o engajamento | Teste narrativas em comparação com listas de recursos, marcadores versus parágrafos e comprimento do conteúdo. |
| Tom do texto do CTA & | Aumente as taxas de cliques | Compare frases de CTA focadas em ação, benefícios e em primeira pessoa. |
| Combinações de conteúdo temático | Descubra combinações de alto desempenho | Misture e combine componentes de assunto, corpo e CTA temáticos para encontrar a melhor combinação geral. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Como funciona?

O Content Optimizer usa um algoritmo [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) não contextual para alocar mais envios a variantes de alto desempenho e reduzir a alocação para as de baixo desempenho. Com o tempo, isso resulta em uma melhoria contínua do conteúdo da sua mensagem, com mínima intervenção manual.

O algoritmo de otimização proprietário da Braze é construído especificamente para a natureza combinatória da etapa do Content Optimizer. Dado que cada mensagem é composta por vários componentes, o bandit aprende simultaneamente sobre o desempenho de cada componente (como a linha de assunto, corpo, CTA) e suas interações quando combinados em uma mensagem. Mais concretamente, quando uma determinada combinação é enviada, todas as combinações que compartilham os mesmos componentes se beneficiam dos dados desse envio. Isso permite que o bandit aprenda muito mais rápido com a mesma quantidade de dados, em relação a um algoritmo bandit padrão.

Quando a etapa é lançada pela primeira vez, o Content Optimizer envia variantes aleatoriamente para coletar dados de desempenho iniciais. Após esse período inicial de exploração, o algoritmo começa a direcionar o tráfego para combinações de conteúdo de maior desempenho, reduzindo gradualmente a alocação para opções de baixo desempenho. Durante o período de exploração, o tráfego é geralmente distribuído entre as variantes disponíveis para permitir que o algoritmo aprenda com seu desempenho relativo.

O Content Optimizer é semelhante à etapa de Mensagem no Canvas, com recursos como horários de silêncio, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) e registro de eventos. Você pode configurar uma etapa do Content Optimizer criando uma mensagem base e definindo quais componentes de conteúdo (como linha de assunto, texto do corpo ou chamada para ação) otimizar. Variantes para cada componente podem ser geradas com IA ou inseridas manualmente, e tags Liquid devem ser adicionadas à mensagem base para mapear componentes no conteúdo da mensagem.

Cada usuário recebe uma mensagem por entrada na etapa do Otimizador de Conteúdo. Reentradas são tratadas como novas, sem memória de variantes anteriores.

Para melhores resultados, use o Otimizador de Conteúdo em Canvases onde os usuários entram na etapa gradualmente ao longo do tempo, como em Canvases recorrentes ou sempre ativos com volume diário consistente. Se todos os usuários entrarem na etapa de uma vez, o agente não terá tempo para aprender com os resultados iniciais. A etapa se comportará mais como um teste A/B estático do que como um motor de otimização ao vivo.

Isso significa que você ainda pode usar o Otimizador de Conteúdo em Canvases de envio único ou de curto prazo, mas apenas se os usuários estiverem entrando na etapa ao longo de um período prolongado (por exemplo, através de uma etapa de postergação, entrada agendada ou fluxo acionado por API). Certifique-se de que a etapa tenha tráfego e tempo suficientes para observar diferenças de desempenho antes de alcançar a maioria dos usuários.

### Conceitos-chave

| Prazo                    | Descrição |
|-------------------------|-------------|
| Mensagem de base   | O modelo de mensagem principal do qual as variantes são construídas, incluindo todas as configurações de envio. |
| Componentes de conteúdo  | Elementos dentro de uma mensagem (por exemplo, linha de assunto ou CTA principal) que podem ser testados e otimizados. Os profissionais de marketing devem inserir a tag Liquid relevante na mensagem onde o componente deve aparecer. |
| Variantes de conteúdo    | Os diferentes valores que um componente de conteúdo pode assumir. |
| Combinações de conteúdo| Mensagens únicas criadas pela mistura e combinação de variantes de conteúdo. |
| Evento de otimização       | Determina como o Otimizador de Conteúdo avalia o desempenho e aloca tráfego para combinações de conteúdo ao longo do tempo, como cliques ou aberturas de e-mail. Aplica-se a todos os componentes de conteúdo em uma etapa. O Otimizador de Conteúdo aprende continuamente com este evento e automaticamente redireciona a entrega para combinações de conteúdo de melhor desempenho. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

- O Content Optimizer está atualmente em beta e disponível apenas para mensagens de e-mail.
- O agente pode gerar até 125 combinações por etapa:
   - Até 3 componentes por etapa
   - Até 5 variantes para cada componente
- Apenas uma mensagem é enviada por usuário por entrada. Não há memória de envios anteriores para reentradas.
- Os profissionais de marketing devem inserir manualmente as tags Liquid para cada componente no criador de mensagem onde as variantes do componente de conteúdo definido devem ser exibidas.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos passos

- Entre em contato com seu gerente de sucesso do cliente para participar da versão beta ou para suporte na integração.
- Saiba como criar uma [etapa do Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).
