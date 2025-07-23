---
nav_title: Localisations et géorepérages
article_title: Localisations et géorepérages pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence explique comment mettre en œuvre des fonctions de localisation et de géorepérage dans votre application iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fonctions de localisation et de géorepérage

Pour prendre en charge les géorepérages pour iOS :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages Braze [doivent être activés]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking) par le biais du SDK, soit implicitement en activant la collecte des données de localisation, soit explicitement en activant la collecte des géorepérages. Ils ne sont pas activés par défaut.

{% alert important %}
Depuis iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de donner leur autorisation de localisation approximative.
{% endalert %}

## Étape 1 : Activer les notifications push d’arrière-plan

Pour utiliser pleinement notre stratégie de synchronisation par géorepérage, vous devez activer le [push en arrière-plan]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work) en plus de réaliser l'intégration push standard.

## Étape 2 : Activer les géorepérages

Par défaut, les géorepérages sont activées en fonction de l’activation ou non de la collecte automatique des emplacements. Vous pouvez activer les géorepérages en utilisant le fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `EnableGeofences` et réglez la valeur sur `YES`. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Vous pouvez également activer les géorepérages au démarrage de l'application à l'aide de la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) méthode. Dans le dictionnaire `appboyOptions`, paramétrez `ABKEnableGeofencesKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

Braze synchronise les géorepérage vers les appareils à l’aide de notifications push en arrière-plan. Suivez l'article de [personnalisation iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) pour vous assurer que votre application ne prend aucune mesure indésirable lors de la réception des notifications de synchronisation de géofence Braze.

## Étape 4 : Ajoutez NSLocationAlwaysUsageDescription à votre Info.plist

Ajoutez les clés `NSLocationAlwaysUsageDescription` et `NSLocationAlwaysAndWhenInUseUsageDescription` à votre `info.plist` avec une valeur `String` qui a une description de la raison pour laquelle votre demande doit suivre la localisation. Les deux clés sont requises par iOS 11 ou version ultérieure.
Cette description s’affichera lorsque l’invite de localisation du système demandera l’autorisation et devrait expliquer clairement les avantages du suivi de la localisation à vos utilisateurs.

## Étape 5 : Demander l’autorisation de l’utilisateur

La fonctionnalité Géorepérages est uniquement fonctionnelle quand l’autorisation de localisation `Always` est accordée.

Pour demander l’autorisation de localisation `Always`, utilisez le code suivant :

{% tabs %}
{% tab OBJECTIF-C %}

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

## Étape 6 : Activer les géorepérages sur le tableau de bord

iOS autorise le stockage de seulement 20 géorepérages pour une application donnée. Les localisations utiliseront certains de ces 20 géorepérages disponibles. Pour éviter toute perturbation accidentelle ou indésirable d’autres fonctionnalités liées au géorepérage dans votre application, les géorepérages de localisation doivent être activés pour les applications individuelles sur le tableau de bord.

Pour que les localisations fonctionnent correctement, vous devez également vérifier que votre application n'utilise pas tous les géorepérages disponibles.

### Activer les géorepérages à partir de la page des localisations

![Les options de géorepérage sur la page des localisations Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les géorepérages à partir de la page des paramètres :

![La case à cocher de géorepérage située sur les pages de paramètres Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Désactiver les requêtes de géorepérage automatique

À partir de la version 3.21.3 du SDK iOS, vous pouvez désactiver les géorepérages d’être automatiquement demandées. Vous pouvez le faire en utilisant le fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `DisableAutomaticGeofenceRequests` et réglez la valeur sur `YES`.

Vous pouvez également désactiver les demandes automatiques de géorepérage au démarrage de l’application via la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Dans le dictionnaire `appboyOptions`, paramétrez `ABKDisableAutomaticGeofenceRequestsKey` sur `YES`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

Si vous choisissez d’utiliser cette option, vous devrez demander manuellement des géorepérages pour que la fonction fonctionne.

## Demander manuellement des géorepérages

Lorsque le SDK Braze demande aux géorepérages de surveiller depuis le backend, il signale la localisation actuelle de l’utilisateur et reçoit des géorepérages jugées pertinentes de manière optimale en fonction de la localisation envoyée. Il y a une limite du taux d’actualisation de géorepérage par session.

Pour contrôler l’emplacement signalé par le SDK afin de recevoir les géorepérages les plus pertinentes, à partir de la version 3.21.3 du SDK iOS, vous pouvez demander manuellement des géorepérages en fournissant la latitude et la longitude d’une localisation. Il est recommandé de désactiver les demandes automatiques de géorepérage lors de l’utilisation de cette méthode. Pour ce faire, utilisez le code suivant :

{% tabs %}
{% tab OBJECTIF-C %}

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


