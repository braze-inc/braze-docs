---
nav_title: Localisations et geofences
article_title: Localisations et geofences pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence explique comment implémenter des positions et des geofences dans votre application iOS."
Outil :
  - Position

---

# Localisations et Geofences

Les geofences sont uniquement disponibles avec certains forfaits Braze. Pour y accéder, créez un [ticket d’assistance][support] ou parlez avec votre gestionnaire du succès des clients Braze.

Pour prendre en charge les geofences pour iOS :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les Geofences Braze [doivent être activés][1] par le biais du SDK, soit implicitement en activant la collecte de sites, soit explicitement en activant la collecte geofence. Ils ne sont pas activés par défaut.

{% alert important %}
Depuis iOS 14, les geofences ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de donner leur autorisation de localisation approximative.
{% endalert %}

## Étape 1 : Activer les notifications push d’arrière-plan

Pour utiliser pleinement notre stratégie de synchronisation de geofence, vous devez avoir activer les [notifications push en arrière-plan][6] en plus de l’intégration des notifications push standard.

## Étape 2 : Activer les geofences

Par défaut, les geofences sont activées en fonction de l’activation ou non de la collecte automatique des emplacements. Vous pouvez activer les geofences en utilisant le fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `EnableGeofences` et réglez la valeur sur `YES`. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également activer les geofences au démarrage de l’application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4]. Dans le dictionnaire `appboyOptions`, paramétrez `ABKEnableGeofencesKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Étape 3 : Vérifier les notifications push en arrière-plan Braze

Braze synchronise les geofence vers les périphériques à l’aide de notifications push en arrière-plan. Suivez l’article sur la [Personnalisation iOS][7] pour s’assurer que votre application ne prend pas de mesures indésirables sur la réception des notifications de synchronisation geofence de Braze.

## Étape 4 : Ajoutez NSLocationAlwaysUsageDescription à votre Info.plist

Ajoutez les clés `NSLocationAlwaysUsageDescription` et `NSLocationAlwaysAndWhenInUseUsageDescription` à votre `info.plist` avec une valeur `String` qui a une description de la raison pour laquelle votre demande doit suivre la localisation. Les deux clés sont requises par iOS 11 ou version ultérieure.
Cette description s’affichera lorsque l’invite de localisation du système demandera l’autorisation et devrait expliquer clairement les avantages du suivi de la localisation à vos utilisateurs.

## Étape 5 : Demander l’autorisation de l’utilisateur

La fonctionnalité Geofences est uniquement fonctionnelle quand l’autorisation de localisation `Always` est accordée.

Pour demander l’autorisation de localisation `Always`, utilisez le code suivant :

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

## Étape 6 : Activer les geofences sur le tableau de bord

iOS autorise le stockage de seulement 20 geofences pour une application donnée. Le produit de localisation de Braze utilisera certains de ces 20 emplacements geofence disponibles. Pour éviter toute perturbation accidentelle ou indésirable d’autres fonctionnalités liées au geofence dans votre application, ceux de position doivent être activés pour les applications individuelles sur le tableau de bord.

Pour que le produit de position de Braze fonctionne correctement, vous devez également vous assurer que votre application n’utilise pas tous les emplacements de geofence disponibles.

### Activer les geofences à partir de la page des positions

![Les options de geofence sur la page des positions Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les geofences à partir de la page des paramètres :

![La case à cocher de geofence située sur les pages de paramètres Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Désactiver les requêtes de geofence automatique

À partir de la version 3.21.3 du SDK iOS, vous pouvez désactiver les geofences d’être automatiquement demandées. Vous pouvez le faire en utilisant le fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `DisableAutomaticGeofenceRequests` et réglez la valeur sur `YES`.

Vous pouvez également désactiver les demandes automatiques geofence au démarrage de l’application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][4]. Dans le dictionnaire `appboyOptions`, paramétrez `ABKDisableAutomaticGeofenceRequestsKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Si vous choisissez d’utiliser cette option, vous devrez demander manuellement des geofences pour que la fonction fonctionne.

## Demander manuellement des geofences

Lorsque le SDK Braze demande aux geofences de surveiller depuis le backend, il signale la localisation actuelle de l’utilisateur et reçoit des geofences jugées pertinentes de manière optimale en fonction de la localisation envoyée. Il y a une limite du taux d’actualisation de geofence par session.

Pour contrôler l’emplacement signalé par le SDK afin de recevoir les geofences les plus pertinentes, à partir de la version 3.21.3 du SDK iOS, vous pouvez demander manuellement des geofences en fournissant la latitude et la longitude d’une localisation. Il est recommandé de désactiver les demandes automatiques de geofence lors de l’utilisation de cette méthode. Pour ce faire, utilisez le code suivant :

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

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking
[4]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/ignoring_internal_push/
[support]: {{site.baseurl}}/braze_support/

