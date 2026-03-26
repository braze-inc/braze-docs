## À propos des cartes de contenu Flutter

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de démarrer avec les cartes de contenu. Pour afficher ce flux, utilisez la méthode `braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze gère l'ensemble du suivi analytique, des masquages et du rendu des cartes de contenu d'un utilisateur.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Méthodes de carte

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application, disponibles sur l'[interface publique du plugin](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart) :

| Méthode                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Demande les dernières cartes de contenu au serveur du SDK Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l'objet de carte de contenu donné.                                                            |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l'objet de carte de contenu donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un masquage pour l'objet de carte de contenu donné.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Réception des données de cartes de contenu

Pour recevoir des données de cartes de contenu dans votre application Flutter, le `BrazePlugin` prend en charge l'envoi de données de cartes de contenu à l'aide de [Dart Streams](https://dart.dev/tutorials/language/streams).

L'[objet](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, notamment `description`, `title`, `image`, `url`, `extras`, et plus encore.

### Écouter les données de cartes de contenu dans la couche Dart

Pour recevoir les données de cartes de contenu dans la couche Dart, utilisez le code ci-dessous pour créer un `StreamSubscription` et appeler `braze.subscribeToContentCards()`. N'oubliez pas d'appeler `cancel()` sur l'abonnement au flux lorsqu'il n'est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Pour un exemple, consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans l'application exemple du SDK Flutter de Braze.

### Transférer les données de cartes de contenu depuis la couche native iOS

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Les données de cartes de contenu sont automatiquement transférées depuis les couches natives Android et iOS. Aucune configuration supplémentaire n'est requise.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Si vous utilisez le SDK Flutter 17.1.0 ou une version antérieure, le transfert des données de cartes de contenu depuis la couche native iOS nécessite une configuration manuelle. Votre application contient probablement un rappel `contentCards.subscribeToUpdates` qui appelle `BrazePlugin.processContentCards(contentCards)`. Pour migrer vers le SDK Flutter 18.0.0, supprimez l'appel à `BrazePlugin.processContentCards(_:)` — le transfert des données est désormais géré automatiquement.

Pour un exemple, consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans l'application exemple du SDK Flutter de Braze.

{% endtab %}
{% endtabs %}

#### Rejouer le rappel pour les cartes de contenu

Pour stocker les cartes de contenu déclenchées avant que le rappel soit disponible et les rejouer une fois celui-ci défini, ajoutez l'entrée suivante à la map `customConfigs` lors de l'initialisation du `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
