## Integración del SDK de Android

### Paso 1: Actualiza tu `build.gradle`

En tu `build.gradle`, añade [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) a tu lista de repositorios.

```kotlin
repositories {
  mavenCentral()
}
```

A continuación, añade Braze a tus dependencias.

{% tabs local %}
{% tab sólo base %}
Si no piensas utilizar componentes de interfaz de usuario Braze, añade el siguiente código a tu página `build.gradle`. Sustituye `SDK_VERSION` por la versión actual de tu SDK Braze para Android. Para ver la lista completa de versiones, consulta [el Registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab con componentes ui %}
Si piensas utilizar componentes de interfaz de usuario Braze más adelante, añade el siguiente código a tu sitio `build.gradle`.  Sustituye `SDK_VERSION` por la versión actual de tu SDK Braze para Android. Para ver la lista completa de versiones, consulta [el Registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Configura tu `braze.xml`

{% alert note %}
A partir de diciembre de 2019, ya no se entregarán puntos finales personalizados; si tienes un punto final personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos finales disponibles</a>.
{% endalert %}

Crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. Si estás en un clúster de datos específico o tienes un punto final personalizado preexistente, tienes que especificar también el punto final en tu archivo `braze.xml`. 

El contenido de ese archivo debe parecerse al siguiente fragmento de código. Asegúrate de sustituir `YOUR_APP_IDENTIFIER_API_KEY` por el identificador que se encuentra en la página **Administrar configuración** del panel de Braze. Inicia sesión en [dashboard.braze.com](https://dashboard.braze.com) para encontrar la [dirección de tu clúster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Paso 3: Añadir permisos a `AndroidManifest.xml`

A continuación, añade los siguientes permisos a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Con el lanzamiento de Android M, Android pasó de un modelo de permisos durante el tiempo de instalación a un modelo de permisos durante el tiempo de ejecución. Sin embargo, ambos permisos son normales y se conceden automáticamente si figuran en el manifiesto de la aplicación. Para más información, visita la [documentación sobre permisos](https://developer.android.com/training/permissions/index.html) de Android.
{% endalert %}

### Paso 4: Habilitar la inicialización retardada (opcional)

Para utilizar la inicialización retardada, se requiere la versión mínima del SDK de Braze:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Mientras está habilitada la inicialización retardada, se cancelan todas las conexiones de red, impidiendo que el SDK envíe datos a los servidores Braze.
{% endalert %}

#### Paso 4.1: Actualiza tu `braze.xml`

La inicialización retardada está desactivada por predeterminado. Para habilitarlo, utiliza una de las siguientes opciones:

{% tabs %}
{% tab Archivo XML Braze %}
En el archivo `braze.xml` de tu proyecto, establece `com_braze_enable_delayed_initialization` en `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab En tiempo de ejecución %}
Para habilitar la inicialización retardada en tiempo de ejecución, utiliza el siguiente método.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Paso 4.2: Configurar análisis push (opcional)

Cuando se habilita la inicialización retardada, los análisis push se ponen en cola de forma predeterminada. Sin embargo, puedes optar por [poner explícitamente en cola](#explicitly-queue-push-analytics) o [eliminar](#drop-push-analytics) los análisis push.

##### Cola explícita {#explicitly-queue-push-analytics}

Para poner en cola explícitamente los análisis push, elige una de las siguientes opciones:

{% tabs %}
{% tab Archivo XML Braze %}
En tu archivo `braze.xml`, establece `com_braze_delayed_initialization_analytics_behavior` en `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab En tiempo de ejecución %}
Añade `QUEUE` a tu [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) método:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Drop {#drop-push-analytics}

Para abandonar los análisis push, elige una de las siguientes opciones:

{% tabs %}
{% tab Archivo XML Braze %}
En tu archivo `braze.xml`, establece `com_braze_delayed_initialization_analytics_behavior` en `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab En tiempo de ejecución %}
Añade `DROP` al [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) método:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Paso 4.3: Inicializa manualmente el SDK

Tras el periodo de retardo que hayas elegido, utiliza el método [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) para inicializar manualmente el SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Paso 5: Habilitar el seguimiento de la sesión del usuario

Cuando habilitas el seguimiento de la sesión del usuario, las llamadas a `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)y al registro `InAppMessageManager` pueden gestionarse automáticamente.

Para registrar las devoluciones de llamada del ciclo de vida de la actividad, añade el siguiente código al método `onCreate()` de tu clase `Application`. 

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

Para ver la lista de parámetros disponibles, consulta [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Probar el seguimiento de la sesión

{% alert tip %}
También puedes utilizar [el Depurador SDK]({{site.baseurl}}/developer_guide/debugging) para diagnosticar problemas del SDK.
{% endalert %}

Si tienes problemas durante las pruebas, habilita el [registro detallado](#android_enabling-logs) y utiliza logcat para detectar las llamadas a `openSession` y `closeSession` que faltan en tus actividades.

1. En Braze, ve a **Resumen**, selecciona tu aplicación y, en el desplegable **Mostrar datos para**, elige **Hoy**.
    ![La página "Resumen" en Braze, con el campo "Mostrar datos para" ajustado a "Hoy".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Abre tu aplicación y actualiza el panel de Braze. Comprueba que tus métricas han aumentado en 1.
3. Navega por tu aplicación y comprueba que sólo se ha registrado una sesión en Braze.
4. Envía la aplicación a un segundo plano durante al menos 10 segundos, y luego tráela al primer plano. Comprueba que se ha registrado una nueva sesión.

## Configuraciones opcionales

### Configuración de tiempo de ejecución

Para establecer tus opciones de Braze en código en lugar de tu archivo `braze.xml`, utiliza [la configuración en tiempo de ejecución](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Si existe un valor en ambos lugares, se utilizará en su lugar el valor en tiempo de ejecución. Una vez proporcionadas todas las configuraciones necesarias en tiempo de ejecución, puedes eliminar tu archivo `braze.xml`.

En el siguiente ejemplo, se crea un [objeto constructor](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) y se pasa a [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Ten en cuenta que sólo se muestran algunas de las opciones de ejecución disponibles; consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) para ver la lista completa.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
¿Buscas otro ejemplo? Consulta nuestra [aplicación de ejemplo Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### ID de publicidad de Google

El [ID de publicidad de Google (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) es un ID opcional específico del usuario, anónimo, único y reajustable para publicidad, proporcionado por los servicios de Google Play. GAID ofrece a los usuarios la posibilidad de restablecer su identificador, excluirse voluntariamente de los anuncios basados en intereses dentro de las aplicaciones de Google Play, y proporciona a los desarrolladores un sistema sencillo y estándar para seguir monetizando sus aplicaciones.

El SDK de Braze no recopila automáticamente el ID de publicidad de Google, por lo que debe establecerse manualmente mediante el método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google requiere que el ID de publicidad se recoja en un hilo no-UI.
{% endalert %}


### Seguimiento de la ubicación

Para habilitar la recogida de ubicaciones Braze, configura `com_braze_enable_location_collection` en `true` en tu archivo `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir de la versión 3.6.0 del SDK para Android de Braze, la recopilación de ubicaciones de Braze está desactivada por defecto.
{% endalert %}

### Registro

De manera predeterminada, el nivel de registro del SDK de Braze para Android está predeterminado en `INFO`. Puedes [suprimir estos registros](#android_suppressing-logs) o [establecer un nivel de registro diferente](#android_enabling-logs), como `VERBOSE`, `DEBUG`, o `WARN`.

#### Habilitación de registros

Para ayudar a solucionar problemas en tu aplicación, o reducir los tiempos de respuesta con el soporte de Braze, querrás habilitar los registros detallados para el SDK. Cuando envíes registros detallados al soporte de Braze, asegúrate de que empiezan en cuanto inicias la aplicación y terminan mucho después de que se produzca el problema.

Ten en cuenta que los registros detallados sólo están pensados para tu entorno de desarrollo, por lo que deberás desactivarlos antes de publicar tu aplicación.

{% alert important %}
Habilita los registros detallados antes de cualquier otra llamada en `Application.onCreate()` para asegurarte de que tus registros son lo más completos posible.
{% endalert %}

{% tabs local %}
{% tab Aplicación %}
Para habilitar los registros directamente en tu aplicación, añade lo siguiente al método `onCreate()` de tu aplicación antes de cualquier otro método.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Sustituye `MIN_LOG_LEVEL` por la **Constante** del nivel de registro que quieras establecer como nivel mínimo de registro. Cualquier registro en un nivel `>=` a tu configuración `MIN_LOG_LEVEL` se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` de tu configuración `MIN_LOG_LEVEL`.

| Constante    | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los destacados generales.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Para habilitar los registros en `braze.xml`, añade lo siguiente a tu archivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Sustituye `MIN_LOG_LEVEL` por el **valor** del nivel de registro que quieras establecer como nivel de registro mínimo. Cualquier registro en un nivel `>=` a tu configuración `MIN_LOG_LEVEL` se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` de tu configuración `MIN_LOG_LEVEL`.

| Constante    | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los destacados generales.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Verificar registros detallados

Para verificar que tus registros están configurados en `VERBOSE`, comprueba si `V/Braze` aparece en algún lugar de tus registros. Si lo hace, es que se han habilitado correctamente los registros detallados. Por ejemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Suprimir registros

Para suprimir todos los registros del SDK para Android de Braze, establece el nivel de registro en `BrazeLogger.SUPPRESS` en el método `onCreate()` de tu aplicación _antes que_ en cualquier otro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Múltiples claves de API

El caso de uso más común para múltiples claves de API es separar las claves de API para las variantes de compilación de depuración y de lanzamiento.

Para cambiar fácilmente entre varias claves de API en tus construcciones, te recomendamos que crees un archivo `braze.xml` distinto para cada [variante de construcción](https://developer.android.com/studio/build/build-variants.html) relevante. Una variante de fabricación es una combinación del tipo de fabricación y la variante de producto. Por defecto, los nuevos proyectos de Android se configuran con [los tipos de compilación`debug` y `release` ](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) y sin sabores de producto.

Para cada variante de construcción relevante, crea un nuevo `braze.xml` en el directorio `src/<build variant name>/res/values/`. Cuando se compile la variante de compilación, utilizará la nueva clave de API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Para saber cómo configurar la clave de API en tu código, consulta [Configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).
{% endalert %}

### Mensaje exclusivo dentro de la aplicación TalkBack

En cumplimiento de las [directrices de accesibilidad de Android](https://developer.android.com/guide/topics/ui/accessibility), el SDK para Android de Braze ofrece Android Talkback de forma predeterminada. Para garantizar que sólo se lea en voz alta el contenido de los mensajes dentro de la aplicación -sin incluir otros elementos de la pantalla, como la barra de título de la aplicación o la navegación-, puedes habilitar el modo exclusivo para TalkBack.

Para habilitar el modo exclusivo para mensajes dentro de la aplicación:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 y ProGuard

La configuración de [la reducción de código](https://developer.android.com/build/shrink-code) se incluye automáticamente con tu integración Braze.

Las aplicaciones cliente que ofuscan el código Braze deben almacenar archivos de mapeado de liberación para que Braze pueda interpretar las trazas de pila. Si quieres seguir conservando todo el código Braze, añade lo siguiente a tu archivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
