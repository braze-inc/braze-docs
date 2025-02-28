---
nav_title: Banner-Cards
article_title: Bannerkarten für das Braze SDK
hidden: true
description: "Dieser Referenzartikel beschreibt Banner-Cards und die Integration dieses Features in das Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Bannerkarten einbinden

> Ähnlich wie [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) werden Banner Cards direkt in Ihre App oder Website eingebettet, so dass Sie die Benutzer mit einem Erlebnis ansprechen können, das sich natürlich anfühlt. Sie sind eine schnelle und nahtlose Lösung, um personalisierte Nachrichten für Ihre Nutzer zu erstellen und gleichzeitig die Reichweite anderer Kanäle (wie E-Mail oder Push-Benachrichtigungen) zu erhöhen.

{% alert important %}
Banner-Cards befinden sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Voraussetzungen

Bevor Sie Banner-Cards integrieren können, müssen Sie [Banner-Card-Platzierungen]({{site.baseurl}}/developer_guide/banner_cards/creating_placements) in Ihrer App erstellen.

Außerdem sind die folgenden SDK-Mindestversionen für die Verwendung von Banner-Cards erforderlich:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Bannerkarten einbinden

### Schritt 2: Aktualisieren Sie die Platzierungen in Ihrer App {#requestBannersRefresh}

Platzierungen können bei jeder Sitzung angefordert werden und werden automatisch zwischengespeichert, wenn die Sitzung eines Benutzers abläuft oder wenn Sie identifizierte Benutzer mit der Methode `changeUser` ändern.

{% alert tip %}
Aktualisieren Sie die Platzierungen so schnell wie möglich, um Verzögerungen beim Herunterladen oder Anzeigen von Bannern zu vermeiden.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```
{% endtab %}
{% tab Java %}
```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
 Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Schritt 3: Auf Updates achten {#subscribeToBannersUpdates}

{% alert tip %}
Wenn Sie Banner mit den SDK-Methoden in dieser Anleitung einfügen, werden alle Analytics-Events automatisch verarbeitet. Wenn Sie den HTML-Code manuell rendern möchten, [teilen Sie uns dies bitte mit](mailto:banners-feedback@braze.com).
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
})

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
    for (banner in update.banners) {
      Log.d(TAG, "Received banner: " + banner.placementId)
    }
}
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Schritt 4: Karten nach Platzierungs-ID einfügen {#insertBanner}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");

    // choose where in the DOM you want to insert the banner HTML
    const container = document.getElementById("global-banner-container");

    // Insert the banner which replacees the innerHTML of that container
    braze.insertBanner(globalBanner, container);

    // Special handling if the user is part of a Control Variant
    if (globalBanner.isControl) {
        // hide or collapse the container
        container.style.display = 'none';
    }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])

```

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(placementId: "global_banner", braze: braze)
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(placementId: "global_banner", braze: braze)
}
```
{% endtab %}
{% tab Java %}
Um das Banner im Java-Code abzurufen, verwenden Sie Folgendes:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Sie können Banner-Cards im Layout von Android Views erstellen, indem Sie diesen XML-Code einfügen:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
Um das Banner in Kotlin abzurufen, verwenden Sie Folgendes:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

Wenn Sie Android Views verwenden, geben Sie folgenden XML-Code ein:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Wenn Sie Jetpack Compose verwenden, können Sie dies nutzen:

```kotlin
Banner(placementId = "global_banner")
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Analytics

Sie müssen sich keine Gedanken um das manuelle Tracking von Impressionen machen. Braze verarbeitet automatisch die Protokollierung aller Impressionen, wenn Sie die SDK-Methoden zum Einfügen von Banner-Cards verwenden.

Wenn Sie den HTML-Code in einer angepassten Ansicht parsen und rendern müssen, [kontaktieren Sie uns bitte](mailto:banners-feedback@braze.com).

{% details Weitere Informationen zum manuellen Tracking von Impressionen %}

{% alert important %}
Eine Anpassung für Ihre Integration ist wahrscheinlich unnötig, daher sollten Sie sich den folgenden Schritt gut überlegen.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
  // do something with the html
  // then log an impression when the HTML is in view
  braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
// First, get the Banner object:
var globalBanner: Braze.Banner?
brazeClient.braze()?.banners.getBanner(for: "global_banner", { banner in
  globalBanner = banner
})

// Then log the impression on the Banner.
globalBanner?.context?.logImpression()
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).logBannerImpression(banner.getPlacementId());
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).logBannerImpression(banner.placementId)
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

{% enddetails %}

## Abmessungen und Größenangaben

Hier finden Sie einige Informationen zu den Abmessungen und der Größe von Bannerkarten:

- Sie können im Composer zwar eine Vorschau der Banner in verschiedenen Größen anzeigen, aber die Informationen werden weder gespeichert noch an das SDK gesendet.
- Der HTML-Code nimmt die gesamte Breite des Containers ein, in dem er dargestellt wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.
