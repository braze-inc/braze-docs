---
nav_title: Criação de agentes
article_title: Criação de agentes personalizados
description: "Saiba como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar em mensagens, decisões e gerenciamento de dados."
alias: /creating-agents/
---

# Criação de agentes personalizados

> Saiba como criar agentes personalizados, o que preparar antes de começar e como colocá-los para trabalhar em mensagens, decisões e gerenciamento de dados. Para obter mais informações gerais, consulte [Agentes do Braze]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Os Agentes Braze estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Pré-requisitos

Antes de começar, você precisará do seguinte:

- Acesso ao **Console do agente** em seu espaço de trabalho. Verifique com os administradores do Braze se você não encontrar essa opção.  
- Permissão para criar e editar agentes de IA personalizados. 
- Uma ideia do que você deseja que o agente realize. Os Agentes Braze podem suportar as seguintes ações:  
   - **Mensagens:** Gere linhas de assunto, manchetes, textos no produto ou outros conteúdos.  
   - **Tomada de decisões:** Encaminhe os usuários no Canvas com base em comportamento, preferências ou atributos personalizados.  
   - **Gerenciamento de dados:** Calcular valores, enriquecer entradas de catálogo ou atualizar campos de perfil.  

## Como funciona

Ao criar um agente, você define a sua finalidade e estabelece as diretrizes de como ele deve se comportar. Depois de entrar em operação, o agente pode ser implantado no Braze para gerar cópias personalizadas, tomar decisões em tempo real ou atualizar campos do catálogo. Você pode pausar ou atualizar um agente a qualquer momento no painel.

## Criar um agente

Para criar seu agente personalizado:  

1. Vá para **Console do agente** > **Gerenciamento de agentes** no painel do Braze.  
2. Selecione **Criar agente**.  
3. Insira um nome e uma descrição para ajudar sua equipe a entender a finalidade.  
4. Escolha o [modelo](#models) que seu agente usará.  

Interface do Console do Agente para criar um agente personalizado no Braze. A tela exibe campos para inserir o nome e a descrição do agente e selecionar um modelo.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. Dê instruções ao agente. Consulte [as instruções de escrita](#writing-instructions) para obter orientação.
6. [Teste a](#testing-your-agent) saída [do agente](#testing-your-agent) e ajuste as instruções conforme necessário.
7. Quando estiver pronto, selecione **Create Agent** para ativar o agente. 

## Próxima etapa

Seu agente agora está pronto para ser usado! Para obter detalhes, consulte [Implantação de agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Referência

### Modelos

Ao configurar um agente, você escolherá o modelo que ele usará para gerar respostas. Você tem duas opções:

#### Opção 1: Use um modelo alimentado pelo Braze

Essa é a opção mais simples, sem necessidade de configuração adicional. O Braze fornece acesso direto a modelos de linguagem grandes (LLM). Para usar essa opção, selecione **Auto**.

{% alert note %}
Se você usar o LLM com tecnologia Braze, não incorrerá em nenhum custo durante o período Beta. A invocação é limitada a 50.000 execuções por dia e 500.000 execuções no total. Consulte [Limitações]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) para obter detalhes.
{% endalert %}

#### Opção 2: Traga sua própria chave de API

Com essa opção, você pode conectar sua conta Braze a provedores como OpenAI, Anthropic, AWS Bedrock ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos serão cobrados diretamente pelo provedor, não pelo Braze.

Para configurar isso:
1. Vá para **Partner Integrations** > **Technology Partners** e encontre seu provedor.
2. Digite sua chave de API do provedor.
3. Selecione **Salvar**.

Em seguida, você pode retornar ao seu agente e selecionar seu modelo.

### Instruções de escrita

Instruções são as regras ou diretrizes que você fornece ao agente (prompt do sistema). Eles definem como o agente deve se comportar sempre que for executado. As instruções do sistema podem ter até 10 KB.

{% tabs %}
{% tab Best practices %}

Aqui estão algumas práticas recomendadas gerais para você começar a usar as solicitações:

1. Comece com o fim em mente. Primeiro, declare o objetivo.
2. Dê ao modelo uma função ou personagem ("Você é um ...").
3. Defina claramente o contexto e as restrições (público, duração, tom, formato).
4. Solicite a estrutura ("Return JSON/bullet list/table...").
5. Mostre, não diga. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1... Etapa 2...").
7. Incentivar o raciocínio ("Pense em voz alta, depois responda").
8. Pilotar, inspecionar e iterar. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione proteções e instruções de recusa.
10. Medir e documentar o que funciona internamente para reutilização e dimensionamento.

Para obter mais detalhes sobre as práticas recomendadas de solicitação, consulte os guias dos seguintes fornecedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Antrópica](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gêmeos](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

Esse prompt de exemplo recebe uma entrada de pesquisa e gera uma análise de sentimento simples:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

Esse prompt de exemplo pega uma entrada de pesquisa de um usuário e a classifica em um único rótulo de sentimento. O resultado pode então ser usado para direcionar os usuários por diferentes caminhos do Canvas (como feedback positivo versus negativo) ou armazenar o sentimento como um atributo personalizado no perfil deles para direcionamento futuro.

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
{% enddetails %}

{% endtab %}
{% endtabs %}


#### Testando seu agente  

O painel de **visualização em tempo real** é uma instância do agente que aparece como um painel lado a lado na experiência de configuração. Você pode usá-lo para testar o agente enquanto estiver criando ou atualizando-o para experimentá-lo de forma semelhante à dos usuários finais. Essa etapa ajuda a confirmar que ele está se comportando da maneira esperada e lhe dá a chance de fazer ajustes finos antes de entrar em operação.

Console do agente mostrando o painel de visualização ao vivo para testar um agente personalizado. A interface exibe um campo de entradas de amostra com dados de clientes de exemplo, um botão Executar teste e uma área de resposta em que a saída do agente é exibida.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. No campo **Sample inputs (Entradas de amostra)**, insira dados de exemplo de clientes ou respostas de clientes - qualquer coisa que reflita cenários reais com os quais seu agente lidará. 
2. Selecione **Executar teste**. O agente será executado com base em sua configuração e exibirá sua resposta. As execuções de teste contam para o seu limite diário e total de invocações.

Analise o resultado com um olhar crítico. Considere as seguintes perguntas:

- O texto está de acordo com a marca? 
- A lógica da decisão encaminha os clientes como pretendido? 
- Os valores calculados são precisos? 

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta aos cenários, especialmente em casos extremos, como ausência de dados ou respostas inválidas.

