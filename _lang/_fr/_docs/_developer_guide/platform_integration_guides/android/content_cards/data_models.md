---
nav_title: Intégration
article_title: Intégration de la carte de contenu pour Android/FireOS
page_order: 1
platform:
  - Android
  - Pare-feu
description: "Cet article couvre l’intégration de la Carte de Contenu et les différents modèles de données et propriétés spécifiques à la carte disponibles pour votre application Android."
channel:
  - cartes de contenu
---

# Intégration des cartes de contenu

Dans Android, le flux des Cartes de Contenu est implémenté en tant que [Fragment][2] qui sont disponibles dans le projet d'interface d'Android Braze. Consultez la documentation de [Google sur Fragments][3] pour plus d'informations sur comment ajouter un fragment à une activité.

La classe [`ContentCardsFragment`][4] actualisera automatiquement et affichera le contenu des Cartes de Contenu et des analyses d'utilisation des logs. Les cartes qui peuvent apparaître dans les ContentCards d'un utilisateur sont créées sur le tableau de bord Braze.

## Modèle de données des cartes de contenu
Le modèle de données des Cartes de Contenu est disponible dans le SDK Android.

## Types de carte {#card-types-for-android}
Braze a 3 types de cartes de contenu uniques qui partagent un modèle de base. Chaque type de carte possède également des propriétés spécifiques à la carte qui sont énumérées ci-dessous.

### Carte de base {#base-card-for-android}

Le modèle de la [carte de base][29] fournit le comportement de base pour toutes les cartes.

| Propriété               | Libellé                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `getId()`               | Renvoie l'ID de la carte défini par Braze.                                                                           |
| `getViewed()`           | Retourne un booléen reflétant si la carte est lue ou non lue par l'utilisateur.                                      |
| `getExtras()`           | Retourne une carte des options de valeur clé pour cette carte.                                                       |
| `getCreated()`          | Retourne l'horodatage unix de l'heure de création de la carte depuis Braze.                                          |
| `Epinglé`               | Retourne un booléen qui indique si la carte est épinglée.                                                            |
| `getOpenUriInWebView()` | Renvoie un booléen qui reflète si Uris pour cette carte doit être ouvert <br> dans le WebView de Braze ou non. |
| `getExpiredAt()`        | Récupère la date d'expiration de la carte.                                                                           |
| `getIsSupprimé()`       | Retourne un booléen qui montre si l'utilisateur final a rejeté cette carte.                                          |
| `getIsDismissible()`    | Retourne un booléen qui indique si la carte est épinglée.                                                            |
{: .reset-td-br-1 .reset-td-br-2}

### Image de la bannière {#banner-image-card-for-android}
Les [Cartes Image de bannière][30] sont des images pleines et cliquables. En plus des propriétés de la carte de base :

| Propriété       | Libellé                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `getImageUrl()` | Retourne l'URL de l'image de la carte.                                                                                       |
| `getUrl()`      | Retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole. |
| `getDomain()`   | Retourne le texte du lien pour l'URL de la propriété.                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

### Carte d'image sous-titrée {#captioned-image-card-for-android}
Les [Cartes d'images sous-titrées][31] sont cliquables en pleine taille avec le texte descriptif qui l'accompagne. En plus des propriétés de la carte de base :

| Propriété          | Libellé                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `getImageUrl()`    | Retourne l'URL de l'image de la carte.                                                                                       |
| `getTitle()`       | Renvoie le texte du titre de la carte.                                                                                       |
| `getDescription()` | Renvoie le corps du texte de la carte.                                                                                       |
| `getUrl()`         | Retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole. |
| `getDomain()`      | Retourne le texte du lien pour l'URL de la propriété.                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

### Carte classique {#text-Announcement-card-for-android}
[Les Cartes d'Annonce de Texte][32] sont des cartes cliquables contenant du texte descriptif. [Les cartes d'actualités courtes][41] sont des cartes cliquables incluant du texte et des images. En plus des propriétés de la carte de base :

| Propriété          | Libellé                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `getTitle()`       | Renvoie le texte du titre de la carte.                                                                                       |
| `getDescription()` | Renvoie le corps du texte de la carte.                                                                                       |
| `getUrl()`         | Retourne l'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole. |
| `getDomain()`      | Retourne le texte du lien pour l'URL de la propriété.                                                                        |
| `getImageUrl()`    | Renvoie l'URL de l'image de la carte, ne s'applique qu'à la carte Short News classique.                                      |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Veuillez noter qu'une carte classique, sans image incluse, donnera lieu à une carte d'annonce textuelle. Si une image est incluse, vous recevrez une courte fiche d'actualité.
{% endalert %}

## Méthodes d'analyse de la carte
Tous les objets du modèle de données `Card` offrent les méthodes d'analyse suivantes pour la journalisation des événements utilisateur sur les serveurs de Braze.

| Méthode                      | Libellé                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `logImpression()`            | Journalisez manuellement une impression à Braze pour une carte particulière.                                                                                       |
| `logClick()`                 | Journalisez manuellement un clic sur Braze pour une carte particulière.                                                                                            |
| `format@@0 setIsDismissed()` | Journalisez manuellement un renvoi à Braze pour une carte particulière. Si une carte est déjà marquée comme rejetée, elle ne peut plus être marquée comme rejetée. |
{: .reset-td-br-1 .reset-td-br-2}

[29]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html
[30]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/BannerImageCard.html
[31]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CaptionedImageCard.html
[32]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/TextAnnouncementCard.html
[41]: https://github.com/Appboy/android-sdk/blob/9a091979b4cbaff7f935c2cae03043a944c3ab53/android-sdk-base/src/main/java/com/appboy/models/cards/ShortNewsCard.java
[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/ContentCardsFragment.html
