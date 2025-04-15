---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do Braze Web SDK
platform: Web
page_order: 0
page_type: reference
---

# Configuração inicial do SDK para a Web

> Este artigo de referência aborda como instalar o SDK da Braze para Web. O SDK da Braze para Web permite que você colete análises de dados e exiba mensagens no app, push e mensagens de cartão de conteúdo para seus usuários da Internet. Consulte nossa [Documentação ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JavaScriptJSDocs") para obter uma referência técnica completa.

{% multi_lang_include archive/web-v4-rename.md %}

## Etapa 1: Instalar a biblioteca do Braze

Você pode instalar a biblioteca Braze usando um dos seguintes métodos. Se o seu site usa um `Content-Security-Policy`, consulte nosso [guia de cabeçalhos de política de segurança de conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/) antes de instalar a biblioteca.

{% alert important %}
Embora a maioria dos bloqueadores de anúncios não bloqueie o SDK da Braze para Web, sabe-se que alguns mais restritivos podem causar problemas.
{% endalert %}

{% tabs local %}
{% tab gerenciador de pacotes %}
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
{% endtab %}

{% tab Google Tag Manager %}
O SDK da Braze para Web pode ser instalado a partir da biblioteca de modelos do Google Tag Manager. Há suporte para duas tags:

1. Tag de inicialização: carrega o SDK para Web no seu site e, opcionalmente, define a ID de usuário externo.
2. Tag Actions: usada para disparar eventos personalizados, compras, alterar IDs de usuário ou alternar o rastreamento do SDK.

Visite o [guia de integração do Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/) para saber mais.
{% endtab %}

{% tab Braze cdn %}
Adicione o SDK da Braze para Web diretamente ao seu HTML fazendo referência ao nosso script hospedado na CDN, que carrega a biblioteca de forma assíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## Etapa 2: Inicializar o SDK

Depois que o SDK da Braze para Web for adicionado ao seu site, inicialize a biblioteca com a chave de API e [o endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) encontrados em **Configurações** > **App Configurações de app** em seu dashboard da Braze.

{% alert note %}
Se tiver configurado suas opções de inicialização da Braze em um Tag Manager, você poderá pular esta etapa.
{% endalert %}

Para obter uma lista completa de opções para `braze.initialize()`, juntamente com nossos outros métodos JavaScript, consulte nossa [documentação JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
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

## Etapa 3: Configure as notificações por push (opcional)

Para configurar notificações por push para o SDK da Braze para Web, é necessária uma configuração adicional. Para obter um passo a passo completo, consulte [Notificações por push para web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/).

## Registro

Para ativar rapidamente o registro, adicione `?brazeLogging=true` como um parâmetro ao URL do seu site. Como alternativa, é possível ativar o registro [básico](#basic-logging) ou [personalizado](#custom-logging).

### Registro básico

{% tabs local %}
{% tab antes da inicialização %}
Use `enableLogging` para registrar mensagens básicas de depuração no console javascript antes de o SDK ser inicializado.

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
Use `braze.toggleLogging()` para registrar mensagens básicas de depuração no console javascript depois que o SDK for inicializado. Seu método deve ser semelhante ao seguinte:

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
Os registros básicos são visíveis para todos os usuários, portanto, considere desativar ou mudar para [`setLogger`](#custom-logging)antes de liberar seu código para produção.
{% endalert %}

### Registro personalizado

Use `setLogger` para registrar mensagens de depuração personalizadas no console javascript. Ao contrário dos registros básicos, esses registros não são visíveis para os usuários.

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

## Métodos alternativos de integração

### Estruturas de renderização no lado do servidor {#ssr}

Se você usar uma estrutura de renderização no lado do servidor, como Next.js, poderá encontrar erros, pois o SDK foi criado para ser executado em um ambiente de navegador. Você pode resolver esses problemas importando dinamicamente o SDK.

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

### Suporte do Vite {#vite}

Se você usa o Vite e vir um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, talvez seja necessário excluir o SDK da Braze de sua [descoberta de dependências](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Suporte do Electron {#electron}

O Electron não oferece suporte oficial a notificações por push na Web (consulte: este [problema no GitHub](https://github.com/electron/electron/issues/6697)). Há outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode tentar e que não foram testadas pelo Braze.

### Carregador de módulos AMD

Se você usa o RequireJS ou outros carregadores de módulos da AMD, recomendamos que hospede uma cópia da nossa biblioteca e faça referência a ela como faria com outros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### Alternativa Sem instalação de AMD

Se o seu site usa o RequireJS ou outro carregador de módulos da AMD, mas você prefere carregar o Braze Web SDK por meio de uma das outras opções acima, é possível carregar uma versão da biblioteca que não inclua o suporte da AMD. Essa versão da biblioteca pode ser carregada no seguinte local da CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
O Tealium iQ oferece uma integração básica do Braze pronta para uso. Para configurar a integração, procure o Braze na interface do Tealium Tag Management e forneça a chave de API do Web SDK em seu dashboard.

Para obter mais detalhes ou suporte aprofundado à configuração do Tealium, consulte nossa [documentação de integração]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com seu gerente de conta do Tealium.

### Outros gerenciadores de tags
O Braze também pode ser compatível com outras soluções de gerenciamento de tags, seguindo nossas instruções de integração em uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.

### Solução de problemas da estrutura Jest {#jest}

Ao usar o Jest, você poderá ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração em `package.json` para ignorar o SDK da Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```
