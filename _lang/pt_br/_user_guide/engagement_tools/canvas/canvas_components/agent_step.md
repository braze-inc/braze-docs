---
nav_title: Agente
article_title: Etapa do agente
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Este artigo de referência aborda como usar a etapa Agent no Canvas para gerar conteúdo ou tomar decisões inteligentes em tempo real."
tool: Canvas
---

# Etapa do agente  

> A etapa Agent permite que você adicione a tomada de decisões e a geração de conteúdo com tecnologia de IA diretamente ao seu fluxo de trabalho do Canvas. Para obter mais informações gerais, consulte [Agentes do Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

Uma etapa do agente em uma jornada do usuário do Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Como funciona

Quando um usuário chega a uma etapa do agente em um Canvas, o Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. Em seguida, o agente processa a entrada usando seu modelo e instruções e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu na etapa.

Você pode usar essa variável de duas maneiras principais:

- **Tomada de decisões:** Encaminhe os usuários por diferentes caminhos do Canvas com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar um número entre 1 e 10. Você pode usar essa pontuação para decidir se deve continuar enviando mensagens a um usuário ou retirá-lo da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente pode analisar o feedback do cliente e gerar um e-mail de acompanhamento empático que faça referência ao comentário do cliente e sugira uma solução.

## Criação de uma etapa do agente

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Agent** da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Agent**.  

### Etapa 2: Selecione seu agente  

Selecione o agente que processará os dados nesta etapa. Escolha um agente existente ou crie um novo agente diretamente nesta etapa. Para obter orientações de configuração, consulte [Criação de agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Etapa 3: Definir a variável de saída

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para facilitar o acesso. Para definir a variável de saída:

1. Dê um nome à variável.
2. Selecione um tipo de dados. 

As saídas do agente podem ser salvas como cadeias de caracteres, números ou booleanos. Isso os torna flexíveis tanto para a personalização de texto quanto para a lógica condicional em seu Canvas. Aqui estão alguns usos comuns para cada tipo:

| Tipo de dados | Usos comuns |
| --- | --- |
| Cordas | Personalização de mensagens (linhas de assunto, cópia, respostas) |
| Número | Pontuação, limites, roteamento em [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Sim/não há ramificação nas [divisões de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando definida, você pode usar uma variável de saída em todo o Canvas usando a mesma sintaxe de modelo que usaria com uma variável de contexto. Use o filtro de segmento de **variável de contexto** ou modele as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

### Etapa 4: Decidir o contexto a ser fornecido ao agente  

Você deve decidir quais dados o agente deve receber em tempo de execução. As seguintes opções estão disponíveis:  

- **Inclua todo o contexto do Canvas:** Passa todas as variáveis de contexto do Canvas disponíveis (como [as propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) e qualquer outro contexto que tenha sido fornecido por meio das etapas do Context.  
- **Fornecer valores:** Transmita apenas propriedades selecionadas, como o primeiro nome ou a cor favorita de um usuário. Escolha essa opção para dar ao agente acesso apenas aos valores que você atribuir aqui. Para cada **chave**, insira a [tag Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) que define o campo específico do perfil do usuário ou a variável de contexto.  

{% alert note %}
O Braze transmitirá apenas os primeiros 10 KB de conteúdo para o agente. O fornecimento de valores com um valor total de mais de 10 KB resultará em truncamento. Para ajudar a economizar custos, os Braze Agents no Canvas usam caches de curta duração para respostas LLM para entradas idênticas. A inclusão de todo o Canvas Context aumenta a probabilidade de que os resultados em cache não possam ser usados, o que pode aumentar os custos do LLM.
{% endalert %}

## Tratamento de erros  

- Se o modelo conectado retornar um erro de limite de taxa, o Braze tentará novamente até cinco vezes com backoff exponencial.  
- Se o agente falhar por qualquer outro motivo (como uma chave de API inválida), a variável de saída será definida como `null`.  
- As respostas são armazenadas em cache para entradas idênticas a fim de reduzir as invocações repetidas.  

## Análises  

Consulte as métricas a seguir para acompanhar o desempenho das etapas do Agent:  

| Métrico | Descrição |
| --- | --- |
| _Entrou_ | O número de vezes que os usuários entraram na etapa do Agente. |
| _Prosseguiu para a próxima etapa_ | O número de usuários que prosseguiram para a próxima etapa do fluxo depois de passar pela etapa do agente. |
| _Tela de saída_ | O número de usuários que saíram do Canvas depois de passar pela etapa do Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Artigos relacionados  

- [Visão geral dos agentes de brasagem]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Criação de agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Implementação de agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  