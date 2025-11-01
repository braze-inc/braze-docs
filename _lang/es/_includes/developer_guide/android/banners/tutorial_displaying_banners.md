## Requisitos previos

Antes de empezar este tutorial, comprueba que tu SDK de Braze cumple los requisitos mínimos de la versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Mostrar banners para el SDK de Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Visualización de banners Android" %}

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

Paso
líneas-MainApplication.kt=12

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-MainApplication.kt=21-28

#### 2\. Suscribirse a las actualizaciones del Banner

Utiliza `subscribeToBannersUpdates()` para registrar un controlador que se ejecute cada vez que se actualice un Banner.

Paso
líneas-MainActivity.kt=10-14

#### 3\. Refresca tus colocaciones

Tras inicializar el SDK de Braze, llama a `requestBannersRefresh(["PLACEMENT_ID"])` para obtener el último contenido de Banner para esa ubicación.

Paso
líneas-banners.xml=15-19

#### 4\. Define `BannerView` en tu `banners.xml`

En `banners.xml`, declara un elemento `<com.braze.ui.banners.BannerView>` con `app:placementId="PLACEMENT_ID"`. Braze utilizará este elemento para insertar tu Banner en tu IU.

{% endscrolly %}
