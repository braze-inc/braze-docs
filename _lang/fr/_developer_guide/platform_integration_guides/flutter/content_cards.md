---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Flutter
platform: Flutter
page_order: 3
page_type: reference
description: "Cet article explique comment se lancer dans les cartes de contenu pour les applications Flutter."
channel: cartes de contenu

---

# Intégration d’une carte de contenu

> Cet article explique comment paramétrer des cartes de contenu pour votre application Flutter.

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de vous lancer dans les cartes de contenu. Pour afficher le flux de carte, vous pouvez utiliser la méthode `braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze traitera tous les suivis, les masquages et le rendu des cartes de contenu d’un utilisateur.

## Personnalisation

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application en utilisant celles disponibles sur le [plug-in d’interface publique][7] :

| Méthode                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Demande les dernières cartes de contenu au serveur Braze SDK.                                           |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l’objet de carte de contenu donné.                                                            |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l’objet de carte de contenu donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un abandon pour l’objet de carte de contenu donné.                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Réception des données de cartes de contenu

Pour recevoir des données dans la carte de contenu dans votre appli Flutter, le `BrazePlugin` est compatible avec l’envoi de données dans une carte de contenu à l’aide de [Dart Streams](https://dart.dev/tutorials/language/streams) (recommandé) ou en utilisant une fonction de rappel de données (hérité).

L’objet `BrazeContentCard` [](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `description`, `title`, `image`, `url`, `extras` et plus encore.

{% alert note %} La méthode de fonction de rappel de données héritées sera bientôt obsolète. Il est possible d’ajouter des cartes de contenu aux flux de données et aux fonctions de rappel de données. Si vous avez déjà des fonctions de rappel de données intégrées et souhaitez utiliser des flux de données, supprimez toute logique de fonction de rappel pour garantir que les cartes de contenu sont traitées exactement une seule fois. {% endalert %}

### Méthode 1  : Flux de données de cartes de contenus (recommandé)

Vous pouvez définir une fonction d’écouteur de flux de données dans Dart pour recevoir les données des cartes de contenus dans votre application Flutter.

Pour commencer à écouter le flux, utilisez le code ci-dessous pour créer un `StreamSubscription` dans votre appli Flutter et appelez la méthode `subscribeToContentCards()` avec une fonction prenant l’instance `List<BrazeContentCard>`. N’oubliez pas de `cancel()` l’abonnement au flux lorsqu’il n’est plus nécessaire.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = _braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Function to handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Consultez [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) dans votre exemple d’application.

### Méthode 2 : Fonction de rappel des données de la carte de contenu (hérité)

Vous pouvez définir une fonction de rappel dans Dart pour recevoir les données de la carte de contenu Braze dans l’application Flutter hôte.

Pour définir la fonction de rappel, appelez `braze.setBrazeContentCardsCallback()` depuis votre application Flutter avec une fonction qui prend une instance `List<BrazeContentCard>`.

{% tabs %}
{% tab Android %}

Cette fonction de rappel marche sans requérir d’intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Mettre en œuvre `contentCards.subscribeToUpdates` pour s’abonner aux mises à jour des cartes de contenu comme décrit dans la documentation [subscribeToUpdates (S’abonner aux mises à jour)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)).

2. Votre implémentation de fonction de rappel `contentCards.subscribeToUpdates` doit appeler `BrazePlugin.processContentCards(contentCards)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans votre exemple d’application.

{% endtab %}
{% endtabs %}

#### Rejouer la fonction de rappel pour les cartes de contenu

Pour enregistrer quelconque carte de contenu déclenchée avant que la fonction de rappel soit disponible et la rejouer une fois qu’elle est définie, ajoutez l’entrée suivante à la map `customConfigs` lors de l’initialisation de `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Test affichant l’exemple de carte de contenu

Suivez ces étapes pour tester un exemple de carte de contenu.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `braze.changeUserId('your-user-id')`.
2. Accédez à **Campaigns (Campagnes)** et suivez [ce guide][3] pour créer une nouvelle campagne de carte de contenu.
3. Composez votre campagne de carte de contenu et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Send Test (Envoyer le test)**.
4. Appuyez sur la notification push qui devrait lancer une carte de contenu sur votre appareil. Il se peut que vous deviez actualiser votre flux pour qu’elle s’affiche.

![Une campagne de carte de contenu Braze indiquant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour tester votre carte de contenu.][4]

Pour plus de détails sur chaque plateforme, suivez les guides [Intégration Android][5] ou [Intégration iOS][6].


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[4]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[6]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
