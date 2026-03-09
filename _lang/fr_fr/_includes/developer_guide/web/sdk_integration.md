## À propos du SDK Web Braze

Le SDK Web Braze vous permet de collecter des données analytiques et d'afficher des messages in-app enrichis, des notifications push et des messages de carte de contenu à vos utilisateurs Web. Pour plus d'informations, veuillez consulter [la documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Intégrer le SDK Web

Vous pouvez intégrer le SDK Web Braze en utilisant les méthodes suivantes. Pour des options supplémentaires, veuillez consulter [les autres méthodes d'intégration](#web_other-integration-methods).

- **Intégration basée sur le code :** Intégrez le SDK Web Braze directement dans votre base de code à l'aide de votre gestionnaire de paquets préféré ou du réseau de diffusion de contenu Braze. Cela vous permet de contrôler entièrement le chargement et la configuration du SDK.
- **Google Tag Manager:** Une solution sans code qui vous permet d'intégrer le SDK Web Braze sans modifier le code de votre site. Pour plus d'informations, veuillez consulter [Google Tag Manager avec le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% alert important %}
Nous recommandons d'utiliser la [méthode d'intégration NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Les avantages comprennent le stockage local des bibliothèques SDK sur votre site web, l'immunité contre les extensions de blocage des publicités et la contribution à des temps de chargement plus rapides dans le cadre de la prise en charge des bundlers.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Étape 1 : Installer la bibliothèque Braze

Vous pouvez installer la bibliothèque Braze en utilisant l'une des méthodes suivantes. Toutefois, si votre site Web utilise un `Content-Security-Policy`, veuillez examiner la [politique de sécurité du contenu]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) avant de poursuivre.

{% alert important %}
Bien que la plupart des bloqueurs de publicités ne bloquent pas le SDK Web Braze, certains bloqueurs plus restrictifs sont connus pour causer des problèmes.
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

{% alert important %}
Le paramètre par défaut **« Empêcher le suivi intersites** » dans Safari peut empêcher l'affichage de certains types de messages in-app, tels que les bannières et les cartes de contenu de type bannière, lorsque vous utilisez la méthode d'intégration du réseau de diffusion de contenu. Pour éviter ce problème, veuillez utiliser la méthode d'intégration NPM afin que Safari ne classe pas ces messages comme du trafic intersite et que vos utilisateurs Web puissent les voir dans tous les navigateurs web pris en charge.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Étape 2 : Initialiser le SDK

Une fois le SDK Web Braze ajouté à votre site Web, veuillez initialiser la bibliothèque à l'aide de la clé API et de [l'URL de l'endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) disponibles dans **Paramètres** > **Paramètres de l'application** dans votre tableau de bord de Braze. Pour obtenir la liste complète des options disponibles`braze.initialize()`, ainsi que nos autres méthodes JavaScript, veuillez consulter [la documentation JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Les domaines personnalisés pour les requêtes Web SDK ne sont pas pris en charge** : Le SDK Web`baseUrl` doit être un endpoint du SDK Braze (par exemple, `sdk.iad-05.braze.com`). Braze ne prend pas en charge le routage du trafic Web SDK via un domaine appartenant au client à l'aide d'enregistrements CNAME. Si vous avez besoin que les requêtes Web SDK proviennent de votre propre domaine, veuillez contacter le service d'assistance Braze.
{% endalert %}

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
**Affichage des messages in-app** : Pour afficher automatiquement les messages in-app lorsqu'ils sont déclenchés, il est nécessaire d'appeler `braze.automaticallyShowInAppMessages()`. Sans cet appel, les messages in-app ne s'affichent pas automatiquement. Si vous souhaitez gérer manuellement l'affichage des messages, veuillez supprimer cet appel et utiliser`braze.subscribeToInAppMessage()`à la place. Pour plus d'informations, veuillez consulter [la section Réception/distribution de messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/delivery/).
{% endalert %}

#### Résolution des problèmes de sessions manquantes pour les utilisateurs anonymes

Si vous constatez un comportement « Session manquante » ou si vous n'êtes pas en mesure de suivre la session des utilisateurs anonymes sur le Web, veuillez vous assurer que votre intégration appelle`braze.openSession()`  lors de l'initialisation.

- **Scénario :** Les utilisateurs anonymes peuvent renvoyer un ID de Braze, mais les données de session sont vides ou manquantes.
- **Cause :** L'implémentation n'appelle pas`braze.openSession()` .
- **Résolution :** Veuillez toujours appeler`braze.openSession()`après l'initialisation (et après`braze.changeUser()`si vous définissez un ID externe).

Pour plus d'informations, veuillez vous référer à [l'étape 2 : Veuillez initialiser le SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Les utilisateurs anonymes sur des appareils mobiles ou web peuvent être comptabilisés dans votre [MAU.]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrage du trafic des robots {#bot-filtering}

Le nombre d'utilisateurs actifs par mois peut inclure un pourcentage d'utilisateurs robots, ce qui gonfle votre nombre d'utilisateurs actifs par mois. Bien que le SDK Web Braze intègre une fonctionnalité de détection de certains robots d'indexation courants (tels que les robots des moteurs de recherche et les robots de prévisualisation des réseaux sociaux), il est particulièrement important de rester proactif en mettant en place des solutions robustes pour détecter les robots, car les mises à jour du SDK ne permettent pas à elles seules de détecter systématiquement tous les nouveaux robots.

### Limites de la détection des bots côté SDK

Le SDK Web comprend une fonctionnalité de détection des robots basée sur l'agent utilisateur qui filtre les robots d'indexation connus. Cependant, cette approche présente certaines limites :

- **De nouveaux robots apparaissent constamment** : Les entreprises spécialisées dans l'intelligence artificielle et d'autres acteurs développent régulièrement de nouveaux robots qui peuvent se dissimuler afin d'échapper à la détection.
- **Usurpation d'identité de l'agent utilisateur** : Les robots sophistiqués peuvent imiter les agents utilisateurs légitimes des navigateurs.
- **Bots personnalisés** : Les utilisateurs non techniciens peuvent désormais créer facilement des bots à l'aide de grands modèles linguistiques (LLM), rendant le comportement des bots imprévisible.

### Mise en œuvre du filtrage des bots

{% alert important %}
Les solutions présentées ci-dessous sont des suggestions générales. Adaptez la logique de filtrage des bots à votre environnement unique et à vos modèles de trafic spécifiques.
{% endalert %}

La solution la plus efficace consiste à mettre en œuvre votre propre logique de filtrage des bots avant d'initialiser le SDK Braze. Les approches courantes comprennent :

#### Nécessite une interaction de l'utilisateur

Envisagez de retarder l'initialisation du SDK jusqu'à ce qu'un utilisateur effectue une interaction significative, telle que l'acceptation d'une bannière de consentement aux cookies, le défilement ou un clic. Cette approche est souvent plus facile à mettre en œuvre et peut s'avérer très efficace pour filtrer le trafic des robots.

{% alert important %}
Retarder l'initialisation du SDK jusqu'à l'interaction de l'utilisateur peut entraîner le non-affichage des bannières et des cartes de contenu de type bannière jusqu'à ce que cette interaction ait lieu.
{% endalert %}

#### Détection personnalisée des bots

Mettez en place une détection personnalisée en fonction des modèles de trafic spécifiques de vos bots, tels que :

- Analyse des chaînes de caractères des agents utilisateurs pour identifier les modèles que vous avez détectés dans votre trafic
- Vérification des indicateurs de navigateur sans interface graphique
- Utilisation de services tiers de détection des bots
- Surveillance des signaux comportementaux spécifiques à votre site

**Exemple d'initialisation conditionnelle :**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### Bonnes pratiques

- Veuillez analyser régulièrement vos données MAU et les tendances de trafic Web afin d'identifier tout nouveau comportement de bot.
- Veuillez effectuer des tests approfondis pour vous assurer que votre filtrage des bots n'empêche pas le suivi des utilisateurs légitimes.
- Veuillez mettre à jour votre logique de filtrage en fonction des modèles de trafic des robots que vous observez dans votre environnement.

## Configurations optionnelles

### Journalisation

Pour activer rapidement la journalisation, vous pouvez ajouter `?brazeLogging=true` comme paramètre à l'URL de votre site web. Vous pouvez également activer la journalisation de [base](#web_basic-logging) ou [personnalisée](#web_custom-logging). Pour obtenir un aperçu centralisé sur toutes les plateformes, veuillez consulter [la section Journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Journalisation de base

{% tabs local %}
{% tab before initialization %}
Veuillez utiliser cette fonction`enableLogging` pour enregistrer les messages de débogage de base dans la console JavaScript avant l'initialisation du SDK.

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

{% tab after initialization %}
Veuillez utiliser cette`braze.toggleLogging()`méthode pour enregistrer les messages de débogage de base dans la console JavaScript après l'initialisation du SDK. Votre méthode doit être similaire à la suivante :

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

Veuillez utiliser cette fonction`setLogger` pour enregistrer des messages de débogage personnalisés dans la console JavaScript. Contrairement aux journaux de base, ces journaux ne sont pas visibles par les utilisateurs.

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

Lorsque vous faites référence au SDK Web Braze à partir de notre réseau de diffusion de contenu, par exemple (`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`comme recommandé par nos instructions d'intégration par défaut), vos utilisateurs reçoivent automatiquement des mises à jour mineures (corrections de bogues et fonctionnalités rétrocompatibles, versions`a.a.a`dans`a.a.z`les exemples ci-dessus) lorsqu'ils actualisent votre site.

Cependant, lorsque nous publions des modifications importantes, nous vous demandons de mettre à jour manuellement le SDK Web Braze afin de garantir que les modifications majeures n'affectent pas votre intégration. De plus, si vous téléchargez notre SDK et l'hébergez vous-même, vous ne recevrez aucune mise à jour automatique et devrez effectuer la mise à niveau manuellement pour bénéficier des dernières fonctionnalités et corrections de bogues.

Vous pouvez vous tenir au courant de notre dernière version [en suivant notre flux de publication](https://github.com/braze-inc/braze-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix, et consulter [notre journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) pour un compte-rendu complet de l'historique des versions de notre SDK Web. Pour mettre à niveau le SDK Braze pour le Web :

- Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou dans les dépendances de votre responsable de packages.
- Si vous avez intégré des notifications push pour le Web, mettez à jour le fichier du service de traitement sur votre site. Par défaut, ce paramètre est situé à `/service-worker.js` dans le répertoire racine de votre site, mais l’emplacement peut être personnalisé dans certaines intégrations. Vous devez accéder au répertoire racine pour héberger un fichier de service de traitement.

Il est nécessaire de mettre à jour ces deux fichiers de manière coordonnée afin d'assurer un fonctionnement optimal.

## Autres méthodes d'intégration

### Pages mobiles accélérées (AMP)
{% details See more %}
#### Étape 1 : Inclure le script de notification push pour le Web en AMP

Ajoutez la balise de script asynchrone suivante à votre en-tête :

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Étape 2 : Ajouter des widgets d'abonnement

Veuillez ajouter un widget au corps de votre code HTML qui permet aux utilisateurs de s'abonner et de se désabonner des notifications push.

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

#### Étape 3 : Veuillez ajouter`helper-iframe`et `permission-dialog`

Le composant AMP Web Push génère une fenêtre contextuelle pour gérer les abonnements push. Il est donc nécessaire d'ajouter les fichiers d'aide suivants à votre projet pour activer cette fonctionnalité :

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Étape 4 : Créer un fichier de service de traitement

Veuillez créer un`service-worker.js`fichier dans le répertoire racine de votre site web et y ajouter l'extrait de code suivant :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Étape 5 : Configurer l’élément HTML des notifications push pour le Web en AMP

Veuillez ajouter l'élément HTML `amp-web-push`suivant à votre corps HTML. Veuillez noter que vous devez ajouter vos paramètres [`apiKey`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)de [`baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)requête [et](https://documenter.getpostman.com/view/4689407/SVYrsdsG) à `service-worker-URL`.

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

### Définition de module asynchrone (AMD)

#### Veuillez désactiver le support.

Si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK Web Braze via l'une des autres options de cette liste, vous pouvez charger une version de la bibliothèque qui n'inclut pas la prise en charge AMD. Il est possible de charger cette version de la bibliothèque depuis l’endroit suivant du CDN :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Chargeur de modules

Si vous utilisez RequireJS ou d’autres chargeurs de module AMD, nous vous recommandons d’auto-héberger une copie de notre bibliothèque et de la référencer comme vous le feriez avec d’autres ressources :

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Électron {#electron}

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

### Cadres SSR {#ssr}

Si vous utilisez un framework de rendu côté serveur (SSR) tel que Next.js, vous pourriez rencontrer des erreurs car le SDK est conçu pour fonctionner dans un environnement de navigateur. Vous pouvez résoudre ces problèmes en important le SDK de façon dynamique.

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

Pour plus de détails ou pour obtenir une assistance approfondie concernant la configuration de Tealium, veuillez consulter notre [documentation sur l'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contacter votre gestionnaire de compte Tealium.

### Vite {#vite}

Si vous utilisez Vite et voyez un avertissement autour des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous pourriez devoir exclure le SDK de Braze de sa [découverte de dépendance](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) :

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Autres gestionnaires de balises

Braze peut également être compatible avec d’autres solutions de gestion des balises en suivant nos instructions d’intégration au sein d’une balise HTML personnalisée. Veuillez contacter un conseiller Braze si vous avez besoin d'aide pour évaluer ces solutions.
