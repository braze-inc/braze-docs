{% multi_lang_include developer_guide/prerequisites/android.md %} Zusätzlich müssen Sie [stille Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Schritt 2: `build.gradle` aktualisieren

Fügen Sie `android-sdk-location` zu Ihrer App-Ebene `build.gradle` hinzu. Fügen Sie außerdem das [Standortpaket](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) der Google-Play-Dienste mithilfe der [Setup-Anleitung](https://developers.google.com/android/guides/setup) der Google-Play-Dienste hinzu:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### Schritt 3: Manifest aktualisieren

Fügen Sie der `AndroidManifest.xml` die folgenden Berechtigungen hinzu:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Die Berechtigung für den Zugriff auf den Standort im Hintergrund wurde in Android 10 hinzugefügt und ist erforderlich, damit Geofences auf allen Geräten ab Android 10 funktionieren, während die App im Hintergrund läuft.
{% endalert %}

Fügen Sie den Braze Boot Receiver in das `application` Element Ihres `AndroidManifest.xml` ein:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### Schritt 4: Aktivieren Sie die Braze-Standorterfassung

Wenn Sie die Braze-Standortermittlung noch nicht aktiviert haben, aktualisieren Sie die Datei `braze.xml` so, dass sie `com_braze_enable_location_collection` enthält, und stellen Sie sicher, dass der Wert auf `true` festgelegt ist:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Ab Version 3.6.0 des Braze Android-SDK ist die Braze-Standortermittlung standardmäßig deaktiviert.
{% endalert %}

Braze-Geofences sind aktiviert, wenn die Braze-Standorterfassung aktiviert ist. Wenn Sie unsere standardmäßige Standortermittlung ablehnen, aber dennoch Geofences verwenden möchten, können Sie diese selektiv aktivieren, indem Sie – unabhängig vom Wert für `com_braze_enable_location_collection` – den Wert des Schlüssels `com_braze_geofences_enabled` in `braze.xml` auf `true` setzen:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### Schritt 5: Berechtigungen zur Standortermittlung vom Endnutzer einholen

Bei Android M und höheren Versionen müssen Sie den Endbenutzer um Standortgenehmigungen bitten, bevor Sie Standortinformationen sammeln oder Geofences registrieren können.

Fügen Sie den folgenden Aufruf hinzu, um Braze zu benachrichtigen, wenn ein Nutzer Ihrer App die Berechtigung zur Standortermittlung erteilt:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

Daraufhin fordert das SDK Geofences von Braze-Servern an und initialisiert das Geofence-Tracking.

Eine Beispielimplementierung finden Sie unter [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) in unserer Beispielanwendung.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY_PERMISSION_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.");
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
          Braze.getInstance(context).requestLocationInitialization();
        } else {
          Log.i(TAG, "Required location permissions NOT granted.");
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  fun handleOnRequestPermissionsResult(context: Context, requestCode: Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false
      }
    }
    return true
  }
}
```

{% endtab %}
{% endtabs %}

Die Verwendung des vorangehenden Beispielcodes erfolgt über:

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Schritt 6: Manuelles Anfordern von Geofence-Updates (optional)

Braze ruft den Standort des Geräts standardmäßig automatisch ab und fordert anhand des erfassten Standorts Geofences an. Sie können jedoch manuell eine GPS-Koordinate angeben, die stattdessen zum Abrufen der nächstgelegenen Braze-Geofences verwendet wird. Um Braze Geofences manuell anzufordern, müssen Sie die automatischen Braze Geofence-Anfragen deaktivieren und eine GPS-Koordinate für Anfragen angeben.

#### Schritt 6.1: Automatische Geofence-Anfragen deaktivieren

Automatische Geofence-Anfragen von Braze können in der Datei `braze.xml` deaktiviert werden, indem `com_braze_automatic_geofence_requests_enabled` auf `false` gesetzt wird:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Dies kann auch zur Laufzeit wie folgt erfolgen:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### Schritt 6.2: Manuelles Anfordern von Braze Geofence mit GPS-Koordinaten

Braze-Geofences werden manuell über die Methode [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) angefordert:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Geofences können nur einmal pro Sitzung angefordert werden. Dies kann entweder automatisch durch das SDK oder manuell mit dieser Methode geschehen.
{% endalert %}

### Enablement von Push-to-Sync

Beachten Sie, dass Braze einen Push im Hintergrund verwendet, um Geofences mit Geräten zu synchronisieren. In den meisten Fällen sind damit keine Code-Änderungen verbunden, da diese Funktion keine weitere Integration auf Seiten der App erfordert.

Wenn Ihre Anwendung jedoch angehalten wurde und einen Push im Hintergrund empfängt, wird sie im Hintergrund gestartet und die Methode `Application.onCreate()` aufgerufen. Wenn Sie eine benutzerdefinierte `Application.onCreate()` -Implementierung haben, sollten Sie automatische Serveraufrufe und alle anderen Aktionen, die nicht durch Hintergrund-Push ausgelöst werden sollen, zurückstellen.
