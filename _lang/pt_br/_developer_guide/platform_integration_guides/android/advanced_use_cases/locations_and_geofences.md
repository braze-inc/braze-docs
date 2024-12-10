---
nav_title: Localização e geofences
article_title: Locais e geofences para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Este artigo de referência aborda como implementar locais e geofences em seu aplicativo para Android ou FireOS."
Tool:
  - Location

---

# Local e geofences

> [As geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) estão disponíveis somente em alguns pacotes da Braze. Para obter acesso, crie um [tíquete de suporte]({{site.baseurl}}/braze_support/) ou fale com seu gerente de sucesso do cliente Braze.

Para oferecer suporte a geofences para Android:

1. Sua integração deve suportar notificações por push em segundo plano.
2. As geofences do Braze ou a coleta de locais devem estar ativadas.

## Etapa 1: Atualize build.gradle

Adicione `android-sdk-location` ao seu nível de app `build.gradle`. Além disso, adicione o [pacote local do](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) Google Play Services usando o [guia de configuração](https://developers.google.com/android/guides/setup) do Google Play Services:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## Etapa 2: Atualizar o manifesto

Adicione permissões de inicialização, de local de trabalho e de local de fundo ao seu site `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
A permissão de acesso ao local em segundo plano foi adicionada no Android 10 e é necessária para que o Geofences funcione enquanto o app estiver em segundo plano em todos os dispositivos Android 10+.
{% endalert %}

Adicione o receptor de inicialização da Braze ao elemento `application` de seu `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

## Etapa 3: Ativar a coleta de locais do Braze

Se ainda não tiver ativado a coleta de locais do Braze, atualize seu arquivo `braze.xml` para incluir `com_braze_enable_location_collection` e confirme que seu valor está definido como `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir da versão 3.6.0 do Braze Android SDK, a coleta de locais da Braze é desativada por padrão.
{% endalert %}

As geofences do Braze são ativadas se a coleta de locais do Braze estiver ativada. Se desejar optar por não participar da nossa coleta de locais padrão, mas ainda quiser usar geofences, isso pode ser ativado seletivamente definindo o valor da chave `com_braze_geofences_enabled` como `true` em `braze.xml`, independentemente do valor de `com_braze_enable_location_collection`:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## Etapa 4: Obter permissões de local do usuário final

Para Android M e versões superiores, é necessário solicitar permissões de localização ao usuário final antes de coletar informações de local ou registrar geofences.

Adicione a seguinte chamada para notificar o Braze quando um usuário conceder a permissão de local ao seu app:

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

Isso fará com que o SDK solicite geofences dos servidores da Braze e inicialize o rastreamento de geofences.

Veja [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) em nosso aplicativo de amostra para ver um exemplo de implementação.

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

O uso do código de exemplo anterior é feito por meio de:

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

## Etapa 5: Ativar geofences no dashboard

O Android só permite o armazenamento de até 100 geofences em um determinado app. Os produtos de localização da Braze usarão até 20 slots de geofence, se disponíveis. Para evitar a interrupção acidental ou indesejada de outras funcionalidades relacionadas a geofences em seu aplicativo, as geofences locais devem ser ativadas para aplicativos individuais no dashboard.

Para que os produtos locais da Braze funcionem corretamente, confirme se o app não está usando todos os pontos de geofence disponíveis.

### Ativar geofences na página de locais

![As opções de geofence na página de locais do Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Ativar geofences na página de configurações

![A caixa de seleção de geofence localizada nas páginas de configurações do Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## Etapa 6: Solicitar manualmente atualizações de geofence (opcional)

Por padrão, a Braze recupera automaticamente o local do dispositivo e solicita geofences com base nesse local coletado. No entanto, você pode fornecer manualmente uma coordenada GPS que será usada para recuperar geofences Braze próximas. Para solicitar geofences do Braze manualmente, você deve desativar as solicitações automáticas de geofences do Braze e fornecer uma coordenada de GPS para as solicitações.

#### Parte 1: Desativar solicitações automáticas de geofence

As solicitações automáticas de geofence da Braze podem ser desativadas em seu arquivo `braze.xml`, definindo `com_braze_automatic_geofence_requests_enabled` como `false`:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Além disso, isso pode ser feito em tempo de execução por meio de:

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

#### Parte 2: Solicitar manualmente a geofence do Braze com coordenadas de GPS

As geofences da Braze são solicitadas manualmente por meio do método [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) método:

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
As geofences só podem ser solicitadas uma vez por sessão, seja automaticamente pelo SDK ou manualmente com esse método.
{% endalert %}

## Push to sync

Note que o Braze sincroniza geofences com dispositivos usando o push em segundo plano. Na maioria dos casos, isso não envolverá alterações de código, pois esse recurso não requer integração adicional por parte do app.

No entanto, note que, se seu aplicativo estiver interrompido, o recebimento de um push em segundo plano o iniciará em segundo plano e seu método `Application.onCreate()` será chamado. Se você tiver uma implementação personalizada do `Application.onCreate()`, deverá adiar as chamadas automáticas ao servidor e quaisquer outras ações que não queira que sejam disparadas pelo push em segundo plano.

