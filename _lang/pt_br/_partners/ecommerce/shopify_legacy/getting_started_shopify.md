---
nav_title: Como começar
article_title: "Introdução ao Shopify"
description: "Este artigo de referência descreve como implementar o SDK da Braze para Web no seu site da Shopify."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Introdução ao Shopify

> Este artigo descreve como implementar o SDK da Braze para Web no seu site da Shopify. Após a implementação, veja [Configurando o Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview) para aprender como finalizar a configuração da integração do Shopify com o Braze.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Lista de verificação de configuração de integração

1. [Implemente o SDK da Braze para Web](#implement-web-sdk)
2. [Configure o Shopify no Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)
3. Teste a integração do Shopify

## Como implementar o SDK para Web no seu site da Shopify {#implement-web-sdk}

O [SDK Web da Braze]({{site.baseurl}}/user_guide/getting_started/web_sdk/) é uma ferramenta poderosa usada para rastrear o comportamento dos clientes da sua loja Shopify. Com o SDK para Web, você pode coletar dados de sessão, identificar usuários e registrar dados de comportamento do usuário a partir de um navegador Web ou móvel. Você também pode desbloquear canais nativos de envio de mensagens, como mensagens no navegador.

Embora a integração do Shopify ofereça um conjunto robusto de recursos padrão, lembre-se de que, se você tiver casos de uso para adicionar rastreamento no local para [eventos não suportados pela integração do Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/) ou quiser adicionar canais como [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), você precisará implementar o Web SDK diretamente no seu site Shopify.

Antes de iniciar a integração, revise os seguintes itens com sua equipe para definir qual caminho você deseja seguir para implementar o SDK para Web.

### Recursos suportados

|Ícone| Definição 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Suportado"></i><span class="sr-only">Suportado</span> | Suportado
|<i aria-hidden="true" class="fas fa-times" title="Não suportado"></i><span class="sr-only">Suportado</span> | Não suportado
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Recursos | SDK da Web via Shopify ScriptTag | Integração direta de SDK via theme.liquid | integração direta de SDK da web via Shopify Hydrogen
|-------------|-------------|-------------|------------
| Rastreamento padrão no local      | <i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-times" title="Não suportado"></i> | <i class="fas fa-times" title="Não suportado"></i>          
| Captura de reconciliação do usuário (requer pouco esforço de engenharia)   | <i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-times" title="Não suportado"></i> 
| Reconciliação do usuário de checkout     | <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-times" title="Não suportado"></i>   | <i class="fas fa-times" title="Não suportado"></i>                                        
| Produto visualizado<br> Produto clicado<br> Carrinho abandonado   | <i class="fas fa-check" title="Suportado"></i> |<i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-times" title="Não suportado"></i> 
| Checkout abandonado<br> Pedido criado<br> Compra da Braze<br> Pedido pago<br> Pedido parcialmente atendido<br> Pedido processado<br> Pedido cancelado<br> Reembolso criado<br> Cliente criar e atualizar | <i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-check" title="Suportado"></i> | <i class="fas fa-check" title="Suportado"></i>
| Provisionamento de dados históricos | <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-check" title="Suportado"></i>  
| Sincronização de catálogo  |<i class="fas fa-check" title="Suportado"></i> |<i class="fas fa-check" title="Suportado"></i>  |<i class="fas fa-check" title="Suportado"></i>
| Coleta de inscritos de e-mail e SMS    | <i class="fas fa-check" title="Suportado"></i>| <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-check" title="Suportado"></i>     
| Suporte padrão para mensagem no app   | <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-check" title="Suportado"></i>  | <i class="fas fa-times" title="Não suportado"></i>     
| Cartões de conteúdo padrão suportam   | <i class="fas fa-times" title="Não suportado"></i> | <i class="fas fa-times" title="Não suportado"></i> | <i class="fas fa-times" title="Não suportado"></i>   
| Suporte padrão para web push     | <i class="fas fa-times" title="Não suportado"></i> | <i class="fas fa-times" title="Não suportado"></i> | <i class="fas fa-times" title="Não suportado"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Como implementar o SDK para Web da Braze via Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) é um código JavaScript remoto carregado nas páginas da sua loja ou na página de status do pedido do checkout. Quando uma página da loja é carregada, o Shopify verificará se há tags de script que precisam ser carregadas na página do site. 

Caso queira começar a usar a Braze em pouco tempo, você tem a opção de permitir que a Braze carregue um script predefinido do SDK para Web da Braze diretamente no site da sua loja da Shopify.

{% alert important %}
O script predefinido para o Braze Web SDK para este método de integração não é personalizável.
{% endalert %}

#### Como funciona com a integração do Shopify

Quando seu site Shopify for carregado, o Shopify verificará se há tags de script que precisam ser carregadas na página. Durante o processo, os scripts do Braze Web SDK serão carregados nas páginas da sua loja ou na página de status do pedido do checkout. 

Também adicionaremos scripts predefinidos se você tiver selecionado eventos de produto visualizado, produto clicado e carrinho abandonado que exigem Shopify ScriptTag ou envio de mensagens no app como um canal.  

#### Como ativar

Para ativar automaticamente os scripts do Braze Web SDK como parte da sua integração, selecione os eventos suportados do Shopify ScriptTag ou ative o envio de mensagens no app como um canal durante sua [configuração de integração do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview). 

Do criador de configuração da Shopify, os eventos denotados com asterisco (\*) são suportados pelo SDK da Web. Se você selecionar esses eventos ou incluir envio de mensagens no navegador, a Braze adicionará a implementação do Web SDK via Shopify ScriptTag à sua loja Shopify como parte da sua configuração.

#### Formulários de captura de e-mail do Shopify e reconciliação de usuários 

Os formulários de captura obtêm informações identificáveis do cliente no início do ciclo de vida do cliente para envio de mensagens e engajamento. 

O SDK para Web rastreia o comportamento no site da Shopify e de usuários anônimos usando o `device_id`. A integração do ScriptTag do Braze Shopify atribui e-mails de formulários de captura de e-mail do Shopify, como uma inscrição em boletim informativo, ao `device_id` do usuário.

Formulários típicos de captura de e-mail incluem: 
- Formulário de captura de e-mail 
- Formulário de inscrição para newsletter

Existem duas maneiras de reconciliar o e-mail do usuário e `device_id`: 
- Usando o script automatizado de captura de e-mail da Braze 
- Chamar os métodos `setEmail` ou `setPhoneNumber`

##### Capturando inscrições por e-mail ou telefone

Com a Braze, você pode usar nossos formulários de inscrição para [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) e [SMS e WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) para extrair benefícios do SDK para Web e das mensagens no app. 

Se estiver usando um e-mail ou número de telefone capturado pela Shopify, ou um formulário de captura de terceiros, você pode configurar diretamente no usuário que é rastreado pelo SDK para Web da Braze. Por exemplo, se você obtiver o endereço de e-mail do cliente, poderá defini-lo no perfil do usuário assim:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Para obter detalhes sobre como definir esses valores, consulte estes recursos de Javascript:

- Configuração do [e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) do usuário
- Definindo o [número de telefone](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) do usuário

Você também pode definir o estado de inscrição dos usuários à medida que coleta seu e-mail ou número de telefone, assim:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Para obter detalhes sobre como definir esses valores, consulte estes recursos de Javascript:

- Definindo o [tipo de inscrição de notificação por e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) do usuário
- Como adicionar o usuário a um [grupo de inscrições](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Exemplo de implementação de formulário de captura de terceiros**

1. Em `theme.liquid`, copie o seguinte snippet no `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Chamamos `setInterval` para que o script seja carregado primeiro
3\. Substitua `{FORM_ID}` pelo ID do elemento do formulário que você deseja capturar
(como "ContactFooter".)
4\. Substitua `{INPUT_EMAIL_ID}` pelo ID do elemento do campo de entrada de e-mail dentro do formulário
5\. Quando o formulário for enviado, o script chamará `setEmail` com o valor do campo de entrada de e-mail
6\. Depois que o script carrega, chamamos `clearInterval` para que ele carregue apenas uma vez

{% alert note %}
Neste momento, o formulário de captura de e-mail da Braze não criará um cliente no Shopify. Como resultado, você pode ter perfis de usuário do Braze sem perfis de usuário do Shopify associados até que o cliente passe pelo checkout ou crie uma conta.
{% endalert %}

#### O que esperar após a implementação

**Inicialização do SDK para Web da Braze**

O SDK da Web será inicializado ao iniciar a sessão. Braze precisará coletar o `device_id` para rastreamento de dados de usuários anônimos, pois outros identificadores como o ID de cliente do Shopify, e-mail ou número de telefone podem não estar prontamente disponíveis para visitantes convidados da sua loja Shopify.

O `device_id` também será usado para reconciliar dados de usuários com o perfil de usuário anônimo à medida que um cliente fornece mais informações identificáveis (como um endereço de e-mail ou número de telefone) após o processo de checkout.

**Versão do SDK para Web da Braze**

A versão atual do SDK para Web da Braze via integração Shopify ScriptTag é v4.2.

**Usuários ativos mensais (MAU)**

O SDK da Web rastreia sessões de seus clientes e convidados do Shopify. Como resultado, isso será considerado como MAU no seu relatório de dashboard do Braze e em suas alocações de MAU. É importante notar que usuários anônimos também contarão para o seu MAU. Para dispositivos móveis, usuários anônimos são dependentes do dispositivo. Para usuários da Web, os usuários anônimos dependem do cache do navegador.

{% endtab %}

{% tab tema liquid %}

### Como implementar o SDK para Web diretamente no seu site da Shopify theme.liquid

A Braze oferece várias maneiras de implementar o SDK para Web, incluindo:
- Adicionar o SDK para Web diretamente ao seu arquivo `theme.liquid` da Shopify
- Google Tag Manager 

Se você já tem o SDK para Web instalado na sua loja da Shopify, ainda pode prosseguir com a configuração do Shopify ScriptTag no processo de integração. 

Durante o processo de instalação, a Braze verificará se instâncias do SDK para Web já estão disponíveis na sua loja da Shopify. Se houver uma implementação existente, Braze não carregará os scripts predefinidos para habilitar o SDK da Web. Em seguida, adicionaremos os scripts necessários para garantir que você possa rastrear os eventos selecionados ou ativar o envio de mensagens no navegador.

#### Como ativar

Para implementar manualmente o SDK para Web, veja [Configuração inicial do SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Para implementar o SDK para Web via Google Tag Manager, veja [Google Tag Manager para Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager). 

Com qualquer jornada de implementação, certifique-se de que sua integração de SDK da Web inclua o seguinte ou a integração com o Shopify não será suportada: 
- Versão v4.0+ do SDK para Web
- O SDK da Web é inicializado ao iniciar a sessão

#### Formulários de captura de e-mail do Shopify e reconciliação de usuários 

Os formulários de captura obtêm informações identificáveis do cliente no início do ciclo de vida do cliente para envio de mensagens e engajamento. 

O SDK para Web rastreia o comportamento no site da Shopify e de usuários anônimos usando o `device_id`. A integração do ScriptTag do Braze Shopify atribui e-mails de formulários de captura de e-mail do Shopify, como uma inscrição em boletim informativo, ao `device_id` do usuário.

Formulários típicos de captura de e-mail incluem: 
- Formulário de captura de e-mail 
- Formulário de inscrição para newsletter

Existem duas maneiras de reconciliar o e-mail do usuário e `device_id`: 
- Usando o script automatizado de captura de e-mail da Braze 
- Chamar os métodos `setEmail` ou `setPhoneNumber`

##### Capturando inscrições por e-mail ou telefone

Com a Braze, você pode usar nossos formulários de inscrição para [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) e [SMS e WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) para extrair benefícios do SDK para Web e das mensagens no app. 

Se estiver usando um formulário de captura de e-mail ou número de telefone do Shopify, ou um formulário de captura de terceiros, você pode ser configurado diretamente no objeto de usuário que é rastreado pelo Braze Web SDK. Por exemplo, se você obtiver o endereço de e-mail do cliente, poderá defini-lo no perfil do usuário assim:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Para obter detalhes sobre como definir esses valores, consulte estes recursos de Javascript:

- Configuração do [e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) do usuário
- Definindo o [número de telefone](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) do usuário

Você também pode definir o estado de inscrição dos usuários enquanto coleta o e-mail ou número de telefone deles assim:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Para obter detalhes sobre como definir esses valores, consulte estes recursos de Javascript:

- Definindo o [tipo de inscrição de notificação por e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) do usuário
- Como adicionar o usuário a um [grupo de inscrições](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Exemplo de implementação de formulário de captura de terceiros**

1. Em `theme.liquid`, copie o seguinte snippet no `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Chamamos `setInterval` para que o script seja carregado primeiro
3\. Substitua `{FORM_ID}` pelo ID do elemento do formulário que você deseja capturar
(como "ContactFooter".)
4\. Substitua `{INPUT_EMAIL_ID}` pelo ID do elemento do campo de entrada de e-mail dentro do formulário
5\. Quando o formulário for enviado, o script chamará `setEmail` com o valor do campo de entrada de e-mail
6\. Depois que o script carrega, chamamos `clearInterval` para que ele carregue apenas uma vez

{% alert note %}
Neste momento, o formulário de captura de e-mail da Braze não criará um cliente no Shopify. Como resultado, você pode ter perfis de usuário do Braze sem perfis de usuário do Shopify associados até que o cliente passe pelo checkout ou crie uma conta.
{% endalert %}

#### O que esperar após a integração

**Inicialização do SDK para Web da Braze**

O SDK da Web será inicializado ao iniciar a sessão. Braze precisará coletar o `device_id` para rastreamento de dados de usuários anônimos, pois outros identificadores como o ID de cliente do Shopify, e-mail ou número de telefone podem não estar prontamente disponíveis para visitantes convidados da sua loja Shopify.

O `device_id` também será usado para reconciliar dados de usuários ao perfil anônimo do usuário à medida que um cliente fornece mais informações identificáveis (como seu e-mail ou número de telefone) durante e após o processo de checkout.

**Versão do SDK para Web da Braze**

A versão atual do SDK para Web da Braze precisa ser v4.0+.

**Usuários ativos mensais (MAU)**

O SDK da Web rastreia as sessões de seus clientes e convidados do Shopify. Como resultado, isso será considerado como MAU no seu relatório de dashboard do Braze e em suas alocações de MAU. É importante notar que usuários anônimos também contarão para o seu MAU. Para dispositivos móveis, usuários anônimos são dependentes do dispositivo. Para usuários da Web, os usuários anônimos dependem do cache do navegador.

{% endtab %}
{% tab Site headless da Shopify %}

### Como implementar o SDK para Web diretamente no seu site headless da Shopify {#headless-site}

A integração Braze Shopify ScriptTag é incompatível com sites headless da Shopify. Como resultado, você não poderá obter suporte padrão para produto visualizado, produto clicado ou eventos de carrinho abandonado, ou ativar envio de mensagens no app através de nossos scripts predefinidos. 

#### Como ativar

Para integrar diretamente o SDK para Web ao seu site headless da Shopify, consulte [Configuração inicial do SDK para Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

Confirme se sua integração SDK para Web inclui o seguinte: 
- A versão do SDK da Web deve ser v4.0+
- O SDK da Web é inicializado ao iniciar a sessão

#### Configurando formulários do Shopify para reconciliação de usuários

As marcas de comércio eletrônico provavelmente têm experiências em seu site da Shopify para capturar informações identificáveis dos clientes antes do checkout, como formulários de captura de e-mail.

O SDK para Web rastreia o comportamento no site da Shopify e de usuários anônimos com o `device_id`. Para confirmar que os endereços de e-mail são adicionados ao perfil de usuário anônimo, adicione o seguinte a um boletim informativo ou formulário de captura de e-mail: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Para captura de e-mail ou inscrições em boletins informativos
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

Quando os usuários se registram ou fazem {registro} em sua conta, você pode querer [identificar o perfil do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) com um ID externo. Após o usuário se registrar e fazer login, adicione o método [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) para atribuir um ID externo se um usuário criar uma conta ou fizer login. 

{% alert note %}
Se você definir um alias temporário no perfil do usuário, poderá prosseguir para fazer uma solicitação ao endpoint [users/merge endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para identificar o usuário posteriormente.
{% endalert %}

#### Configurando a reconciliação do usuário de checkout {#headless-checkout}

Quando você ativar o evento de checkout abandonado, a Braze receberá o webhook de checkouts/create da Shopify. Braze tentará corresponder a um perfil de usuário existente por endereço de e-mail, número de telefone ou ID de cliente do Shopify. Se não houver correspondência, a Braze criará um perfil de alias. 

Para garantir que o perfil do usuário rastreado no site se mescle com o perfil de usuário do alias Shopify criado pelos webhooks do Shopify, você pode usar o [`/users/merge` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) seguindo os passos abaixo. 

{% alert tip %}
Você pode registrar um evento personalizado via chamada de SDK ou API feita no arquivo `theme.liquid` para disparar um canva que inclui uma solicitação para o endpoint `users/merge`. Estes métodos estão descritos abaixo.
{% endalert %}

Assim que um cliente visita seu site da Shopify, um usuário anônimo é criado. Este usuário é automaticamente atribuído a um Braze `device_id`. 

1. Atribuir aleatoriamente um [alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) exclusivo para o visitante do seu site em uma nova sessão.

2. À medida que os usuários realizam ações em seu site, registre-as como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) ou [capture atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web). Quando o usuário prossegue para o checkout e insere seu e-mail em um formulário da Shopify, um ID de cliente da Shopify é criado. Braze processará os webhooks do Shopify e criará um novo perfil de usuário se o e-mail, telefone ou alias do Shopify não corresponder a um usuário existente.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\. Para evitar perfis de usuário duplicados, você precisa mesclar o perfil de usuário contendo o Braze `device_id` com o perfil de usuário contendo o perfil de alias do Shopify. Você pode criar um canva acionado por API que definirá uma postergação, atualizará seu usuário com o atributo `do_not_merge` e fará uma solicitação para o endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/). Você também pode registrar um evento personalizado como `merge_user` para disparar seu canva. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. Quando os usuários saem do fluxo ou concluem a finalização da compra, você pode registrar um evento personalizado, como `merge_user`, para disparar um canva que definirá uma postergação, atualizará seu usuário com o atributo `do_not_merge` e fará uma solicitação ao endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. Nos seus critérios de entrada do canva, direcione apenas perfis de usuários não identificados, ou seja, aqueles sem ID externo e para os quais `do_not_merge` não é verdadeiro. <br><br>![A etapa "Público de entrada" no criador de canva com `do_not_merge` como filtro.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. Depois de configurar seus critérios de entrada do canva, você pode criar seu Canvas Flow. Defina o primeiro passo do seu canva como uma etapa de **postergação** para evitar possíveis condições de corrida durante o processamento.<br><br>![Etapa de postergação no criador do canva.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. Você pode criar uma **Atualização do Usuário** etapa para atualizar `do_not_merge` atributo personalizado para “verdadeiro” como esses usuários serão mesclados na próxima etapa. <br><br>![Etapa de atualização do usuário no criador do canva com `do_not_merge` selecionado como atributo.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. Em seguida, crie uma etapa de **mensagem** com um webhook.<br><br>![Etapa de mensagem no criador do canva com um canal de envio de mensagens por webhook.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
Para obter informações sobre o comportamento `merge_users`, consulte [POST: Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. À medida que os usuários saem do fluxo ou concluem a finalização da compra, os webhooks subsequentes do Shopify serão correspondidos pelo endereço de e-mail ou número de telefone ou usando o alias do Shopify.

{% endtab %}
{% endtabs %}
