---
nav_title: Integration
article_title: News Feed Integration für Android und FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel befasst sich mit den verschiedenen News Feed-Kartentypen, den verschiedenen verfügbaren kartenspezifischen Eigenschaften und einem Beispiel für eine benutzerdefinierte Integration für Ihre Android- oder FireOS-Anwendung."
channel:
  - news feed
  
---

# Integration von News Feeds

> Dieser Referenzartikel befasst sich mit den verschiedenen News Feed-Kartentypen, den verschiedenen verfügbaren kartenspezifischen Eigenschaften und einem Beispiel für eine benutzerdefinierte Integration für Ihre Android- oder FireOS-Anwendung.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

In Android ist der Newsfeed als [Fragment](http://developer.android.com/guide/components/fragments.html) implementiert, das im Braze Android UI-Projekt verfügbar ist. In der [Google-Dokumentation zu Fragmenten ](https://developer.android.com/guide/fragments#Adding "Android-Dokumentation: Fragmente") finden Sie Informationen darüber, wie Sie ein Fragment zu einer Aktivität hinzufügen.

Die Klasse `BrazeFeedFragment` wird automatisch aktualisiert, zeigt den Inhalt des Newsfeeds an und protokolliert die Analytics zur Nutzung. Die Karten, die im News Feed eines Benutzers erscheinen können, werden auf dem Braze-Dashboard festgelegt.

## Karten-Typen

Braze verfügt über fünf einzigartige Kartentypen: Bannerbild, Bildunterschrift, Textankündigung und Kurznachrichten. Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

### Eigenschaften der Basiskartenmodelle

Das [Basiskartenmodell](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) bietet grundlegende Verhaltensweisen für alle Karten.  

|Eigenschaft|Beschreibung|
|---|---|
| `getId()` | Gibt die von Braze eingestellte ID der Karte zurück. |
| `getViewed()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte vom Benutzer gelesen oder ungelesen ist. |
| `getExtras()` | Gibt eine Karte mit Schlüssel-Wert-Extras für diese Karte zurück. |
| `setViewed(boolean)` | Legt das Feld für die Ansicht einer Karte fest. |
| `getCreated()` | Gibt den Unix-Zeitstempel der Erstellungszeit der Karte aus dem Braze Dashboard zurück. |
| `getUpdated()` | Gibt den Unix-Zeitstempel der letzten Aktualisierungszeit der Karte aus dem Braze Dashboard zurück. |
| `getCategories()` | Gibt die Liste der Kategorien zurück, die der Karte zugewiesen sind. Karten ohne Kategorie werden `ABKCardCategoryNoCategory` zugewiesen. |
| `isInCategorySet(EnumSet)` | Gibt true zurück, wenn die Karte zum angegebenen Kategoriensatz gehört. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bannerbildkarte

[Banner-Bildkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) sind anklickbare Bilder in voller Größe.

|Eigenschaft|Beschreibung|
|---|---|
| `getImageUrl()` | Gibt die URL des Bildes der Karte zurück. |
| `getUrl()` | Gibt die URL zurück, die geöffnet wird, wenn Sie auf die Karte klicken. Dabei kann es sich um eine HTTP- oder HTTPS-URL oder eine Protokoll-URL handeln. |
| `getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bildkarte mit Beschriftung

[Bildunterschriftenkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft|Beschreibung|
|---|---|
| `getImageUrl()` | Gibt die URL des Bildes der Karte zurück. |
| `getTitle()` | Gibt den Titeltext für die Karte zurück. |
| `getDescription()` | Gibt den Text für die Karte zurück. |
| `getUrl()` | Gibt die URL zurück, die geöffnet wird, wenn Sie auf die Karte klicken.  Dabei kann es sich um eine HTTP- oder HTTPS-URL oder eine Protokoll-URL handeln. |
| `getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Textankündigungskarte (Bildunterschrift ohne Bild) Eigenschaften

[Textankündigungskarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) sind anklickbare Karten mit beschreibendem Text.

|Eigenschaft|Beschreibung|
|---|---|
| `getTitle()` | Gibt den Titeltext für die Karte zurück. |
| `getDescription()` | Gibt den Text für die Karte zurück. |
| `getUrl()` | Gibt die URL zurück, die geöffnet wird, wenn Sie auf die Karte klicken. Dabei kann es sich um eine HTTP- oder HTTPS-URL oder eine Protokoll-URL handeln. |
| `getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Kurznachrichtenkarte

[Kurznachrichtenkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) sind anklickbare Karten mit Bildern und begleitendem beschreibendem Text.

|Eigenschaft|Beschreibung|
|---|---|
| `getImageUrl()` | Gibt die URL des Bildes der Karte zurück. |
| `getTitle()` | Gibt den Titeltext für die Karte zurück. |
| `getDescription()` | Gibt den Text für die Karte zurück. |
| `getUrl()` | Gibt die URL zurück, die geöffnet wird, wenn Sie auf die Karte klicken. Dabei kann es sich um eine HTTP- oder HTTPS-URL oder eine Protokoll-URL handeln. |
| `getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Session-Analysen

Die Fragmente der Android-Benutzeroberfläche zeichnen nicht automatisch Sitzungsanalysen auf. Um sicherzustellen, dass die Sitzungen [korrekt getrackt]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/) werden, rufen Sie `IBraze.openSession()` auf, wenn Ihre App geöffnet wird.

## Verlinkung

Die Verlinkung mit dem Newsfeed von einer In-App-Nachricht aus muss durch Registrieren von `BrazeFeedActivity` in der `AndroidManifest.xml` aktiviert werden.

## Integration benutzerdefinierter Feeds

Wenn Sie den Feed auf eine völlig individuelle Weise anzeigen möchten, können Sie Ihre eigenen Ansichten verwenden, die mit Daten aus unseren Modellen gefüllt werden. Um News Feed-Modelle zu erhalten, müssen Sie sich für News Feed-Updates anmelden und die daraus resultierenden Modelldaten zum Auffüllen Ihrer Ansichten verwenden. Sie müssen auch Analysen zu den Modellobjekten protokollieren, wenn Benutzer mit Ihren Ansichten interagieren.

### Teil 1: Abonnieren von Feed-Updates

Deklarieren Sie zunächst eine private Variable in Ihrer angepassten Feed-Klasse, um Ihren Abonnenten zu speichern:

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Als Nächstes fügen Sie den folgenden Code – typischerweise innerhalb von `Activity.onCreate()` der angepassten Feed-Aktivität – hinzu, um Feed-Updates von Braze zu abonnieren:

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

Wir empfehlen Ihnen außerdem, sich abzumelden, wenn Ihre angepasste Feed-Aktivität nicht mehr sichtbar ist. Fügen Sie den folgenden Code in die Lebenszyklusmethode Ihrer Aktivität `onDestroy()` ein:

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Teil 2: Protokollieren von Analytics

Wenn Sie benutzerdefinierte Ansichten verwenden, müssen Sie die Analysen manuell protokollieren, da die Analysen nur bei der Verwendung von Braze-Ansichten automatisch verarbeitet werden.

Um eine Anzeige des Feeds zu protokollieren, rufen Sie [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html).

Um eine Impression oder einen Klick auf eine Karte zu protokollieren, rufen Sie [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) bzw. [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) auf.

