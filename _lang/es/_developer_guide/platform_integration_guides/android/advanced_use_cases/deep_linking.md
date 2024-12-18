---
nav_title: Vinculación en profundidad
article_title: Vinculación en profundidad para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Este artículo explica cómo implementar el delegado universal de vinculación en profundidad para tu aplicación de Android o FireOS, así como ejemplos de cómo establecer una vinculación en profundidad con la configuración de la aplicación."

---

# Vínculos profundos

> Como parte del [proceso de implementación de tu SDK para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links), configurarás la capacidad de tu aplicación para utilizar vínculos en profundidad. Este artículo proporciona ejemplos adicionales de casos de uso de los vínculos profundos.

Para obtener información introductoria sobre los vínculos profundos, consulta el [artículo de nuestra Guía del usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% alert note %}
Este artículo incluye información sobre la Fuente de noticias, que está siendo obsoleta. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Delegado universal de vínculos profundos

El SDK de Android ofrece la posibilidad de establecer un único objeto delegado para gestionar de forma personalizada todos los vínculos profundos abiertos por Braze a través de tarjetas de contenido, mensajes dentro de la aplicación y notificaciones push.

Tu objeto delegado debe implementar la interfaz [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html) y configurarse mediante la función [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html). En la mayoría de los casos, el delegado debe establecerse en la página `Application.onCreate()` de tu aplicación.

A continuación se muestra un ejemplo de anulación del comportamiento predeterminado [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) con indicadores de intención personalizados y un comportamiento personalizado para las URL de YouTube:

{% tabs %}
{% tab JAVA %}

```java
public class CustomDeeplinkHandler implements IBrazeDeeplinkHandler {
  private static final String TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler.class);

  @Override
  public void gotoNewsFeed(Context context, NewsfeedAction newsfeedAction) {
    newsfeedAction.execute(context);
  }

  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    String uri = uriAction.getUri().toString();
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.setUseWebView(false);
    }

    CustomUriAction customUriAction = new CustomUriAction(uriAction);
    customUriAction.execute(context);
  }

  public static class CustomUriAction extends UriAction {

    public CustomUriAction(@NonNull UriAction uriAction) {
      super(uriAction);
    }

    @Override
    protected void openUriWithActionView(Context context, Uri uri, Bundle extras) {
      Intent intent = getActionViewIntent(context, uri, extras);
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
      if (intent.resolveActivity(context.getPackageManager()) != null) {
        context.startActivity(intent);
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomDeeplinkHandler : IBrazeDeeplinkHandler {

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {
    newsfeedAction.execute(context)
  }

  override fun gotoUri(context: Context, uriAction: UriAction) {
    val uri = uriAction.uri.toString()
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.useWebView = false
    }

    val customUriAction = CustomUriAction(uriAction)
    customUriAction.execute(context)
  }

  class CustomUriAction(uriAction: UriAction) : UriAction(uriAction) {

    override fun openUriWithActionView(context: Context, uri: Uri, extras: Bundle) {
      val intent = getActionViewIntent(context, uri, extras)
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
      if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
      }
    }
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

## Vínculo profundo con la configuración de la aplicación

Para permitir que los vínculos profundos abran directamente la configuración de tu aplicación, necesitarás una página personalizada `BrazeDeeplinkHandler`. En el siguiente ejemplo, la presencia de un par clave-valor personalizado llamado `open_notification_page` hará que el vínculo profundo abra la página de configuración de la aplicación:

{% tabs %}
{% tab JAVA %}

```java
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(new IBrazeDeeplinkHandler() {
  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    final Bundle extras = uriAction.getExtras();
    if (extras.containsKey("open_notification_page")) {
      Intent intent = new Intent();
      intent.setAction("android.settings.APP_NOTIFICATION_SETTINGS");
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

      //for Android 5-7
      intent.putExtra("app_package", context.getPackageName());
      intent.putExtra("app_uid", context.getApplicationInfo().uid);

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.getPackageName());
      context.startActivity(intent);
    }
  }

  @Override
  public void gotoNewsFeed(Context context, NewsfeedAction newsfeedAction) {}
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(object : IBrazeDeeplinkHandler {
  override fun gotoUri(context: Context, uriAction: UriAction) {
    val extras = uriAction.extras
    if (extras.containsKey("open_notification_page")) {
      val intent = Intent()
      intent.action = "android.settings.APP_NOTIFICATION_SETTINGS"
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK

      //for Android 5-7
      intent.putExtra("app_package", context.packageName)
      intent.putExtra("app_uid", context.applicationInfo.uid)

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.packageName)
      context.startActivity(intent)
    }
  }

  override fun gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {}
})
```

{% endtab %}
{% endtabs %}

## Establecimiento de vínculos profundos con el canal de noticias {#Android_Deep_Advance}

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Para establecer un vínculo profundo con el canal de noticias de Braze desde una notificación push, [crea un vínculo profundo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links) para tu actividad en el canal de noticias.

A continuación, cuando configures tu campaña de notificaciones push (ya sea a través del [panel]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) o de [la API]({{site.baseurl}}/api/endpoints/messaging/)), configura la notificación para que navegue hasta el vínculo profundo de tu fuente de noticias.

## Actividad WebView personalizada {#Custom_Webview_Activity}

De forma predeterminada, cuando Braze abre vínculos profundos a sitios web dentro de la aplicación, los gestiona [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html). Para cambiar esto:

**1\.** Crea una nueva Actividad que maneje la URL de destino de `Intent.getExtras()` con la clave `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`. Consulta [`BrazeWebViewActivity.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt) para ver un ejemplo.<br><br>
**2\.** Añade esa actividad a `AndroidManifest.xml` y establece `exported` en `false`.

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3\.** Configura tu Actividad personalizada en un [objeto constructor de](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) `BrazeConfig`. Crea el constructor y pásalo a [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721) en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class)
    ...
    .build();
Braze.configure(this, brazeConfig);
```

 {% endtab %}
 {% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class.java)
    ...
    .build()
Braze.configure(this, brazeConfig)
```

 {% endtab %}
 {% endtabs %}


