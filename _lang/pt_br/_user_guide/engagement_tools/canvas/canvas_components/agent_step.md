---
nav_title: Agente
article_title: Etapa do agente
alias: /agent_step/
page_order: 2
page_type: reference
description: "Este artigo de referência cobre como usar a etapa do Agente no Canvas para gerar conteúdo ou tomar decisões inteligentes em tempo real."
tool: Canvas
toc_headers: h2
---

# Etapa do Agente  

> A etapa do Agente permite que você adicione decisões e geração de conteúdo impulsionadas por IA diretamente no seu fluxo de trabalho do Canvas. Para mais informações gerais, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Uma etapa do Agente em uma jornada do usuário no Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Como funciona

Quando um usuário chega a uma etapa do Agente em um Canvas, a Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. O agente então processa a entrada usando seu modelo e instruções, e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu na etapa.

Você pode então usar essa variável de três maneiras principais:

- **Decisões:** Direcione usuários por diferentes jornadas do Canvas com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar um número entre 1 e 10. Você pode usar essa pontuação para decidir se deve continuar enviando mensagens a um usuário ou removê-lo da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente poderia analisar o feedback do cliente e gerar um e-mail de acompanhamento empático que faz referência ao comentário do cliente e sugere uma resolução.
- **Processando dados de usuários:** Analise e padronize seus dados de usuários, depois armazene-os no perfil de usuário ou envie-os usando um webhook. Por exemplo, um agente poderia retornar uma pontuação de sentimento ou atribuição de afinidade de produto. Você pode armazenar esses dados em um perfil de usuário para uso futuro.

## Pré-requisito

As etapas do Agente usam [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) para ingerir contexto relevante e gerar uma variável que pode ser aproveitada no Canvas.

## Criando uma etapa de Agente

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Agente** da barra lateral, ou selecione o botão <i class="fas fa-plus-circle"></i> de mais na parte inferior de uma etapa e selecione **Agente**.  

### Etapa 2: Escolha seu agente  

Selecione o agente que processará os dados nesta etapa. Escolha um agente existente. Para orientações de configuração, veja [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Etapa 3: Defina a saída do seu agente {#define-the-output-variable}

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para fácil acesso. Para definir a variável de saída, dê um nome à variável.

Observe que o tipo de dado da variável de saída é definido a partir do [Console do Agente]({{site.baseurl}}/user_guide/brazeai/agents). As saídas do agente podem ser salvas como strings, números, booleanos ou objetos. Isso as torna flexíveis tanto para personalização de texto quanto para lógica condicional no seu Canvas. Aqui estão alguns usos comuns para cada tipo:

| Tipo de dados | Usos comuns |
| --- | --- |
| String | Personalização de mensagens (linhas de assunto, textos, respostas) |
| Número | Pontuação, limites, roteamento em [Jornadas do Público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Ramificações Sim/Não em [Divisões de Decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objeto | Aproveite um ou mais dos tipos de dados acima com uma única chamada LLM em uma estrutura de dados previsível |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode usar uma variável de saída em todo o Canvas usando a mesma sintaxe de modelo que usaria com uma variável de contexto. Use o filtro de segmento **Variável de Contexto**, ou insira as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para usar uma propriedade específica de uma variável de saída de objeto, use a notação de ponto para acessar essa propriedade usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Etapa do agente para o Escritor de HTML do Corpo com um tipo de dado objeto para a variável "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Etapa 4: Adicione qualquer contexto adicional (opcional)

Você pode decidir incluir valores de contexto adicionais para a etapa do agente referenciar quando for executada. Você pode inserir quaisquer valores de Liquid que normalmente usaria em um Canvas.

{% alert note %}
Observe que o agente já está recebendo automaticamente o contexto configurado na seção **Instruções**. As variáveis Liquid que já foram configuradas lá não precisam ser reinseridas aqui.
{% endalert %}

![A opção de adicionar contexto adicional a uma etapa de Agente usando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Etapa 5: Teste o agente

Após configurar sua etapa de Agente, você pode testar e visualizar a saída desta etapa.

![Visualize a saída do agente como um usuário aleatório.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Tratamento de erros  

- Se o modelo conectado retornar um erro de limite de taxa, a Braze tenta novamente até cinco vezes com retrocesso exponencial.  
- Se o agente falhar por qualquer outro motivo (como um erro de tempo limite ou chave de API inválida), a variável de saída é definida como `null`.
    - Se um agente atingir seu limite diário de invocações, a variável de saída é definida como `null`. 
- Use [valores padrão de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values) para se proteger contra erros. Por exemplo, no modal **Adicionar Personalização**, você pode inserir um valor padrão de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos.
    - As respostas que usam valores em cache ainda contam para o total e as invocações diárias.
- As etapas de Agente podem levar tempo para processar um grande lote de usuários. Se você perceber que há usuários ainda pendentes nesta etapa, verifique seus registros para confirmar que as invocações estão acontecendo.

## Análise de dados  

Consulte as seguintes métricas para acompanhar o desempenho das suas etapas de Agente:  

| Métrica | Descrição |
| --- | --- |
| _Entraram_ | O número de vezes que os usuários entraram na etapa do Agente. |
| _Avançaram para a etapa seguinte_ | O número de usuários que prosseguiram para a próxima etapa no fluxo após passar pela etapa do Agente. |
| _Saíram do Canvas_ | O número de usuários que saíram do Canvas após passar pela etapa do Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### Quando devo usar uma etapa de Agente?

Em geral, recomendamos usar uma etapa de Agente quando você deseja fornecer dados contextuais específicos a um LLM e fazer com que ele atribua de forma agêntica uma variável de contexto do Canvas de maneira inteligente, em uma escala impossível para humanos.

Vamos supor que você esteja enviando uma mensagem personalizada para recomendar um novo sabor de sorvete a um usuário que anteriormente pediu chocolate e morango. Aqui está a diferença entre usar uma etapa de Agente e recomendações de itens de IA:

- **Etapa de Agente:** Usa LLMs para tomar uma decisão qualitativa sobre o que o usuário pode querer com base nas instruções e pontos de dados contextuais fornecidos ao agente. Neste exemplo, uma etapa de Agente pode recomendar um novo sabor com base na possibilidade de o usuário querer experimentar sabores diferentes.
- **Recomendações de itens de IA:** Usa modelos de machine learning para prever os produtos que um usuário tem mais probabilidade de querer com base em eventos passados do usuário, como compras. Neste exemplo, as recomendações de itens de IA sugeririam um sabor (baunilha) com base nos dois pedidos anteriores do usuário (chocolate e morango) e como esses se comparam aos comportamentos de outros usuários no seu espaço de trabalho.

### Como as etapas de Agente usam dados de entrada?

Uma etapa de Agente analisa os dados contextuais que o agente está configurado para usar, bem como qualquer contexto adicional que seja [fornecido ao agente](#step-4-add-any-additional-context-optional).

## Artigos relacionados  

- [Visão geral dos Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)