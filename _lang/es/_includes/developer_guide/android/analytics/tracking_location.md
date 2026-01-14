## Registro de la ubicación actual

Aunque el seguimiento continuo esté desactivado, puedes registrar manualmente la ubicación actual del usuario utilizando el método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) método.

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

## Seguimiento continuo de la ubicación

{% alert important %}
[A partir de Android Marshmallow](https://developer.android.com/training/permissions/index.html), debes pedir a tus usuarios que acepten explícitamente el seguimiento de ubicación. Una vez que lo hagan, Braze puede empezar a seguir su ubicación al inicio de la siguiente sesión. A diferencia de las versiones anteriores de Android, en las que sólo era necesario declarar los permisos de ubicación en tu `AndroidManifest.xml`.
{% endalert %}

Para realizar un seguimiento continuo de la ubicación de un usuario, tendrás que declarar la intención de tu aplicación de recopilar datos de ubicación añadiendo al menos uno de los siguientes permisos a tu archivo `AndroidManifest.xml`.

|Permiso|Descripción|
|---|---|
| `ACCESS_COARSE_LOCATION` | Utiliza el proveedor no GPS que consuma menos batería (como una red doméstica). Normalmente, esto es suficiente para la mayoría de las necesidades de datos de ubicación. Según el modelo de permisos en tiempo de ejecución, la concesión del permiso de ubicación autoriza implícitamente la recopilación de datos de ubicación fina. |
| `ACCESS_FINE_LOCATION`   | Incluye datos GPS para una ubicación más precisa. Según el modelo de permisos en tiempo de ejecución, conceder permiso de ubicación también cubre el acceso a la ubicación fina. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Tu `AndroidManifest.xml` debe ser similar al siguiente:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Desactivar el seguimiento continuo

Puedes desactivar el seguimiento continuo en tiempo de compilación o de ejecución.

{% tabs local %}
{% tab tiempo de compilación %}

Para desactivar el seguimiento de ubicación continuo en tiempo de compilación, configura `com_braze_enable_location_collection` en `false` en `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab tiempo de ejecución %}

Para desactivar selectivamente el seguimiento de ubicación continuo en tiempo de ejecución, utiliza [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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
