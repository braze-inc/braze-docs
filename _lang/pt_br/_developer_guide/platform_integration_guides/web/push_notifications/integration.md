---
nav_title: Integração
article_title: Integração push para web
platform: Web
channel: push
page_order: 0
page_type: reference
description: "Este artigo descreve como integrar o web push da Braze por meio do SDK da Braze."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# Integração de notificações por push

> Uma notificação por push é um alerta que aparece na tela do usuário quando ocorre uma atualização importante. As notificações por push podem ser recebidas mesmo quando a página da Web não estiver aberta no navegador do usuário. As notificações por push são uma maneira valiosa de fornecer aos seus usuários conteúdo relevante e sensível ao tempo ou de reengajá-los com o seu site. Este artigo de referência aborda como integrar o web push da Braze com o SDK da Braze.

Consulte nossas [práticas recomendadas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) para obter mais recursos.

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

As notificações por push da Web são implementadas usando o [padrão push do W3C](http://www.w3.org/TR/push-api/), que é suportado pela maioria dos principais navegadores.

Para saber mais sobre os padrões do protocolo push e o suporte a navegadores, consulte os recursos de [AppleSafari](https://developer.apple.com/notifications/safari-push-notifications/ "Push Notifications") [, MozillaMozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Push API browser compatibility") e [MicrosoftMicrosoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Push API")

{% multi_lang_include archive/web-v4-rename.md %}

## Integração

### Etapa 1: Configurar o service worker do seu site

- Se você ainda não tiver um service worker, crie um novo arquivo chamado `service-worker.js` com o seguinte snippet e coloque-o no diretório raiz do seu site.
- Caso contrário, se o seu site já registrar um service worker, adicione o seguinte trecho ao arquivo do service worker e defina a opção de inicialização [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) como `true` ao inicializar o Web SDK.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

Se o nome de arquivo do service worker não for `service-worker.js`, será necessário usar a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.

{% alert important %}
Seu servidor da Web deve retornar um `Content-Type: application/javascript` ao servir seu arquivo de service worker.
{% endalert %}

#### E se eu não conseguir registrar um service worker no diretório raiz?

Por padrão, um service worker só pode ser usado no mesmo diretório em que está registrado. Por exemplo, se o seu arquivo de service worker existir em `/assets/service-worker.js`, só será possível registrá-lo em `example.com/assets/*` ou em um subdiretório da pasta `assets`, mas não na sua página inicial (`example.com/`). Por isso, é recomendável hospedar e registrar o service worker no diretório raiz (como `https://example.com/service-worker.js`).

Se não for possível registrar um service worker no domínio raiz, uma alternativa é usar o cabeçalho HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) ao servir o arquivo do service worker. Ao configurar seu servidor para retornar `Service-Worker-Allowed: /` na resposta para o service worker, isso instruirá o navegador a ampliar o escopo e permitir que ele seja usado em um diretório diferente.

#### Posso criar um service worker usando um Tag Manager?

Não, os service workers devem ser hospedados no servidor de seu site e não podem ser carregados por meio do Tag Manager.

### Etapa 2: Registro do navegador

Para que um navegador receba notificações por push, é necessário registrá-lo chamando `braze.requestPushPermission()`. Isso solicitará imediatamente a permissão para push do usuário. 

Se quiser mostrar sua própria interface de usuário relacionada a push ao usuário antes de solicitar permissão de push (conhecido como prompt de soft push), é possível testar para ver se o push é compatível com o navegador do usuário com `braze.isPushSupported()`. Consulte o [exemplo de prompt soft push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) usando mensagens no app.

Para cancelar a inscrição de um usuário, chame `braze.unregisterPush()`.

{% alert important %}
As versões recentes do Safari e do Firefox exigem que você chame esse método de um manipulador de eventos de curta duração (por exemplo, de um manipulador de clique de botão ou de um prompt soft push). Isso está de acordo com as [práticas recomendadas de experiência do usuário do Chrome](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) para registro push.
{% endalert %}

### Etapa 3: Configurar o push do Safari (opcional) {#safari}

{% alert important %}
Essa etapa não é mais necessária a partir do Safari 16 no macOS 13. Conclua esta etapa somente se quiser oferecer suporte a versões mais antigas do macOS Safari.
{% endalert %}

Para oferecer suporte a notificações por push para o Safari no macOS X, siga estas outras instruções:

- Gere um certificado de push do Safari seguindo as instruções de [Registro na Apple](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33).
- No dashboard da Braze, na página **Configurações** (onde estão localizadas suas chaves de API), selecione seu app da Web. Clique em **Configure Safari Push** e siga as instruções, fazendo upload do certificado push que você acabou de gerar.
- Ao chamar `braze.initialize`, forneça a opção de configuração opcional `safariWebsitePushId` com o ID de push do site que você usou ao gerar o certificado de push do Safari. Por exemplo `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Safari Mobile push {#safari-mobile}

O Safari 16.4+ no iOS e iPadOS suporta web push para apps que foram [adicionados à tela inicial](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) e têm um arquivo [Web Application Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest). Depois de concluir as etapas para integrar as notificações por web push, você poderá fornecer suporte para push móvel também para o Safari. 

Para oferecer suporte ao push para mobile e web do Safari, siga nosso guia [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

## Propt de soft push

Um prompt de soft push (também conhecido como "push primer") ajuda a otimizar sua taxa de aceitação quando se trata de pedir permissão.

Visite [Soft push prompt]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) para saber mais sobre a configuração de um soft push prompt.

## Requisito de HTTPS

Os padrões da web exigem que o domínio que está solicitando a permissão de notificação por push seja seguro.

### O que define um site seguro?

Um site é considerado seguro se corresponder a um dos seguintes padrões de origem segura:

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (arquivo, \*, -)
- (chrome-extension, \*, -)

Esse requisito de segurança na especificação de padrões abertos sobre a qual web push da Braze é desenvolvido evita ataques do tipo man-in-the-middle.

### E se um site seguro não estiver disponível?

Embora a prática recomendada do setor seja tornar todo o site seguro, os clientes que não podem proteger o domínio do site podem contornar o requisito usando um modal seguro. Leia mais em nosso guia para usar o [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) ou veja uma [demonstração funcional](http://appboyj.com/modal-test.html).

## Configurações avançadas do trabalhador de serviço

Nosso arquivo de service worker chamará automaticamente o endereço `skipWaiting` após a instalação. Se quiser evitar isso, adicione o seguinte código ao seu arquivo de service worker, antes de importar a Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Solução de problemas

**Segui as instruções de integração, mas ainda não estou recebendo notificações por push.**
- As notificações por push da Web exigem que seu site seja HTTPS.
- Nem todos os navegadores podem receber mensagens de navegador. Certifique-se de que `braze.isPushSupported()` retorne `true` no navegador.
- Se um usuário tiver negado o acesso push a um site, ele não será solicitado a dar permissão novamente, a menos que remova o status de negação das preferências do navegador.

