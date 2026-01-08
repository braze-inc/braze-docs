---
nav_title: Messages in-app au format HTML
article_title: Messages in-app personnalisés en HTML
page_order: 0
page_type: reference
description: "Cet article donne un aperçu des messages in-app code personnalisés, y compris les méthodes JavaScript, le suivi des boutons et l'utilisation de l'aperçu HTML interactif dans Braze."
channel:
  - in-app messages
---

# Messages in-app en HTML personnalisés {#custom-html-messages}

> Bien que nos messages in-app standard puissent être personnalisés de diverses manières, vous pouvez avoir un contrôle encore plus grand sur l'aspect et la convivialité de vos campagnes en utilisant des messages conçus et créés à l'aide de HTML, CSS et JavaScript. Avec une simple composition, vous pouvez débloquer des fonctionnalités et une image de marque personnalisées pour répondre à tous vos besoins. 

Les messages in-app en HTML permettent de mieux contrôler l'aspect et la convivialité d'un message, notamment grâce aux éléments suivants :

- Polices et styles personnalisés
- Vidéos
- Images multiples
- Comportements au clic
- Composants interactifs
- Animations personnalisées

Les messages HTML personnalisés peuvent utiliser les méthodes du [pont JavaScript](#javascript-bridge) pour enregistrer des événements, définir des attributs personnalisés, fermer le message, et bien plus encore ! Consultez notre [dépôt GitHub](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser les messages in-app HTML pour vos besoins, et pour un ensemble de modèles de messages in-app HTML5 pour vous aider à démarrer.

{% alert note %}
Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze : par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci pour des raisons de sécurité puisque les messages in-app en HTML peuvent exécuter du JavaScript, nous demandons donc à un responsable de site de les activer.
{% endalert %}

## Pont JavaScript {#javascript-bridge}

Les messages in-app HTML pour le Web, Android, iOS et les SDK Swift prennent en charge un "pont" JavaScript pour s'interfacer avec le SDK Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments comportant des liens ou s'engagent d'une autre manière avec votre contenu. Ces méthodes existent avec la variable globale `brazeBridge` ou `appboyBridge`.

{% alert important %}
Braze vous recommande d'utiliser la variable globale `brazeBridge`. La variable globale `appboyBridge` est obsolète mais continuera à fonctionner pour les utilisateurs existants. Si vous utilisez `appboyBridge`, nous vous suggérons de migrer vers `brazeBridge`. <br><br> `appboyBridge` est obsolète dans les versions suivantes du SDK :
- Web : [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android : [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS : [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Par exemple, pour enregistrer un attribut personnalisé et un événement personnalisé, puis fermer le message, vous pouvez utiliser le JavaScript suivant dans votre message HTML in-app :

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

### Méthodes JavaScript Bridge {#bridge}

Les méthodes JavaScript suivantes sont prises en charge dans les messages in-app de Braze HTML :

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
Vous ne pouvez pas faire référence à Liquid pour insérer des <code>customAttributes</code> dans les méthodes JavaScript Bridge.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## Actions basées sur les liens

Outre le JavaScript personnalisé, les SDK de Braze peuvent également envoyer des données d'analyse/analytique à l'aide de ces raccourcis URL pratiques. Notez que ces paramètres de requête et ces schémas d'URL sont tous sensibles à la casse.

### Suivi des clics sur les boutons (obsolète)

{% alert warning %}
L'utilisation de `abButtonID` n'est pas prise en charge dans les types de messages [HTML avec aperçu.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/)  Pour plus d'informations, consultez notre [guide de mise à niveau]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Pour enregistrer les clics sur les boutons pour l'analyse des messages in-app, vous pouvez ajouter `abButtonId` comme paramètre de requête à tout lien profond, URL de redirection ou élément d'ancrage `<a>`. Utilisez `?abButtonId=0` pour enregistrer un clic sur le "bouton 1" et `?abButtonId=1` pour enregistrer un clic sur le "bouton 2".

Comme pour les autres paramètres d'URL, le premier paramètre doit commencer par un point d'interrogation `?`, tandis que les paramètres suivants doivent être séparés par une esperluette `&`.

#### Exemples d'URL

- `https://example.com/?abButtonId=0` - Clic sur le bouton 1
- `https://example.com/?abButtonId=1` - Clic sur le bouton 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Bouton 1 click avec d'autres paramètres URL existants
- `myApp://deep-link?page=home&abButtonId=1` - Mobile deeplink avec bouton 2 click
- `<a href="https://example.com/?abButtonId=1">` - Élément d'ancrage `<a>` avec le clic du bouton 2

{% alert note %}
Les messages in-app ne prennent en charge que les clics du bouton 1 et du bouton 2. Les URL qui ne spécifient pas l'un de ces deux ID de bouton seront enregistrés comme des "clics de corps" génériques.
{% endalert %}

### Ouvrir le lien dans une nouvelle fenêtre (mobile uniquement)

Pour ouvrir les liens en dehors de votre application dans une nouvelle fenêtre, définissez `?abExternalOpen=true`. Le message sera rejeté avant l'ouverture du lien.

Pour la création de liens profonds, Braze ouvrira votre URL quelle que soit la valeur de `abExternalOpen`.

### Ouvrir en tant que lien profond (mobile uniquement)

Pour que Braze traite votre lien HTTP ou HTTPS comme un lien profond, définissez `?abDeepLink=true`.

Lorsque ce paramètre de chaîne de caractères est absent ou défini sur `false`, Braze tente d'ouvrir le lien web dans un navigateur web interne à l'application hôte.

### Fermer le message in-app

Pour fermer un message in-app, vous pouvez utiliser la méthode javascript `brazeBridge.closeMessage()`.

Par exemple, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` fermera le message in-app.

## Téléchargement HTML avec aperçu

Lorsque vous rédigez des messages personnalisés en HTML in-app, vous pouvez prévisualiser votre contenu interactif directement dans Braze. 

Le panneau de prévisualisation des messages de l'éditeur affiche un aperçu réaliste qui rend le JavaScript inclus dans votre message. Vous pouvez prévisualiser vos messages personnalisés et interagir avec eux à partir du panneau de prévisualisation en cliquant sur la pagination, en soumettant des formulaires ou des enquêtes, en regardant des animations JavaScript, et bien plus encore !

Interagir avec l'aperçu HTML en faisant défiler les pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Toutes les méthodes JavaScript `brazeBridge` que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateurs lors de la prévisualisation dans le tableau de bord.
{% endalert %}

### Exigences du SDK {#supported-sdk-versions}

Pour utiliser l'aperçu HTML pour les messages in-app, vous devez passer aux versions minimales suivantes du SDK de Braze :

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Ce type de message ne pouvant être reçu que par certaines versions ultérieures du SDK, les utilisateurs de versions non prises en charge du SDK ne recevront pas le message. Envisagez d'adopter ce type de message une fois qu'une partie importante de votre base d'utilisateurs est joignable, ou ne ciblez que les utilisateurs dont la version de l'application est postérieure aux exigences. En savoir plus sur le [filtrage en fonction de la version la plus récente de l'application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Créer une campagne {#instructions}

Les utilisateurs de votre application mobile doivent passer aux versions SDK prises en charge pour recevoir un message in-app avec **code personnalisé**. Nous vous recommandons de [pousser les utilisateurs à mettre à jour]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) leurs applications mobiles avant de lancer des campagnes qui dépendent de versions plus récentes du SDK de Braze.

#### Dossiers de ressources

Lors de la création de messages in-app avec code personnalisé avec téléchargement HTML, vous pouvez télécharger des ressources de campagne dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) pour les référencer dans votre message.

Les types de fichiers suivants sont pris en charge pour le téléchargement :

| Type de fichier        | Extension de fichier                    |
| :--------------- | :-------------------------------- |
| Fichiers de polices       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Images SVG       | `.svg`                            |
| Fichiers JavaScript | `.js`                             |
| Fichiers CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze recommande de télécharger des ressources dans la bibliothèque multimédia pour deux raisons :

1. Les ressources ajoutées à une campagne via la bibliothèque multimédia permettent d'afficher vos messages même lorsque l'utilisateur n'est pas en ligne ou dispose d'une mauvaise connexion internet.
2. Les ressources téléchargées sur Braze peuvent être réutilisées dans toutes les campagnes.

##### Ajouter des ressources

Vous pouvez ajouter des ressources nouvelles ou existantes à votre campagne.

Pour ajouter de nouvelles ressources à votre campagne, utilisez la section glisser-déposer pour télécharger un fichier. Les ressources ajoutées dans cette section seront également ajoutées automatiquement à la bibliothèque multimédia. Pour ajouter des ressources que vous avez déjà téléchargées dans la bibliothèque multimédia, sélectionnez **Ajouter à partir de la bibliothèque multimédia**.

Une fois vos ressources ajoutées, elles apparaîtront dans la section **Ressources pour cette campagne.**  

Si le nom de fichier d'une ressource correspond à celui d'une ressource HTML locale, il sera automatiquement remplacé (par exemple, `cat.png` est téléchargé et `<img src="cat.png" />` existe). 

Sinon, survolez une ressource dans la liste et sélectionnez <i class="fas fa-copy"></i> **Copy** pour copier l'URL du fichier dans votre presse-papiers. Collez ensuite l'URL de la ressource copiée dans votre code HTML comme vous le feriez normalement pour faire référence à une ressource distante.


### Editeur HTML

Les modifications que vous apportez au code HTML s'affichent automatiquement dans le panneau de prévisualisation au fur et à mesure que vous tapez. Toutes les méthodes [JavaScript`brazeBridge` ](#bridge) que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateurs lors de la prévisualisation dans le tableau de bord.

{% alert tip %}
Vous pouvez sélectionner <i class="fa-solid fa-magnifying-glass"></i> **Search** dans l'éditeur HTML pour effectuer une recherche dans votre code !
{% endalert %}

### Suivi des boutons {#button-tracking-improvements}

Vous pouvez suivre les performances dans votre code personnalisé dans un message in-app à l'aide de la méthode [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) méthode JavaScript. Cela vous permet de suivre par programme le "bouton 1", le "bouton 2" et les "clics du corps" en utilisant respectivement `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` ou `brazeBridge.logClick()`.

| Clics     | Méthode                       |
| ---------- | ---------------------------- |
| Bouton 1   | `brazeBridge.logClick('0')` |
| Bouton 2   | `brazeBridge.logClick('1')` |
| Cliquez sur le corps | `brazeBridge.logClick()`    |
| Suivi des boutons personnalisés |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Cette méthode de suivi des boutons remplace les anciennes méthodes de suivi automatique des clics (telles que `?abButtonId=0`), qui ont été supprimées.
{% endalert %}

Vous pouvez suivre plusieurs clics sur les boutons par impression. Par exemple, pour fermer un message et enregistrer un clic sur le bouton 2, vous pouvez utiliser ce qui suit :

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

Vous pouvez également suivre les nouveaux noms de boutons personnalisés - jusqu'à 100 noms uniques par campagne. Par exemple, `brazeBridge.logClick('blue button')` ou `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Lorsque vous utilisez des méthodes JavaScript à l'intérieur d'un attribut `onclick`, entourez les valeurs chaînes de caractères de guillemets simples afin d'éviter tout conflit avec l'attribut HTML à guillemets doubles.
{% endalert %}

#### Limites

- Vous pouvez avoir jusqu'à 100 ID de bouton uniques par campagne.
- Les ID des boutons peuvent comporter jusqu'à 255 caractères chacun.
- Les ID des boutons ne peuvent comporter que des lettres, des chiffres, des espaces, des tirets et des traits de soulignement.

### Changements incompatibles avec le passé {#backward-incompatible-changes}

1. Le changement incompatible le plus notable avec ce nouveau type de message concerne les exigences du SDK. Les utilisateurs dont le SDK de l'app ne répond pas aux [exigences](#supported-sdk-versions) minimales [en matière de version du SDK](#supported-sdk-versions) ne verront pas le message s'afficher.
<br>

2. Le lien profond `braze://close`, qui était auparavant pris en charge par les applications mobiles, a été supprimé au profit du lien JavaScript `brazeBridge.closeMessage()`. Cela permet d'envoyer des messages HTML sur plusieurs plates-formes, puisque le web ne prend pas en charge les liens profonds.

3. Le suivi automatique des clics, qui utilisait `?abButtonId=0` pour les ID des boutons, et le suivi des "clics du corps" sur les boutons de fermeture ont été supprimés. Les exemples de code suivants montrent comment modifier votre code HTML pour utiliser nos nouvelles méthodes JavaScript de suivi des clics :

   | Avant | Après |
   |:-------- |:------------|
   |<code><a href="braze://close">Bouton de fermeture</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">Bouton de fermeture</a></code>|
   |<code><a href="braze://close?abButtonId=0">Bouton de fermeture</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">Bouton de fermeture</a></code>|
   |<code><a href="app://deeplink?abButtonId=0">Bouton de piste 1</a></code>|<code><a href="app://deeplink" onclick="brazeBridge.logClick('0')">Bouton de piste 1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1") ;<br>  brazeBridge.closeMessage() ;<br>}) ;<br></script></code>|

