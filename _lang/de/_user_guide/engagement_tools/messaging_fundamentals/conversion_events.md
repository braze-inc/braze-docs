---
nav_title: Konversions-Events
article_title: Konversions-Events
page_order: 4
page_type: reference
description: "Dieser referenzierende Artikel definiert Konversions-Events, wie Sie damit Ihre Metriken für den Erfolg in Braze definieren und wie Sie diese Events nutzen können, um zu sehen, wie engagiert Ihre Nutzer:innen sind."
tool:
    - Campaigns
    - Canvas
---

# Konversions-Events

> Ein Konversions-Event ist eine Art Erfolgsmetrik, die verfolgt, ob ein Empfänger Ihres Messagings innerhalb eines bestimmten Zeitraums nach Erhalt Ihres Engagements eine hochwertige Aktion durchführt. Nutzen Sie diese Ereignisse, um sicherzustellen, dass Sie relevante, nützliche Informationen sammeln, die Sie später nutzen können, um Insights für Ihre Kampagne oder Ihr Canvas zu gewinnen.

## Funktionsweise

Angenommen, Sie erstellen eine personalisierte Urlaubskampagne für aktive Nutzer:innen. Dann könnte ein Konversions-Event wie " **Starten Sie eine Sitzung** innerhalb von zwei oder drei Tagen" angemessen sein, da Sie auf diese Weise ein Gefühl für das Engagement der Nutzer:innen beim Empfang Ihrer Nachricht bekommen. Weitere Ereignisse wie **Kauf tätigen**, **App aktualisieren** oder benutzerdefinierte Ereignisse können ebenfalls als Konversionsereignisse ausgewählt werden.

{% alert tip %}
Wenn Sie mehr über Konversionen erfahren möchten, lesen Sie unseren [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen.
{% endalert %}

### Regeln zum Konversionstracking

Konversionsereignisse ermöglichen es, Nutzeraktionen auf einen bestimmten Punkt der Interaktion zurückzuführen. Allerdings gibt es ein paar Dinge zu beachten, wenn es darum geht, wie Braze mit Mehrfachkonvertierungen umgeht. In den folgenden Beispielen wird gezeigt, wie Braze diese Konversionen verfolgt:

- Die Konversion erfolgt pro Benutzer, nicht pro Gerät. Das bedeutet, dass ein Benutzer nur einmal als Konversionsereignis gezählt wird, auch wenn eine Nachricht an mehrere Geräte gesendet wird. Ein weiteres Beispiel: Nehmen wir an, eine Kampagne hat nur ein Conversion-Ereignis, nämlich "Tätigt einen Kauf". Wenn ein Nutzer, der diese Kampagne erhält, innerhalb der Umwandlungsfrist zwei separate Käufe tätigt, wird nur eine Umwandlung gezählt.
- Wenn ein Benutzer ein Konversionsereignis innerhalb der Frist für zwei separate Kampagnen oder Canvases durchführt, wird diese Konversion bei beiden registriert.
- Eine Konversion wird auch dann festgestellt, wenn ein Benutzer das jeweilige Konversionsereignis im Fenster durchführt, auch wenn er die Nachricht nicht geöffnet oder angeklickt hat.
- Bei Canvase funktioniert das Tracking der Konversion auf der Grundlage der endgültigen Konversionsfrist, die beginnt, wenn ein Nutzer:innen das Canvas betritt, und nicht auf der Grundlage der einzelnen Nachrichten. Das bedeutet, dass Konversionen auch bei Verzögerungen zwischen Nachrichten in Canvas gezählt werden können.

### Primäres Konversionsereignis

Das primäre Konversionsereignis  ist das erste Ereignis, das bei der Erstellung einer Kampagne oder eines Canvas hinzugefügt wird. Es hat den größten Einfluss auf Engagement und Berichterstattung. Das können Sie mit primären Konversionsereignissen tun:

- Berechnen Sie die siegreiche Variation der Nachrichten in [multivariaten]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) Kampagnen oder Canvase.
- Legen Sie das Zeitfenster fest, in dem die Einnahmen für die Kampagne oder das Canvas berechnet werden.
- Passen Sie die Verteilung von Nachrichten für Kampagnen und Canvase mithilfe der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) an.

{% alert note %}
Wenn Nachrichten mit dem Liquid-Tag `abort` abgebrochen werden, werden nur die Benutzer, die die Varianten durchgehen, potenziell abgebrochen. Das bedeutet, dass die Nachrichten an Benutzer, die die Kontrollgruppe durchlaufen, nicht abgebrochen werden, was zu verzerrten Konvertierungsprozentsätzen zwischen Varianten und Kontrollgruppen führen kann. Als Abhilfe verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), um Ihre Benutzer bei der Eingabe von Kampagnen und Canvas anzusprechen.
{% endalert %}

## Erstellen einer Kampagne mit Konversion Tracking

### Schritt 1: Richten Sie Ihre Kampagne ein

[Erstellen Sie eine Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) für Ihren gewünschten Nachrichtenkanal. Wenn Sie die Nachrichten und den Zeitplan für Ihre Kampagne festgelegt haben, können Sie bis zu vier Konvertierungsereignisse verfolgen.

Wir empfehlen Ihnen, so viele Konversions-Ereignisse zu verwenden, wie Sie für notwendig erachten, da die Hinzufügung eines zweiten (oder dritten) Konversions-Ereignisses Ihre Berichterstattung erheblich bereichern kann. Angenommen, Sie haben eine Kampagne, die auf passive Nutzer abzielt. In diesem Fall können Sie durch Hinzufügen eines sekundären Conversion-Ereignisses und des primären Conversion-Ereignisses **"Starts Session"** besser verstehen, wie effektiv Ihre Kampagne Ihre Benutzer zurück in Ihre Anwendung bringt. 

### Schritt 2: Hinzufügen der Konversions-Events

Wählen Sie zunächst den allgemeinen Ereignistyp aus, den Sie verwenden möchten:

| Konversions-Event Typ         | Beschreibung                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Startet Sitzung**      | Ein Benutzer zählt als Konversion, wenn er eine der von Ihnen angegebenen Apps öffnet (standardmäßig sind das alle Apps im Workspace).                                                                                                                                                                                                         |
| **Kauft etwas**      | Ein Benutzer zählt als Konversion, wenn er das von Ihnen angegebene Produkt kauft (standardmäßig sind das alle Produkte).                                                                                                                                                                                                                                 |
| **Führt angepasstes Event aus** | Ein Benutzer zählt als Konversion, wenn er eines Ihrer benutzerdefinierten Ereignisse ausführt (keine Standardeinstellung, Sie müssen das Ereignis angeben).                                                                                                                                                                                                        |
| **App upgraden**         | Ein Benutzer zählt als Konversion, wenn er die eine der von Ihnen angegebenen Apps aktualisiert (standardmäßig sind das alle Apps im Workspace). Braze führt einen numerischen Best-Efforts-Vergleich durch, um festzustellen, ob es sich bei der Änderung um ein Upgrade handelt. Nicht-numerische Versionen werden als Konversion gezählt, wenn sich die Version ändert.              |
| **Öffnet E-Mail**         | Ein Benutzer zählt als Konversion, wenn er die E-Mail öffnet (nur bei E-Mail-Kampagnen).                                                                                                                                                                                                                                                 |
| **Klickt E-Mail an**        | Ein Benutzer zählt als Konversion, wenn er auf einen Link in der E-Mail klickt (nur bei E-Mail-Kampagnen).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Setzen Sie sich eine Konversionsfrist. Das ist die maximale Zeitspanne, die bis zur Konversion vergehen darf. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen einzuräumen, in dem es als Konversion zählt, wenn der Benutzer die angegebene Aktion durchführt.

![Der Konversions-Event-Typ "Tätigt einen Kauf" als Beispiel für die Aufzeichnung von Konversionen für Nutzer:innen, die einen Kauf tätigen. Die Frist beträgt 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, fahren Sie mit der Kampagnenerstellung fort und beginnen mit dem Versand Ihrer Kampagne.

### Schritt 3: Ihre Ergebnisse ansehen

Gehen Sie auf die Seite **Details**, um die Details für jedes Conversion-Ereignis anzuzeigen, das mit der soeben erstellten Kampagne verbunden ist. Unabhängig von den von Ihnen ausgewählten Konversionsereignissen können Sie auch die Gesamteinnahmen sehen, die dieser spezifischen Kampagne sowie bestimmten Varianten während des Zeitfensters des primären Konversionsereignisses zugeschrieben werden können.

{% alert note %}
Wenn bei der Erstellung der Kampagne keine Konversionsereignisse ausgewählt werden, wird die Zeit auf drei Tage voreingestellt.
{% endalert %}

Bei Nachrichten mit mehreren Varianten können Sie außerdem die Anzahl und relative Häufigkeit der Konversionsereignisse für Ihre Kontrollgruppe und die einzelnen Varianten einsehen.

![Vier Konversions-Events, die Konversionen tracken, basierend darauf, wann ein Kauf innerhalb von drei Stunden getätigt wurde, ein Kauf innerhalb von zwei Stunden getätigt wurde, eine Sitzung innerhalb von 30 Minuten begonnen wurde und eine Sitzung innerhalb von 25 Minuten begonnen wurde.]({% image_buster /assets/img_archive/conversion_event_details.png %})


