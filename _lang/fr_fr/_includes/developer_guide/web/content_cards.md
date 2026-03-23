{% multi_lang_include archive/web-v4-rename.md %}

## Conditions préalables

Avant de pouvoir utiliser les cartes de contenu, vous devez [intégrer le SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) dans votre application. Cependant, aucune configuration supplémentaire n'est nécessaire. Pour créer votre propre interface utilisateur, consultez le [Guide de personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/).

## IU de flux standard

Pour utiliser l'IU de cartes de contenu incluse, vous devez spécifier où afficher le flux sur votre site Internet.

Dans cet exemple, nous avons un `<div id="feed"></div>` dans lequel nous voulons placer le flux de cartes de contenu. Nous utiliserons trois boutons pour masquer, afficher ou basculer le flux (masquer ou afficher en fonction de son état actuel).

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

Lorsque vous utilisez les méthodes `toggleContentCards(parentNode, filterFunction)` et `showContentCards(parentNode, filterFunction)`, si aucun argument n'est fourni, toutes les cartes de contenu seront affichées dans une barre latérale à position fixe sur le côté droit de la page. Sinon, le flux sera placé dans l'option `parentNode` spécifiée.

|Paramètres | Description |
|---|---|
|`parentNode` | Le nœud HTML dans lequel afficher les cartes de contenu. Si le nœud parent possède déjà une vue de cartes de contenu Braze comme descendant direct, les cartes de contenu existantes seront remplacées. Par exemple, vous devriez transmettre `document.querySelector(".my-container")`.|
|`filterFunction` | Un filtre ou une fonction de tri pour les cartes affichées dans cette vue. Invoquée avec le tableau d'objets `Card`, triés selon `{pinned, date}`. Doit retourner un tableau d'objets `Card` triés à afficher pour cet utilisateur. Si omis, toutes les cartes seront affichées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consultez la documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) pour plus d'informations sur la façon de basculer les cartes de contenu.

## Tester les cartes de contenu sur le web

Vous pouvez tester votre intégration de cartes de contenu à l'aide des outils de développement de votre navigateur.

1. Créez une campagne de cartes de contenu et ciblez votre utilisateur test.
2. Connectez-vous au site web qui intègre votre SDK Web.
3. Ouvrez la console de votre navigateur. Pour Chrome, faites un clic droit sur la page, sélectionnez **Inspecter**, puis sélectionnez l'onglet **Console**.
4. Exécutez ces commandes dans la console :
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Types de cartes et propriétés

Le modèle de données des cartes de contenu est disponible dans le SDK Web et offre les types de cartes de contenu suivants : [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) et [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Chaque type hérite des propriétés communes d'un modèle de base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) et possède les propriétés supplémentaires suivantes.

{% alert tip %}
Pour enregistrer les données des cartes de contenu, consultez la section [Enregistrement des analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Modèle de carte de base

Toutes les cartes de contenu partagent ces propriétés :

|Propriété|Description|
|---|---|
| `expiresAt` | L'horodatage UNIX du moment d'expiration de la carte.|
| `extras`| (Facultatif) Données de paires clé-valeur formatées en tant qu'objet chaîne de caractères avec une valeur chaîne de caractères. |
| `id` | (Facultatif) L'ID de la carte. Celui-ci sera transmis à Braze avec les événements à des fins d'analytique. |
| `pinned` | Cette propriété indique si la carte a été définie comme « épinglée » dans le tableau de bord.|
| `updated` | L'horodatage UNIX de la dernière modification de cette carte. |
| `viewed` | Cette propriété indique si l'utilisateur a vu la carte ou non.|
| `isControl` | Cette propriété vaut `true` lorsqu'une carte est un groupe de « contrôle » dans un test A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image uniquement

Les cartes [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) sont des images cliquables en taille réelle.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant le chargement complet de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est destinée uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L'URL de l'image de la carte.|
| `linkText` | Le texte d'affichage de l'URL. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image avec légende

Les cartes [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant le chargement complet de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est destinée uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L'URL de l'image de la carte.|
| `linkText` | Le texte d'affichage de l'URL. |
| `title` | Le texte du titre de cette carte. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classique

Le modèle [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) peut contenir une image sans texte ou un texte avec image.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l'image de la carte, servant d'indication avant le chargement complet de l'image. Notez que cette propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est destinée uniquement à l'organisation dans votre implémentation personnalisée ; ces catégories peuvent être définies dans le compositeur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L'horodatage UNIX du moment de création de la carte depuis Braze. |
| `description` | Le texte du corps de cette carte. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété indique si l'utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L'URL de l'image de la carte.|
| `linkText` | Le texte d'affichage de l'URL. |
| `title` | Le texte du titre de cette carte. |
| `url` | L'URL qui sera ouverte après un clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Groupe de contrôle

Si vous utilisez le flux par défaut des cartes de contenu, les impressions et les clics seront automatiquement suivis.

Si vous utilisez une intégration personnalisée pour les cartes de contenu, vous devez [enregistrer les impressions]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) lorsqu'une carte de contrôle aurait été vue. Dans ce cadre, veillez à gérer les cartes de contrôle lorsque vous enregistrez des impressions dans un test A/B. Ces cartes sont vierges et, bien qu'elles ne soient pas vues par les utilisateurs, vous devez tout de même enregistrer les impressions afin de comparer leurs performances à celles des cartes hors contrôle.

Pour déterminer si une carte de contenu se trouve dans le groupe de contrôle d'un test A/B, vérifiez la propriété `card.isControl` (SDK Web v4.5.0+) ou vérifiez si la carte est une instance de `ControlCard` (`card instanceof braze.ControlCard`).

## Méthodes de carte

### Méthodes de flux par défaut

Utilisez ces méthodes lorsque vous affichez les cartes de contenu avec l'IU par défaut de Braze :

|Méthode | Description |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Affiche le flux par défaut des cartes de contenu. Rend les cartes dans un élément HTML `parentNode` fourni, ou sous forme de barre latérale à position fixe sur le côté droit de la page si aucun élément n'est spécifié. Accepte une `filterFunction` facultative pour trier ou filtrer les cartes avant l'affichage. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Masque le flux par défaut des cartes de contenu s'il est actuellement affiché. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Affiche le flux par défaut des cartes de contenu s'il est masqué, ou le masque s'il est visible. Si vous devez afficher plusieurs flux de cartes de contenu simultanément, utilisez plutôt `showContentCards` et `hideContentCards`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Méthodes de flux personnalisé

Utilisez ces méthodes lorsque vous créez votre propre IU de cartes de contenu :

|Méthode | Description |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Enregistre une fonction de rappel invoquée chaque fois que les cartes de contenu sont mises à jour pour l'utilisateur actuel, par exemple au démarrage de la session. Utilisez cette méthode comme moyen principal de recevoir les données de cartes pour votre flux personnalisé. Elle doit être appelée avant `openSession()` pour recevoir les mises à jour de la session initiale. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| Retourne toutes les cartes actuellement disponibles depuis le dernier rafraîchissement des cartes de contenu. Utilisez cette méthode pour afficher immédiatement les cartes au chargement de la page sans attendre une nouvelle requête serveur, par exemple lorsque l'utilisateur revient sur une page pendant une session active. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Demande un rafraîchissement immédiat des cartes de contenu depuis les serveurs Braze. Par défaut, les cartes sont rafraîchies au démarrage de la session et lorsque le flux par défaut est rouvert. Utilisez cette méthode pour forcer un rafraîchissement à d'autres moments, par exemple après une action spécifique de l'utilisateur. Tenez compte des [limites de débit]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/#rate-limit). |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Enregistre des événements d'impression pour un tableau de cartes. Appelez cette méthode lorsque les cartes sont rendues et visibles par l'utilisateur. Nécessaire pour un reporting de campagne précis lors de l'utilisation d'une IU personnalisée, car les impressions ne sont pas suivies automatiquement en dehors du flux par défaut. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Enregistre un événement de clic pour une carte unique. Appelez cette méthode lorsqu'un utilisateur interagit avec une carte dans votre IU personnalisée. Nécessaire pour un reporting de campagne précis, car les clics ne sont pas suivis automatiquement en dehors du flux par défaut. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| Traite l'URL d'une carte et exécute l'action au clic configurée, y compris les actions Braze (URLs `brazeActions://`) et la navigation URL standard. Appelez cette méthode dans votre gestionnaire de clic de carte pour vous assurer que les comportements au clic configurés dans le tableau de bord de Braze sont exécutés. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| Rejette une carte de manière programmatique, la supprimant du flux de l'utilisateur. Utilisez cette méthode pour permettre aux utilisateurs de rejeter des cartes dans votre IU personnalisée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus de détails, reportez-vous à la [documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Bonnes pratiques

### Appeler les méthodes dans le bon ordre

Pour les flux personnalisés, les cartes de contenu ne sont rafraîchies au démarrage de la session que si `subscribeToContentCardsUpdates()` est appelée avant `openSession()`. Appelez vos méthodes Braze dans cet ordre :

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Utiliser les cartes en cache pour conserver le contenu entre les chargements de page

Étant donné que `subscribeToContentCardsUpdates()` n'invoque son rappel que lorsqu'il y a de nouvelles mises à jour (par exemple au démarrage de la session), les cartes peuvent disparaître de votre flux personnalisé si un utilisateur actualise la page en cours de session. Pour éviter cela, utilisez `getCachedContentCards()` pour afficher immédiatement les cartes depuis le cache local, en complément de votre abonnement aux nouvelles mises à jour :

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Enregistrer les analyses pour les flux personnalisés

Lorsque vous utilisez une IU personnalisée, les impressions, les clics et les rejets ne sont pas suivis automatiquement. Vous devez enregistrer chaque événement manuellement :

- **Impressions :** Appelez `logContentCardImpressions([card1, card2, ...])` avec un tableau d'objets carte lorsque les cartes deviennent visibles pour l'utilisateur.
- **Clics :** Appelez `logContentCardClick(card)` lorsqu'un utilisateur interagit avec une carte.
- **Comportement au clic :** Appelez `handleBrazeAction(card.url)` pour exécuter l'action au clic configurée de la carte (comme naviguer vers une URL ou enregistrer un événement personnalisé).

{% alert warning %}
L'argument passé à `logContentCardClick()` doit être un objet `Card` Braze original. Si vous transformez ou reconstruisez les données de la carte (par exemple, en sérialisant et désérialisant), les clics ne seront pas enregistrés et vous verrez l'erreur : « card must be a Card object. »
{% endalert %}

## Utilisation de Google Tag Manager

Google Tag Manager fonctionne en injectant le [réseau de diffusion de contenu de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (une version de notre SDK Web) directement dans le code de votre site web, ce qui signifie que toutes les méthodes du SDK sont disponibles comme si vous aviez intégré le SDK sans Google Tag Manager, sauf lors de l'implémentation des cartes de contenu.

### Mise en place des cartes de contenu

{% tabs local %}
{% tab google tag manager %}
Pour une intégration standard du flux de cartes de contenu, vous pouvez utiliser une balise **HTML personnalisée** dans Google Tag Manager. Ajoutez ce qui suit à votre balise HTML personnalisée, ce qui activera le flux de cartes de contenu standard :

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuration de balise dans Google Tag Manager d'une balise HTML personnalisée montrant le flux de cartes de contenu.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Pour plus de liberté dans la personnalisation de l'apparence de vos cartes de contenu et de leur flux, vous pouvez intégrer directement les cartes de contenu dans votre site Internet natif. Deux approches s'offrent à vous : utiliser l'IU de flux standard ou créer une IU de flux personnalisée.

{% subtabs local %}
{% subtab standard feed %}
Lors de l'implémentation de l'[IU de flux standard]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), les méthodes de Braze doivent être précédées de `window.`. Par exemple, `braze.showContentCards` devrait être `window.braze.showContentCards` à la place.
{% endsubtab %}

{% subtab custom feed %}
Pour l'habillage du [flux personnalisé]({{site.baseurl}}/developer_guide/content_cards/creating_cards/), les étapes sont les mêmes que si vous aviez intégré le SDK sans GTM. Par exemple, si vous souhaitez personnaliser la largeur de votre flux de cartes de contenu, vous pouvez coller ce qui suit dans votre fichier CSS :

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Mise à jour des modèles {#upgrading}

Pour obtenir la dernière version du SDK Web de Braze, effectuez les trois étapes suivantes dans votre tableau de bord Google Tag Manager :

1. **Mise à jour du modèle de balise**<br>Accédez à la page **Modèles** de votre espace de travail. Vous devriez y voir une icône indiquant qu'une mise à jour est disponible.<br><br>![Page des modèles indiquant qu'une mise à jour est disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Cliquez sur cette icône et, après avoir examiné la modification, cliquez sur **Accepter la mise à jour**.<br><br>![Un écran comparant l'ancien et le nouveau modèle de balise avec un bouton « Accepter la mise à jour »]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Mise à jour du numéro de version**<br>Une fois votre modèle de balise mis à jour, modifiez la balise d'initialisation Braze et mettez à jour la version du SDK sur la version `major.minor` la plus récente. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modèle d'initialisation Braze avec un champ de saisie permettant de modifier la version du SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **AQ et publication**<br>Vérifiez que la nouvelle version du SDK fonctionne à l'aide de l'[outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager avant de publier une mise à jour de votre conteneur de balises.

### Résolution des problèmes {#troubleshooting}

#### Activer le débogage de balise {#debugging}

Chaque modèle de balise Braze dispose d'une case à cocher facultative **Débogage de balises GTM** qui peut être utilisée pour enregistrer les messages de débogage dans la console JavaScript de votre page web.

![Outil de débogage de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrer dans le mode débogage

Un autre moyen de déboguer votre intégration Google Tag Manager est d'utiliser la fonctionnalité de [prévisualisation](https://support.google.com/tagmanager/answer/6107056) de Google.

Cela permet d'identifier les valeurs envoyées par la couche de données de votre page web à chaque balise Braze déclenchée et d'expliquer quelles balises ont été déclenchées ou non.

![La page de résumé de la balise d'initialisation Braze fournit un aperçu de la balise, y compris des informations sur les balises déclenchées.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Vérifier le séquencement des balises pour les événements personnalisés {#tag-sequencing}

Si les événements personnalisés ou d'autres actions ne sont pas enregistrés dans Braze, une cause fréquente est une condition de concurrence où une balise d'action (comme **Événement personnalisé** ou **Achat**) se déclenche avant que la balise **Initialisation Braze** ne soit terminée. Pour corriger cela, configurez le [séquencement des balises](https://support.google.com/tagmanager/answer/6238868) dans GTM :

1. Ouvrez la balise d'action qui ne s'enregistre pas correctement.
2. Sous **Paramètres avancés** > **Séquencement des balises**, sélectionnez **Une balise qui se déclenche avant \[cette balise\]**.
3. Choisissez votre balise **Initialisation Braze** comme balise de configuration.

Cela garantit que le SDK est entièrement initialisé avant que les balises d'action ne tentent d'envoyer des données à Braze.

#### Activer la journalisation détaillée

Pour capturer des journaux détaillés à des fins de résolution des problèmes, vous pouvez activer la journalisation détaillée sur votre intégration Google Tag Manager. Ces journaux apparaîtront dans l'onglet **Console** des [outils de développement](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) de votre navigateur.

Dans votre intégration Google Tag Manager, accédez à votre balise d'initialisation Braze et sélectionnez **Activer la journalisation du SDK Web**.

![La page de résumé de la balise d'initialisation Braze avec l'option Activer la journalisation du SDK Web activée.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md