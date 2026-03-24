### Conditions préalables

Avant de pouvoir utiliser cette méthode d'intégration, il est nécessaire de [créer un compte et un conteneur pour Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Étape 1 : Veuillez ouvrir la galerie de modèles de tags.

Dans [Google Tag Manager](https://tagmanager.google.com/), veuillez sélectionner votre espace de travail, puis choisissez **Modèles**. Dans le volet **Modèle d’étiquette**, veuillez sélectionner **Rechercher dans la galerie**.

![La page des modèles pour un exemple d'espace de travail dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Étape 2 : Veuillez ajouter le modèle de balise d'initialisation.

Dans la galerie de modèles, veuillez rechercher`braze-inc`, puis sélectionner **l’étiquette Braze Initialization**.

![La galerie de modèles présentant les différents modèles « Braze-inc ».]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Veuillez sélectionner **Ajouter à l'espace de travail** > **Ajouter**.

![La page « Étiquette d'initialisation Braze » dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Étape 3 : Veuillez configurer l'étiquette.

Dans la section **Modèles**, veuillez sélectionner le modèle que vous venez d'ajouter.

![La page « Modèles » dans Google Tag Manager affichant le modèle d'étiquette d'initialisation Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Veuillez sélectionner l'icône en forme de crayon pour ouvrir le menu déroulant **« Configuration des étiquettes** ».

![La vignette Configuration des étiquettes avec l'icône « crayon » affichée.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Veuillez saisir les informations minimales requises :

| Champ         | Description |
| ------------- | ----------- |
| **Clé API**   | Votre [clé API Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), disponible dans le tableau de bord de Braze sous **Paramètres** > **Paramètres de l'application**. |
| **Endpoint de l’API** | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| **Version du SDK**  | La dernière`MAJOR.MINOR`version du SDK Web Braze mentionnée dans le [journal des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Pour plus d'informations, veuillez consulter [la section À propos de la gestion des versions du SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour accéder à des paramètres d'initialisation supplémentaires, veuillez sélectionner **Options d'initialisation Braze** et choisir les options qui vous sont nécessaires.

![La liste des options d'initialisation Braze se trouve sous « Configuration des étiquettes ».]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Étape 4 : Choisir les options d’initialisation

L'étiquette d'initialisation Braze propose les options suivantes. La plupart d'entre elles correspondent directement au [SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) [Web`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), et certaines correspondent aux méthodes du SDK Web que l'étiquette appellera lors de l'initialisation. Veuillez sélectionner les options qui correspondent à vos besoins d'intégration :

| Option GTM | Configuration ou méthode du SDK Web | Description |
| --- | --- | --- |
| **Autoriser les messages in-app HTML** | `allowUserSuppliedJavascript` | Active les messages in-app HTML, les bannières et les actions de clic JavaScript fournies par l'utilisateur. Nécessaire pour [les messages in-app HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) et [les bannières]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) qui utilisent du code HTML personnalisé. Veuillez activer cette option uniquement si vous avez confiance dans le contenu HTML et JavaScript, car elle autorise l'exécution de JavaScript fourni par l'utilisateur. |
| **Numéro de version de l’application** | `appVersion`, `appVersionNumber` | Version de l'application pour la segmentation (par exemple, `1.2.3.4`). |
| **Ouvrir automatiquement une nouvelle session** | `braze.openSession()` | Ouvre une nouvelle session après l'initialisation du SDK en appelant cette méthode pour vous. |
| **Afficher automatiquement les nouveaux messages in-app** | `braze.automaticallyShowInAppMessages()` | Affiche automatiquement les nouveaux messages in-app lorsqu'ils arrivent du serveur en appelant cette méthode après l'initialisation. |
| **Désactiver la maintenance automatique des jetons Push** | `disablePushTokenMaintenance` | Empêche le SDK de synchroniser les jetons push avec le backend Braze lors de nouvelles sessions. |
| **Désactiver l'enregistrement automatique des services de traitement** | `manageServiceWorkerExternally` | Veuillez utiliser cette option si vous enregistrez et gérez vous-même le service de traitement. |
| **Désactiver les cookies** | `noCookies` | Utilise localStorage à la place des cookies pour les données utilisateur/session. Empêche la reconnaissance entre sous-domaines. |
| **Désactiver Font Awesome** | `doNotLoadFontAwesome` | Empêche le SDK de charger Font Awesome à partir du réseau de diffusion de contenu. Veuillez utiliser cette option si votre site dispose de sa propre police Font Awesome. |
| **Activer l'authentification SDK** | `enableSdkAuthentication` | Active [l'authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/). |
| **Activer la journalisation du SDK Web** | `enableLogging` | Active la journalisation de la console à des fins de débogage. Veuillez retirer avant la production du produit. |
| **Intervalle minimal entre les messages déclenchés** | `minimumIntervalBetweenTriggerActionsInSeconds` | Nombre minimum de secondes entre les actions de déclenchement (valeur par défaut : 30). |
| **Ouvrir les cartes dans un nouvel onglet** | `openCardsInNewTab` | Ouvre les liens des cartes de contenu dans un nouvel onglet lorsque l'interface utilisateur par défaut du flux est utilisée. |
| **Localisation des travailleurs du service de traitement** | `serviceWorkerLocation` | Chemin d'accès personnalisé pour le fichier du service de traitement (par défaut : `/service-worker.js`). |
| **Délai d'expiration de la session (en secondes)** | `sessionTimeoutInSeconds` | Délai d'expiration de la session en secondes (valeur par défaut : 1800). |

{% alert note %}
Pour activer [les messages in-app personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) lorsque vous utilisez la balise d'initialisation Braze de Google Tag Manager, veuillez sélectionner **« Autoriser les messages in-app personnalisés** » dans **les options d'initialisation Braze**. Ce mappage correspond à l'option`allowUserSuppliedJavascript`d'initialisation dans`braze.initialize()`et la définit sur `true`. La balise d'initialisation Braze de Google Tag Manager utilise cette étiquette à la place du nom de l'option.
{% endalert %}

Pour les options non exposées dans le modèle GTM (telles que `contentSecurityNonce`, `localization`, ou `devicePropertyAllowlist`), veuillez utiliser [l'initialisation à l'exécution]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) à la place.

### Étape 5 : Définir pour être un déclencheur sur *toutes les pages*

La étiquette d'initialisation doit être exécutée sur toutes les pages de votre site. Cela vous permet d'utiliser les méthodes SDK Braze et d'enregistrer les analyses des notifications push Web.

### Étape 6 : Veuillez vérifier votre intégration.

Vous pouvez vérifier votre intégration en utilisant l'une des options suivantes :

- **Option 1 :** À l'aide de [l'outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, vous pouvez vérifier si la balise d'initialisation Braze se déclenche correctement sur les pages ou les événements que vous avez configurés.
- **Option 2 :** Veuillez vérifier si des requêtes réseau ont été envoyées à Braze depuis votre page Web. De plus, la bibliothèque `window.braze`globale devrait maintenant être définie.
