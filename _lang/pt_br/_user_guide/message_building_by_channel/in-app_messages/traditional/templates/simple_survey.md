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

![Três mensagens de pesquisa simples: preferências de notificação, preferências alimentares e uma pesquisa de satisfação do cliente. As opções selecionadas nas pesquisas correspondem a atributos personalizados que serão registrados para esse usuário.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos do SDK {#supported-sdk-versions}

Esta mensagem no app será entregue apenas para dispositivos que suportam [Flex CSS](https://caniuse.com/flexbox), e devem ter pelo menos as seguintes [versões do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para ativar mensagens no app HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze.
{% endalert %}

## Criando uma pesquisa {#create}

Ao criar uma [mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), selecione **Pesquisa Simples** para o seu **Tipo de Mensagem**.

Este modelo de pesquisa é compatível com aplicativos móveis e navegadores da web. Lembre-se de verificar se seus SDKs estão nas [versões mínimas de SDK](#supported-sdk-versions) necessárias para este recurso.

### Etapa 1: Adicione sua pergunta da pesquisa

Para começar a construir sua pesquisa, adicione sua pergunta ao campo **Header** da pesquisa. Se desejar, você pode adicionar uma mensagem opcional **Body** que aparecerá sob sua pergunta da pesquisa.

![A guia de composição do editor de pesquisa simples, com campos para um cabeçalho, corpo opcional e texto auxiliar opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Esses campos podem incluir tanto Liquid quanto emojis, então seja criativo!
{% endalert %}

### Etapa 2: Configurar escolhas {#single-multiple-choice}

Você pode adicionar até 12 opções em uma pesquisa.

Selecione **Seleção única** ou **Seleção múltipla**. O **Texto auxiliar** será atualizado automaticamente quando você alternar entre as duas opções para informar aos usuários quantas escolhas eles podem selecionar. 

Em seguida, determine se você irá [coletar atributos personalizados](#custom-attributes) ou [registrar apenas respostas](#no-attributes).

![Dropdown de escolhas com "Registrar atributos ao enviar" selecionado.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Coletar atributos personalizados {#custom-attributes}

Selecione **atributos de registro na submissão** para coletar atributos com base na submissão do usuário. Você pode usar esta opção para criar novos segmentos e campanhas de redirecionamento. Por exemplo, em uma [pesquisa de satisfação](#user-satisfaction), você poderia enviar um e-mail de acompanhamento para todos os usuários que não estavam satisfeitos.

Para adicionar um atributo personalizado a cada escolha, selecione um nome de atributo personalizado no menu suspenso (ou crie um novo) e, em seguida, insira o valor a ser definido quando essa escolha for enviada. Você também pode criar um novo atributo personalizado na sua [Página de Configurações]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

O tipo de dado dos seus atributos personalizados importa dependendo de como você configurou sua pesquisa.

- **Seleção de múltipla escolha:** O tipo de dado do atributo personalizado deve ser um array. Se o atributo personalizado estiver definido para um tipo de dado diferente, as respostas não serão registradas.
- **Seleção de escolha única:** O tipo de dado do atributo personalizado deve ser uma string. Atributos personalizados que não são do tipo string não aparecerão no dropdown, e as respostas não serão registradas.

{% alert important %}
Quando a coleta de atributo personalizado está ativada, as escolhas que compartilham o mesmo nome de atributo personalizado serão combinadas em um array.
{% endalert %}

##### Exemplo 

Por exemplo, em uma [pesquisa de preferências de notificação](#notification-preferences), você pode fazer com que cada escolha seja um atributo booleano (verdadeiro/falso) para permitir que os usuários selecionem quais tópicos eles estão interessados. Se um usuário marcar a opção "Promoções", isso atualizará seu [perfil de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) com o atributo personalizado `Promotions Topic` definido como `true`. Se eles deixarem a escolha desmarcada, esse mesmo atributo permanecerá inalterado.

Você pode então usar o `Custom Attribute` filtro para criar um segmento para usuários com o atributo personalizado `Promotions Topic` `is` `true` para garantir que apenas usuários interessados em suas promoções receberão as campanhas relevantes.

#### Registrando apenas respostas {#no-attributes}

Alternativamente, você pode optar por **registrar apenas as respostas (sem atributos)**. Quando esta opção é selecionada, as respostas da pesquisa são registradas como cliques de botão, mas os atributos personalizados não são registrados no perfil do usuário. Isso significa que você ainda pode ver as métricas de cliques para cada opção de pesquisa (veja [análise de dados](#analytics)), mas essa escolha não será refletida no perfil do usuário.

Essas métricas de cliques não estão disponíveis para redirecionamento.

### Etapa 4: Escolha o comportamento de envio

Depois que um usuário enviar sua resposta, você pode opcionalmente mostrar uma página de confirmação ou simplesmente fechar a mensagem.

Uma página de confirmação é um ótimo lugar para agradecer aos usuários pelo seu tempo ou fornecer informações adicionais. Você pode personalizar a chamada para ação nesta página para guiar os usuários para outra página do seu app ou site.

Edite o texto do seu botão e o comportamento ao clicar na seção **Botão de Enviar** na parte inferior da guia **Pesquisa**:

![Comportamento ao clicar definido como "Enviar respostas e exibir página de confirmação".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Se você optar por adicionar uma página de confirmação, mude para a guia **Confirmation Page** para personalizar sua mensagem:

![Guia da Página de Confirmação do editor de pesquisa simples. Os campos disponíveis são cabeçalho, corpo opcional, texto do botão e comportamento ao clicar do botão.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Se você deseja guiar os usuários para outra página do seu app ou site, altere o **comportamento ao clicar** do botão.

### Etapa 5: Estilize sua mensagem (opcional) {#styling}

Você pode personalizar a cor da fonte e a cor de destaque da mensagem usando o seletor de **tema de cores**.

![A guia de composição do editor de pesquisa simples com o seletor de tema de cor expandido após um usuário clicar na paleta de cores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analisar resultados {#analytics}

Depois que sua campanha for lançada, você poderá analisar os resultados em tempo real para ver a divisão de cada escolha selecionada. Se você ativou a [coleta de atributo personalizado](#custom-attributes), também poderá criar novos segmentos ou campanhas de acompanhamento para usuários que responderam à pesquisa.

{% alert note %}
As escolhas de pesquisa excluídas ainda aparecerão na análise de dados, mas não serão mostradas como uma escolha para novos usuários.
{% endalert %}

Você pode encontrar suas métricas de desempenho da pesquisa expandindo o **Resultados** dropdown para uma variante específica na seção **Desempenho de Mensagem no App** da análise de dados. Aqui está uma visão geral do que você verá:

- **O engajamento da pesquisa** mostra como os usuários interagiram com a pesquisa de forma geral, incluindo total de envios, rejeições e cliques dentro do corpo da mensagem.
- **Os resultados da pesquisa** exibem uma divisão de quantos usuários selecionaram cada opção de resposta, junto com a porcentagem do total de envios que cada escolha representa.
- **Métricas da página de confirmação** (se habilitado) incluem quantos usuários visualizaram a tela de confirmação, clicaram em seu botão ou a rejeitaram sem interagir.

Para definições de métricas de pesquisa, consulte o [Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data/report_metrics/) e filtre por "mensagem no app".

Confira [mensagem no app relatórios]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para uma análise detalhada das métricas da sua campanha.

### Currents {#currents}

As escolhas selecionadas serão automaticamente transferidas para Currents, no campo [**Eventos de Clique de Mensagem no App**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id`. Cada escolha será enviada com seu identificador único universal (UUID).

## Casos de uso

{% tabs %}
{% tab User satisfaction %}

### Satisfação do usuário

**Objetivo:** Meça a satisfação do cliente e envie campanhas de recuperar para usuários que deixaram baixas pontuações.

Para configurar isso, use uma pesquisa de seleção de escolha única com cinco opções que variam de “😡 Muito Insatisfeito” a “😍 Muito Satisfeito.” Cada escolha é mapeada para o atributo personalizado `customer_satisfaction`, com um valor numérico de 1 a 5—onde 1 indica o menos satisfeito e 5 o mais satisfeito. Nota que esses valores numéricos são armazenados como strings, pois atributos personalizados do tipo string são necessários para seleção de escolha única.

| Escolha                                | Atributo              | Valor |
|---------------------------------------|------------------------|-------|
| 😡 Muito Insatisfeito                  | `customer_satisfaction` | 1     |
| 😟 Insatisfeito                       | `customer_satisfaction` | 2     |
| 🙂 Nem Satisfeito nem Insatisfeito | `customer_satisfaction` | 3     |
| 😊 Satisfeito                          | `customer_satisfaction` | 4     |
| 😍 Muito Satisfeito                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, seu valor selecionado é registrado como um atributo personalizado. Você pode então construir campanhas de acompanhamento usando filtros de público. Por exemplo, direcione mensagens de recuperação para usuários cujo atributo `customer_satisfaction` é "1" ou "2".

{% endtab %}
{% tab Notification preferences %}

### Preferências de notificação

**Objetivo:** Deixe os usuários optarem por tipos específicos de notificações.

Para configurar isso, use uma pesquisa de seleção de múltiplas escolhas onde cada escolha representa um tópico de notificação. Em vez de atribuir o mesmo atributo com valores diferentes, cada escolha mapeia para um atributo booleano distinto que reflete o interesse do usuário naquele tópico. Se um usuário selecionar uma escolha, o atributo correspondente é definido como `true`. Se não for selecionado, o atributo permanece inalterado.

| Escolha             | Atributo              | Valor  |
|--------------------|------------------------|--------|
| Atualizações de Produto    | `wants_product_updates`| `true` |
| Promoções         | `wants_promotions`     | `true` |
| Convites para Eventos      | `wants_event_invites`  | `true` |
| Pesquisas & Feedback | `wants_surveys`        | `true` |
| Dicas & Tutoriais   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Identificar metas do cliente

**Objetivo:** Identifique os principais motivos pelos quais os usuários visitam seu app.

Para configurar isso, use uma pesquisa de seleção de escolha única com cada opção representando um objetivo ou intenção comum. Cada escolha é mapeada para o atributo personalizado `product_goal` com um valor correspondente à intenção do usuário selecionada.

| Escolha                     | Atributo       | Valor     |
|----------------------------|------------------|-----------|
| Verificando status            | `product_goal`   | `status`  |
| Atualizando minha conta       | `product_goal`   | `upgrade` |
| Agendando uma consulta  | `product_goal`   | `schedule`|
| Suporte ao cliente           | `product_goal`   | `support` |
| Apenas navegando              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, o valor selecionado é registrado como um atributo personalizado em seu perfil. Você pode então usar esses dados para personalizar experiências futuras ou segmentar usuários com base em seu objetivo principal.

{% endtab %}
{% tab Improve conversion rates %}

### Melhore as taxas de conversão

**Objetivo:** Entenda por que os clientes não estão atualizando ou comprando.

Para configurar isso, use uma pesquisa de seleção de escolha única com cada opção representando uma barreira comum à atualização. Cada escolha é mapeada para o atributo personalizado `upgrade_reason` com um valor correspondente que reflete a seleção do usuário.

| Escolha              | Atributo        | Valor       |
|---------------------|------------------|-------------|
| Muito caro       | `upgrade_reason` | `expensive` |
| Não valioso        | `upgrade_reason` | `value`     |
| Difícil de usar    | `upgrade_reason` | `difficult` |
| Usando um concorrente  | `upgrade_reason` | `competitor`|
| Outro Motivo        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário envia a pesquisa, o valor selecionado é salvo em seu perfil. Você pode então direcionar esses usuários com campanhas adaptadas à sua objeção específica, como ofertas de desconto ou melhorias de usabilidade.

{% endtab %}
{% tab Favorite features %}

### Recursos favoritos

**Objetivo:** Compreenda quais recursos os clientes gostam de usar.

Para configurar isso, use uma pesquisa de seleção de múltipla escolha onde cada opção representa um recurso do seu app. Cada escolha é mapeada para o atributo personalizado `favorite_features`, e quando o usuário envia a pesquisa, o atributo é definido como um array dos valores selecionados.

| Escolha            | Atributo          | Valor        |
|-------------------|--------------------|--------------|
| Marcadores         | `favorite_features`| `bookmarks`  |
| App Móvel        | `favorite_features`| `mobile`     |
| Compartilhando Postagens     | `favorite_features`| `sharing`    |
| Suporte ao Cliente  | `favorite_features`| `support`    |
| Personalização     | `favorite_features`| `custom`     |
| Preço / Valor     | `favorite_features`| `value`      |
| Comunidade         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Porque esta pesquisa usa seleção de múltipla escolha, o perfil do usuário será atualizado com uma lista de todos os valores de recurso selecionados.

{% endtab %}
{% endtabs %}
