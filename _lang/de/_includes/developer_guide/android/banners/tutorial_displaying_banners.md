## Voraussetzungen

Bevor Sie mit diesem Tutorial beginnen, überprüfen Sie, ob Ihr Braze SDK die Mindestanforderungen erfüllt:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Anzeige von Bannern für das Android SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Anzeigen von Bannern Android" %}

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

!Schritt
Zeilen-MainApplication.kt=12

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-MainApplication.kt=21-28

#### 2\. Banner Updates abonnieren

Verwenden Sie `subscribeToBannersUpdates()`, um einen Handler zu registrieren, der immer dann ausgeführt wird, wenn ein Banner aktualisiert wird.

!Schritt
Zeilen-MainActivity.kt=10-14

#### 3\. Aktualisieren Sie Ihre Praktika

Nach der Initialisierung des Braze SDK rufen Sie `requestBannersRefresh(["PLACEMENT_ID"])` auf, um die neuesten Banner-Inhalte für diese Platzierung abzurufen.

!Schritt
Zeilen-banners.xml=15-19

#### 4\. Definieren Sie `BannerView` in Ihrem `banners.xml`

In `banners.xml` deklarieren Sie ein `<com.braze.ui.banners.BannerView>` Element mit `app:placementId="PLACEMENT_ID"`. Braze verwendet dieses Element, um Ihr Banner in Ihr UI einzufügen.

{% endscrolly %}
