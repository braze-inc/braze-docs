---
nav_title: Politique de sécurité du contenu
article_title: En-têtes de politique de sécurité du contenu pour le Web
platform: Web
page_order: 25
page_type: Référence
description: "Cet article couvre les en-têtes des politiques Content-Security-Policy nécessaires avec le Braze Web SDK"
---

# En-têtes de la politique de sécurité du contenu

Content-Security-Policy fournit une sécurité supplémentaire en limitant la façon et le lieu de chargement du contenu sur votre site Web.

{% alert important %}
Cet article est destiné aux développeurs travaillant sur des sites web qui appliquent les règles CSP, et comment s'intégrer au Brésil. Il ne s'agit pas de conseils sur la façon dont vous devriez aborder la sécurité.
{% endalert %}

## Attributs Nonce {#nonce}

Si vous utilisez une valeur `nonce` dans vos directives `script-src` ou `style-src` , transmettent cette valeur à l'option d'initialisation `contentSecurityNonce` pour la propager à des scripts et styles nouvellement créés générés par le SDK.

```javascript
import braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assume une valeur CSP "nonce-YOUR-NONCE-HERE"
});
```

## Directives {#directives}

### connect-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com` - permet au SDK de communiquer avec les API Braze.
  - Changez cette URL pour qu'elle corresponde à votre `baseUrl` d'initialisation API Endpoint, comme trouvé [ici](https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints/).

### script-src {#script-src}

- `script-src https://js.appboycdn.com` - requis lors de l'utilisation de l'intégration hébergée sur CDN.
- `script-src 'unsafe-eval'` - demandé uniquement lors de l'intégration snippet qui contient des références à `appboyQueue`
  - Pour éviter d'utiliser cette directive, intégrez plutôt en utilisant NPM.
- `script-src 'nonce-...'` ou `script-src 'unsafe-inline'` sont requis pour certains messages In-App (HTML personnalisé, par exemple).

### img-src {#img-src}
- `img-src : appboy-images.com braze-images.com cdn.braze.eu` - requis lors de l'utilisation des images hébergées par Braze CDN. Ces noms d'hôtes peuvent varier en fonction du cluster du tableau de bord.

## Génial {#font-awesome}

Pour désactiver l'inclusion automatique de Font Awesome, utilisez l'option d'initialisation `doNotLoadFontAwesome`:

```javascript
importer le braze depuis "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Si vous choisissez d'utiliser Font Awesome, les directives CSP suivantes sont requises :

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` ou `style-src 'unsafe-inline'` sont également requis.
- `font-src https://use.fontawesome.com`
