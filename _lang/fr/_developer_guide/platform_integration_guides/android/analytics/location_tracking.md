---
nav_title: Suivre la position
article_title: Suivre la position pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Cet article montre comment configurer le suivi de la position pour votre application Android ou FireOS."
Tool:
  - Position

---

# Suivre la position pour Android et FireOS

Ajoutez au moins l’une des autorisations suivantes à votre fichier `AndroidManifest.xml` pour déclarer l’intention de votre application de collecter les données de position :

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` comprend les données GPS lors de la signalisation de la position de l’utilisateur alors que `ACCESS_COARSE_LOCATION` comprend des données provenant du fournisseur non-GPS le plus économe en batterie du marché (par ex., le réseau). La position approximative sera probablement suffisante pour la plupart des cas d’utilisation ce type de données. Cependant, sous le modèle d’autorisations de temps d’exécution, recevoir l’autorisation de position de la part de l’utilisateur autorise implicitement la collecte des données de position précise. Consultez les [stratégies de position][1] des développeurs Android pour en savoir plus sur les différences entre ces autorisations de position et la façon dont vous devez les utiliser.

{% alert important %}
Avec la sortie d’Android M, Android est passé d’un modèle d’autorisation de temps d’installation à un de temps d’exécution. Pour activer le suivi des positions sur les appareils exécutant Android M ou suivants, l’application doit explicitement recevoir l’autorisation d’utiliser la position de l’utilisateur (Braze ne le fera pas). Une fois les autorisations de position obtenues, Braze commencera automatiquement le suivi de la position au-début de la prochaine session, si la collecte de la position est activée dans `braze.xml`. Les appareils exécutant des versions antérieures d’Android exigent uniquement que les autorisations de position soient déclarées dans le `AndroidManifest.xml`. Pour plus d’informations, consultez la [documentation d’autorisation](https://developer.android.com/training/permissions/index.html) d’Android.
{% endalert %}

## Désactiver le suivi automatique de la position

Pour désactiver le suivi automatique de la position, définissez `com_braze_enable_location_collection` sur faux dans `braze.xml` :

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

Vous pouvez ensuite enregistrer manuellement les points de données de position unique via la méthode [`setLastKnownLocation()`][4] sur `BrazeUser` comme suit :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
```

{% endtab %}
{% endtabs %}

[1]: https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html
