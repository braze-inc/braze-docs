---
nav_title: Conexão de várias lojas
article_title: Suporte a várias lojas da Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "Este artigo de referência aborda como conectar e configurar várias lojas da Shopify em um único espaço de trabalho."
---

# Conecte várias lojas da Shopify

> Conecte vários domínios de lojas da Shopify a um único espaço de trabalho para ter uma visão holística de seus clientes em todos os mercados. Crie e lance programas e jornadas de automação em um único espaço de trabalho sem duplicar esforços em lojas regionais.  

{% alert important %}
Esse recurso não é compatível com o Shopify Markets ou o Markets Pro. Se você quiser solicitar suporte para eles, envie uma [solicitação de produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Solicitações

| Requisito | Descrição |
| ----------- | ----------- |
| Ativar várias lojas | Entre em contato com o gerente de sucesso do cliente para ativar o suporte a várias lojas da Shopify. |
| Configurar uma loja da Shopify | Certifique-se de que você já tenha configurado [pelo menos uma loja Shopify com o Braze]({{site.baseurl}}/shopify_overview/). |
| Domínios exclusivos de vitrines da Shopify para cada região | O suporte a várias lojas destina-se ao uso com domínios de loja exclusivos da Shopify para diferentes vitrines regionais. <br><br>Se você quiser conectar várias submarcas ao Braze, recomendamos a criação de espaços de trabalho separados para cada submarca. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conexão de uma loja adicional
Depois de instalar o app Braze em sua loja Shopify e instalar sua primeira loja, selecione **\+ Conectar nova loja**.

![O botão "+ Connect New Store" (+ Conectar nova loja) na página de integração do Shopify.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Para sua loja regional adicional da Shopify, selecione **Begin setup (Iniciar configuração)**.

![A seção "Integration settings" (Configurações de integração) com um botão para "Begin setup" (Iniciar configuração).]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Como em sua primeira integração com a loja do Shopify, você pode escolher entre uma configuração padrão ou personalizada.

![Seção "Ativar os SDKs do Braze" com opções para implementar o SDK do Braze Web com a configuração padrão ou personalizada.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Escolha a opção que melhor atenda às suas necessidades:

{% multi_lang_include shopify.md section='Integration Tabs' %}

Para visualizar a integração de cada loja e definir configurações avançadas, selecione uma loja no menu suspenso.

!["Configurações de integração" com um menu suspenso para selecionar uma loja do Shopify.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Sincronização de usuários entre lojas

### Alias do Shopify

Quando você conecta várias lojas, os usuários sincronizados do Shopify que registraram ou fizeram um pedido receberão um novo alias no formato: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### ID externa do Braze

Você pode escolher entre as seguintes opções para sua ID externa Braze:

|Opção|Descrição|
|------|-----------|
|ID de cliente da Shopify|Se você usar o ID de cliente do Shopify como seu ID externo do Braze, cada loja gerará um ID de cliente exclusivo para cada usuário. Isso significa que, se um usuário interagir com várias lojas, ele terá perfis separados no Braze.|
|E-mail, e-mail com hash ou ID externa personalizada|Se você usar os tipos de e-mail, e-mail com hash ou ID externo personalizado, os usuários que se engajarem em várias lojas terão seus perfis mesclados em um único perfil consolidado quando registrarem ou fizerem um pedido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campos mesclados

Quando um perfil de usuário é sincronizado, os seguintes campos são mesclados. Para obter detalhes completos sobre o comportamento de mesclagem, consulte [Comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Informações sobre o dispositivo
- Contagem total de sessões (combinada de ambos os perfis)
- Dados personalizados de eventos e compras
- Propriedades de eventos personalizados para segmentação (por exemplo, "X vezes em Y dias" onde X ≤ 50 e Y ≤ 30)
- Contagem de eventos (combinada de ambos os perfis)
- Datas do primeiro e último eventos (o Braze seleciona as datas mais antigas e mais recentes)
- Dados de interação da campanha (campos de data mais recentes)
- Resumos do fluxo de trabalho (campos de data mais recentes)
- Histórico de mensagens e engajamento
- Grupos de inscrições

### Coleta de assinantes (opcional)

Você pode optar por coletar assinantes diretamente pelo Braze (nas configurações do seu conector Shopify) ou por meio de alternativas de API e SDK que sincronizam dados do Shopify.

{% tabs local %}
{% tab Shopify connector %}
Na etapa **Gerenciar usuários** das configurações do seu conector Shopify, é possível usar o Braze para coletar envios de e-mail e aceitação de assinantes por SMS e organizá-los em um grupo de inscrições dedicado:

1. Crie um grupo de inscrições exclusivo para cada loja que você conectar. Isso o ajuda a manter dados precisos sobre a origem dos assinantes.
2. Ativar a coleta de assinantes de e-mail e SMS.
{% endtab %}

{% tab Braze API or SDKs %}
Como alternativa, você pode sincronizar as informações de aceitação de marketing por e-mail e SMS diretamente do Shopify usando a API ou os SDKs do Braze.

|Opção|Recursos|
|------|---------|
|API |- [Pontos de extremidade do grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) para substituir diretamente o que é suportado pela integração<br>- [Ponto de extremidade`Users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) para definir os dados do grupo de inscrições ou o [estado da inscrição global de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Central de Preferências do Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) para opções de coleta de aceitação de marketing mais personalizadas|
|SDKs |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Dados da Shopify 

### Atribuições sincronizadas

Quando você conecta mais de uma loja, as seguintes atribuições serão sincronizadas com o estado mais recente do perfil da Shopify:
- Nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- País
- Cidade
- Último uso do app
- Idioma
- Fuso horário
- Tags da Shopify
- Contagem de pedidos da Shopify
- Total de gastos da Shopify

### Eventos apoiados

#### Eventos recomendados para comércio eletrônico 

Quando você conecta várias lojas, os eventos recomendados de comércio eletrônico recebidos incluirão uma propriedade de evento de origem. Essa propriedade identifica de qual URL da loja o evento se originou, permitindo que você use essas informações para segmentação ou para disparar casos de uso específicos.

![Um Canva baseado em ação com um disparador para inserir usuários que realizam o evento personalizado `ecommerce.order_placed`.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Os eventos recomendados de comércio eletrônico compatíveis na integração com a Shopify são:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Eventos personalizados da Shopify 

Os eventos personalizados do Shopify que chegam incluem uma propriedade de evento chamada `shopify_storefront`. Essa propriedade indica de qual URL da loja o evento veio, permitindo que você a utilize para segmentação ou dispare casos de uso.

![Um Canva baseado em ação com um disparador para inserir usuários que realizam o evento personalizado `shopify_paid_order`.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Os eventos personalizados da Shopify compatíveis incluem:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Para obter uma visão geral completa de todas as cargas úteis de eventos, consulte [os recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features/).

### Sincronização de produtos do Shopify 

Ao conectar e configurar cada loja Shopify no Braze, você pode, opcionalmente, ativar a sincronização de produtos Shopify como parte da integração.

Se você ativar a sincronização de produtos para cada loja, o Braze incluirá o nome de sua loja Shopify no nome do catálogo. Isso distingue os produtos de diferentes lojas.

![Catálogos da Shopify com sua loja da Shopify em seu nome.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

