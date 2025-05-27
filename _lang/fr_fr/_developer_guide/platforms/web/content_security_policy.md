---
nav_title: En-têtes de la politique de sécurité du contenu
article_title: En-têtes de la politique de sécurité du contenu pour le Web
platform: Web
page_order: 21
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

### `connect-src` {#connect-src}

{% alert warning %}
Votre URL doit correspondre à l'[endpoint du SDK API]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) de l'option d'initialisation `baseUrl` que vous avez choisie.
{% endalert %}

|URL|Information|
|---|-----------|
|`connect-src https://sdk.iad-01.braze.com`|Permet au SDK de communiquer avec les API de Braze. Modifiez cette URL pour qu'elle corresponde au [point d'endpoint du SDK API]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) pour l'option d'initialisation `baseUrl` que vous avez choisie.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `script-src` {#script-src}

|URL|Information|
|---|-----------|
|`script-src https://js.appboycdn.com`|Requis lors de l'utilisation de l'intégration hébergée par le réseau diffusion de contenu.|
|`script-src 'unsafe-eval'`|Requis lors de l'utilisation de l'extrait de code d'intégration qui contient une référence à `appboyQueue`. Pour éviter d'utiliser cette directive, [intégrez le SDK à l'aide de NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager).|
|`script-src 'nonce-...'`<br>ou<br>`script-src 'unsafe-inline'`|Requis pour certains messages in-app, tels que le HTML personnalisé.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `img-src` {#img-src}

|URL|Information|
|---|-----------|
|`img-src: appboy-images.com braze-images.com cdn.braze.eu`|Requis lors de l'utilisation d'images hébergées par le réseau de diffusion de Braze. Les noms d'hôte peuvent varier en fonction du tableau de bord.<br><br>**Important :** Si vous utilisez des polices personnalisées, vous devez également inclure `font-src`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` ou `style-src 'unsafe-inline'`
