---
nav_title: Beacon-Integration
article_title: Beacon-Integration für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie benutzerdefinierte Ereignisse mit Gimbal Beacons für Android oder FireOS protokollieren können."

---

# Beacon-Integration

> In diesem Artikel erfahren Sie, wie Sie bestimmte Arten von Beacons zu Segmentierungs- und Messaging-Zwecken in Braze integrieren.

## Gimbal-Beacons

Sobald Sie Ihre Gimbal Beacons eingerichtet und in Ihre App integriert haben, können Sie benutzerdefinierte Ereignisse protokollieren, z. B. den Beginn oder das Ende eines Besuchs oder die Sichtung eines Beacons. Sie können auch Eigenschaften für diese Events wie den Ortsnamen oder die Verweildauer protokollieren.

Um ein angepasstes Event zu protokollieren, wenn ein Nutzer einen Ort betritt, fügen Sie diesen Code in die Methode `onVisitStart` ein:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

`requestImmediateDataFlush` überprüft, dass das Event auch dann protokolliert wird, wenn sich die App im Hintergrund befindet. Der gleiche Prozess kann für das Verlassen eines Orts implementiert werden. Beachten Sie, dass die Aktivität und der Kontext, in dem Sie arbeiten, die Art und Weise, wie Sie die Zeilen `logCustomEvent` und `requestImmediateDataFlush` integrieren, verändern können. Beachten Sie außerdem, dass dieser Code für jeden neuen Ort, den der Nutzer betritt, ein eindeutiges angepasstes Event erstellt und inkrementiert. Wenn Sie also mehr als 50 Orte erstellen möchten, empfehlen wir Ihnen, ein allgemeines angepasstes Event des Typs "Betretener Ort" zu erstellen und den Ortsnamen als Event-Eigenschaft aufzunehmen.
