---
nav_title: Criar agentes
article_title: Criar agentes personalizados
description: "Saiba como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar no envio de mensagens, na tomada de decisões e no gerenciamento de dados."
alias: /creating-agents/
---

# Criar agentes personalizados

> Saiba como criar agentes personalizados, o que preparar antes de começar e como colocá-los em ação no envio de mensagens, na tomada de decisões e no gerenciamento de dados. Para saber mais sobre informações gerais, consulte [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Os Braze Currents estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Pré-requisitos

Antes de começar, você precisará do seguinte:

- Acesso ao **Console do agente** em seu espaço de trabalho. Verifique com seus administradores do Braze se você não vê essa opção.  
- Permissão para criar e editar agentes de IA personalizados. 
- Uma ideia do que você deseja que o agente realize. Os agentes Braze podem suportar as seguintes ações:  
   - **Envio de mensagens:** Gere linhas de assunto, manchetes, textos no produto ou outros conteúdos.  
   - **Tomada de decisões:** Direcione os usuários no Canva com base no comportamento, nas preferências ou em atributos personalizados.  
   - **Gerenciamento de dados:** Calcular valores, enriquecer entradas de catálogo ou atualizar campos de perfil.  

## Como funciona?

Ao criar um agente, você define a sua finalidade e estabelece as diretrizes de como ele deve se comportar. Depois de estar ativo, o agente pode ser implantado no Braze para gerar cópias personalizadas, tomar decisões em tempo real ou atualizar os campos do catálogo. Você pode pausar ou atualizar um agente a qualquer momento no dashboard.

Os casos de uso a seguir mostram algumas maneiras de aproveitar os agentes personalizados.

| Caso de uso | Descrição |
| --- | --- |
| Tratamento do feedback do cliente | Transmita o feedback do usuário a um agente para analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir vantagens. |
| Localização de conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais ou ajuste o tom e a duração para canais específicos de uma região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster" ou encurte as descrições das campanhas de SMS. |
| Resumir comentários ou feedbacks | Resuma o sentimento ou o feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo de texto curto, como "A maioria dos clientes menciona o ótimo ajuste, mas nota a demora no envio". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Criar um agente

Para criar seu agente personalizado:  

1. Acesse **Console do agente** > **Gerenciamento de agentes** no dashboard do Braze.  
2. Selecione **Criar agente**.  
3. Digite um nome e uma descrição para ajudar a sua equipe a entender a finalidade.
4. Escolha o [modelo](#models) que seu agente usará.  

![Interface do console do agente para criar um agente personalizado no Braze. A tela exibe campos para inserir o nome e a descrição do agente e selecionar um modelo.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Dê instruções ao agente. Consulte [as instruções de escrita](#writing-instructions) para obter orientação.
6\. [Teste a](#testing-your-agent) saída [do agente](#testing-your-agent) e ajuste as instruções conforme necessário.
7\. Quando estiver pronto, selecione **Create Agent** para ativar o agente. 

Seu agente agora está pronto para ser usado! Para obter detalhes, consulte [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Modelos

Ao configurar um agente, você pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo alimentado pelo Braze ou trazer sua própria chave de API.

{% alert important %}
Ao usar o modelo **automático** alimentado pelo Braze, otimizamos para modelos cuja capacidade de raciocínio é suficiente para executar tarefas como pesquisa de catálogo e associação de segmentação de usuários. Ao usar outros modelos, recomendamos que você faça testes para confirmar se o modelo funciona bem para o seu caso de uso. Talvez seja necessário ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhes ou etapas para modelos com diferentes velocidades e capacidades.
{% endalert %}

### Opção 1: Use um modelo movido a Braze

Essa é a opção mais simples, sem necessidade de configuração adicional. O Braze fornece acesso direto a modelos de linguagem grandes (LLM). Para usar essa opção, selecione **Auto**, que usa modelos Gemini.

### Opção 2: Traga sua própria chave de API

Com essa opção, você pode conectar sua conta Braze a provedores como OpenAI, Anthropic, AWS Bedrock ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos do token serão cobrados diretamente pelo provedor, não pelo Braze.

{% alert important %}
Recomendamos testar rotineiramente os modelos mais recentes, pois os modelos legados podem ser descontinuados ou obsoletos após alguns meses.
{% endalert %}

Para configurar isso:

1. Acesse **Partner Integrations** > **Technology Partners** e encontre seu provedor.
2. Digite sua chave de API do provedor.
3. Selecione **Salvar**.

Em seguida, você pode retornar ao seu agente e selecionar seu modelo.

{% alert important %}
Quando você usar um LLM fornecido pela Braze, os fornecedores desse modelo estarão agindo como subprocessadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre você e a Braze. Se o usuário optar por trazer sua própria chave de API, o provedor de sua inscrição no LLM será considerado um provedor terceirizado nos termos do contrato entre o usuário e a Braze.  
{% endalert %}

## Instruções de escrita

As instruções são as regras ou diretrizes que você fornece ao agente (prompt do sistema). Eles definem como o agente deve se comportar sempre que for executado. As instruções do sistema podem ter até 25 KB.

Aqui estão algumas práticas recomendadas gerais para você começar a usar as solicitações:

1. Comece com o fim em mente. Primeiro, declare o objetivo.
2. Dê ao modelo uma função ou personagem ("Você é um ...").
3. Defina claramente o contexto e as restrições (público, duração, tom, formato).
4. Solicite a estrutura ("Return JSON/bullet list/table...").
5. Mostre, não conte. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1... Etapa 2...").
7. Incentivar o raciocínio ("Pense em voz alta, depois responda").
8. Pilotar, inspecionar e iterar. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione proteções e instruções de recusa.
10. Medir e documentar o que funciona internamente para reutilização e dimensionamento.

Recomendamos também incluir um padrão como uma resposta genérica se o agente receber uma resposta que não possa ser analisada. Esse tratamento de erros permite que o agente o informe sobre uma variável de resultado desconhecida. Por exemplo, em vez de solicitar ao agente apenas valores de sentimento "positivo" ou "negativo", peça que ele retorne "inseguro" se não puder decidir.

### Aviso simples

Esse prompt de exemplo recebe uma entrada de pesquisa e gera uma análise de sentimento simples:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Solicitação complexa 

Esse prompt de exemplo pega uma entrada de pesquisa de um usuário e a classifica em um único rótulo de sentimento. O resultado pode ser usado para direcionar os usuários por diferentes jornadas do Canva (como feedback positivo versus negativo) ou armazenar o sentimento como um atributo personalizado em seu perfil para direcionamento futuro.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}

Para obter mais detalhes sobre as práticas recomendadas de solicitação, consulte os guias dos seguintes fornecedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Antrópica](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gêmeos](https://support.google.com/a/users/answer/14200040?hl=en)

### Formato de saída

Use o campo **Formato de saída** para organizar e definir a saída do agente estruturando manualmente os campos ou usando JSON. 

- **Campos:** Uma maneira sem código de impor uma saída de agente que você pode usar de forma consistente. 
- **JSON:** Uma abordagem de código para criar um formato de saída preciso, em que você pode aninhar variáveis e objetos no esquema JSON.

#### Campos

Digamos que você queira formatar as respostas a uma simples pesquisa de feedback para determinar a probabilidade de os entrevistados recomendarem o mais novo sabor de sorvete do seu restaurante. Você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor
| --- | --- |
| **likelihood_score** | Número |
| **explicação** | Texto |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Console do agente mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### Esquema JSON

Digamos que você queira coletar feedback do usuário sobre a experiência gastronômica mais recente na sua rede de restaurantes. Você pode selecionar **JSON Schema** como o formato de saída e inserir o seguinte JSON para retornar um objeto de dados que inclui uma variável de sentimento e uma variável de raciocínio.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

Se você tentar usar um agente com uma saída JSON em um catálogo, ele não seguirá seu esquema. Em vez disso, considere usar os [campos de saída definidos](#fields).

{% alert important %}
Atualmente, os formatos de saída não são compatíveis com o Claude IA. Se você estiver usando uma chave Anthropic, recomendamos adicionar manualmente a estrutura ao prompt do agente.
{% endalert %}

## Configurações opcionais

### Diretrizes da marca

É possível selecionar [as diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que seu agente deve seguir em suas respostas. Por exemplo, se quiser que seu agente gere uma cópia de SMS para incentivar os usuários a inscreverem-se em uma academia, poderá usar esse campo para fazer referência à sua diretriz motivacional e em negrito predefinida.

### Catálogos

Escolha catálogos específicos para que um agente faça referência e forneça ao seu agente o contexto necessário para entender seus produtos e outros dados de usuários, quando relevante.

![O catálogo "restaurants" e a coluna "Loyalty_Program" selecionados para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### Contexto de associação de segmento

É possível selecionar até três segmentos para o agente fazer referência cruzada da associação de segmento de cada usuário quando o agente for usado em uma tela. Digamos que seu agente tenha a associação de segmento selecionada para um segmento "Usuários de fidelidade" e que o agente seja usado em uma tela. Quando os usuários entram em uma etapa do agente, o agente pode fazer referência cruzada se cada usuário é membro de cada segmento especificado no console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O segmento "Usuários de fidelidade" selecionado para acesso de associação de agentes.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### Temperatura

Se o seu objetivo é usar um agente para gerar uma cópia para incentivar os usuários a registrar seu app móvel, você pode definir uma temperatura mais alta para que o agente seja mais criativo e use as nuances das variáveis de contexto. Se você estiver usando um agente para gerar pontuações de sentimento, pode ser ideal definir uma temperatura mais baixa para evitar qualquer especulação do agente sobre respostas negativas à pesquisa. Recomendamos testar essa configuração e revisar a saída gerada pelo agente para adequá-la ao seu cenário.

{% alert note %}
No momento, as temperaturas não são suportadas para uso com o OpenAI.
{% endalert %}

## Teste seu agente

O painel de **prévia ao vivo** é uma instância do agente que aparece como um painel lado a lado na experiência de configuração. Você pode usá-lo para testar o agente enquanto cria ou atualiza o agente para experimentá-lo de forma semelhante à dos usuários finais. Essa etapa ajuda a confirmar se o comportamento é o esperado e lhe dá a chance de fazer ajustes finos antes de acessar o site.

![Console do agente mostrando o painel de prévia ao vivo para testar um agente personalizado. A interface exibe um campo de entradas de amostra com dados de cliente de exemplo, um botão Executar teste e uma área de resposta em que a saída do agente é exibida.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. No campo **Sample inputs (Entradas de amostra)**, insira exemplos de dados de clientes ou respostas de clientes - qualquer coisa que reflita cenários reais com os quais seu agente lidará. 
2. Selecione **Executar teste**. O agente será executado com base em sua configuração e exibirá sua resposta. As execuções de teste contam para seu limite diário de execução.

Analise o resultado com um olhar crítico. Considere as seguintes perguntas:

- O texto está de acordo com a marca? 
- A lógica da decisão encaminha os clientes como pretendido? 
- Os valores calculados são precisos? 

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta aos cenários, especialmente em casos extremos, como ausência de dados ou respostas inválidas.

### Monitore seu agente

Na guia **Registros** do seu agente, é possível monitorar as chamadas de agente reais que ocorrem em suas telas e catálogos. Você pode filtrar por informações como o intervalo de datas, o resultado (sucesso ou falha) ou o local da chamada.

![Registros de um agente Random Sport Assignment, que incluem quando e onde o agente foi chamado.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

Selecione **Exibir** para uma chamada de agente específica para ver a entrada, a saída e a ID do usuário.

![Registros de um agente City Trends e Recommendation Booking. O painel de detalhes mostra o prompt de entrada, a resposta de saída e uma ID de usuário associada.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
