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

Ao criar uma [mensagem no app][1], selecione **Pesquisa Simples** para o seu **Tipo de Mensagem**.

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

Este modelo de pesquisa é compatível com aplicativos móveis e navegadores da web. Lembre-se de verificar se seus SDKs estão nas [versões mínimas de SDK](#supported-sdk-versions) necessárias para este recurso.

### Etapa 1: Adicione sua pergunta da pesquisa

Para começar a construir sua pesquisa, adicione sua pergunta ao campo **Header** da pesquisa. Se desejar, você pode adicionar uma mensagem opcional **Body** que aparecerá sob sua pergunta da pesquisa.

![Guia de composição do editor de pesquisa simples, com campos para um cabeçalho, corpo opcional e texto auxiliar opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
Esses campos podem incluir tanto Liquid quanto emojis, então seja criativo!
{% endalert %}

### Etapa 2: Escolha entre única ou múltipla escolha {#single-multiple-choice}

Use **Seleção de escolha única** ou **Seleção de múltipla escolha** para controlar se um usuário pode selecionar apenas uma escolha ou várias escolhas. Você pode adicionar até 12 opções em uma pesquisa.

![Menu suspenso de escolhas com "Seleção de múltipla escolha" selecionada.]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
Seu **texto de ajuda** será atualizado automaticamente quando você alternar entre **seleção de escolha única** e **seleção de múltipla escolha** para informar aos usuários quantas escolhas eles podem selecionar.
{% endalert %}

### Etapa 3: Coletar atributos personalizados {#custom-attributes}

Selecione **atributos de registro na submissão** para coletar atributos com base na submissão do usuário. Você pode usar esta opção para criar novos segmentos e campanhas de redirecionamento. Por exemplo, em uma pesquisa de satisfação, você poderia enviar um e-mail de acompanhamento para todos os usuários que não estavam satisfeitos.

![Opções suspensas com "registro de atributos ao enviar" selecionado.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

Para adicionar um atributo personalizado a cada escolha, selecione um nome de atributo personalizado no menu suspenso (ou crie um novo) e, em seguida, insira o valor a ser definido quando essa escolha for enviada. Você pode criar um novo atributo personalizado na sua [Página de Configurações][5].

Por exemplo, em uma pesquisa de preferências de notificação, você pode fazer de cada escolha um atributo booleano (verdadeiro/falso) para permitir que os usuários selecionem quais tópicos lhes interessam. Se um usuário marcar a opção "Promoções", isso atualizará seu [perfil de usuário][3] com o atributo personalizado `Promotions Topic` definido como `true`. Se eles deixarem a escolha desmarcada, esse mesmo atributo permanecerá inalterado.

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

Você pode então criar um segmento para usuários com `Promotions Topic = true` para garantir que apenas os usuários interessados em suas promoções receberão as campanhas relevantes.

{% alert important %}
Quando a coleta de atributo personalizado está ativada, as escolhas que compartilham o mesmo nome de atributo personalizado serão combinadas em um array.
{% endalert %}

#### Tipos de dados de atributo personalizado

O tipo de dado dos seus atributos personalizados importa dependendo de como você configurou sua pesquisa.

- **Seleção de múltipla escolha:** O tipo de dado do atributo personalizado deve ser um array. Se o atributo personalizado estiver definido para um tipo de dado diferente, as respostas não serão registradas.
- **Seleção de escolha única:** O tipo de dado do atributo personalizado _não deve_ ser um array. As respostas não serão registradas se o atributo for um array.

#### Registrando apenas respostas

Alternativamente, você pode optar por **registrar apenas as respostas (sem atributos)**. Quando esta opção é selecionada, as respostas da pesquisa são registradas como cliques de botão, mas os atributos personalizados não são registrados no perfil do usuário. Isso significa que você ainda pode ver as métricas de cliques para cada opção de pesquisa (veja [análise de dados](#analytics)), mas essa escolha não será refletida no perfil do usuário.

Essas métricas de cliques não estão disponíveis para redirecionamento.

### Etapa 4: Escolha o comportamento de envio

Depois que um usuário enviar sua resposta, você pode opcionalmente mostrar uma página de confirmação ou simplesmente fechar a mensagem.

Uma página de confirmação é um ótimo lugar para agradecer aos usuários pelo seu tempo ou fornecer informações adicionais. Você pode personalizar o Call To Action nesta página para guiar os usuários para outra página do seu app ou site.

Edite o texto do seu botão e o comportamento ao clicar na seção **Botão de Enviar** na parte inferior da guia **Pesquisa**:

![Comportamento ao clicar definido como "Enviar respostas e exibir página de confirmação".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Se você optar por adicionar uma página de confirmação, mude para a guia **Confirmation Page** para personalizar sua mensagem:

![Guia da Página de Confirmação do editor de pesquisa simples. Os campos disponíveis são cabeçalho, corpo opcional, texto do botão e comportamento ao clicar do botão.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

Se você deseja guiar os usuários para outra página do seu app ou site, altere o **comportamento ao clicar** do botão.

### Etapa 5: Estilize sua mensagem (opcional) {#styling}

Você pode personalizar a cor da fonte e a cor de destaque da mensagem usando o seletor de **tema de cores**.

![Guia de composição do editor de pesquisa simples com o seletor de tema de cores expandido após um usuário ter clicado na paleta de cores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analisar resultados {#analytics}

Depois que sua campanha for lançada, você poderá analisar os resultados em tempo real para ver a divisão de cada escolha selecionada. Se você ativou a [coleta de atributo personalizado](#custom-attributes), também poderá criar novos segmentos ou campanhas de acompanhamento para usuários que responderam à pesquisa.

{% alert note %}
As escolhas de pesquisa excluídas ainda aparecerão na análise de dados, mas não serão mostradas como uma escolha para novos usuários.
{% endalert %}

Para definições de métricas de pesquisa, consulte o [Glossário de Métricas de Relatório][11] e filtre por "mensagem no app".

![Painel de performance de mensagem no app com análise de dados de cliques para cada escolha e botão na pesquisa.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

Confira [mensagem no app relatórios][4] para uma análise detalhada das métricas da sua campanha.

### Currents {#currents}

As escolhas selecionadas serão automaticamente transferidas para Currents, no campo [**Eventos de Clique de Mensagem no App**][6] `button_id`. Cada escolha será enviada com seu identificador único universal (UUID).

## Casos de uso

### Satisfação do usuário

**Objetivo:** Meça a satisfação do cliente e envie campanhas de recuperar para usuários que deixaram baixas pontuações.

Para este caso de uso, use a seleção de escolha única, com opções variando de "Muito Insatisfeito" a "Muito Satisfeito". Cada escolha tem o atributo personalizado `customer_satisfaction` definido para um número de 1 a 5, sendo 1 o menos satisfeito e 5 o mais satisfeito.

Depois de lançar sua pesquisa, você pode direcionar suas campanhas de recuperar para usuários que relataram estar "Muito Insatisfeitos" ou "Insatisfeitos", que são usuários com `customer_satisfaction` definido como 1 ou 2.

![][7]

### Identificar metas do cliente

**Objetivo:** Identifique os principais motivos pelos quais os usuários visitam seu app.

Para este caso de uso, use a seleção de escolha única, com cada escolha sendo um motivo comum pelo qual um usuário pode estar visitando seu app. Cada escolha tem o atributo personalizado `product_goal` definido para o tópico do caso de uso. 

Por exemplo, se o usuário selecionar "Atualizando minha conta", isso definirá `product_goal = upgrade` no perfil do usuário.

![][8]

### Melhore as taxas de conversão

**Objetivo:** Entenda por que os clientes não estão atualizando ou comprando.

Para este caso de uso, use a seleção de escolha única, com cada escolha sendo um motivo comum pelo qual um usuário pode não fazer upgrade para uma conta premium. Cada escolha tem o atributo personalizado `upgrade_reason` definido para a seleção do usuário. 

Por exemplo, se o usuário selecionar "Muito Caro", isso definirá `upgrade_reason = expensive` no perfil do usuário. Você pode direcionar esses usuários para campanhas promocionais como descontos ou testes gratuitos.

![][9]

### Recursos favoritos

**Objetivo:** Compreenda quais recursos os clientes gostam de usar.

Para este caso de uso, use a seleção de múltipla escolha com cada escolha sendo um recurso do app. Cada escolha tem o atributo personalizado `favorite_features` definido para a seleção do usuário. Como este caso de uso envolve múltipla escolha, após o usuário concluir a pesquisa, seu perfil será atualizado com o atributo `favorite_features` definido como uma matriz de todas as opções selecionadas.

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
