---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour React Native
platform: React Natif
page_order: 3
page_type: Référence
description: "Cet article explique comment démarrer avec les cartes de contenu pour les applications natives de React."
channel: cartes de contenu
---

# Cartes de contenu

Les SDK Braze incluent un flux de carte par défaut pour vous aider à démarrer avec les Cartes de Contenu. Pour afficher le flux de cartes, vous pouvez utiliser la méthode `ReactAppboy.launchContentCards()`. Le flux de carte par défaut inclus avec le Braze SDK gère le suivi de toutes les données analytiques, les licenciements et le rendu pour les cartes de contenu d'un utilisateur.

## Personnalisation

Vous pouvez utiliser ces méthodes supplémentaires pour construire un flux de cartes de contenu personnalisé dans votre application :

| Méthode                                        | Libellé                                                                                               |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `ReactAppboy.requestContentCardsRefresh()`     | Demande les dernières Cartes de Contenu au serveur Braze SDK.                                         |
| `ReactAppboy.getContentCards()`                | Récupère les Cartes de Contenu du Braze SDK. Ceci retournera la dernière liste des cartes du serveur. |
| `ReactAppboy.logContentCardsDisplayed()`       | Enregistre un flux de contenu affiché                                                                 |
| `ReactAppboy.logContentCardClicked(cardId)`    | Enregistre un clic sur l'ID de la carte de contenu donnée.                                            |
| `ReactAppboy.logContentCardImpression(cardId)` | Enregistre une impression pour l'ID de la carte de contenu donnée.                                    |
| `ReactAppboy.logContentCardDismissed(cardId)`  | Enregistre un rejet pour l'ID de la carte de contenu donnée.                                          |

{: .reset-td-br-1 .reset-td-br-2}

## Tester l'affichage de l'échantillon de la carte de contenu

Suivez les étapes ci-dessous pour tester un exemple de carte de contenu.

1. Définissez un utilisateur actif dans l'application React en appelant la méthode `ReactAppboy.changeUserId('votre-utilisateur-id')`.
2. Rendez-vous sur **Campagnes** et suivez [ce guide][4] pour créer une nouvelle campagne de **Carte de Contenu**.
3. Écrivez votre campagne de carte de contenu de test et dirigez-vous vers l’onglet **Test**. Ajoutez le même `identifiant utilisateur` que l'utilisateur de test et cliquez sur **Envoyer le test**. Vous devriez pouvoir lancer une carte de contenu sur votre appareil sous peu.

!\[Test de la campagne de la carte de contenu\]\[5\]

Pour plus d'intégrations, suivez les [instructions d'intégration Android][2] ou les instructions d'intégration [iOS][3], selon votre plateforme.

Un exemple d'implémentation de ceci peut être trouvé dans AppboyProject, dans le [React SDK][1].
[5]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"

[1]: https://github.com/Appboy/appboy-react-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
