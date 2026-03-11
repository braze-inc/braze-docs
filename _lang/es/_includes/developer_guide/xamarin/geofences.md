{% multi_lang_include developer_guide/prerequisites/xamarin.md %} Además, tendrás que [configurar notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Requisitos previos

Estas son las versiones mínimas del SDK necesarias para empezar a utilizar geovallas:

{% sdk_min_versions xamarin:9.0.0 %}

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitar en Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

A continuación, sigue las instrucciones específicas de la plataforma que se indican a continuación para Android o iOS:

{% tabs %}
{% tab Android %}

### Paso 2: Añadir dependencias

Añade la siguiente referencia al paquete NuGet a tu proyecto:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Paso 3: Actualiza tu AndroidManifest.xml

Añade los siguientes permisos a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Se requiere el permiso de acceso a la ubicación en segundo plano para que las geovallas funcionen mientras la aplicación está en segundo plano en dispositivos con Android 10 o superior.
{% endalert %}

### Paso 4: Configurar la recopilación de ubicación de Braze

Asegúrate de que la recopilación de ubicación esté habilitada en tu configuración de Braze. Si deseas habilitar las geovallas sin la recopilación automática de la ubicación, configura lo siguiente en tu `Braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Paso 5: Solicitar permisos de ubicación en tiempo de ejecución

Debes solicitar permisos de ubicación al usuario antes del registro de geovallas. En tu código C#, utiliza el siguiente patrón:

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

Una vez concedidos los permisos, inicializa la recopilación de ubicación de Braze:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Paso 6: Solicitar manualmente actualizaciones de geovallas (opcional)

Para solicitar manualmente geovallas para una ubicación específica:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Las geovallas solo pueden solicitarse una vez por sesión, ya sea automáticamente por el SDK o manualmente con este método.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Paso 2: Añadir dependencias

Añade la siguiente referencia al paquete NuGet a tu proyecto:

- `Braze.iOS.BrazeLocation`

### Paso 3: Configura el uso de la ubicación en Info.plist

Añade una cadena con la descripción del uso de los servicios de ubicación en tu `Info.plist`:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple ha dejado de utilizar `NSLocationAlwaysUsageDescription`. Utiliza las teclas anteriores para iOS 14+.
{% endalert %}

### Paso 4: Habilita las geovallas en tu configuración de Braze.

En el código de inicio de tu aplicación (e.g., `App.xaml.cs`), configura Braze con las geovallas habilitadas:

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

### Paso 5: Habilita las actualizaciones de ubicación en segundo plano (opcional)

Para supervisar las geovallas en segundo plano, habilita el modo de fondo **de actualizaciones de ubicación** añadiendo la siguiente configuración a tu `Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

A continuación, en tu configuración de Braze, establece:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Establece`DistanceFilter`un valor que se ajuste a las necesidades de tu aplicación para evitar que se agote la batería.
{% endalert %}

### Paso 6: Solicitar autorización de ubicación

Solicita al usuario la autorización`Always`  o`When In Use`  :

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Sin`Always`autorización, iOS restringe el funcionamiento de los servicios de ubicación mientras la aplicación no está en uso. Esto lo impone el sistema operativo y no puede ser eludido por el SDK de Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
