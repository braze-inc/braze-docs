{% alert important %}
À partir d'iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de n'autoriser que leur emplacement approximatif.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Activez les services de localisation de votre application.

Par défaut, les services de localisation Braze ne sont pas activés. Pour les activer dans votre application, veuillez suivre les étapes suivantes. Pour un tutoriel étape par étape, veuillez consulter [le Tutoriel : Emplacements Braze et géorepérage](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Étape 2.1 : Veuillez ajouter le`BrazeLocation`module

Dans Xcode, veuillez ouvrir l'onglet **Général**. Sous **Frameworks, Libraries, and Embedded Content**, veuillez ajouter le`BrazeLocation`module.

![Veuillez ajouter le module BrazeLocation à votre projet Xcode.]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Étape 2.2 : Mettez à jour votre `Info.plist`

Dans votre `info.plist`, veuillez attribuer une`String`valeur à l'une des clés suivantes qui décrit pourquoi votre application doit suivre les emplacements. Cette chaîne de caractères s'affichera lorsque vos utilisateurs seront invités à activer les services de localisation. Veuillez donc expliquer clairement l'intérêt d'activer cette fonctionnalité pour votre application.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist chaînes de caractères de localisation dans Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple a déprécié `NSLocationAlwaysUsageDescription`. Pour plus d'informations, veuillez consulter [la documentation pour développeurs d'Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Étape 3 : Activez les géorepérages dans votre code.

Dans le code de votre application, veuillez activer les géorepérages en définissant`location.geofencesEnabled`  sur`true`  dans `configuration`l'objet  qui initialise [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)l'instance . Pour d'autres options`location` de configuration, veuillez consulter [la référence Braze Swift SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Étape 3.1 : Activer les rapports en arrière-plan (facultatif)

Par défaut, les événements de géorepérage ne sont surveillés que si votre application est au premier plan ou dispose`Always`d'une autorisation qui surveille tous les états de l'application.

Cependant, vous pouvez également choisir de surveiller les événements de géorepérage si votre application est en arrière-plan ou dispose[`When In Use`](#swift_request-authorization)[d'une autorisation](#swift_request-authorization). 

Pour surveiller ces événements de géorepérage supplémentaires, veuillez ouvrir votre projet Xcode, puis accédez à **Signing&Capabilities**. Sous **Modes d'arrière-plan**, veuillez cocher **Mises à jour de l'emplacement/localisation**.

![Dans Xcode, Mode arrière-plan > Mises à jour d’emplacement]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Ensuite, veuillez activer`allowBackgroundGeofenceUpdates`dans le code de votre application. Cela permet à Braze de prolonger le statut « En cours d'utilisation » de votre application en surveillant en permanence les mises à jour d'emplacement. Ce paramètre ne fonctionne que lorsque votre application est en arrière-plan. Lorsque l'application se rouvre, tous les processus d'arrière-plan existants sont mis en pause et les processus d'avant-plan sont prioritaires.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Afin d'éviter une décharge excessive de la batterie et une limite de débit, veuillez configurer`distanceFilter`  à une valeur qui répond aux besoins spécifiques de votre application. En définissant une valeur plus élevée pour `distanceFilter`, vous évitez que votre application ne demande trop souvent l'emplacement/localisation de votre utilisateur.
{% endalert %}

### Étape 4 : Veuillez demander l'autorisation {#request-authorization}

Lorsque vous sollicitez l'autorisation d'un utilisateur, veuillez demander l'autorisation`When In Use`ou`Always`l'autorisation.

{% tabs local %}
{% tab When In Use %}
Pour demander l'autorisation `When In Use`, utilisez la méthode `requestWhenInUseAuthorization()` :

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
Par défaut, `requestAlwaysAuthorization()` n'accorde à votre appli que l'autorisation `When In Use` et demandera à nouveau à votre utilisateur l'autorisation `Always` après un certain temps.

Cependant, vous pouvez choisir d'interroger immédiatement votre utilisateur en appelant d'abord`requestWhenInUseAuthorization()`  puis en appelant`requestAlwaysAuthorization()`  après avoir reçu votre autorisation `When In Use`initiale .

{% alert important %}
Vous ne pouvez demander immédiatement l'autorisation de `Always` qu'une seule fois.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 5 : Vérifier la mise à jour en arrière-plan

Braze synchronise les géorepérage vers les appareils à l’aide de notifications push en arrière-plan. Veuillez suivre ces instructions pour [configurer les notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) afin que les mises à jour de géorepérage provenant du serveur soient correctement gérées.

{% alert note %}
Afin de garantir que votre application n'effectue aucune action indésirable lors de la réception des notifications de synchronisation de géorepérage Braze, veuillez suivre les instructions fournies dans l'article [sur l'ignorance des notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Demander manuellement des géorepérages {#manually-request-geofences}

Lorsque le SDK Braze demande des géorepérages au backend, il communique l'emplacement actuel de l'utilisateur et reçoit les géorepérages jugés les plus pertinents en fonction de l'emplacement communiqué.

Pour contrôler l'emplacement/localisation que le SDK signale afin de recevoir les géorepérages les plus pertinents, vous pouvez demander manuellement des géorepérages en fournissant les coordonnées souhaitées.

### Étape 1 : Définir `automaticGeofenceRequests` à `false`

Vous pouvez désactiver les demandes automatiques de géorepérage dans votre objet `configuration` passé à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Définissez `automaticGeofenceRequests` sur `false`.

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
{% tab OBJECTIVE-C %}

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

### Étape 2 : Veuillez appeler`requestGeofences`manuellement

Dans votre code, veuillez demander des géorepérages avec la latitude et la longitude appropriées.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

#### Pourquoi ne reçois-je pas les géorepérages sur mon appareil ?

Pour vérifier si les géorepérages sont bien reçus sur votre appareil, veuillez d'abord utiliser l'[outil]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) afin de consulter les journaux du SDK. Vous pourrez alors vérifier si les géorepérages sont correctement reçus depuis le serveur et s'il existe des erreurs notables.

Voici d'autres raisons possibles pour lesquelles les géorepérages peuvent ne pas être reçus sur votre appareil :

##### Limitations du système d'exploitation iOS

Le système d'exploitation iOS ne permet de stocker que 20 géorepérages maximum pour une application donnée. Avec les géorepérages activés, Braze utilisera une partie de ces 20 emplacements disponibles.

Afin d'éviter toute perturbation accidentelle ou indésirable des autres fonctionnalités liées aux géorepérages dans votre application, il est nécessaire d'activer les géorepérages d'emplacement pour chaque application sur le tableau de bord. Pour que nos services d'emplacement/localisation fonctionnent correctement, vérifiez que votre appli n'utilise pas tous les emplacements de géorepérage disponibles.

##### Limitation du taux

Braze impose une limite d'une actualisation du géorepérage par session afin d'éviter les requêtes superflues.

#### Comment cela fonctionne-t-il si j'utilise à la fois les fonctionnalités de géorepérage Braze et non Braze ?

Comme mentionné précédemment, iOS permet à une seule application de stocker un maximum de 20 unités de géorepérage. Cet espace de stockage est partagé entre les géorepérages Braze et non Braze et est géré par [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Par exemple, si votre application contient 20 géorepérages non Braze, il n'y aurait pas de stockage disponible pour suivre les géorepérages Braze (ou vice versa). Afin de recevoir de nouveaux géorepérages, il est nécessaire d'utiliser [les API de localisation d'Apple](https://developer.apple.com/documentation/corelocation) pour désactiver la surveillance de certains géorepérages existants sur l'appareil.

#### La fonctionnalité de géorepérage peut-elle être utilisée lorsqu'un appareil est hors ligne ?

Un appareil doit être connecté à Internet uniquement lorsqu'il est nécessaire d'actualiser. Une fois les géorepérages reçus avec succès depuis le serveur, il est possible d'enregistrer une entrée ou une sortie de géorepérage même si l'appareil est hors ligne. En effet, l'emplacement d'un appareil fonctionne indépendamment de sa connexion Internet.

Par exemple, supposons qu'un appareil ait reçu et enregistré avec succès du géorepérage au début de la session et se déconnecte. Si l'utilisateur pénètre dans l'une de ces zones de géorepérage enregistrées, cela peut déclencher une campagne Braze.

#### Pourquoi les géorepérages ne sont-ils pas surveillés lorsque mon application est en arrière-plan ou fermée ?

Sans`Always`autorisation, Apple limite l'exécution des services de localisation lorsqu'une application n'est pas utilisée. Cette mesure est appliquée par le système d'exploitation et échappe au contrôle du SDK Braze. Bien que Braze propose des configurations distinctes pour exécuter des services lorsque l'application est en arrière-plan, il n'existe aucun moyen de contourner ces restrictions pour les applications qui sont fermées sans l'autorisation explicite de l'utilisateur.