{% alert important %}
Depuis iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de ne donner que l'autorisation de leur emplacement/localisation approximatif.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Mise en place de géorepérages {#setting-up-geofences}

### Étape 1 : Activer en Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Activez les services d'emplacement/localisation de votre application.

Par défaut, les services d'emplacement/localisation de Braze ne sont pas activés. Pour les activer dans votre application, suivez les étapes suivantes. Pour un tutoriel étape par étape, voir [Tutorial : Emplacements de Braze et géorepérages](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Étape 2.1 : Ajoutez le module `BrazeLocation` 

Dans Xcode, ouvrez l'onglet **Général**. Sous **Frameworks, Libraries, and Embedded Content**, ajoutez le module `BrazeLocation`.

![Ajoutez le module BrazeLocation dans votre projet Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Étape 2.2 : Mettez à jour votre `Info.plist`

Dans votre site `info.plist`, attribuez une valeur `String` à l'une des clés suivantes qui décrit la raison pour laquelle votre application a besoin de suivre l'emplacement/localisation. Cette chaîne de caractères s'affichera lorsque vos utilisateurs seront invités à utiliser les services d'emplacement/localisation. Veillez donc à expliquer clairement la valeur de l'activation de cette fonctionnalité pour votre application.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist chaînes d'emplacement/localisation dans Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple a supprimé `NSLocationAlwaysUsageDescription`. Pour plus d'informations, consultez [la documentation d'Apple destinée aux développeurs](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Étape 3 : Activez les géorepérages dans votre code

Dans le code de votre application, activez les géorepérages en définissant `location.geofencesEnabled` sur `true` dans l'objet `configuration` qui initialise l' [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) instance. Pour connaître les autres options de configuration de `location`, consultez la [référence du SDK Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

#### Étape 3.1 : Activer les rapports d'arrière-plan (facultatif)

Par défaut, les événements de géorepérage ne sont surveillés que si votre application est au premier plan ou si elle dispose de l'autorisation `Always`, qui surveille tous les états de l'application.

Toutefois, vous pouvez choisir de surveiller également les événements de géorepérage si votre app est en arrière-plan ou dispose d'une [autorisation`When In Use` ](#swift_request-authorization). 

Pour surveiller ces événements de géorepérage supplémentaires, ouvrez votre projet Xcode, puis allez sur **Signing & Capabilities**. Sous **Modes d'arrière-plan**, cochez **Mise à jour de l'emplacement/localisation**.

![Dans Xcode, Mode arrière-plan > Mises à jour des emplacements.]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Ensuite, activez `allowBackgroundGeofenceUpdates` dans le code de votre application. Cela permet à Braze de prolonger le statut " En cours d'utilisation " de votre application en surveillant en permanence les mises à jour d'emplacement/localisation. Ce paramètre ne fonctionne que lorsque votre application est en arrière-plan. À la réouverture de l'application, tous les processus d'arrière-plan existants sont mis en pause et les processus d'avant-plan sont prioritaires.

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
Pour éviter le déchargement de la batterie et la limite de débit, configurez `distanceFilter` à une valeur qui répond aux besoins spécifiques de votre app. En définissant une valeur plus élevée pour `distanceFilter`, vous évitez que votre application ne demande trop souvent l'emplacement/localisation de votre utilisateur.
{% endalert %}

### Étape 4 : Demande d'autorisation {#request-authorization}

Lorsque vous demandez l'autorisation à un utilisateur, demandez l'autorisation `When In Use` ou `Always`.

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

Toutefois, vous pouvez choisir d'inviter immédiatement votre utilisateur en appelant d'abord `requestWhenInUseAuthorization()`, puis `requestAlwaysAuthorization()` après avoir reçu votre autorisation initiale `When In Use`.

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

### Étape 5 : Vérifier la poussée de fond

Braze synchronise les géorepérage vers les appareils à l’aide de notifications push en arrière-plan. Suivez ces instructions pour [configurer les notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) afin que les mises à jour de géorepérage du serveur soient correctement traitées.

{% alert note %}
Pour vous assurer que votre application n'entreprend aucune action indésirable lors de la réception de notifications de synchronisation de géorepérage de Braze, suivez l'article [ignorer les push silencieux]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Demander manuellement des géorepérages {#manually-request-geofences}

Lorsque le SDK de Braze demande des géorepérages au backend, il signale l'emplacement actuel de l'utilisateur et reçoit des géorepérages dont la pertinence est déterminée de manière optimale en fonction de l'emplacement signalé.

Pour contrôler l'emplacement/localisation que le SDK signale afin de recevoir les géorepérages les plus pertinents, vous pouvez demander manuellement des géorepérages en fournissant les emplacements souhaités.

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

### Étape 2 : Appeler `requestGeofences` manuellement

Dans votre code, demandez des géorepérages avec la latitude et la longitude appropriées.

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

Pour confirmer si les géorepérages sont reçus ou non sur votre appareil, utilisez d'abord l' [outil SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) pour vérifier les journaux du SDK. Vous pourrez alors voir si les géorepérages sont reçus avec succès du serveur et s'il y a des erreurs notables.

Vous trouverez ci-dessous d'autres raisons possibles pour lesquelles les géorepérages ne sont pas reçus sur votre appareil :

##### Limites du système d'exploitation iOS

Le système d'exploitation iOS ne permet de stocker que 20 géorepérages au maximum pour une app donnée. Avec les géorepérages activés, Braze utilisera une partie de ces 20 emplacements disponibles.

Pour éviter toute perturbation accidentelle ou indésirable d'autres fonctionnalités liées à la géorepérage dans votre app, vous devez activer les géorepérages d'emplacement/localisation pour les apps individuelles sur le tableau de bord. Pour que nos services d'emplacement/localisation fonctionnent correctement, vérifiez que votre appli n'utilise pas tous les emplacements de géorepérage disponibles.

##### Limitation du taux

Braze a une limite de 1 actualisation de géorepérage par session pour éviter les demandes inutiles.

#### Comment cela fonctionne-t-il si j'utilise à la fois des fonctionnalités de géorepérage Braze et non Braze ?

Comme indiqué plus haut, iOS permet à une même app de stocker un maximum de 20 géorepérages. Ce stockage est partagé par les géorepérages Braze et non Braze et est géré par [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Par instance, si votre application contient 20 géorepérages non Braze, il n'y aura pas de stockage pour suivre les géorepérages Braze (ou vice versa). Pour recevoir de nouveaux géorepérages, vous devrez utiliser [les API d'emplacement/localisation d'Apple](https://developer.apple.com/documentation/corelocation) pour arrêter le suivi de certains géorepérages existants sur l'appareil.

#### La fonctionnalité de géorepérage peut-elle être utilisée lorsqu'un appareil est hors ligne ?

Un appareil ne doit être connecté à l'internet que lorsqu'il est actualisé. Une fois qu'il a réussi à recevoir des géofences du serveur, il est possible d'enregistrer une entrée ou une sortie de géorepérage, même si l'appareil est hors ligne. En effet, l'emplacement/localisation d'un appareil fonctionne séparément de sa connectivité internet.

Par exemple, supposons qu'un appareil ait reçu et enregistré avec succès des géorepérages au début de la session et qu'il se mette hors ligne. S'il pénètre ensuite dans l'un de ces géorepérages enregistrés, il peut déclencher une campagne Braze.

#### Pourquoi les géorepérages ne sont-ils pas surveillés lorsque mon application est en arrière-plan/terminée ?

Sans l'autorisation de `Always`, Apple empêche les services d'emplacement/localisation de fonctionner lorsqu'une application n'est pas utilisée. Cette règle est appliquée par le système d'exploitation et échappe au contrôle du SDK de Braze. Bien que Braze propose des configurations distinctes pour exécuter des services lorsque l'app est en arrière-plan, il n'y a aucun moyen de contourner ces restrictions pour les apps qui sont terminées sans avoir reçu l'autorisation explicite de l'utilisateur.