---
nav_title: Intégration
article_title: Intégration d’une carte de contenu pour le Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "Cet article couvre l’intégration d’une carte de contenu pour le Web, y compris les modèles de données de carte de contenu, les options standard d’IU de flux et des méthodes de carte supplémentaires."
search_rank: 1
---

# Intégration d’une carte de contenu

> Cet article couvre l’intégration d’une carte de contenu pour le Web, y compris les modèles de données de carte de contenu, les options standard d’IU de flux et des méthodes de carte supplémentaires.

{% multi_lang_include archive/web-v4-rename.md %}

Le SDK Braze pour le Web comprend une IU de flux de cartes de contenu pour accélérer vos efforts d’intégration. Si vous préférez créer votre propre interface utilisateur, consultez le [Guide de personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

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

## Modèle de données de cartes de contenu {#data-models}

Le modèle de données de cartes de contenu est disponible dans le SDK Web.

Le SDK Braze pour le Web propose trois types de carte de contenu : [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) et [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Chaque type hérite des propriétés communes d'un modèle de base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) et possède les propriétés supplémentaires suivantes.

Voir [Enregistrer les analyses]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) pour plus d'informations sur l’abonnement aux données de cartes.

### Propriétés du modèle de carte de contenu de base : Card

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

### Propriétés de la carte de contenu pour les images seulement - ImageOnly

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

### Propriétés de la carte de contenu de l’image sous-titrée : CaptionedImage

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

### Propriétés de la Classic Content Card : ClassicCard

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

Si vous utilisez une intégration personnalisée pour les cartes de contenu, vous devez [enregistrer les impressions]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/) lorsqu'une carte de contrôle aurait été vue. Dans ce cadre, veillez à gérer les cartes de contrôle lorsque vous enregistrez des impressions dans un test A/B. Ces cartes sont vierges et, bien qu'elles ne soient pas vues par les utilisateurs, vous devriez tout de même enregistrer les impressions afin de comparer leurs performances à celles des cartes de non-contrôle.

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

{% alert note %}
Vous souhaitez aller plus loin ? Lorsque vous aurez compris les principes de base des cartes de contenu, consultez le [Guide de personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards) pour commencer à les personnaliser.
{% endalert %}
