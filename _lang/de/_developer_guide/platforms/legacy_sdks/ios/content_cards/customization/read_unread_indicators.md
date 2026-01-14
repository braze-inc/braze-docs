---
nav_title: Gelesen &amp; Ungelesen Indikatoren
article_title: Content-Card Lese- &amp; Ungelesen-Anzeigen für iOS
platform: iOS
page_order: 4
description: "Dieser Artikel referenziert die iOS Lese- und Ungelesen-Anzeigen und wie Sie sie in Ihre Content-Cards implementieren."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Indikatoren für gelesen und ungelesen

## Deaktivieren der Nicht-aufgerufen-Anzeige

![Zwei Inhaltskarten werden nebeneinander angezeigt. Die Karte auf der linken Seite hat unten eine blaue Linie, die anzeigt, dass sie nicht gesehen wurde. Die Karte auf der rechten Seite hat keine blaue Linie, was bedeutet, dass sie bereits gesehen wurde.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Sie können die blaue Linie am unteren Rand der Karte, die anzeigt, ob die Karte angesehen wurde oder nicht, deaktivieren, indem Sie die Eigenschaft `disableUnviewedIndicator` in `ABKContentCardsTableViewController` auf `YES` setzen.

## Anpassen der Nicht-aufgerufen-Anzeige

Auf den nicht angezeigten Indikator kann über die Eigenschaft `unviewedLineView` der Klasse `ABKBaseContentCardCell` zugegriffen werden. Wenn Sie `UITableViewCell`-Implementierungen verwenden, sollten Sie auf die Eigenschaft zugreifen, bevor die Zelle gezeichnet wird.

So setzen Sie beispielsweise die Farbe der Nicht-aufgerufen-Anzeige auf Rot:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab schnell %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
