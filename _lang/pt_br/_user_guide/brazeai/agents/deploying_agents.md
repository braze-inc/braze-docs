---
nav_title: Implantar agentes
article_title: Implantar agentes personalizados
description: "Aprenda como utilizar agentes personalizados no Braze após criá-los."
alias: /deploying-agents/
page_order: 2
---

# Implantar agentes personalizados

> Aprenda como utilizar agentes personalizados em etapas do Canvas ou campos do catálogo após criá-los. Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agentes no Canvas  

Você pode usar agentes como etapas em uma jornada para personalizar mensagens ou guiar decisões em tempo real. Para etapas de configuração detalhadas, consulte [Agent step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Pontuação e qualificação de leads | Use uma etapa de Agente para avaliar leads recebidos em uma escala (por exemplo, 1-10). Roteie usuários com uma pontuação acima de um limite para caminhos de nutrição, enquanto desqualifica leads de baixo ajuste. |
| Personalização dinâmica de mensagens | Faça um agente gerar linhas de assunto, recomendações de produtos ou cópias de mensagens com base em atributos do usuário ou comportamentos recentes. A resposta pode ser inserida diretamente em uma etapa de Mensagem. |
| Tratamento de feedback do cliente | Passe comentários dos clientes para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Roteamento inteligente | Use saídas do agente (booleanas ou numéricas) para dividir usuários em diferentes caminhos do Canvas. Por exemplo, classifique usuários como "em risco" ou "saudáveis" e ajuste a cadência das mensagens de acordo. |
| Interpretação de pesquisa ou resposta | Permita que um agente analise respostas abertas de pesquisas ou campos de texto livre, retornando valores estruturados (por exemplo, categorizando intenção ou necessidade) que direcionam caminhos subsequentes. |
| Raciocínio em múltiplas etapas | Configure um agente para combinar campos de contexto e tomar decisões complexas, como recomendar a próxima melhor ação (e-mail, SMS ou contato humano) com base em múltiplos atributos do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agentes em catálogos  

Você pode aplicar um agente a campos de catálogo para que ele gere ou calcule automaticamente valores para cada linha. O agente também funcionará em novas linhas que forem adicionadas ao catálogo no futuro. 

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Gerar descrições de produtos | Crie automaticamente textos curtos de marketing para novas entradas do catálogo, por exemplo, gerando uma descrição atraente a partir de dados estruturados do produto, como nome, categoria e características. |
| Enriquecer atributos de produtos | Preencha valores ausentes, como família de cores, estilo ou estação, com base no nome e detalhes do produto. Por exemplo, se o nome do produto for “Óculos de sol Laguna Polarized”, o agente poderia atribuir o estilo como “esportivo” e a família de cores como “azul”. |
| Calcular campos derivados | Use campos existentes para gerar novos dados, como um “índice de ajuste” com base em atributos ou uma “tag de popularidade” a partir de contagens de vendas e avaliações. |
| Categorizar ou etiquetar itens | Atribua tags para lógica de recomendação para que modelos de personalização possam segmentar produtos de forma mais eficaz. Por exemplo, etiquete produtos como “ao ar livre”, “pronto para festivais” ou “premium”. |
| Localizar conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais, ou ajuste o tom e o comprimento para canais específicos da região. Por exemplo, traduza “Óculos de sol Classic Clubmaster” para o espanhol como “Gafas de sol Classic Clubmaster”, ou encurte descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resumir sentimentos ou feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo curto como “A maioria dos clientes menciona um ótimo ajuste, mas nota o envio lento.” |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapas

![Uma etapa de Agente em um campo de catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para adicionar um agente ao seu campo de catálogo:

1. No seu catálogo, adicione um novo campo.  
2. Selecione **Aplicar agente IA**.
3. Atribuir um agente a este campo.  
4. Selecione quais colunas devem ser passadas como entrada. Se nenhuma for selecionada, o agente terá acesso a todas as colunas no catálogo.  
5. Decida se o agente deve recalcular os campos quando as linhas do catálogo forem atualizadas. Se você não selecionar esta opção, o agente será executado apenas uma vez por linha.
6. Selecione **Adicionar campos** para implantar o agente e revisar as estimativas de custo. O modal de **Estimativa de custo** mostra quantas vezes o agente será executado neste catálogo, aproximadamente igual ao número total de linhas. Para continuar, selecione **Confirmar**.

### Como os agentes de catálogo funcionam  

Após o lançamento, o agente executa e avalia cada linha, levando as colunas selecionadas em seu contexto para produzir uma saída. Os agentes são executados em todas as novas linhas adicionadas após você implantar o agente. Se você selecionou **Recalcular quando as linhas do catálogo forem atualizadas**, todos os valores para este campo serão atualizados se os campos de origem existentes mudarem.

Você pode atualizar e editar os campos em seu catálogo que usam agentes. Para remover um agente de uma coluna, desmarque **Aplicar agente IA**. Isso reverte a coluna para uma coluna não agente, e os campos mantêm os últimos valores que o agente aplicou na última vez que foi executado no catálogo.

Referências circulares em catálogos não são suportadas, o que significa que o seguinte cenário não pode ocorrer:

- A Coluna Agente 1 usa a Coluna Agente 2 como entrada
- A Coluna Agente 2 usa a Coluna Agente 1 como entrada

![A opção de selecionar "Aplicar agente IA" para um campo de catálogo.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Agentes de catálogo estão limitados a processar valores de entrada de até 25 KB por linha.
{% endalert %}

#### Defina campos de resposta

Se o seu agente usar [fields]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) como o formato de saída, você pode selecionar o campo correspondente do agente para **Campo de Resposta** para usar no campo do catálogo. 

Vamos supor que você tenha um agente que adiciona descrições de produtos a um catálogo com os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **descrição** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode adicionar um campo chamado **product_description** a um catálogo e selecionar **descrição** como o **Campo de Resposta** para preencher a coluna com as descrições do agente.

![Um campo "product_description" com o agente "Descriptor" aplicado. A saída "descrição" é selecionada como o campo de resposta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Você também pode substituir manualmente a célula gerada pelo agente selecionando **Editar Item** e atualizando a descrição gerada pelo agente com suas edições. Para reverter à descrição gerada pelo agente, selecione o símbolo de atualizar na célula.

### Tratamento de erros em catálogos  

- Invocações de catálogo com falha não são tentadas novamente.
- Se a chamada da API para o provedor do modelo fundamental retornar qualquer erro, como um erro de chave de API inválida ou um erro de limite de frequência, o valor do campo não é atualizado.
- Você pode revisar os logs do agente para detalhes sobre execuções com falha.

## Monitore seu agente

Na seção **Uso** do seu agente, você pode referenciar e navegar para onde o agente está sendo usado ativamente em catálogos e canvases.

![Seção de Uso do Agente que mostra dois agentes ativos e um agente inativo para Canvases.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Na seção **Logs** do seu agente, você pode monitorar chamadas reais de agentes que ocorrem em seus Canvases e catálogos. Você pode filtrar por informações como intervalo de datas, resultado (sucesso ou falha) ou local de chamada. Você também pode selecionar **Exportar CSV** para exportar os logs mostrados apenas na página atual.

{% alert tip %}
Você também pode monitorar erros de limite de invocação diária no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).
{% endalert %}

![Logs para um agente de Pontuação de Sentimento de IA.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecione **Ver** para uma chamada de agente específica para ver a entrada, saída e ID do usuário.

![O painel de detalhes para uma Atribuição Aleatória de Esportes de agente que mostra o prompt de entrada, resposta de saída e um ID de usuário associado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Use Currents

Você também pode usar esses eventos Currents para acessar os esquemas de registro do Kafka:

- Eventos de execução de agente
- Eventos de invocação de ferramenta

Consulte o [glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) para mais detalhes.

## Artigos relacionados  

- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)