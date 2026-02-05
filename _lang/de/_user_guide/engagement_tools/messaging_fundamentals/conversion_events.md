---
nav_title: Konversions-Events
article_title: Konversions-Events
page_order: 3
page_type: reference
description: "Dieser referenzierende Artikel definiert Konversions-Events, wie Sie damit Ihre Metriken für den Erfolg in Braze definieren und wie Sie diese Events nutzen können, um zu sehen, wie engagiert Ihre Nutzer:innen sind."
tool:
    - Campaigns
    - Canvas
---

# Konversions-Events

> Ein Konversions-Event ist eine Art Erfolgsmetrik, die verfolgt, ob ein Empfänger Ihres Messagings innerhalb eines bestimmten Zeitraums nach Erhalt Ihres Engagements eine hochwertige Aktion durchführt. Nutzen Sie diese Ereignisse, um sicherzustellen, dass Sie relevante, nützliche Informationen sammeln, die Sie später nutzen können, um Insights für Ihre Kampagne oder Ihr Canvas zu gewinnen.

## Funktionsweise

Für eine personalisierte Urlaubskampagne, die auf aktive Nutzer:innen abzielt, kann ein Konversions-Event wie " **Starten Sie eine Sitzung** innerhalb von zwei oder drei Tagen" angemessen sein, da Sie so ein Gefühl für das Engagement der Nutzer:innen nach dem Erhalt Ihrer Nachricht bekommen können. Sie können auch zusätzliche Events wie **Places Order**, **Upgrade App** oder eines Ihrer angepassten Events als Konversions-Events auswählen.

{% alert tip %}
Wenn Sie mehr über Konversionen erfahren möchten, lesen Sie unseren [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen.
{% endalert %}

### Regeln zum Konversionstracking

Konversions-Events attributieren Nutzer:innen-Aktionen auf einen Punkt des Engagements zurück. Beachten Sie die folgenden Hinweise zum Umgang von Braze mit Mehrfachkonversionen:

- **Kampagnen mit einem Kanal**: Die Konversion erfolgt pro Benutzer, nicht pro Gerät. Innerhalb eines Kanals konvertiert ein Nutzer:in nur einmal pro Konversions-Event, auch wenn eine Nachricht an mehrere Geräte gesendet wird. Wenn in einer Kampagne beispielsweise nur ein Konversions-Event auf "Tätigt einen beliebigen Kauf" eingestellt ist und ein Nutzer:innen innerhalb der Konversionsfrist zwei separate Käufe tätigt, zählt Braze nur eine Konversion.
- **Kampagnen mit mehreren Kanälen**: Bei Kampagnen mit mehreren Kanälen hat jeder Kanal seine eigene Opportunity für die Konversion. Ein Nutzer:innen kann einmal pro Kanal konvertieren, nachdem er eine Nachricht auf diesem Kanal erhalten hat. Das heißt, wenn ein Nutzer:innen Nachrichten auf mehreren Kanälen erhält (z.B. sowohl per E-Mail als auch per Push) und die Konversionsaktion ausführt, zählt Braze eine Konversion für jeden Kanal, was zu Konversionsraten von über 100% führen kann.
- Wenn ein Nutzer:innen ein Konversions-Event innerhalb der Konversionsfristen von zwei separaten Kampagnen oder Canvase, die er erhalten hat, durchführt, wird die Konversion bei beiden registriert.
- Ein Nutzer:innen gilt als konvertiert, wenn er das spezifische Konversions-Event im Fenster durchgeführt hat, auch wenn er die Nachricht nicht geöffnet oder angeklickt hat.
- Bei Canvase funktioniert das Tracking der Konversion auf der Grundlage der endgültigen Konversionsfrist, die beginnt, wenn ein Nutzer:innen das Canvas betritt, und nicht auf der Grundlage der einzelnen Nachrichten. Braze zählt Konversionen auch während der Verzögerungszeiten zwischen Nachrichten in Canvas.

### Primäres Konversionsereignis

Das primäre Konversions-Event ist das erste Ereignis, das Sie bei der Erstellung einer Kampagne oder eines Canvas hinzufügen. Es hat den größten Einfluss auf Engagement und Berichterstattung. Braze verwendet Ihr primäres Konversions-Event, um:

- Berechnen Sie die siegreiche Variation der Nachrichten in [multivariaten]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) Kampagnen oder Canvase.
- Legen Sie das Zeitfenster fest, in dem die Einnahmen für die Kampagne oder das Canvas berechnet werden.
- Passen Sie die Verteilung von Nachrichten für Kampagnen und Canvase mithilfe der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) an.

Die Anzahl der primären Konversions-Events ist die Anzahl der aufgetretenen Konversions-Events. Bei Kampagnen mit mehreren Kanälen zählt Braze die Konversionen pro Kanal (wie in den [Regeln für das Tracking von Konversionen](#conversion-tracking-rules) beschrieben). Das bedeutet, dass die Anzahl der Konversionen die Anzahl der eindeutigen Nutzer:innen übersteigen und zu Konversionsraten von mehr als 100% führen kann. Braze berechnet die primäre Konversions-Event-Rate, indem es diese Zahl durch die Anzahl der eindeutigen Empfänger:innen teilt. Braze betrachtet einen Nutzer:innen als Empfänger, wenn die Nachricht gesendet oder angezeigt wird, je nach Kanal. Bei Push oder E-Mail wird ein Nutzer:in zum Beispiel zum Empfänger, nachdem Braze die Nachricht gesendet hat. Bei In-App-Nachrichten oder Content-Cards muss der Nutzer:innen die Nachricht sehen, um als Empfänger:in zu gelten.

{% alert note %}
Wenn Sie Nachrichten mit dem Tag Liquid `abort` abbrechen, bricht Braze Nachrichten nur für Nutzer:innen ab, die Varianten durchlaufen. Nachrichten an Nutzer:innen in der Kontrollgruppe werden nicht abgebrochen, was zu verzerrten Prozentsätzen bei der Konversion zwischen Varianten und Kontrollgruppen führen kann. Als Abhilfe verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), um Ihre Benutzer bei der Eingabe von Kampagnen und Canvas anzusprechen.
{% endalert %}

## Erstellen einer Kampagne mit Konversion Tracking

### Schritt 1: Richten Sie Ihre Kampagne ein

[Erstellen Sie eine Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) für Ihren gewünschten Nachrichtenkanal. Nachdem Sie die Nachrichten und den Zeitplan für Ihre Kampagne eingerichtet haben, können Sie bis zu vier Konversions-Events zum Tracking hinzufügen.

Verwenden Sie so viele Konversions-Events wie nötig. Die Hinzufügung eines zweiten oder dritten Konversions-Events bereichert Ihre Berichterstattung erheblich. Wenn Sie zum Beispiel für eine Kampagne, die auf passive Nutzer:innen abzielt, neben dem primären Konversions-Event **"Starts Session"** ein sekundäres Konversions-Event hinzufügen, können Sie besser nachvollziehen, wie effektiv Ihre Kampagne Nutzer:innen zurück in Ihre Anwendung bringt. 

### Schritt 2: Hinzufügen der Konversions-Events

Wählen Sie zunächst den allgemeinen Ereignistyp aus, den Sie verwenden möchten:

| Konversions-Event Typ   | Beschreibung                |
|-------------------------|----------------------------|
| **Startet Sitzung**      | Ein Benutzer zählt als Konversion, wenn er eine der von Ihnen angegebenen Apps öffnet (standardmäßig sind das alle Apps im Workspace).|
| **Kauft etwas**      | Ein Nutzer:innen wird als konvertiert gezählt, wenn er ein [Kauf-Event]({{site.baseurl}}/api/objects_filters/purchase_object/) erfasst. Damit wird standardmäßig jeder Kauf getrackt, oder Sie können ein bestimmtes Produkt angeben.|
| **Bestellung wird aufgegeben**        | Ein Nutzer:innen wird als konvertiert gezählt, wenn er das [empfohlene Ereignis Order Placed eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events) triggert. Standardmäßig wird jede Bestellung getrackt, oder Sie können nach einem bestimmten Produkt filtern.|
| **Führt angepasstes Event aus**| Ein Benutzer zählt als Konversion, wenn er eines Ihrer benutzerdefinierten Ereignisse ausführt (keine Standardeinstellung, Sie müssen das Ereignis angeben).|
| **App upgraden**         | Ein Benutzer zählt als Konversion, wenn er die eine der von Ihnen angegebenen Apps aktualisiert (standardmäßig sind das alle Apps im Workspace). Braze führt einen numerischen Best-Efforts-Vergleich durch, um festzustellen, ob es sich bei der Änderung um ein Upgrade handelt. Nicht-numerische Versionen werden als Konversion gezählt, wenn sich die Version ändert.|
| **Öffnet E-Mail**         | Ein Benutzer zählt als Konversion, wenn er die E-Mail öffnet (nur bei E-Mail-Kampagnen).|
| **Klickt E-Mail an**        | Ein Benutzer zählt als Konversion, wenn er auf einen Link in der E-Mail klickt (nur bei E-Mail-Kampagnen).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Verschachtelte Eigenschaften werden in Konversions-Events nicht unterstützt**. Sie können verschachtelte Eigenschaften nicht in Konversions-Events verwenden. Wenn z.B. `product_code` oder `product_name` verschachtelte Eigenschaften innerhalb eines `products` Arrays (wie `products[].product_code`) sind, können Sie diese nicht verwenden, um zu prüfen, ob ein bestimmtes Produkt in einem Konversions-Event gekauft wurde.
{% endalert %}

Setzen Sie sich eine Konversionsfrist. Dies ist die maximale Zeitspanne, die vergehen kann, bevor Braze eine Konversion in Betracht zieht. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze die Konversion zählt, wenn der Nutzer:innen die angegebene Aktion durchführt.

![Der Ereignistyp "Kauf tätigen" erfasst z. B. Benutzer als Konversion, die einen Kauf tätigen. Die Frist beträgt 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, fahren Sie mit der Kampagnenerstellung fort und beginnen mit dem Versand Ihrer Kampagne.

### Schritt 3: Ihre Ergebnisse ansehen

Gehen Sie auf die Seite **Details**, um die Details für jedes Konversions-Event anzuzeigen, das mit der von Ihnen erstellten Kampagne verbunden ist. Unabhängig von den ausgewählten Konversions-Events können Sie während des Zeitfensters des primären Konversions-Events auch den Gesamtumsatz sehen, der dieser spezifischen Kampagne sowie bestimmten Varianten zugewiesen wurde.

{% alert note %}
Wenn Sie bei der Erstellung der Kampagne keine Konversions-Events auswählen, wird die Zeit standardmäßig auf drei Tage festgelegt.
{% endalert %}

Bei Nachrichten mit mehreren Varianten können Sie außerdem die Anzahl und relative Häufigkeit der Konversionsereignisse für Ihre Kontrollgruppe und die einzelnen Varianten einsehen.

![Vier Konversions-Events zum Tracking von Konversionen, die darauf basieren, wann ein Kauf innerhalb von drei Stunden getätigt wurde, wann ein Kauf innerhalb von zwei Stunden getätigt wurde, wann eine Sitzung innerhalb von 30 Minuten begonnen wurde und wann eine Sitzung innerhalb von 25 Minuten begonnen wurde.]({% image_buster /assets/img_archive/conversion_event_details.png %})