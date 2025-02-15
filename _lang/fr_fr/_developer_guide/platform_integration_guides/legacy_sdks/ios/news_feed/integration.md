---
nav_title: Intégration
article_title: Intégration du fil d’actualité pour iOS
platform: iOS
page_order: 0
description: "Cet article couvre une vue d’ensemble du modèle de données du fil d’actualités, l’intégration du fil d’actualités dans votre application iOS et un exemple d’intégration de contrôleur de visualisation personnalisée."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration du fil d’actualité

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Modèle de données de fil d’actualités

### Obtenir les données

Pour accéder au modèle de données de fil d’actualités, abonnez-vous aux événements de mise à jour du fil d’actualités :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Si vous souhaitez modifier les données de la carte après qu’elles aient été envoyées par Braze, nous vous recommandons de stocker localement (copie complète) les données de la carte, de les mettre à jour et de les afficher vous-même. Les cartes sont accessibles via [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "le contrôleur d'alimentation abk").

## Modèle de fil d’actualités

Braze propose cinq types de cartes uniques : image de bannière, image sous-titrée, annonce textuelle et classique. Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de base

|Propriété|Description|
|---|---|
| `idString` | (Lecture seule) L’ID de la carte est défini par Braze. |
| `viewed` | Cette propriété reflète si la carte est lue ou non lue par l’utilisateur. |
| `created` | (Lecture seule) La propriété est l’horodatage Unix du temps de création de la carte depuis le tableau de bord de Braze. |
| `updated` | (Lecture seule) La propriété est l’horodatage Unix du dernier temps de mise à jour de la carte depuis le tableau de bord de Braze. |
| `categories` | La liste des catégories attribuées à la carte, les cartes sans catégorie seront attribuées `ABKCardCategoryNoCategory`.<br><br>Catégories disponibles :<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | Un `NSDictionary` facultatif de valeurs `NSString`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte image de bannière

|Propriété|Description|
|---|---|
| `image` | (Obligatoire) Cette propriété est l’URL de l’image de la carte. |
| `URL` | (Facultatif) L’URL qui s’ouvrira après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP(S) ou d’une URL de protocole. |
| `domain` | (Facultatif) Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action et la direction de cliquer sur la carte, mais est masqué dans le fil d’actualité de Braze par défaut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de carte image sous-titrée

|Propriété|Description|
|---|---|
| `image` | (Obligatoire) Cette propriété est l’URL de l’image de la carte. |
| `title` | (Obligatoire) Le texte du titre de la carte. |
| `description`(Obligatoire) Le texte du corps de la carte. |
| `URL` | (Facultatif) L’URL qui s’ouvrira après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP(S) ou d’une URL de protocole. |
| `domain` | (Facultatif) Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte d’annonce textuelle (image sous-titrée sans image)

|Propriété|Description|
|---|---|
| `title` | (Obligatoire) Le texte du titre de la carte. |
| `description` | (Obligatoire) Le texte du corps de la carte. |
| `url` | (Facultatif) L’URL qui s’ouvrira après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP(S) ou d’une URL de protocole. |
| `domain` | (Facultatif) Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte classique

|Propriété|Description|
|---|---|
| `image` | (Obligatoire) Cette propriété est l’URL de l’image de la carte. |
| `title` | (Facultatif) Le texte du titre de la carte. |
| `description` | (Obligatoire) Le texte du corps de la carte. |
| `URL` | (Facultatif) L’URL qui s’ouvrira après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP(S) ou d’une URL de protocole. |
| `domain` | (Facultatif) Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de carte

|Méthode|Description|
|---|---|
| `logCardImpression` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
| `logCardClicked` | Enregistrer manuellement un clic sur Braze pour une carte particulière. Le SDK ne journalisera une carte que lorsque la carte aura la propriété `url` avec une valeur valide. Toutes les sous-classes de `ABKCard` ont la propriété `url`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Affichage du flux de fil d’actualité

Lorsque vous affichez le fil d’actualités dans votre propre interface utilisateur, vous pouvez enregistrer manuellement les impressions du fil d’actualités via `- (void)logFeedDisplayed;`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

## Intégration du contrôleur de visualisation du fil d’actualités

Intégrer le contrôleur de visualisation `ABKNewsFeedViewController` affichera le fil d’actualité Braze.

Vous disposez d’une grande flexibilité dans la manière dont vous choisissez d’afficher les contrôleurs de vue. Il existe différentes versions des contrôleurs de vue permettant de s’adapter aux différentes structures de navigation.

{% alert note %}
Le fil d’actualités appelé par le comportement par défaut d’un clic sur un message in-app ne respectera aucun des délégués que vous avez définis pour le fil d’actualités. Si vous souhaitez respecter cela, vous devez [définir le délégué sur `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) et implémenter la méthode du délégué `ABKInAppMessageUIDelegate` [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks).
{% endalert %}

Le fil d’actualité peut être intégré à deux contextes de contrôleur de visualisation : navigation ou modal.

### Contexte de navigation - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIF-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

Pour personnaliser la barre de navigation `title`, définissez la propriété de titre de l’instance `ABKNewsFeedTableViewController` `navigationItem`.

### Contexte modal - ABKFeedViewControllerModalContext

Cette fenêtre modale est utilisée pour présenter le contrôleur de vue dans une vue modale, avec une barre de navigation en haut et un bouton **Terminé** sur le côté droit de la barre. Pour personnaliser le titre du modal, définissez `title`la propriété de l’instance `ABKNewsFeedTableViewController` `navigationItem`. 

Si un délégué **n'est PAS défini**, le bouton **Terminé** fermera la fenêtre modale. Si un délégué **est défini**, le bouton **Terminé** appellera le délégué, et le délégué lui-même sera responsable de la fermeture de la vue.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Pour consulter des exemples de contrôleur, reportez-vous à notre [exemple d’application de fil d’actualités](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample).


