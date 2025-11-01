## Sobre o SDK Braze para Web

O SDK Braze para Web permite coletar análises e exibir mensagens ricas no aplicativo, push e mensagens de Cartão de Conteúdo para seus usuários da web. Para mais informações, consulte [documentação de referência do Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integrando o SDK para Web

Você pode integrar o SDK Braze para Web usando os seguintes métodos. Para opções adicionais, consulte [outros métodos de integração](#web_other-integration-methods).

- **Integração Baseada em Código:** Integre o SDK Braze para Web diretamente em seu código usando seu gerenciador de pacotes preferido ou a CDN do Braze. Isso lhe dará controle total sobre como o SDK é carregado e configurado.
- **Google Tag Manager:** Uma solução sem código que permite integrar o SDK Braze para Web sem modificar o código do seu site. Para mais informações, consulte [Google Tag Manager com o SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% tabs local %}
{% tab integração baseada em código %}
### Etapa 1: Instalar a biblioteca do Braze

Você pode instalar a biblioteca Braze usando um dos seguintes métodos. No entanto, se seu site usar um `Content-Security-Policy`, revise a [Política de Segurança de Conteúdo]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) antes de continuar.

{% alert important %}
Embora a maioria dos bloqueadores de anúncios não bloqueie o SDK Braze para Web, alguns bloqueadores de anúncios mais restritivos são conhecidos por causar problemas.
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
{% endsubtab %}
{% endsubtabs %}

### Etapa 2: Inicializar o SDK

Após adicionar o SDK Braze para Web ao seu site, inicialize a biblioteca com a chave de API e [URL do endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) encontrados em **Configurações** > **Configurações do App** dentro do seu painel do Braze. Para uma lista completa de opções para `braze.initialize()`, juntamente com nossos outros métodos JavaScript, consulte [documentação do Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// optionally show all in-app messages without custom handling
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
{% tab antes da inicialização %}
Use `enableLogging` para registrar mensagens básicas de depuração no console JavaScript antes que o SDK seja inicializado.

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

{% tab após a inicialização %}
Use `braze.toggleLogging()` para registrar mensagens básicas de depuração no console JavaScript após a inicialização do SDK. Seu método deve ser semelhante ao seguinte:

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

Ao fazer referência ao Braze Web SDK a partir de nossa rede de fornecimento de conteúdo, por exemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (conforme recomendado por nossas instruções de integração padrão), seus usuários receberão pequenas atualizações (correções de bugs e recursos compatíveis com versões anteriores, versões `a.a.a` a `a.a.z` nos exemplos acima) automaticamente quando atualizarem seu site.

No entanto, quando lançamos alterações importantes, solicitamos que você faça upgrade do SDK da Braze para Web manualmente para garantir que nada em sua integração seja afetado por quaisquer alterações significativas. Além disso, se você baixar nosso SDK e hospedá-lo você mesmo, não receberá nenhuma atualização de versão automaticamente e deverá fazer upgrade manualmente para receber os recursos e as correções de bugs mais recentes.

Mantenha-se atualizado com a versão mais recente [seguindo nosso feed de versões](https://github.com/braze-inc/braze-web-sdk/tags.atom) com o leitor de RSS ou serviço de sua preferência e consulte [nosso changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para obter uma contabilidade completa do histórico de versões do Web SDK. Para fazer upgrade do SDK da Braze para Web:

- Atualize a versão da biblioteca do Braze alterando o número da versão em `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou nas dependências do gerenciador de pacotes.
- Se você tiver o web push integrado, atualize o arquivo do service worker em seu site - por padrão, ele está localizado em `/service-worker.js` no diretório raiz do site, mas o local pode ser personalizado em algumas integrações. Você deve acessar o diretório raiz para hospedar um arquivo de service worker.

Esses dois arquivos devem ser atualizados em coordenação um com o outro para a funcionalidade adequada.

## Outros métodos de integração

### Páginas Móveis Aceleradas (AMP)
{% details Veja mais %}
#### Etapa 1: Incluir script de push para web de AMP

Adicione a seguinte tag de script assíncrono em seu cabeçalho:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Etapa 2: Adicionar widgets de inscrição

Adicione um widget ao corpo do seu HTML que permite aos usuários se inscreverem e cancelarem a inscrição do push.

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

#### Etapa 3: Adicionar `helper-iframe` e `permission-dialog`

O componente AMP Web Push cria um popup para gerenciar inscrições de push, então você precisará adicionar os seguintes arquivos auxiliares ao seu projeto para ativar esse recurso:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Etapa 4: Criar um arquivo de service worker

Crie um arquivo `service-worker.js` no diretório raiz do seu site e adicione o seguinte trecho:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Etapa 5: Configurar o elemento HTML do AMP web push

Adicione o seguinte elemento HTML `amp-web-push` ao corpo do seu HTML. Lembre-se, você precisa anexar seu [`apiKey` e `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parâmetros de consulta para `service-worker-URL`.

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

### Definição de Módulo Assíncrono (AMD)

#### Desativar suporte

Se o seu site usa RequireJS ou outro carregador de módulos AMD, mas você prefere carregar o Braze Web SDK através de uma das outras opções nesta lista, você pode carregar uma versão da biblioteca que não inclui suporte a AMD. Essa versão da biblioteca pode ser carregada no seguinte local da CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Carregador de módulos

Se você usa o RequireJS ou outros carregadores de módulos da AMD, recomendamos que hospede uma cópia da nossa biblioteca e faça referência a ela como faria com outros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

O Electron não oferece suporte oficial a notificações por push na Web (consulte: este [problema no GitHub](https://github.com/electron/electron/issues/6697)). Há outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode tentar e que não foram testadas pelo Braze.

### Framework Jest {#jest}

Ao usar o Jest, você poderá ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração em `package.json` para ignorar o SDK da Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Frameworks SSR {#ssr}

Se você usar um framework de Renderização do Lado do Servidor (SSR) como Next.js, pode encontrar erros porque o SDK foi projetado para ser executado em um ambiente de navegador. Você pode resolver esses problemas importando dinamicamente o SDK.

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

Para obter mais detalhes ou suporte aprofundado à configuração do Tealium, consulte nossa [documentação de integração]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com seu gerente de conta do Tealium.

### Vite {#vite}

Se você usa o Vite e vir um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, talvez seja necessário excluir o SDK da Braze de sua [descoberta de dependências](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Outros gerenciadores de tags

O Braze também pode ser compatível com outras soluções de gerenciamento de tags, seguindo nossas instruções de integração em uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.
