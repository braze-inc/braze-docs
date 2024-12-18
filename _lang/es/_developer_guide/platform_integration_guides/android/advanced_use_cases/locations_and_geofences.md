---
nav_title: Ubicación y geovallas
article_title: Ubicación y geovallas para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Este artículo de referencia explica cómo implementar la ubicación y los geovallados en tu aplicación Android o FireOS."
Tool:
  - Location

---

# Ubicación y geovallas

> [Las geovallas]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) solo están disponibles en determinados paquetes Braze. Para acceder, crea un [ticket de soporte]({{site.baseurl}}/braze_support/) o habla con tu administrador del éxito del cliente Braze.

Para admitir geovallas para Android:

1. Tu integración debe admitir notificaciones push en segundo plano.
2. Las geovallas Braze o la recopilación de ubicaciones deben estar habilitadas.

## Paso 1: Actualiza build.gradle

Añade `android-sdk-location` al nivel de tu aplicación `build.gradle`. Además, añade el [paquete de ubicación](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) de Google Play Services utilizando la [guía de configuración](https://developers.google.com/android/guides/setup) de Google Play Services:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## Paso 2: Actualiza el manifiesto

Añade permisos de arranque, ubicación fina y ubicación en segundo plano a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
El permiso de acceso a la ubicación en segundo plano se añadió en Android 10 y es necesario para que las geovallas funcionen mientras la aplicación está en segundo plano para todos los dispositivos Android 10+.
{% endalert %}

Añade el receptor de arranque Braze al elemento `application` de tu `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

## Paso 3: Habilitar la recogida de ubicaciones Braze

Si aún no has habilitado la recopilación de ubicaciones de Braze, actualiza tu archivo `braze.xml` para incluir `com_braze_enable_location_collection` y confirma que su valor es `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir de la versión 3.6.0 del SDK para Android de Braze, la recopilación de ubicaciones de Braze está desactivada por defecto.
{% endalert %}

Las geovallas Braze están habilitadas si está habilitada la recopilación de ubicaciones Braze. Si deseas excluirte de nuestra recopilación predeterminada de ubicaciones, pero quieres seguir utilizando geovallas, puedes habilitarlo selectivamente estableciendo el valor de la clave `com_braze_geofences_enabled` en `true` en `braze.xml`, independientemente del valor de `com_braze_enable_location_collection`:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## Paso 4: Obtener permisos de ubicación del usuario final

Para Android M y versiones superiores, debes solicitar permisos de ubicación al usuario final antes de recopilar información de ubicación o registrar geovallas.

Añade la siguiente llamada para notificar a Braze cuando un usuario conceda el permiso de ubicación a tu aplicación:

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

Esto hará que el SDK solicite geovallas a los servidores Braze e inicie el seguimiento de geovallas.

Consulta [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) en nuestro ejemplo de aplicación para ver un ejemplo de implementación.

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

El uso del código de ejemplo anterior se realiza mediante:

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

## Paso 5: Habilitar geovallas en el panel

Android solo permite almacenar hasta 100 geovallas para una aplicación determinada. Los productos de ubicación Braze utilizarán hasta 20 ranuras de geovalla si están disponibles. Para evitar interrupciones accidentales o no deseadas de otras funciones relacionadas con la geovalla en tu aplicación, las geovallas de ubicación deben estar habilitadas para aplicaciones individuales en el panel.

Para que los productos de ubicación Braze funcionen correctamente, confirma que tu aplicación no está utilizando todos los puntos de geovalla disponibles.

### Habilitar geovallas desde la página de ubicaciones

![Las opciones de geovalla en la página de ubicaciones de Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Habilitar geovallas desde la página de configuración

![La casilla de geovalla situada en las páginas de configuración de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## Paso 6: Solicitar manualmente actualizaciones de geovallas (opcional)

Por defecto, Braze recupera automáticamente la ubicación del dispositivo y solicita geovallas basadas en esa ubicación recopilada. Sin embargo, puedes proporcionar manualmente una coordenada GPS que se utilizará para recuperar geovallas próximas de Braze. Para solicitar manualmente geovallas Braze, debes desactivar las solicitudes automáticas de geovallas Braze y proporcionar una coordenada GPS para las solicitudes.

#### Parte 1: Desactivar las solicitudes automáticas de geovallas

Las solicitudes automáticas de geovallas de Braze pueden desactivarse en tu archivo `braze.xml` configurando `com_braze_automatic_geofence_requests_enabled` como `false`:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Esto puede hacerse adicionalmente en tiempo de ejecución mediante:

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

#### Parte 2: Solicitar manualmente la geovalla Braze con coordenadas GPS

Las geovallas de Braze se solicitan manualmente mediante el método [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html):

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
Las geovallas solo pueden solicitarse una vez por sesión, ya sea automáticamente por el SDK o manualmente con este método.
{% endalert %}

## Push para sincronizar

Ten en cuenta que Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. En la mayoría de los casos, esto no implicará cambios en el código, ya que esta característica no requiere una mayor integración por parte de la aplicación.

Sin embargo, nota que si tu aplicación está parada, al recibir un push en segundo plano se lanzará en segundo plano y se llamará a su método `Application.onCreate()`. Si tienes una implementación personalizada de `Application.onCreate()`, debes aplazar las llamadas automáticas al servidor y cualquier otra acción que no quieras que sea desencadenada por el push en segundo plano.

