---
nav_title: Emplacements & Géorepérages
article_title: Localisation & Géorepérages pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence couvre la façon d'implémenter des localisations et des géorepérages dans votre application iOS."
Tool:
  - Localisation
---

# Emplacements et géorepérages

Les géofences ne sont disponibles que dans certains paquets Braze. Pour y accéder, veuillez créer un [ticket de support][support] ou parler avec votre Responsable du service client de Braze.

Pour prendre en charge les géorepérages pour iOS:

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.

2. Braze Geofences [doit être activé][1] via le SDK soit implicitement en activant la collection d'emplacements, soit explicitement en activant la collection de géorepéres. Ils ne sont pas activés par défaut.

{% alert important %}
Depuis iOS 14, Geofences ne fonctionne pas de manière fiable pour les utilisateurs qui choisissent de donner leur autorisation de localisation approximative.
{% endalert %}

## Étape 1 : Activer le push en arrière-plan

Pour utiliser pleinement notre stratégie de synchronisation de géorepérage, vous devez avoir [Background Push][6] activé en plus de compléter l'intégration standard de push.

## Étape 2 : Activer les géorepérages

Par défaut, les géorepérages sont activés en fonction de l'activation de la collection automatique de localisation. Vous pouvez activer les géorepérages en utilisant le fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez la sous-entrée booléenne `EnableGeofences` et définissez la valeur à `OUI`. Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

 Vous pouvez également activer les géorepérages au démarrage de l'application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4]. Dans le dictionnaire `appboyOptions` , définissez `ABKEnableGeofencesKey` à `OUI`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"VOTRE API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Étape 3 : Vérifier la poussée d'arrière-plan Braze

Braze synchronise les géorepérages sur les appareils en utilisant les notifications push en arrière-plan. Suivez les instructions [ici][7] pour vous assurer que votre application ne prend aucune action indésirable après avoir reçu les notifications de synchronisation de Braze.

## Étape 4 : Ajouter NSLocationAlwaysUsageDescription à votre Info.plist

Ajoutez la clé `NSLocationAlwaysUsageDescription` et `NSLocationAlwaysAndWhenInUseUsageDescription` à vos `informations. liste` avec une valeur `Chaîne` qui a une description des raisons pour lesquelles votre application a besoin de suivre l'emplacement. Les deux clés sont requises pour iOS 11 et plus. Cette description sera affichée lorsque la localisation du système demande une autorisation et devrait expliquer clairement les avantages du suivi de la localisation à vos utilisateurs.

## Étape 5 : Demander une autorisation à l'utilisateur

La fonctionnalité de géorepérage n'est fonctionnelle que lorsque l'autorisation de localisation `Toujours` est accordée.

Pour demander une autorisation de localisation `Toujours` , utilisez le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Étape 6 : Activer les géorepérages sur le tableau de bord

iOS permet uniquement de stocker jusqu'à 20 géorepérages pour une application donnée. Le produit de Braze Locations utilisera certains de ces 20 emplacements de géorepérage disponibles. Pour éviter des perturbations accidentelles ou indésirables à d'autres fonctionnalités liées à la géolocalisation dans votre application, la géolocalisation doit être activée pour chaque application sur le tableau de bord.

Pour que le produit de Braze fonctionne correctement, vous devez également vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

### Activer les géorepérages à partir de la page des localisations :

![Console de Développeur Appboy]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les géorepérages depuis la page des paramètres:

![Console de Développeur Appboy]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Désactivation des requêtes automatiques de géorepérage

À partir de la version 3.21.3 du SDK d'iOS, vous pouvez désactiver la demande automatique de géorepéres. Vous pouvez le faire en utilisant le fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez la sous-entrée booléenne `DisableAutomaticGeofenceRequests` et définissez la valeur à `OUI`.

 Vous pouvez également désactiver les requêtes automatiques de géorepérage au démarrage de l'application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4]. Dans le dictionnaire `appboyOptions` , définissez `ABKDisableAutomaticGeofenceRequestsKey` à `OUI`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"VOTRE API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Si vous choisissez d'utiliser cette option, vous devrez demander manuellement des géorepérages pour que la fonctionnalité fonctionne.

## Demande manuelle de géorepérages

Lorsque le Braze SDK demande des géorepérages à surveiller depuis le backend, il signale l'emplacement actuel de l'utilisateur et, à son tour, reçoit des géorepérages qui sont déterminés à être optimalement pertinents en fonction de l'emplacement signalé. Pour contrôler l'emplacement que le SDK rapporte pour recevoir les géofences les plus pertinentes, à partir de iOS SDK version 3. 1.3 vous pouvez demander manuellement des géorepérages en fournissant la latitude et la longitude d'un emplacement. Pour ce faire, utilisez le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}

__Remarque :__ Il y a une limite de vitesse d'une mise à jour de géorepérage par session. __Remarque :__ Il est recommandé de désactiver les requêtes automatiques de géorepérage lors de l'utilisation de cette méthode.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/#enabling-automatic-location-tracking
[4]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/#ignoring-brazes-internal-push-notifications
[support]: {{site.baseurl}}/braze_support/

