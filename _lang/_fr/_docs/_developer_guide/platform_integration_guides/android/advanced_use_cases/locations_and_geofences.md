---
nav_title: Emplacements & Géorepérages
article_title: Emplacements & Géorepérages pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 6
description: "Cet article de référence couvre la façon d'implémenter des localisations et des géorepérages dans votre application Android."
Tool:
  - Localisation
---

# Emplacements et géorepérages

Les géofences ne sont disponibles que dans certains paquets Braze. Pour y accéder, veuillez créer un [ticket de support][support] ou parler avec votre Responsable du service client de Braze. En savoir plus dans [Braze Docs]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/).

Pour prendre en charge les géorepérages pour Android:

1. Votre intégration doit prendre en charge les notifications push en arrière-plan.
2. Les géorepérages ou la collecte de localisation doivent être activés.

## Étape 1 : Mettre à jour build.gradle

Ajoutez le pack de localisation des services [Google Play][3] à votre app-level `build.gradle` en utilisant le [guide de configuration des services Google Play][10]:

```
dépendances {
  implémentation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## Étape 2 : Mettre à jour le manifeste

Ajoutez les permissions de démarrage, de localisation fine et de localisation en arrière-plan à votre `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
L'autorisation d'accès à la localisation en arrière-plan a été ajoutée dans Android 10 et est nécessaire pour que Geofences fonctionne pendant que l'application est en arrière-plan. Cette autorisation est nécessaire pour que Geofences fonctionne correctement sur les appareils Android 10+.
{% endalert %}

Ajoutez le récepteur de démarrage Braze à l'élément `application` de votre `AndroidManifest.xml`:

```xml
<receiver android:name="com.appboy.AppboyBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

{% alert note %}
Si vous utilisez une version du SDK Android inférieure à `2.3.0`, la déclaration de manifeste suivante est également requise :

```
<service android:name="com.appboy.services.AppboyGeofenceService"/>
```
{% endalert %}

## Étape 3 : Activer la collecte de l'emplacement de Braze

Si vous n'avez pas encore activé la collecte de l'emplacement de Braze, mettez à jour votre `brasier. ml` fichier à inclure `com_appboy_enable_location_collection` et s'assurer que sa valeur est définie à `true`.

```xml
<bool name="com_appboy_enable_location_collection">vrai</bool>
```

{% alert important %}
La collection d'emplacement Braze Android SDK 3.6.0 Braze est désactivée par défaut.
{% endalert %}

Les géorepérages sont activés si la collection de localisation de Braze est activée. Si vous souhaitez vous retirer de notre collection d'emplacement par défaut, mais que vous voulez toujours utiliser des géorepérages, il peut être activé sélectivement en définissant la valeur de la clé `com_appboy_geofences_enabled` à `true` dans `braze. ml`, indépendamment de la valeur de `com_appboy_enable_location_collection`.

```xml
<bool name="com_appboy_geofences_enabled">vrai</bool>
```

## Étape 4 : Obtenir les autorisations de localisation de l'utilisateur final

Pour Android M et les versions supérieures, vous devez demander des autorisations de localisation à l'utilisateur final avant de recueillir des informations de localisation ou d'enregistrer des géo-références.

Ajouter l'appel suivant pour notifier Braze lorsqu'un utilisateur accorde la permission de localisation à votre application :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(contexte).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(contexte).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

Cela fera que le SDK demandera des géorepérages aux serveurs de Braze et initialisera le suivi de géorepérage.

Voir [`RuntimePermissionUtils.java`][4] dans notre exemple d'application pour un exemple d'implémentation.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils. laiton) :
  int statique public final DROIDBOY_PERMISSION_LOCATION = 40 ;

  public static void handleOnRequestPermissionsResult(Contexte contextuel, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // Dans Android Q, nous avons besoin des autorisations d'emplacement FINE et BACKGROUND. Les deux
        // sont demandés simultanément.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Autorisations de localisation requises accordées. :
          Toast.makeText(contexte, "Autorisations de localisation requises accordées. , Toast.LENGTH_SHORT).show();
          Brésil. etInstance(context).requestLocationInitialization();
        } else {
          Log. (TAG, "Autorisations de localisation requises NON autorisées.");
          Toast.makeText(contexte, "Autorisations de localisation requises PAS accordées. , Toast.LENGTH_SHORT). comment();
        }
        casse ;
      par défaut :
        pause ;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult ! Gestionnaire de paquets. ERMISSION_GRANTED) {
        return false;
      }
    }
    retour vrai ;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  TAG privé = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  amusant handleOnRequestPermissionsResult(contexte: Context, requestCode : Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // Dans Android Q, nous avons besoin des autorisations d'emplacement FINE et BACKGROUND. Les deux
        // sont demandés simultanément.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Autorisations de localisation requises accordées.")
          Toast.makeText(context "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(contexte, "Autorisations de localisation requises PAS accordées.", Toast.LENGTH_SHORT). how()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult ! Gestionnaire de paquets. ERMISSION_GRANTED) {
        return false
      }
    }
    retour vrai
  }
}
```

{% endtab %}
{% endtabs %}

L'utilisation de l'échantillon de code ci-dessus se fait via :

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION. DK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils. asPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils. asPermission(getApplicationContext(), Manifest.permission. CCESS_FINE_LOCATION);
    si (! asAllPermissions) {
      // Demande les autorisations de localisation BACKGROUND et FINE
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils. ROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission. CCESS_FINE_LOCATION)) {
      // Demande uniquement la permission d'emplacement FINE
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils. ROIDBOY_PERMISSION_LOCATION );
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION. DK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils. asPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils. asPermission(applicationContext, Manifest.permission. CCESS_FINE_LOCATION)
    si (! asAllPermissions) {
      // Demande les permissions d'emplacement BACKGROUND et FINE
      requestPermissions(arrayOf(android. animé. ermission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils. ROIDBOY_PERMISSION_LOCATION)
    }
  } autre {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission. CCESS_FINE_LOCATION)) {
      // Demande uniquement la permission d'emplacement FINE
      requestPermissions(arrayOf(android.Manifest. ermission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

## Étape 5 : Activer les géorepérages sur le tableau de bord

Android permet seulement de stocker jusqu'à 100 géorepérages pour une application donnée. Le produit de Braze Locations utilisera jusqu'à 20 de ces emplacements de géorepérage si disponible. Pour éviter des perturbations accidentelles ou indésirables à d'autres fonctionnalités liées à la géolocalisation dans votre application, la géolocalisation doit être activée pour chaque application sur le tableau de bord.

Pour que le produit de Braze fonctionne correctement, vous devez également vous assurer que votre application n'utilise pas tous les points de géorepérage disponibles.

## Étape 6 : Demander manuellement des mises à jour de géorepérage (optionnel)

Par défaut, Braze récupère automatiquement la localisation de l'appareil et demande des géorepérages en fonction de cet emplacement collecté. Cependant, vous pouvez fournir manuellement une coordonnée GPS qui sera utilisée pour récupérer les géofences proximales de Braze à la place. Pour demander manuellement des géofences de Braze, vous devez désactiver les demandes automatiques de géorepérage de Braze et fournir une coordonnée GPS pour les requêtes.

#### Partie 1 : Désactiver les requêtes automatiques de géorepérage

Les requêtes automatiques Braze Geofence peuvent être désactivées dans votre fichier `braze.xml` en définissant `com_appboy_automatic_geofence_requests_enabled` à `false`.

```xml
<bool name="com_appboy_automatic_geofence_requests_enabled">faux</bool>
```

Cela peut être fait en plus lors de l'exécution via :

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

#### Partie 2 : Demande manuelle de géorepérage de Braze avec coordonnées GPS

Les géofences Braze sont demandées manuellement via la méthode [`requestGeofences()`][11].

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
Braze Geofences ne peut être demandé qu'une seule fois par session, soit automatiquement par le SDK soit manuellement avec la méthode ci-dessus.
{% endalert %}

##### Activer les géorepérages à partir de la page des localisations :

![Console de Développeur Braze]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

##### Activer les géorepérages depuis la page des paramètres:

![Console de Développeur Braze]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## Note à propos de push to sync

Notez que Braze synchronise les géorepérages sur les périphériques en utilisant une poussée de fond. Dans la plupart des cas, cela n'entraînera aucun changement de code, car cette fonctionnalité ne nécessite aucune intégration de la part de l'application.

Cependant, notez que si votre application est arrêtée, recevoir une poussée en arrière-plan la lancera en arrière-plan et en son `application. La méthode nCreate()` sera appelée. Si vous avez une application personnalisée. nCreate() implémentation, vous devriez reporter les appels automatiques au serveur et toutes les autres actions que vous ne voulez pas être déclenchées par une poussée en arrière-plan.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://github.com/Appboy/appboy-android-sdk/blob/91622eb6cd4bba2e625cc22f00ca38e6136a0596/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.java
[10]: https://developers.google.com/android/guides/setup
[11]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/request-geofences.html
[support]: {{site.baseurl}}/braze_support/
