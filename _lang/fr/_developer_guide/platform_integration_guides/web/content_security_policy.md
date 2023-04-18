---
nav_title: En-têtes de la politique de sécurité du contenu
article_title: En-têtes de la politique de sécurité du contenu pour le Web
platform: Web
page_order: 25
page_type: reference
description: "Cet article couvre les en-têtes de la politique de sécurité du contenu nécessaires au SDK Braze pour le Web."

---

# En-têtes de la politique de sécurité du contenu

> La politique de sécurité du contenu fournit une sécurité supplémentaire en limitant la manière dont le contenu peut être chargé sur votre site Internet. Cet article de référence explique quels en-têtes de la politique de sécurité du contenu sont nécessaires avec le SDK Web.

{% alert important %}
Cet article est destiné aux développeurs travaillant sur des sites Web qui appliquent des règles CSP et s’intègrent à Braze. Il n’est pas destiné à donner des conseils sur la manière dont vous devez aborder la sécurité.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Attributs Nonce {#nonce}

Si vous utilisez une valeur `nonce` dans votre `script-src` ou vos directives `style-src`, transmettez cette valeur à l’option d’initialisation `contentSecurityNonce` pour la propager aux scripts et styles nouvellement créés générés par le SDK :

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Directives {#directives}

### connexion-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com` : permet au SDK de communiquer avec les API Braze.
  - Modifiez cette URL pour la faire correspondre à votre `baseUrl` des options d’initialisation de l’[endpoint du SDK de l’API]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### script-src {#script-src}

- `script-src https://js.appboycdn.com` : requis lors de l’utilisation d’une intégration hébergée par le CDN (réseau de diffusion de contenu).
- `script-src 'unsafe-eval'` : requis lors de l’utilisation de l’extrait de code d’intégration qui contient une référence à `appboyQueue`
  - Pour éviter d’utiliser cette directive, intégrez plutôt à l’aide de NPM.
- `script-src 'nonce-...'` ou `script-src 'unsafe-inline'` : requis pour certains messages in-app (par exemple, HTML personnalisé).

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu` : requis lors de l’utilisation d’images hébergées par Braze CDN. Ces noms d’hôte peuvent varier en fonction du cluster de tableau de bord.

## Font Awesome {#font-awesome}

Pour désactiver l’inclusion automatique de Font Awesome, utilisez l’option d’initialisation `doNotLoadFontAwesome` :

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Si vous choisissez d’utiliser Font Awesome, les directives CSP suivantes sont requises :

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` ou `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
