---
nav_title: Otimizador de conteúdo
article_title: Otimizador de conteúdo
alias: "/content_optimizer/"
description: "O Content Optimizer é um agente que o ajuda a testar e otimizar o conteúdo de mensagens em escala, usando IA para gerar e avaliar automaticamente grandes volumes de variantes de conteúdo."
page_type: reference
page_order: 4
---

# Otimizador de conteúdo

> O Content Optimizer é um agente que o ajuda a testar e otimizar o conteúdo de mensagens em escala, usando IA para gerar e avaliar automaticamente grandes volumes de variantes de conteúdo.

{% alert important %}
O Content Optimizer está atualmente na versão beta e só está disponível para envios de e-mail. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Sobre o Content Optimizer

O Content Optimizer é um agente que é executado em uma etapa do Canva. Ele ajuda a definir componentes de mensagens para testar, gerar variantes usando IA generativa ou entrada manual e otimizar automaticamente quais combinações de conteúdo são enviadas aos usuários. Esse recurso ajuda você a:

- Otimize as linhas de assunto, o cabeçalho do corpo, o conteúdo do corpo ou a CTA principal dos e-mails.
- Melhore continuamente a performance das mensagens sem a necessidade de configuração manual de Testes A/B.
- Teste rapidamente grandes volumes de variantes de conteúdo, aproveitando a IA para a ideação.
- Elimine automaticamente o conteúdo de baixo desempenho e amplie os vencedores.

Saiba como criar uma [etapa do Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Casos de uso

### E-mail

| Caso de uso de otimização | Objetivo | Descrição |
| --- | --- | --- |
| Variações da linha de assunto | Aumentar a taxa de abertura | Teste o tom, a urgência, a personalização e o uso de emojis. |
| Estilos de envio de mensagens de cabeçalho | Aumente o engajamento | Compare o envio de mensagens emocionais, orientadas por valores e claras no cabeçalho do corpo. | 
| Formato do conteúdo do corpo | Melhorar a legibilidade e o engajamento | Teste a narrativa versus as listas de recursos, os marcadores versus os parágrafos e o tamanho do conteúdo. |
| Cópia da CTA & tone | Aumentar os cliques | Compare as frases de CTA orientadas para a ação, com foco nos benefícios e em primeira pessoa. |
| Combinações de conteúdo temático | Descubra combinações de alta performance | Misture e combine componentes temáticos de assunto, corpo e CTA para encontrar a melhor combinação geral. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Como funciona?

O Content Optimizer usa um algoritmo de [bandido multiarmas](https://en.wikipedia.org/wiki/Multi-armed_bandit) não contextual para alocar mais envios para variantes de alta performance e reduzir a alocação para variantes de baixa performance. Com o tempo, isso resulta em um aprimoramento contínuo do conteúdo de suas mensagens, com o mínimo de intervenção manual.

Quando a etapa é iniciada pela primeira vez, o Content Optimizer envia variantes aleatoriamente para coletar dados iniciais de performance. Após esse período inicial de exploração, o algoritmo começa a transferir o tráfego para combinações de conteúdo de maior performance, reduzindo gradualmente a alocação para opções de baixa performance. Durante o período de exploração, o tráfego é geralmente distribuído entre as variantes disponíveis para permitir que o algoritmo aprenda com seu desempenho relativo.

O Content Optimizer é semelhante à etapa do Message no Canva, com recursos como horário de silêncio, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) e registro de eventos. Você pode configurar uma etapa do Content Optimizer criando uma mensagem de base e definindo quais componentes de conteúdo (como linha de assunto, corpo do texto ou chamada para ação) devem ser otimizados. As variantes de cada componente podem ser geradas com IA ou inseridas manualmente, e as tags Liquid devem ser adicionadas à mensagem base para mapear os componentes no conteúdo da mensagem.

Cada usuário recebe uma mensagem por entrada na etapa do Content Optimizer. As reentradas são tratadas como novas, sem memória das variantes anteriores.

Para obter os melhores resultados, use o Content Optimizer em Canvases em que os usuários entram na etapa gradualmente ao longo do tempo, como em Canvases recorrentes ou sempre ativos com volume diário consistente. Se todos os usuários entrarem na etapa de uma só vez, o agente não terá tempo de aprender com os primeiros resultados. A etapa se comportará mais como um teste A/B estático do que como um mecanismo de otimização ativo.

Isso significa que ainda é possível usar o Content Optimizer em Canvas de envio único ou de curto prazo, mas somente se os usuários estiverem entrando na etapa durante um período prolongado (por exemplo, por meio de uma etapa de postergação, entrada programada ou fluxo disparado por API). Certifique-se de que a etapa tenha tráfego e tempo suficientes para observar as diferenças de performance antes de atingir a maioria dos usuários.


### Conceitos-chave

| Prazo                    | Descrição |
|-------------------------|-------------|
| Mensagem de base   | O modelo principal de mensagem a partir do qual as variantes são criadas, incluindo todas as configurações de envio. |
| Componentes de conteúdo  | Elementos em uma mensagem (por exemplo, linha de assunto ou CTA principal) que podem ser testados e otimizados. Os profissionais de marketing devem inserir a Liquid tag relevante na mensagem em que o componente deve aparecer. |
| Variantes de conteúdo    | Os diferentes valores que um componente de conteúdo pode assumir. |
| Combinações de conteúdo| Mensagens exclusivas criadas pela mistura e combinação de variantes de conteúdo. |
| Evento de otimização       | Determina como o Content Optimizer avalia a performance e aloca o tráfego para combinações de conteúdo ao longo do tempo, como cliques ou aberturas de e-mail. Aplica-se a todos os componentes de conteúdo em uma etapa. O Content Optimizer aprende continuamente com esse evento e muda automaticamente a entrega para combinações de conteúdo com melhor performance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

- O Content Optimizer está atualmente na versão beta e só está disponível para envios de e-mail.
- O agente pode gerar até 125 combinações por etapa:
   - Até 3 componentes por etapa
   - Até 5 variantes para cada componente
- Apenas uma mensagem é enviada por usuário e por entrada. Não há memória de envios anteriores para reentradas.
- Os profissionais de marketing devem inserir manualmente Liquid tags para cada componente no criador de mensagens, onde as variantes de componentes de conteúdo definidas devem ser renderizadas.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos passos

- Entre em contato com o gerente de sucesso do cliente para participar da versão beta ou para obter suporte à integração.
- Saiba como criar uma [etapa do Content Optimizer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).
