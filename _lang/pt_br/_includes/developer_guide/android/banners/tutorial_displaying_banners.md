## Pré-requisitos

Antes de iniciar este tutorial, verifique se o SDK do Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibição de banners para o Android SDK

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

!!!etapa
linhas-MainApplication.kt=12

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!!etapa
Linhas -MainApplication.kt=21-28

#### 2\. Assine as atualizações do Banner

Use `subscribeToBannersUpdates()` para registrar um manipulador que é executado sempre que um banner é atualizado.

!!!etapa
linhas-MainActivity.kt=10-14

#### 3\. Atualize suas colocações

Depois de inicializar o SDK do Braze, chame `requestBannersRefresh(["PLACEMENT_ID"])` para buscar o conteúdo mais recente do Banner para esse posicionamento.

!!!etapa
Linhas -banners.xml=15-19

#### 4\. Defina `BannerView` em seu `banners.xml`

Em `banners.xml`, declare um elemento `<com.braze.ui.banners.BannerView>` com `app:placementId="PLACEMENT_ID"`. O Braze usará esse elemento para inserir seu banner em sua UI.

{% endscrolly %}
