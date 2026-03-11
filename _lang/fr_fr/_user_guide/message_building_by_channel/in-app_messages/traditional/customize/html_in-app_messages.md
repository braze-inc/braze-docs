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
Pour activer les messages in-app HTML via le SDK Web, il est nécessaire de fournir l'option`allowUserSuppliedJavascript`d'initialisation à Braze : par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.
{% endalert %}

## Pont JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}

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

![Interaction avec l’aperçu HTML en faisant défiler les pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Toutes les méthodes Javascript `brazeBridge` que vous utilisez dans votre HTML ne mettent pas à jour les profils utilisateur lors de la prévisualisation dans le tableau de bord.
{% endalert %}

### Exigences du SDK {#supported-sdk-versions}

Pour utiliser l’aperçu HTML des messages in-app, vous devez mettre à niveau les versions minimum suivantes du SDK Braze :

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Étant donné que ce type de message ne peut être reçu que par certaines versions ultérieures du SDK, les utilisateurs qui utilisent des versions non prises en charge du SDK ne recevront pas le message. Pensez à adopter ce type de message quand une partie importante de votre base d’utilisateurs est accessible, ou ciblez uniquement les utilisateurs dont la version d’application est ultérieure aux exigences. En savoir plus sur le [filtrage en fonction de la version la plus récente de l'application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Créer une campagne {#instructions}

Les utilisateurs de votre application mobile doivent effectuer une mise à niveau vers les versions SDK prises en charge afin de recevoir un message in-app **avec code personnalisé**. Nous vous recommandons de [pousser les utilisateurs à mettre à jour]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) leurs applications mobiles avant de lancer des campagnes qui dépendent de versions plus récentes du SDK de Braze.

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

1. Les ressources ajoutées à une campagne via la bibliothèque multimédia permettent d'afficher vos messages même lorsque l'utilisateur est hors ligne ou dispose d'une connexion Internet de mauvaise qualité.
2. Les ressources téléchargées dans Braze peuvent être réutilisées dans les campagnes.

##### Ajout de fichiers de ressources

Vous pouvez ajouter des ressources nouvelles ou existantes à votre campagne.

Pour ajouter de nouvelles ressources à votre campagne, utilisez la section de glisser-déposer pour télécharger un fichier. Les ressources ajoutées dans cette section seront également ajoutées automatiquement à la bibliothèque multimédia. Pour ajouter des ressources que vous avez déjà téléchargées dans la bibliothèque multimédia, sélectionnez **Ajouter à partir de la bibliothèque multimédia**.

Une fois vos ressources ajoutées, elles apparaîtront dans la section **Ressources pour cette campagne.**  

Si le nom de fichier d'une ressource correspond à celui d'une ressource HTML locale, elle est automatiquement remplacée (par exemple, si`cat.png`  est téléchargé et que`<img src="cat.png" />`  existe déjà). 

Sinon, survolez une ressource dans la liste et sélectionnez <i class="fas fa-copy"></i> **Copy** pour copier l'URL du fichier dans votre presse-papiers. Collez ensuite l’URL de la ressource copiée dans votre HTML comme lors du référencement d’une ressource distante.

### Éditeur HTML

Les modifications effectuées dans le HTML sont automatiquement affichées dans le panneau d’aperçu à la saisie. Toutes les méthodes [JavaScript`brazeBridge` ](#bridge) que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateurs lors de la prévisualisation dans le tableau de bord.

{% alert tip %}
Vous pouvez sélectionner<i class="fa-solid fa-magnifying-glass"></i>**Rechercher** dans l'éditeur HTML pour effectuer une recherche dans votre code.
{% endalert %}

### Suivi des boutons {#button-tracking-improvements}

Vous pouvez suivre les performances dans votre message in-app avec code personnalisé à l’aide de la méthode Javascript [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/). Pour la référence complète, veuillez consulter [les méthodes JavaScript Bridge](#bridge) ci-dessus.

{% alert note %}
Cette méthode de suivi des boutons remplace les anciennes méthodes de suivi automatique des clics (telles que `?abButtonId=0`), qui ont été supprimées.
{% endalert %}

### Changements non-rétrocompatibles {#backward-incompatible-changes}

1. Les exigences de SDK sont le changement incompatible le plus notable avec ce nouveau type de message. Les utilisateurs dont le SDK de l'app ne répond pas aux [exigences minimales en matière de version du SDK](#supported-sdk-versions) ne verront pas le message s'afficher.
2. Le lien profond `braze://close`, auparavant pris en charge par les applications mobiles, a été supprimé en faveur du Javascript `brazeBridge.closeMessage()`. Vous bénéficiez ainsi de messages HTML multiplateforme, sachant que le Web ne prend pas en charge les liens profonds.
3. Le suivi automatique des clics, qui utilisait `?abButtonId=0` pour les ID de boutons et le suivi de clics dans le corps pour les boutons de fermeture, a été supprimé. Les exemples de code suivants montrent comment modifier votre HTML pour utiliser nos nouvelles méthodes Javascript de suivi des clics :

   | Avant | Après |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_070d8d89-2417-4055-881a-afbca50be046/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_71a13303-c6e2-4bd4-a3ae-4f521bce2a78/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_dd691bf3-bf93-47b2-acc2-0d9393752531/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_b1cc5eac-cfdd-489a-b510-9ea9cf11ff2e/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_15393df5-6914-4b03-89df-0d0f693d36f2/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

