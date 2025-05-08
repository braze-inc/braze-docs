---
nav_title: Définir des délégués
article_title: Configuration des délégués de message in-app pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence couvre les délégués de messagerie in-app pour votre application iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Définir des délégués

Les affichages de messages In-app et les personnalisations de livraison peuvent être déterminés dans le code en définissant nos délégués facultatifs.

## Délégué de message in-app

Le délégué [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) peut être utilisé pour recevoir des envois de messages in-app déclenchés en vue d'un traitement ultérieur, pour recevoir des événements liés au cycle de vie de l'affichage et pour contrôler la synchronisation de l'affichage. 

Définissez votre objet délégué `ABKInAppMessageUIDelegate` sur l’instance Braze en utilisant :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

Consultez notre [exemple d'application d'](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) envoi de messages in-app pour un exemple de mise en œuvre. Notez que si vous n’incluez pas la bibliothèque d’interface utilisateur de Braze dans votre projet (peu courant), ce délégué n’est pas disponible.

## Délégué principal de message in-app

Si vous n’incluez pas la bibliothèque d’interface utilisateur de Braze dans votre projet et que vous souhaitez recevoir des charges utiles de messages in-app déclenchés pour un traitement ultérieur ou un affichage personnalisé dans votre application, implémentez le protocole [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/).

Définissez votre objet délégué `ABKInAppMessageControllerDelegate` sur l’instance Braze en utilisant :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Vous pouvez également définir votre délégué principal de message in-app au moment de l’initialisation via `appboyOptions` à l’aide de la clé `ABKInAppMessageControllerDelegateKey` :
{% tabs %}
{% tab OBJECTIF-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Déclarations de méthode

Pour plus d’informations, voir les fichiers d’en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Exemples d’implémentation

Voir [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) dans l'exemple d’application de message in-app.


