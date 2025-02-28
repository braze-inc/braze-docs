---
nav_title: Integration
article_title: News Feed Integration für iOS
platform: iOS
page_order: 0
description: "Dieser Artikel enthält einen Überblick über das News Feed-Datenmodell, die Integration des News Feeds in Ihre iOS-Anwendung und ein Beispiel für die Integration eines benutzerdefinierten View Controllers."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration von News Feeds

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## News Feed Datenmodell

### Abrufen der Daten

Um auf das Newsfeed-Datenmodell zuzugreifen, abonnieren Sie Update-Events für Newsfeeds:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab schnell %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Wenn Sie die Kartendaten ändern möchten, nachdem sie von Braze gesendet wurden, empfehlen wir Ihnen, die Kartendaten lokal zu speichern (Deep Copy), sie zu aktualisieren und sie selbst anzuzeigen. Die Karten sind über [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller") zugänglich.

## News Feed Modell

Braze verfügt über fünf einzigartige Kartentypen: Bannerbild, Bildunterschrift, Textankündigung und klassisch. Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

### Eigenschaften der Basiskartenmodelle

|Eigenschaft|Beschreibung|
|---|---|
| `idString` | (Nur Lesen) Die von Braze festgelegte ID der Karte. |
| `viewed` | Diese Eigenschaft zeigt an, ob die Karte vom Benutzer gelesen oder ungelesen ist. |
| `created` | (Nur Lesen) Die Eigenschaft ist der Unix-Zeitstempel der Erstellungszeit der Karte im Braze Dashboard. |
| `updated` | (Nur Lesen) Die Eigenschaft ist der Unix-Zeitstempel der letzten Aktualisierungszeit der Karte vom Braze Dashboard. |
| `categories` | Die Liste der Kategorien, die der Karte zugeordnet sind. Karten ohne Kategorie werden `ABKCardCategoryNoCategory` zugeordnet.<br><br>Verfügbare Kategorien:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | Eine optionale `NSDictionary` von `NSString` Werten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bannerbildkarte

|Eigenschaft|Beschreibung|
|---|---|
| `image` | (Erforderlich) Diese Eigenschaft ist die URL des Bildes der Karte. |
| `URL` | (Optional) Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. Dabei kann es sich um eine HTTP(S)-URL oder eine Protokoll-URL handeln. |
| `domain` | (Optional) Der Linktext für die URL der Eigenschaft, z.B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion und die Richtung des Klicks auf die Karte anzuzeigen, ist aber im standardmäßigen Braze News Feed verborgen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bildkarte mit Beschriftung

|Eigenschaft|Beschreibung|
|---|---|
| `image` | (Erforderlich) Diese Eigenschaft ist die URL des Bildes der Karte. |
| `title` | (Erforderlich) Der Titeltext für die Karte. |
| `description` (Erforderlich) Der Text für die Karte. |
| `URL` | (Optional) Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. Dabei kann es sich um eine HTTP(S)-URL oder eine Protokoll-URL handeln. |
| `domain` | (Optional) Der Linktext für die URL der Eigenschaft, z.B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion und die Richtung des Klickens auf die Karte anzuzeigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Textankündigungskarte (Bildunterschrift ohne Bild) Eigenschaften

|Eigenschaft|Beschreibung|
|---|---|
| `title` | (Erforderlich) Der Titeltext für die Karte. |
| `description` | (Erforderlich) Der Text für die Karte. |
| `url` | (Optional) Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. Dabei kann es sich um eine HTTP(S)-URL oder eine Protokoll-URL handeln. |
| `domain` | (Optional) Der Linktext für die URL der Eigenschaft, z.B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion und die Richtung des Klickens auf die Karte anzuzeigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassische Karteneigenschaften

|Eigenschaft|Beschreibung|
|---|---|
| `image` | (Erforderlich) Diese Eigenschaft ist die URL des Bildes der Karte. |
| `title` | (Optional) Der Titeltext für die Karte. |
| `description` | (Erforderlich) Der Text für die Karte. |
| `URL` | (Optional) Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. Dabei kann es sich um eine HTTP(S)-URL oder eine Protokoll-URL handeln. |
| `domain` | (Optional) Der Linktext für die URL der Eigenschaft, z.B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion und die Richtung des Klickens auf die Karte anzuzeigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Karten-Methoden

|Methode|Beschreibung|
|---|---|
| `logCardImpression` | Protokollieren Sie manuell einen Abdruck in Braze für eine bestimmte Karte. |
| `logCardClicked` | Protokollieren Sie manuell einen Klick auf Braze für eine bestimmte Karte. Das SDK protokolliert nur dann einen Klick auf die Karte, wenn die Eigenschaft `url` einen gültigen Wert aufweist. Alle Unterklassen von `ABKCard` haben die Eigenschaft `url`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Protokollieren der Newsfeed-Anzeige

Wenn Sie den News Feed in Ihrer eigenen Benutzeroberfläche anzeigen, können Sie die Eindrücke des News Feeds über `- (void)logFeedDisplayed;` manuell aufzeichnen. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## Integration des View-Controllers für Newsfeeds

Durch die Integration des View-Controllers `ABKNewsFeedViewController` wird der Braze-Newsfeed angezeigt.

Bei der Anzeige der View-Controller gibt es ein hohes Maß an Flexibilität. Es gibt verschiedene Versionen der View-Controller, um unterschiedliche Navigationsstrukturen zu berücksichtigen.

{% alert note %}
Der News Feed, der durch das Standardverhalten eines Klicks auf eine In-App-Nachricht aufgerufen wird, beachtet keine Delegierten, die Sie für den News Feed festgelegt haben. Hierzu müssen Sie [den Delegaten auf `ABKInAppMessageUIController` festlegen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) und die Delegate-Methode [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks) für `ABKInAppMessageUIDelegate` implementieren.
{% endalert %}

Der News Feed kann in zwei View-Controller-Kontexte integriert werden: Navigation oder modal.

### Navigationskontext - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab schnell %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

Um die Navigationsleiste `title` anzupassen, legen Sie die Titel-Eigenschaft `navigationItem` der Instanz `ABKNewsFeedTableViewController` fest .

### Modaler Kontext - ABKFeedViewControllerModalContext

Dieses Modal wird verwendet, um den View Controller in einer modalen Ansicht zu präsentieren, mit einer Navigationsleiste oben und einer Schaltfläche **Erledigt** auf der rechten Seite der Leiste. Um den Titel des Modals anzupassen, legen Sie die Eigenschaft `title` der Instanz `ABKNewsFeedTableViewController` auf `navigationItem` fest. 

Wenn **KEIN** Delegat festgelegt ist, blendet der Button **Fertig** die modale Ansicht aus. Wenn ein Delegat **festgelegt ist**, ruft die Schaltfläche **Erledigt** den Delegaten auf und der Delegat selbst ist für das Beenden der Ansicht verantwortlich.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab schnell %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Beispiele für View-Controller finden Sie in unserer [News Feed-Beispielanwendung](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample).


