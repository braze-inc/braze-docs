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

Für eine personalisierte Weihnachtskampagne, die sich an aktive Nutzer:innen richtet, könnte ein Konversions-Event wie **„Eine Sitzung starten“** innerhalb von zwei oder drei Tagen angemessen sein, da Sie so einen Eindruck vom Engagement der Nutzer:innen nach dem Erhalt Ihrer Nachricht gewinnen können. Sie können auch zusätzliche Ereignisse wie **„Bestellung aufgeben**“, **„App upgraden**“ oder eines Ihrer angepassten Events als Konversions-Events auswählen.

{% alert tip %}
Wenn Sie mehr über Konversionen erfahren möchten, lesen Sie unseren [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen.
{% endalert %}

### Regeln zum Konversionstracking

Konversions-Events ordnen Benutzeraktionen einem bestimmten Punkt des Engagements zu. Bitte beachten Sie Folgendes zur Handhabung mehrerer Konversionen durch Braze:

- **Einkanal-Kampagnen**: Die Konversion erfolgt pro Benutzer, nicht pro Gerät. Innerhalb eines einzelnen Kanals konvertiert eine Nutzer:in nur einmal pro Konversions-Event, selbst wenn eine Nachricht an mehrere Geräte gesendet wird. Wenn beispielsweise für eine Kampagne nur ein Konversions-Event auf „Kauf tätigen“ festgelegt ist und eine Nutzer:in innerhalb der Conversion-Frist zwei separate Käufe tätigt, zählt Braze nur eine Konversion.
- **Multichannel-Kampagnen**: Bei Multichannel-Kampagnen verfügt jeder Kanal über seine eigene Konversion-Möglichkeit. Ein Nutzer:in kann nach Erhalt einer Nachricht in einem Kanal einmal pro Kanal konvertieren. Das bedeutet, wenn eine Nutzer:in Nachrichten über mehrere Kanäle (z. B. sowohl per E-Mail als auch per Push-Benachrichtigung) erhält und die Konversion-Aktion durchführt, zählt Braze für jeden Kanal eine Konversion, was zu Konversionsraten von über 100 % führen kann.
- Wenn eine Nutzer:in innerhalb der Fristen für Konversionen von zwei separaten Kampagnen oder Canvases, die sie erhalten haben, ein Konversions-Event durchführt, wird die Konversion in beiden Fällen registriert.
- Eine Nutzer:in gilt als konvertiert, wenn sie das spezifische Konversions-Event im Fenster durchgeführt hat, auch wenn sie die Nachricht nicht geöffnet oder geklickt hat.
- Bei Canvases basiert das Conversion-Tracking auf der endgültigen Frist für die Konversion, die beginnt, wenn eine Nutzer:in das Canvas aufruft, und nicht auf dem Zeitpunkt einzelner Nachrichten. Braze erfasst Konversionen auch während Verzögerungszeiten zwischen Nachrichten in Canvas.

### Primäres Konversionsereignis

Das primäre Konversions-Event ist das erste Ereignis, das Sie während der Erstellung von Kampagnen oder Canvas hinzufügen. Es hat den größten Einfluss auf Engagement und Berichterstattung. Braze verwendet Ihr primäres Konversions-Event, um:

- Berechnen Sie die siegreiche Variation der Nachrichten in [multivariaten]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) Kampagnen oder Canvase.
- Legen Sie das Zeitfenster fest, in dem die Einnahmen für die Kampagne oder das Canvas berechnet werden.
- Passen Sie die Verteilung von Nachrichten für Kampagnen und Canvase mithilfe der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) an.

Das primäre Konversions-Event-Ereignis ist die Anzahl der aufgetretenen Konversions-Events. Bei Multichannel-Kampagnen zählt Braze die Konversionen pro Kanal (wie in [den Regeln für das Conversion-Tracking](#conversion-tracking-rules) beschrieben), was bedeutet, dass die Anzahl der Konversionen die Anzahl der eindeutigen Nutzer:innen übersteigen und zu Konversionsraten von über 100 % führen kann. Braze berechnet die primäre Konversions-Event-Rate, indem diese Anzahl durch die Anzahl der eindeutigen Empfänger:innen dividiert wird. Braze betrachtet einen Nutzer:in als Empfänger:in, wenn die Nachricht gesendet oder angezeigt wird, je nach Kanal. Beispielsweise wird eine Nutzer:in in Push- oder E-Mail-Benachrichtigungen zum Empfänger:in, nachdem Braze die Nachricht versendet hat. Bei In-App-Nachrichten oder Content-Cards muss der Nutzer die Nachricht anzeigen, um als Empfänger:in zu gelten.

{% alert note %}
Wenn Sie Nachrichten mithilfe des `abort`Liquid-Tags abbrechen, bricht Braze Nachrichten nur für Nutzer:innen ab, die Varianten durchlaufen. Nachrichten an Nutzer:innen in der Kontrollgruppe werden nicht abgebrochen, was zu verzerrten Prozentsätzen der Konversion zwischen Varianten und Kontrollgruppen führen kann. Als Abhilfe verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), um Ihre Benutzer bei der Eingabe von Kampagnen und Canvas anzusprechen.
{% endalert %}

## Erstellen einer Kampagne mit Konversion Tracking

### Schritt 1: Richten Sie Ihre Kampagne ein

[Erstellen Sie eine Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) für Ihren gewünschten Nachrichtenkanal. Nachdem Sie die Nachrichten und den Zeitplan Ihrer Kampagne festgelegt haben, können Sie bis zu vier Konversions-Events zum Tracking hinzufügen.

Verwenden Sie so viele Konversions-Events wie erforderlich. Das Hinzufügen eines zweiten oder dritten Konversions-Events bereichert Ihre Berichterstattung erheblich. Bei einer Kampagne, die sich an passive Nutzer:innen richtet, können Sie beispielsweise durch Hinzufügen eines sekundären Konversions-Events neben dem primären Konversions-Event **„Sitzung starten“** besser nachvollziehen, wie effektiv Ihre Kampagne dabei ist, Nutzer:innen zurück in Ihre Anwendung zu holen. 

### Schritt 2: Hinzufügen der Konversions-Events

Wählen Sie zunächst den allgemeinen Ereignistyp aus, den Sie verwenden möchten:

| Konversions-Event Typ   | Beschreibung                |
|-------------------------|----------------------------|
| **Startet Sitzung**      | Ein Benutzer zählt als Konversion, wenn er eine der von Ihnen angegebenen Apps öffnet (standardmäßig sind das alle Apps im Workspace).|
| **Kauft etwas**      | Eine Nutzer:in wird als konvertiert gezählt, wenn sie ein [Kauf-Event]({{site.baseurl}}/api/objects_filters/purchase_object/) verzeichnet. Dies erfasst standardmäßig alle Käufe, oder Sie können ein bestimmtes Produkt angeben.|
| **Bestellung wird aufgegeben**        | Eine Nutzer:in wird als konvertiert gezählt, wenn sie das [von E-Commerce empfohlene Ereignis „Bestellung aufgegeben“]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events) triggert. Standardmäßig wird das Tracking für alle Bestellungen durchgeführt, oder Sie können nach einem bestimmten Produkt filtern.<br><br>Das Event „Places Order“ befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten. |
| **Führt angepasstes Event aus**| Ein Benutzer zählt als Konversion, wenn er eines Ihrer benutzerdefinierten Ereignisse ausführt (keine Standardeinstellung, Sie müssen das Ereignis angeben).|
| **App upgraden**         | Ein Benutzer zählt als Konversion, wenn er die eine der von Ihnen angegebenen Apps aktualisiert (standardmäßig sind das alle Apps im Workspace). Braze führt einen numerischen Best-Efforts-Vergleich durch, um festzustellen, ob es sich bei der Änderung um ein Upgrade handelt. Nicht-numerische Versionen werden als Konversion gezählt, wenn sich die Version ändert.|
| **Öffnet E-Mail**         | Ein Benutzer zählt als Konversion, wenn er die E-Mail öffnet (nur bei E-Mail-Kampagnen).|
| **Klickt E-Mail an**        | Ein Benutzer zählt als Konversion, wenn er auf einen Link in der E-Mail klickt (nur bei E-Mail-Kampagnen).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Verschachtelte Eigenschaften werden in Konversions-Events nicht unterstützt**. Sie können in Konversions-Events keine verschachtelten Eigenschaften verwenden. Wenn beispielsweise`product_code`  oder  verschachtelte `product_name`Eigenschaften innerhalb eines`products`  Arrays sind (wie z. B. `products[].product_code`), können Sie diese nicht verwenden, um zu überprüfen, ob ein bestimmter Produktkauf in einem Konversions-Event getätigt wurde.
{% endalert %}

Setzen Sie sich eine Konversionsfrist. Dies ist die maximale Zeitspanne, die vergehen kann, bevor Braze eine Konversion berücksichtigt. Sie können einen Zeitraum von bis zu 30 Tagen festlegen, in dem Braze die Konversion zählt, wenn die Nutzer:innen die angegebene Aktion ausführen.

![Der Ereignistyp "Kauf tätigen" erfasst z. B. Benutzer als Konversion, die einen Kauf tätigen. Die Frist beträgt 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, fahren Sie mit der Kampagnenerstellung fort und beginnen mit dem Versand Ihrer Kampagne.

### Schritt 3: Ihre Ergebnisse ansehen

Bitte gehen Sie zur Seite **„Details“,** um die Einzelheiten zu jedem Konversions-Event anzuzeigen, das mit der von Ihnen erstellten Kampagne verbunden ist. Unabhängig der ausgewählten Konversions-Events können Sie auch den Gesamtumsatz einsehen, der dieser spezifischen Kampagne sowie bestimmten Varianten während des Zeitfensters des primären Konversions-Events zugeordnet wurde.

{% alert note %}
Wenn Sie bei der Erstellung einer Kampagne keine Konversions-Events auswählen, wird standardmäßig eine Dauer von drei Tagen festgelegt.
{% endalert %}

Bei Nachrichten mit mehreren Varianten können Sie außerdem die Anzahl und relative Häufigkeit der Konversionsereignisse für Ihre Kontrollgruppe und die einzelnen Varianten einsehen.

![Vier Konversions-Events, die Konversionen auf der Grundlage der folgenden Kriterien verfolgen: Kauf innerhalb von drei Stunden, Kauf innerhalb von zwei Stunden, Beginn einer Sitzung innerhalb von 30 Minuten und Beginn einer Sitzung innerhalb von 25 Minuten.]({% image_buster /assets/img_archive/conversion_event_details.png %})