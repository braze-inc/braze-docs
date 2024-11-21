---
nav_title: Contrôleur de visualisation personnalisée
article_title: Message in-app dans un contrôleur de visualisation personnalisée pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence explique comment tirer parti d’un contrôleur de visualisation personnalisée de messagerie in-app pour votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Afficher les messages in-app dans un contrôleur de visualisation personnalisée

Les messages in-app peuvent également être affichés dans un contrôleur de visualisation personnalisée, que vous transmettez à Braze. Braze animera le message personnalisé dans et hors de l’application et traitera l'analyse du message in-app. Le contrôleur de visualisation doit répondre aux exigences suivantes :

- Il doit s’agir d’une sous-classe ou d’une instance de `ABKInAppMessageViewController`.
- La vue du contrôleur de visualisation renvoyé doit être une instance de `ABKInAppMessageView` ou de sa sous-classe.

La méthode suivante de délégation de l’interface utilisateur est appelée chaque fois qu’un message in-app est proposé à `ABKInAppMessageViewController` pour permettre à l’application de transmettre un contrôleur de visualisation personnalisée à Braze pour l’affichage de messages in-app :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Nos [contrôleurs d'envoi de messages in-app](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) sont personnalisables. Vous pouvez utiliser des sous-classes ou des catégories pour personnaliser l’affichage ou le comportement des messages in-app.

## Déclarations de méthode

Pour plus d’informations, voir les fichiers d’en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## Exemples d’implémentation

Voir [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) et [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/) dans l'exemple d’application de messages in-app.

