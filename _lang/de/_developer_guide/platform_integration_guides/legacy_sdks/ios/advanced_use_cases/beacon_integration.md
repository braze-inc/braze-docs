---
nav_title: Beacon-Integration
article_title: Beacon-Integration für iOS
platform: iOS
page_order: 4
description: "Dieser Artikel behandelt die Protokollierung angepasster Events mit Gimbal Beacons für iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Beacon-Integration

Hier erfahren Sie, wie Sie bestimmte Arten von Beacons zu Segmentierungs- und Messaging-Zwecken in Braze integrieren.

## Gimbal-Beacons

Sobald Sie Ihre Gimbal Beacons eingerichtet und in Ihre App integriert haben, können Sie angepasste Events protokollieren, z.B. den Beginn oder das Ende eines Besuchs oder die Sichtung eines Beacons. Sie können auch Eigenschaften für diese Events wie den Ortsnamen oder die Verweildauer protokollieren.

Um ein angepasstes Event zu protokollieren, wenn ein Nutzer einen Ort betritt, geben Sie diesen Code in die Methode `didBeginVisit` ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue` bestätigt, dass das Event auch dann protokolliert wird, wenn sich die App im Hintergrund befindet. Der gleiche Prozess kann für das Verlassen eines Orts implementiert werden. Beachten Sie, dass dieser Code für jeden neuen Ort, den der Nutzer betritt, ein eindeutiges angepasstes Event erstellt und inkrementiert. Wenn Sie mehr als 50 Orte erstellen möchten, empfehlen wir Ihnen, ein allgemeines angepasstes Event des Typs "Betretener Ort" zu erstellen und den Ortsnamen als Event-Eigenschaft aufzunehmen.
