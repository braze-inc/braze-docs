---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour le Web
platform: Web
page_order: 0
page_type: reference
description: "Cet article couvre la configuration initiale du SDK pour le SDK Braze pour le Web."
search_rank: 4
---

# Configuration initiale du SDK

> Cet article de référence explique comment installer le SDK Web de Braze. Le SDK Braze pour le Web vous permet de collecter des analytiques et d’afficher des messages in-app détaillés, des messages de notification push et de carte de contenu à vos utilisateurs Web.

Consultez notre [Documentation JavaScript][9] pour obtenir une référence technique complète.

{% multi_lang_include archive/web-v4-rename.md %}

## Étape 1 : Installer la bibliothèque Braze

Il existe trois manières simples d’intégrer le SDK pour le Web pour inclure des éléments d’analytique et de messagerie sur votre site. Assurez-vous de consulter notre [guide d’intégration des notifications push][16] si vous prévoyez d’utiliser des fonctions de ce type pour le Web.

Si votre site Internet utilise un `Content-Security-Policy`, suivez notre [guide d’en-tête CSP][19] en plus des étapes d’intégration suivantes.

### Option 1 : NPM ou Yarn {#install-npm}

Si votre site utilise des gestionnaires de packages NPM ou Yarn, vous pouvez ajouter le [package NPM Braze](https://www.npmjs.com/package/@braze/web-sdk) en tant que dépendance.

Les définitions TypeScript sont désormais comprises dans la version v3.0.0. Pour obtenir les notes de mise à niveau de 2.x à 3.x, consultez notre [Journal de modifications][17].

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Une fois installé, vous pouvez `import` ou `require` la bibliothèque de la manière habituelle :

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```

### Option 2 : Google Tag Manager {#install-gtm}

Le SDK Braze pour le Web peut être rapidement installé à partir de la bibliothèque de modèles de Google Tag Manager. Deux balises sont prises en charge :

1. Balise d’initialisation : charge le SDK pour le Web sur votre site Internet et définit facultativement l’ID d’utilisateur externe.
2. Balise Actions : utilisée pour déclencher des événements personnalisés, des achats, modifier des ID utilisateur ou basculer le suivi du SDK.

Consultez le [guide d’intégration de Google Tag Manager][18] pour plus d’informations.

### Option 3 : Braze CDN {#install-cdn}

Ajoutez le SDK Braze pour le Web directement à votre code HTML en faisant référence à notre script hébergé par le CDN (réseau de diffusion de contenu), qui charge la bibliothèque asynchrone.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>


## Étape 2 : Initialiser Braze

Une fois que le SDK Braze pour le Web est ajouté à votre site Internet, initialisez la bibliothèque avec `API Key` et l’[URL de l’endpoint du SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) trouvé dans **Gestion des paramètres > Paramètres** dans votre tableau de bord de Braze.

{% alert note %}
Si vous avez configuré vos options d’initialisation Braze dans un gestionnaire de balises, vous pouvez ignorer cette étape.
{% endalert %}

Pour une liste complète des options pour `braze.initialize()` consultez notre [documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

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

// optionally set the current user's External ID
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// Be sure to call `openSession` after `automaticallyShowInAppMessages`
braze.openSession();
```

Consultez notre [documentation de référence JavaScript][9] pour toutes les autres méthodes JavaScript.

{% alert note %}
Les utilisateurs anonymes sur les appareils mobiles ou Web peuvent être comptés dans vos [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}

## Étape 3 : Notification push pour le Web (en option)

Une configuration supplémentaire est requise pour utiliser les notifications push pour le Web. Consultez [Notifications push][16] pour obtenir des instructions.

## Résolution des problèmes{#error-logging}

Pour faciliter la résolution des problèmes, vous pouvez activer la journalisation verbeuse dans le SDK. Cela est utile pour le développement, mais est visible pour tous les utilisateurs. Vous devriez donc supprimer cette option ou fournir un autre enregistreur avec `braze.setLogger()` dans votre environnement de production.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true
});

// or, after initialization:

braze.toggleLogging()
```

Si vous utilisez un cadre de rendu côté serveur, consultez nos étapes d’intégration supplémentaires pour intégrer[Vite](#vite) ou d’autres [cadres SSR](#ssr)


## Mise à niveau du SDK

{% multi_lang_include archive/web-v4-rename.md %}

Lorsque vous consultez le SDK Braze pour le Web de notre réseau de diffusion de contenu, par exemple, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (tel que recommandé par nos instructions d’intégration par défaut), vos utilisateurs recevront des mises à jour mineures (correctifs de bogues et fonctions rétrocompatibles, versions) `a.a.a` par `a.a.z` dans les exemples ci-dessus) automatiquement lorsqu’ils actualisent votre site.

Cependant, lorsque nous publions des changements majeurs, nous vous demandons de mettre à niveau manuellement le SDK Braze pour le Web afin de vous assurer que rien dans votre intégration ne sera affecté par des pannes. De plus, si vous téléchargez notre SDK et l’hébergez vous-même, vous ne recevrez aucune mise à jour automatique et vous devrez le mettre à niveau manuellement pour obtenir les dernières fonctionnalités et corrections de bogues.

Vous pouvez vous maintenir à jour avec notre dernière version [en suivant notre flux de versions](https://github.com/braze-inc/braze-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix et consulter [notre journal de modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) pour une description complète de notre historique de versions SDK pour le Web. Pour mettre à niveau le SDK Braze pour le Web :

- Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou dans les dépendances de votre responsable de packages.
- Si vous avez intégré des notifications push pour le Web, mettez à jour le fichier du service de traitement sur votre site. Par défaut, ce paramètre est situé à `/service-worker.js` dans le répertoire racine de votre site, mais l’emplacement peut être personnalisé dans certaines intégrations. Vous devez accéder au répertoire racine pour héberger un fichier de service de traitement.

Ces deux fichiers doivent être mis à jour en coordination les uns avec les autres afin de garantir une fonctionnalité appropriée.

## Méthodes d’intégration alternatives

### Cadres de rendu côté serveur {#ssr}

Si vous utilisez un cadre de rendu côté serveur comme Next.js, vous pourriez rencontrer des erreurs, car le SDK est conçu pour être exécuté dans un environnement de navigateur. Vous pouvez résoudre ces problèmes en important le SDK de façon dynamique.

Vous pouvez conserver les bénéfices du nettoyage lorsque vous y procédez en exportant les parties du SDK dont vous avez besoin dans un fichier séparé et en important ensuite de façon dynamique ce fichier dans votre composant.

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

Alternativement, si vous utilisez un pack Web pour regrouper votre application, vous pouvez tirer parti de ses commentaires magiques pour importer de façon dynamique uniquement les parties du SDK dont vous avez besoin.

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

### Prise en charge de Vite {#vite}

Si vous utilisez Vite et voyez un avertissement autour des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous pourriez devoir exclure le SDK de Braze de sa [découverte de dépendance](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) :

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Prise en charge d’Electron {#electron}

Electron ne prend pas officiellement en charge les notifications push Web (voir : ce [problème GitHub](https://github.com/electron/electron/issues/6697)). Il existe d’autres [solutions de contournement open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pourriez essayer et qui n’ont pas été testées par Braze.

### Chargeur de module AMD

Si vous utilisez RequireJS ou d’autres chargeurs de module AMD, nous vous recommandons d’auto-héberger une copie de notre bibliothèque et de la référencer comme vous le feriez avec d’autres ressources :

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### Autre installation sans AMD

Si votre site utilise RequireJS ou un autre chargeur de module AMD, mais que vous préférez charger le SDK Braze pour le Web via l’une des autres options ci-dessus, vous pouvez charger une version de la bibliothèque qui n’inclut pas le support AMD. Il est possible de charger cette version de la bibliothèque depuis l’endroit suivant du CDN :

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ propose une intégration de base de Braze. Pour configurer l’intégration, recherchez Braze dans l’interface Tealium Tag Management et fournissez la clé API du SDK pour le Web à partir de votre tableau de bord.

Pour plus de détails ou pour obtenir de l’aide sur la configuration de Tealium, consultez notre [document d’intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

### Autres gestionnaires de balises
Braze peut également être compatible avec d’autres solutions de gestion des balises en suivant nos instructions d’intégration au sein d’une balise HTML personnalisée. Contactez un conseiller Braze si vous avez besoin d’aide pour évaluer ces solutions.

### Résolution des problèmes du cadre Jest {#jest}

Lorsque vous utilisez Jest, vous pouvez visualiser une erreur similaire à `SyntaxError: Unexpected token 'export'`. Pour la réparer, ajustez votre configuration dans `package.json` pour ignorer le Braze SDK :

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

[9]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs"
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[17]: https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/
<!-- wesley wanted an empty line at the end -->
