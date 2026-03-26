---
nav_title: Gelesen- und Ungelesen-Anzeige
article_title: Gelesen- und Ungelesen-Anzeige für Content-Cards unter iOS
platform: iOS
page_order: 4
description: "In diesem Referenzartikel erfahren Sie mehr über die iOS Gelesen- und Ungelesen-Anzeige und wie Sie diese in Ihre Content-Cards implementieren."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Gelesen- und Ungelesen-Anzeige

## Deaktivieren der Ungelesen-Anzeige

![Zwei Content-Cards werden nebeneinander angezeigt. Die Karte auf der linken Seite hat unten eine blaue Linie, die anzeigt, dass sie noch nicht gesehen wurde. Die Karte auf der rechten Seite weist keine blaue Linie auf, was darauf hinweist, dass sie bereits angesehen wurde.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Sie können die blaue Linie am unteren Rand der Karte, die anzeigt, ob die Karte angesehen wurde oder nicht, deaktivieren, indem Sie die Eigenschaft `disableUnviewedIndicator` in `ABKContentCardsTableViewController` auf `YES` setzen.

## Anpassen der Ungelesen-Anzeige

Auf die Ungelesen-Anzeige kann über die Eigenschaft `unviewedLineView` der Klasse `ABKBaseContentCardCell` zugegriffen werden. Wenn Sie `UITableViewCell`-Implementierungen verwenden, sollten Sie auf die Eigenschaft zugreifen, bevor die Zelle gezeichnet wird.

So setzen Sie beispielsweise die Farbe der Ungelesen-Anzeige auf Rot:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}