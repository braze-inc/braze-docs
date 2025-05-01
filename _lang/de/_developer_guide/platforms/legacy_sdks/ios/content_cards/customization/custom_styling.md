---
nav_title: Angepasste Stile
article_title: Individuelle Gestaltung von Inhaltskarten für iOS
platform: iOS
page_order: 1
description: "Dieser Artikel befasst sich mit den Optionen für die individuelle Gestaltung von Inhaltskarten für Ihre iOS-Anwendung."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Stile

## Überschreiben der Standardbilder

{% alert important %}
Die Integration von `SDWebImage` ist erforderlich, wenn Sie unsere Braze UI für die Anzeige von Bildern in iOS In-App-Nachrichten oder Content Cards verwenden möchten.
{% endalert %}

Braze ermöglicht es Kunden, vorhandene Standardbilder durch eigene angepasste Bilder zu ersetzen. Erstellen Sie dazu eine neue `png`-Datei mit dem angepassten Bild und fügen Sie sie dem Bild-Bundle der App hinzu. Benennen Sie dann die Datei in den Namen des Bildes um, um das Standardbild in unserer Bibliothek zu überschreiben. Stellen Sie außerdem sicher, dass Sie die Versionen `@2x` und `@3x` der Bilder hochladen, damit sie für verschiedene Handygrößen geeignet sind. Folgende Bilder können in Content-Cards überschrieben werden:

- Platzhalterbild: `appboy_cc_noimage_lrg`
- Angepinntes Symbolbild: `appboy_cc_icon_pinned`

Da Content-Cards eine maximale Größe von 2 KB für Inhalte haben, die Sie im Dashboard eingeben haben (einschließlich Nachrichtentext, Bild-URLs, Links und aller Schlüssel-Wert-Paare), sollten Sie die Größe vor dem Senden überprüfen. Wenn Sie diesen Betrag überschreiten, kann die Karte nicht gesendet werden.

{% alert important %}
Das Überschreiben von Standardbildern wird in unserer Xamarin iOS-Integration derzeit nicht unterstützt.
{% endalert %}

## Deaktivieren des dunklen Modus

Um zu verhindern, dass die Content-Card-UI ein dunkles Design annimmt, wenn der Dark Mode auf dem Nutzergerät aktiviert ist, legen Sie die Eigenschaft `ABKContentCardsTableViewController.enableDarkTheme` fest. Sie können direkt auf einer Instanz von `ABKContentCardsTableViewController` oder über die Eigenschaft `ABKContentCardsViewController.contentCardsViewController` auf die Eigenschaft `enableDarkTheme` zugreifen, um Ihre Benutzeroberfläche optimal zu gestalten.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab schnell %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

