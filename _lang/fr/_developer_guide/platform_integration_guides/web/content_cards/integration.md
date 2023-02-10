---
nav_title: Intégration
article_title: Intégration d’une carte de contenu pour le Web
page_order: 0
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article couvre l’intégration d’une carte de contenu pour le Web, y compris les modèles de données de carte de contenu, les options standard d’IU de flux et des méthodes de carte supplémentaires."
search_rank: 4
---

# Intégration d’une carte de contenu

{% multi_lang_include archive/web-v4-rename.md %}

## Modèle de données de carte de contenu {#data-models}

Le modèle de données de cartes de contenu est disponible dans le SDK Web.

## Modèle de carte de contenu
Le SDK Braze pour le Web propose trois types de carte de contenu : [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), et [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Chaque type hérite des propriétés communes d’un modèle de [carte](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de contenu de base : Card

|Propriété|Description|
|---|---|
| `expiresAt` | L’horodatage UNIX du moment d’expiration de la carte.|
| `extras`| (Facultatif) Les données de paires clé-valeur formatées en tant qu’objet de chaîne de caractères avec une chaîne de valeur. |
| `id` | (Facultatif) L’ID de la carte. Cela sera rapporté à Braze avec des événements à des fins d’analytique. |
| `pinned` | Cette propriété reflète si la carte a été définie comme « épinglée » dans le tableau de bord.|
| `updated` | L’horodatage UNIX de la dernière modification de cette carte. |
| `viewed` | Cette propriété indique si l’utilisateur a vu la carte ou non.|
| `isControl` | Cette propriété est `true` lorsqu’une carte est un groupe de « contrôle » au cours d’un test A/B.|
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la Content Cards bannière : Banner

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport d’aspect de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est purement destinée à l’organisation de votre implémentation personnalisée. Ces catégories peuvent être définies dans le monteur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `url` | L’URL qui sera ouvert après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte de contenu de l’image sous-titrée : CaptionedImage

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport d’aspect de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est purement destinée à l’organisation de votre implémentation personnalisée. Ces catégories peuvent être définies dans le monteur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `title` | Le texte du titre pour cette carte. |
| `url` | L’URL qui sera ouvert après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la Classic Content Card : ClassicCard

|Propriété|Description|
|---|---|
| `aspectRatio` | Le rapport d’aspect de l’image de la carte sert d’indice avant le chargement complet de l’image. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
| `categories` | Cette propriété est purement destinée à l’organisation de votre implémentation personnalisée. Ces catégories peuvent être définies dans le monteur du tableau de bord. |
| `clicked` | Cette propriété indique si cette carte a déjà été cliquée sur cet appareil. |
| `created` | L’horodatage UNIX du moment de création de la carte depuis Braze. |
| `description` | Le texte du corps pour cette carte. |
| `dismissed` | Cette propriété indique si cette carte a été rejetée. |
| `dismissible` | Cette propriété reflète si l’utilisateur peut rejeter la carte, la supprimant de la vue. |
| `imageUrl` | L’URL de l’image de la carte.|
| `linkText` | Le texte d’affichage de l’URL. |
| `title` | Le texte du titre pour cette carte. |
| `url` | L’URL qui sera ouvert après avoir cliqué sur la carte. |
{: .reset-td-br-1 .reset-td-br-2}

## Méthodes de carte

|Méthode | Description | Lien|
|---|---|---|
|`logContentCardImpressions`| Enregistre un événement d’impression pour la liste de cartes donnée. Cela est nécessaire si vous utilisez une IU personnalisée et non l’IU Braze.| [Documents JS pour logCardImpressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)|
|`logCardClick`| Enregistre un événement de clic pour une carte donnée. Cela est nécessaire si vous utilisez une IU personnalisée et non l’IU Braze.| [Documents JS pour logCardClick](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardclick)|
|`showContentCards`| Affiche les cartes de contenu de l’utilisateur. | [Documents JS pour showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)|
|`hideContentCards`| Masque les cartes de contenu Braze actuellement affichées. | [Documents JS pour hideContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)
|`toggleContentCards`| Affiche les cartes de contenu de l’utilisateur. | [Documents JS pour toggleContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)
|`getCachedContentCards()`|Obtient toutes les cartes actuellement disponibles depuis le dernier rafraîchissement de cartes de contenu.| [Documents JS pour getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|
|`subscribeToContentCardsUpdates(subscriber)`| Abonne aux mises à jour des cartes de contenu. <br> La fonction de rappel de l’abonné sera appelée chaque fois que les cartes de contenu seront mises à jour. |  [Documents JS pour subscribeToContentCardsUpdates](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)|
|`dismissCard()`|Rejette la carte de manière programmatique (disponible dans la version 2.4.1).| [Documents JS pour dismissCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismissCard)|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Reportez-vous à la [documentation JS](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) pour plus de détails

## Intégration d’une carte de contenu

Le SDK Braze pour le Web comprend une IU de flux de cartes de contenu pour accélérer vos efforts d’intégration. Si vous préférez construire votre propre IU, consultez la page [IU personnalisée]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/).

### IU de flux standard

Pour utiliser l’IU de cartes de contenu comprise, vous devez spécifier où afficher le flux sur votre site Internet. 

Dans cet exemple, nous avons un `<div id="feed"></div>` dans lequel nous voulons placer le flux de cartes de contenu. Nous utiliserons trois boutons pour masquer, afficher ou basculer le flux (masquer ou afficher en fonction de son état actuel).

```html

<button id="toggle" type="button">Basculer le fil des cartes</button>
<button id="hide" type="button">Dissimuler le fil des cartes</button>
<button id="show" type="button">Afficher le fil des cartes</button>

<nav>
    <h1>Votre fil personnalisé</h1>
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
{: .reset-td-br-1 .reset-td-br-2}

[Consultez les documents JS](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) pour plus d’informations sur la bascule des cartes de contenu.

## Groupe de contrôle 

Si vous utilisez les flux de cartes de contenu par défaut de Braze, les impressions et les clics seront automatiquement suivis.

Si vous utilisez une intégration personnalisée pour les cartes de contenu, votre intégration doit enregistrer les impressions lorsqu’une carte de contrôle aurait dû être vue ; même pour les cartes de « contrôle » durant un test A/B.

Pour déterminer si une carte de contenu se trouve dans le groupe de « contrôle » d’un test A/B, vous pouvez vérifier la propriété `card.isControl` (Web SDK v4.5.0+) ou vérifier si la carte est une instance ControlCard (`card instanceof braze.ControlCard`).

{% alert note %}
Consultez les articles de personnalisation suivants pour obtenir de la documentation sur l’ajout d’une [IU personnalisée]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/), de [style personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling), de [paires clé-valeur]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/key_value_pairs), d’[indicateurs de messages non lus et lus]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/read_and_unread/) et de [demande de dénombrement des cartes de contenu non visualisées]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/badges).
{% endalert %}

