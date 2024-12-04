---
nav_title: Cabeçalhos de política de segurança de conteúdo
article_title: Cabeçalhos de política de segurança de conteúdo para a Web
platform: Web
page_order: 25
page_type: reference
description: "Este artigo aborda os cabeçalhos de política de segurança de conteúdo necessários com o Braze Web SDK."

---

# Cabeçalhos de política de segurança de conteúdo

> A Content-Security-Policy oferece segurança adicional ao restringir como e onde o conteúdo pode ser carregado em seu site. Este artigo de referência aborda quais cabeçalhos de política de segurança de conteúdo são necessários com o Web SDK.

{% alert important %}
Este artigo é destinado a desenvolvedores que trabalham em sites que aplicam regras de CSP e se integram ao Braze. Não se trata de um conselho sobre como você deve abordar a segurança.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Atribuições de nonce {#nonce}

Se você usar um valor `nonce` nas diretivas `script-src` ou `style-src`, passe esse valor para a opção de inicialização `contentSecurityNonce` para propagá-lo para scripts e estilos recém-criados gerados pelo SDK:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Diretrizes {#directives}

### connect-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com`: permite que o SDK se comunique com as APIs da Braze.
  - Altere esse URL para corresponder ao [endpoint de SDK da API]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) de sua opção de inicialização `baseUrl`.

### script-src {#script-src}

- `script-src https://js.appboycdn.com`: necessário ao usar a integração hospedada por CDN.
- `script-src 'unsafe-eval'`: obrigatório ao usar o snippet de integração que contém referência a `appboyQueue`
  - Para evitar o uso dessa diretriz, faça a integração usando o NPM.
- `script-src 'nonce-...'` ou `script-src 'unsafe-inline'`: obrigatório para determinadas mensagens no app (por exemplo, HTML personalizado).

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu`: obrigatório ao usar imagens hospedadas pelo Braze CDN. Esses nomes de host podem variar de acordo com o cluster do dashboard.

## Font Awesome {#font-awesome}

Para desativar a inclusão automática da Font Awesome, use a opção de inicialização `doNotLoadFontAwesome`:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Se você optar por usar a Font Awesome, as seguintes diretivas do CSP serão necessárias:

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` ou `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
