## Voraussetzungen

Bevor Sie mit diesem Tutorial beginnen, überprüfen Sie, ob Ihr Braze SDK die Mindestanforderungen erfüllt:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Anzeige von Bannern für das Internet SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Anzeigen von Bannern im Internet" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!Schritt
Zeilen-index.js=5

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-index.js=8-23

#### 2\. Banner Updates abonnieren

Verwenden Sie `subscribeToBannersUpdates()`, um einen Handler zu registrieren, der immer dann ausgeführt wird, wenn ein Banner aktualisiert wird. Rufen Sie innerhalb des Handlers `braze.getBanner("global_banner")` auf, um die letzte Platzierung zu erhalten.

!Schritt
Zeilen-index.js=15-22

#### 3\. Fügen Sie das Banner ein und behandeln Sie Kontrollgruppen

Verwenden Sie `braze.insertBanner(banner, container)`, um ein Banner einzufügen, wenn es zurückgegeben wird. Damit Ihr Layout übersichtlich bleibt, blenden Sie Banner aus oder ein, die zu einer Kontrollgruppe gehören (zum Beispiel, wenn `isControl` `true` ist).

!Schritt
Zeilen-index.js=25

#### 4\. Aktualisieren Sie Ihre Banner

Rufen Sie nach der Initialisierung des SDK `requestBannersRefresh(["global_banner", ...])` auf, um sicherzustellen, dass die Banner zu Beginn jeder Sitzung aktualisiert werden.

Sie können diese Funktion auch jederzeit aufrufen, um die Bannerplatzierungen später zu aktualisieren.

!Schritt
Zeilen-main.html=3

#### 5\. Fügen Sie einen Container für Ihr Banner hinzu

Fügen Sie in Ihrem HTML ein neues Element `<div>` hinzu und geben Sie ihm einen kurzen, bannerbezogenen `id`, wie z.B. `global-banner-container`. Braze verwendet diese `<div>`, um Ihr Banner auf der Seite einzufügen.

{% endscrolly %}
