---
nav_title: Suivi de la localisation
article_title: Suivi de localisation pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 6
description: "Cet article montre comment configurer le suivi de localisation pour votre application Android."
Tool:
  - Localisation
---

# Suivi de localisation pour Android/FireOS

Ajoutez au moins une des permissions suivantes à votre fichier `AndroidManifest.xml` pour déclarer l'intention de votre application de collecter les données de localisation :

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
Ou:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

{% alert important %}
  Avec la sortie d'Android M, Android est passé d'un modèle d'autorisation d'installation à un modèle d'autorisation d'exécution. Pour activer le suivi de localisation sur les appareils fonctionnant M et ci-dessus, l'application doit recevoir explicitement l'autorisation d'utiliser l'emplacement de l'utilisateur (Braze ne le fera pas). Une fois les autorisations de localisation obtenues, Braze commencera automatiquement à suivre l'emplacement au prochain démarrage de la session, si la collecte de l'emplacement est activée dans `braze. ml`. Les appareils exécutant des versions antérieures d'Android ne nécessitent que les autorisations de localisation pour être déclarées dans le `AndroidManifest.xml`. Pour plus d'informations, visitez la [documentation de permission](https://developer.android.com/training/permissions/index.html) d'Android.
{% endalert %}

`ACCESS_FINE_LOCATION` inclut les données GPS dans la localisation de l'utilisateur alors que `ACCESS_COARSE_LOCATION` inclut les données du fournisseur non GPS le plus efficace de batterie disponible (e. . le réseau). La localisation approximative sera probablement suffisante pour la majorité des cas d'utilisation des données de localisation ; cependant, sous le modèle des permissions d'exécution, recevant l'autorisation de localisation de l'utilisateur autorise implicitement la collecte de données de localisation fine. Vous pouvez en savoir plus sur les différences entre ces permissions de localisation et comment vous devriez les utiliser [ici][1].

## Désactivation du suivi automatique de la localisation

Pour désactiver le suivi automatique d'emplacement, mettez `com_appboy_enable_location_collection` à false dans `braze.xml`:

```xml
<bool name="com_appboy_enable_location_collection">faux</bool>
```

Ensuite, vous pouvez enregistrer manuellement des points de données d'emplacement unique via la méthode `setLastKnownLocation()` sur `BrazeUser` comme ceci :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, EXACTITUDE_DOUBLE_VALUE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, EXACTITUDE_DOUBLE_VALUE)
```

{% endtab %}
{% endtabs %}

Voir [ici dans notre KDoc][4] pour plus d'informations sur la méthode `setLastKnownLocation()`.

[1]: https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html
