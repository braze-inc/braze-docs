## About GIFs

Braze offers the ability to use a custom image library to display animated GIFs. Although the example below uses [Glide](https://bumptech.github.io/glide/), any image library that supports GIFs is compatible.

## Integrating a custom image library

### Step 1: Creating the image loader delegate

The Image Loader delegate must implement the following methods:

* [`getInAppMessageBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html)
* [`getPushBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html)
* [`renderUrlIntoCardView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html)
* [`renderUrlIntoInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html)
* [`setOffline()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html)

The integration example below is taken from the [Glide integration sample app](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration) included with the Braze Android SDK.

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

### Step 2: Setting the image loader delegate

The Braze SDK will use any custom image loader set with [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html). We recommend setting the custom image loader in a custom application subclass:

{% tabs %}
{% tab JAVA %}

```java
public class GlideIntegrationApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Braze.getInstance(context).setImageLoader(new GlideBrazeImageLoader());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideIntegrationApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    Braze.getInstance(context).imageLoader = GlideBrazeImageLoader()
  }
}
```

{% endtab %}
{% endtabs %}

## Custom Image Loading with Jetpack Compose

To override image loading with Jetpack Compose, you can pass in a value to [`imageComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-808910455%2FProperties%2F-1725759721). This function will take a `Card` and render the image and the modifiers needed. Alternatively, you can use `customCardComposer` of `ContentCardsList` to render the entire card.

In the following example, Glide's Compose library is used for the cards listed in the `imageComposable` function:

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
