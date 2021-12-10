---
nav_title: Liens profonds
article_title: Liens profonds pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 0
description: "Cet article couvre comment implémenter le délégué universel de liaison profonde pour votre application Android, ainsi que des exemples sur la façon de créer un lien profond vers les paramètres de l'application ou un fil d'actualité."
---

# Liaison profonde d'Android

## Délégué du lien profond universel

Le SDK Android fournit la possibilité de définir un seul objet délégué pour gérer sur mesure tous les liens profonds ouverts par Braze sur les Cartes de Contenu, messages intégrés à l'application et notifications push.

Votre objet délégué devrait implémenter l'interface [`IAppboyNavigator`][udl-3] et être défini en utilisant [`AppboyNavigator.setAppboyNavigator()`][udl-2]. Dans la plupart des cas, le délégué doit être défini dans votre application `Application.onCreate()`.

Ce qui suit est un exemple d'outrepasser le comportement par défaut [`UriAction`][udl-1] avec des drapeaux d'intention personnalisés et un comportement personnalisé pour les URL YouTube.

{% tabs %}
{% tab JAVA %}

```java
CustomNavigator de classe publique implémente IAppboyNavigator {
  privé static final String TAG = BrazeLogger.getBrazeLogTag(CustomAppboyNavigator. lass);

  @Override
  public vide gotoNewsFeed(Contexte contextuel, NewsfeedAction newsfeedAction) {
    newsfeedAction. xecute(contexte);
  }

  @Override
  public nul(Contexte contextuel, gotoUri) UriAction Action) {
    String uri = uriAction. etUri().toString();
    // Ouvre les URL YouTube dans l'application YouTube et pas notre application
    if (!StringUtils. sNullOrBlank(uri) && uri.contains("youtube. om")) {
      uriAction. etUseWebView(false);
    }

    customUriAction = new CustomUriAction(uriAction);
    customUriAction. xecute(contexte);
  }

  de classe statique publique CustomUriAction extends UriAction {

    public CustomUriAction(@NonNull UriAction uriAction) {
      super(uriAction);
    }

    @Override
    annulé openUriWithActionView(Contexte contextuel Uri uri, Bundle extras) {
      Intent intent = getActionViewIntent(context, uri, extras);
      intentions. etFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
      if (intent. esolveActivity(context.getPackageManager()) != null) {
        contexte. tartActivity(intent);
      } else {
        BrazeLogger. (TAG, "Impossible de trouver une activité appropriée pour ouvrir un lien profond " + uri + ". );
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomNavigator : IAppboyNavigator {

  outrepasser gotoNewsFeed(context: Context, newsfeedAction: NewsfeedAction) {
    newsfeedAction. xecute(contexte)
  }

  écraser gotoUri(context: Context, uriAction: UriAction) {
    uri val = uriAction.uri. oString()
    // Ouvre les URL YouTube dans l'application YouTube et non notre application
    if (!StringUtils. sNullOrBlank(uri) && uri.contains("youtube. om")) {
      uriAction. seWebView = false
    }

    customUriAction val = CustomUriAction(uriAction)
    customUriAction. xecute(contexte)
  }

  class CustomUriAction(uriAction: UriAction) : UriAction(uriAction) {

    override fun openUriWithActionView(context: Context, uri: Uri, extras: Bundle) {
      intention val = getActionViewIntent(context, uri, extras)
      intention. lags = Intent.FLAG_ACTIVITY_NEW_TASK ou Intenent. LAG_ACTIVITY_CLEAR_TOP ou Intent.FLAG_ACTIVITY_SINGLE_TOP
      if (intent.resolveActivity(context.packageManager) != null) {
        context . tartActivity(intent)
      } else {
        BrazeLogger. (TAG, "Impossible de trouver une activité appropriée pour ouvrir le lien profond $uri.")
      }
    }
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(CustomAppboyNavigator::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

## Liaison profonde vers les paramètres de l'application

Pour permettre à des liens profonds d'ouvrir directement les paramètres de votre application, vous aurez besoin d'un AppboyNavigator personnalisé. Dans l'exemple suivant, la présence d'une paire clé-valeur personnalisée appelée `open_notification_page` fera ouvrir la page de configuration de l'application.

{% tabs %}
{% tab JAVA %}

```java

  AppboyNavigator. etAppboyboyNavigator(new IAppboyNavigator() { 
 @Override
  public void gotoUri(Contexte contextuel, UriAction uriAction) {
    bundle final extras = uriAction. etExtras();
    si (extras. ontainsKey("open_notification_page")) {
      Intendant = new Intent();
      intent.setAction("android.settings. PP_NOTIFICATION_SETTINGS");
      intent.setFlags(Intent. LAG_ACTIVITY_NEW_TASK);

      //pour une intention Android 5-7
      . utExtra("app_package", context.getPackageName());
      intent.putExtra("app_uid", context.getApplicationInfo(). id);

      // pour Android 8 et supérieur
      intent.putExtra("android.provider.extra. PP_PACKAGE", context.getPackageName());
      contexte. tartActivity(intention);
    }
  }

  @Override
  public void gotoNewsFeed(Contexte contextuel NewsfeedAction newsfeedAction) {}
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyNavigator.setAppAppboyNavigator(object : IAppboyNavigator {
  override fun gotoUri(context: Context, uriAction: UriAction) {
    val extras = uriAction. xtras
    si (extras. ontainsKey("open_notification_page")) {
      intention val = Intent()
      intent.action = "android.settings. PP_NOTIFICATION_SETTINGS"
      intent.flags = Intent. LAG_ACTIVITY_NEW_TASK

      //pour l'intention Android 5-7
      . utExtra("app_package", context.packageName)
      intent.putExtra("app_uid", context.applicationInfo. id)

      // pour Android 8 et supérieur
      intent.putExtra("android.provider.extra. PP_PACKAGE", context.packageName)
      contexte. tartActivity(intent)
    }
  }

  remplacent gotoNewsFeed(contexte: Context, newsfeedAction : NewsfeedAction) {}
})
```

{% endtab %}
{% endtabs %}

## Liens profonds vers le fil d'actualité {#Android_Deep_Advance}

Pour créer un lien profond vers le flux d'actualités Braze à partir d'une notification push, [créez un lien profond personnalisé][1] pour votre activité de flux d'actualités.

Ensuite, lorsque vous configurez votre campagne de notification push (soit via le tableau de bord [][2] ou [API][3]), configurez la notification pour accéder à votre lien de fond de fil d'actualité.

## Activité de WebView personnalisée {#Custom_Webview_Activity}

Par défaut, lorsque des approfondissements de site web sont ouverts dans l'application par Braze, ils sont gérés par [`BrazeWebViewActivity`][udl-4]. Pour changer ceci :

**1.** Créez une nouvelle activité qui gère l'URL cible à partir de `Intent.getExtras()` avec la clé `com.appboy.Constants.APPBOY_WEBVIEW_URL_EXTRA`. Voir [`BrazeWebViewActivity.java`][udl-8] pour un exemple.<br><br> **2.** Ajoutez cette activité à `AndroidManifest.xml` et définissez `exporté` à `false`.

```xml
<activity
    android:name=".MyCustomWebViewActivity"
    android:exported="false" />
```

**3.** Définissez votre activité personnalisée dans un objet constructeur `BrazeConfig` [][udl-6]. Construisez le constructeur et passez le à [Braze.configure()][udl-5] dans votre [`Application.onCreate()`][udl-7]

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class)
...
    .build();
Braze.configure(ceci, brazeConfig);
```

 {% endtab %}
 {% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class.java)
...
    .build()
Braze.configure(ceci, brazeConfig)
```

 {% endtab %}
 {% endtabs %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-4-add-deep-links
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[3]: {{site.baseurl}}/api/endpoints/messaging/
[udl-1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/actions/UriAction.html
[udl-2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/AppboyNavigator.html#setAppboyNavigator-com.appboy.IAppboyNavigator-
[udl-3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/IAppboyNavigator.html
[udl-4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/BrazeWebViewActivity.html
[udl-5]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#configure-android.content.Context-com.appboy.configuration.BrazeConfig-
[udl-6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html
[udl-6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html
[udl-7]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[udl-8]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.java
