---
nav_title: Agente
article_title: Etapa do agente
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Este artigo de referência cobre como usar o passo do Agente no Canva para gerar conteúdo ou tomar decisões inteligentes em tempo real."
tool: Canvas
toc_headers: h2
---

# Passo do Agente  

> O passo do Agente permite que você adicione decisões e geração de conteúdo impulsionadas por IA diretamente no seu fluxo de trabalho do Canva. Para mais informações gerais, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Um passo do Agente em uma jornada do usuário no Canva.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Como funciona?

Quando um usuário chega a um passo do Agente em um Canva, o Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. O agente então processa a entrada usando seu modelo e instruções, e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu no passo.

Você pode então usar essa variável de duas maneiras principais:

- **Decisões:** Roteie os usuários por diferentes caminhos do Canva com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar um número entre 1 e 10. Você pode usar essa pontuação para decidir se deve continuar enviando mensagens a um usuário ou removê-lo da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente poderia analisar o feedback do cliente e gerar um e-mail de acompanhamento empático que faz referência ao comentário do cliente e sugere uma resolução.

## Criando um passo do Agente

### Etapa 1: Adicionar um passo

Arraste e solte o componente **Agente** da barra lateral, ou selecione o botão de mais <i class="fas fa-plus-circle"></i> na parte inferior de um passo e selecione **Agente**.  

### Etapa 2: Selecione seu agente  

Selecione o agente que processará os dados nesta etapa. Escolha um agente existente ou crie um novo diretamente deste passo. Para orientações de configuração, veja [Crie agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Etapa 3: Defina a variável de saída

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para fácil acesso. Para definir a variável de saída:

1. Dê um nome à variável.
2. Selecione um tipo de dados. 

As saídas do agente podem ser salvas como strings, números, booleanos ou objetos. Isso as torna flexíveis tanto para personalização de texto quanto para lógica condicional em seu Canva. Aqui estão alguns usos comuns para cada tipo:

| Tipo de dados | Usos comuns |
| --- | --- |
| String | Personalização de mensagens (linhas de assunto, cópias, respostas) |
| Número | Pontuação, limites, roteamento em [Caminhos do Público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Divisões Sim/Não em [Divisões de Decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objeto | Aproveite um ou mais dos tipos de dados acima com uma única chamada LLM em uma estrutura de dados previsível |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando definido, você pode usar uma variável de saída em todo o Canva usando a mesma sintaxe de modelo que você usaria com uma variável de contexto. Use o filtro de segmento **Variável de Contexto**, ou modele as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para usar uma propriedade específica de uma variável de saída de objeto, use a notação de ponto para acessar essa propriedade usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Etapa do agente para o Escritor de HTML do Corpo com um tipo de dado de objeto de saída para a variável "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

Use os padrões de sintaxe Liquid mostrados acima para referenciar campos particulares da saída do agente em etapas futuras do Canva.

### Etapa 4: Decida qual contexto fornecer ao agente  

Você deve decidir quais dados o agente deve receber em tempo de execução. As seguintes opções estão disponíveis:  

- **Incluir todo o contexto do Canvas:** Passe todas as variáveis de contexto do Canvas disponíveis (como [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) para a etapa do Agente. Você pode usar etapas de Contexto a montante das etapas do agente para adicionar mais dados ao Contexto antes dele.
- **Fornecer valores:** Passe apenas propriedades selecionadas, como o primeiro nome ou a cor favorita de um usuário. Escolha esta opção para dar ao agente acesso apenas aos valores que você atribui aqui. Para cada **Chave**, insira a [tag Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) que define o campo de perfil de usuário específico ou variável de contexto.  

{% alert note %}
Braze passa os primeiros 10 KB de conteúdo para o agente. Fornecer valores que tenham um valor total superior a 10 KB resulta em truncamento.
{% endalert %}

### Etapa 5: Teste o agente

Após configurar sua etapa do Agente, você pode testar e visualizar a saída desta etapa.

## Tratamento de erros  

- Se o modelo conectado retornar um erro de limite de frequência, o Braze tenta novamente até cinco vezes com retrocesso exponencial.  
- Se o agente falhar por qualquer outro motivo (como chave de API inválida), a variável de saída é definida como `null`.
    - Se um agente atingir seu limite diário de invocações, a variável de saída é definida como `null`. Se você estiver usando a saída de um agente em uma etapa de Mensagem, considere usar a lógica de abortar Liquid.
- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos.
    - As respostas que usam valores em cache ainda contam para o total e as invocações diárias.

## Análise de dados  

Consulte as seguintes métricas para acompanhar o desempenho das suas etapas do Agente:  

| Métrico | Descrição |
| --- | --- |
| _Entraram_ | O número de vezes que os usuários entraram na etapa do Agente. |
| _Avançaram para a etapa seguinte_ | O número de usuários que prosseguiram para a próxima etapa no fluxo após passar pela etapa do Agente. |
| _Saíram do canva_ | O número de usuários que saíram do Canvas após passar pela etapa do Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### Quando devo usar uma etapa de Agente?

Em geral, recomendamos usar uma etapa de Agente quando você quiser fornecer dados contextuais específicos a um LLM e fazer com que ele atribua variáveis de contexto do Canvas de forma inteligente em uma escala impossível para humanos.

Vamos supor que você esteja enviando uma mensagem personalizada para recomendar um novo sabor de sorvete a um usuário que anteriormente pediu chocolate e morango. Aqui está a diferença entre usar uma etapa de Agente versus recomendações de itens de IA:

- **Etapa de Agente:** Usa LLMs para tomar uma decisão qualitativa sobre o que o usuário pode querer com base nas instruções e pontos de dados contextuais fornecidos ao agente. Neste exemplo, uma etapa de Agente pode recomendar um novo sabor com base na possibilidade de o usuário querer experimentar sabores diferentes.
- **Recomendações de itens de IA:** Usa modelos de aprendizado de máquina para prever os produtos que um usuário é mais provável de querer com base em eventos passados do usuário, como compras. Neste exemplo, as recomendações de itens de IA sugeririam um sabor (baunilha) com base nos dois pedidos anteriores do usuário (chocolate e morango) e como esses se comparam aos comportamentos de outros usuários em seu espaço de trabalho.

### Quando devo usar um formato de saída padrão para um agente?

Recomendamos usar o formato de saída quando você quiser que o agente retorne uma estrutura de dados com múltiplos valores definidos de maneira estruturada, em vez de uma saída de valor único. Isso permite que a saída seja melhor formatada como uma variável de contexto consistente.

Por exemplo, você pode usar um formato de saída dentro de um agente que tem a intenção de criar um itinerário de viagem de amostra para um usuário com base em um formulário que eles enviaram. O formato de saída permite que você defina que cada resposta do agente deve retornar com valores para `tripStartDate`, `tripEndDate` e `destination`. Cada um desses valores pode ser extraído de variáveis de contexto e colocado em uma etapa de Mensagem para personalização usando Liquid.

### Como as etapas de Agente usam dados de entrada?

As etapas de Agente usam dados contextuais específicos que são [fornecidos ao agente](#step-4-decide-what-context-to-provide-the-agent). 

Você pode escolher passar a totalidade do contexto do Canvas para o agente como contexto, ou passar valores específicos usando tags Liquid para o contexto dessa etapa de Agente. Você também pode usar Conteúdo Conectado como um valor de entrada em uma etapa do Agente.

## Artigos relacionados  

- [Visão geral dos Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  