---
nav_title: "Pesquisa simples"
article_title: Mensagem no app de pesquisa simples
page_order: 1.5
page_type: reference
description: "Este artigo de referência cobre como coletar atributos, percepções e preferências do usuário para impulsionar sua estratégia de campanha usando as pesquisas de mensagem no app."
channel:
  - in-app messages
tool:
  - Templates
---

# Pesquisa simples

> Use o **Simple Survey** modelo de mensagem no app para coletar atributos, percepções e preferências dos usuários que impulsionam sua estratégia de campanha. 

Por exemplo, pergunte aos usuários como eles gostariam de usar seu app, saiba mais sobre suas preferências pessoais ou até mesmo pergunte sobre a satisfação deles com um recurso específico.

![Três mensagens de pesquisa simples: preferências de notificação, preferências alimentares e uma pesquisa de satisfação do cliente. As opções selecionadas nas pesquisas correspondem a atributos personalizados que serão registrados para aquele usuário.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos do SDK {#supported-sdk-versions}

Esta mensagem no app será entregue apenas para dispositivos que suportam [Flex CSS](https://caniuse.com/flexbox), e devem ter pelo menos as seguintes [versões do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para ativar mensagens no app HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze.
{% endalert %}

## Criando uma pesquisa {#create}



Este modelo de pesquisa é compatível com aplicativos móveis e navegadores da web. Lembre-se de verificar se seus SDKs estão nas [versões mínimas de SDK](#supported-sdk-versions) necessárias para este recurso.

### Etapa 1: Adicione sua pergunta da pesquisa

Para começar a construir sua pesquisa, adicione sua pergunta ao campo **Header** da pesquisa. Se desejar, você pode adicionar uma mensagem opcional **Body** que aparecerá sob sua pergunta da pesquisa.



{% alert tip %}
Esses campos podem incluir tanto Liquid quanto emojis, então seja criativo!
{% endalert %}

### Etapa 2: 

Você pode adicionar até 12 opções em uma pesquisa.

  



![Opções suspensas com "registro de atributos ao enviar" selecionado.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Coletar atributos personalizados {#custom-attributes}

Selecione **atributos de registro na submissão** para coletar atributos com base na submissão do usuário. Você pode usar esta opção para criar novos segmentos e campanhas de redirecionamento. 

Para adicionar um atributo personalizado a cada escolha, selecione um nome de atributo personalizado no menu suspenso (ou crie um novo) e, em seguida, insira o valor a ser definido quando essa escolha for enviada. 

O tipo de dado dos seus atributos personalizados importa dependendo de como você configurou sua pesquisa.

- **Seleção de múltipla escolha:** O tipo de dado do atributo personalizado deve ser um array. Se o atributo personalizado estiver definido para um tipo de dado diferente, as respostas não serão registradas.
- **Seleção de escolha única:** O tipo de dado do atributo personalizado _não deve_ ser um array. As respostas não serão registradas se o atributo for um array.

{% alert important %}
Quando a coleta de atributo personalizado está ativada, as escolhas que compartilham o mesmo nome de atributo personalizado serão combinadas em um array.
{% endalert %}

#####  

  Se eles deixarem a escolha desmarcada, esse mesmo atributo permanecerá inalterado.



#### 

Alternativamente, você pode optar por **registrar apenas as respostas (sem atributos)**. Quando esta opção é selecionada, as respostas da pesquisa são registradas como cliques de botão, mas os atributos personalizados não são registrados no perfil do usuário. Isso significa que você ainda pode ver as métricas de cliques para cada opção de pesquisa (veja [análise de dados](#analytics)), mas essa escolha não será refletida no perfil do usuário.

Essas métricas de cliques não estão disponíveis para redirecionamento.

### Etapa 4: Escolha o comportamento de envio

Depois que um usuário enviar sua resposta, você pode opcionalmente mostrar uma página de confirmação ou simplesmente fechar a mensagem.

Uma página de confirmação é um ótimo lugar para agradecer aos usuários pelo seu tempo ou fornecer informações adicionais. 

Edite o texto do seu botão e o comportamento ao clicar na seção **Botão de Enviar** na parte inferior da guia **Pesquisa**:

![Comportamento ao clicar definido como "Enviar respostas e exibir página de confirmação".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Se você optar por adicionar uma página de confirmação, mude para a guia **Confirmation Page** para personalizar sua mensagem:

![Guia da Página de Confirmação do editor de pesquisa simples. 

Se você deseja guiar os usuários para outra página do seu app ou site, altere o **comportamento ao clicar** do botão.

### Etapa 5: Estilize sua mensagem (opcional) {#styling}

Você pode personalizar a cor da fonte e a cor de destaque da mensagem usando o seletor de **tema de cores**.

![Guia de composição do editor de pesquisa simples com o seletor de tema de cores expandido após um usuário ter clicado na paleta de cores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analisar resultados {#analytics}

Depois que sua campanha for lançada, você poderá analisar os resultados em tempo real para ver a divisão de cada escolha selecionada. Se você ativou a [coleta de atributo personalizado](#custom-attributes), também poderá criar novos segmentos ou campanhas de acompanhamento para usuários que responderam à pesquisa.

{% alert note %}
As escolhas de pesquisa excluídas ainda aparecerão na análise de dados, mas não serão mostradas como uma escolha para novos usuários.
{% endalert %}

 

- 
- 
- 





### Currents {#currents}

 Cada escolha será enviada com seu identificador único universal (UUID).

## Casos de uso

### Satisfação do usuário

**Objetivo:** Meça a satisfação do cliente e envie campanhas de recuperar para usuários que deixaram baixas pontuações.

 

|                                 |               |  |
|---------------------------------------|------------------------|-------|
|                   |  |      |
|                        |  |      |
|  |  |      |
|                           |  |      |
|                      |  |      |


  

### 

**Objetivo:** 

   

|              |               |   |
|--------------------|------------------------|--------|
|     | |  |
|          |      |  |
|       |   |  |
|  |         |  |
|    |            |  |


### Identificar metas do cliente

**Objetivo:** Identifique os principais motivos pelos quais os usuários visitam seu app.

 

|                      |        |      |
|----------------------------|------------------|-----------|
|             |    |   |
|        |    |  |
|   |    | |
|            |    |  |
|               |    |   |


 

### Melhore as taxas de conversão

**Objetivo:** 

 

|               |         |        |
|---------------------|------------------|-------------|
|        |  |  |
|         |  |      |
|     |  |  |
|   |  | |
|         |  |      |


 

### Recursos favoritos

**Objetivo:** Compreenda quais recursos os clientes gostam de usar.

 

|             |           |         |
|-------------------|--------------------|--------------|
|          | |   |
|         | |      |
|      | |     |
|   | |     |
|      | |      |
|      | |       |
|          | |   |






