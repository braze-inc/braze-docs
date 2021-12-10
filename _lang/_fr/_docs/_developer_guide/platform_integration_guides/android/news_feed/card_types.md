---
nav_title: Types de cartes
article_title: Types de cartes de flux d'actualités pour Android/FireOS
page_order: 5
platform:
  - Android
  - Pare-feu
description: "Cet article couvre les différents types de cartes de News Feed et les différentes propriétés spécifiques à la carte disponibles."
channel:
  - fil d'actualité
---

# Types de carte
Braze a cinq types uniques de cartes de nouvelles qui partagent un modèle de base. Chaque type de carte possède également des propriétés spécifiques à la carte qui sont énumérées ci-dessous.

## Carte de base

Le modèle de la [carte de base][29] fournit le comportement de base pour toutes les cartes.

- `getId()` - retourne l'identifiant de la carte défini par Braze
- `getViewed()` - retourne un booléen reflet si la carte est lue ou non lue par l'utilisateur
- `getExtras()` - retourne une carte des options de valeur clé pour cette carte
- `setViewed(boolean)` - définit le champ visualisé d'une carte
- `getCreated()` - retourne l'horodatage unix du temps de création de la carte à partir du tableau de bord de Braze
- `getUpdated()` - retourne l'horodatage unix de la dernière mise à jour de la carte depuis le tableau de bord de Braze
- `getCategories()` - retourne la liste des catégories assignées à la carte, les cartes sans catégorie seront assignées ABKCardCategoryNoCategory
- `isInCategorySet(EnumSet)` - renvoie vrai si la carte appartient à la catégorie donnée définie

## Image de la bannière
Les [Cartes Image de bannière][30] sont des images pleines et cliquables. En plus des propriétés de la carte de base :

- `getImageUrl()` - retourne l'URL de l'image de la carte
- `getUrl()` - retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `getDomain()` - retourne le texte du lien pour la propriété url.

## Carte d'image sous-titrée
Les [Cartes d'images sous-titrées][31] sont cliquables en pleine taille avec le texte descriptif qui l'accompagne. En plus des propriétés de la carte de base :

- `getImageUrl()` - retourne l'URL de l'image de la carte
- `getTitle()` - retourne le texte du titre de la carte
- `getDescription()` - retourne le corps du texte de la carte
- `getUrl()` - retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `getDomain()` - retourne le texte du lien pour la propriété url.

## Carte d'annonce de texte (image sous-titrée sans image)
[Les Cartes d'Annonce de Texte][32] sont des cartes cliquables contenant du texte descriptif. En plus des propriétés de la carte de base :

- `getTitle()` - retourne le texte du titre de la carte
- `getDescription()` - retourne le corps du texte de la carte
- `getUrl()` - retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `getDomain()` - retourne le texte du lien pour la propriété url.

## Courte fiche d'actualité
[Les cartes d'actualités courtes][33] sont des cartes cliquables avec des images et du texte descriptif qui l'accompagne.  En plus des propriétés de la carte de base :

- `getImageUrl()` - retourne l'URL de l'image de la carte
- `getTitle()` - retourne le texte du titre de la carte
- `getDescription()` - retourne le corps du texte de la carte
- `getUrl()` - retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `getDomain()` - retourne le texte du lien pour la propriété url.

[29]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html
[30]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/BannerImageCard.html
[31]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CaptionedImageCard.html
[32]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/TextAnnouncementCard.html
[33]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/ShortNewsCard.html
