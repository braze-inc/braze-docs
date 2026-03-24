---
nav_title: Criar agentes
article_title: Criar agentes personalizados
description: "Aprenda como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados."
page_order: 1
alias: /creating-agents/
---

# Criar agentes personalizados

> Aprenda como criar agentes personalizados, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados. Para mais informações gerais, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Pré-requisitos

Antes de começar, você precisará do seguinte:

- [Permissão]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) para acessar o **Agent Console** no seu espaço de trabalho. Verifique com seus administradores da Braze se você não vê esta opção.  
- Permissão para criar e editar Agentes de IA personalizados.
- Um [provedor de modelo de IA]({{site.baseurl}}/partners/ai_model_providers) integrado com a Braze.
- Uma ideia do que você quer que o agente realize. Os Braze Agents podem suportar as seguintes ações:  
   - **Envio de mensagens:** Gerar linhas de assunto, manchetes, textos dentro do produto ou outros conteúdos.  
   - **Tomada de decisões:** Direcionar usuários no Canvas com base em comportamento, preferências ou atributos personalizados.  
   - **Gerenciamento de dados:** Calcular valores, enriquecer entradas de catálogo ou atualizar campos de perfil.  

## Como funciona

Quando você cria um agente, define seu propósito e estabelece diretrizes sobre como ele deve se comportar. Depois que estiver ativo, o agente pode ser implantado na Braze para gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo. Você pode pausar ou atualizar um agente a qualquer momento a partir do dashboard.

Os seguintes casos de uso mostram algumas maneiras de aproveitar agentes personalizados.

| Caso de uso | Descrição |
| --- | --- |
| Tratamento de feedback do cliente | Passe o feedback do usuário para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Localizar conteúdo | Traduzir o texto do catálogo para outro idioma para campanhas globais, ou ajustar o tom e o comprimento para canais específicos da região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster," ou encurte descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resumir o sentimento ou feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo de texto curto como "A maioria dos clientes menciona um ótimo caimento, mas nota o envio lento." |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Criar um agente

### Etapa 1: Escolher um tipo de agente

Para criar seu agente personalizado:

1. Acesse **Agent Console** > **Agent Management** no dashboard da Braze.  
2. Selecione **Criar agente**.
3. Escolha criar um agente Canvas ou um agente de catálogo.

### Etapa 2: Configurar detalhes

Em seguida, configure os detalhes do seu agente:

1. Digite um nome e uma descrição para ajudar sua equipe a entender seu propósito.
2. (opcional) Adicione tags para filtrar seu agente.
3. Escolha o [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que seu agente deve usar.
4. Se você não estiver usando o modelo **Braze Auto**, selecione o [nível de pensamento]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) do modelo. Você pode escolher entre mínimo, baixo, médio ou alto. Recomendamos começar com **Mínimo** e testar as respostas do seu agente, ajustando conforme necessário.
5. Defina um limite diário de execução. Por padrão, esse valor é definido como 250.000, mas pode ser aumentado para 1.000.000. Se você tiver interesse em aumentar o limite acima de 1.000.000, entre em contato com seu gerente de sucesso do cliente para saber mais.

![Interface do Agent Console para criar um agente personalizado na Braze. A tela exibe campos para inserir o nome e a descrição do agente, selecionar um modelo e definir um limite diário de execução.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Etapa 3: Escreva as instruções {#agent-instructions}

Dê instruções ao agente. Recomendamos incluir instruções sobre o que o agente deve fazer em cenários inesperados ou ambíguos. Isso minimiza o risco de que a confusão do agente leve a erros. Por exemplo, em vez de pedir ao agente apenas valores de sentimento "positivo" ou "negativo", peça para retornar "incerto" se ele não conseguir decidir.

Consulte [Escrevendo instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) para melhores práticas e [Exemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) para inspiração sobre como orientar seu agente.

{% alert tip %}
Para agentes Canvas, você pode usar Liquid nas suas instruções para referenciar atributos do usuário, como primeiro e último nome, ou atributos personalizados. Qualquer variável Liquid nas instruções do agente é automaticamente passada para a etapa do Agente quando um usuário entra na etapa.
{% endalert %}

#### Etapa 3.1: Adicionar recursos

Selecione **Adicionar recursos** para escolher o que seu agente pode referenciar. Isso inclui:

- [Campos de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Dê ao agente acesso aos dados do seu catálogo para respostas mais precisas.
- [Associação a segmentos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Permita que o agente personalize respostas com base nos segmentos aos quais um usuário pertence. Você pode selecionar até cinco segmentos.
- [Diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Referencie a voz da marca e as diretrizes de estilo para o agente seguir. Por exemplo, se você quiser que seu agente gere textos de SMS para incentivar os usuários a se inscreverem em uma academia, você pode usar este campo para referenciar sua diretriz da marca motivacional e em negrito pré-definida.
- [Todo o contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analise todos os dados de contexto do Canvas para um usuário quando este agente for invocado, incluindo quaisquer variáveis que não estão referenciadas na seção **Instruções**.

#### Etapa 3.2: Adicione configurações opcionais

Nas **Configurações opcionais**, você pode ajustar a [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) do texto gerado pelo agente. Uma temperatura mais alta permite que o agente use as informações fornecidas de forma mais criativa.

### Etapa 4: Selecione a saída {#select-output}

Na seção **Saída**, você pode organizar e definir a saída do agente por esquemas básicos ou esquemas avançados.

Para melhores resultados, certifique-se de que o que você especifica na seção **Saída** corresponda às instruções do agente que você inseriu na [Etapa 3](#agent-instructions). Por exemplo, se você mencionou nas instruções do agente que deseja um objeto com duas strings, certifique-se de especificar um objeto com duas strings na seção **Saída**. Se as instruções do seu agente não estiverem alinhadas com a saída especificada, o agente pode ficar confuso, expirar ou gerar saídas indesejadas.

#### Esquemas básicos

Esquemas básicos são uma saída simples que um agente retorna. Isso pode ser uma string, um número, um booleano, um array de strings ou um array de números.

Por exemplo, se você quiser coletar pontuações de sentimento dos usuários a partir de uma pesquisa de feedback simples para determinar quão satisfeitos seus clientes estão após receber um produto, você pode selecionar **Número** como esquema básico para estruturar o formato da saída.

{% alert important %}
Arrays estão disponíveis apenas para agentes Canvas, não para agentes de catálogo.
{% endalert %}

![Agent Console com número selecionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Esquemas avançados

As opções de esquema avançado incluem estruturar campos manualmente ou usar JSON.

- **Campos:** Uma maneira sem código de definir uma saída de agente que você pode usar de forma consistente.
- **JSON:** Uma abordagem com código para criar um formato de saída preciso, onde você pode aninhar variáveis e objetos dentro do esquema JSON. Disponível apenas para agentes Canvas, não para agentes de catálogo.

Recomendamos usar esquemas avançados quando você deseja que o agente retorne uma estrutura de dados com múltiplos valores definidos de maneira estruturada, em vez de uma saída de valor único. Isso permite que a saída seja melhor formatada como uma variável de contexto consistente.

Por exemplo, você pode usar um formato de saída dentro de um agente destinado a criar um itinerário de viagem de exemplo para um usuário com base em um formulário que ele enviou. O formato de saída permite que você defina que cada resposta do agente deve retornar com valores para `tripStartDate`, `tripEndDate` e `destination`. Cada um desses valores pode ser extraído de variáveis de contexto e colocado em uma etapa de Mensagem para personalização usando Liquid.

{% tabs %}
{% tab Fields %}

Se você quiser formatar respostas de uma pesquisa de feedback simples para determinar quão propensos os respondentes estão a recomendar o novo sabor de sorvete do seu restaurante, você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **likelihood_score** | Número |
| **explanation** | String |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agent Console mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Se você quiser coletar feedback dos usuários sobre a experiência de jantar mais recente na sua rede de restaurantes, pode selecionar **JSON Schema** como o formato de saída e inserir o seguinte JSON para retornar um objeto de dados que inclui uma variável de sentimento e uma variável de raciocínio.

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

{% endtab %}
{% endtabs %}

### Etapa 5: Teste e crie o agente

O painel **Prévia** é uma instância do agente que aparece como um painel lado a lado dentro da experiência de configuração. Você pode usá-lo para testar o agente enquanto está criando ou fazendo atualizações, vivenciando-o de maneira semelhante aos usuários finais. Esta etapa ajuda você a confirmar que ele está se comportando da maneira esperada e dá a chance de fazer ajustes antes de colocá-lo no ar.

1. No campo **Teste seu agente**, insira dados de cliente de exemplo ou respostas de clientes — qualquer coisa que reflita cenários reais que seu agente vai lidar.
2. Visualize a resposta do agente para um usuário aleatório, usuário existente ou usuário personalizado.
3. Selecione **Simular resposta**. O agente executará com base na sua configuração e exibirá sua resposta.

{% alert note %}
Os testes contam para o seu limite diário de execução.
{% endalert %}

![Agent Console mostrando o painel de Prévia para testar um agente personalizado. A interface exibe um campo de Entradas de exemplo com dados de cliente, um botão Executar teste e uma área de resposta onde a saída do agente aparece.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revise a saída com um olhar crítico. Considere as seguintes perguntas:

- O texto parece estar alinhado com a marca?
- A lógica de decisão direciona os clientes conforme o esperado?
- Os valores calculados estão precisos?

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta a diferentes cenários, especialmente casos extremos como ausência de dados ou respostas inválidas.

{% alert tip %}
Evite dizer ao agente exatamente o que você não quer que ele faça. Os LLMs ainda podem gerar esse conteúdo se você mencioná-lo nas instruções.
{% endalert %}

### Etapa 6: Use seu agente

Seu agente está pronto para uso! Para mais detalhes, consulte [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Artigos relacionados  

- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)