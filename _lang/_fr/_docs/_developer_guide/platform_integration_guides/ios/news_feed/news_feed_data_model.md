---
nav_title: Modèle de données du flux d'actualités
article_title: Modèle de données du flux d'actualité pour iOS
platform: iOS
page_order: 6
description: "Cet article couvre le modèle de données iOS News Feed, les différents types de cartes et les différentes propriétés spécifiques à la carte disponibles."
channel:
  - fil d'actualité
---

# Modèle de données du flux d'actualités

## Récupération des données

Pour accéder au modèle de données du flux d'actualités, abonnez-vous aux événements de mise à jour du flux d'actualités :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// S'abonner aux mises à jour du flux
// Note: vous devriez supprimer l'observateur le cas échéant
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```

```objc
// Appelé lorsque le flux est actualisé (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification. serInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // vérifie le succès
  // récupère les cartes en utilisant [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// S'abonner aux mises à jour du flux
// Note: vous devriez supprimer l'observateur le cas échéant
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Appelé lorsque le flux est actualisé (via `requestFeedRefresh`)
privé func feedUpdated(_ notification: Notification) {
  si let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] comme? Bool {
    // vérifie le succès
    // récupère les cartes en utilisant Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
 } }
```

{% endtab %}
{% endtabs %}

Si vous voulez changer les données de la carte après qu'elle ait été envoyée par Braze, Nous vous recommandons de stocker (copier en profondeur) les données de la carte localement, de mettre à jour les données et de vous afficher. Les cartes sont accessibles via [ABKFeedController][44].

## Modèle de carte de base

Braze a cinq types de cartes uniques qui partagent un modèle de base. Chaque type de carte a également des propriétés supplémentaires qui sont spécifiques à chaque carte qui sont énumérées ci-dessous.

## Propriétés du modèle de carte de base

- `idString` (lecture seule) - L'ID de la carte défini par Braze
- `vue` - Cette propriété reflète si la carte est lue ou non lue par l'utilisateur
- `créé` (lecture seule) - La propriété est l'horodatage unix de l'heure de création de la carte à partir du tableau de bord Braze
- `mis à jour` (lecture seule) - La propriété est l'horodatage unix de la dernière mise à jour de la carte depuis le tableau de bord de Braze
- `Catégories` - La liste des catégories assignées à la carte, les cartes sans catégorie seront assignées `ABKCardCategoryNoCategory`
- `extras` - Un NSDictionary optionnel de valeurs NSString.

### Catégories

- `La catégorie ABC n'est pas une catégorie`
- `Nouvelles de la catégorie ABK`
- `Annonce de la catégorie ABK`
- `Annonces de la catégorie ABK`
- `ABKCardCategorySocial`
- `Toutes les catégories ABK`

## Propriétés de la bannière
En plus des propriétés de la carte de base :

- `image` (obligatoire) - Cette propriété est l'URL de l'image de la carte
- `URL` (facultatif) - L'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `domain` (facultatif) - Le texte du lien pour l'URL de la propriété, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte, mais est caché dans le flux de nouvelles Braze par défaut.

## Propriétés de l'image sous-titrée
En plus des propriétés de la carte de base :

- `image` (obligatoire) - Cette propriété est l'URL de l'image de la carte
- `title` (requis) - Le texte de titre de la carte
- `description` (obligatoire) - Le corps du texte de la carte
- `URL` (facultatif) - L'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `domain` (facultatif) - Le texte du lien pour la propriété url, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte.

## Propriétés de l'annonce de texte (image sous-titrée sans image)
En plus des propriétés de la carte de base :

- `title` (requis) - Le texte de titre de la carte
- `description` (obligatoire) - Le corps du texte de la carte
- `url` (facultatif) - L'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `domain` (facultatif) - Le texte du lien pour l'URL de la propriété, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte.

## Propriétés de la carte classique
En plus des propriétés de la carte de base :

- `image` (obligatoire) - Cette propriété est l'URL de l'image de la carte
- `title` (facultatif) - Le texte du titre de la carte
- `description` (obligatoire) - Le corps du texte de la carte
- `URL` (facultatif) - L'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole
- `domain` (facultatif) - Le texte du lien pour l'URL de la propriété, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte.

## Méthodes de la carte :

- `logCardImpression` - Enregistrer manuellement une impression sur Braze pour une carte particulière.
- `logCardClicked` - log manuel à un clic sur Braze pour une carte particulière. Le SDK ne consigne une carte cliquera que lorsque la carte aura la propriété `url` avec une valeur valide. Toutes les sous-classes de `ABKCard` ont la propriété `url`.

## Affichage du flux de log

Lors de l'affichage du fil d'actualité dans votre propre interface utilisateur, vous pouvez enregistrer manuellement les impressions du flux d'actualité via `- (void)logFeedDisplayed;`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
