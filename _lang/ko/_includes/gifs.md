{% if include.channel=="in-app messages" %}
Braze는 HTML 인앱 메시지에 대해 기본적으로 애니메이션 GIF 및 SVG 이미지 표시를 지원합니다. 다른 모든 인앱 메시지의 경우 사용자 지정 이미지 라이브러리가 필요합니다.
{% else %}
Braze에서 {{ include.channel }}로 애니메이션 GIF를 표시하려면 외부 이미지 라이브러리가 필요합니다.
{% endif %}

{% alert note %}
이 글의 예시는 GIF를 다루지만 통합하려는 커스텀 이미지 라이브러리가 SVG 파일을 지원하는 경우 이 가이드에 따라 SVG를 표시할 수도 있습니다.
{% endalert %}

## 사용자 지정 이미지 라이브러리 통합 {#gifs-delegate-integration}

Braze는 사용자 지정 이미지 라이브러리를 사용하여 {{ include.channel }} 로 애니메이션 GIF를 표시하는 기능을 제공합니다.

아래 예시에서는 [글라이드][gifs-67]를 사용했지만, GIF를 지원하는 모든 이미지 라이브러리가 호환됩니다.

### 1단계: 이미지 로더 위임 만들기

이미지 로더 위임은 다음 메서드를 구현해야 합니다.

* [`getInAppMessageBitmapFromUrl()`][gifs-71]
* [`getPushBitmapFromUrl()`][gifs-72]
* [`renderUrlIntoCardView()`][gifs-73]
* [`renderUrlIntoInAppMessageView()`][gifs-74]
* [`setOffline()`][gifs-70]

아래 연동 예시는 Braze Android SDK에 포함된 [Glide 연동 샘플 앱][gifs-65]에서 가져온 것입니다.

{% tabs %}
{% tab 자바 %}

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
{% tab 코틀린 %}

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

### 2단계: 이미지 로더 위임 설정

Braze SDK는 [`setBrazeImageLoader`][gifs-66]로 설정된 모든 커스텀 이미지 로더를 사용합니다. 사용자 정의 애플리케이션 하위 클래스에서 사용자 정의 이미지 로더를 설정하는 것이 좋습니다:

{% tabs %}
{% tab 자바 %}

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
{% tab 코틀린 %}

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

## Jetpack Compose으로 커스텀 이미지 로딩

Jetpack Compose로 이미지 로딩을 재정의하려면 `imageComposable`에 값을 전달하면 됩니다. 이 함수는 `Card`를 받아 이미지와 필요한 수정자를 렌더링합니다. 또는 `ContentCardsList` 의 `customCardComposer`를 사용하여 전체 카드를 렌더링할 수 있습니다.

다음 예시에서는 `imageComposable` 함수에 나열된 카드에 글라이드의 작성 라이브러리를 사용했습니다.

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
