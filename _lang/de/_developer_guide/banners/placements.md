---
nav_title: Platzierungen verwalten
article_title: Verwalten Sie Bannerplatzierungen für das Braze SDK
description: "Lernen Sie, wie Sie Bannerplatzierungen im Braze SDK erstellen und verwalten, einschließlich des Zugriffs auf ihre eindeutigen Eigenschaften und der Protokollierung von Impressionen."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Verwalten Sie Bannerplatzierungen

> Lernen Sie, wie Sie Bannerplatzierungen im Braze SDK erstellen und verwalten, einschließlich des Zugriffs auf ihre eindeutigen Eigenschaften und der Protokollierung von Impressionen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/developer_guide/banners).

## Über Anfragen zur Platzierung {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Erstellen einer Platzierung

### Voraussetzungen

Dies sind die Mindestversionen des SDK, die für die Erstellung von Bannerplatzierungen erforderlich sind:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Schritt 2: Aktualisieren Sie die Platzierungen in Ihrer App {#requestBannersRefresh}

Die Platzierungen können durch den Aufruf der unten beschriebenen Aktualisierungsmethoden aufgefrischt werden. Diese Platzierungen werden automatisch zwischengespeichert, wenn die Sitzung eines Nutzers abläuft oder wenn Sie die Bezeichner:innen mit der Methode `changeUser` ändern.

{% alert tip %}
Aktualisieren Sie die Platzierungen so schnell wie möglich, um Verzögerungen beim Herunterladen oder Anzeigen von Bannern zu vermeiden.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
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
Wenn Sie Banner mit den SDK-Methoden in dieser Anleitung einfügen, werden alle Analytics-Ereignisse (wie Impressionen und Klicks) automatisch verarbeitet und Impressionen werden nur protokolliert, wenn das Banner zu sehen ist.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab Javascript %}
Wenn Sie Vanilla JavaScript mit dem Internet Braze SDK verwenden, benutzen Sie [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) um auf Updates für die Platzierung zu warten und rufen dann [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) um sie zu holen.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Wenn Sie React mit dem Internet Braze SDK verwenden, richten Sie [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) innerhalb eines `useEffect` Hooks ein und rufen [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) nachdem Sie Ihren Listener registriert haben.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
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
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
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

### Schritt 4: Einfügen unter Verwendung der ID der Platzierung {#insertBanner}

{% alert tip %}
Eine vollständige Schritt-für-Schritt-Anleitung finden Sie unter [Anzeigen eines Banners nach Platzierungs-ID]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Erstellen Sie ein Containerelement für das Banner. Stellen Sie sicher, dass Sie die Breite und Höhe festlegen.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Wenn Sie Vanilla JavaScript mit dem Internet Braze SDK verwenden, rufen Sie die [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) Methode auf, um den inneren HTML-Code des Container-Elements zu ersetzen.

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

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Wenn Sie React mit dem Internet Braze SDK verwenden, rufen Sie die [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) Methode mit einem `ref` auf, um das innere HTML des Container-Elements zu ersetzen.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Um Impressionen zu tracken, rufen Sie bitte `insertBanner` für `isControl` auf. Anschließend können Sie Ihren Container ausblenden oder einklappen.
{% endalert %}

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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Um das Banner im Java-Code abzurufen, verwenden Sie Folgendes:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Sie können Banner im Layout Ihrer Android-Ansichten erstellen, indem Sie diese XML-Datei einfügen:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
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

Um das Banner in Kotlin abzurufen, verwenden Sie Folgendes:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
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
Für die einfachste Integration fügen Sie das folgende JavaScript XML (JSX) Snippet in Ihre Ansichtshierarchie ein und geben nur die ID der Platzierung an.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Um das Datenmodell des Banners in React Native abzurufen oder um zu prüfen, ob diese Platzierung im Cache Ihres Nutzers:in vorhanden ist, verwenden Sie:

```javascript
const banner = await Braze.getBanner("global_banner");
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
Für die einfachste Integration fügen Sie das folgende Widget in Ihre Ansichtshierarchie ein und geben nur die ID der Platzierung an.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Mit der Methode `getBanner` können Sie prüfen, ob diese Platzierung im Cache Ihres Nutzer:in vorhanden ist.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
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

### Schritt 5: Senden Sie ein Testbanner (optional) {#handling-test-cards}

Bevor Sie eine Kampagne starten, können Sie [ein Testbanner versenden]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), um Ihre Integration zu überprüfen. Testbanner werden in einem separaten Cache gespeichert und bleiben bei Neustarts der App nicht erhalten. Es ist zwar keine zusätzliche Einrichtung erforderlich, aber Ihr Gerät muss in der Lage sein, Push-Benachrichtigungen im Vordergrund zu empfangen, damit es den Test anzeigen kann.

{% alert note %}
Testbanner sind wie alle anderen Banner, nur dass sie bei der nächsten App-Sitzung wieder entfernt werden.
{% endalert %}

## Impressionen protokollieren

Braze protokolliert automatisch Impressionen für Banner, die angezeigt werden, wenn Sie SDK-Methoden zum Einfügen eines Banners verwenden - Sie müssen also keine Impressionen manuell tracken.

## Abmessungen und Größenangaben

Hier erfahren Sie, was Sie über die Abmessungen und die Größe von Bannern wissen müssen:

- Der Composer erlaubt Ihnen zwar die Vorschau von Bannern in verschiedenen Größen, aber diese Informationen werden nicht gespeichert oder an das SDK gesendet.
- Der HTML-Code nimmt die gesamte Breite des Containers ein, in dem er dargestellt wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.

## Angepasste Eigenschaften {#custom-properties}

Sie können angepasste Eigenschaften aus Ihrer Banner-Kampagne verwenden, um Key-Value-Daten über das SDK abzurufen und das Verhalten oder Aussehen Ihrer App zu ändern. Sie könnten zum Beispiel:

- Senden Sie Metadaten für Ihre Analytics oder Integrationen von Drittanbietern.
- Verwenden Sie Metadaten wie z.B. ein `timestamp` oder JSON-Objekt, um bedingte Logik zu triggern.
- Steuern Sie das Verhalten eines Banners auf der Grundlage von enthaltenen Metadaten wie `ratio` oder `format`.

### Voraussetzungen

Sie müssen [angepasste Eigenschaften]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties) zu Ihrer Banner Kampagne [hinzufügen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties). Außerdem sind dies die Mindestversionen des SDKs, die für den Zugriff auf angepasste Eigenschaften erforderlich sind:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Zugriff auf angepasste Eigenschaften

Um auf die angepassten Eigenschaften eines Banners zuzugreifen, verwenden Sie eine der folgenden Methoden, basierend auf dem im Dashboard definierten Typ der Eigenschaft. Wenn der Schlüssel nicht mit einer Eigenschaft dieses Typs übereinstimmt oder nicht vorhanden ist, gibt die Methode `null` zurück.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object propertyßß
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}
