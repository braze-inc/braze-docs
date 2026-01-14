---
nav_title: Conectando Múltiplas Lojas
article_title: Suporte a Múltiplas Lojas Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "Este artigo de referência cobre como conectar e configurar várias lojas Shopify a um único espaço de trabalho."
---

# Conectando várias lojas Shopify

> Conecte vários domínios de lojas Shopify a um único espaço de trabalho para ter uma visão holística de seus clientes em todos os mercados. Crie e lance programas de automação e jornadas em um único espaço de trabalho sem duplicar esforços entre lojas regionais.  

{% alert important %}
Este recurso não suporta Shopify Markets ou Markets Pro. Se você gostaria de solicitar suporte para esses, envie uma [solicitação de produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Solicitações

| Requisito | Descrição |
| ----------- | ----------- |
| Ativar múltiplas lojas | Entre em contato com seu gerente de sucesso do cliente para ativar o suporte a múltiplas lojas Shopify. |
| Configurar uma loja Shopify | Certifique-se de que você já [configurou pelo menos uma loja Shopify com Braze]({{site.baseurl}}/shopify_overview/). |
| Domínios exclusivos de vitrine Shopify para cada região | O suporte a múltiplas lojas é destinado ao uso com domínios de loja Shopify exclusivos para diferentes vitrines regionais. <br><br>Se você deseja conectar várias sub-marcas ao Braze, recomendamos criar espaços de trabalho separados para cada sub-marca. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conectando uma loja adicional
Depois de instalar o aplicativo Braze em sua loja Shopify e instalar sua primeira loja, selecione **\+ Conectar Nova Loja**.

![O botão "+ Conectar Nova Loja" na página de integração do Shopify.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Para sua loja regional Shopify adicional, selecione **Iniciar configuração**.

![A seção "Configurações de integração" com um botão para "Iniciar configuração".]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Assim como na sua primeira integração com a Shopify, você pode escolher entre uma configuração padrão ou personalizada.

!["Ativar a seção do SDK da Braze" com opções para implementar o SDK Web da Braze com a configuração padrão ou personalizada.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Escolha a opção que melhor atende às suas necessidades:

{% multi_lang_include shopify.md section='Integration Tabs' %}

Para visualizar cada integração de loja e configurar as configurações avançadas, selecione uma loja no menu suspenso.

!["Configurações de integração" com um menu suspenso para selecionar uma loja Shopify.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Sincronizando usuários entre lojas

### Alias do Shopify

Quando você conecta várias lojas, os usuários sincronizados da Shopify que fizeram login ou realizaram um pedido receberão um novo alias no formato: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### ID externo da Braze

Você pode escolher entre as seguintes opções para seu ID externo da Braze:

|Opção|Descrição|
|------|-----------|
|ID de cliente da Shopify|Se você usar o ID do cliente da Shopify como seu ID externo da Braze, cada loja gerará um ID de cliente exclusivo para cada usuário. Isso significa que, se um usuário interagir com várias lojas, ele terá perfis separados na Braze.|
|E-mail, E-mail Hash, ou ID Externo Personalizado|Se você usar os tipos de e-mail, e-mail hash ou ID externo personalizado, os usuários que interagem com várias lojas terão seus perfis mesclados em um único perfil consolidado quando fizerem login ou realizarem um pedido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campos mesclados

Quando um perfil de usuário é sincronizado, os seguintes campos serão mesclados. Para detalhes completos sobre o comportamento de mesclagem, consulte [Comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Informações sobre o dispositivo
- Contagem total de sessões (combinada de ambos os perfis)
- Dados de evento personalizado e compra
- Propriedades de evento personalizado para segmentação (por exemplo, “X vezes em Y dias” onde X ≤ 50 e Y ≤ 30)
- Contagem de eventos (combinada de ambos os perfis)
- Datas dos primeiros e últimos eventos (Braze seleciona as datas mais antigas e mais recentes)
- Dados de interação da campanha (campos de data mais recentes)
- Resumos de fluxo de trabalho (campos de data mais recentes)
- Histórico de mensagens e engajamento
- Grupos de inscrições

### Coletando assinantes (opcional)

Você pode optar por coletar assinantes diretamente através do Braze (nas configurações do conector Shopify) ou através de alternativas de API e SDK que sincronizam dados do Shopify.

{% tabs local %}
{% tab Conector Shopify %}
Na etapa **Gerenciar usuários** das configurações do seu conector Shopify, você pode usar o Braze para coletar opt-ins de assinantes de e-mail e SMS e organizá-los em um grupo de inscrições dedicado:

1. Crie um grupo de inscrições exclusivo para cada loja que você conectar. Isso ajuda você a manter dados precisos sobre de onde os assinantes estão vindo.
2. Ative a coleta de assinantes de e-mail e SMS.
{% endtab %}

{% tab API ou SDKs do Braze %}
Alternativamente, você pode sincronizar informações de opt-in de marketing por e-mail e SMS diretamente do Shopify usando a API ou SDKs do Braze.

|Opção|Recursos|
|------|---------|
|API |- [Pontos finais do grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) para substituir diretamente o que é suportado pela integração<br>- [`Users/track` ponto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) para definir dados do grupo de inscrições ou o [estado global de inscrição por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Central de Preferências do Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) para opções de coleta de opt-in de marketing mais personalizadas|
|SDKs |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Dados da Shopify 

### Atributos sincronizados

Quando você conecta mais de uma loja, os seguintes atributos serão sincronizados com o estado mais recente do perfil do Shopify:
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
- Tags do Shopify
- Contagem de pedidos da Shopify
- Total de gastos da Shopify

### Eventos suportados

#### Eventos recomendados de eCommerce 

Quando você conecta várias lojas, os eventos recomendados de eCommerce recebidos incluirão uma propriedade de evento de origem. Essa propriedade identifica de qual URL de loja o evento se originou, permitindo que você use essas informações para segmentação ou disparar casos de uso específicos.

![Uma Canvas baseada em ação com um disparador para entrar usuários que realizam o evento personalizado `ecommerce.order_placed`.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Os eventos recomendados de eCommerce suportados dentro da integração do Shopify são:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Eventos personalizados da Shopify 

Os eventos personalizados recebidos do Shopify incluem uma propriedade de evento chamada `shopify_storefront`. Essa propriedade indica de qual URL de loja o evento veio, permitindo que você a utilize para segmentação ou disparar casos de uso.

![Uma Canvas baseada em ação com um disparador para entrar usuários que realizam o evento personalizado `shopify_paid_order`.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Os eventos personalizados suportados do Shopify incluem:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Para uma visão completa de todos os payloads de eventos, consulte [recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features/).

### Sincronização de produtos do Shopify 

Quando você conecta e configura cada loja Shopify no Braze, você pode opcionalmente ativar a sincronização de produtos do Shopify como parte da integração.

Se você ativar a sincronização de produtos para cada loja, o Braze incluirá o nome da sua loja Shopify no nome do catálogo. Isso ajuda você a distinguir produtos de diferentes lojas.

![Catálogos do Shopify com sua loja Shopify no nome.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

