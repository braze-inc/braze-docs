---
nav_title: Integración de SDK para Android
article_title: Integración de SDK para Android y FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo integrar el SDK de Android en tu aplicación Android o FireOS."
search_rank: 4
---

# Integración de SDK de Android

> Este artículo de referencia explica cómo integrar el SDK de Android en tu aplicación Android o FireOS. La instalación del SDK de Braze te proporcionará una funcionalidad básica de análisis y mensajes dentro de la aplicación con los que podrás interactuar con tus usuarios.

{% alert note %}
Para obtener un rendimiento óptimo en Android 12, recomendamos actualizar a [la versión 13.1.2+ del SDK para Android de Braze ](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) lo antes posible. Para más información, consulta nuestra [guía de actualización a Android 12]({{site.baseurl}}/android_12/).
{% endalert %}

## Paso 1: Integrar la biblioteca Braze

El SDK para Android de Braze puede integrarse opcionalmente sin componentes de interfaz de usuario. Sin embargo, las tarjetas de contenido y la mensajería dentro de la aplicación quedarán inoperativas a menos que pases los datos personalizados a una interfaz de usuario exclusivamente diseñada por ti. Además, las notificaciones push no funcionarán porque nuestro código de gestión de notificaciones push está en la biblioteca de interfaz de usuario. Es importante tener en cuenta que estos elementos de la IU son totalmente personalizables. Recomendamos encarecidamente la integración de estas características. Consulta las [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) y la documentación [de mensajes dentro de la]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) aplicación para obtener una lista de las ventajas de utilizar cada canal o herramienta.

### Integración básica

Para acceder a las características de mensajería de Braze, debes integrar la biblioteca de IU. Consulta las siguientes instrucciones de Android Studio para integrar la biblioteca de interfaz de usuario en función de tu IDE:

#### Añadir dependencia de Braze

Añade la dependencia `android-sdk-ui` a la página `build.gradle` de tu aplicación. 

Si utilizas alguna funcionalidad de ubicación o de geovalla Braze, incluye también `android-sdk-location` en la dirección `build.gradle` de tu aplicación.

{% alert important %}
Si utilizas un SDK de Android no nativo (por ejemplo, Flutter, Cordova, Unity, etc.), ese SDK ya tiene la dependencia `android-sdk-ui` para la versión correcta del SDK de Android. No actualices esa versión manualmente.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

El siguiente ejemplo muestra dónde colocar la línea de dependencia en tu `build.gradle`. Ten en cuenta que la versión utilizada en el ejemplo es una versión antigua. Visita [Lanzamientos del SDK para Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) de Braze para obtener la versión más actualizada del SDK para Android de Braze.

![Android studio mostrando el "build.gradle", con el código de dependencia añadido al final del archivo.]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Realiza la sincronización de Gradle

Asegúrate de realizar una sincronización Gradle para construir tu proyecto e incorporar las [adiciones de dependencia](#add-braze-dependency).

![Un banner en Android Studio que dice: "Los archivos Gradle han cambiado desde la última sincronización del proyecto. Puede ser necesaria una sincronización del proyecto para que el IDE funcione correctamente. Sincroniza ahora."]({% image_buster /assets/img_archive/androidstudio3.png %})

## Paso 2: Configura el SDK de Braze en braze.xml

{% alert note %}
A partir de diciembre de 2019, ya no se entregarán puntos finales personalizados; si tienes un punto final personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos finales disponibles</a>.
{% endalert %}

Ahora que las bibliotecas están integradas, debes crear un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. Si estás en un clúster de datos específico o tienes un punto final personalizado preexistente, tienes que especificar también el punto final en tu archivo `braze.xml`. 

El contenido de ese archivo debe parecerse al siguiente fragmento de código. Asegúrate de sustituir `YOUR_APP_IDENTIFIER_API_KEY` por el identificador que se encuentra en la página **Administrar configuración** del panel de Braze. Inicia sesión en [dashboard.braze.com](https://dashboard.braze.com) para encontrar la [dirección de tu clúster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Paso 3: Añade los permisos necesarios a AndroidManifest.xml
Ahora que has añadido tu clave de API, tienes que añadir los siguientes permisos a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Con el lanzamiento de Android M, Android pasó de un modelo de permisos durante el tiempo de instalación a un modelo de permisos durante el tiempo de ejecución. Sin embargo, ambos permisos son normales y se conceden automáticamente si figuran en el manifiesto de la aplicación. Para más información, visita la [documentación sobre permisos](https://developer.android.com/training/permissions/index.html) de Android.
{% endalert %}

## Paso 4: Seguimiento de las sesiones de usuario en Android

### Integración de devolución de llamada del ciclo de vida de la actividad

Las llamadas a `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)y al registro `InAppMessageManager` se gestionan opcionalmente de forma automática.

#### Registra las devoluciones de llamada del ciclo de vida de la actividad

Añade el siguiente código al método `onCreate()` de tu clase `Application`:

{% tabs %}
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

{% endtab %}
{% endtabs %}

Consulta nuestra documentación de referencia del SDK para obtener más información sobre los parámetros disponibles para [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Paso 5: Habilitar el seguimiento de ubicación

Si quieres habilitar la recopilación de ubicaciones de Braze, actualiza tu archivo `braze.xml` para incluir `com_braze_enable_location_collection` y asegúrate de que su valor es `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir de la versión 3.6.0 del SDK para Android de Braze, la recopilación de ubicaciones de Braze está desactivada por defecto.
{% endalert %}

## Integración de SDK completa

Ahora Braze podrá recopilar [los datos especificados de tu aplicación]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) y tu integración básica debería estar completa.

Visita los siguientes artículos para habilitar [el seguimiento de eventos personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/), la [mensajería push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), [las tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) y la línea completa de características de Braze.

