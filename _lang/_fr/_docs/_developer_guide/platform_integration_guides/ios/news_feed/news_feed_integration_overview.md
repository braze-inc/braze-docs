---
nav_title: Vue d'ensemble de l'intégration des fils d'actualité
article_title: Aperçu de l’intégration des flux d’actualités pour iOS
platform: iOS
page_order: 1
description: "Cet article couvre un aperçu de la façon d'intégrer le fil d'actualité dans votre application iOS."
channel:
  - fil d'actualité
---

# Vue d'ensemble de l'intégration des fils d'actualité

{% alert note %}
Braze recommande que les clients qui utilisent notre outil News Feed passent à notre canal de messagerie de cartes de contenu - il est plus flexible, personnalisable et fiable. Il est également plus facile à trouver et à utiliser dans le produit Braze. Contactez votre responsable de compte Braze pour plus d'informations.
{% endalert %}

Intégrer le contrôleur de vue `ABKNewsFeedViewController` affichera le flux d'actualités de Braze.

Vous avez une grande flexibilité dans la façon dont vous choisissez d'afficher les contrôleurs de vue. Il existe différentes versions des contrôleurs de vue pour accommoder différentes structures de navigation.

> Le fil d'actualité qui est appelé par le comportement par défaut d'un clic de message dans l'application ne respectera aucun délégué que vous avez défini pour le fil d'actualité. Si vous voulez respecter cela, vous devez [définir le délégué sur `ABKInAppMessageUIController`][1] et implémenter la `ABKInAppMessageUIDelegate` méthode déléguée [`onInAppMessageClicked:`][2].

## Options d'intégration du contrôleur de vue flux d'actualités

Le flux de nouvelles peut être intégré avec 2 contextes de contrôleur de vue, soit dans le code, soit via une implémentation de storyboard.

### Contexte de navigation -- ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] ;
[self.navigationController pushViewController:newsFeed animé:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animé: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Pour personnaliser le titre de la barre de navigation, définissez la propriété titre de l'instance `ABKNewsFeedTableViewController` `navigationItem`.
{% endalert %}

### Contexte modal -- ABKFeedViewControllerModalContext

- Utilisé pour présenter le contrôleur de vue dans une vue modale, avec une barre de navigation en haut et un bouton Terminé sur le côté droit de la barre
- Définissez le titre du modal via la propriété intégrée `ABKNewsFeedTableViewController` de l'instance `navigationItem` `title` de la propriété
- Si un délégué __n'est PAS défini__ le bouton Terminé va rejeter la vue modale
- Si un délégué __est réglé__ le bouton Terminé appellera le délégué, et le délégué lui-même sera responsable du rejet de la vue

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animé:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animé: true, completion: nil)
```

{% endtab %}
{% endtabs %}

> L' [application d'échantillon de flux d'actualités][3] contient des exemples de contrôleurs de vue.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#setting-delegates
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#customizing-in-app-message-body-clicks
[3]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
