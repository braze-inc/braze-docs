# Seguimiento de la ubicación

> Este artículo muestra cómo configurar el seguimiento de ubicación para tu aplicación Android o FireOS.

Añade al menos uno de los siguientes permisos a tu archivo `AndroidManifest.xml` para declarar la intención de tu aplicación de recopilar datos de ubicación:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` incluye datos GPS al informar de la ubicación del usuario, mientras que `ACCESS_COARSE_LOCATION` incluye datos del proveedor no GPS más eficiente en cuanto a batería disponible (por ejemplo, la red). La ubicación aproximada será probablemente suficiente para la mayoría de los casos de uso de los datos de ubicación; sin embargo, según el modelo de permisos en tiempo de ejecución, recibir el permiso de ubicación del usuario autoriza implícitamente la recopilación de datos de ubicación precisos. Echa un vistazo a [Estrategias de ubicación](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html) de los desarrolladores de Android para saber más sobre las diferencias entre estos permisos de ubicación y cómo debes utilizarlos.

{% alert important %}
Con el lanzamiento de Android M, Android pasó de un modelo de permisos durante el tiempo de instalación a un modelo de permisos durante el tiempo de ejecución. Para habilitar el seguimiento de ubicación en dispositivos con Android M o posterior, la aplicación debe recibir explícitamente permiso del usuario para utilizar la ubicación (Braze no lo hará). Una vez obtenidos los permisos de ubicación, Braze iniciará automáticamente el seguimiento de ubicación en el siguiente inicio de sesión si la recopilación de ubicaciones está habilitada en `braze.xml`. Los dispositivos que ejecutan versiones anteriores de Android solo requieren que los permisos de ubicación se declaren en `AndroidManifest.xml`. Para más información, visita la [documentación sobre permisos](https://developer.android.com/training/permissions/index.html) de Android.
{% endalert %}

## Desactivar el seguimiento de ubicación automático

### Opción de compilación

Para desactivar el seguimiento de ubicación automático durante el tiempo de compilación, configura `com_braze_enable_location_collection` en `false` en `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### Opción de tiempo de ejecución

Para desactivar selectivamente el seguimiento de ubicación automático durante el tiempo de ejecución, utiliza [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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

## Registrar manualmente la ubicación

Aunque el seguimiento automático esté desactivado, puedes registrar manualmente puntos de datos de ubicación individuales mediante el método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) en `BrazeUser` de esta forma:

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

