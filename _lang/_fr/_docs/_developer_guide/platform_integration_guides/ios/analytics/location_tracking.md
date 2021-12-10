---
nav_title: Suivi de la localisation
article_title: Suivi de localisation pour iOS
platform: iOS
page_order: 6
description: "Cet article montre comment configurer le suivi de localisation pour votre application iOS."
Tool:
  - Localisation
---

# Suivi de localisation pour iOS

Par défaut, Braze désactive le suivi d'emplacement. Nous activons le suivi de localisation après que l'application hôte ait choisi de suivre la localisation et obtenu l'autorisation de l'utilisateur. À condition que les utilisateurs aient opté pour le suivi de la localisation, Braze enregistrera un seul emplacement pour chaque utilisateur au démarrage de la session.

{% alert important %}
Afin que le suivi de localisation fonctionne de manière fiable dans iOS 14 pour les utilisateurs qui donnent l'autorisation de localisation approximative, vous devez mettre à jour votre version de SDK à au moins `3. 6.1`.
{% endalert %}

## Activation du suivi de localisation automatique
À partir de Braze iOS SDK `v3.17.0`, le suivi de localisation est désactivé par défaut. Vous pouvez activer le suivi automatique de la localisation en utilisant le fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez la sous-entrée booléenne `EnableAutomaticLocationCollection` et définissez la valeur à `OUI`. Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

 Vous pouvez également activer le suivi automatique de la localisation au démarrage de l'application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4]. Dans le dictionnaire `appboyOptions` , définissez `ABKEnableAutomaticLocationCollectionKey` à `OUI`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"VOTRE API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "VOTRE API-KEY",
                 en:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### Passage des données de localisation à Braze

Les deux méthodes suivantes peuvent être utilisées pour définir manuellement le dernier emplacement connu pour l'utilisateur.

{% tabs %}
{% tab OBJECTIVE-C %}

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

Pour plus d'informations, voir [`ABKUser.h`][5].

[4]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h
