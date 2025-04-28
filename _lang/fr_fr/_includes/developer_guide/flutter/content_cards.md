## À propos des cartes de contenu de Flutter

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de vous lancer dans les cartes de contenu. Pour afficher le flux de carte, vous pouvez utiliser la méthode `braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze traitera tous les suivis, les masquages et le rendu des cartes de contenu d’un utilisateur.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Méthodes de carte

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application en utilisant les méthodes suivantes disponibles sur l'[interface publique du plugin](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Méthode                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Demande les dernières cartes de contenu au serveur Braze SDK.                                           |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l’objet de carte de contenu donné.                                                            |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l’objet de carte de contenu donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un abandon pour l’objet de carte de contenu donné.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Réception des données de cartes de contenu

Pour recevoir des données de cartes de contenu dans votre application Flutter, le `BrazePlugin` prend en charge l'envoi de données de cartes de contenu à l’aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

L’[objet](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `description`, `title`, `image`, `url`, `extras` et plus encore.

### Étape 1 : Écoutez les données de la carte de contenu dans la couche Dart

Pour recevoir les données de cartes de contenu dans la couche Dart, utilisez le code ci-dessous pour créer un `StreamSubscription` et appeler `braze.subscribeToContentCards()`. N’oubliez pas de `cancel()` l’abonnement au flux lorsqu’il n’est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans notre exemple d'application.

### Étape 2 : Transférer les données de la carte de contenu depuis la couche native

Pour recevoir les données dans la couche Dart à partir de l'étape 1, ajoutez le code suivant pour transférer les données de la carte de contenu des couches natives.

{% tabs %}
{% tab Android %}

Les données de la carte de contenu sont automatiquement transférées depuis la couche Android.

{% endtab %}
{% tab iOS %}

1. Implémentez `contentCards.subscribeToUpdates` pour vous abonner aux mises à jour des cartes de contenu comme décrit dans la documentation [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)).

2. Votre implémentation de fonction de rappel `contentCards.subscribeToUpdates` doit appeler `BrazePlugin.processContentCards(contentCards)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d'application.

{% endtab %}
{% endtabs %}

#### Rejouer la fonction de rappel pour les cartes de contenu

Pour enregistrer n’importe quelle carte de contenu déclenchée avant que la fonction de rappel soit disponible et la rejouer une fois qu’elle est définie, ajoutez l’entrée suivante à la map `customConfigs` lors de l’initialisation du `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
