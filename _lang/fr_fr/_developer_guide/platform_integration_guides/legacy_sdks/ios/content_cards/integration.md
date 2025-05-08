---
nav_title: Intégration
article_title: Intégration de la carte de contenu pour les contrôleurs iOS
platform: iOS
page_order: 1
description: "Cet article de référence couvre les étapes d’intégration, les modèles de données et les propriétés spécifiques à la carte disponibles pour votre application iOS."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration d’une carte de contenu

## Modèle de données de cartes de contenu

Le modèle de données de cartes de contenu est disponible dans le SDK iOS.

### Obtenir les données

Pour accéder au modèle de données des cartes de contenu, abonnez-vous aux événements de mise à jour des cartes de contenu :

{% tabs %}
{% tab OBJECTIF-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Si vous souhaitez modifier les données de la carte après qu’elles aient été envoyées par Braze, nous vous recommandons de stocker localement une copie complète des données de la carte, de mettre les données à jour et de les afficher vous-même. Les cartes sont accessibles via [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Modèle de carte de contenu

Braze propose trois types de cartes de contenu : bannière, image légendée et classique. Chaque type hérite des propriétés communes d’une classe `ABKContentCard` de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de contenu de base : ABKContentCard

|Propriété|Description|
|---|---|
|`idString` | (Lecture seule) L’ID de la carte est défini par Braze. |
| `viewed` | Cette propriété indique si l’utilisateur a vu la carte ou non.|
| `created` | (Lecture seule) Cette propriété est l’horodatage Unix du temps de création de la carte par Braze. |
| `expiresAt` | (Lecture seule) Cette propriété est l’horodatage Unix du temps du délai d’expiration de la carte.|
| `dismissible` | Cette propriété indique si l’utilisateur peut ignorer la carte.|
| `pinned` | Cette propriété reflète si la carte a été définie comme « épinglée » dans le tableau de bord.|
| `dismissed` | Cette propriété reflète si l’utilisateur a rejeté la carte.|
| `url` | L’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP(S) ou d’une URL de protocole.|
| `openURLInWebView` | Cette propriété détermine si l’URL sera ouverte dans l’application ou dans un navigateur Web externe.|
| `extras`| Un `NSDictionary` facultatif de valeurs `NSString`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la Content Card de la bannière - ABKBannerContentCard

|Propriété|Description|
|---|---|
| `image` | Cette propriété est l’URL de l’image de la carte.|
| `imageAspectRatio` | Cette propriété est le rapport hauteur/largeur de l’image de la carte et sert d’indice avant que le chargement d’image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte de contenu de l’image sous-titrée : ABKCaptionedImageCard

|Propriété|Description|
|---|---|
| `image` | Cette propriété est l’URL de l’image de la carte.|
| `imageAspectRatio` | Cette propriété est le rapport hauteur/largeur de l’image de la carte.|
| `title` | Le texte du titre pour la carte.|
| `cardDescription` | Le texte du corps pour la carte.|
| `domain` | Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la Classic Content Card - ABKClassicContentCard

|Propriété|Description|
|---|---|
| `image` | (Facultatif) Cette propriété est l’URL de l’image de la carte.|
| `title` | Le texte du titre pour la carte. |
| `cardDescription` | Le texte du corps pour la carte. |
| `domain` | Le texte du lien pour l’URL de propriété, par exemple @"blog.braze.com". Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action et la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de carte

|Méthode|Description|
|---|---|
| `logContentCardImpression` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
| `logContentCardClicked` | Enregistrer manuellement un clic sur Braze pour une carte particulière. Le SDK ne journalisera une carte que lorsque la carte aura la propriété `url` avec une valeur valide. |
| `logContentCardDismissed` | Enregistrer manuellement un rejet sur Braze pour une carte particulière. Le SDK ne journalisera qu’une fermeture de carte de contenu si la propriété `dismissed` de la carte n’est pas déjà définie sur `true`. |
| `isControlCard` | Déterminez si une carte est la carte de contrôle pour un test A/B. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Reportez-vous à la [documentation de référence de classe](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) pour plus de détails.

## Intégration du contrôleur de visualisation des cartes de contenu

Les cartes de contenu peuvent être intégrées à deux contextes de contrôleur de visualisation : navigation ou modal.

### Contexte de navigation

Exemple de notification push d’une instance `ABKContentCardsTableViewController` dans un contrôleur de navigation :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Pour personnaliser le titre de la barre de navigation, définissez la propriété de titre de `ABKContentCardsTableViewController` l’instance `navigationItem`.
{% endalert %}

### Contexte modal

Cette fenêtre modale est utilisée pour présenter le contrôleur de visualisation dans une vue modale, avec une barre de navigation sur le dessus et un **Terminé** sur le côté de la barre.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Pour des exemples de contrôleurs de vue, consultez notre [exemple d'application Cartes de contenu.](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)

{% alert note %}
Pour personnaliser l’en-tête, définissez la propriété de titre du `navigationItem` appartenant à l’instance `ABKContentCardsTableViewController` intégrée dans l’instance `ABKContentCardsViewController` parente.
{% endalert %}
