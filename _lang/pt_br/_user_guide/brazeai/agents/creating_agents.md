---
nav_title: Criar agentes
article_title: Criar agentes personalizados
description: "Saiba como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar no envio de mensagens, na tomada de decisões e no gerenciamento de dados."
page_order: 1
alias: /creating-agents/
---

# Criar agentes personalizados

> Saiba como criar agentes personalizados, o que preparar antes de começar e como colocá-los para trabalhar no envio de mensagens, na tomada de decisões e no gerenciamento de dados. Para saber mais sobre informações gerais, consulte [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). 

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

### Etapa 1: Detalhes da configuração

Para criar seu agente personalizado:

1. Acesse **Console do agente** > **Gerenciamento do agente** no dashboard do Braze.  
2. Selecione **Criar agente**.
3. Digite um nome e uma descrição para ajudar a sua equipe a entender a finalidade.
4. (opcional) Adicione tags para filtrar seu agente.
5. Selecione o site de interação, que é o local onde o agente está implantado. Note que o site de interação não pode ser atualizado depois que um agente é criado.
6. Escolha o [modelo]({{site.baseurl}}/docs/user_guide/brazeai/agents/reference/#models) que seu agente usará.

![Interface do console do agente para criar um agente personalizado no Braze. A tela exibe campos para inserir o nome e a descrição do agente e selecionar um modelo.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

### Etapa 2: Escreva as instruções

Dê instruções ao agente. Consulte a [referência dos agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/) para obter orientação.

{% alert tip %}
É possível usar o Liquid em suas instruções para fazer referência a atribuições do usuário, como nome e sobrenome, ou atributos personalizados.
{% endalert %}

#### Etapa 2.1: Adicionar contexto

Selecione **Adicionar contexto** para escolher o que seu agente pode referenciar. Isso inclui:

- [Campos do catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Forneça campos de catálogo para o agente fazer referência.
- [Participação no segmento]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Considere a participação de um usuário em um segmento ao personalizar mensagens. Você pode selecionar até três segmentos.
- [Diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Faça referência à voz da marca e às diretrizes de estilo a serem seguidas pelo agente. Por exemplo, se quiser que seu agente gere uma cópia de SMS para incentivar os usuários a inscreverem-se em uma academia, poderá usar esse campo para fazer referência à sua diretriz motivacional e em negrito predefinida.
- [Variáveis de contexto da tela]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analise todas as variáveis do Canvas Context para um usuário quando esse agente for chamado.

#### Etapa 2.2: Adicionar configurações opcionais

Nas **configurações opcionais**, você pode ajustar a [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) da cópia gerada pelo agente. Uma temperatura mais alta permite que o agente use as informações fornecidas para ser mais criativo.

Você também pode definir o limite de execução diária para seu agente. Por padrão, esse valor é definido como 50.000, mas pode ser aumentado para 100.000. Se estiver interessado em aumentar o limite acima de 100.000, entre em contato com o gerente de sucesso do cliente para saber mais.

### Etapa 3: Selecione a saída

Na seção **Saída**, é possível organizar e definir a saída do agente por esquemas básicos ou esquemas avançados.

#### Esquemas básicos

Os esquemas básicos são uma saída simples que um agente retorna. Pode ser uma string, um número, um booleano, uma matriz de strings ou uma matriz de números.

Digamos que você queira coletar pontuações de sentimento do usuário de uma simples pesquisa de feedback para determinar o grau de satisfação dos clientes após receberem um produto. Você pode selecionar **Número** como um esquema básico para estruturar o formato de saída.

{% alert important %}
As matrizes estão disponíveis apenas para agentes do Canva, não para agentes de catálogo.
{% endalert %}

![Console do agente com número selecionado como um esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Esquemas avançados

As opções avançadas de esquema incluem a estruturação manual de campos ou o uso de JSON.

- **Campos:** Uma maneira sem código de impor uma saída de agente que você pode usar de forma consistente. 
- **JSON:** Uma abordagem de código para criar um formato de saída preciso, em que você pode aninhar variáveis e objetos no esquema JSON.

{% tabs %}
{% tab Fields %}

Digamos que você queira formatar as respostas a uma simples pesquisa de feedback para determinar a probabilidade de os entrevistados recomendarem o mais novo sabor de sorvete do seu restaurante. Você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor
| --- | --- |
| **likelihood_score** | Número |
| **explicação** | Texto |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Console do agente mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

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

{% endtab %}
{% endtabs %}

### Etapa 4: Teste e crie o agente

O painel **Prévia** é uma instância do agente que aparece como um painel lado a lado na experiência de configuração. Você pode usá-lo para testar o agente enquanto cria ou atualiza o agente para experimentá-lo de forma semelhante à dos usuários finais. Essa etapa o ajuda a confirmar se o comportamento está sendo o esperado e lhe dá a chance de fazer ajustes finos antes de acessar o site.

1. No campo **Teste seu agente**, insira dados de clientes de exemplo ou respostas de clientes - qualquer coisa que reflita cenários reais com os quais seu agente lidará.
2. Pré-visualize a resposta do agente para um usuário aleatório, usuário existente ou usuário personalizado.
3. Selecione **Simular resposta**. O agente será executado com base em sua configuração e exibirá sua resposta. As execuções de teste contam para seu limite diário de execução.

![Console do agente mostrando o painel Pré-visualização para testar um agente personalizado. A interface exibe um campo de entradas de amostra com dados de cliente de exemplo, um botão Executar teste e uma área de resposta em que a saída do agente é exibida.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Analise o resultado com um olhar crítico. Considere as seguintes perguntas:

- O texto está de acordo com a marca?
- A lógica da decisão encaminha os clientes como pretendido?
- Os valores calculados são precisos?

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta aos cenários, especialmente em casos extremos, como ausência de dados ou respostas inválidas.

### Etapa 5: Use e monitore seu agente

Seu agente agora está pronto para ser usado! Para obter detalhes, consulte [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

Na guia **Registros** do seu agente, é possível monitorar as chamadas de agente reais que ocorrem em suas telas e catálogos. Você pode filtrar por informações como o intervalo de datas, o resultado (sucesso ou falha) ou o local da chamada.

![Registros de um agente Story Teller, que incluem quando e onde o agente foi chamado.]({% image_buster /assets/img/ai_agent/agent_activity_logs.png %})

Selecione **Exibir** para uma chamada de agente específica para ver a entrada, a saída e a ID do usuário.

![Registros para um agente contador de histórias. O painel de detalhes mostra o prompt de entrada, a resposta de saída e uma ID de usuário associada.]({% image_buster /assets/img/ai_agent/agent_logs.png %})
