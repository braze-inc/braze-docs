{% multi_lang_include archive/web-v4-rename.md %}

## Conditions préalables

Avant de pouvoir utiliser les cartes de contenu, vous devez [intégrer le SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) dans votre application. Cependant, aucune configuration supplémentaire n'est nécessaire. Pour créer votre propre interface utilisateur, consultez le [Guide de personnalisation des cartes de contenu.]({{site.baseurl}}/developer_guide/content_cards/)

## IU de flux standard

Pour utiliser l’IU de cartes de contenu comprise, vous devez spécifier où afficher le flux sur votre site Internet. 

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

Lorsque vous utilisez les méthodes `toggleContentCards(parentNode, filterFunction)` et `showContentCards(parentNode, filterFunction)`, si aucun argument n’est fourni, toutes les cartes de contenu seront affichées dans une barre latérale à position fixe sur le côté droit de la page. Sinon, l’alimentation sera placée dans les options `parentNode` de l’appareil.

|Paramètres | Description |
|---|---|
|`parentNode` | Le nœud HTML pour y afficher les cartes de contenu. Si le nœud parent possède déjà une vue de carte de contenu Braze comme descendant direct, les cartes de contenu existantes seront remplacées. Par exemple, vous devriez transmettre en `document.querySelector(".my-container")`.|
|`filterFunction` | Un filtre ou une fonction de tri pour les cartes affichées dans cette vue. Invoqué avec le tableau d’objets `Card`, triés selon `{pinned, date}`. On s’attend à ce qu’il retourne un tableau d’objets `Card` triés à afficher pour cet utilisateur. S’il est omis, toutes les cartes seront affichées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Consultez la documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) pour plus d'informations sur la façon de basculer les cartes de contenu.

## Types de cartes et propriétés

Le modèle de données des cartes de contenu est disponible dans le SDK Web et offre les types de cartes de contenu suivants : [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) et [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Chaque type hérite des propriétés communes d'un modèle de base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) et possède les propriétés supplémentaires suivantes.

{% alert tip %}
Pour enregistrer les données de la carte de contenu, reportez-vous à la section [Enregistrement des analyses des]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) cartes.
{% endalert %}

### Modèle de carte de base

Toutes les cartes de contenu ont ces propriétés communes :

|Propriété|Description|
|---|---|
| `expiresAt` | L’horodatage UNIX du moment d’expiration de la carte.|
| `extras`| (Facultatif) Les données de paires clé-valeur formatées en tant qu’objet de chaîne de caractères avec une chaîne de valeur. |
| `id` | (Facultatif) L’ID de la carte. Cela sera rapporté à Braze avec des événements à des fins d’analytique. |
| `pinned` | Cette propriété reflète si la carte a été définie comme « épinglée » dans le tableau de bord.|
| `updated` | L’horodatage UNIX de la dernière modification de cette carte. |
| `viewed` | Cette propriété indique si l’utilisateur a vu la carte ou non.|
| `isControl` | Cette propriété est `true` lorsqu’une carte est un groupe de « contrôle » au cours d’un test A/B.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image uniquement

Les cartes [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) sont des images cliquables en taille réelle.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété vous permet d'organiser votre mise en œuvre personnalisée. Ces catégories peuvent être définies dans le générateur de tableaux de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `url` | L’URL qui sera ouverte après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image avec légende

Les cartes d'[images sous-titrées](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété vous permet d'organiser votre mise en œuvre personnalisée. Ces catégories peuvent être définies dans le générateur de tableaux de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `title` | Le texte du titre pour cette carte. |
| `url` | L’URL qui sera ouverte après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classique

Le modèle [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) peut contenir une image sans texte ou un texte avec image.

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport hauteur/largeur de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété vous permet d'organiser votre mise en œuvre personnalisée. Ces catégories peuvent être définies dans le générateur de tableaux de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `description` | Le texte du corps pour cette carte. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `title` | Le texte du titre pour cette carte. |
| `url` | L’URL qui sera ouverte après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Groupe de contrôle

Si vous utilisez le flux par défaut des cartes de contenu, les impressions et les clics seront automatiquement suivis.

Si vous utilisez une intégration personnalisée pour les cartes de contenu, vous devez [enregistrer les impressions]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) lorsqu'une carte de contrôle aurait été vue. Dans ce cadre, veillez à gérer les cartes de contrôle lorsque vous enregistrez des impressions dans un test A/B. Ces cartes sont vierges et, bien qu'elles ne soient pas vues par les utilisateurs, vous devriez tout de même enregistrer les impressions afin de comparer leurs performances à celles des cartes de non-contrôle.

Pour déterminer si une carte de contenu se trouve dans le groupe de contrôle pour un test A/B, vérifiez la propriété `card.isControl` (SDK Web v4.5.0+) ou vérifiez si la carte est une instance de `ControlCard` (`card instanceof braze.ControlCard`).

## Méthodes de carte

|Méthode | Description |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Enregistre un événement d’impression pour la liste de cartes donnée. Cela est nécessaire si vous utilisez une IU personnalisée et non l’IU Braze.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Enregistre un événement de clic pour une carte donnée. Cela est nécessaire si vous utilisez une IU personnalisée et non l’IU Braze.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Affiche les cartes de contenu de l’utilisateur. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Masque les cartes de contenu Braze actuellement affichées. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Affiche les cartes de contenu de l’utilisateur. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|Obtient toutes les cartes actuellement disponibles depuis le dernier rafraîchissement de cartes de contenu.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Abonne aux mises à jour des cartes de contenu. <br> La fonction de rappel de l’abonné sera appelée chaque fois que les cartes de contenu seront mises à jour. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|Rejette la carte de manière programmatique (disponible dans la version 2.4.1).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus de détails, reportez-vous à la [documentation de référence du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)

## Utilisation de Google Tag Manager

Google Tag Manager fonctionne en injectant le [réseau de diffusion de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (une version de notre SDK Web) directement dans le code de votre site web, ce qui signifie que toutes les méthodes du SDK sont disponibles comme si vous aviez intégré le SDK sans Google Tag Manager, sauf lors de l'implémentation des cartes de contenu.

### Mise en place des cartes de contenu

{% tabs local %}
{% tab Google Tag Manager %}
Pour une intégration standard du flux de la carte de contenu, vous pouvez utiliser une étiquette **HTML personnalisée** dans Google Tag Manager. Ajoutez ce qui suit à votre balise HTML personnalisée, ce qui activera le flux de carte de contenu standard :

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuration dans Google Tag Manager d'une étiquette HTML personnalisée qui affiche le flux de la carte de contenu.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manuel %}
Pour obtenir plus de libertés pour personnaliser l’apparence de vos cartes de contenu et leurs flux, vous pouvez intégrer directement les cartes de contenu dans votre site Internet natif. Vous pouvez suivre deux approches dans ce domaine : utiliser l’IU de flux standard ou créer une IU de flux personnalisée.

{% subtabs local %}
{% subtab standard feed %}
Lors de l'implémentation de l'[interface utilisateur standard]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), les méthodes de Braze doivent être précédées de `window.`. Par exemple, `braze.showContentCards` devrait être `window.braze.showContentCards` à la place.
{% endsubtab %}

{% subtab custom feed %}
Pour l’habillage du [flux personnalisé]({{site.baseurl}}/developer_guide/content_cards/creating_cards/), les étapes sont les mêmes que si vous aviez intégré le SDK sans GTM. Par exemple, si vous désirez personnaliser la largeur de votre flux de carte de contenu, vous pouvez coller ce qui suit dans votre fichier CSS :

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

Pour obtenir la dernière version du SDK Web de Braze, effectuez les trois étapes suivantes dans votre tableau de bord Google Tag Manager :

1. **Mise à jour du modèle de balise**<br>Accédez à la page **Modèles** de votre espace de travail. Vous devez y voir une icône indiquant qu’une mise à jour est disponible.<br><br>![Modèles de page indiquant qu'une mise à jour est disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Cliquez sur cette icône et, après avoir révisé la modification, cliquez sur **Accepter la mise à jour**.<br><br>![Un écran comparant les anciens et les nouveaux modèles d'étiquettes avec un bouton pour "Accepter la mise à jour"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Mise à jour du numéro de version**<br>Une fois votre modèle de balise mis à jour, modifiez la balise d’initialisation Braze et mettez à jour la version SDK sur la version la plus récente`major.minor`. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modèle d'initialisation de Braze avec un champ de saisie pour changer la version du SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **AQ et publication**<br>Vérifiez que la nouvelle version du SDK fonctionne à l'aide de l' [outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager avant de publier une mise à jour de votre conteneur d'étiquettes.

### Résolution des problèmes{#troubleshooting}

#### Activer le débogage de balise {#debugging}

Chaque modèle de balise de Braze dispose d’une case à cocher facultative **Débogage de balises GTM** qui peut être utilisée pour enregistrer les messages de débogage sur la console JavaScript de votre page Web.

![L'outil de gestion de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrer dans le mode débogage

Un autre moyen de déboguer l'intégration de Google Tag Manager est d'utiliser la fonctionnalité de [prévisualisation](https://support.google.com/tagmanager/answer/6107056) de Google.

Cela permet d'identifier les valeurs envoyées par la couche de données de votre page web à chaque étiquette Braze déclenchée et d'expliquer quelles étiquettes ont été déclenchées ou non.

![La page de résumé de l'étiquette d'initialisation de Braze fournit un aperçu de l'étiquette, y compris des informations sur les tags qui ont été déclenchés.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Activer la jounalisation verbeuse

Pour permettre à l’assistance technique de Braze de soutenir les journaux d’accès lors du test, vous pouvez activer la journalisation verbeuse sur votre intégration de Google Tag Manager. Ces journaux apparaîtront dans l'onglet **Console** des outils de développement de votre navigateur [.](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)

Dans votre intégration Google Tag Manager, accédez à votre balise d’initialisation Braze et sélectionnez **Activer la journalisation du SDK Web**.

![La page de résumé de l'étiquette d'initialisation de Braze avec l'option Activer la journalisation du SDK Web activée.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
