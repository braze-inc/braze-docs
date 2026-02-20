## 前提条件

このチュートリアルを開始する前に、Braze SDKが最低バージョン要件を満たしていることを確認してください。

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Android SDKのバナーの表示

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger

public class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.logLevel = Log.VERBOSE

        // Configure Braze with your SDK key and endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        // Subscribe to Banner updates
        Braze.getInstance(this)
            .subscribeToBannersUpdates { update ->
                for (banner in update.banners) {
                    Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                    // Add any custom banner logic you'd like
                }
            }
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Inflate the XML layout
        setContentView(R.layout.banners)

        // Refresh placements
        Braze.getInstance(this)
            .requestBannersRefresh(
                listOf("top-1")
            )
    }
}
```

```xml file=banners.xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal">

        <!-- Banner placement -->
        <com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:placementId="top-1" />

        <!-- ...the rest of your activity layout -->

    </LinearLayout>
</ScrollView>
```

!!step
lines-MainApplication.kt=12

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-MainApplication.kt=21-28

#### 2\.バナー更新の購読

`subscribeToBannersUpdates()` を使用して、バナーが更新d のときに実行されるハンドラーを登録します。

!!step
lines-MainActivity.kt=10-14

#### 3\.配置を更新する

Braze SDKを初期化した後、`requestBannersRefresh(["PLACEMENT_ID"])` を呼び出して、そのプレイスメントの最新のバナーコンテンツを取得します。

!!step
lines-banners.xml=15-19

#### 4. あなたの中で`BannerView`を定義する `banners.xml`

`banners.xml`で、`<com.braze.ui.banners.BannerView>`要素を`app:placementId="PLACEMENT_ID"`で宣言します。Braze は、この要素を使用してバナーをユーザーインターフェイスに挿入します。

{% endscrolly %}
