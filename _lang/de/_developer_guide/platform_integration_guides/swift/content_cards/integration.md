---
nav_title: Integration
article_title: Content Card Integration für iOS
platform: Swift
page_order: 0
description: "Dieser Artikel behandelt die Integrationsschritte, Datenmodelle und kartenspezifischen Eigenschaften, die im Swift SDK verfügbar sind."
channel:
  - content cards

---

# Integration von Inhaltskarten

> Dieser Referenzartikel beschreibt die Content-Card-Integration sowie die verschiedenen Datenmodelle und kartenspezifischen Eigenschaften, die für Ihre Swift-Anwendung zur Verfügung stehen. Ziehen Sie den [Anpassungsleitfaden für Content-Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards) zurate, um mit der Implementierung und Anpassung zu beginnen.

## Über die Integration

Die standardmäßige Content-Cards-UI kann aus der Bibliothek `BrazeUI` des Braze SDK integriert werden. Erstellen Sie den View-Controller für Content-Cards unter Verwendung der Instanz `braze`. Wenn Sie auf den Lifecycle der Content-Card-UI reagieren möchten, implementieren Sie [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) als Delegaten für `BrazeContentCardUI.ViewController`.

{% alert note %}
Weitere Informationen zu den Optionen für iOS-View-Controller finden Sie in der [Apple-Entwicklerdokumentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

Die Bibliothek `BrazeUI` des Swift SDK bietet zwei Standardkontexte für View-Controller: Navigation oder Modal. Das bedeutet, dass Sie Content-Cards in diese Kontexte integrieren können, indem Sie ein paar Codezeilen zu Ihrer App oder Website hinzufügen. Beide Ansichten bieten Anpassungs- und Gestaltungsmöglichkeiten, wie in der [Anpassungsanleitung]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios) beschrieben. Sie können auch einen benutzerdefinierten Content Card View Controller erstellen, anstatt den Standard-Controller von Braze zu verwenden, um noch mehr Anpassungsmöglichkeiten zu haben - ein Beispiel finden Sie im [Content Cards UI-Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% alert important %}
Um Content-Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie das Objekt [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann ein Nutzer die Kontrollkarte gesehen hätte.
{% endalert %}

## Navigationskontext

Ein Navigationscontroller ist ein View-Controller, der mindestens einen untergeordneten View-Controller in einer Navigationsschnittstelle verwaltet. Hier ist ein Beispiel, wie Sie eine Instanz von `BrazeContentCardUI.ViewController` in einen Navigationscontroller pushen:

{% tabs %}
{% tab schnell %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

## Modaler Kontext

Verwenden Sie modale Präsentationen, um den Workflow Ihrer App vorübergehend zu unterbrechen, z. B. indem Sie die Nutzer zur Angabe wichtiger Informationen auffordern. Diese Modellansicht verfügt über eine Navigationsleiste am oberen Rand und eine Schaltfläche **Erledigt** an der Seite der Leiste. Hier ist ein Beispiel, wie Sie eine Instanz von `BrazeContentCard.ViewController` in einen modalen Controller pushen:

{% tabs %}
{% tab schnell %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Ein Beispiel für die Verwendung von `BrazeUI` View Controllern finden Sie in den entsprechenden Content Cards UI-Beispielen in unserer [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Content-Cards-Datenmodell

Das Content-Cards-Datenmodell ist im Modul `BrazeKit` des iOS Swift SDK verfügbar.

Braze bietet fünf Content Card-Typen: nur Bild, Bild mit Untertitel, klassisch, klassisches Bild und Kontrolle. Jeder Typ ist eine Implementierung des Typs `Braze.ContentCard`. Beachten Sie, dass `BrazeKit` eine alternative Klasse des Typs [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) für Objective-C Kompatibilität anbietet.

Eine vollständige Liste der Eigenschaften von Content-Cards sowie Einzelheiten zur Verwendung von Content-Cards finden Sie in der [Dokumentation zur Klasse `ContentCard` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie `contentCards.cards` in Ihrer `braze`-Instanz auf. Weitere Informationen zum Abonnieren von Kartendaten finden Sie unter [Logging-Analysen]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics).

## Karten-Methoden

Jede Karte wird mit einem Objekt des Typs `Context` initialisiert, das verschiedene Methoden zur Verwaltung des Kartenstatus enthält. Rufen Sie diese Methoden auf, wenn Sie die entsprechende Statuseigenschaft für ein bestimmtes Kartenobjekt ändern möchten.

| Methode                               | Beschreibung                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Protokolliert das Event "Content-Card-Impression".                                                                                                   |
| `card.context?.logClick()`           | Protokolliert das Event "Klick auf Content-Card".                                                                                                        |
| `card.context?.processClickAction()` | Verarbeiten Sie eine gegebene [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) Eingabe. |
| `card.context?.logDismissed()`       | Protokolliert das Event "Content-Card ausgeblendet".                                                                                                    |
| `card.context?.logError()`           | Protokollieren Sie einen Fehler im Zusammenhang mit der Inhaltskarte.                                                                                                |
| `card.context?.loadImage()`          | Lädt ein bestimmtes Content-Card-Bild von einer URL. Diese Methode kann null sein, wenn die Content-Card kein Bild enthält.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten finden Sie in der [Dokumentation zur Klasse `Context` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)

{% alert important %}
Das Swift SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Die Unterstützung kann durch Wrapping einer Drittanbieteransicht oder Ihrer eigenen Ansicht in eine Instanz von `GIFViewProvider` hinzugefügt werden.

Weitere Einzelheiten zur GIF-Unterstützung finden Sie in dieser [Anleitung](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}
