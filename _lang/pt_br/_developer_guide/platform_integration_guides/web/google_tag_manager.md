---
nav_title: Google Tag Manager
article_title: Google Tag Manager para Web
platform: Web
page_order: 20
description: "Este artigo aborda como usar o Google Tag Manager para implantar a Braze em seu site."

---

# Google Tag Manager

> Este artigo fornece um guia passo a passo sobre como adicionar o SDK da Braze para Web ao seu site usando o Google Tag Manager (GTM). [O Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) permite adicionar, remover e editar remotamente tags em seu site sem exigir uma versão de código de produção ou recursos de engenharia.

Há dois modelos do Google Tag Manager criados pelo Braze, a [tag de inicialização](#initialization-tag) e a [tag de ações](#actions-tag).

Ambas as tags podem ser adicionadas ao seu espaço de trabalho a partir da [galeria da comunidade do Google](https://tagmanager.google.com/gallery/#/?filter=braze) ou pesquisando por Braze ao adicionar uma nova tag a partir dos modelos da comunidade.

![imagem da pesquisa da galeria]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Política de consentimento do usuário da UE do Google atualizada

{% alert important %}
O Google está atualizando sua [Política de Consentimento do Usuário da UE](https://www.google.com/about/company/user-consent-policy/) em resposta às alterações na [Lei de Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que entrará em vigor a partir de 6 de março de 2024. Essa nova alteração exige que os anunciantes divulguem determinadas informações aos seus usuários finais do EEE e do Reino Unido, bem como obtenham deles os consentimentos necessários. Consulte a documentação a seguir para saber mais.
{% endalert %}

Como parte da Política de consentimento do usuário da UE do Google, os seguintes atributos booleanos personalizados precisam ser registrados nos perfis de usuário:

- `$google_ad_user_data`
- `$google_ad_personalization`

Se estiver configurando-os por meio da integração com o GTM, os atributos personalizados exigirão a criação de uma tag HTML personalizada. A seguir, um exemplo de como registrar esses valores como tipos de dados booleanos (não como strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para saber mais, consulte [Sincronização do público do Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Modelo de tag de inicialização {#initialization-tag}

Use a tag de inicialização para adicionar o SDK da Braze para Web ao seu site.

### Etapa 1: Configuração do push (opcional)

Opcionalmente, se você quiser enviar push por meio do Google Tag Manager, primeiro siga as diretrizes [de integração de push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) para:
1. Configure o service worker do seu site, colocando-o no diretório raiz do site
2. Configure o registro do navegador. Depois que o service worker for configurado, você deverá definir o método `braze.requestPushPermission()` nativamente no app ou por meio de uma tag HTML personalizada (via dashboard do GTM). Você também precisará se certificar de que a tag seja acionada depois que o SDK for inicializado.

### Etapa 2: Selecione a tag de inicialização

Procure a Braze na galeria de modelos da comunidade e selecione a **tag Braze Initialization**.

![Uma caixa de diálogo que mostra as definições de configuração da tag Braze Initialization. As configurações incluídas são "tag type", "API key", "API endpoint", "SDK version", "external user ID" e "Safari web push ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Etapa 3: Configurar definições

Insira sua chave de identificador do app Braze API e o endpoint de SDK, que podem ser encontrados na página **Manage Settings (Gerenciar configurações)** de seu dashboard. Digite a versão mais recente do SDK para Web em `major.minor`. Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Você pode ver uma lista das versões do SDK em nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Etapa 4: Escolha as opções de inicialização

Escolha entre o conjunto opcional de opções de inicialização adicionais descritas no [Initial setup]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) guide.

### Etapa 5: Verificação e controle de qualidade

Depois de implementar essa tag, há duas maneiras de verificar uma integração adequada:

1. Usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, você verá que a tag Braze Initialization foi disparada em suas páginas ou eventos configurados.
2. Você deverá ver solicitações de rede feitas à Braze e a biblioteca global `window.braze` deverá estar definida em sua página da Web.

## Modelo de tag de ações {#actions-tag}

O modelo Braze Actions Tag permite disparar eventos personalizados, rastrear compras, alterar IDs de usuários e interromper ou retomar o rastreamento para atender a requisitos de privacidade.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### Alteração da ID externa do usuário {#external-id}

O tipo de tag **Change User (Alterar usuário** ) chama o [método`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). 

Use essa tag sempre que um usuário registrar-se ou for identificado de outra forma com seu identificador exclusivo `external_id`.

Certifique-se de inserir o ID exclusivo do usuário atual no campo **External User ID (ID do usuário externo** ), normalmente preenchido usando uma variável de camada de dados enviada pelo seu site.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (tipo de tag) e "external user ID" (ID de usuário externo).]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### Registre eventos personalizados {#custom-events}

O tipo de tag **Custom Event** chama o [método`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

Use essa tag para enviar eventos personalizados para o Braze, incluindo opcionalmente propriedades de eventos personalizados.

Digite o **nome do evento** usando uma variável ou digitando um nome de evento.

Use o botão **Adicionar linha** para adicionar propriedades de eventos.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (evento personalizado), "event name" (nome do evento) (clique no botão) e "event properties" (propriedades do evento).]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### Eventos de comércio eletrônico {#ecommerce}

Se o seu site registra compras usando o item padrão da camada de dados de [eventos de comércio eletrônico](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) para o Google Tag Manager, é possível usar o tipo de tag **E-commerce Purchase**. Esse tipo de ação registrará uma "compra" separada no Braze para cada item enviado na lista de `items`.

Você também pode especificar nomes de propriedades adicionais que deseja incluir como propriedades de compra, especificando suas chaves na lista Propriedades de compra. Note que o Braze procurará no site `item` individual que está sendo registrado todas as propriedades de compra que você adicionar à lista.

Por exemplo, digamos que sua carga útil de comércio eletrônico contenha o seguinte `items`:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Se você quiser que apenas `item_brand` e `item_name` sejam passados como propriedades de compra, basta adicionar esses dois campos à tabela de propriedades de compra. Se você não fornecer nenhuma propriedade, nenhuma propriedade de compra será enviada na [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) chamada para o Braze.

### Rastreamento de compra {#purchases}

O tipo de tag **Purchase** chama o [método`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase).

Use essa tag para rastrear as compras no Braze, incluindo opcionalmente as propriedades de compra.

Os campos **ID do produto** e **Preço** são obrigatórios.

Use o botão **Adicionar linha** para adicionar propriedades de compra.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (tipo de tag), "external ID" (ID externa), "price" (preço), "currency code" (código de moeda), "quantity" (quantidade) e "purchase properties" (propriedades de compra).]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### Parar e retomar o rastreamento {#stop-tracking}

Às vezes, pode ser necessário desativar ou reativar o rastreamento do Braze em seu site, por exemplo, depois que um usuário indicar que aceitou o rastreamento da Web por motivos de privacidade.

Use o tipo de tag **Disable Tracking (Desativar rastreamento** ) ou **Resume Tracking (Retomar rastreamento)** para desativar ou reativar o rastreamento da Web, respectivamente. Essas duas opções chamam [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) e [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

### Atributos personalizados do usuário {#custom-attributes}

Os atributos personalizados do usuário não estão disponíveis devido a uma limitação na linguagem de script do Google Tag Manager. Para registrar atributos personalizados, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
O modelo GTM não oferece suporte a propriedades aninhadas em eventos ou compras. É possível usar o HTML anterior para registrar quaisquer eventos ou compras que exijam propriedades aninhadas.
{% endalert %}

### Atribuições padrão do usuário {#standard-attributes}

Os atributos padrão do usuário, como o nome do usuário, devem ser registrados da mesma forma que os atributos personalizados do usuário. Certifique-se de que os valores que está passando para as atribuições padrão correspondam ao formato esperado especificado na documentação da [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por exemplo, o atributo gender pode aceitar qualquer um dos seguintes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Portanto, para definir o gênero de um usuário como feminino, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Integração de cartões de conteúdo

Há algumas etapas adicionais para integrar o canal de envio de mensagens [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) usando o Google Tag Manager. O Google Tag Manager funciona injetando o [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (uma versão do nosso Web SDK) diretamente no código do seu site, o que significa que todos os métodos do SDK estão disponíveis como se você tivesse integrado o SDK sem o Google Tag Manager, exceto ao implementar cartões de conteúdo.

### Opção 1: Integração usando o GTM

Para uma integração padrão do feed do cartão de conteúdo, você pode usar uma tag **HTML personalizada** no Google Tag Manager. Adicione o seguinte em sua tag HTML personalizada, que ativará o feed padrão do cartão de conteúdo:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuração de tag no Google Tag Manager de uma tag HTML personalizada que mostra o feed do cartão de conteúdo.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### Opção 2: Integração direta em seu site

Para ter mais liberdade na personalização da aparência dos cartões de conteúdo e de seu feed, é possível integrar diretamente os cartões de conteúdo em seu site nativo. Há duas abordagens que você pode adotar: usar a interface de usuário de feed padrão ou criar uma interface de usuário de feed personalizada.

#### Feed padrão

Ao implementar a [UI de feed padrão]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), os métodos da Braze devem ter `window.` adicionado ao início do método. Por exemplo, `braze.showContentCards` deve ser `window.braze.showContentCards`.

#### Interface de usuário de feed personalizada

Para o estilo de [feed personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling), as etapas são as mesmas que se você tivesse integrado o SDK sem o GTM. Por exemplo, se quiser personalizar a largura do feed do cartão de conteúdo, você pode colar o seguinte em seu arquivo CSS:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## Fazer upgrade e atualizar modelos {#upgrading}

Para fazer upgrade para a versão mais recente do SDK da Braze para Web, siga as três etapas a seguir em seu dashboard do Google Tag Manager:

1. **Atualizar modelo de tag**<br>Acesse a página **Modelos** em seu espaço de trabalho. Aqui você verá um ícone indicando que há uma atualização disponível.<br><br>![Página de modelos mostrando que uma atualização está disponível]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Clique nesse ícone e, após revisar a alteração, clique em **Accept Update (Aceitar atualização)**.<br><br>![Uma tela comparando os modelos de tag antigos e novos com um botão para "Aceitar atualização"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Atualizar o número da versão**<br>Depois que seu modelo de tag tiver sido atualizado, edite a tag de inicialização da Braze e atualize a versão do SDK para a versão mais recente `major.minor`. Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Você pode ver uma lista das versões do SDK em nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modelo de inicialização do Braze com um campo de entrada para alterar a versão do SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Controle de qualidade e publicação**<br>Verifique se a nova versão do SDK está funcionando usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager antes de publicar uma atualização no seu contêiner de tags.

## Etapas de solução de problemas {#troubleshooting}

### Ativar a depuração de tag {#debugging}

Cada modelo de tag do Braze tem uma caixa de seleção opcional **de depuração de tag GTM** que pode ser usada para registrar mensagens de depuração no console JavaScript da sua página da Web.

![Ferramenta de debug do Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### Entrar no modo de depuração

Outra maneira de ajudar a depurar sua integração com o Google Tag Manager é usar o recurso de [modo de prévia](https://support.google.com/tagmanager/answer/6107056) do Google.

Isso ajudará a identificar quais valores estão sendo enviados da camada de dados da sua página da Web para cada tag do Braze disparada e também explicará quais tags foram ou não disparadas.

![A página de resumo da tag de inicialização do Braze fornece uma visão geral da tag, incluindo informações sobre quais tags foram disparadas.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### Ativar o registro detalhado

Para permitir que o suporte técnico da Braze acesse os registros durante os testes, é possível ativar o registro detalhado na integração com o Google Tag Manager. Esses registros serão exibidos na guia **Console** das ferramentas de desenvolvedor do seu navegador [.](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)

Em sua integração do Google Tag Manager, navegue até a tag de inicialização da Braze e selecione **Ativar registro do SDK para Web**.

![A página de resumo da tag de inicialização do Braze com a opção de ativar o registro do SDK da Web.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
