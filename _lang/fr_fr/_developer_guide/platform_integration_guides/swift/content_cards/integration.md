---
nav_title: Intégration
article_title: Intégration de la carte de contenu pour iOS
platform: Swift
page_order: 0
description: "Cet article aborde les étapes d'intégration, les modèles de données et les propriétés spécifiques aux cartes disponibles dans le SDK Swift."
channel:
  - content cards

---

# Intégration d’une carte de contenu

> Cet article de référence traite de l'intégration de la carte de contenu et des différents modèles de données et propriétés spécifiques à la carte disponibles pour votre application Swift. Lorsque vous êtes prêt à vous lancer dans la mise en œuvre et la personnalisation, consultez le [Guide de personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

## À propos de l'intégration

L'interface utilisateur par défaut des cartes de contenu peut être intégrée à partir de la bibliothèque `BrazeUI` du SDK Braze. Créez le contrôleur de vue des cartes de contenu en utilisant l'instance `braze`. Si vous souhaitez intercepter le cycle de vie de l'interface utilisateur de la carte de contenu et y réagir, implémentez [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) en tant que délégué pour votre `BrazeContentCardUI.ViewController`.

{% alert note %}
Pour plus d'informations sur les options du contrôleur de vue iOS, reportez-vous à la [documentation du développeur Apple](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

La bibliothèque `BrazeUI` du SDK Swift propose deux contextes de contrôleur de vue par défaut : navigation ou fenêtre modale. Cela signifie que vous pouvez intégrer les cartes contenu dans ces contextes en ajoutant quelques lignes de code à votre app ou site. Les deux vues offrent des options de personnalisation et de style décrites dans le [guide de personnalisation]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). Vous pouvez également créer un contrôleur de vue de cartes de contenu personnalisé au lieu d'utiliser le contrôleur de vue standard de Braze pour bénéficier d'encore plus d'options de personnalisation. Reportez-vous au [tutoriel sur l'interface utilisateur des cartes de contenu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) pour voir un exemple.

{% alert important %}
Pour gérer la variante de contrôle des cartes de contenu dans votre interface utilisateur personnalisée, transmettez votre objet [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de carte de contenu. L'objet enregistrera implicitement une impression de contrôle pour informer notre analyse/analytique du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}

## Contexte de navigation

Un contrôleur de navigation est un contrôleur de vue qui gère un ou plusieurs contrôleurs de vue enfant dans une interface de navigation. Voici un exemple d'introduction d'une instance de `BrazeContentCardUI.ViewController` dans un contrôleur de navigation :

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

## Contexte modal

Utilisez les présentations modales pour créer des interruptions temporaires dans le flux de travail de votre application, par exemple en demandant à l'utilisateur de fournir des informations importantes. Cette vue modèle comporte une barre de navigation en haut et un bouton **Terminé** sur le côté de la barre. Voici un exemple d'insertion d'une instance de `BrazeContentCard.ViewController` dans un contrôleur modal :

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Pour un exemple d'utilisation des contrôleurs de vue `BrazeUI`, consultez les exemples d'interface utilisateur des cartes de contenu correspondants dans notre [application Exemples.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)

## Modèle de données de cartes de contenu

Le modèle de données des cartes de contenu est disponible dans le module `BrazeKit` du SDK Swift pour iOS.

Braze propose cinq types de cartes de contenu : image seule, image légendée, classique, image classique et contrôle. Chaque type est une implémentation du type `Braze.ContentCard`. Notez que `BrazeKit` propose une classe [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) alternative pour la compatibilité avec Objective-C.

Pour obtenir une liste complète des propriétés des cartes de contenu, ainsi que des détails sur l'utilisation des cartes de contenu, reportez-vous à la [documentation de classe `ContentCard`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

Pour accéder au modèle de données des cartes de contenu, appelez `contentCards.cards` sur votre instance `braze`. Voir [Enregistrer les analyses]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) pour plus d'informations sur l’abonnement aux données de cartes.

## Méthodes de carte

Chaque carte est initialisée avec un objet `Context`, qui contient diverses méthodes pour gérer l'état de votre carte. Appelez ces méthodes lorsque vous souhaitez modifier la propriété d'état correspondante d'un objet de carte particulier.

| Méthode                               | Description                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Enregistrez l'événement d'impression de la carte de contenu.                                                                                                   |
| `card.context?.logClick()`           | Enregistrez l'événement de clic sur la carte de contenu.                                                                                                        |
| `card.context?.processClickAction()` | Traiter une entrée [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) donnée. |
| `card.context?.logDismissed()`       | Enregistrer l'événement de carte de contenu rejetée.                                                                                                    |
| `card.context?.logError()`           | Enregistrer une erreur liée à la carte de contenu.                                                                                                |
| `card.context?.loadImage()`          | Charger une image de carte de contenu donnée à partir d'une URL. Cette méthode peut être nulle si la carte de contenu n'a pas d'image.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus de détails, reportez-vous à la [documentation de la classe`Context`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)

{% alert important %}
Par défaut, le SDK Swift ne prend pas en charge les GIF animés. La prise en charge peut être ajoutée en enveloppant une vue tierce ou votre propre vue dans une instance de `GIFViewProvider`.

Pour plus d’informations sur la prise en charge des GIF, reportez-vous à ce [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}
