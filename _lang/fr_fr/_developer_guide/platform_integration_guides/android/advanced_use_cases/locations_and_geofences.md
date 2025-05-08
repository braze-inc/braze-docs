---
nav_title: Position et géorepérages 
article_title: Position et géorepérages pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Cet article de référence explique comment mettre en œuvre une localisation et des géorepérages dans votre application Android ou FireOS."
Tool:
  - Location

---

# Position et géorepérages

> Les [géorepérages]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) sont uniquement disponibles dans certains forfaits Braze. Pour y accéder, créez un [ticket d'assistance]({{site.baseurl}}/braze_support/) ou adressez-vous à votre gestionnaire satisfaction client Braze.

Pour prendre en charge les géorepérages pour Android :

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages de Braze ou la collecte des données de localisation doivent être activés.

## Étape 1 : Mise à jour build.gradle

Ajoutez `android-sdk-location` à votre `build.gradle` au niveau de l’application. Ajoutez également les [services de localisation](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) de Google Play en utilisant le [guide de configuration](https://developers.google.com/android/guides/setup) des services Google Play :

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## Étape 2 : Mettre à jour le manifeste

Ajoutez des autorisations de démarrage, de recherche de position et de position en arrière-plan à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
L’autorisation d’accès à la localisation en arrière-plan a été ajoutée dans Android 10 et est requise pour que les géorepérages fonctionnent, tandis que l’application est mise en arrière-plan pour tous les appareils Android 10 et suivants.
{% endalert %}

Ajoutez le récepteur de démarrage Braze à l’élément `application` de votre `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

## Étape 3 : Activer le recueil des données de localisation Braze

Si vous n'avez pas encore activé la collecte d'emplacements/localisations de Braze, mettez à jour votre fichier `braze.xml` pour y inclure `com_braze_enable_location_collection` et confirmez que sa valeur est fixée à `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Braze pour Android, le recueil des données de localisation Braze est désactivé par défaut.
{% endalert %}

Les géorepérages de Braze sont activés si la fonction de géolocalisation de Braze est activée. Si vous souhaitez désactiver notre fonction de géolocalisation par défaut mais que vous souhaitez toujours utiliser des géorepérages, elle peut être activée de manière sélective en définissant la valeur de la clé `com_braze_geofences_enabled` sur `true` dans `braze.xml`, indépendamment de la valeur de `com_braze_enable_location_collection` :

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## Étape 4 : Obtenir les autorisations de localisation de l’utilisateur final

Pour Android M et les versions plus élevées, vous devez demander des autorisations de position auprès de l’utilisateur final avant de collecter des informations de position ou d’enregistrer des géorepérages.

Ajoutez l’appel suivant pour notifier Braze lorsqu’un utilisateur accorde l’autorisation de position à votre application :

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

Le SDK va alors demander des géorepérages aux serveurs de Braze et initialiser le suivi du géorepérage.

Voir [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) dans notre exemple d'application pour un exemple de mise en œuvre.

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

L’utilisation de l’exemple de code précédent est effectuée via :

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

## Étape 5 : Activer les géorepérages sur le tableau de bord

Android autorise le stockage de seulement 100 géorepérages pour une application donnée. Les produits de localisation de Braze utiliseront jusqu'à 20 emplacements de géorepérage, sous réserve de disponibilité. Pour éviter toute perturbation accidentelle ou indésirable d’autres fonctionnalités liées au géorepérage dans votre application, les géorepérages de localisation doivent être activés pour les applications individuelles sur le tableau de bord.

Pour que les produits de localisation de Braze fonctionnent correctement, vérifiez que votre appli n'utilise pas tous les emplacements de géorepérage disponibles.

### Activer les géorepérages à partir de la page des localisations

![Les options de géorepérage sur la page des localisations Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Activer les géorepérages à partir de la page des paramètres

![La case à cocher de géorepérage située sur les pages de paramètres de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## Étape 6 : Demander manuellement des mises à jour de géorepérage (facultatif)

Par défaut, Braze récupère automatiquement la localisation de l’appareil et demande des géorepérages en fonction de la localisation collectée. Cependant, vous pouvez fournir manuellement une coordonnée GPS qui sera utilisée pour récupérer à la place les géorepérages de proximité de Braze. Pour demander manuellement des géorepérages Braze, vous devez désactiver les demandes de géorepérage automatiques de Braze et fournir une coordonnée GPS pour les demandes.

#### Partie 1 : Désactiver les requêtes de géorepérage automatique

Les demandes de géorepérage automatique de Braze peuvent être désactivées dans votre fichier `braze.xml` en définissant `com_braze_automatic_geofence_requests_enabled` sur `false` :

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Cela peut également être effectué au moment de l’exécution via :

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

#### Partie 2 : Demander manuellement un géorepérage Braze avec des coordonnées GPS

Les géorepérages de Braze sont demandés manuellement via la méthode [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) :

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
Les géorepérages ne peuvent être demandés qu’une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}

## Notification push pour synchroniser

Notez que Braze synchronise les géorepérages vers les dispositifs à l’aide de notifications push en arrière-plan. Dans la plupart des cas, cela n’implique aucun changement de code, car cette fonctionnalité ne nécessite aucune intégration supplémentaire de la part de l’application.

Cependant, notez que si votre application est arrêtée, la réception d’une notification push en arrière-plan la lancera en arrière-plan et la méthode `Application.onCreate()` sera appelé. Si vous avez une implémentation personnalisée `Application.onCreate()`, vous devez reporter les appels de serveur automatique et toute autre action que vous ne souhaitez pas déclencher par la notification push en arrière-plan.

