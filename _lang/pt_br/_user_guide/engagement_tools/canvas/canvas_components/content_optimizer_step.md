---
nav_title: Otimizador de conteúdo
article_title: Etapa do agente do Content Optimizer 
alias: "/content_optimizer_step/"
page_order: 5
description: "A etapa do agente Content Optimizer permite configurar e testar várias versões de componentes de conteúdo em uma única etapa. Ele o ajuda a experimentar variações de conteúdo e otimiza automaticamente para as combinações de melhor performance ao longo do tempo."
page_type: reference

---

# Etapa do agente do Content Optimizer

> A etapa do agente Content Optimizer permite configurar e testar várias versões de componentes de conteúdo em uma única etapa. Ele o ajuda a experimentar variações de conteúdo e otimiza automaticamente para as combinações de melhor performance ao longo do tempo. Para obter uma introdução, consulte [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
O Content Optimizer está atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Criação de uma etapa do Content Optimizer

Para obter melhores resultados, use o agente Content Optimizer em Canvas em que os usuários entram na etapa gradualmente ao longo do tempo. Se todos os usuários entrarem na etapa de uma só vez, o agente não terá tempo de aprender com os primeiros resultados. 

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Content Optimizer** da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Content Optimizer**.

### Etapa 2: Crie sua mensagem básica

A mensagem base é o ponto de partida para sua etapa. As variantes de cada componente de conteúdo são inseridas dinamicamente com base nas combinações definidas na guia **Content Optimizer Settings (Configurações do otimizador de conteúdo** ). 

{% alert note %}
Durante o período beta, o e-mail é o único canal suportado.
{% endalert %}

Na guia **Canais de envio de mensagens**, selecione **E-mail** e crie sua mensagem de e-mail básica. Consulte nossa seção dedicada a [e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email) para obter ajuda. 

O agente Content Optimizer usa as configurações de envio (como o domínio de e-mail e o endereço de resposta) especificadas nessa variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para essa mensagem. Nessa etapa, considere quais componentes da mensagem você deseja otimizar. Você os definirá na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

### Etapa 3: Especificar configurações de entrega

Na guia **Delivery Settings (Configurações de entrega** ), você pode especificar se a etapa deve usar o Intelligent Timing ou validações de entrega. Para obter mais detalhes, consulte [Editar configurações de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) na etapa Mensagem.

### Etapa 4: Adicionar componentes e variantes de conteúdo {#step-4}

Os componentes de conteúdo são os elementos individuais da sua mensagem que você deseja testar, como diferentes linhas de assunto, títulos, corpo do texto ou chamadas à ação primárias. Esses componentes permitem que você gere várias versões de uma mensagem e otimize automaticamente com base no desempenho ao longo do tempo.

Você pode adicionar até três componentes de conteúdo por etapa e até cinco variantes por componente, para um total de 125 combinações de conteúdo exclusivas.

![Opções para adicionar e configurar componentes de conteúdo na interface do Content Optimizer. A interface exibe componentes selecionáveis, como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal, cada um com campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Etapa 4.1: Configurar componentes de conteúdo

Para configurar componentes:

1. Acesse a guia **Content Optimizer Settings (Configurações do otimizador de conteúdo** ).
2. Escolha quais componentes você deseja otimizar. Opções compatíveis:
  - Assunto
  - Cabeçalho do corpo
  - Conteúdo do corpo
  - CTA principal
3. Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que diferem em tom, estrutura ou conteúdo. Isso ajuda o Content Optimizer a identificar as melhores performances de forma mais eficaz. Você pode:
  - Escreva suas próprias variantes manualmente.
  - Use sugestões geradas por IA para explorar novas opções rapidamente.

![Interface de configurações do Content Optimizer mostrando opções para adicionar e configurar componentes de conteúdo para otimização de e-mail. Cada componente tem campos de entrada para inserir diferentes variantes. O texto visível inclui nomes de componentes e campos para inserir texto de variante.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Etapa 4.2: Adicione Liquid à sua mensagem

Depois de definir pelo menos duas variantes para cada componente, copie a Liquid tag associada a cada um deles e cole-a no local correspondente em sua mensagem básica.

- Por exemplo, se estiver otimizando a linha de assunto, cole a tag {% raw %}`{% message_component "Subject" %}`{% endraw %} no campo de assunto do criador do e-mail.
- Você também pode incluir tags de componente dentro de um texto mais longo para testar apenas uma parte do componente. Por exemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opções para adicionar e configurar componentes de conteúdo, como Assunto, Cabeçalho do corpo, Conteúdo do corpo e CTA principal. Cada componente tem campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Se não adicionar uma Liquid tag para um componente de conteúdo selecionado, você verá um aviso na guia **Content Optimizer Settings (Configurações do otimizador de conteúdo** ) e um erro na guia **Messaging Channels (Canais de envio de mensagens** ). O Canva não poderá ser iniciado até que todos os componentes selecionados sejam devidamente adicionados à sua mensagem base.

À medida que o Canva é executado, o agente mistura e combina variantes entre os componentes para gerar diferentes combinações de conteúdo. Com o tempo, as combinações de melhor desempenho são priorizadas para entrega, ajudando a melhorar a performance sem intervenção manual.

#### Referência Liquid

| Componente | Snippet do Liquid |
| --- | --- | 
| Assunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Cabeçalho do corpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Conteúdo do corpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 5: Selecione o evento de otimização

O evento de otimização determina como o agente Content Optimizer avalia a performance e aloca o tráfego para combinações de conteúdo ao longo do tempo. 

Para envio de e-mail, você pode otimizar para um dos seguintes eventos. O agente usa aberturas e cliques registrados em até 7 dias após o envio de uma mensagem para mudar a entrega para combinações de conteúdo com melhor desempenho.

| Evento | Descrição | Casos de uso |
| --- | --- | --- |
| Aberturas | Otimiza as combinações que levam os destinatários a abrir o e-mail. | Teste de linhas de assunto ou com o objetivo de aumentar a visibilidade |
| Cliques | Otimiza para combinações que impulsionam o engajamento com links. Não inclui cliques de bots ou cliques de cancelamento de inscrição reconhecidos pelo Braze. | Impulsionar o tráfego, o engajamento ou a conversão a partir de links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O evento de otimização selecionado se aplica a todos os componentes de conteúdo nesta etapa. 

## Análise de dados

Para analisar o desempenho, abra o painel de análise de dados em nível de etapa para ver as métricas por variante de conteúdo e o desempenho geral da combinação. A etapa Content Optimizer usa a mesma análise de dados que a etapa Message. Para obter detalhes, consulte [Análise]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics) de dados na etapa de mensagens.  

## Solução de problemas

| Problema | Descrição | Consertar |
| --- | --- | --- |
| Tags Liquid ausentes | Se você adicionar um componente de conteúdo (como Assunto ou CTA), mas não inserir a Liquid tag correspondente em sua mensagem básica, verá: <br>\- Um aviso na guia **Content Optimizer Settings (Configurações do otimizador de conteúdo** ) <br>\- Um erro na guia **Canais de envio de mensagens**  | Copie o snippet do Liquid mostrado sob cada componente na guia **Content Optimizer Settings (Configurações do otimizador de conteúdo** ) e cole-o na parte apropriada de sua mensagem. |
| Tags Liquid órfãs | Se você excluir um componente de conteúdo, mas deixar a tag Liquid dele na mensagem base, a mensagem poderá não ser renderizada conforme o esperado quando for enviada. | Remova todas as tags `message_component` não utilizadas de sua mensagem base antes de lançá-la. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

