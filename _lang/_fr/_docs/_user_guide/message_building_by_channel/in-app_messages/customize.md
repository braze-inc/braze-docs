---
nav_title: Personnaliser
article_title: Personnalisation
page_order: 2
description: "En plus des modèles de messages In-App, Braze propose également des modèles de messagerie personnalisés qui permettent de personnaliser HTML, Modales avec CSS personnalisé, Vidéo et plus encore."
channel:
  - messages intégrés à l'application
---

# Personnalisation

En plus des [modèles de messages intégrés à l'application][1], vous pouvez également créer des modèles de messages personnalisés avec les fonctionnalités suivantes :

- [Modèles HTML personnalisés](#custom-html-messages) - créez un modèle personnalisé avec HTML, JavaScript et CSS.
- [Modal avec CSS personnalisé (web seulement)](#web-modal-css) - ajouter des CSS personnalisés aux modèles standards pour des options de style plus flexibles.
- [Formulaire de capture d'email (web seulement)](#email-capture-form) - collectez les adresses e-mail en brési.
- [Profils de couleurs réutilisables et CSS](#reusable-color-profiles) - enregistrer et réutiliser les profils de couleurs pour les modèles de messages intégrés à l'application.
- [Vidéo](#video) - ajoute une vidéo à un message personnalisé dans l'application.

{% alert tip %}
Une personnalisation supplémentaire de l'apparence de vos messages intégrés peut être effectuée par vos développeurs. Consultez notre documentation d'intégration [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-message-customization), ou [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/) sur les messages In-App pour plus de détails.
{% endalert %}

## Messages HTML dans l'application {#custom-html-messages}

Pendant que les messages intégrés de Braze peuvent être personnalisés de différentes manières, vous pouvez prendre encore plus de contrôle sur l'apparence de vos campagnes en utilisant des messages conçus et construits en utilisant HTML, CSS et JavaScript. Avec une composition simple, vous pouvez déverrouiller des fonctionnalités personnalisées et une image de marque pour répondre à vos besoins.

Les messages HTML intégrés à l'application permettent un plus grand contrôle sur l'apparence et l'apparence d'un message, y compris les suivants :

- Polices et styles personnalisés
- Vidéos
- Images multiples
- Comportements du clic
- Composants interactifs
- Animations personnalisées

Les messages HTML personnalisés peuvent utiliser les méthodes [JavaScript Bridge](#javascript-bridge) pour enregistrer les événements, définir des attributs personnalisés, fermer le message, et plus encore ! Consultez notre [dépôt GitHub][2] qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser les messages HTML dans l'application en fonction de vos besoins. et pour un ensemble de modèles de messages HTML5 dans l'application pour vous aider à démarrer.

{% alert note %}
Pour activer les messages HTML dans l'application dans le SDK Web, votre intégration SDK doit fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze: par exemple `appboy. nitialize('VOTRE API_COUR', {allowUserSuppliedJavascript: true})`. Ceci est pour des raisons de sécurité puisque les messages HTML dans l'application peuvent exécuter JavaScript, donc nous avons besoin d'un responsable du site pour les activer.
{% endalert %}

### Pont de connexion JavaScript {#javascript-bridge}

Les messages HTML dans l'application pour Web, Android et iOS prennent en charge une interface JavaScript "passerelle" vers le SDK Web de Braze, vous permettant de déclencher des actions personnalisées de Braze lorsque les utilisateurs cliquent sur des éléments avec des liens ou s'engagent autrement avec votre contenu. Ces méthodes existent avec la variable globale `appboyBridge`.

Par exemple, pour enregistrer un attribut personnalisé et un événement personnalisé, puis fermer le message, vous pouvez utiliser le JavaScript suivant dans votre message HTML dans l'application:

```html
<button id="button">Définir la couleur préférée</button>
<script>
// attendre l'événement prêt `appboyBridge`, fenêtre "ab.BridgeReady"
. ddEventListener("ab.BridgeReady", function(){
  // gestionnaire d'événements lorsque le bouton est cliqué
  document. uerySelector("#button"). nclick = function(){
    // track Button 1 clicks for analytics
    // Note: cela nécessite Android SDK v8. .0, Web SDK v2.5.0, et iOS SDK v3.23.0
    appboyBridge. ogClick("0");
    // définit l'attribut personnalisé de l'utilisateur
    appboyBridge.getUser(). etCustomUserAttribute("couleur préférée", "bleu");
    // suit un événement personnalisé
    appboyBridge. ogCustomEvent("enquête complétée");
    // envoie les données mises en file d'attente à Braze
    appboyBridge. equestImmediateDataFlush();
    // ferme ce message dans l'application
    appboyBridge. loseMessage();
  };
}, false);
</script>
```

#### Méthodes appboyBridge

Les méthodes JavaScript suivantes sont prises en charge dans les messages HTML de Braze dans l'application:

<style>
/* makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% include archive/appboyBridge.md %}

### Actions basées sur les liens

En plus de JavaScript personnalisé, Braze SDKs peut également envoyer des données d'analyse avec ces raccourcis URL pratiques. Notez que ces paramètres de requête et les schémas d'URL sont tous sensibles à la casse.

#### Suivi des clics des boutons

{% alert warning %}
L'utilisation de `abButtonID` n'est pas prise en charge en [HTML avec les types de message Aperçu]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/). Pour plus d'informations, consultez notre [guide de mise à jour]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Pour enregistrer les clics de bouton pour les analyses de messages dans l'application, vous pouvez ajouter `abButtonId` comme paramètre de requête à n'importe quel lien profond, rediriger l'URL, ou la balise `<a>`.

Utilisez `?abButtonId=0` pour enregistrer un clic "Bouton 1", et `?abButtonId=1` pour enregistrer un clic "Bouton 2".

Comme pour les autres paramètres d'URL, le premier paramètre devrait commencer par un point d'interrogation `?`, alors que les paramètres suivants doivent être séparés par un esperluette `&`.

**Exemples**:

- `https://example.com/?abButtonId=0` - Bouton 1 clic
- `https://example.com/?abButtonId=1` - Bouton 2 clic
- `https://example.com/?utm_source=braze&abButtonId=0` - Bouton 1 clic avec d'autres paramètres d'URL existants
- `monApp://deep-link?page=home&abButtonId=1` - approfondissement mobile avec le bouton 2 clic
- `<a href="https://example.com/?abButtonId=1">` - `<a>` tag with Button 2 click

{% alert note %}
Les messages intégrés ne prennent en charge que les boutons 1 et 2 clics. Les URLs qui ne spécifient pas un de ces deux identifiants de bouton seront enregistrées comme génériques « clics sur le corps ».
{% endalert %}

#### Ouvrir le lien dans une nouvelle fenêtre

Pour ouvrir les liens dans une nouvelle fenêtre, définissez `?abExternalOpen=true`. Le message sera rejeté avant d'ouvrir le lien.

Pour un lien profond, Braze ouvrira votre URL quelle que soit la valeur de `abExternalOpen`.

#### Ouvrir en profondeur (mobile seulement)

Pour que Braze gère votre lien HTTP(S) en tant que lien profond, définissez `?abDeepLink=true`.

Lorsque ce paramètre de chaîne de requête est absent ou mis à `false`, Braze essaiera d'ouvrir le lien web dans un navigateur web interne dans l'application hôte.

#### Événements personnalisés (mobile uniquement)

Pour les applications mobiles, vous pouvez enregistrer un événement personnalisé en définissant l'URL d'un lien à `appboy://customEvent` avec un paramètre d'URL `nom`.

Par exemple, `appboy://customEvent?name=eventName` va enregistrer un événement personnalisé de `eventName`.

Assurez-vous d'encoder des espaces d'URL et d'autres caractères spéciaux comme vous le feriez dans n'importe quelle autre URL. Par exemple, `appboy://customEvent?name=event%20name` envoie `nom d'événement`.

Des paramètres de requête supplémentaires seront passés sous la forme de paires clé-valeur.

`appboy://customEvent? ame=eventName&property1=value1&property2=value2` enregistrerait un événement appelé `eventName` avec les propriétés `property1`=`value1` et `property2`=`value2`.

#### Flux d'actualité (mobile uniquement)

Pour les applications mobiles, vous pouvez ouvrir le fil d'actualité en définissant l'URL d'un lien vers `appboy://feed`.

Par exemple, `<a href="appboy://feed">Voir le flux</a>`.

#### Fermer le message dans l'application (mobile seulement)

Pour fermer un message dans l'application, vous pouvez définir l'URL d'un lien à `appboy://close`.

Par exemple, `<a href="appboy://close">Fermer</a>` fermera le message dans l'application.

## Modal avec CSS (web seulement) {#web-modal-css}

Si vous choisissez d'utiliser un Web modal uniquement avec un message CSS vous pouvez [appliquer votre propre modèle](#css-template) ou écrire votre propre CSS dans l'espace fourni. Cet espace est déjà pré-rempli avec le CSS affiché dans l'aperçu de votre message, mais n'hésitez pas à l'ajuster légèrement pour répondre à vos besoins.

Si vous choisissez d'appliquer votre propre modèle, cliquez sur __Appliquer le modèle__ et choisissez dans la Galerie de modèle de message In-App. Si tu n'as pas d'options, tu peux télécharger un [modèle CSS](#in-app-message-templates) en utilisant le constructeur de modèles CSS.

## Formulaire de capture d'email Web {#email-capture-form}

Les messages de capture de courriel vous permettent d'inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi il sera disponible dans leur profil utilisateur pour être utilisé dans toutes vos campagnes de messagerie.

Lorsqu'un utilisateur final saisit son adresse e-mail dans ce formulaire, l'adresse e-mail sera ajoutée à son profil utilisateur.

- Pour les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) qui n'ont pas encore de compte, l'adresse e-mail vivra sur le profil d'utilisateur anonyme qui est lié au périphérique de l'utilisateur.
- Si une adresse e-mail existe déjà sur le profil de l'utilisateur, alors l'adresse e-mail existante sera remplacée par l'adresse e-mail nouvellement saisie.
- Si un utilisateur saisit une adresse e-mail non valide, l'utilisateur verra le message d'erreur : "Veuillez entrer un e-mail valide."
    - Adresses e-mail invalides :
        - `exemple`
        - `exemple@`
        - `@gmail.com`
        - `exemple@gmail`
    - Adresses email valides :
        - `exemple@gmail.com`
        - `exemple@gnail.com` (avec une faute de frappe)
    - Pour plus d'informations sur la validation de l'e-mail au Brésil, reportez-vous aux [directives techniques et aux notes]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation/).

{% details More on identified versus anonymous users %}

En général, la logique derrière le formulaire de saisie de courriel web est simple. Il définira l'adresse e-mail sur le profil de l'utilisateur à Braze pour l'utilisateur actuellement actif. Cependant, cela signifie que le comportement diffère selon que l'utilisateur est identifié (connecté, `changeUser` appelé) ou non.

Si un utilisateur anonyme entre son email dans le formulaire et le soumet, Braze ajoute l'adresse e-mail à son profil d'alias uniquement. Si `changeUser` est appelé plus tard dans leur voyage web et qu'un nouveau `external_id` est assigné (i. ., lorsqu'un nouvel utilisateur s'inscrit avec le service), toutes les données de profil d'utilisateur anonymes sont fusionnées, y compris l'adresse e-mail.

Si `changeUser` est appelé avec un `external_id existant,`, le profil d'utilisateur anonyme est orphelin et toutes les données de ce profil sont perdues, y compris l'adresse e-mail.

Pour plus d'informations, reportez-vous au [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/).

{% enddetails %}


### Étape 1 : Créer une campagne de message dans l'application

Pour accéder à cette option, vous devez créer une campagne de messagerie intégrée à l'application. À partir de là, assurez-vous que **Envoyer à** est réglé sur **Navigateurs Web**, puis sélectionnez **Formulaire de capture de courriel Web** pour votre **Type de message**.

!\[Select Web Email Capture Form\]\[4\]

{% alert note %}
Pour activer les messages de capture d'email dans l'application, votre intégration de SDK doit fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, . `appboy.initialize('VOTRE API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est pour des raisons de sécurité puisque les messages HTML dans l'application peuvent exécuter JavaScript, donc nous avons besoin d'un responsable du site pour les activer.
{% endalert %}

### Étape 2 : Personnaliser le formulaire {#customizable-features}

Ensuite, personnalisez votre formulaire au besoin. Vous pouvez personnaliser les fonctionnalités suivantes pour votre formulaire de capture d'e-mail:

- En-tête, corps et texte du bouton Soumettre
- Une image optionnelle
- Un lien optionnel "Conditions d'utilisation"
- Couleurs différentes pour l'en-tête et le corps du texte, les boutons et l'arrière-plan
- Paires clé-valeur
- Style pour l'en-tête et le corps du texte, les boutons, la couleur de la bordure du bouton, l'arrière-plan et la superposition

!\[emailimage\]\[5\]

Si vous avez besoin de personnaliser votre **type de message** , choisissez **Code personnalisé**. Vous pouvez utiliser ce [modèle modal de capture d'email](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) depuis le dépôt GitHub de [Braze](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) comme code de démarrage.

### Étape 3 : Définissez le public de votre entrée

Si vous voulez seulement envoyer ce formulaire aux utilisateurs sans adresses e-mail existantes, utilisez le filtre `Email Disponible est faux`.

!\[Filtre par email disponible est false\]\[10\]{: style="max-width:50%"}

Si vous voulez seulement envoyer ce formulaire aux utilisateurs sans ID externe (c'est-à-dire, utilisateurs anonymes), utilisez le filtre `ID d'utilisateur externe est vide`.

!\[Filter by external user ID is blank\]\[11\]{: style="max-width:50%"}

Vous pouvez également combiner les deux filtres en utilisant la logique `ET` , si désiré.

### Étape 4 : Destiner les utilisateurs qui ont rempli le formulaire

Après avoir lancé le formulaire de saisie de courriels web et récupéré les adresses e-mail de vos utilisateurs, vous pouvez cibler ces utilisateurs avec le filtre `Cliqué/Ouvert Campagne`.

Définit le filtre à `A cliqué sur le bouton de message 1` pour la campagne `<CAMPAIGN_NAME>`. Remplacez `<CAMPAIGN_NAME>` par le nom de votre campagne de saisie de courrier électronique.

!\[Filter for has clicked in-app message button 1 for your web email capture form campaign\]\[12\]

## Modèles de messages réutilisables {#reusable-color-profiles}

Vous pouvez enregistrer des modèles de messages dans l'application et dans le navigateur sur le tableau de bord pour construire rapidement de nouvelles campagnes et de nouveaux messages en utilisant votre style. Allez dans __Modèles & Médias__, puis dans l'onglet __Modèles de messages dans l'application__. À partir de cette page, vous pouvez soit modifier des modèles existants, soit cliquer sur __+ Créer__ et choisir __Profil de couleur__ ou __Modèle CSS__ pour créer de nouveaux modèles à utiliser dans vos messages intégrés.

### Profil de couleur

Vous pouvez personnaliser le schéma de couleur de votre modèle de message en entrant le code de couleur HEX ou en cliquant sur la case de couleur et en sélectionnant une couleur avec le sélecteur de couleur.

Cliquez sur __Enregistrer le profil de couleur__ en bas à droite lorsque vous avez terminé.

#### Gestion des profils de couleurs

Vous pouvez aussi [dupliquer des modèles][6] et [archiver][7]! En savoir plus sur la création et la gestion de modèles et de contenus créatifs dans [Modèles & Médias][8].

### CSS template {#in-app-message-templates}

Vous pouvez personnaliser un modèle CSS complet pour votre message [Web Modal In-App](#web-modal-css).

Nommez et étiquetez votre modèle CSS, puis choisissez si oui ou non il sera votre modèle par défaut. Vous pouvez écrire votre propre CSS dans l'espace fourni. Cet espace est déjà pré-rempli avec le CSS affiché dans l'aperçu de votre message, et vous devriez être libre de l'ajuster légèrement pour répondre à vos besoins.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

. b-message-header {
  font-size: 20px;
  font-weight: bold;
}

. b-message-text {
  font-size: 14px;
  font-weight: normal;
}

. b-close-button svg {
  fill: #9b9b9b9b;
}

. b-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
. b-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, . b-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

. b-background {
  background-color: white;
}

. b-icon {
  background-color: #0073d5;
  color: blanc;
}

. b-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Comme vous pouvez le voir, vous pouvez tout modifier de la couleur de fond à la taille et au poids de la police, et bien plus encore.

#### Managing CSS templates

Vous pouvez aussi [dupliquer des modèles][6] et [archiver][7]! En savoir plus sur la création et la gestion de modèles et de contenus créatifs dans [Modèles & Médias][8].

## Vidéo {#video}

Pour lire une vidéo dans un message HTML dans l'application, incluez l'élément `<video>` suivant dans votre HTML, et remplacez les noms de la vidéo par le nom de votre fichier (ou l'URL de l'actif distant).

Pour utiliser une ressource vidéo locale, assurez-vous d'inclure ce fichier lorsque vous téléchargez des ressources dans votre campagne.

Pour prendre en charge les appareils iOS, vous devez inclure l'attribut `playsinline` car la lecture en plein écran n'est pas prise en charge pour le moment.

{% alert note %}
iOS ne prend pas en charge la lecture automatique par défaut. Pour mettre à jour cette option par défaut, vous pouvez modifier le [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)
{% endalert %}

Intégrer la vidéo et d'autres contenus HTML5 dans les messages HTML dans l'application sur Android, l'accélération matérielle est nécessaire pour être activée dans l'activité où le message dans l'application est affiché. Pour plus d'informations, reportez-vous au [guide des développeurs Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#youtube-in-html-in-app-messages).

Vous pouvez trouver d'autres options possibles `<video>` sur [la documentation Web MDN][9]

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Votre appareil ne prend pas en charge la lecture de cette vidéo.
</video>
```

{% alert warning %}
Les vidéos en plein écran ne seront pas affichées correctement sur iOS et ne sont pas prises en charge pour le moment. Vous devez inclure l'attribut `playsinline` pour afficher la vidéo dans le message HTML à la place.
{% endalert %}
[4]: {% image_buster /assets/img/email_capture_config.png %} [5]: {% image_buster /assets/img/email_capture.png %} [10]: {% image_buster /assets/img_archive/web_email_filter_1. ng %} [11]: {% image_buster /assets/img_archive/web_email_filter_2.png %} [12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[2]: https://github.com/braze-inc/in-app-message-templates
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/
[7]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/
[8]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[9]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
