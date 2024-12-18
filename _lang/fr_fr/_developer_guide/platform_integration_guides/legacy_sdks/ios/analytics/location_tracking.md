---
nav_title: Suivi de localisation
article_title: Suivi de la localisation pour iOS
platform: iOS
page_order: 6
description: "Cet article montre comment configurer la géolocalisation pour votre application iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Suivi de la localisation pour iOS

Par défaut, Braze désactive le suivi de la localisation. Nous autorisons le suivi de la localisation après que l’application hôte a choisi le suivi de la localisation et obtenu l’autorisation de l’utilisateur. Si les utilisateurs ont opté pour le suivi de la localisation, Braze enregistrera une localisation unique pour chaque utilisateur au démarrage de la session.

{% alert important %}
Pour que le suivi de la localisation fonctionne de manière fiable dans iOS 14 pour les utilisateurs ayant octroyé une autorisation de localisation approximative, vous devez mettre à jour votre version SDK vers au moins `3.26.1`.
{% endalert %}

## Activer le suivi automatique de la localisation

À partir du SDK Braze pour iOS `v3.17.0`, le suivi de la localisation est désactivé par défaut. Vous pouvez activer le suivi automatique des localisations à l’aide du fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `EnableAutomaticLocationCollection` et réglez la valeur sur `YES`. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également activer le suivi automatique de l'emplacement au démarrage de l'application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Dans le dictionnaire `appboyOptions`, paramétrez `ABKEnableAutomaticLocationCollectionKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### Transfert des données de localisation vers Braze

Les deux méthodes suivantes peuvent être utilisées pour définir manuellement la dernière localisation connue de l’utilisateur.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, reportez-vous à [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h).

