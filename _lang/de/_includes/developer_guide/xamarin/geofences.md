{% multi_lang_include developer_guide/prerequisites/xamarin.md %} Darüber hinaus müssen Sie [stille Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Voraussetzungen

Dies sind die Mindestversionen des SDK, die erforderlich sind, um Geofences zu verwenden:

{% sdk_min_versions xamarin:9.0.0 %}

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Befolgen Sie anschließend die unten aufgeführten plattformspezifischen Anweisungen für Android oder iOS:

{% tabs %}
{% tab Android %}

### Schritt 2: Abhängigkeiten hinzufügen

Fügen Sie die folgende NuGet-Paket-Referenz zu Ihrem Projekt hinzu:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Schritt 3: Aktualisieren Sie Ihr AndroidManifest.xml

Fügen Sie die folgenden Berechtigungen zu Ihrer Datei `AndroidManifest.xml`hinzu:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Die Berechtigung für den Zugriff auf den Standort im Hintergrund ist erforderlich, damit Geofences funktionieren, während sich die App auf Android 10+-Geräten im Hintergrund befindet.
{% endalert %}

### Schritt 4: Konfigurieren Sie die Erfassung der Standorte von Braze.

Bitte stellen Sie sicher, dass die Erfassung der Standorte in Ihrer Braze-Konfiguration aktiviert ist. Wenn Sie Geofences ohne automatische Standortbestimmung aktivieren möchten, nehmen Sie bitte folgende Einstellungen in Ihrer Konfiguration`Braze.xml` vor:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Schritt 5: Anfrage für Standortberechtigungen zur Laufzeit stellen

Bitte stellen Sie bei der Registrierung von Geofences eine Anfrage an die Nutzer:innen um die Erlaubnis zur Standortbestimmung. Verwenden Sie in Ihrem C#-Code das folgende Muster:

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

Nachdem die Berechtigungen erteilt wurden, initialisieren Sie die Erfassung der Standorte von Braze:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Schritt 6: Manuelles Anfordern von Geofence-Updates (optional)

Um Geofences für einen bestimmten Standort manuell anzufordern:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Geofences können nur einmal pro Sitzung angefordert werden. Dies kann entweder automatisch durch das SDK oder manuell mit dieser Methode geschehen.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Schritt 2: Abhängigkeiten hinzufügen

Fügen Sie die folgende NuGet-Paket-Referenz zu Ihrem Projekt hinzu:

- `Braze.iOS.BrazeLocation`

### Schritt 3: Konfigurieren Sie die Nutzung der Standorte Info.plist

Fügen Sie einen String mit der Beschreibung der Verwendung von Standortdiensten in Ihrer Datei `Info.plist`hinzu:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple hat `NSLocationAlwaysUsageDescription` veraltet. Bitte verwenden Sie die oben genannten Tasten für iOS 14+.
{% endalert %}

### Schritt 4: Bitte aktivieren Sie Geofences in Ihrer Braze-Konfiguration.

Bitte konfigurieren Sie Braze in Ihrem App-Startcode (e.g., `App.xaml.cs`) mit aktivierten Geofences:

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

### Schritt 5: Aktivieren Sie Hintergrund-Updates für Standorte (optional)

Um Geofences im Hintergrund zu überwachen, aktivieren Sie bitte den Hintergrundmodus für **Standort-Updates**, indem Sie die `Info.plist`folgende Konfiguration zu Ihrer hinzufügen:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Legen Sie anschließend in Ihrer Braze-Konfiguration Folgendes fest:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Bitte stellen`DistanceFilter`Sie einen Wert ein, der den Anforderungen Ihrer App entspricht, um einen übermäßigen Batterieverbrauch zu vermeiden.
{% endalert %}

### Schritt 6: Anfrage für die Standortberechtigung stellen

Bitte stellen Sie bei den Nutzern:innen entweder `When In Use`die  oder`Always`die  Autorisierung an:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Ohne`Always`Genehmigung schränkt iOS die Ausführung von Ortungsdiensten ein, wenn die App nicht verwendet wird. Dies wird vom Betriebssystem erzwungen und kann vom Braze SDK nicht umgangen werden.
{% endalert %}
{% endtab %}
{% endtabs %}
