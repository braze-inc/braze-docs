## À propos du SDK de Braze

Le SDK Web Braze vous permet de collecter des analyses/analytiques et d'afficher des messages in-app riches, des messages push et des cartes de contenu à vos utilisateurs web. Pour plus d'informations, consultez la [documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Intégration du SDK Web

Vous pouvez intégrer le SDK de Braze Web à l'aide des méthodes suivantes. Pour d'autres options, voir les [autres méthodes d'intégration](#web_other-integration-methods).

- **L'intégration basée sur le code :** Intégrez le SDK Braze directement dans votre base de code à l'aide de votre gestionnaire de paquets préféré ou du réseau de diffusion de Braze. Vous aurez ainsi un contrôle total sur le chargement et la configuration du SDK.
- **Google Tag Manager :** Une solution sans code qui vous permet d'intégrer le SDK de Braze sans modifier le code de votre site. Pour plus d'informations, consultez [Google Tag Manager avec le SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% tabs local %}
{% tab l'intégration basée sur le code %}
### Étape 1 : Installer la bibliothèque Braze

Vous pouvez installer la bibliothèque Braze en utilisant l'une des méthodes suivantes. Toutefois, si votre site web utilise un site `Content-Security-Policy`, examinez la [politique de sécurité du contenu]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) avant de continuer.

{% alert important %}
La plupart des bloqueurs de publicité ne bloqueront pas le SDK Braze Web, mais certains bloqueurs de publicité plus restrictifs sont connus pour causer des problèmes.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
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
{% endsubtab %}

{% subtab braze cdn %}
Ajoutez le SDK Braze pour le Web directement à votre code HTML en faisant référence à notre script hébergé par le CDN (réseau de diffusion de contenu), qui charge la bibliothèque asynchrone.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endsubtab %}
{% endsubtabs %}

### Étape 2 : Initialiser le SDK

Une fois le SDK Web de Braze ajouté à votre site Web, initialisez la bibliothèque à l'aide de la clé API et de l'[URL de l'endpoint du SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que vous trouverez dans **Paramètres** > **Paramètres de l'application** dans votre tableau de bord de Braze. Pour obtenir une liste complète des options de `braze.initialize()`, ainsi que de nos autres méthodes JavaScript, consultez la [documentation JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

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
Les utilisateurs anonymes sur des appareils mobiles ou web peuvent être comptabilisés dans votre [MAU.]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Configurations optionnelles

### Journalisation

Pour activer rapidement la journalisation, vous pouvez ajouter `?brazeLogging=true` comme paramètre à l'URL de votre site web. Vous pouvez également activer la journalisation de [base](#web_basic-logging) ou [personnalisée](#web_custom-logging).

#### Journalisation de base

{% tabs local %}
{% tab avant l'initialisation %}
Utilisez `enableLogging` pour enregistrer des messages de débogage de base dans la console JavaScript avant l'initialisation du SDK.

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
Utilisez `braze.toggleLogging()` pour enregistrer des messages de débogage de base dans la console JavaScript après l'initialisation du SDK. Votre méthode doit être similaire à la suivante :

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
Les journaux de base sont visibles par tous les utilisateurs, il faut donc envisager de les désactiver ou de passer à [`setLogger`](#web_custom-logging)avant de mettre votre code en production.
{% endalert %}

#### Journalisation personnalisée

Utilisez `setLogger` pour enregistrer des messages de débogage personnalisés dans la console JavaScript. Contrairement aux journaux de base, ces journaux ne sont pas visibles par les utilisateurs.

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

## Autres méthodes d'intégration

### Pages mobiles accélérées (AMP)
{% details Voir plus d'informations %}
#### Étape 1 : Inclure le script de notification push pour le Web en AMP

Ajoutez la balise de script asynchrone suivante à votre en-tête :

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Étape 2 : Ajouter des widgets d'abonnement

Ajoutez un widget dans le corps de votre HTML qui permet aux utilisateurs de s'abonner et de se désabonner de push.

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

#### Étape 3 : Ajoutez `helper-iframe` et `permission-dialog`

Le composant AMP Web Push crée une fenêtre contextuelle pour gérer les abonnements push. Vous devrez donc ajouter les fichiers d'aide suivants à votre projet pour activer cette fonctionnalité :

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Étape 4 : Créer un fichier de service de traitement

Créez un fichier `service-worker.js` dans le répertoire racine de votre site web et ajoutez l'extrait de code suivant :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Étape 5 : Configurer l’élément HTML des notifications push pour le Web en AMP

Ajoutez l'élément HTML `amp-web-push` suivant au corps de votre HTML. Gardez à l'esprit que vous devez ajouter vos [`apiKey` et `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) en tant que paramètres de requête à `service-worker-URL`.

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

### Définition du module asynchrone (AMD)

#### Désactiver le soutien

Si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK Braze via l'une des autres options de cette liste, vous pouvez charger une version de la bibliothèque qui n'inclut pas la prise en charge AMD. Il est possible de charger cette version de la bibliothèque depuis l’endroit suivant du CDN :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Chargeur de modules

Si vous utilisez RequireJS ou d’autres chargeurs de module AMD, nous vous recommandons d’auto-héberger une copie de notre bibliothèque et de la référencer comme vous le feriez avec d’autres ressources :

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron ne prend pas officiellement en charge les notifications push Web (voir ce [problème GitHub](https://github.com/electron/electron/issues/6697)). Il existe d'autres [solutions de contournement open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pouvez essayer mais qui n'ont pas été testées par Braze.

### Cadre Jest {#jest}

Lorsque vous utilisez Jest, vous pouvez visualiser une erreur similaire à `SyntaxError: Unexpected token 'export'`. Pour la réparer, ajustez votre configuration dans `package.json` pour ignorer le Braze SDK :

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Cadres de la RSS {#ssr}

Si vous utilisez un cadre de rendu côté serveur (SSR) tel que Next.js, vous risquez de rencontrer des erreurs car le SDK est conçu pour être exécuté dans un environnement de navigateur. Vous pouvez résoudre ces problèmes en important le SDK de façon dynamique.

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

### Tealium iQ

Tealium iQ propose une intégration de base de Braze. Pour configurer l’intégration, recherchez Braze dans l’interface Tealium Tag Management et fournissez la clé API du SDK pour le Web à partir de votre tableau de bord.

Pour plus de détails ou une assistance approfondie sur la configuration de Tealium, consultez notre [documentation sur l'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

### Vite {#vite}

Si vous utilisez Vite et voyez un avertissement autour des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous pourriez devoir exclure le SDK de Braze de sa [découverte de dépendance](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) :

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Autres gestionnaires de balises

Braze peut également être compatible avec d’autres solutions de gestion des balises en suivant nos instructions d’intégration au sein d’une balise HTML personnalisée. Contactez un conseiller Braze si vous avez besoin d’aide pour évaluer ces solutions.
