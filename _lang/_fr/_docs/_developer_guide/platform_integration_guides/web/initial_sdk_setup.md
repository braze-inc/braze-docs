---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour le Web
platform: Web
page_order: 0
page_type: Référence
description: "Cet article couvre la configuration initiale du SDK pour le Braze Web SDK."
---

# Configuration initiale du SDK

Le SDK Web Braze vous permet de collecter des messages d'analyse et d'afficher des messages riches dans l'application, Push, et de carte de contenu à vos utilisateurs Web.

Pour une référence technique complète, veuillez consulter notre [Documentation JavaScript][9].

## Étape 1 : Installer la bibliothèque Braze

Il y a trois façons faciles d'intégrer le SDK Web pour inclure des composants d'analyse et de messagerie sur votre site. N’oubliez pas de consulter notre [Guide d’intégration Push][16] si vous prévoyez d’utiliser les fonctionnalités Push Web.

Si votre site Web utilise une `Content-Security-Policy`, veuillez suivre notre [Guide d'en-tête CSP][19] en plus des étapes d'intégration ci-dessous.

### Option 1 : NPM ou Yarn {#install-npm}

Si votre site utilise des gestionnaires de paquets NPM ou Yarn, vous pouvez ajouter le paquet [Braze NPM](https://www.npmjs.com/package/@braze/web-sdk) comme dépendance.

Les définitions de types sont maintenant incluses depuis v3.0.0 🎉. Pour des notes sur la mise à jour de 2.x vers 3.x, veuillez consulter notre [Changelog][17].

```bash
npm install --save @braze/web-sdk
# ou, en utilisant yarn:
# yarn add @braze/web-sdk
```

Une fois installé, vous pouvez `importer` ou `demander` la bibliothèque de la manière habituelle :

```javascript
importer appboy de "@braze/web-sdk";
// ou, en utilisant `require`
const appboy = require("@braze/web-sdk");
```

### Option 2 : Gestionnaire de tags Google {#install-gtm}

Le SDK Web Braze peut être rapidement installé à partir de la bibliothèque de modèles Google Tag Manager. Deux tags sont pris en charge :

1. Étiquette d'initialisation - charge le SDK Web sur votre site Web et définit éventuellement l'ID d'utilisateur externe

2. Étiquette d'actions - utilisée pour déclencher des événements personnalisés, des achats, changer l'ID de l'utilisateur ou activer/désactiver le suivi SDK

Pour plus d'informations, veuillez consulter le [Guide d'intégration du Gestionnaire de Google Tag][18].

### Option 3 : Braze CDN {#install-cdn}

Ajoutez le SDK Braze Web directement à votre HTML en référençant notre script hébergé par CDN, qui charge la bibliothèque de manière asynchrone.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2FAppboy%2Fappboy-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Étape 2 : Initialiser Braze

Une fois que le Braze Web SDK est ajouté à votre site web, initialisez la bibliothèque avec la `clé API` et l'URL d'extrémité [SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) trouvée dans **Gérer les paramètres** > **Paramètres** dans votre tableau de bord Braze.

**Note**: Si vous avez configuré vos options d'initialisation Braze dans un Gestionnaire de tags, vous pouvez sauter cette étape.

Pour une liste complète des options pour `appboy.initialize()` , veuillez consulter notre [Documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).


```javascript
// initialise l'appboy SDK
. nitialize('VOTRE-API-KEY-ICI', {
    baseUrl: "VOTRE SDK-ENDPOINT-HERE"
});

// affiche optionnellement tous les messages In-App sans gestion personnalisée
appboy.display. utomatialShowNewInAppMessages();

// éventuellement définit l'ID externe de l'utilisateur courant
if (isLoggedIn){
    appboy. hangeUser(userIdentifier);
}

// démarre (ou continue) une session
appboy.openSession();
```

Pour toutes les autres méthodes JavaScript, veuillez consulter notre [Documentation de référence JavaScript][9] complète.

{% alert note %}
Les utilisateurs anonymes sur des appareils mobiles ou web peuvent être pris en compte dans votre [MAU]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#monthly-active-users). En conséquence, vous pouvez vouloir charger ou initialiser le SDK de manière conditionnelle pour exclure ces utilisateurs de votre compte MAU.
{% endalert %}

## Étape 3 : Push Web (facultatif)

Une configuration supplémentaire est nécessaire pour utiliser les notifications Web push. Veuillez consulter notre section [Notifications Push][16] pour obtenir des instructions.

## Dépannage {#error-logging}

Pour aider à résoudre les problèmes, vous pouvez activer la connexion verbeuse dans le SDK. Ceci est utile pour le développement, mais est visible pour tous les utilisateurs, donc vous devriez supprimer cette option ou fournir un enregistreur alternatif avec `appboy. etLogger()` dans votre environnement de production.

```javascript
appboy.initialize("VOTRE API-KEY-ICI", {
    baseUrl: "",
    enableLogging: true
});

// ou, après l'initialisation:

appboy.toggleAppboyLogging()
```

## Mise à jour du SDK

Lorsque vous faites référence au SDK Braze Web depuis notre réseau de distribution de contenu, par exemple, `https://js.appboycdn.com/web-sdk/a.a/appboy.min. s` (comme recommandé par nos instructions d'intégration par défaut), vos utilisateurs recevront des mises à jour mineures (corrections de bugs et fonctionnalités rétrocompatibles, versions `a. .a` à travers `a.a.z` dans les exemples ci-dessus) automatiquement quand ils rafraîchissent votre site.

Cependant, lorsque nous publions des changements majeurs, nous vous demandons de mettre à jour le Braze Web SDK manuellement pour vous assurer que rien dans votre intégration ne sera affecté par tout changement de rupture. De plus, si vous téléchargez notre SDK et l'hébergez vous-même, vous ne recevrez aucune mise à jour de version automatiquement et vous devriez mettre à jour manuellement pour recevoir les dernières fonctionnalités et corrections de bogues.

Vous pouvez vous tenir à jour avec notre dernière version [suivant notre flux de publication](https://github.com/Appboy/appboy-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix, et voir [notre changelog](https://github.com/Appboy/appboy-web-sdk/blob/master/CHANGELOG.md) pour une comptabilisation complète de notre historique de version du Web SDK. Pour mettre à jour le SDK Braze Web:

* Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/appboy.min.js`, ou dans les dépendances de votre gestionnaire de paquets.
* Si vous avez un push web intégré, mettez à jour le fichier du service sur votre site - par défaut, il se trouve à `/service-worker. s` à la racine de votre site, mais l'emplacement peut être personnalisé dans certaines intégrations. Veuillez noter que vous devez être en mesure d'accéder au répertoire racine pour héberger un fichier de travail de service.

Ces deux dossiers doivent être mis à jour en coordination afin d'assurer une bonne fonctionnalité.

## Méthodes d'intégration alternatives

### Chargeur de module AMD
Si vous utilisez Google Tag Manager à côté d'un chargeur de modules AMD tel que RequireJS pour charger le SDK de Brase, vous devrez utiliser le snippet d'intégration compatible RequireJS dans votre balise `<head>`.

Pour plus d'instructions à ce sujet, veuillez consulter la section appropriée de notre [Dépôt Github de Braze Web SDK][2].

### Tealium iQ

Tealium iQ offre une intégration clé en main de base de Braze. Pour configurer l'intégration, il vous suffit de rechercher Braze dans l'interface de gestion des balises Tealium, et de fournir la clé API Web SDK depuis votre tableau de bord.

Pour plus de détails, ou un support de configuration approfondi de Tealium, consultez notre [documentation d'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

### Autres gestionnaires de tags

Braze peut également être compatible avec d'autres solutions de gestion des balises en suivant nos instructions d'intégration dans une balise HTML personnalisée. Veuillez contacter un représentant de Braze si vous avez besoin d'aide pour évaluer ces solutions.
<!-- wesley wanted an empty line at the end -->
[2]: https://github.com/Appboy/appboy-web-sdk#getting-started "Braze Web SDK Github Repository"
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html "JSDocs"
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html "JSDocs"
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[17]: https://github.com/Appboy/appboy-web-sdk/blob/master/CHANGELOG.md#300
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/
