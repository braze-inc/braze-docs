{% multi_lang_include developer_guide/prerequisites/xamarin.md %} De plus, il sera nécessaire de [configurer les notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Conditions préalables

Voici les versions minimales requises du SDK pour commencer à utiliser les géorepérages :

{% sdk_min_versions xamarin:9.0.0 %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Veuillez ensuite suivre les instructions spécifiques à la plateforme ci-dessous, pour Android ou iOS :

{% tabs %}
{% tab Android %}

### Étape 2 : Ajouter des dépendances

Veuillez ajouter la référence au package NuGet suivante à votre projet :

- `BrazePlatform.BrazeAndroidLocationBinding`

### Étape 3 : Mettez à jour votre AndroidManifest.xml

Veuillez ajouter les autorisations suivantes à votre `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
L'autorisation d'accès à l'emplacement en arrière-plan est nécessaire pour que les géorepérages fonctionnent lorsque l'application est en arrière-plan sur les appareils Android 10+.
{% endalert %}

### Étape 4 : Configurer la collecte de données d'emplacement Braze

Veuillez vous assurer que la collecte des données d’emplacement est activée dans votre configuration Braze. Si vous souhaitez activer les géorepérages sans collecte automatique d’emplacements, veuillez définir les paramètres suivants dans votre `Braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Étape 5 : Demander des autorisations d'emplacement lors de l'exécution

Il est nécessaire de demander l'autorisation d'emplacement à l'utilisateur avant d'enregistrer du géorepérage. Dans votre code C#, veuillez utiliser le modèle suivant :

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

Une fois les autorisations accordées, veuillez initialiser la collecte d’emplacements/localisations Braze :

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Étape 6 : Demander manuellement des mises à jour de géorepérage (facultatif)

Pour demander manuellement des géorepérages pour un emplacement spécifique :

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Les géorepérages ne peuvent être demandés qu’une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Étape 2 : Ajouter des dépendances

Veuillez ajouter la référence au package NuGet suivante à votre projet :

- `Braze.iOS.BrazeLocation`

### Étape 3 : Veuillez configurer l'utilisation de l'emplacement/localisation dans Info.plist

Veuillez ajouter une chaîne de caractères de description d'utilisation pour les services de localisation dans votre `Info.plist`:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple a déprécié `NSLocationAlwaysUsageDescription`. Veuillez utiliser les clés ci-dessus pour iOS 14 et versions ultérieures.
{% endalert %}

### Étape 4 : Activez les géorepérages dans votre configuration Braze.

Dans le code de démarrage de votre application (e.g., `App.xaml.cs`), veuillez configurer Braze avec les géorepérages activés :

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### Étape 5 : Activer les mises à jour de localisation en arrière-plan (facultatif)

Pour surveiller le géorepérage en arrière-plan, veuillez activer le mode arrière-plan **des mises à jour d’emplacement** en ajoutant la configuration suivante à votre `Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Ensuite, dans votre configuration Braze, veuillez définir :

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Veuillez`DistanceFilter`définir une valeur adaptée aux besoins de votre application afin d'éviter une consommation excessive de la batterie.
{% endalert %}

### Étape 6 : Demander l'autorisation pour l'emplacement/la localisation

Veuillez demander`When In Use``Always` l'autorisation à l'utilisateur :

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Sans`Always`autorisation, iOS empêche les services d'emplacement de fonctionner lorsque l'application n'est pas utilisée. Cette mesure est appliquée par le système d'exploitation et ne peut être contournée par le SDK Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
