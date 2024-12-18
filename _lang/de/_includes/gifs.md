{% if include.channel=="in-app messages" %}
Braze unterstützt standardmäßig die Anzeige von animierten GIFs und SVG-Bildern für HTML-In-App-Nachrichten. Für alle anderen In-App-Nachrichten ist eine eigene Bildbibliothek erforderlich.
{% else %}
Braze benötigt eine externe Bildbibliothek, um animierte GIFs mit {{ include.channel }} anzuzeigen.
{% endif %}

{% alert note %}
Die Beispiele in diesem Artikel beziehen sich zwar speziell auf GIFs, aber Sie können diese Anleitung auch für die Anzeige von SVGs verwenden, wenn die von Ihnen integrierte benutzerdefinierte Bildbibliothek SVG-Dateien unterstützt.
{% endalert %}

## Integration einer benutzerdefinierten Bildbibliothek {#gifs-delegate-integration}

Braze bietet die Möglichkeit, eine benutzerdefinierte Bildbibliothek zu verwenden, um animierte GIFs mit {{ include.channel }} anzuzeigen.

Obwohl das folgende Beispiel [Glide][gifs-67] verwendet, ist jede Bildbibliothek, die GIFs unterstützt, kompatibel.

### Schritt 1: Erstellen des Image Loader Delegaten

Der Image Loader-Delegat muss die folgenden Methoden implementieren:

* [`getInAppMessageBitmapFromUrl()`][gifs-71]
* [`getPushBitmapFromUrl()`][gifs-72]
* [`renderUrlIntoCardView()`][gifs-73]
* [`renderUrlIntoInAppMessageView()`][gifs-74]
* [`setOffline()`][gifs-70]

Das folgende Integrationsbeispiel stammt aus der [Glide-Integrationsbeispiel-App][gifs-65], die im Braze Android SDK enthalten ist.

{% tabs %}
{% tab JAVA %}

```java
public class GlideBrazeImageLoader implements IBrazeImageLoader {
  private static final String TAG = GlideBrazeImageLoader.class.getName();

  private RequestOptions mRequestOptions = new RequestOptions();

  @Override
  public void renderUrlIntoCardView(Context context, Card card, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds);
  }

  @Override
  public void renderUrlIntoInAppMessageView(Context context, IInAppMessage inAppMessage, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds);
  }

  @Override
  public Bitmap getPushBitmapFromUrl(Context context, Bundle extras, String imageUrl, BrazeViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  @Override
  public Bitmap getInAppMessageBitmapFromUrl(Context context, IInAppMessage inAppMessage, String imageUrl, BrazeViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  private void renderUrlIntoView(Context context, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
    Glide.with(context)
        .load(imageUrl)
        .apply(mRequestOptions)
        .into(imageView);
  }

  private Bitmap getBitmapFromUrl(Context context, String imageUrl, BrazeViewBounds viewBounds) {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get();
    } catch (Exception e) {
      Log.e(TAG, "Failed to retrieve bitmap at url: " + imageUrl, e);
    }
    return null;
  }

  @Override
  public void setOffline(boolean isOffline) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideBrazeImageLoader : IBrazeImageLoader {
  companion object {
    private val TAG = GlideBrazeImageLoader::class.qualifiedName
  }

  private var mRequestOptions = RequestOptions()

  override fun renderUrlIntoCardView(context: Context, card: Card, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds)
  }

  override fun renderUrlIntoInAppMessageView(context: Context, inAppMessage: IInAppMessage, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView, viewBounds)
  }

  override fun getPushBitmapFromUrl(context: Context, extras: Bundle, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  override fun getInAppMessageBitmapFromUrl(context: Context, inAppMessage: IInAppMessage, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  private fun renderUrlIntoView(context: Context, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
    Glide.with(context)
        .load(imageUrl)
        .apply(mRequestOptions)
        .into(imageView)
  }

  private fun getBitmapFromUrl(context: Context, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get()
    } catch (e: Exception) {
      Log.e(TAG, "Failed to retrieve bitmap at url: $imageUrl", e)
    }

    return null
  }

  override fun setOffline(isOffline: Boolean) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline)
  }
}
```

{% endtab %}
{% endtabs %}

### Schritt 2: Einstellen des Delegaten für den Bildlader

Das Braze SDK verwendet jeden benutzerdefinierten Bildlader, der mit [`setBrazeImageLoader`][gifs-66]. Wir empfehlen, den benutzerdefinierten Bildlader in einer benutzerdefinierten Anwendungsunterklasse festzulegen:

{% tabs %}
{% tab JAVA %}

```java
public class GlideIntegrationApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Braze.getInstance(context).setBrazeImageLoader(new GlideBrazeImageLoader());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideIntegrationApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    Braze.getInstance(context).appboyImageLoader = GlideBrazeImageLoader()
  }
}
```

{% endtab %}
{% endtabs %}

## Benutzerdefiniertes Laden von Bildern mit Jetpack Compose

Um das Laden von Bildern mit Jetpack Compose außer Kraft zu setzen, können Sie einen Wert an `imageComposable` übergeben. Diese Funktion nimmt eine `Card` und rendert das Bild und die benötigten Modifikatoren. Alternativ können Sie auch `customCardComposer` von `ContentCardsList` verwenden, um die gesamte Karte zu rendern.

Im folgenden Beispiel wird die Compose-Bibliothek von Glide für die in der Funktion `imageComposable` aufgeführten Karten verwendet:

```kotlin
ContentCardsList(
    cardStyle = ContentCardStyling(
        imageComposable = { card ->
            when (card.cardType) {
                CardType.CAPTIONED_IMAGE -> {
                    val captionedImageCard = card as CaptionedImageCard
                    GlideImage(
                        modifier = Modifier
                            .fillMaxWidth()
                            .wrapContentHeight()
                            .run {
                                if (captionedImageCard.aspectRatio > 0) {
                                    aspectRatio(captionedImageCard.aspectRatio)
                                } else {
                                    this
                                }
                            },
                        contentScale = ContentScale.Crop,
                        model = captionedImageCard.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                CardType.IMAGE -> {
                    val imageOnlyCard = card as ImageOnlyCard
                    GlideImage(
                        modifier = Modifier
                            .fillMaxWidth()
                            .run {
                                if (imageOnlyCard.aspectRatio > 0) {
                                    aspectRatio(imageOnlyCard.aspectRatio)
                                } else {
                                    this
                                }
                            },
                        contentScale = ContentScale.Crop,
                        model = imageOnlyCard.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                CardType.SHORT_NEWS -> {
                    val shortNews = card as ShortNewsCard
                    GlideImage(
                        modifier = Modifier
                            .width(100.dp)
                            .height(100.dp),
                        model = shortNews.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                else -> Unit
            }
        }
    )
)
```

[gifs-56]: http://developer.android.com/reference/android/app/Application.html
[gifs-59]: https://github.com/braze-inc/braze-android-sdk#version-support
[gifs-60]: http://developer.android.com/guide/topics/manifest/application-element.html#nm
[gifs-61]: https://github.com/braze-inc/braze-android-sdk/tree/master/droidboy
[gifs-64]: https://github.com/braze-inc/braze-android-sdk/tree/master/droidboy
[gifs-65]: https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration
[gifs-66]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html
[gifs-67]: https://bumptech.github.io/glide/
[gifs-70]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html
[gifs-71]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html
[gifs-72]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html
[gifs-73]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html
[gifs-74]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html
