## Enregistrement de l'emplacement/localisation actuel

Même si le suivi continu est désactivé, vous pouvez enregistrer manuellement l'emplacement/localisation actuel de l'utilisateur à l'aide de la méthode [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) méthode.

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

## Suivi continu de l'emplacement/localisation

{% alert important %}
[À partir d'Android Marshmallow](https://developer.android.com/training/permissions/index.html), vous devez demander à vos utilisateurs d'accepter explicitement l'emplacement/localisation. Une fois qu'ils l'ont fait, Braze peut commencer à suivre leur emplacement/localisation au début de la session suivante. Contrairement aux versions antérieures d'Android, où il suffisait de déclarer les autorisations d'emplacement/localisation sur votre site `AndroidManifest.xml`.
{% endalert %}

Pour suivre en permanence l'emplacement/localisation d'un utilisateur, vous devrez déclarer l'intention de votre application de collecter des données d'emplacement/localisation en ajoutant au moins l'une des autorisations suivantes à votre fichier `AndroidManifest.xml`.

|Autorisation|Description|
|---|---|
| `ACCESS_COARSE_LOCATION` | Utilise le fournisseur d'accès non GPS le plus économe en batterie (réseau domestique, par exemple). En général, cela suffit pour répondre à la plupart des besoins en matière de données d'emplacement/localisation. Dans le cadre du modèle de permissions d'exécution, l'octroi d'une permission d'emplacement/localisation autorise implicitement la collecte de données d'emplacement/localisation fines. |
| `ACCESS_FINE_LOCATION`   | Inclut des données GPS pour une localisation plus précise. Dans le cadre du modèle d'autorisations d'exécution, l'octroi d'une autorisation d'emplacement/localisation couvre également l'accès à l'emplacement/localisation fin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Votre site `AndroidManifest.xml` devrait ressembler à ce qui suit :

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Désactiver le suivi continu

Vous pouvez désactiver le suivi continu au moment de la compilation ou de l'exécution.

{% tabs local %}
{% tab temps de compilation %}

Pour désactiver le suivi continu de l'emplacement/localisation au moment de la compilation, définissez `com_braze_enable_location_collection` sur `false` dans `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab durée d'exécution %}

Pour désactiver de manière sélective le suivi continu de l'emplacement/localisation au moment de l'exécution, utilisez l'option [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
