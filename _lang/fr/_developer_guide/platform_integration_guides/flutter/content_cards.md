---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Flutter
platform: Flutter
page_order: 3
page_type: reference
description: "Cet article explique comment se lancer dans les cartes de contenu pour les applications Flutter."
channel: cartes de contenu

---

# Cartes de contenu

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de vous lancer dans les cartes de contenu. Pour afficher le flux de cartes, vous pouvez utiliser la méthode `braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze traitera toutes les analytiques de traçages, d’abandons et de rendu des cartes de contenu d’un utilisateur.

## Personnalisation

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application en utilisant celles disponibles sur le [plug-in d’interface publique][7] :

| Méthode                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Demande les dernières cartes de contenu du serveur SDK Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l’objet de carte de contenu donné.                                                            |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l’objet de carte de contenu donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un abandon pour l’objet de carte de contenu donné.                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Fonction de rappel des données de la carte de contenu

Vous pouvez définir une fonction de rappel dans Dart pour recevoir les données de la carte de contenu Braze dans l’application Flutter hôte.

Pour définir la fonction de rappel, appelez `braze.setBrazeContentCardsCallback()` depuis votre application Flutter avec une fonction qui prend une instance `List<BrazeContentCard>`. L’objet `BrazeContentCard` prend en charge un sous-ensemble de champs disponibles dans les objets du modèle natif, y compris `description`, `title`, `image`, `url`, `extras` et plus encore.

{% tabs %}
{% tab Android %}

Cette fonction de rappel marche sans requérir d’intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Créez un écouteur `NotificationCenter` pour les événements `NSNotification.Name.ABKContentCardsProcessed` décrits dans notre article [Intégration des contrôleurs de vues des cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/#getting-the-data).

2. Votre implémentation de fonction de rappel `NotificationCenter` doit appeler `BrazePlugin.processContentCards(contentCards)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d’application pour en avoir un exemple.

{% endtab %}
{% endtabs %}

### Rejouer la fonction de rappel pour les cartes de contenu

Pour enregistrer une carte de contenu déclenchée avant que la fonction de rappel soit disponible et les rejouer une fois qu’elle est définie, ajoutez l’entrée suivante à la map `customConfigs` lors de l’initialisation de `BrazePlugin` :
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Tester l’affichage de l’exemple de carte de contenu

Suivez ces étapes pour tester un exemple de carte de contenu.

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `braze.changeUserId('your-user-id')`.
2. Rendez-vous dans **Campaigns** et suivez [ce guide][3] pour créer une nouvelle campagne de carte de contenu.
3. Composez votre campagne de carte de contenu et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Send Test (Envoyer un test)**.
4. Appuyez sur la notification push qui devrait lancer une carte de contenu sur votre appareil. Il se peut que vous deviez actualiser votre flux pour qu’elle s’affiche.

![Une campagne de carte de contenu Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre carte de contenu.][4]

Pour plus de détails sur chaque plateforme, suivez les guides [Intégration Android][5] ou [Intégration iOS][6].


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[4]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
