---
nav_title: Implantar agentes
article_title: Implantar agentes personalizados
description: "Saiba como colocar agentes personalizados em uso no Braze depois de criá-los."
alias: /deploying-agents/
---

# Implantar agentes personalizados

> Saiba como colocar agentes personalizados para uso nas etapas do Canva ou nos campos do catálogo depois de criá-los. Para obter uma introdução, consulte [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Os Braze Currents estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Uso do agente

Na seção **Agent Usage (Uso do agente** ) do seu agente, é possível fazer referência e navegar para onde o agente está sendo usado ativamente em catálogos e Canvas.

![A seção Agent Usage mostra dois agentes ativos e um agente inativo para Canvas.]( {% image_buster /assets/img/ai_agent/agent_usage.png %} )

## Agentes no Canva  

É possível usar os agentes como etapas de uma jornada para personalizar mensagens ou orientar a tomada de decisões em tempo real. Para obter etapas detalhadas de configuração, consulte [Etapa do agente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Pontuação e qualificação de leads | Use uma etapa do Agent para avaliar os leads recebidos em uma escala (por exemplo, de 1 a 10). Encaminhe os usuários com uma pontuação acima de um limite para jornadas de nutrição, enquanto desqualifica os leads de baixa adequação. |
| Personalização dinâmica de mensagens | Faça com que um agente gere linhas de assunto, recomendações de produtos ou textos de mensagens com base nas atribuições do usuário ou em comportamentos recentes. A resposta pode ser inserida diretamente em uma etapa de mensagens. |
| Tratamento do feedback do cliente | Transmita os comentários dos clientes a um agente para analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir vantagens. |
| Roteamento inteligente | Use as saídas do agente (booleanas ou numéricas) para dividir os usuários em diferentes jornadas do Canva. Por exemplo, classifique os usuários como "em risco" ou "saudáveis" e ajuste a cadência do envio de mensagens de acordo. |
| Interpretação de pesquisas ou respostas | Permita que um agente analise as respostas abertas da pesquisa ou os campos de texto livre, retornando valores estruturados (por exemplo, categorizando a intenção ou a necessidade) que direcionam as jornadas downstream. |
| Raciocínio em várias etapas | Configure um agente para combinar campos de contexto e tomar decisões complexas, como recomendar a próxima melhor ação (envio de e-mail, SMS ou contato humano) com base em várias atribuições do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agentes em catálogos  

Você pode aplicar um agente aos campos do catálogo para que ele gere ou calcule automaticamente os valores de cada linha. O agente também será executado em novas linhas que forem adicionadas ao catálogo no futuro. 

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Gerar descrições de produtos | Crie automaticamente uma cópia curta de marketing para novas entradas de catálogo, por exemplo, gerando uma descrição atraente a partir de dados estruturados do produto, como nome, categoria e recursos. |
| Enriquecer as atribuições do produto | Preencha os valores ausentes, como família de cores, estilo ou estação, com base no nome e nos detalhes de um produto. Por exemplo, se o nome de um produto for "Laguna Polarized Sunglasses", o agente poderá atribuir o estilo como "esporte" e a família de cores como "azul". |
| Calcular campos derivados | Use os campos existentes para gerar novos dados, como uma "pontuação de ajuste" com base em atribuições ou uma "tag de popularidade" a partir de contagens de vendas e avaliações. |
| Categorizar ou tagear itens | Atribuir tags para a lógica de recomendação para que os modelos de personalização possam segmentar os produtos de forma mais eficaz. Por exemplo, tag de produtos como "outdoor", "pronto para festival" ou "premium". |
| Localização de conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais ou ajuste o tom e a duração para canais específicos de uma região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster" ou encurte as descrições das campanhas de SMS. |
| Resumir comentários ou feedbacks | Resuma o sentimento ou o feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo de texto curto, como "A maioria dos clientes menciona o ótimo ajuste, mas nota a demora no envio". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapas

![Uma etapa do agente em um campo do catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para adicionar um agente ao seu campo de catálogo:

1. Em seu catálogo, adicione um novo campo.  
2. Selecione **Aplicar agente IA**.
3. Atribuir um agente a esse campo.  
4. Selecione quais colunas devem ser passadas como entrada. Se nenhuma for selecionada, o agente terá acesso a todas as colunas do catálogo.  
5. Decida se o agente deve recalcular os campos quando as linhas do catálogo forem atualizadas. Se você não selecionar essa opção, o agente será executado apenas uma vez por linha.
6. Selecione **Adicionar campos** para implementar o agente e revisar as estimativas de custo. O modal **Estimativa de custo** mostra quantas vezes o agente será executado nesse catálogo, aproximadamente igual ao número total de linhas. Para continuar, selecione **Confirm (Confirmar**).

### Como os agentes de catálogo são executados  

Após a inicialização, o agente executa e avalia cada linha, considerando as colunas selecionadas em seu contexto para produzir um resultado. Os agentes são executados em todas as novas linhas adicionadas depois que você implanta o agente. Se você selecionou **Recalcular quando as linhas do catálogo forem atualizadas**, todos os valores desse campo serão atualizados se os campos de origem existentes forem alterados.

Você pode atualizar e editar os campos em seu catálogo que usam agentes. Para remover um agente de uma coluna, desmarque **Aplicar agente IA**. Isso reverte a coluna para uma coluna não agêntica, e os campos mantêm os valores mais recentes que o agente aplicou na última vez em que foi executado no catálogo.

Não há suporte para referências circulares em catálogos, o que significa que o cenário a seguir não pode ocorrer:

- A Coluna Agêntica 1 usa a Coluna Agêntica 2 como entrada
- A Coluna Agêntica 2 usa a Coluna Agêntica 1 como entrada

![A opção de selecionar "Apply IA agent" (Aplicar agente IA) para um campo de catálogo.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Durante o período beta, os agentes de catálogo estão limitados ao processamento de valores de entrada de até 25 KB por linha.
{% endalert %}

#### Definir campos de resposta

Se o seu agente usar [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#fields) como formato de saída, você poderá selecionar o campo correspondente do agente para **Campo de resposta** a ser usado no campo do catálogo. 

Digamos que você tenha um agente que adiciona descrições de produtos a um catálogo com os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **descrição** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode adicionar um campo chamado **product_description** a um catálogo e selecionar **descrição** como o **campo de resposta** para preencher a coluna com as descrições do agente.

![Um campo "product_description" com o agente "Descriptor" aplicado. A saída "description" é selecionada como o campo de resposta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Você também pode substituir manualmente a célula gerada pelo agente selecionando **Editar item** e atualizando a descrição gerada pelo agente com suas edições. Para reverter suas edições de volta à descrição gerada pelo agente, selecione o símbolo de atualização na célula.

### Tratamento de erros em catálogos  

- As invocações de catálogo com falha não são repetidas.
- Se a chamada de API para o provedor do modelo básico retornar algum erro, como um erro de chave de API inválida ou um erro de limite de frequência, o valor do campo não será atualizado.
- É possível revisar os registros do agente para obter detalhes sobre execuções com falha.
