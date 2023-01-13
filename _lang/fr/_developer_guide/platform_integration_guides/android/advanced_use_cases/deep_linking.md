---
nav_title: Création de liens profonds
article_title: Création de liens profonds pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Cet article explique comment implémenter le délégué universel de création de liens profonds pour votre application Android ou FireOS, ainsi que des exemples sur la manière de créer des liens profonds avec des paramètres d’application ou un fil d'actualité."

---

# Création de liens profonds Android

## Délégué universel de lien profond

Le SDK Android offre la possibilité de définir un objet de délégué unique pour personnaliser les liens profonds ouverts par Braze sur les cartes de contenu, les messages in-app et les notifications push.

Votre objet délégué doit implémenter l’interface [`IBrazeDeeplinkHandler`][udl-3] et être défini en utilisant [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`][udl-2]. Dans la plupart des cas, le délégué doit être défini dans le `Application.onCreate()` de l’application.

Voici un exemple de contournement du comportement par défaut [`UriAction`][udl-1] avec des indicateurs d’intention personnalisés et de comportement personnalisé pour les URL YouTube :

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

## Création de liens profonds vers les paramètres d’application

Pour permettre aux liens profonds d’ouvrir directement les paramètres de votre application, vous aurez besoin d’un `BrazeDeeplinkHandler` personnalisé. Dans l’exemple suivant, la présence d’une paire clé-valeur personnalisée appelée `open_notification_page` fera en sorte que le lien profond ouvre la page paramètres de l’application :

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

## Création de liens profonds avec le fil d'actualité {#Android_Deep_Advance}

Pour réaliser un lien profond avec le fil d’actualité de Braze à partir d’une notification push, [créez un lien profond personnalisé][1] pour votre activité de fil d'actualité.

Ensuite, lorsque vous configurez votre campagne de notification push (soit par le biais du [tableau de bord][2] ou de l’[API][3]), configurez la notification pour accéder à votre lien profond de fil d’actualité.

## Activité personnalisée WebView {#Custom_Webview_Activity}

Par défaut, lorsque les liens profonds du site Internet sont ouverts à l’intérieur de l’application par Braze, ils sont gérés par [`BrazeWebViewActivity`][udl-4]. Pour modifier ceci :

**1.** Créez une nouvelle activité qui gère l’URL cible de `Intent.getExtras()` avec la clé `com.appboy.Constants.BRAZE_WEBVIEW_URL_EXTRA`. Consultez [`BrazeWebViewActivity.java`][udl-8] pour un exemple.<br>
<br>

**2.** Ajoutez cette activité à `AndroidManifest.xml` et définir `exported` sur `false`.

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3.** Définissez votre activité personnalisée dans un `BrazeConfig`[objet générateur][udl-6]. Construisez le générateur et transmettez-le à [`Braze.configure()`][udl-5] dans votre [`Application.onCreate()`][udl-7]

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


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-add-deep-links
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[3]: {{site.baseurl}}/api/endpoints/messaging/
[udl-1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html
[udl-2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html
[udl-3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html
[udl-4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html
[udl-5]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/index.html#-1864418529%2FFunctions%2F-1725759721
[udl-6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html
[udl-7]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[udl-8]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.java
