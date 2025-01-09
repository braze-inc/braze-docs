{% if include.channel=="in-app messages" %}
Braze は、HTML アプリ内メッセージのアニメーションGIF およびSVG イメージの表示をデフォルトでサポートしています。他のすべてのアプリ内メッセージには、カスタムイメージライブラリが必要です。
{% else %}
Braze で、{{ include.channel }} を使ってアニメーションGIF を表示するには外部画像ライブラリが必要です。
{% endif %}

{% alert note %}
この記事の例はGIF に固有ですが、統合しているカスタムイメージライブラリがSVG ファイルをサポートしている場合は、このガイドに従ってSVG を表示することもできます。
{% endalert %}

## カスタムイメージライブラリの統合 {#gifs-delegate-integration}

Braze では、カスタムイメージライブラリを使用して、{{ include.channel }} でアニメーションGIF を表示することができます。

以下の例では[Glide][gifs-67] を使用していますが、GIF をサポートするイメージライブラリには互換性があります。

### ステップ 1: イメージローダーデリゲートの作成

Image Loader デリゲートは、次のメソッドを実装する必要があります。

* [`getInAppMessageBitmapFromUrl()`][gifs-71]
* [`getPushBitmapFromUrl()`][gifs-72]
* [`renderUrlIntoCardView()`][gifs-73]
* [`renderUrlIntoInAppMessageView()`][gifs-74]
* [`setOffline()`][gifs-70]

以下の統合例は、Braze Android SDK に含まれる[Glide 統合サンプルアプリ][gifs-65] のものです。

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

### ステップ2:イメージローダーデリゲートの設定

Braze SDK は、[`setBrazeImageLoader`][gifs-66] で設定された任意のカスタム画像ローダーを使用します。カスタム・アプリケーション・サブクラスでカスタム・イメージ・ローダーを設定することをお勧めします。

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

## Jetpack Compose によるカスタムイメージのロード

Jetpack Compose で画像の読み込みをオーバーライドするには、`imageComposable` に値を渡します。この関数は`Card` を取り、必要な画像と修飾子をレンダリングします。または、`ContentCardsList` の`customCardComposer` を使用してカード全体をレンダリングすることもできます。

次の例では、`imageComposable` 関数にリストされているカードにGlide のCompose ライブラリが使用されています。

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
