---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK Web de Braze
platform: Web
page_order: 0
page_type: reference
---

# Configuration initiale du SDK pour le web

> Cet article de référence explique comment installer le SDK Web de Braze. Le SDK Braze pour le Web vous permet de collecter des analyses et d’afficher des messages in-app détaillés, des messages de notification push et de carte de contenu à vos utilisateurs Web. Consultez notre [documentation ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JavaScriptJSDocs") pour une référence technique complète.

{% multi_lang_include archive/web-v4-rename.md %}

## Étape 1 : Installer la bibliothèque Braze

Vous pouvez installer la bibliothèque Braze en utilisant l'une des méthodes suivantes. Si votre site web utilise un `Content-Security-Policy`, consultez notre [guide sur les en-têtes de la politique de sécurité du contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/) avant d'installer la bibliothèque.

{% alert important %}
La plupart des bloqueurs de publicités ne bloqueront pas le SDK Web de Braze, mais certains bloqueurs de publicités plus restrictifs sont connus pour causer des problèmes.
{% endalert %}

{% tabs local %}
{% tab gestionnaire de paquets %}
Si votre site utilise les gestionnaires de paquets NPM ou Yarn, vous pouvez ajouter le [paquet NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) comme dépendance.

Les définitions TypeScript sont désormais comprises dans la version v3.0.0. Pour obtenir les notes sur la mise à jour de 2.x vers 3.x, consultez notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

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
{% endtab %}

{% tab Google Tag Manager %}
Le SDK Web de Braze peut être installé à partir de la bibliothèque de modèles de Google Tag Manager. Deux balises sont prises en charge :

1. Balise d’initialisation : charge le SDK pour le Web sur votre site Internet et définit facultativement l’ID d’utilisateur externe.
2. Balise Actions : utilisée pour déclencher des événements personnalisés, des achats, modifier des ID utilisateur ou basculer le suivi du SDK.

Consultez le [guide d'intégration de Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/) pour plus d'informations.
{% endtab %}

{% tab Braze cdn %}
Ajoutez le SDK Braze pour le Web directement à votre code HTML en faisant référence à notre script hébergé par le CDN (réseau de diffusion de contenu), qui charge la bibliothèque asynchrone.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## Étape 2 : Initialiser le SDK

Une fois le SDK Web de Braze ajouté à votre site Web, initialisez la bibliothèque à l'aide de la clé API et de l'[URL de l'endpoint du SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que vous trouverez dans **Paramètres** > **Paramètres de l'application** dans votre tableau de bord de Braze.

{% alert note %}
Si vous avez configuré vos options d’initialisation Braze dans un gestionnaire de balises, vous pouvez ignorer cette étape.
{% endalert %}

Pour obtenir une liste complète des options de `braze.initialize()`, ainsi que de nos autres méthodes JavaScript, consultez notre [documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

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
Les utilisateurs anonymes sur des appareils mobiles ou web peuvent être comptabilisés dans votre [MAU.]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}

## Étape 3 : Configurer les notifications push (facultatif)

Pour configurer les notifications push pour le SDK Web de Braze, une configuration supplémentaire est nécessaire. Pour une présentation complète, consultez les [notifications push pour le Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/).

## Journalisation

Pour activer rapidement la journalisation, vous pouvez ajouter `?brazeLogging=true` comme paramètre à l'URL de votre site web. Vous pouvez également activer la journalisation de [base](#basic-logging) ou [personnalisée](#custom-logging).

### Journalisation de base

{% tabs local %}
{% tab avant l'initialisation %}
Utilisez `enableLogging` pour enregistrer les messages de débogage de base dans la console javascript avant l'initialisation du SDK.

```javascript
enableLogging: true
```

Votre méthode doit être similaire à la suivante :

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab après l'initialisation %}
Utilisez `braze.toggleLogging()` pour enregistrer des messages de débogage de base dans la console javascript après l'initialisation du SDK. Votre méthode doit être similaire à la suivante :

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
Les journaux de base sont visibles par tous les utilisateurs, il faut donc envisager de les désactiver ou de passer à [`setLogger`](#custom-logging)avant de mettre votre code en production.
{% endalert %}

### Journalisation personnalisée

Utilisez `setLogger` pour enregistrer des messages de débogage personnalisés dans la console javascript. Contrairement aux journaux de base, ces journaux ne sont pas visibles par les utilisateurs.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Remplacez `STRING` par votre message sous la forme d'une chaîne de caractères unique. Votre méthode doit être similaire à la suivante :

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Mise à niveau du SDK

{% multi_lang_include archive/web-v4-rename.md %}

Lorsque vous consultez le SDK Braze pour le Web de notre réseau de diffusion de contenu, par exemple, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (tel que recommandé par nos instructions d’intégration par défaut), vos utilisateurs recevront des mises à jour mineures (correctifs de bogues et fonctions rétrocompatibles, versions) `a.a.a` par `a.a.z` dans les exemples ci-dessus) automatiquement lorsqu’ils actualisent votre site.

Cependant, lorsque nous publions des changements majeurs, nous vous demandons de mettre à niveau manuellement le SDK Braze pour le Web afin de vous assurer que rien dans votre intégration ne sera affecté par des pannes. De plus, si vous téléchargez notre SDK et l’hébergez vous-même, vous ne recevrez aucune mise à jour automatique et vous devrez le mettre à niveau manuellement pour obtenir les dernières fonctionnalités et corrections de bogues.

Vous pouvez vous tenir au courant de notre dernière version [en suivant notre flux de publication](https://github.com/braze-inc/braze-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix, et consulter [notre journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) pour un compte-rendu complet de l'historique des versions de notre SDK Web. Pour mettre à niveau le SDK Braze pour le Web :

- Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou dans les dépendances de votre responsable de packages.
- Si vous avez intégré des notifications push pour le Web, mettez à jour le fichier du service de traitement sur votre site. Par défaut, ce paramètre est situé à `/service-worker.js` dans le répertoire racine de votre site, mais l’emplacement peut être personnalisé dans certaines intégrations. Vous devez accéder au répertoire racine pour héberger un fichier de service de traitement.

Ces deux fichiers doivent être mis à jour en coordination l'un avec l'autre pour fonctionner correctement.

## Méthodes d’intégration alternatives

### Cadres de rendu côté serveur {#ssr}

Si vous utilisez un framework de rendu côté serveur comme Next.js, vous pourriez rencontrer certaines erreurs, car le SDK est conçu pour être exécuté dans un environnement de navigateur. Vous pouvez résoudre ces problèmes en important le SDK de façon dynamique.

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

Electron ne prend pas officiellement en charge les notifications push Web (voir ce [problème GitHub](https://github.com/electron/electron/issues/6697)). Il existe d'autres [solutions de contournement open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pouvez essayer mais qui n'ont pas été testées par Braze.

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

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ propose une intégration de base de Braze. Pour configurer l’intégration, recherchez Braze dans l’interface Tealium Tag Management et fournissez la clé API du SDK pour le Web à partir de votre tableau de bord.

Pour plus de détails ou une assistance approfondie sur la configuration de Tealium, consultez notre [documentation sur l'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

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
