---
nav_title: Events
article_title: Events
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt die verschiedenen Events in Braze - Standard-Events, Kauf-Events und angepasste Events - und deren Zweck."
---

# Events 

> Auf dieser Seite finden Sie die verschiedenen Veranstaltungen in Braze und deren Zweck.

Braze verwendet einige verschiedene Ereignistypen, um ein umfassendes Verständnis des Verhaltens der Nutzer:innen und des Engagements für Ihre Marke zu erhalten. Jede Art von Veranstaltung dient einem eindeutigen Zweck:

- [Standard-Ereignisse](#standard-events): Vermitteln Sie ein grundlegendes Verständnis des Engagements der Nutzer:innen Ihrer App oder Website.
- [Kauf-Events](#purchase-events): Entscheidend für das Verständnis des Kaufverhaltens der Nutzer:innen und für das Tracking der Einnahmen. 
- [Angepasste Events](#custom-events): Verschaffen Sie sich tiefere Insights in das Nutzer:innen-Verhalten, das für Ihre App oder Ihr Unternehmen eindeutig ist.

Durch das Tracking dieser verschiedenen Arten von Ereignissen erhalten Sie ein tieferes Verständnis Ihrer Nutzer:innen, das Sie in Ihre Marketing Strategien einfließen lässt, Ihnen bei der Optimierung Ihrer App hilft und Sie in die Lage versetzt, ein personalisiertes Nutzer:innen-Erlebnis zu bieten. Lassen Sie uns eintauchen!

## Standard-Ereignisse

In Braze sind Standardereignisse vordefinierte Aktionen, die Nutzer:innen in Ihrer App ausführen können und die Braze automatisch trackt, nachdem Sie das Braze SDK integriert haben. Hier sind einige Beispiele für Standardereignisse:

- App starten
- [Kauf](#purchase-events)
- Beginn der Sitzung
- Ende der Sitzung
- Push-Benachrichtigung angeklickt
- E-Mail geöffnet

Als Marketer können Sie diese Standardereignisse nutzen, um das Verhalten der Nutzer:innen und das Engagement für Ihre App zu verstehen. Sie können zum Beispiel sehen, wie oft Nutzer:innen Ihre App starten oder wie viele Käufe getätigt werden. Diese Informationen können von unschätzbarem Wert sein, wenn es darum geht, gezielte Marketing Kampagnen zu erstellen.

Während Standard-Events von Braze automatisch getrackt werden, müssen Kauf-Events, angepasste Events und angepasste Attribute von Ihrem Entwicklerteam auf der Grundlage Ihrer spezifischen Anforderungen und Ziele eingerichtet werden.

## Kauf-Events

Kauf-Events sind eine Möglichkeit, die Einkäufe Ihrer Nutzer:innen zu erfassen und zu tracken. Sie sind eine Art von Standard-Ereignis, das nach der Integration des Braze SDK standardmäßig verfügbar ist. Wenn Sie also Kauf-Events zum Tracking von Käufen verwenden, können Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg direkt von Braze aus überwachen.

Kauf-Events zeichnen die folgenden Schlüsselinformationen über einen Kauf auf:

- Produkt ID (in der Regel der Produktname oder die Kategorie)
- Währung
- Preis
- Menge

Sie können diese Daten dann verwenden, um Ihre Nutzer:innen auf der Grundlage ihres Lifetime-Value, ihrer Kaufhäufigkeit, bestimmter Käufe und mehr zu segmentieren.

Braze unterstützt auch Käufe in mehreren Währungen. Wenn ein Kauf in einer anderen Währung als USD gemeldet wird, wird er auf dem Braze-Dashboard in USD angezeigt, basierend auf dem Wechselkurs zum Zeitpunkt der Meldung des Kaufs.

Wenn Sie mehr erfahren möchten, besuchen Sie unseren Artikel über [Kauf-Events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/).

{% details Example implementation %}

Beachten Sie, dass die tatsächliche Implementierung von Kauf-Events einige technische Kenntnisse erfordert, da es um die Integration des Braze SDK mit Ihrer App geht. Ihr Customer-Success-Manager wird Ihr Team im Rahmen Ihres Onboardings durch diesen Prozess führen, aber die allgemeinen Schritte sind wie folgt:

1. **Integrieren Sie das Braze SDK:** Bevor Sie irgendwelche Ereignisse protokollieren, müssen Sie das Braze SDK in Ihre App integrieren.
2. **Protokollieren Sie das Kauf-Event:** Nach der Integration des SDK können Sie ein Kauf-Event protokollieren, wenn ein Nutzer:innen einen Kauf in Ihrer App tätigt. Dies geschieht normalerweise in der Funktion oder Methode, die aufgerufen wird, wenn ein Kauf abgeschlossen ist.

Hier sehen Sie ein Beispiel für die Protokollierung eines Kauf-Events in einer iOS App mit Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

In diesem Beispiel ist "product_name" der Name des gekauften Produkts, "USD" ist die Währung des Kaufs, "1.99" ist der Preis des Produkts und "1" ist die gekaufte Menge.

{:start="3"}
3\. **Sehen Sie sich das Kauf-Event im Braze-Dashboard an:** Nachdem das Kauf-Event protokolliert wurde, können Sie es auf dem Braze-Dashboard einsehen. Sie können diese Daten nutzen, um Ihren Umsatz zu analysieren, Ihre Nutzer:innen zu segmentieren und vieles mehr.

Denken Sie daran, dass die genaue Implementierung je nach Plattform (iOS, Android, Internet) und den spezifischen Anforderungen Ihrer App variieren kann. 

{% enddetails %}

## Angepasste Events

Angepasste Events sind Ereignisse, die Sie auf der Grundlage der spezifischen Aktionen definieren, die Sie innerhalb Ihrer App oder Website tracken möchten. Braze verfolgt sie nicht automatisch. Sie müssen diese Ereignisse manuell in Ihrer Braze SDK-Implementierung einrichten. Angepasste Events können alles sein, vom Abschluss eines Levels in einem Spiel bis zum Update des Profils eines Nutzers:innen.

Hier ein Beispiel dafür, wie Sie ein angepasstes Event in einer iOS App mit Swift protokollieren:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

In diesem Beispiel ist "completed_level" der Name des angepassten Events, das protokolliert wird, wenn ein Nutzer:innen einen Level in einem Spiel abschließt. Dieses angepasste Event wird dann auf dem Profil des Nutzers:in in Braze aufgezeichnet, das Sie zum Triggern von Kampagnen und zur Personalisierung von Messaging verwenden können.

Wenn Sie mehr erfahren möchten, besuchen Sie unseren Artikel über [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

{% details Example implementation %}

Ähnlich wie bei Kauf-Events erfordern angepasste Events zusätzliche Einstellungen. Im Folgenden finden Sie eine allgemeine Vorgehensweise für die Implementierung angepasster Events in Braze:

1. **Integrieren Sie das Braze SDK:** Bevor Sie irgendwelche Ereignisse protokollieren können, müssen Sie das Braze SDK in Ihre App integrieren.
2. **Definieren Sie Ihr angepasstes Event:** Entscheiden Sie, welche Aktion in Ihrer App Sie als angepasstes Event tracken möchten. Das kann alles sein, was für Ihre App von Bedeutung ist, z. B. wenn ein Nutzer:innen ein Level in einem Spiel abschließt, sein Profil aktualisiert oder eine bestimmte Art von Kauf tätigt.
3. **Protokollieren Sie das angepasste Event:** Nachdem Sie Ihr angepasstes Event definiert haben, können Sie es im Code Ihrer App protokollieren. Dies geschieht normalerweise in der Funktion oder Methode, die aufgerufen wird, wenn die Aktion stattfindet.

Hier ein Beispiel dafür, wie Sie ein angepasstes Event in einer iOS App mit Swift protokollieren:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

In diesem Beispiel ist "updated_profile" der Name des angepassten Events, das protokolliert wird, wenn ein Nutzer:in sein Profil aktualisiert.

{:start="4"}
4\. **Fügen Sie Eigenschaften zu Ihrem angepassten Event hinzu (optional):** Wenn Sie zusätzliche Details über das angepasste Event erfassen möchten, können Sie ihm Eigenschaften hinzufügen. Dazu übergeben Sie ein Wörterbuch mit Eigenschaften, wenn Sie das Ereignis protokollieren.

Hier ein Beispiel dafür, wie Sie ein angepasstes Event mit Eigenschaften in einer iOS App mit Swift protokollieren:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

In diesem Beispiel hat das angepasste Event eine Eigenschaft namens "Property Name" mit dem Wert "Property Value".

{:start="5"}
5\. **Sehen Sie sich das angepasste Event im Braze-Dashboard an:** Nachdem das angepasste Event protokolliert wurde, können Sie es im Braze-Dashboard einsehen. Sie können diese Daten verwenden, um das Nutzer:innen-Verhalten zu analysieren, Ihre Nutzer:innen zu segmentieren und vieles mehr.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


