---
nav_title: "Pesquisa simples"
article_title: Mensagem simples de pesquisa no aplicativo
page_order: 1.5
page_type: reference
description: "Este artigo de referência aborda como coletar atributos, insights e preferências do usuário para impulsionar sua estratégia de campanha usando as pesquisas de mensagens in-app."
channel:
  - in-app messages
tool:
  - Templates
---

# Pesquisa simples

> Use o modelo de mensagem in-app do **Simple Survey** para coletar atributos, insights e preferências do usuário que impulsionam sua estratégia de campanha. 

Por exemplo, pergunte aos usuários como eles gostariam de usar seu aplicativo, saiba mais sobre suas preferências pessoais ou até mesmo pergunte sobre a satisfação deles com um determinado recurso.

\![Três mensagens de pesquisa simples: preferências de notificação, preferências alimentares e uma pesquisa de satisfação do cliente. As opções selecionadas nas pesquisas correspondem a atributos personalizados que serão registrados para esse usuário.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos do SDK {#supported-sdk-versions}

Essa mensagem no aplicativo só será entregue a dispositivos que suportam [Flex CSS](https://caniuse.com/flexbox) e devem ter pelo menos as seguintes [versões do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para ativar as mensagens HTML in-app por meio do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` ao Braze.
{% endalert %}

## Criação de uma pesquisa {#create}

Ao criar uma [mensagem no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), selecione **Pesquisa simples** como **tipo de mensagem**.

Esse modelo de questionário é compatível tanto com aplicativos móveis quanto com navegadores da Web. Lembre-se de verificar se seus SDKs estão nas [versões mínimas de SDK](#supported-sdk-versions) necessárias para esse recurso.

### Etapa 1: Adicione sua pergunta de pesquisa

Para começar a criar seu questionário, adicione sua pergunta ao campo **Cabeçalho** do questionário. Se desejar, é possível adicionar uma mensagem de **corpo** opcional que aparecerá abaixo da pergunta do questionário.

Guia Compor do editor de questionário simples, com campos para um cabeçalho, corpo opcional e texto auxiliar opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Esses campos podem incluir tanto o Liquid quanto emojis, portanto, capriche!
{% endalert %}

### Etapa 2: Configurar opções {#single-multiple-choice}

É possível adicionar até 12 opções em um questionário.

Selecione **Seleção de escolha única** ou **Seleção de escolha múltipla**. O **texto do Helper** será atualizado automaticamente quando você alternar entre as duas opções para informar aos usuários quantas opções eles podem selecionar. 

Em seguida, determine se você [coletará atributos personalizados](#custom-attributes) ou [apenas respostas de registro](#no-attributes).

\![Menu suspenso de opções com a opção "Registrar atributos no envio" selecionada.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Coletar atributos personalizados {#custom-attributes}

Selecione **Log attributes upon submission (Registrar atributos no envio)** para coletar atributos com base no envio do usuário. Você pode usar essa opção para criar novos segmentos e campanhas de redirecionamento. Por exemplo, em uma [pesquisa de satisfação](#user-satisfaction), você pode enviar um e-mail de acompanhamento para todos os usuários que não ficaram satisfeitos.

Para adicionar um atributo personalizado a cada opção, selecione um nome de atributo personalizado no menu suspenso (ou crie um novo) e, em seguida, insira o valor a ser definido quando essa opção for enviada. Você também pode criar um novo atributo personalizado em sua [página de configurações]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

O tipo de dados de seus atributos personalizados é importante, dependendo de como você configurou o questionário.

- **Seleção de múltipla escolha:** O tipo de dados do atributo personalizado deve ser uma matriz. Se o atributo personalizado for definido como um tipo de dados diferente, as respostas não serão registradas.
- **Seleção de escolha única:** O tipo de dados do atributo personalizado _não deve_ ser uma matriz. As respostas não serão registradas se o atributo for uma matriz.

{% alert important %}
Quando a coleção de atributos personalizados estiver ativada, as opções que compartilham o mesmo nome de atributo personalizado serão combinadas em uma matriz.
{% endalert %}

##### Exemplo 

Por exemplo, em uma [pesquisa de preferências de notificação](#notification-preferences), você pode fazer de cada opção um atributo booleano (verdadeiro/falso) para permitir que os usuários selecionem os tópicos nos quais estão interessados. Se um usuário marcar a opção "Promotions" (Promoções), isso atualizará seu [perfil de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) com o atributo personalizado `Promotions Topic` definido como `true`. Se eles deixarem a opção desmarcada, esse mesmo atributo permanecerá inalterado.

Em seguida, é possível usar o filtro `Custom Attribute` para criar um segmento para usuários com o atributo personalizado `Promotions Topic` `is` `true` para garantir que somente os usuários interessados em suas promoções recebam as campanhas relevantes.

#### Registro de respostas apenas {#no-attributes}

Como alternativa, você pode optar por **registrar apenas as respostas (sem atributos)**. Quando essa opção é selecionada, as respostas da pesquisa são registradas como cliques em botões, mas os atributos personalizados não são registrados no perfil do usuário. Isso significa que ainda é possível visualizar as métricas de cliques de cada opção de questionário (consulte o [Analytics](#analytics)), mas essa escolha não será refletida no perfil do usuário.

Essas métricas de cliques não estão disponíveis para retargeting.

### Etapa 4: Escolha o comportamento de envio

Depois que o usuário enviar sua resposta, você poderá exibir uma página de confirmação ou simplesmente fechar a mensagem.

Uma página de confirmação é um ótimo lugar para agradecer aos usuários pelo tempo despendido ou fornecer informações adicionais. Você pode personalizar a chamada para ação nessa página para orientar os usuários para outra página do seu aplicativo ou site.

Edite o texto do botão e o comportamento ao clicar na seção **Botão Enviar**, na parte inferior da guia **Questionário**:

\![Comportamento ao clicar definido como "Enviar respostas e exibir página de confirmação".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Se optar por adicionar uma página de confirmação, vá para a guia **Confirmation Page (Página de confirmação** ) para personalizar sua mensagem:

\![Guia Página de confirmação do editor de questionário simples. Os campos disponíveis são cabeçalho, corpo opcional, texto do botão e comportamento ao clicar no botão.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Se quiser guiar os usuários para outra página do seu aplicativo ou site, altere o **comportamento On-click** do botão.

### Etapa 5: Estilize sua mensagem (opcional) {#styling}

Você pode personalizar a cor da fonte e a cor de destaque da mensagem usando o seletor **Color Theme**.

Guia Compose do editor de questionário simples com o seletor Color Theme expandido depois que um usuário clica na paleta de cores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analisar resultados {#analytics}

Após o lançamento da campanha, você pode analisar os resultados em tempo real para ver o detalhamento de cada opção selecionada. Se tiver ativado [a coleta de atributos personalizados](#custom-attributes), também será possível criar novos segmentos ou campanhas de acompanhamento para os usuários que enviaram o questionário.

{% alert note %}
As opções de questionário excluídas ainda aparecerão nas análises, mas não serão exibidas como opção para novos usuários.
{% endalert %}

É possível encontrar as métricas de desempenho do questionário expandindo o menu suspenso **Resultados** para uma variante específica na seção **Desempenho de mensagens no aplicativo** da análise. Aqui está um resumo do que você verá:

- **O envolvimento com** o questionário mostra como os usuários interagiram com o questionário em geral, incluindo o total de envios, recusas e cliques no corpo da mensagem.
- **Os resultados da pesquisa** exibem um detalhamento de quantos usuários selecionaram cada opção de resposta, juntamente com a porcentagem do total de envios que cada opção representa.
- **As métricas da página de confirmação** (se ativadas) incluem quantos usuários visualizaram a tela de confirmação, clicaram em seu botão ou a descartaram sem interagir.

Para obter definições das métricas de pesquisa, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics/) e filtre por "Mensagem no aplicativo".

Confira [os relatórios de mensagens in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para obter um detalhamento das métricas de sua campanha.

### Correntes {#currents}

As opções selecionadas serão automaticamente transferidas para o Currents, na seção [**Eventos de clique em mensagens no aplicativo**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` campo. Cada escolha será enviada com seu identificador universalmente exclusivo (UUID).

## Casos de uso

{% tabs %}
{% tab User satisfaction %}

### Satisfação do usuário

**Objetivo:** Meça a satisfação do cliente e envie campanhas de recuperação para os usuários que deixaram pontuações baixas.

Para configurar isso, use uma pesquisa de seleção de escolha única com cinco opções que variam de "😡 Muito insatisfeito" a "😍 Muito satisfeito". Cada escolha é mapeada para o atributo personalizado `customer_satisfaction`, com um valor numérico de 1 a 5, em que 1 indica o menos satisfeito e 5 o mais satisfeito.

| Escolha                                | Atributo              | Valor |
|---------------------------------------|------------------------|-------|
| Muito insatisfeito                  | `customer_satisfaction` | 1     |
| Insatisfeito                       | `customer_satisfaction` | 2     |
| 🙂 Nem satisfeito nem insatisfeito | `customer_satisfaction` | 3     |
| 😊 Satisfeito                          | `customer_satisfaction` | 4     |
| Muito satisfeito                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, o valor selecionado é registrado como um atributo personalizado. Em seguida, você pode criar campanhas de acompanhamento usando filtros de público-alvo. Por exemplo, direcione as mensagens de recuperação para usuários cujo atributo `customer_satisfaction` seja 1 ou 2.

{% endtab %}
{% tab Notification preferences %}

### Preferências de notificação

**Objetivo:** Permita que os usuários optem por tipos específicos de notificações.

Para configurar isso, use uma pesquisa de seleção de múltipla escolha em que cada opção represente um tópico de notificação. Em vez de atribuir o mesmo atributo com valores diferentes, cada escolha é mapeada para um atributo booleano distinto que reflete o interesse do usuário naquele tópico. Se um usuário selecionar uma opção, o atributo correspondente será definido como `true`. Se não for selecionado, o atributo permanecerá inalterado.

| Escolha             | Atributo              | Valor  |
|--------------------|------------------------|--------|
| Atualizações de produtos    | `wants_product_updates`| `true` |
| Promoções         | `wants_promotions`     | `true` |
| Convites para eventos      | `wants_event_invites`  | `true` |
| Pesquisas & Feedback | `wants_surveys`        | `true` |
| Dicas & Tutoriais   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Identificar as metas do cliente

**Objetivo:** Identifique os principais motivos pelos quais os usuários visitam seu aplicativo.

Para configurar isso, use um questionário de seleção de escolha única com cada opção representando uma meta ou intenção comum. Cada opção é mapeada para o atributo personalizado `product_goal` com um valor correspondente à intenção do usuário selecionada.

| Escolha                     | Atributo       | Valor     |
|----------------------------|------------------|-----------|
| Verificação de status            | `product_goal`   | `status`  |
| Atualizando minha conta       | `product_goal`   | `upgrade` |
| Agendamento de um compromisso  | `product_goal`   | `schedule`|
| Suporte ao cliente           | `product_goal`   | `support` |
| Apenas navegando              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, o valor selecionado é registrado como um atributo personalizado em seu perfil. Em seguida, é possível usar esses dados para personalizar experiências futuras ou segmentar usuários com base em seu objetivo principal.

{% endtab %}
{% tab Improve conversion rates %}

### Melhorar as taxas de conversão

**Objetivo:** Entenda por que os clientes não estão fazendo upgrade ou comprando.

Para configurar isso, use uma pesquisa de seleção de escolha única com cada opção representando uma barreira comum à atualização. Cada opção é mapeada para o atributo personalizado `upgrade_reason` com um valor correspondente que reflete a seleção do usuário.

| Escolha              | Atributo        | Valor       |
|---------------------|------------------|-------------|
| Muito caro       | `upgrade_reason` | `expensive` |
| Não valioso        | `upgrade_reason` | `value`     |
| Difícil de usar    | `upgrade_reason` | `difficult` |
| Usando um concorrente  | `upgrade_reason` | `competitor`|
| Outro motivo        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, o valor selecionado é salvo em seu perfil. Em seguida, é possível direcionar esses usuários com campanhas adaptadas às suas objeções específicas, como ofertas de desconto ou melhorias de usabilidade.

{% endtab %}
{% tab Favorite features %}

### Recursos favoritos

**Objetivo:** Entenda quais recursos os clientes gostam de usar.

Para configurar isso, use uma pesquisa de seleção de múltipla escolha em que cada opção represente um recurso do seu aplicativo. Cada opção é mapeada para o atributo personalizado `favorite_features` e, quando o usuário envia a pesquisa, o atributo é definido como uma matriz dos valores selecionados.

| Escolha            | Atributo          | Valor        |
|-------------------|--------------------|--------------|
| Marcadores         | `favorite_features`| `bookmarks`  |
| Aplicativo móvel        | `favorite_features`| `mobile`     |
| Compartilhamento de postagens     | `favorite_features`| `sharing`    |
| Suporte ao cliente  | `favorite_features`| `support`    |
| Personalização     | `favorite_features`| `custom`     |
| Preço / Valor     | `favorite_features`| `value`      |
| Comunidade         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como essa pesquisa usa seleção de múltipla escolha, o perfil do usuário será atualizado com uma lista de todos os valores de recursos selecionados.

{% endtab %}
{% endtabs %}
