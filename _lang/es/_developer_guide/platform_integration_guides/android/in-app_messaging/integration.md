---
nav_title: Integración
article_title: Integración de mensajes dentro de la aplicación para Android y FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo integrar la mensajería dentro de la aplicación en tu aplicación Android o FireOS."
channel:
  - in-app messages
search_rank: 2
---

# Integración de mensajes dentro de la aplicación

> Este artículo de referencia explica cómo integrar la mensajería dentro de la aplicación en tu aplicación Android o FireOS.

[Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) te ayudan a hacer llegar contenido a tus usuarios sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con varios diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca.

Para ver ejemplos de mensajes dentro de la aplicación, consulta nuestros [casos de estudio](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Tipos de mensajes dentro de la aplicación

Braze ofrece varios tipos de mensajes dentro de la aplicación predeterminados, cada uno personalizable con mensajes, imágenes, iconos [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), acciones de clic, análisis, estilos editables y esquemas de color. Los tipos disponibles actualmente son:

- [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html)
- [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html)
- [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)
- [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)

También es posible definir tu [propia vista personalizada de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory).

Todos los mensajes dentro de la aplicación implementan la interfaz [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) que define el comportamiento y las características básicas de todos los mensajes dentro de la aplicación. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) es una clase abstracta que implementa `IInAppMessage` y proporciona la implementación básica de los mensajes dentro de la aplicación. Todas las clases de mensajes dentro de la aplicación son subclases de `InAppMessageBase`.

Además, hay una subinterfaz de `IInAppMessage` llamada [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)que añade [botones de](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) acción de clic y habilitación de análisis, así como texto de cabecera y un botón de cierre.

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el mensaje `clickAction` también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) es una clase abstracta que implementa `IInAppMessageImmersive` y proporciona la implementación básica de los mensajes dentro de la aplicación `immersive`. Los mensajes dentro de la aplicación `Modal` son una subclase de `InAppMessageImmersiveBase`.

Los mensajes HTML dentro de la aplicación son instancias [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html), que implementan [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), otra subclase de `IInAppMessage`.

### Comportamientos esperados según el tipo de mensaje

Así es como se ven tus usuarios al abrir uno de nuestros tipos predeterminados de mensajes dentro de la aplicación.

{% tabs local %}
{% tab Deslizamiento hacia arriba %}
[`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) Los mensajes dentro de la aplicación se llaman así porque "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Un mensaje dentro de la aplicación que se desliza desde la parte inferior de la pantalla de un teléfono y que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en la esquina inferior derecha de una página Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Son útiles para una mensajería más crítica y pueden equiparse con dos botones de acción de clic y habilitación de análisis.

![Un mensaje modal dentro de la aplicación en el centro de una pantalla de teléfono que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en el centro de una página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}
[`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen, y la mitad inferior muestra texto y hasta dos botones de acción de clic y habilitación de análisis.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono y que dice: "Los humanos somos complicados. La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en gran parte en el centro de una página web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab HTML personalizado %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) Los mensajes dentro de la aplicación son útiles para crear contenido de usuario totalmente personalizado. El contenido HTML de los mensajes dentro de la aplicación, definido por el usuario, se muestra en `WebView` y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. <br><br>Los mensajes dentro de la aplicación Android admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK Braze Web desde dentro de tu HTML, consulta nuestras <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">mejores prácticas</a> para más detalles.

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Definir tipos de mensajes dentro de la aplicación personalizados

El objeto de mensaje dentro de la aplicación `slideup` extiende [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).
Los mensajes de tipo `full` y `modal` se extienden [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html). Extender una de estas clases te da la opción de añadir funcionalidad personalizada a tus mensajes dentro de la aplicación generados localmente.

## Integración {#in-app-messaging-integration}

### Paso 1: Registro del administrador de mensajes dentro de la aplicación Braze

La visualización de mensajes dentro de la aplicación es gestionada por la clase [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Cada actividad de tu aplicación debe registrarse en `BrazeInAppMessageManager` para que pueda añadir vistas de mensajes dentro de la aplicación a la jerarquía de vistas. Hay dos formas de conseguirlo:

#### Integración de devolución de llamada del ciclo de vida de la actividad (recomendado)

La [integración de la devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) gestiona automáticamente el registro de mensajes dentro de la aplicación; no se requiere ninguna integración adicional. Esta es la integración recomendada para gestionar el registro de mensajes dentro de la aplicación.

#### Registro manual de mensajes dentro de la aplicación

{% alert warning %}
Si hiciste la integración del ciclo de vida de la actividad, *no* debes hacer una integración manual de mensajes dentro de la aplicación.
{% endalert %}

Primero, en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()), llama a [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

A continuación, en cada actividad en la que se puedan mostrar mensajes dentro de la aplicación, [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) debe llamarse en la página `onResume()` de esa actividad:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

Por último, en todas las actividades en las que [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) se haya llamado a [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) debe llamarse en la `onPause()` de esa actividad:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### Paso 2: Lista de bloqueo del administrador de mensajes dentro de la aplicación (opcional)

En tu integración, puedes requerir que ciertas actividades de tu aplicación no muestren mensajes dentro de la aplicación. La [integración de la devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) proporciona una forma sencilla de conseguirlo.

El siguiente código de ejemplo añade dos actividades a la lista de bloqueo de registro de mensajes dentro de la aplicación, `SplashActivity` y `SettingsActivity`:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```

{% endtab %}
{% endtabs %}


