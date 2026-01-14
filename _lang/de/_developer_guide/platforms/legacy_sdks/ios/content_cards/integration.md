---
nav_title: Integration
article_title: Content-Card View Controller Integration für iOS
platform: iOS
page_order: 1
description: "Dieser Referenzartikel behandelt die Integrationsschritte, Datenmodelle und kartenspezifischen Eigenschaften, die für Ihre iOS-Anwendung zur Verfügung stehen."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration von Inhaltskarten

## Content-Cards-Datenmodell

Das Content-Cards-Datenmodell ist im iOS SDK verfügbar.

### Abrufen der Daten

Um auf das Content-Cards-Datenmodell zuzugreifen, abonnieren Sie die Update-Events für Content-Cards:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab schnell %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Wenn Sie die Kartendaten ändern möchten, nachdem sie von Braze gesendet wurden, empfehlen wir Ihnen, eine Tiefenkopie der Kartendaten lokal zu speichern, die Daten zu aktualisieren und sie selbst anzuzeigen. Die Karten sind zugänglich über [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Content-Card-Modell

Braze bietet drei Content-Card-Typen: Banner, Bild mit Bildunterschrift und klassisch. Jeder Typ erbt gemeinsame Eigenschaften von einer Basisklasse `ABKContentCard` und hat die folgenden zusätzlichen Eigenschaften.

### Eigenschaften des Basis-Content-Card-Modells - ABKContentCard

|Eigenschaft|Beschreibung|
|---|---|
|`idString` | (Nur Lesen) Die von Braze festgelegte ID der Karte. |
| `viewed` | Diese Eigenschaft zeigt an, ob der Benutzer die Karte angesehen hat oder nicht.|
| `created` | (Nur Lesen) Diese Eigenschaft ist der Unix-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `expiresAt` | (Nur Lesen) Diese Eigenschaft ist der Unix-Zeitstempel der Ablaufzeit der Karte.|
| `dismissible` | Diese Eigenschaft gibt an, ob der Nutzer:in die Karte einsteigen kann.|
| `pinned` | Diese Eigenschaft zeigt an, ob die Karte im Dashboard als "angeheftet" eingerichtet wurde.|
| `dismissed` | Diese Eigenschaft gibt an, ob der Nutzer:innen die Karte entsorgt hat.|
| `url` | Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. Dabei kann es sich um eine HTTP(S)-URL oder eine Protokoll-URL handeln.|
| `openURLInWebView` | Diese Eigenschaft bestimmt, ob die URL innerhalb der App oder in einem externen Webbrowser geöffnet wird.|
| `extras`| Eine optionale `NSDictionary` von `NSString` Werten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Banner-Content-Card Eigenschaften - ABKBannerContentCard

|Eigenschaft|Beschreibung|
|---|---|
| `image` | Diese Eigenschaft ist die URL des Bildes der Karte.|
| `imageAspectRatio` | Diese Eigenschaft ist das Seitenverhältnis des Kartenbildes und dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften von Content-Cards mit Bildunterschriften - ABKCaptionedImageCard

|Eigenschaft|Beschreibung|
|---|---|
| `image` | Diese Eigenschaft ist die URL des Bildes der Karte.|
| `imageAspectRatio` | Bei dieser Eigenschaft handelt es sich um das Seitenverhältnis des Bildes der Karte.|
| `title` | Der Titeltext für die Karte.|
| `cardDescription` | Der Text für die Karte.|
| `domain` | Der Linktext für die Eigenschaft URL, z. B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der klassischen Content-Card - ABKClassicContentCard

|Eigenschaft|Beschreibung|
|---|---|
| `image` | (Optional) Diese Eigenschaft ist die URL des Bildes der Karte.|
| `title` | Der Titeltext für die Karte. |
| `cardDescription` | Der Text für die Karte. |
| `domain` | Der Linktext für die Eigenschaft URL, z. B. @"blog.braze.com". Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion und die Richtung des Klickens auf die Karte anzuzeigen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Karten-Methoden

|Methode|Beschreibung|
|---|---|
| `logContentCardImpression` | Protokollieren Sie manuell einen Abdruck in Braze für eine bestimmte Karte. |
| `logContentCardClicked` | Protokollieren Sie manuell einen Klick auf Braze für eine bestimmte Karte. Das SDK protokolliert einen Klick auf die Karte nur, wenn die Eigenschaft `url` einen gültigen Wert hat. |
| `logContentCardDismissed` | Protokollieren Sie manuell eine Kündigung in Braze für eine bestimmte Karte. Das SDK protokolliert eine Karten-Ausblendung nur, wenn die Eigenschaft `dismissed` der Karte nicht bereits auf `true` gesetzt ist. |
| `isControlCard` | Bestimmen Sie, ob eine Karte die Kontrollkarte für einen A/B-Test ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten finden Sie in der [Dokumentation der Klassenreferenzierung](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Integration von View-Controllern und Content-Cards

Content-Cards können in zwei View-Controller-Kontexte integriert werden: Navigation oder Modal.

### Kontext "Navigation"

Beispiel für das Pushing einer Instanz von `ABKContentCardsTableViewController` in einen Navigation-Controller:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab schnell %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Um den Titel der Navigationsleiste anzupassen, legen Sie die Eigenschaft title der Instanz `ABKContentCardsTableViewController` `navigationItem` fest.
{% endalert %}

### Modaler Kontext

Dieses Modal wird verwendet, um den View Controller in einer modalen Ansicht zu präsentieren, mit einer Navigationsleiste oben und einem **Done** Button an der Seite der Leiste.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab schnell %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Beispiele für View-Controller finden Sie in unserer [Beispiel-App Content-Cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Um die Kopfzeile anzupassen, stellen Sie die Eigenschaft title der Instanz `navigationItem` ein, die zu der Instanz `ABKContentCardsTableViewController` gehört, die wiederum in der übergeordneten Instanz `ABKContentCardsViewController` eingebettet ist.
{% endalert %}
