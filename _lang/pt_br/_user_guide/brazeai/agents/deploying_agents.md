---
nav_title: Implementação de agentes
article_title: Implementação de agentes personalizados
description: "Saiba como colocar agentes personalizados em uso no Braze depois de criá-los."
alias: /deploying-agents/
---

# Implementação de agentes personalizados

> Saiba como colocar agentes personalizados para uso nas etapas do Canvas ou nos campos do catálogo depois de criá-los. Para obter uma introdução, consulte [Agentes de brasagem]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Os Agentes Braze estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}  

## Agentes no Canvas  

Você pode usar os agentes como etapas de uma jornada para personalizar mensagens ou orientar a tomada de decisões em tempo real. Para obter etapas detalhadas de configuração, consulte [Etapa do agente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Pontuação e qualificação de leads | Use uma etapa do Agent para avaliar os leads recebidos em uma escala (por exemplo, de 1 a 10). Encaminhe os usuários com uma pontuação acima de um limite para caminhos de nutrição, enquanto desqualifica os leads de baixa adequação. |
| Personalização dinâmica de mensagens | Faça com que um agente gere linhas de assunto, recomendações de produtos ou textos de mensagens com base nos atributos do usuário ou em comportamentos recentes. A resposta pode ser inserida diretamente em uma etapa de Mensagem. |
| Tratamento do feedback do cliente | Transmita os comentários dos clientes a um agente para analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir vantagens. |
| Roteamento inteligente | Use as saídas do agente (booleanas ou numéricas) para dividir os usuários em diferentes caminhos do Canvas. Por exemplo, classifique os usuários como "em risco" ou "saudáveis" e ajuste a cadência das mensagens de acordo. |
| Interpretação de pesquisas ou respostas | Permita que um agente analise as respostas abertas da pesquisa ou os campos de texto livre, retornando valores estruturados (por exemplo, categorizando a intenção ou a necessidade) que direcionam os caminhos de downstream. |
| Raciocínio em várias etapas | Configure um agente para combinar campos de contexto e tomar decisões complexas, como recomendar a próxima melhor ação (e-mail, SMS ou contato humano) com base em vários atributos do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agentes em catálogos  

Você pode aplicar um agente aos campos do catálogo para que ele gere ou calcule automaticamente os valores de cada linha. O agente também será executado em novas linhas que forem adicionadas ao catálogo no futuro. 

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Gerar descrições de produtos | Crie automaticamente uma cópia curta de marketing para novas entradas de catálogo, por exemplo, gerando uma descrição atraente a partir de dados estruturados do produto, como nome, categoria e recursos. |
| Enriquecer os atributos do produto | Preencha os valores ausentes, como família de cores, estilo ou estação, com base no nome e nos detalhes de um produto. Por exemplo, se o nome de um produto for "Laguna Polarized Sunglasses", o agente poderá atribuir o estilo como "esporte" e a família de cores como "azul". |
| Calcular campos derivados | Use os campos existentes para gerar novos dados, como uma "pontuação de ajuste" com base em atributos ou uma "etiqueta de popularidade" a partir de contagens de vendas e avaliações. |
| Categorizar ou marcar itens | Atribua tags para a lógica de recomendação para que os modelos de personalização possam segmentar os produtos com mais eficiência. Por exemplo, marque os produtos como "outdoor", "pronto para festivais" ou "premium". |
| Localize o conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais ou ajuste o tom e a duração para canais específicos de uma região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster" ou encurte as descrições das campanhas de SMS. |
| Resumir comentários ou feedbacks | Resuma o sentimento ou o feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo de texto curto, como "A maioria dos clientes menciona um ótimo ajuste, mas nota um envio lento". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapas

\![Uma etapa do agente em um campo do catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para adicionar um agente ao seu campo de catálogo:

1. Em seu catálogo, adicione um novo campo.  
2. Selecione **Aplicar agente de IA**.
3. Atribua um agente a esse campo.  
4. Selecione quais colunas devem ser passadas como entrada. Se nenhuma for selecionada, o agente terá acesso a todas as colunas do catálogo.  
5. Decida se o agente deve recalcular os campos quando as linhas do catálogo forem atualizadas. Se você não selecionar essa opção, o agente será executado apenas uma vez por linha.
6. Selecione **Adicionar campos** para implementar o agente e revisar as estimativas de custo. O modal **Estimativa de custo** mostra quantas vezes o agente será executado nesse catálogo, aproximadamente igual ao número total de linhas. Para continuar, selecione **Confirm (Confirmar**).

### Como os agentes de catálogo são executados  

Após a inicialização, o agente será executado e avaliará cada linha, considerando as colunas selecionadas em seu contexto para produzir um resultado. Os agentes são executados em todas as novas linhas adicionadas depois que o agente é implantado. Se você selecionou **Recalcular quando as linhas do catálogo forem atualizadas**, todos os valores desse campo serão atualizados se os campos de origem existentes forem alterados.  

{% alert note %}
Durante o período beta, os agentes de catálogo estão limitados ao processamento de valores de entrada de até 10 KB por linha e atualizarão somente as primeiras 10.000 linhas em um catálogo.
{% endalert %}

### Tratamento de erros em catálogos  

- As invocações de catálogo com falha não são repetidas.
- Se a chamada de API para o provedor do modelo básico retornar algum erro, como um erro de chave de API inválida ou um erro de limite de taxa, o valor do campo não será atualizado.   
- É possível revisar os logs do agente para obter detalhes sobre execuções com falha.  
