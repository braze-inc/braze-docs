## Délégué universel de lien profond

Le SDK Android offre la possibilité de définir un objet de délégué unique pour personnaliser les liens profonds ouverts par Braze sur les cartes de contenu, les messages in-app et les notifications push.

Votre objet délégué doit implémenter l’interface [`IAppboyNavigator`][udl-3] et être défini en utilisant [`AppboyNavigator.setAppboyNavigator()`][udl-2]. Dans la plupart des cas, le délégué doit être défini dans le `Application.onCreate()` de l’application.

Voici un exemple de contournement du comportement par défaut [`UriAction`][udl-1] avec des indicateurs d’intention personnalisés et un comportement personnalisé pour les URL YouTube. 

{% tabs %}
{% tab JAVA %}

```java
public class CustomNavigator implements IAppboyNavigator {
  private static final String TAG = AppboyLogger.getAppboyLogTag(CustomAppboyNavigator.class);

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
        AppboyLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomNavigator : IAppboyNavigator {

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
        AppboyLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
      }
    }
  }

  companion object {
    private val TAG = AppboyLogger.getAppboyLogTag(CustomAppboyNavigator::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

[udl-1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.actions/-uri-action/index.html
[udl-2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.ui/-appboy-navigator/set-appboy-navigator.html
[udl-3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy/-i-appboy-navigator/index.html
