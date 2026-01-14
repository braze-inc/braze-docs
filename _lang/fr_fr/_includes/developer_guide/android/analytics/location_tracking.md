# Suivi de localisation

> Cet article montre comment configurer la géolocalisation pour votre application Android ou FireOS.

Ajoutez au moins l’une des autorisations suivantes à votre fichier `AndroidManifest.xml` pour déclarer l’intention de votre application de collecter les données de position :

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` inclut les données GPS dans le rapport de localisation de l'utilisateur tandis que `ACCESS_COARSE_LOCATION` inclut les données du fournisseur non-GPS le plus économe en batterie disponible (par exemple, le réseau). La localisation approximative sera probablement suffisante pour la plupart des cas d’utilisation ce type de données. Cependant, sous le modèle d’autorisations de temps d’exécution, recevoir l’autorisation de position de la part de l’utilisateur autorise implicitement la collecte des données de localisation précise. Jetez un œil à [Stratégies de localisation](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html) des développeurs Android pour en savoir plus sur les différences entre ces autorisations de localisation et comment vous devez les utiliser.

{% alert important %}
Avec la sortie d’Android M, Android est passé d’un modèle d’autorisation de temps d’installation à un de temps d’exécution. Pour activer le suivi des positions sur les appareils exécutant Android M ou suivants, l’application doit explicitement recevoir l’autorisation d’utiliser la position de l’utilisateur (Braze ne le fera pas). Après l'obtention des autorisations de localisation, Braze commencera automatiquement à suivre la localisation au début de la session suivante si la collecte de localisation est activée dans `braze.xml`. Les appareils exécutant des versions antérieures d’Android exigent uniquement que les autorisations de position soient déclarées dans le `AndroidManifest.xml`. Pour plus d’informations, consultez la [documentation sur les autorisations](https://developer.android.com/training/permissions/index.html) d’Android.
{% endalert %}

## Désactiver le suivi automatique de la localisation

### Option de temps de compilation

Pour désactiver le suivi automatique de la localisation lors de la compilation, définissez `com_braze_enable_location_collection` sur `false` dans `braze.xml` :

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### Option d’exécution

Pour désactiver sélectivement le suivi automatique de la localisation lors de l’exécution, utilisez [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration) :

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## Enregistrer manuellement la position

Même lorsque le suivi automatique est désactivé, vous pouvez enregistrer manuellement des points de données de localisation uniques via la méthode [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) sur `BrazeUser` comme ceci :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

