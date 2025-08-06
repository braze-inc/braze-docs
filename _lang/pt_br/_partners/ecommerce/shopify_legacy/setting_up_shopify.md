---
nav_title: Como configurar a Shopify
article_title: "Como configurar a Shopify"
description: "Este artigo de referência descreve como configurar a Shopify após integrá-la ao seu SDK para Web da Braze."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Configurando Shopify no Braze

> Este artigo descreve como concluir a configuração da integração da Shopify com a Braze. Siga estas instruções após [implementar o SDK para Web da Braze]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) no seu site da Shopify.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Configuração de integração do Shopify no Braze

### Etapa 1: Conecte sua loja da Shopify

Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e depois procure "Shopify".

{% alert note %}
Se você estiver usando a navegação antiga, poderá encontrar **Parceiros de Tecnologia** em **Integrações**.
{% endalert %}

Na página de parceiros da Shopify, selecione **Acessar Shopify App Store** para iniciar o processo de integração.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

Você será direcionado para a Shopify App Store para instalar o app da Braze.

{% alert note %}
Se a sua conta do Shopify estiver associada a mais de uma loja, você pode alternar a loja em que está logado selecionando o ícone da loja no canto superior direito da página e selecionando **Alternar lojas**.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

Depois de selecionar sua loja de escolha, selecione **Install** (Instalar) na página do app da Braze. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Depois de instalar o app da Braze, você acessará automaticamente a Braze para confirmar o espaço de trabalho que deseja conectar à Shopify. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

Depois de confirmar que você está no espaço de trabalho correto, você pode concluir a configuração da sua integração com o Shopify selecionando **Iniciar configuração**.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
Você só pode conectar uma loja por espaço de trabalho neste momento. Se você tiver várias lojas Shopify que gostaria de conectar ao seu espaço de trabalho, entre em contato com seu gerente de sucesso do cliente para obter detalhes sobre o beta de várias lojas do Shopify.
{% endalert %}

### Etapa 2: selecione eventos e preenchimento histórico

Depois de conectar sua loja Shopify, prossiga para a etapa 2 e selecione os eventos a serem incluídos como parte de sua integração. Você deve selecionar pelo menos um evento.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

A seleção dos eventos **Product Viewed** (Produto visualizado), **Product Clicked** (Produto clicado) ou **Abandoned Cart** (Carrinho abandonado) exige o SDK para Web da Braze para rastreamento. Se você implementar o Braze Web SDK através do [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) ou diretamente no site do seu Shopify [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features), o Braze gerará automaticamente os scripts de rastreamento e os carregará em seu site. Se você implementar o SDK para Web no seu [site headless da Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), ative manualmente o rastreamento desses eventos. 

#### Preencher dados históricos (opcional)

Você pode opcionalmente ativar um preenchimento retroativo de compras dos últimos 90 dias antes da sua instalação. Ao sincronizar de modo automático os dados de clientes e compras anteriores, você pode começar imediatamente o direcionamento e o engajamento com seus clientes. Para saber mais, confira o preenchimento histórico da Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Para o preenchimento retroativo importar Eventos de Pedido Criado e Eventos de Compra do Braze, você deve ter selecionado **Pedido Criado** e **Evento de Compra do Braze** para incluir como parte da sua integração.
{% endalert %}

### Etapa 3: Coletar assinantes (opcional)

Usando a integração da Shopify, você pode coletar assinantes de e-mail e SMS da sua loja da Shopify para a Braze. Para saber mais, consulte [Como sincronizar assinantes da Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Etapa 4: Configurar sincronizações de produtos do Shopify (opcional)

Você pode opcionalmente sincronizar seus produtos em quase tempo real da sua loja Shopify para um catálogo Braze, automatizando o processo para trazer dados de produtos para uma personalização mais profunda de suas mensagens. Para saber mais, confira [sincronizações de produtos do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Etapa 5: ativar envio de mensagens no navegador 

Você pode opcionalmente usar um canal adicional na sua loja Shopify para mensagens no navegador ativando este recurso. Isso permite que você use nossos tipos básicos de mensagem, como slide-up, modal, tela cheia, pesquisas simples e HTML personalizado.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

Se você ativar mensagens no navegador, será necessário implementar o SDK para Web da Braze para rastreamento. Se você implementar o Braze Web SDK através do [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) ou diretamente no site do seu Shopify [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features), o Braze gerará automaticamente o script básico de implementação de mensagem no navegador no seu site. Se você implementar o Web SDK no seu [site Shopify headless]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) ou planejar adicionar personalizações às mensagens no navegador, você deve adicionar manualmente as mensagens no navegador ao seu site usando nosso [guia do desenvolvedor]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web). 

### Etapa 6: Concluir configuração

Depois de fazer as configurações, selecione **Finish Setup** (Concluir configuração).

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

É isso! O status “Conexão Pendente” será atualizado para “Conectado” e exibirá o carimbo de data/hora de quando a conexão foi estabelecida. Você também verá se cada recurso do Shopify foi ativado com sucesso na página. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Configurações Avançadas (opcional) 

#### Atualizar atrasos de carrinho abandonado e checkout abandonado

Por padrão, a Braze define automaticamente a postergação para disparar os eventos `shopify_abandoned_checkout` e `shopify_abandoned_cart` para uma hora de inatividade. Você pode definir a **Postergação de Carrinho Abandonado** e a **Postergação de Checkout Abandonado** para cada evento de 5 minutos até 24 horas selecionando o menu suspenso e, em seguida, selecionando **Definir Postergação** na página de parceiros do Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Defina seu identificador de produto preferido

Se você incluiu eventos de compra da Braze na configuração da sua integração com a Shopify, por padrão, a Braze definirá o ID do produto da Shopify como o `product_id` usado no evento de compra da Braze. Isso será usado quando você filtrar produtos comprados em Y dias ou personalizar o conteúdo da sua mensagem usando Liquid.

Você também pode optar por definir o SKU ou o título do produto da Shopify em vez do ID do produto da Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Solução de problemas

{% details Por que a instalação do meu app Shopify ainda está pendente? %}
Sua instalação ainda pode estar pendente por um dos seguintes motivos:
 - Quando a Braze está configurando seus webhooks do Shopify
 - Quando a Braze está se comunicando com a Shopify


Se a instalação do seu app ficar pendente por 1 hora, a Braze falhará na instalação, e você verá uma opção para tentar a configuração novamente.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Por que a instalação do meu app do Shopify falhou? %}
Sua instalação pode ter falhado por um dos seguintes motivos:
 - Braze não conseguiu alcançar Shopify
 - Braze falhou ao processar a solicitação
 - Seu token de acesso do Shopify é inválido
 - O app Braze Shopify foi excluído da sua página de administração do Shopify


Se isso acontecer, você poderá selecionar **Repetir Configuração** e iniciar o processo de instalação novamente.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Como desinstalo o aplicativo Braze da minha loja Shopify? %}

Existem duas maneiras de desinstalar a Braze da sua loja da Shopify:

1. Na página de parceiros da Shopify, selecione **Desconectar**.<br><br> ![A seção "Desconectar Integração" com um link para desconectar.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Acessar sua página de administração do Shopify localizada em **Apps**. Em seguida, você verá uma opção para excluir o aplicativo da Braze.<br><br> ![Um modal pedindo confirmação se você gostaria de deletar o app Braze.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details Estou tendo dificuldades para reconciliar meus usuários. Qual pode ser a razão? %}

O tipo de suporte necessário para a reconciliação do usuário é determinado por como você implementou o SDK para Web. Para saber mais, consulte [Primeiros passos com a Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/). 

- Se você estiver em um site headless da Shopify, confira a [implementação headless]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) para confirmar se você ativou a reconciliação do usuário no checkout.
- Se você estiver encontrando perfis de usuário duplicados com o mesmo e-mail ou número de telefone, você pode usar as seguintes ferramentas do Braze para mesclar os duplicados em um único perfil: 
    - endpoint [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
    - [Mesclagem em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- Se você usar a integração ScriptTag, e sua loja Shopify oferecer uma opção "Comprar Agora" que pula o carrinho, o Braze pode ter dificuldades para reconciliar os usuários, pois o Shopify não permite que as tags de script recuperem um `device_id` para mapear os eventos para um usuário que pula o carrinho.

{% enddetails %}
