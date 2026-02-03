## Sobre o SDK do Braze Web

O SDK do Web Braze permite coletar análises de dados e exibir mensagens no app, mensagens push e de cartão de conteúdo para seus usuários da Internet. Para saber mais, consulte a [documentação de referência do Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integrar o Web SDK

Você pode integrar o SDK do Braze Web usando os seguintes métodos. Para obter opções adicionais, consulte [outros métodos de integração](#web_other-integration-methods).

- **Integração baseada em código:** Integre o SDK do Braze Web diretamente em sua base de código usando seu gerenciador de pacotes preferido ou a CDN do Braze. Isso lhe dá controle total sobre como o SDK é carregado e configurado.
- **Google Tag Manager:** Uma solução sem código que permite integrar o Web Braze SDK sem modificar o código do seu site. Para saber mais, consulte [Google Tag Manager com o SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% alert important %}
Recomendamos usar o [método de integração NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Os benefícios incluem o armazenamento de bibliotecas SDK localmente em seu site, o fornecimento de imunidade a extensões de bloqueadores de anúncios e a contribuição para tempos de carregamento mais rápidos como parte do suporte do pacote.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Etapa 1: Instalar a biblioteca do Braze

Você pode instalar a biblioteca Braze usando um dos seguintes métodos. No entanto, se o seu site usa um `Content-Security-Policy`, revise a [Política de Segurança de Conteúdo]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) antes de continuar.

{% alert important %}
Embora a maioria dos bloqueadores de anúncios não bloqueie o Braze Web SDK, alguns bloqueadores de anúncios mais restritivos são conhecidos por causar problemas.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Se o seu site usar os gerenciadores de pacotes NPM ou Yarn, você poderá adicionar o [pacote Braze NPM](https://www.npmjs.com/package/@braze/web-sdk) como uma dependência.

As definições do Typescript agora estão incluídas a partir da versão 3.0.0. Para notas sobre como fazer upgrade da versão 2.x para a 3.x, consulte nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Depois de instalada, você pode `import` ou `require` a biblioteca da maneira habitual:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Adicione o SDK da Braze para Web diretamente ao seu HTML fazendo referência ao nosso script hospedado na CDN, que carrega a biblioteca de forma assíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
A configuração padrão **Prevent Cross-Site Tracking (Impedir rastreamento entre sites** ) no Safari pode impedir a exibição de tipos de mensagens no app, como Banners e Cartões de conteúdo, quando você usa o método de integração CDN. Para evitar esse problema, use o método de integração NPM para que o Safari não classifique essas mensagens como tráfego entre sites e seus usuários da Web possam vê-las em todos os navegadores compatíveis.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Etapa 2: Inicializar o SDK

Depois que o Braze Web SDK for adicionado ao seu site, inicialize a biblioteca com a chave de API e [o endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) encontrados em **Settings** > **App Settings** em seu dashboard do Braze. Para obter uma lista completa de opções para `braze.initialize()`, juntamente com nossos outros métodos JavaScript, consulte [a documentação do Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
**Exibição de mensagens no app**: Para exibir mensagens no app automaticamente quando elas forem disparadas, você deve chamar `braze.automaticallyShowInAppMessages()`. Sem essa chamada, as mensagens no app não são exibidas automaticamente. Se quiser gerenciar a exibição de mensagens manualmente, remova essa chamada e use `braze.subscribeToInAppMessage()` em vez disso. Para saber mais, consulte [Envio de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/delivery/).
{% endalert %}

{% alert important %}
Usuários anônimos em dispositivos móveis ou da Web podem ser contabilizados no seu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Como resultado, talvez seja necessário carregar ou inicializar condicionalmente o SDK para excluir esses usuários da sua contagem de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Configurações opcionais

### Registro

Para ativar rapidamente o registro, adicione `?brazeLogging=true` como um parâmetro ao URL do seu site. Como alternativa, é possível ativar o registro [básico](#web_basic-logging) ou [personalizado](#web_custom-logging).

#### Registro básico

{% tabs local %}
{% tab before initialization %}
Use `enableLogging` para registrar mensagens básicas de depuração no console JavaScript antes de o SDK ser inicializado.

```javascript
enableLogging: true
```

Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Use `braze.toggleLogging()` para registrar mensagens básicas de depuração no console JavaScript depois que o SDK for inicializado. Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Os registros básicos são visíveis para todos os usuários, portanto, considere desativar ou mudar para [`setLogger`](#web_custom-logging)antes de liberar seu código para produção.
{% endalert %}

#### Registro personalizado

Use `setLogger` para registrar mensagens de depuração personalizadas no console JavaScript. Ao contrário dos registros básicos, esses registros não são visíveis para os usuários.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Substitua `STRING` por sua mensagem como um único parâmetro string. Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Fazendo upgrade do SDK

{% multi_lang_include archive/web-v4-rename.md %}

Ao fazer referência ao Braze Web SDK a partir de nossa rede de fornecimento de conteúdo, por exemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (conforme recomendado por nossas instruções de integração padrão), seus usuários recebem pequenas atualizações (correções de bugs e recursos compatíveis com versões anteriores, versões `a.a.a` a `a.a.z` nos exemplos acima) automaticamente quando atualizam seu site.

No entanto, quando lançamos alterações importantes, solicitamos que você faça upgrade do Braze Web SDK manualmente para garantir que as alterações não afetem sua integração. Além disso, se você baixar nosso SDK e hospedá-lo você mesmo, não receberá nenhuma atualização de versão automaticamente e deverá fazer upgrade manualmente para receber os recursos e as correções de bugs mais recentes.

Mantenha-se atualizado com a versão mais recente [seguindo nosso feed de versões](https://github.com/braze-inc/braze-web-sdk/tags.atom) com o leitor de RSS ou serviço de sua preferência e consulte [nosso changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para obter uma contabilidade completa do histórico de versões do Web SDK. Para fazer upgrade do SDK da Braze para Web:

- Atualize a versão da biblioteca do Braze alterando o número da versão em `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou nas dependências do gerenciador de pacotes.
- Se você tiver o web push integrado, atualize o arquivo do service worker em seu site - por padrão, ele está localizado em `/service-worker.js` no diretório raiz do site, mas o local pode ser personalizado em algumas integrações. Você deve acessar o diretório raiz para hospedar um arquivo de service worker.

Você deve atualizar esses dois arquivos em coordenação um com o outro para obter a funcionalidade adequada.

## Outros métodos de integração

### Accelerated Mobile Pages (AMP)
{% details See more %}
#### Etapa 1: Incluir script de push para web de AMP

Adicione a seguinte tag de script assíncrono em seu cabeçalho:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Etapa 2: Adicionar widgets de inscrição

Adicione um widget ao corpo do seu HTML que permita que os usuários assinem e cancelem a inscrição no push.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### Etapa 3: Adicione `helper-iframe` e `permission-dialog`

O componente AMP Web Push cria um pop-up para lidar com inscrições push, portanto, você deve adicionar os seguintes arquivos auxiliares ao seu projeto para ativar esse recurso:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Etapa 4: Criar um arquivo de service worker

Crie um arquivo `service-worker.js` no diretório raiz do seu site e adicione o seguinte snippet:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Etapa 5: Configurar o elemento HTML do AMP web push

Adicione o seguinte elemento HTML `amp-web-push` ao corpo do HTML. Lembre-se de que você precisa anexar [`apiKey` e `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parâmetros de consulta a `service-worker-URL`.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### Definição de módulo assíncrono (AMD)

#### Desativar o suporte

Se o seu site usa o RequireJS ou outro carregador de módulos da AMD, mas você prefere carregar o Braze Web SDK por meio de uma das outras opções desta lista, é possível carregar uma versão da biblioteca que não inclua o suporte da AMD. Essa versão da biblioteca pode ser carregada no seguinte local da CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Carregador de módulos

Se você usa o RequireJS ou outros carregadores de módulos da AMD, recomendamos que hospede uma cópia da nossa biblioteca e faça referência a ela como faria com outros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Elétrons {#electron}

O Electron não oferece suporte oficial a notificações por push na Web (consulte: este [problema no GitHub](https://github.com/electron/electron/issues/6697)). Há outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode tentar e que não foram testadas pelo Braze.

### Estrutura Jest {#jest}

Ao usar o Jest, você poderá ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração em `package.json` para ignorar o SDK da Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Estruturas de SSR {#ssr}

Se você usar uma estrutura de renderização do lado do servidor (SSR), como Next.js, poderá encontrar erros porque o SDK foi criado para ser executado em um ambiente de navegador. Você pode resolver esses problemas importando dinamicamente o SDK.

Você pode manter os benefícios do tree-shaking ao fazer isso exportando as partes do SDK de que precisa em um arquivo separado e, em seguida, importando dinamicamente esse arquivo para o seu componente.

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Como alternativa, se estiver usando o Webpack para empacotar seu app, poderá aproveitar os comentários mágicos para importar dinamicamente apenas as partes do SDK de que precisa.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Tealium iQ

O Tealium iQ oferece uma integração básica do Braze pronta para uso. Para configurar a integração, procure o Braze na interface do Tealium Tag Management e forneça a chave de API do Web SDK em seu dashboard.

Para obter mais detalhes ou suporte aprofundado à configuração do Tealium, consulte nossa [documentação de integração]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com o gerente de conta do Tealium.

### Vite {#vite}

Se você usa o Vite e vir um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, talvez seja necessário excluir o SDK da Braze de sua [descoberta de dependências](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Outros gerenciadores de tags

O Braze também pode ser compatível com outras soluções de gerenciamento de tags, seguindo nossas instruções de integração em uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.
