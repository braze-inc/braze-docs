---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Flutter
platform: Flution
page_order: 3
page_type: reference
description: "Cet article explique comment démarrer avec les cartes de contenu pour les applications Flut."
channel: cartes de contenu
---

# Cartes de contenu

Le SDK Braze inclut un flux de carte par défaut pour vous aider à démarrer avec les Cartes de Contenu. Pour afficher le flux de cartes, vous pouvez utiliser la méthode `braze.launchContentCards()`. Le flux de carte par défaut inclus avec le Braze SDK gère le suivi de toutes les données analytiques, les licenciements et le rendu pour les cartes de contenu d'un utilisateur.

## Personnalisation

Vous pouvez utiliser ces méthodes supplémentaires pour construire un flux de cartes de contenu personnalisé dans votre application en utilisant les méthodes suivantes disponibles sur l'interface publique du plugin [][7]:

| Méthode                                       | Libellé                                                                                                             |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `braze.requestContentCardsRefresh()`          | Demande les dernières Cartes de Contenu au serveur Braze SDK.                                                       |
| `braze.logContentCardsDisplayed()`            | Enregistre un flux de contenu affiché Ceci est utile lorsque vous utilisez une interface utilisateur personnalisée. |
| `braze.logContentCardClicked(contentCard)`    | Enregistre un clic pour l'objet Carte de contenu donné.                                                             |
| `braze.logContentCardImpression(contentCard)` | Enregistre une impression pour l'objet Carte de contenu donné.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Enregistre un rejet pour l'objet de carte de contenu donné.                                                         |
{: .reset-td-br-1 .reset-td-br-2}

## Rappel des données de la carte de contenu

Vous pouvez définir un callback dans Dart pour recevoir les données de la carte de contenu Braze dans l'application hôte Flux.

Pour définir la fonction de rappel, appelez `braze.setBrazeContentCardsCallback()` depuis votre application Flutter avec une fonction qui prend une instance `Liste<BrazeContentCard>`. L'objet `BrazeContentCard` prend en charge un sous-ensemble de champs disponibles dans les objets modèles natifs, y compris `description`, `titre`, `image`, `url`, `extras`, et plus.

{% tabs %}
{% tab Android %}

Ce callback fonctionne sans intégration supplémentaire.

{% endtab %}
{% tab iOS %}

1. Créez un écouteur `NotificationCenter` pour `NSNotification.Name.ABKContentCardsProcessed` comme décrit dans notre [intégration du contrôleur de cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/#getting-the-data) article.

2. Votre implémentation de callback `NotificationCenter` doit appeler `BrazePlugin.processContentCards(contentCards)`.

Pour un exemple, voir [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d'application.

{% endtab %}
{% endtabs %}

### Relecture de la fonction de rappel pour les cartes de contenu

Pour stocker les cartes de contenu déclenchées avant que la fonction de rappel ne soit disponible et les rejouer une fois qu'elle est définie, ajouter l'entrée suivante à la carte `customConfigs` lors de l'intimidation du `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## Tester l'affichage de l'échantillon de la carte de contenu

Suivez les étapes ci-dessous pour tester un exemple de carte de contenu.

1. Définissez un utilisateur actif dans l'application React en appelant la méthode `braze.changeUserId('votre-utilisateur-id')`.
2. Rendez-vous sur **Campagnes** et suivez [ce guide][3] pour créer une nouvelle campagne de **Carte de Contenu**.
3. Écrivez votre campagne de carte de contenu de test et dirigez-vous vers l’onglet **Test**. Ajoutez le même `identifiant utilisateur` que l'utilisateur de test et cliquez sur **Envoyer le test**.
4. Appuyez sur la notification push et cela devrait lancer une carte de contenu sur votre appareil. Vous devrez peut-être actualiser votre flux pour qu'il s'affiche.

!\[Test de la campagne de la carte de contenu\]\[4\]

Pour plus de détails sur chaque plateforme, suivez les guides d'intégration [Android][5] ou [iOS][6].
[4]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
