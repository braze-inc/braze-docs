---
nav_title: "Von Content-Cards migrieren"
article_title: "Migration von Content-Cards zu Bannern"
description: "Erfahren Sie, wie Sie von Content-Cards zu Bannern migrieren können, einschließlich Code-Beispiele für alle unterstützten SDKs, Einschränkungen und Vorteile."
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

# Migration von Content-Cards zu Bannern

> Diese Anleitung hilft Ihnen bei der Migration von Content-Cards zu Bannern für Messaging-Anwendungsfälle im Banner-Stil. Banner sind ideal für persistente In-App- und Internet-Nachrichten, die an bestimmten Stellen in Ihrer Anwendung erscheinen.

## Warum die Migration zu Banners?

- Wenn Ihr Entwicklerteam angepasste Content-Cards erstellt oder pflegt, kann die Migration zu Banners diese laufenden Investitionen reduzieren. Mit Bannern können Marketer das UI direkt steuern und Entwickler:in für andere Aufgaben freistellen.
- Wenn Sie neue Nachrichten für Ihre Homepage, Onboarding-Flows oder persistente Ankündigungen einführen möchten, sollten Sie mit Bannern beginnen, anstatt auf Content-Cards aufzubauen. Profitieren Sie von der Personalisierung in Realtime, der unbegrenzten Gültigkeit von 30 Tagen, der unbegrenzten Größe und der nativen Priorisierung vom ersten Tag an.
- Wenn Sie die 30-tägige Ablauffrist umgehen, eine komplexe Logik für die Wiederzulassung verwalten oder sich über veraltete Personalisierung ärgern müssen, löst Banners diese Probleme von Haus aus.

Banner bieten mehrere Vorteile gegenüber Content-Cards für bannerähnliches Messaging:

### Beschleunigte Produktion

- **Geringerer Bedarf an laufender technischer Unterstützung**: Marketer können angepasste Nachrichten mit einem Drag-and-Drop-Editor und angepasstem HTML erstellen, ohne dass Entwickler:in für die Anpassung benötigt werden.
- **Flexible Anpassungsmöglichkeiten**: Gestalten Sie direkt im Editor, verwenden Sie HTML oder nutzen Sie vorhandene Datenmodelle mit angepassten Eigenschaften.

### Bessere UX

- **Dynamische Updates von Inhalten**: Banner aktualisieren Liquid logic und Eignung bei jeder Aktualisierung, so dass die Nutzer:innen immer die relevantesten Inhalte sehen.
- **Unterstützung bei der Platzierung von Einheimischen**: Nachrichten erscheinen in bestimmten Kontexten und nicht in einem Feed, was eine bessere kontextuelle Relevanz bietet
- **Einheimische Prioritäten**: Kontrolle über die Anzeigereihenfolge ohne angepasste Logik, wodurch die Verwaltung der Nachrichtenhierarchie erleichtert wird

### Persistenz

- **Kein Verfallsdatum**: Banner-Kampagnen haben keine 30-tägige Ablauffrist wie Content-Cards, was eine echte Persistenz der Nachrichten zulässt.

## Wann Sie migrieren sollten

Ziehen Sie eine Migration zu Banners in Betracht, wenn Sie Content-Cards für verwenden:

- Homepage-Helden, Aktionen auf der Produktseite, Angebote an der Kasse
- Persistente Ankündigungen in der Navigation oder Nachrichten in der Seitenleiste
- Immer aktive Nachrichten, die länger als 30 Tage laufen
- Nachrichten, bei denen Sie eine Personalisierung in Realtime und eine Berechtigung wünschen

## Wann Sie Content-Cards behalten sollten

Verwenden Sie bei Bedarf weiterhin Content-Cards:

- **Erfahrungen füttern:** Jeder Anwendungsfall, der mehrere scrollbare Nachrichten oder einen kartenbasierten "Posteingang" beinhaltet.
- **Besondere Features:** Nachrichten, die Connected-Content oder Aktionscodes erfordern, da Banner diese von Haus aus nicht unterstützen.
- **Ausgelöste Zustellung:** Anwendungsfälle, die unbedingt eine API-getriggerte oder aktionsbasierte Zustellung erfordern. Während Banner keine API-getriggerte oder aktionsbasierte Zustellung unterstützen, bedeutet die Bewertung der Eignung in Realtime, dass Nutzer:innen bei jeder Aktualisierung sofort anhand ihrer Segmentzugehörigkeit qualifiziert oder disqualifiziert werden.

## Leitfaden für die Migration

### Voraussetzungen

Stellen Sie vor der Migration sicher, dass Ihr Braze SDK die Mindestanforderungen an die Version erfüllt:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Updates abonnieren

#### Content-Cards Ansatz

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

#### Banner Ansatz

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const globalBanner = braze.getBanner("global_banner");
  if (globalBanner) {
    console.log("Banner received for placement:", globalBanner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val globalBanner = Braze.getInstance(context).getBanner("global_banner")
  if (globalBanner != null) {
    Log.d(TAG, "Banner received for placement: ${globalBanner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "global_banner") { banner in
    if let banner = banner {
      print("Banner received for placement: \(banner.placementId)")
    }
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("global_banner").then(banner => {
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
  braze.getBanner("global_banner").then((banner) {
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
Content-Cards können manuell mit angepasster UI-Logik gerendert werden, während Banner nur mit den Out-of-the-Box SDK-Methoden gerendert werden können.
{% endalert %}

#### Content-Cards Ansatz

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

#### Banner Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="global_banner" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("global_banner"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
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

braze.banners.requestBannersRefresh(placementIds: ["global_banner"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='global_banner'
/>

// Or get banner data
const banner = await Braze.getBanner("global_banner");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "global_banner",
)

// Or get banner data
final banner = await braze.getBanner("global_banner");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% endtabs %}

### Log Analytics (angepasste Implementierungen)

{% alert note %}
Sowohl Content-Cards als auch Banner verfolgen automatisch Analytics, wenn Sie ihre Standard UI-Komponenten verwenden. Die folgenden Beispiele sind für angepasste Implementierungen, bei denen Sie Ihr eigenes UI erstellen.
{% endalert %}

#### Content-Cards Ansatz

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

#### Banner Ansatz

{% tabs %}
{% tab Web %}

{% alert important %}
Analytics werden automatisch getrackt, wenn Sie `insertBanner()` verwenden. Die manuelle Protokollierung sollte nicht verwendet werden, wenn Sie `insertBanner()` verwenden.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([globalBanner]);

// Log click (with optional buttonId)
braze.logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Analytics werden automatisch getrackt, wenn Sie BannerView verwenden. Die manuelle Protokollierung sollte bei der Verwendung von BannerView nicht verwendet werden.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("global_banner");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Analytics werden automatisch getrackt, wenn Sie BannerUIView verwenden. Die manuelle Protokollierung sollte nicht für Standard BannerUIView verwendet werden.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Log impression
braze.banners.logImpression(placementId: "global_banner")

// Log click (with optional buttonId)
braze.banners.logClick(placementId: "global_banner", buttonId: buttonId)

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Analytics werden automatisch getrackt, wenn Sie BrazeBannerView verwenden. Keine manuelle Protokollierung erforderlich.
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
Analytics werden automatisch getrackt, wenn Sie BrazeBannerView verwenden. Keine manuelle Protokollierung erforderlich.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Umgang mit Kontrollgruppen

#### Content-Cards Ansatz

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

#### Banner Ansatz

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  
  // Always call insertBanner to track impression (including control)
  braze.insertBanner(globalBanner, container);
  
  // Hide if control group
  if (globalBanner.isControl) {
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
  placementId = "global_banner"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "global_banner",
)
```
{% endtab %}
{% endtabs %}

## Beschränkungen

Bei der Migration von Content-Cards zu Bannern sollten Sie die folgenden Einschränkungen beachten:

### Migration getriggerter Nachrichten

Banner unterstützen nur Kampagnen mit Zeitplan für die Zustellung. Um eine Nachricht zu migrieren, die zuvor API-getriggert oder aktionsbasiert war, konvertieren Sie sie in segmentbasiertes Targeting:

- **Beispiel:** Anstatt eine Karte "Profil vervollständigen" mit der API zu triggern, erstellen Sie ein Segment für Nutzer:innen, die sich in den letzten 7 Tagen angemeldet, aber ihr Profil nicht vervollständigt haben.
- **Teilnahmeberechtigung in Echtzeit:** Nutzer:innen qualifizieren oder disqualifizieren sich für das Banner sofort bei jeder Aktualisierung auf der Grundlage ihrer Mitgliedschaft in einem Segment.

### Feature Unterschiede

| Feature | Content-Cards | Banner |
|---------|--------------|---------|
| **Inhaltliche Struktur** |
| Mehrere Karten im Feed | ✅ Unterstützt | ✅ Sie können mehrere Platzierungen erstellen, um eine karussellartige Implementierung zu erreichen. Pro Platzierung wird nur ein Banner zurückgegeben. |
| Mehrere Platzierungen | -- | ✅ Mehrere Platzierungen unterstützt |
| Kartentypen (Klassisch, Mit Bildunterschrift, Nur Bild) | ✅ Mehrere vordefinierte Typen | ✅ Einzelner HTML-basierter Banner (flexibler) |
| **Content Management** |
| Drag-and-Drop-Editor | ❌ Benötigt Entwickler:in für die Anpassung | ✅ Marketer können ohne Technik erstellen/aktualisieren |
| Angepasstes HTML/CSS | ❌ Begrenzt auf die Kartenstruktur | Vollständige HTML/CSS-Unterstützung |
| Schlüssel-Wert-Paare für die Anpassung | ✅ Erforderlich für fortgeschrittene Anpassungen | Stark typisierte Schlüssel-Wert-Paare, so genannte "Eigenschaften", für fortgeschrittene Anpassungen |
| **Persistenz & Verfall** |
| Ablauf der Karte | ✅ Unterstützt (30-Tage-Limit) | ✅ Unterstützt (kein Verfallsdatum) |
| Echte Persistenz | ❌ Maximal 30 Tage | ✅ Unbegrenzte Persistenz |
| **Anzeige & Targeting** |
| Feed UI | ✅ Standard Futtermittel verfügbar | ❌ Nur platzierungsbezogen |
| Kontextspezifische Platzierung | ❌ Futtermittelbasiert | ✅ Unterstützung der nativen Platzierung |
| Native Prioritätensetzung | ❌ Benötigt angepasste Logik | ✅ Eingebaute Prioritätensetzung |
| **Nutzer:in Interaktion** |
| Manuelle Entlassung | ✅ Unterstützt | ❌ Nicht unterstützt |
| Gepinnte Karten | ✅ Unterstützt | -- |
| **Analytics** |
| Automatische Analytics (Standard UI) | ✅ Unterstützt | ✅ Unterstützt |
| Prioritätssortierung | ❌ Nicht unterstützt | ✅ Unterstützt | 
| **Contentful Updates** |
| Liquid-Templates aktualisieren | ❌ Einmal pro Karte beim Senden/Launch | ✅ Aktualisiert bei jeder Aktualisierung |
| Berechtigung aktualisieren | ❌ Einmal pro Karte beim Senden/Launch | ✅ Erfrischt bei jeder Sitzung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Einschränkungen des Produkts

- Bis zu 25 aktive Nachrichten pro Platzierung.
- Bis zu 10 IDs pro Aktualisierungsanfrage; darüber hinausgehende Anfragen werden abgeschnitten.

### SDK Einschränkungen

- Banner werden derzeit nicht auf den Plattformen .NET MAUI (Xamarin), Cordova, Unity, Vega oder TV unterstützt.
- Stellen Sie sicher, dass Sie die in den Voraussetzungen aufgeführten Mindestversionen des SDK verwenden.

## Ähnliche Artikel

- [Banner Platzierungen]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Anzeige eines Banners nach Platzierungs-ID]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Banner-Analytik]({{site.baseurl}}/developer_guide/banners/analytics)
- [Banner FAQ]({{site.baseurl}}/developer_guide/banners/faq)

