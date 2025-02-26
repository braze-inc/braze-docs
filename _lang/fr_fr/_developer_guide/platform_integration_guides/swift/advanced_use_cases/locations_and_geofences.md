---
nav_title: Localisations et géorepérages
article_title: Localisations et géorepérages pour iOS
platform: Swift
page_order: 4
description: "Cet article de référence traite de la mise en œuvre des localisations et des géorepérages dans votre SDK Swift pour iOS."
Tool:
  - Location

---

# Fonctions de localisation et de géorepérage

> Cet article traite de la configuration des géorepérages pour votre intégration SDK iOS. Les Géorepérages sont uniquement disponibles dans certains forfaits Braze. Contactez votre gestionnaire de satisfaction client Braze pour commencer.

Le concept de [géorepérage]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences) est au cœur de l'offre d'emplacement/localisation en temps réel de Braze. Une géorepérage est une zone géographique virtuelle, représentée par des coordonnées latitudinales et longitudinales associées à un rayon, formant un cercle autour d’une position générale spécifique.

{% alert important %}
Depuis iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de donner leur autorisation de localisation approximative.
{% endalert %}

## Étape 1 : Activer les notifications push d’arrière-plan

Pour utiliser pleinement notre stratégie de synchronisation des géorepérages, vous devez activer les [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) en plus de réaliser l'intégration des notifications push standard.

## Étape 2 : Activer les services d'emplacement/localisation de Braze
Les services de localisation de Braze [doivent être activés](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) via le SDK. Ils ne sont pas activés par défaut.

## Étape 3 : Activer les géorepérages

Activez les géorepérages en définissant `location.geofencesEnabled` sur `true` dans l'objet `configuration` qui initialise l'instance [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). D'autres options de configuration de `location` sont disponibles [ici.](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)
{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Configuration des géorepérages pour les rapports d'arrière-plan

Par défaut, les géorepérages ne sont surveillés que si votre application est au premier plan, ou si elle dispose de l'autorisation `Always` (qui surveille tous les états de l'application).

Cependant, vous pouvez choisir de surveiller les événements de géorepérage lorsque votre appli est en arrière-plan ou lorsqu'elle dispose de l'autorisation `When In Use` en ajoutant la capacité `Background Mode -> Location updates` à votre projet Xcode et en activant `allowBackgroundGeofenceUpdates`. Cela permet à Braze de prolonger le statut "en cours d'utilisation" de votre application en surveillant en permanence les mises à jour d'emplacement/localisation.

`allowBackgroundGeofenceUpdates` ne fonctionne que lorsque votre application est en arrière-plan. À sa réouverture, les processus d'arrière-plan existants sont mis en pause, ce qui permet de donner la priorité aux processus d'avant-plan.

{% alert important %}
Pour éviter le déchargement de la batterie et la limitation du débit, veillez à configurer `distanceFilter` à une valeur qui répond aux besoins spécifiques de votre app. En définissant une valeur plus élevée pour `distanceFilter`, vous évitez que votre application ne demande trop souvent l'emplacement/localisation de votre utilisateur.
{% endalert %}

## Étape 4 : Vérifier les notifications push en arrière-plan Braze

Braze synchronise les géorepérage vers les appareils à l’aide de notifications push en arrière-plan. Suivez l'article [ignorer les push silencieux]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) pour vous assurer que votre application n'entreprend aucune action indésirable à la réception des notifications de synchronisation de géorepérage de Braze.

## Étape 5 : Ajoutez des chaînes de caractères de description de l'emplacement/localisation à vos Info.plist

Ajoutez la clé `NSLocationAlwaysUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription` ou `NSLocationWhenInUseUsageDescription` à votre `info.plist` avec une valeur `String` qui contient une description de la raison pour laquelle votre application a besoin de suivre la localisation.

Cette description s’affichera lorsque l’invite de localisation du système demandera l’autorisation et devrait expliquer clairement les avantages du suivi de la localisation à vos utilisateurs.

## Étape 6 : Demander l’autorisation de l’utilisateur

Lorsque vous demandez l'autorisation d'un utilisateur, vous pouvez demander l’autorisation [`When In Use`](#when-in-use) ou [`Always`](#always).

### En cours d'utilisation

Pour demander l'autorisation `When In Use`, utilisez la méthode `requestWhenInUseAuthorization()` :

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab OBJECTIF-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### Toujours

Par défaut, `requestAlwaysAuthorization()` n'accorde à votre appli que l'autorisation `When In Use` et demandera à nouveau à votre utilisateur l'autorisation `Always` après un certain temps. Toutefois, vous pouvez choisir d'inviter immédiatement votre utilisateur en appelant d'abord `requestWhenInUseAuthorization()`, puis `requestAlwaysAuthorization()` après avoir reçu votre autorisation `When In Use` initiale.

{% alert important %}
Vous ne pouvez demander immédiatement l'autorisation de `Always` qu'une seule fois.
{% endalert %}

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab OBJECTIF-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## Étape 7 : Activer les géorepérages sur le tableau de bord

iOS autorise le stockage de seulement 20 géorepérages pour une application donnée. Avec les géorepérages activés, Braze utilisera une partie de ces 20 emplacements disponibles. Pour éviter toute perturbation accidentelle ou indésirable d’autres fonctionnalités liées au géorepérage dans votre application, les géorepérages de localisation doivent être activés pour les applications individuelles sur le tableau de bord. Pour que nos services d'emplacement/localisation fonctionnent correctement, vérifiez que votre appli n'utilise pas tous les emplacements de géorepérage disponibles.

Il existe deux façons d'activer les géorepérages pour une app particulière : depuis la page **Emplacements** ou depuis la page **Gérer les paramètres**.

### Activer les géorepérages à partir de la page Localisations

Activez les géorepérages sur la page **Emplacements** du tableau de bord.

1. Sélectionnez **Audience** > **Localisations**.
{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **Emplacements** sous **Engagement.**
{% endalert %}

{:start="2"}
2\. Le nombre d'applis de votre espace de travail pour lesquelles les géorepérages sont actuellement activés s'affiche sous le mappage, par exemple : **0 appli sur 1 avec géorepérages activés**. Cliquez sur ce texte.
3\. Sélectionnez l'appli pour activer les géorepérages. Cliquez sur **Terminé.**
![Les options de géorepérage sur la page des localisations Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les géorepérages à partir de la page Gérer les paramètres

Activez les géorepérages depuis les paramètres de votre appli.

1. Allez dans **Réglages** > **Réglages de l'application**.
{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les géorepérages dans **Gérer les paramètres** > **Paramètres**.
{% endalert %}

{:start="2"}
2\. Sélectionnez l'appli pour laquelle vous souhaitez activer les géorepérages.
3\. Cochez la case **Géorepérages activés**. Cliquez sur **Enregistrer.**

![La case à cocher de géorepérage située sur les pages de paramètres Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Désactiver les requêtes de géorepérage automatique

Vous pouvez désactiver les demandes automatiques de géorepérage dans votre objet `configuration` passé à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Définissez `automaticGeofenceRequests` sur `false`. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Si vous choisissez d’utiliser cette option, vous devrez demander manuellement des géorepérages pour que la fonction fonctionne.

## Demander manuellement des géorepérages

Lorsque le SDK Braze demande aux géorepérages de surveiller depuis le backend, il signale la localisation actuelle de l’utilisateur et reçoit des géorepérages jugées pertinentes de manière optimale en fonction de la localisation envoyée. Il y a une limite du taux d’actualisation de géorepérage par session.

Pour contrôler la localisation que le SDK signale afin de recevoir les géorepérages les plus pertinents, vous pouvez demander manuellement des géorepérages en fournissant la latitude et la longitude d'un emplacement. Il est recommandé de désactiver les demandes automatiques de géorepérage lors de l’utilisation de cette méthode. Pour ce faire, utilisez le code suivant :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

