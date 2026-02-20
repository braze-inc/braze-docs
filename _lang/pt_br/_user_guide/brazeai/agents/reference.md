---
nav_title: Referência
article_title: Referência de agentes
description: "Consulte os principais detalhes sobre os agentes de brasagem."
page_order: 3
---

# Referência de agentes

> Ao criar agentes personalizados, consulte este artigo para obter mais informações sobre as principais configurações, como instruções e esquemas de saída. Para obter uma introdução, consulte [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

{% alert important %}
Os Braze Currents estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Modelos

Ao configurar um agente, você pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo alimentado pelo Braze ou trazer sua própria chave de API.

{% alert important %}
O modelo **automático** alimentado pelo Braze é otimizado para modelos cujas capacidades de raciocínio são suficientes para executar tarefas como pesquisa de catálogo e associação de segmentação de usuários. Ao usar outros modelos, recomendamos que você faça testes para confirmar se o modelo funciona bem para o seu caso de uso. Talvez seja necessário ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhes ou etapas para modelos com diferentes velocidades e capacidades.
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

Instruções são as regras ou diretrizes que você fornece ao agente (prompt do sistema). Eles definem como o agente deve se comportar sempre que for executado. As instruções do sistema podem ter até 25 KB.

Aqui estão algumas práticas recomendadas gerais para você começar a usar os avisos:

1. Comece com o fim em mente. Primeiro, declare o objetivo.
2. Dê ao modelo uma função ou personagem ("Você é um ...").
3. Defina claramente o contexto e as restrições (público, duração, tom, formato).
4. Solicite a estrutura ("Return JSON/bullet list/table...").
5. Mostre, não conte. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1... Etapa 2...").
7. Incentive o raciocínio ("Pense nas etapas internamente e, em seguida, forneça uma resposta final concisa" ou "explique brevemente sua decisão").
8. Pilotar, inspecionar e iterar. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione proteções e instruções de recusa.
10. Medir e documentar o que funciona internamente para reutilização e dimensionamento.

Recomendamos também incluir um padrão como uma resposta genérica se o agente receber uma resposta que não possa ser analisada. Esse tratamento de erros permite que o agente o informe sobre uma variável de resultado desconhecida. Por exemplo, em vez de solicitar ao agente apenas valores de sentimento "positivo" ou "negativo", peça que ele retorne "inseguro" se não puder decidir.

### Aviso simples

Esse prompt de exemplo recebe uma entrada de pesquisa e gera uma análise de sentimento simples:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Prompt complexo 

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

### Usando Liquid

Incluir o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) nas instruções de seu agente pode adicionar uma camada extra de personalização à resposta. Você pode especificar a variável Liquid exata que o agente recebe e pode incluí-la no contexto de seu prompt. Por exemplo, em vez de escrever explicitamente "first name" (nome), você pode usar o snippet Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Na seção **Registros** do **Console do agente**, é possível revisar os detalhes da entrada e saída do agente para entender qual valor é renderizado a partir do Liquid.

![Os detalhes de um agente que tenha Liquid em suas instruções.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## Catálogos e campos

Escolha catálogos específicos para que um agente faça referência e forneça ao seu agente o contexto necessário para entender seus produtos e outros dados de usuários, quando relevante. Os agentes usam ferramentas para encontrar apenas os itens relevantes e enviá-los ao LLM para minimizar o uso de tokens.

![O catálogo "restaurants" e a coluna "Loyalty_Program" selecionados para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## Contexto de associação de segmento

É possível selecionar até três segmentos para o agente fazer referência cruzada da associação de segmento de cada usuário quando o agente for usado em uma tela. Digamos que seu agente tenha a associação de segmento selecionada para um segmento "Usuários de fidelidade" e que o agente seja usado em uma tela. Quando os usuários entram em uma etapa do agente, o agente pode fazer referência cruzada se cada usuário é membro de cada segmento especificado no console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O segmento "Usuários de fidelidade" selecionado para acesso de associação de agentes.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## Diretrizes da marca

É possível selecionar [as diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que seu agente deve seguir em suas respostas. Por exemplo, se quiser que seu agente gere uma cópia de SMS para incentivar os usuários a inscreverem-se em uma academia, poderá usar esse campo para fazer referência à sua diretriz motivacional e em negrito predefinida.

## Temperatura

Se o seu objetivo é usar um agente para gerar uma cópia para incentivar os usuários a registrar seu app móvel, você pode definir uma temperatura mais alta para que o agente seja mais criativo e use as nuances das variáveis de contexto. Se você estiver usando um agente para gerar pontuações de sentimento, pode ser ideal definir uma temperatura mais baixa para evitar qualquer especulação do agente sobre respostas negativas à pesquisa. Recomendamos testar essa configuração e revisar a saída gerada pelo agente para adequá-la ao seu cenário.

{% alert note %}
No momento, as temperaturas não são suportadas para uso com o OpenAI.
{% endalert %}