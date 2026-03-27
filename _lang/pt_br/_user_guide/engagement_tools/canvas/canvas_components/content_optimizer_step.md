---
nav_title: Otimizador de conteúdo
article_title: Etapa do agente de Otimizador de Conteúdo 
alias: "/content_optimizer_step/"
page_order: 5
description: "A etapa do agente de Otimizador de Conteúdo permite que você configure e teste várias versões de componentes de conteúdo dentro de uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente as combinações de melhor desempenho ao longo do tempo."
page_type: reference

---

# Etapa do agente de Otimizador de Conteúdo

> A etapa do agente de Otimizador de Conteúdo permite que você configure e teste várias versões de componentes de conteúdo dentro de uma única etapa. Ela ajuda você a experimentar variações de conteúdo e otimiza automaticamente as combinações de melhor desempenho ao longo do tempo. Para uma introdução, veja [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
O Otimizador de Conteúdo está atualmente em beta. Para ajuda para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Criando uma etapa do Otimizador de Conteúdo

Para melhores resultados, use o agente de Otimizador de Conteúdo em canvas onde os usuários entram na etapa gradualmente ao longo do tempo. Se todos os usuários entrarem na etapa de uma vez, o agente não terá tempo para aprender com os resultados iniciais. 

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Otimizador de Conteúdo** da barra lateral, ou selecione o botão <i class="fas fa-plus-circle"></i> de mais na parte inferior de uma etapa e selecione **Otimizador de Conteúdo**.

### Etapa 2: Crie sua mensagem base

A mensagem base é o ponto de partida para sua etapa. As variantes para cada componente de conteúdo são inseridas dinamicamente com base nas combinações definidas na guia **Configurações do Otimizador de Conteúdo**. 

{% alert note %}
Durante o período beta, o e-mail é o único canal suportado. 
{% endalert %}

Na guia **Canais de Mensagens**, selecione **E-mail** e crie sua mensagem base de e-mail. Consulte nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email) para ajuda. 

O agente de Otimizador de Conteúdo usa as configurações de envio (como o domínio de e-mail e o endereço de resposta) especificadas nesta variante para enviar todas as mensagens. Você pode começar com um novo design ou selecionar um modelo existente para esta mensagem. Nesta etapa, considere quais componentes da mensagem você deseja otimizar. Você definirá isso na [etapa 4](#step-4).

Os componentes suportados para otimização incluem:

- Assunto
- Cabeçalho do corpo
- Conteúdo do corpo
- CTA principal

### Etapa 3: Especifique as configurações de entrega

Na guia **Configurações de Entrega**, você pode especificar se a etapa deve usar Intelligent Timing ou validações de entrega. Para mais detalhes, consulte [Editar configurações de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) na etapa de Mensagem.

### Etapa 4: Adicione componentes de conteúdo e variantes {#step-4}

Os componentes de conteúdo são os elementos individuais da sua mensagem que você deseja testar, como diferentes linhas de assunto, títulos, texto do corpo ou chamadas à ação principais. Esses componentes permitem que você gere várias versões de uma mensagem e otimize automaticamente com base no desempenho ao longo do tempo.

Você pode adicionar até três componentes de conteúdo por etapa e até cinco variantes por componente, totalizando 125 combinações únicas de conteúdo.

![Opções para adicionar e configurar componentes de conteúdo na interface do Otimizador de Conteúdo. A interface exibe componentes selecionáveis, como Assunto, Cabeçalho do Corpo, Conteúdo do Corpo e CTA Principal, cada um com campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Etapa 4.1: Configurar componentes de conteúdo

Para configurar componentes:

1. Acesse a guia **Configurações do Otimizador de Conteúdo**.
2. Escolha quais componentes você deseja otimizar. Opções suportadas:
  - Assunto
  - Cabeçalho do corpo
  - Conteúdo do corpo
  - CTA principal
3. Para cada componente selecionado, defina um conjunto de versões alternativas desse conteúdo (variantes). Use variantes claras e distintas que diferem em tom, estrutura ou conteúdo. Isso ajuda o Otimizador de Conteúdo a identificar os melhores desempenhos de forma mais eficaz. Você pode:
  - Escrever suas próprias variantes manualmente.
  - Usar sugestões geradas por IA para explorar novas opções rapidamente.

![Interface de Configurações do Otimizador de Conteúdo mostrando opções para adicionar e configurar componentes de conteúdo para otimização de e-mail. Cada componente tem campos de entrada para inserir diferentes variantes. O texto visível inclui nomes de componentes e campos para inserir o texto da variante.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Etapa 4.2: Adicione Liquid à sua mensagem

Após definir pelo menos duas variantes para cada componente, copie a Liquid tag associada a cada um e cole-a no local correspondente na sua mensagem base.

- Por exemplo, se você estiver otimizando a linha de assunto, cole a tag {% raw %}`{% message_component "Subject" %}`{% endraw %} no campo de assunto do criador de e-mail.
- Você também pode incluir tags de componentes dentro de textos mais longos para testar apenas uma parte do componente. Por exemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opções para adicionar e configurar componentes de conteúdo como Assunto, Cabeçalho do Corpo, Conteúdo do Corpo e CTA Principal. Cada componente tem campos para inserir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Se você não adicionar uma Liquid tag para um componente de conteúdo selecionado, verá um aviso na guia **Configurações do Otimizador de Conteúdo** e um erro na guia **Canais de Mensagens**. O Canvas não pode ser lançado até que todos os componentes selecionados sejam adicionados corretamente à sua mensagem base.

À medida que o Canvas é executado, o agente mistura e combina variantes entre componentes para gerar diferentes combinações de conteúdo. Com o tempo, combinações de melhor desempenho são priorizadas para entrega, ajudando você a melhorar a performance sem intervenção manual.

#### Referência Liquid

| Componente | Snippet Liquid |
| --- | --- | 
| Assunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Cabeçalho do corpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Conteúdo do corpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 5: Selecione o evento de otimização

O evento de otimização determina como o agente do Otimizador de Conteúdo avalia o desempenho e aloca tráfego para combinações de conteúdo ao longo do tempo. 

Para e-mail, você pode otimizar para um dos seguintes eventos. O agente usa aberturas e cliques registrados dentro de 7 dias após o envio de uma mensagem para direcionar a entrega para combinações de conteúdo de melhor desempenho.

| Evento | Descrição | Casos de uso |
| --- | --- | --- |
| Aberturas | Otimiza para combinações que fazem os destinatários abrirem o e-mail. | Testando linhas de assunto ou visando aumentar a visibilidade |
| Cliques | Otimiza para combinações que impulsionam o engajamento com links. Não inclui cliques de bots ou cliques de cancelamento de inscrição reconhecidos pela Braze. | Gerando tráfego, engajamento ou conversão a partir de links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O evento de otimização selecionado se aplica a todos os componentes de conteúdo nesta etapa. 

## Práticas recomendadas

- De modo geral, recomendamos testar mais de um componente na etapa do Otimizador de Conteúdo.
- Se você estiver otimizando para cliques, inclua linhas de assunto nos seus testes, pois linhas de assunto mais fortes podem contribuir para mais aberturas e criar mais oportunidades de cliques.
- Se você estiver otimizando para aberturas, mantenha seus testes focados na linha de assunto.

## Análise de dados

Para revisar o desempenho, abra o painel de análise de dados no nível da etapa para ver métricas por variante de conteúdo e desempenho geral da combinação. A etapa do Otimizador de Conteúdo usa a [mesma análise de dados que a etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Análise de dados do Otimizador de Conteúdo para três botões e a porcentagem de alocação de envios, que tende a aumentar.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Solução de problemas

| Problema | Descrição | Correção |
| --- | --- | --- |
| Liquid tags ausentes | Se você adicionar um componente de conteúdo (como Assunto ou CTA) mas não inserir a Liquid tag correspondente na sua mensagem base, você verá: <br>- Um aviso na guia **Configurações do Otimizador de Conteúdo** <br>- Um erro na guia **Canais de Mensagens** | Copie o snippet Liquid mostrado sob cada componente na guia **Configurações do Otimizador de Conteúdo** e cole-o na parte apropriada da sua mensagem. |
| Liquid tags órfãs | Se você excluir um componente de conteúdo, mas deixar sua Liquid tag na mensagem base, a mensagem pode não ser renderizada como esperado ao ser enviada. | Remova quaisquer tags `message_component` não utilizadas da sua mensagem base antes de lançar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }