---
nav_title: Intégration
article_title: Intégration du contrôleur de la vue de carte de contenu pour iOS
platform: iOS
page_order: 1
description: "Cet article couvre les étapes d'intégration, les modèles de données et les propriétés spécifiques à la carte disponibles pour votre application iOS."
channel:
  - cartes de contenu
---

# Intégration du contrôleur de visualisation des cartes de contenu

Les cartes de contenu peuvent être intégrées avec deux contextes de contrôleur de vue: Navigation ou Modal.

## Navigation context

Exemple de poussage d'une instance `ABKContentCardsTableViewController` dans un contrôleur de navigation :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Titre des cartes de contenu";
contentCards.disableUnreadIndicator = OUI;
[self.navigationController pushViewController:contentCards animés:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Titre des Cartes de Contenu"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(Cartes de Contenu: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Pour personnaliser le titre de la barre de navigation, définissez la propriété titre de l'instance `ABKContentCardsTableViewController` `navigationItem`.
{% endalert %}

## Contexte modal

Cette modale est utilisée pour présenter le contrôleur de vue dans une vue modale, avec une barre de navigation en haut et un bouton Terminé sur le côté droit de la barre.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Titre des cartes de contenu";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animés:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animé: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Pour des exemples de ces contrôleurs de vue, consultez notre [application d'échantillon de Cartes de Contenu](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Pour personnaliser l'en-tête, définir la propriété titre de la propriété `navigationItem` appartenant à l'instance `ABKContentCardsTableViewController` intégrée dans l'instance parent `ABKContentCardsViewController`.
{% endalert %}

# Modèle de données des cartes de contenu

Le modèle de données des Cartes de Contenu est disponible dans le SDK iOS.

## Récupération des données

Pour accéder au modèle de données des Cartes de Contenu, abonnez-vous aux événements de mise à jour des Cartes de Contenu:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// S'abonner aux mises à jour des fiches de contenu
// Note: vous devriez supprimer l'observateur le cas échéant
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Appelé lorsque les cartes de contenu sont actualisées (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification. serInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // récupère les cartes en utilisant [[Appboy sharedInstance]. ontentCardsController getContentCards] ;
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// S'abonner aux mises à jour de la fiche de contenu
// Note: vous devriez supprimer l'observateur le cas échéant
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Appelé lorsque les cartes de contenu sont actualisées (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification. serInfo?[ABKContentCardsProcessedIsSuccessfulKey] en tant que ? Bool {
    if (updateIsSuccessful) {
      // récupère les cartes en utilisant Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
 } } }
```
{% endtab %}
{% endtabs %}

Si vous voulez changer les données de la carte après qu'elle ait été envoyée par Braze, Nous vous recommandons de stocker une copie profonde des données de la carte localement, de mettre à jour les données et de vous afficher. Les cartes sont accessibles via [ABKContentCardsController](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Modèle de carte de contenu

Braze offre trois types de cartes de contenu : Bannière, Image sous-titrée et Classique. Chaque type hérite de propriétés communes d'une classe ABKContentCard de base, plus a des propriétés supplémentaires telles que décrites ci-dessous.

### Propriétés du modèle de carte de contenu de base - ABKContentCard

| Modélisation                     | Libellé                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `idString`                       | (lecture seule) L'ID de la carte défini par Braze.                                                                  |
| `consulté`                       | Cette propriété reflète si la carte est vue ou non par l'utilisateur                                                |
| `créé`                           | (lecture seule) Cette propriété est l'horodatage unix de l'heure de création de la carte depuis Braze.              |
| `expiresAt`                      | (lecture seule) Cette propriété est l'horodatage unix de la date d'expiration de la carte.                          |
| `Rejetable`                      | Cette propriété reflète si la carte peut être rejetée par l'utilisateur.                                            |
| `épinglé`                        | Cette propriété reflète si la carte a été configurée comme "épinglée" dans le tableau de bord.                      |
| `rejetée`                        | Cette propriété reflète si la carte a été rejetée par l'utilisateur.                                                |
| `Url`                            | L'URL qui sera ouverte après avoir cliqué sur la carte. Il peut s'agir d'une URL http(s) ou d'une URL de protocole. |
| `Ouvrir l\'URL dans la vue Web` | Cette propriété détermine si l'URL sera ouverte dans l'application ou dans un navigateur web externe.               |
| `extras`                         | Un NSDictionary optionnel des valeurs NSString.                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés du contenu de la bannière - ABKBannerContentCard

| Modélisation       | Libellé                                                       |
| ------------------ | ------------------------------------------------------------- |
| `image`            | Cette propriété est l'URL de l'image de la carte.             |
| `imageAspectRatio` | Cette propriété est le ratio d'aspect de l'image de la carte. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte de contenu d'image sous-titrée - ABKCaptionedImageCard

| Modélisation              | Libellé                                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`                   | Cette propriété est l'URL de l'image de la carte.                                                                                                                             |
| `imageAspectRatio`        | Cette propriété est le ratio d'aspect de l'image de la carte.                                                                                                                 |
| `Titre:`                  | Le texte du titre de la carte.                                                                                                                                                |
| `Description de la carte` | Le corps du texte de la carte.                                                                                                                                                |
| `domaine`                 | Le texte du lien pour l'URL de la propriété, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte de contenu classique - ABKClassicContentCard

| Modélisation              | Libellé                                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`                   | (optionnel) Cette propriété est l'URL de l'image de la carte.                                                                                                                 |
| `Titre:`                  | Le texte du titre de la carte.                                                                                                                                                |
| `Description de la carte` | Le corps du texte de la carte.                                                                                                                                                |
| `domaine`                 | Le texte du lien pour l'URL de la propriété, comme @"blog.braze.com". Il peut être affiché sur l'interface de la carte pour indiquer l'action/direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2}

## Méthodes de carte

| Méthode                           | Libellé                                                                                                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `logContentCardImpression`        | Journalisez manuellement une impression à Braze pour une carte particulière.                                                                                                              |
| `format@@0 logContentCardClicked` | Journalisez manuellement un clic sur Braze pour une carte particulière. Le SDK ne consigne une carte cliquera que lorsque la carte aura la propriété `url` avec une valeur valide.        |
| `logContentCardDismissed`         | Journalisez manuellement un renvoi à Braze pour une carte particulière. Le SDK ne conservera un rejet de carte que si la propriété `rejetée` de la carte n'est pas déjà définie à `true`. |
| `isControlCard`                   | Détermine si une carte est la carte de contrôle pour un test A/B.                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus de détails, consultez la [documentation de référence de classe complète](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)

## Affichage des cartes de contenu du journal

Lors de l'affichage des Cartes de Contenu dans votre propre interface utilisateur, vous pouvez enregistrer manuellement des Cartes de Contenu via la méthode `logContentCardsDisplay;` sur l'interface `Appboy`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logContentCardsDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logContentCardsDisplayed()
```

{% endtab %}
{% endtabs %}
