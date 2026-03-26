---
nav_title: "Von Content-Cards migrieren"
article_title: "Von Content-Cards zu Bannern migrieren"
description: "Erfahren Sie, wie Sie von Content-Cards zu Bannern migrieren können, einschließlich Code-Beispielen für alle unterstützten SDKs, Einschränkungen und Vorteilen."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Von Content-Cards zu Bannern migrieren

> Dieser Leitfaden unterstützt Sie bei der Migration von Content-Cards zu Bannern für Anwendungsfälle im Bereich des bannerartigen Messaging. Banner eignen sich ideal für Inline-Anzeigen, persistente In-App- und Internet-Nachrichten, die an bestimmten Stellen in Ihrer App erscheinen.

## Warum zu Bannern migrieren?

- Wenn Ihr Entwicklerteam angepasste Content-Cards erstellt oder wartet, kann die Migration zu Bannern diese laufenden Investitionen reduzieren. Mit Bannern können Marketer die UI direkt steuern, wodurch Entwickler:innen für andere Aufgaben entlastet werden.
- Wenn Sie neue Homepage-Nachrichten, Onboarding-Abläufe oder persistente Ankündigungen einführen möchten, empfehlen wir, zunächst mit Bannern zu beginnen, anstatt auf Content-Cards aufzubauen. Sie profitieren von Realtime-Personalisierung, keiner 30-tägigen Ablaufzeit, keiner Größenbeschränkung und nativer Priorisierung vom ersten Tag an.
- Wenn Sie mit der 30-tägigen Ablaufgrenze arbeiten, komplexe Logik zur erneuten Berechtigungsprüfung verwalten oder von veralteter Personalisierung frustriert sind, löst Banners diese Probleme auf native Weise.

Banner bieten gegenüber Content-Cards mehrere Vorteile für das Messaging im Banner-Stil:

### Beschleunigte Produktion

- **Reduzierter laufender technischer Support erforderlich**: Marketer können mithilfe eines Drag-and-Drop-Editors und angepasstem HTML individuelle Nachrichten erstellen, ohne dass sie für die Anpassung die Unterstützung von Entwickler:innen benötigen.
- **Flexible Anpassungsmöglichkeiten**: Entwerfen Sie direkt im Editor, verwenden Sie HTML oder nutzen Sie vorhandene Datenmodelle mit angepassten Eigenschaften.

### Verbesserte Benutzererfahrung

- **Dynamische Content-Updates**: Banner aktualisieren Liquid Logic und die Berechtigung bei jeder Aktualisierung, um sicherzustellen, dass die Nutzer:innen stets die relevantesten Inhalte sehen.
- **Native Platzierungsunterstützung**: Nachrichten werden in bestimmten Kontexten und nicht in einem Feed angezeigt, wodurch eine bessere kontextuelle Relevanz gewährleistet wird.
- **Native Priorisierung**: Steuerung der Anzeigereihenfolge ohne angepasste Logik, wodurch die Verwaltung der Nachrichtenhierarchie vereinfacht wird.

### Persistenz

- **Keine Verfallsfrist**: Bannerkampagnen haben keine 30-tägige Ablaufgrenze wie Content-Cards, was eine echte Persistenz der Nachrichten ermöglicht.

## Wann sollte die Migration erfolgen?

Erwägen Sie eine Migration zu Bannern, wenn Sie Content-Cards für folgende Zwecke verwenden:

- Homepage-Banner, Aktionen auf Produktseiten, Checkout-Angebote
- Persistente Navigationsansagen oder Sidebar-Nachrichten
- Always-on-Nachrichten, die länger als 30 Tage angezeigt werden
- Nachrichten, bei denen Sie eine Realtime-Personalisierung und eine Eignungsprüfung wünschen

## Wann sollten Sie Content-Cards beibehalten?

Verwenden Sie weiterhin Content-Cards, wenn Sie Folgendes benötigen:

- **Feed-Erlebnisse:** Jeder Anwendungsfall, der mehrere scrollbare Nachrichten oder einen kartenbasierten „Posteingang" umfasst.
- **Besondere Features:** Nachrichten, die Connected-Content oder Aktionscodes erfordern, da Banner diese nicht nativ unterstützen.
- **Getriggerte Zustellung:** Anwendungsfälle, die eine API-gesteuerte oder aktionsbasierte Zustellung erfordern. Obwohl Banner keine API-gesteuerte oder aktionsbasierte Zustellung unterstützen, bedeutet die Realtime-Berechtigungsevaluierung, dass Nutzer:innen bei jeder Aktualisierung sofort anhand ihrer Segmentzugehörigkeit qualifiziert oder disqualifiziert werden.

## Migrationsleitfaden

### Voraussetzungen

Stellen Sie vor der Migration sicher, dass das Braze SDK die Mindestversionsanforderungen erfüllt:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Updates abonnieren

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Inhalt anzeigen

{% alert note %}
Content-Cards können manuell mit angepasster UI-Logik gerendert werden, während Banner nur mit den vorgefertigten SDK-Methoden gerendert werden können.
{% endalert %}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Analytics protokollieren (angepasste Implementierungen)

{% alert note %}
Sowohl Content-Cards als auch Banner erfassen automatisch Analytics, wenn ihre Standard-UI-Komponenten verwendet werden. Die folgenden Beispiele beziehen sich auf angepasste Implementierungen, bei denen Sie Ihre eigene UI erstellen.
{% endalert %}

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}

{% alert important %}
Analytics werden bei der Verwendung von `insertBanner()` automatisch erfasst. Bei der Verwendung von `insertBanner()` sollte keine manuelle Protokollierung verwendet werden.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Bei der Verwendung von BannerView werden Analytics automatisch erfasst. Bei der Verwendung von BannerView sollte keine manuelle Protokollierung durchgeführt werden.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Bei der Verwendung von BannerUIView werden Analytics automatisch erfasst. Die manuelle Protokollierung sollte nicht für die Standard-BannerUIView verwendet werden.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Bei der Verwendung von BrazeBannerView werden Analytics automatisch erfasst. Es ist keine manuelle Protokollierung erforderlich.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
Bei der Verwendung von BrazeBannerView werden Analytics automatisch erfasst. Es ist keine manuelle Protokollierung erforderlich.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Eigenschaften abrufen

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Umgang mit Kontrollgruppen

#### Content-Cards-Ansatz

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Banner-Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Einschränkungen

Beachten Sie bei der Migration von Content-Cards zu Bannern die folgenden Einschränkungen:

### Migration getriggerter Nachrichten

Banner unterstützen ausschließlich geplante Zustellungskampagnen. Um eine Nachricht zu migrieren, die zuvor API-gesteuert oder aktionsbasiert war, konvertieren Sie sie in ein segmentbasiertes Targeting:

- **Beispiel:** Anstatt eine Karte „Profil vervollständigen" mit der API zu triggern, erstellen Sie ein Segment für Nutzer:innen, die sich in den letzten 7 Tagen registriert haben, ihr Profil jedoch noch nicht vervollständigt haben.
- **Realtime-Berechtigung:** Nutzer:innen werden bei jeder Aktualisierung sofort für das Banner qualifiziert oder disqualifiziert, basierend auf ihrer Segmentzugehörigkeit.

### Unterschiede in den Features

| Feature | Content-Cards | Banner |
|---------|--------------|---------|
| **Inhaltsstruktur** |
| Mehrere Karten im Feed | ✅ Unterstützt | ✅ Es können mehrere Platzierungen erstellt werden, um eine karussellähnliche Implementierung zu erzielen. Pro Platzierung wird nur ein Banner zurückgegeben. |
| Mehrere Platzierungen | N/A | ✅ Mehrere Platzierungen werden unterstützt |
| Kartentypen (klassisch, mit Bildunterschrift, nur Bild) | ✅ Mehrere vordefinierte Typen | ✅ Einzelnes HTML-basiertes Banner (flexibler) |
| **Inhaltsverwaltung** |
| Drag-and-Drop-Editor | ❌ Erfordert Entwickler:innen für die Anpassung | ✅ Marketer können ohne technische Unterstützung Inhalte erstellen und Updates durchführen |
| Angepasstes HTML/CSS | ❌ Beschränkt auf die Kartenstruktur | ✅ Vollständige HTML/CSS-Unterstützung |
| Schlüssel-Wert-Paare für die Anpassung | ✅ Für erweiterte Anpassungen erforderlich | ✅ Stark typisierte Schlüssel-Wert-Paare, die als „Eigenschaften" bezeichnet werden, ermöglichen eine erweiterte Anpassung |
| **Persistenz & Ablauf** |
| Ablauf der Karte | ✅ Unterstützt (30-Tage-Limit) | ✅ Unterstützt (ohne Ablaufdatum) |
| Wahre Persistenz | ❌ Maximal 30 Tage | ✅ Unbegrenzte Persistenz |
| **Anzeige & Targeting** |
| Feed-UI | ✅ Standard-Feed verfügbar | ❌ Nur platzierungsbasiert |
| Kontextspezifische Platzierung | ❌ Feed-basiert | ✅ Native Platzierungsunterstützung |
| Native Priorisierung | ❌ Erfordert angepasste Logik | ✅ Integrierte Priorisierung |
| **Benutzerinteraktion** |
| Manuelles Schließen | ✅ Unterstützt | ❌ Nicht unterstützt |
| Gepinnte Karten | ✅ Unterstützt | N/A |
| **Analytics** |
| Automatische Analytics (Standard-UI) | ✅ Unterstützt | ✅ Unterstützt |
| Prioritätssortierung | ❌ Nicht unterstützt | ✅ Unterstützt |
| **Inhaltsupdates** |
| Liquid-Template-Aktualisierung | ❌ Einmal pro Karte beim Senden/Starten | ✅ Aktualisiert bei jeder Aktualisierung |
| Aktualisierung der Berechtigung | ❌ Einmal pro Karte beim Senden/Starten | ✅ Wird bei jeder Sitzung aktualisiert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Produkteinschränkungen

- Bis zu 25 aktive Nachrichten pro Platzierung.
- Bis zu 10 Platzierungs-IDs pro Aktualisierungsanfrage; darüber hinausgehende Anfragen werden gekürzt.

### SDK-Einschränkungen

- Banner werden derzeit auf den Plattformen .NET MAUI (Xamarin), Cordova, Unity, Vega oder TV nicht unterstützt.
- Stellen Sie sicher, dass Sie die in den Voraussetzungen aufgeführten Mindestversionen des SDK verwenden.

## Verwandte Artikel

- [Bannerplatzierungen]({{site.baseurl}}/developer_guide/banners/placements)
- [Anleitung: Anzeige eines Banners anhand der Platzierungs-ID]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Banner-Analytics]({{site.baseurl}}/developer_guide/banners/analytics)
- [Häufig gestellte Fragen zu Bannern]({{site.baseurl}}/developer_guide/banners/faq)