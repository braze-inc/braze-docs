---
nav_title: Messages in-app HTML
article_title: Messages in-app HTML personnalisés
page_order: 0
page_type: reference
description: "Le présent article fournit un overview des messages in-app avec code personnalisé, y compris les méthodes Javascript, le suivi des boutons et l’utilisation de l’aperçu HTML interactif dans Braze."
channel:
  - in-app messages
---

# Messages in-app HTML personnalisés {#custom-html-messages}

> Bien que nos messages in-app standard puissent être personnalisés de diverses manières, vous pouvez avoir un contrôle encore plus grand sur l'aspect et la convivialité de vos campagnes en utilisant des messages conçus et créés à l'aide de HTML, CSS et JavaScript. Via à une composition simple, vous pouvez débloquer des fonctionnalités et des marques personnalisées pour répondre à vos besoins. 

Les messages in-app HTML permettent de contrôler davantage l’apparence et l’impression d’un message, y compris les éléments suivants :

- Polices et styles personnalisés
- Vidéos
- Plusieurs images
- Comportements lors du clic
- Composants interactifs
- Animations personnalisées

Les messages HTML personnalisés peuvent utiliser les méthodes du [pont JavaScript](#javascript-bridge) pour enregistrer des événements, définir des attributs personnalisés, fermer le message, et bien plus encore ! Découvrez notre [référentiel GitHub](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur l’utilisation et la personnalisation de messages in-app HTML selon vos besoins, ainsi qu’un ensemble de modèles de messages in-app HTML5 pour vous aider à démarrer.

{% alert note %}
Pour activer les messages in-app HTML, votre intégration SDK doit fournir l’option d’initialisation à Braze `allowUserSuppliedJavascript`, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.
{% endalert %}

## Pont JavaScript {#javascript-bridge}

Les messages in-app HTML pour les SDK Web, Android, iOS et Swift prennent en charge un pont Javascript pour interagir avec le SDK Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments avec des liens ou montrent un engagement avec votre contenu. Ces méthodes existent avec la variable globale `brazeBridge` ou `appboyBridge`.

{% alert important %}
Braze vous recommande d'utiliser la variable globale `brazeBridge`. La variable globale `appboyBridge` est obsolète mais continuera à fonctionner pour les utilisateurs existants. Si vous utilisez `appboyBridge`, nous vous suggérons de migrer vers `brazeBridge`. <br><br> `appboyBridge` est obsolète dans les versions suivantes du SDK :
- Web : [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android : [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS : [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Par exemple, pour enregistrer un attribut et un événement personnalisés puis fermer le message, vous pouvez utiliser le Javascript suivant dans votre message in-app HTML :

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Méthodes de pont Javascript {#bridge}

Les méthodes Javascript suivantes sont prises en charge dans les messages in-app HTML de Braze :

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Vous ne pouvez pas faire référence à Liquid pour insérer <code>customAttributes</code> en méthodes JavaScript Bridge.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## Actions basées sur des liens

Outre un Javascript personnalisé, les SDK Braze peuvent envoyer des données d’analyse avec ces raccourcis d’URL pratiques. Notez que tous ces paramètres de requête et les schémas d’URL sont sensibles à la casse.

### Suivi des clics sur les boutons (obsolète)

{% alert warning %}
L'utilisation de `abButtonID` n'est pas prise en charge dans les types de messages [HTML avec aperçu.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) Pour plus d'informations, consultez notre [guide de mise à niveau]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Pour enregistrer les clics de bouton dans l’analyse des messages in-app, vous pouvez ajouter `abButtonId` comme paramètre de requête à tout lien profond, URL de redirection ou élément d’ancrage `<a>`. Utilisez `?abButtonId=0` pour enregistrer un clic de « Bouton 1 », et `?abButtonId=1` pour enregistrer un clic de « Bouton 2 ».

Comme avec d’autres paramètres d’URL, le premier paramètre doit commencer par un point d’interrogation `?`, et les paramètres suivants doivent être séparés par une esperluette `&`.

#### Exemples d'URL

- `https://example.com/?abButtonId=0` - clic de bouton 1
- `https://example.com/?abButtonId=1` - clic de bouton 2
- `https://example.com/?utm_source=braze&abButtonId=0` - clic de bouton 1avec d’autres paramètres d’URL existants
- `myApp://deep-link?page=home&abButtonId=1` - lien profond mobile avec clic de bouton 2
- `<a href="https://example.com/?abButtonId=1">` - élément d’ancrage `<a>` avec clic de bouton 2

{% alert note %}
Les messages in-app prennent uniquement en charge les clics de bouton 1 et bouton 2. Les URL qui ne spécifient pas l’un de ces deux ID de bouton sont consignées comme des clics génériques dans le corps.
{% endalert %}

### Ouvrir le lien dans une nouvelle fenêtre (mobile uniquement)

Pour ouvrir des liens en dehors de votre application dans une nouvelle fenêtre, définissez `?abExternalOpen=true`. Le message est rejeté avant d’ouvrir le lien.

Pour un lien profond, Braze ouvre votre URL indépendamment de la valeur de `abExternalOpen`.

### Ouvrir comme lien profond (mobile uniquement)

Pour que Braze traite votre lien HTTP ou HTTPS comme un lien profond, définissez `?abDeepLink=true`.

Lorsque ce paramètre de chaîne de requête est absent ou défini sur `false`, Braze tente d’ouvrir le lien Web dans un navigateur Web interne au sein de l’application hôte.

### Fermer un message in-app

Pour fermer un message in-app, vous pouvez utiliser la méthode Javascript `brazeBridge.closeMessage()`.

Par exemple, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` ferme le message in-app.

## Téléchargement HTML avec aperçu

Lorsque vous concevez des messages in-app HTML personnalisés, vous pouvez prévisualiser votre contenu interactif directement dans Braze. 

Le panneau d’aperçu de message de l’éditeur offre un aperçu réaliste avec le rendu du Javascript inclus dans votre message. Vous pouvez prévisualiser et interagir avec vos messages personnalisés depuis le panneau d’aperçu en cliquant sur les pages, en soumettant des formulaires ou des enquêtes, en regardant des animations Javascript, et bien plus encore !

![Interagir avec l'aperçu HTML en faisant défiler les pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Toutes les méthodes Javascript `brazeBridge` que vous utilisez dans votre HTML ne mettent pas à jour les profils utilisateur lors de la prévisualisation dans le tableau de bord.
{% endalert %}

### Exigences du SDK {#supported-sdk-versions}

Pour utiliser l’aperçu HTML des messages in-app, vous devez mettre à niveau les versions minimum suivantes du SDK Braze :

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Ce type de message ne pouvant être reçu que par certaines versions SDK ultérieures, les utilisateurs avec des versions SDK non prises en charge ne reçoivent pas le message. Pensez à adopter ce type de message quand une partie importante de votre base d’utilisateurs est accessible, ou ciblez uniquement les utilisateurs dont la version d’application est ultérieure aux exigences. En savoir plus sur le [filtrage en fonction de la version la plus récente de l'application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Créer une campagne {#instructions}

Lors de la création d'un message in-app **avec code personnalisé**, choisissez **Chargement de code HTML avec aperçu** comme type personnalisé. Si vous n’avez pas créé de messages in-app avec code personnalisé (terminés ou brouillons), cette option est automatiquement appliquée et vous n’avez pas besoin de faire un choix.

![Création d’un message in-app envoyé à la fois à des applications mobiles et à des navigateurs Web, avec le type de message défini sur Code personnalisé et le type personnalisé défini sur Chargement de code HTML avec aperçu.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

N’oubliez pas que les utilisateurs de votre application mobile doivent mettre à niveau vers les versions SDK prises en charge pour recevoir ce message. Nous vous recommandons de [pousser les utilisateurs à mettre à jour]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) leurs applications mobiles avant de lancer des campagnes qui dépendent de versions plus récentes du SDK de Braze.

#### Fichiers de ressources

Lors de la création de messages in-app avec code personnalisé avec téléchargement HTML, vous pouvez télécharger des ressources de campagne dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) pour les référencer dans votre message.

Les types de fichiers suivants sont pris en charge pour téléchargement :

| Type de fichier        | Extension de fichier                    |
| :--------------- | :-------------------------------- |
| Fichiers de polices       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Images SVG       | `.svg`                            |
| Fichiers JavaScript | `.js`                             |
| Fichiers CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze recommande de télécharger des ressources dans la bibliothèque multimédia pour deux raisons :

1. Les ressources ajoutées à une campagne via la bibliothèque multimédia permettent d'afficher vos messages même lorsque l'utilisateur n'est pas en ligne ou dispose d'une mauvaise connexion internet.
2. Les ressources téléchargées dans Braze peuvent être réutilisées dans les campagnes.

##### Ajout de fichiers de ressources

Vous pouvez ajouter des ressources nouvelles ou existantes à votre campagne.

Pour ajouter de nouvelles ressources à votre campagne, utilisez la section de glisser-déposer pour télécharger un fichier. Les ressources ajoutées dans cette section seront également ajoutées automatiquement à la bibliothèque multimédia. Pour ajouter des ressources que vous avez déjà téléchargées dans la bibliothèque multimédia, sélectionnez **Ajouter à partir de la bibliothèque multimédia**.

Une fois vos ressources ajoutées, elles apparaîtront dans la section **Ressources pour cette campagne.**  

Si le nom de fichier d’une ressource correspond à celui d’un ressource HTML locale, il est remplacé automatiquement (par exemple, `cat.png` est téléchargé et `<img src="cat.png" />` existe). 

Sinon, survolez une ressource dans la liste et sélectionnez <i class="fas fa-copy"></i> **Copy** pour copier l'URL du fichier dans votre presse-papiers. Collez ensuite l’URL de la ressource copiée dans votre HTML comme lors du référencement d’une ressource distante.


### Éditeur HTML

Les modifications effectuées dans le HTML sont automatiquement affichées dans le panneau d’aperçu à la saisie. Toutes les méthodes [JavaScript`brazeBridge` ](#bridge) que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateurs lors de la prévisualisation dans le tableau de bord.

Vous pouvez configurer **les paramètres de l'éditeur** pour basculer l'habillage du texte, modifier la taille de la police ou choisir un thème de couleurs. L’éditeur de code comprend différents thèmes de couleur pour mettre la syntaxe évidence, ce qui vous aide à repérer les erreurs de code potentielles directement dans le composeur de messages et à mieux organiser votre code (à l’aide d’espaces ou d’onglets, selon le côté de l’argument où vous êtes).

![Options de mise en évidence de la syntaxe dans le menu déroulant "Paramètres de l'éditeur" lors de la composition d'un message in-app en HTML.]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

{% alert tip %}
Vous pouvez appuyer sur <kbd>Ctrl</kbd> + <kbd>F</kbd> (Windows) ou <kbd>Commande</kbd> + <kbd>F</kbd> (Mac) dans l’éditeur HTML pour faire des recherches dans votre code.
{% endalert %}

### Suivi des boutons {#button-tracking-improvements}

Vous pouvez suivre les performances dans votre message in-app avec code personnalisé à l’aide de la méthode Javascript [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/). Vous pouvez ainsi effectuer un suivi par programmation des clics de bouton 1, bouton 2 et dans le corps en utilisant `brazeBridge.logClick("0")`, `brazeBridge.logClick("1")` ou `brazeBridge.logClick()`, respectivement.

| Clics     | Méthode                       |
| ---------- | ---------------------------- |
| Bouton 1   | `brazeBridge.logClick("0")` |
| Bouton 2   | `brazeBridge.logClick("1")` |
| Clic dans le corps | `brazeBridge.logClick()`    |
| Suivi personnalisé des boutons |`brazeBridge.logClick("your custom name here")`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Cette méthode de suivi des boutons remplace les anciennes méthodes de suivi automatique des clics (telles que `?abButtonId=0`), qui ont été supprimées.
{% endalert %}

Vous pouvez suivre plusieurs événements de clic de bouton par impression. Par exemple, pour fermer un message et enregistrer un clic de bouton 2, vous pouvez utiliser ce qui suit :

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

Vous pouvez également suivre de nouveaux noms de boutons personnalisés (jusqu’à 100 noms uniques par campagne). Par exemple, `brazeBridge.logClick("blue button")` ou `brazeBridge.logClick("viewed carousel page 3")`.

#### Limitations

- Vous pouvez avoir jusqu’à 100 ID de boutons uniques par campagne.
- Les ID de boutons peuvent contenir jusqu’à 255 caractères chacun.
- Les ID de boutons ne peuvent inclure que des lettres, des chiffres, des espaces, des tirets et des traits de soulignement.

### Changements non-rétrocompatibles {#backward-incompatible-changes}

1. Les exigences de SDK sont le changement incompatible le plus notable avec ce nouveau type de message. Les utilisateurs dont le SDK de l'app ne répond pas aux [exigences minimales en matière de version du SDK](#supported-sdk-versions) ne verront pas le message s'afficher.
<br>

2. Le lien profond `braze://close`, auparavant pris en charge par les applications mobiles, a été supprimé en faveur du Javascript `brazeBridge.closeMessage()`. Vous bénéficiez ainsi de messages HTML multiplateforme, sachant que le Web ne prend pas en charge les liens profonds.

3. Le suivi automatique des clics, qui utilisait `?abButtonId=0` pour les ID de boutons et le suivi de clics dans le corps pour les boutons de fermeture, a été supprimé. Les exemples de code suivants montrent comment modifier votre HTML pour utiliser nos nouvelles méthodes Javascript de suivi des clics :

   | Avant | Après |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_874077ba-9f68-4ab3-8ce5-83569e7e4efd/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_f3d9371c-7562-42cc-8df3-765d76bc1455/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_fd36e679-ff7e-473d-a16f-be382cff174e/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_823673d3-6120-4af9-aa1a-7010c1effc12/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_e430d232-7145-430f-804c-a3f6f25538a7/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

