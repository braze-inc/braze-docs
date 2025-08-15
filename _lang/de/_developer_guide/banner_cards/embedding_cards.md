---
nav_title: Karten einbetten
article_title: Einbinden von Bannerkarten für das Braze SDK
description: "Erfahren Sie, wie Sie Banner Cards für das Braze SDK einbinden."
platform:
  - iOS
  - Android
  - Web
  
---

# Bannerkarten einbinden

> Erfahren Sie, wie Sie mit dem Braze SDK Bannerkarten einbinden können, um Nutzer:innen ein natürliches Engagement zu bieten. Weitere allgemeine Informationen finden Sie unter [Über Bannerkarten]({{site.baseurl}}/developer_guide/banner_cards/).

{% alert important %}
Banner-Cards befinden sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Voraussetzungen

Dies sind die Mindestversionen des SDK, die Sie benötigen, um Banner Cards zu verwenden:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Einbinden einer Bannerkarte

{% multi_lang_include banners/creating_placements.md %}

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
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  data => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map(banner => banner.placementId),
    );
  },
);
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
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Schritt 4: Einbetten unter Verwendung der ID der Platzierung {#insertBanner}

{% tabs %}
{% tab JavaScript %}

Erstellen Sie ein Containerelement für das Banner. Stellen Sie sicher, dass Sie die Breite und Höhe festlegen.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

Als nächstes verwenden Sie die [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) Methode, um das innere HTML des Container-Elements zu ersetzen.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
    baseUrl: "sdk-base-url",
    allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");
    if (!globalBanner) {
        return;
    }

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
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
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

Wenn Sie [die neue Architektur von React Native](https://reactnative.dev/architecture/landing-page) verwenden, müssen Sie `BrazeBannerView` als Fabric-Komponente in Ihrem `AppDelegate.mm` registrieren.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```

Um das Datenmodell der Banner Card in React Native zu erhalten, verwenden Sie:

```javascript
const banner = await Braze.getBanner("global_banner");
```

Sie können die Methode `getBanner` verwenden, um zu prüfen, ob diese Platzierung im Cache Ihres Nutzer:in vorhanden ist. Für die einfachste Integration fügen Sie jedoch das folgende JavaScript-XML-Snippet (JSX) in Ihre Ansichtshierarchie ein und geben nur die ID der Platzierung an.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
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
Um das Datenmodell der Banner Card in Flutter zu erhalten, verwenden Sie:

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

Sie können die Methode `getBanner` verwenden, um zu prüfen, ob diese Platzierung im Cache Ihres Nutzer:in vorhanden ist. Für die einfachste Integration fügen Sie jedoch das folgende Widget in Ihre Ansichtshierarchie ein und geben nur die ID der Platzierung an.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Schritt 5: Senden Sie eine Testkarte (optional) {#handling-test-cards}

Bevor Sie [eine Kampagne starten]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/), können Sie eine Testbannerkarte versenden, um die Integration zu überprüfen. Testkarten werden in einem separaten Zwischenspeicher gespeichert und bleiben nicht über Neustarts der App hinweg erhalten. Es ist zwar keine zusätzliche Einrichtung erforderlich, aber Ihr Gerät muss in der Lage sein, Push-Benachrichtigungen im Vordergrund zu empfangen, damit es die Testkarte anzeigen kann.

{% alert note %}
Testbannerkarten sind wie alle anderen Banner, nur dass sie bei der nächsten App-Sitzung wieder entfernt werden.
{% endalert %}

## Protokollieren von Analytics

Braze protokolliert Impressionen automatisch, wenn Sie SDK-Methoden zum Einfügen einer Bannerkarte verwenden - Sie müssen Impressionen also nicht manuell tracken. Wenn Sie das HTML in einer angepassten Ansicht parsen und rendern müssen, kontaktieren Sie uns unter [banners-feedback@braze.com](mailto:banners-feedback@braze.com).

## Abmessungen und Größenangaben

Hier finden Sie einige Informationen zu den Abmessungen und der Größe von Bannerkarten:

- Sie können im Composer zwar eine Vorschau der Banner in verschiedenen Größen anzeigen, aber die Informationen werden weder gespeichert noch an das SDK gesendet.
- Der HTML-Code nimmt die gesamte Breite des Containers ein, in dem er dargestellt wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.
