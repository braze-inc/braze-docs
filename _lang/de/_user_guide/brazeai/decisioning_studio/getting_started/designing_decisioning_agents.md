---
nav_title: Entwurf von Entscheidungsagenten
article_title: Entwurf von Entscheidungsagenten
page_order: 4
page_type: reference
description: "Dieser referenzierte Artikel behandelt die wichtigsten Konzepte und bewährten Verfahren für die Gestaltung und Konfiguration Ihres Entscheidungsagenten."
---

# Entwurf von Entscheidungsagenten

> Dieser referenzierte Artikel behandelt die wichtigsten Konzepte und bewährten Verfahren für die Gestaltung und Konfiguration Ihres Entscheidungsagenten.

## Über Entscheidungsfindungsagenten

Der Entwurf Ihres Entscheidungsagenten ist der erste Schritt bei der Einrichtung von Decisioning Studio. Damit der entscheidungsbefugte Agent Entscheidungen treffen kann, müssen Sie festlegen, welches Ergebnis Sie maximieren möchten und welche Aktionen der Agent dazu durchführen kann.

### Wichtige Konzepte

Auf die folgenden Begriffe wird im gesamten Decisioning Studio Handbuch referenziert.

| Term | Definition |
| --- | --- |
| **Entscheidender Agent** | Ein Decisioning Agent ist eine angepasste Konfiguration für BrazeAI Decisioning Studio™, die auf ein bestimmtes Geschäftsziel zugeschnitten ist. Dies wird durch die Erfolgsmetrik, die Dimensionen und die von Ihnen gewählten Optionen definiert. |
| **Erfolgsmetrik** | Die spezifische Metrik, für die Sie optimieren möchten, z. B. Umsatz, Konversionen oder durchschnittlicher Umsatz pro Nutzer:innen (ARPU). Dies ist die Metrik, die der entscheidungsbefugte Agent durch seine Handlungen zu maximieren versucht. |
| **Format** | Dimensionen kann man sich als die *Arten von Hebeln* vorstellen, die der entscheidungsbefugte Agent ziehen kann, um die Erfolgsmetrik zu maximieren. Typische Dimensionen sind Angebot, Betreffzeile, Kreativ, Kanal oder Sendezeit. |
| **Action Bank** | Die Aktionsbank definiert die *spezifischen Optionen*, die dem Entscheidungsagenten für jede Dimension "Hebel" zur Verfügung stehen. Für eine Kanaldimension würden Sie zum Beispiel die spezifischen Kanäle definieren, auf die der Entscheidungsagent Zugriff hat. Für eine Angebotsdimension würden Sie die spezifischen Angebote definieren, die der Entscheidungsträger testen kann. 
| **Einschränkungen** | Im Allgemeinen kann der Entscheidungsagent jede beliebige Kombination von Aktionen ausführen, die Sie in der Aktionsbank hinterlegen. Sie können jedoch auch Einschränkungen definieren, um die Aktionen des Entscheidungsagenten auf die Einhaltung wichtiger Geschäftsregeln zu beschränken. So kann beispielsweise verhindert werden, dass ein bestimmtes Angebot für Kund:in einer nicht zugelassenen Region ausgewählt wird, oder es kann ein maximales Budget festgelegt werden, das der Entscheidungsträger ausgeben darf. 
{: .reset-td-br-1 .reset-td-br-2}

![Eine Übersicht über einen Entscheidungsagenten auf hoher Ebene]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
Der Decisioning Agent kann nur Aktionen ausführen, die *Sie* konfigurieren und zur Aktionsbank hinzufügen. Das bedeutet, dass alle möglichen Aktionen durch die Kombinationen dessen, was Sie in die Aktionsbank legen, definiert sind.
{% endalert %}

## Wie Sie Ihren Entscheidungsagenten gestalten

Wenn Sie einen Entscheidungsagenten einrichten, müssen Sie vier wesentliche Gestaltungselemente berücksichtigen:

### Das "Ziel": Definieren Sie Ihre Erfolgsmetrik

> Welches Ergebnis möchten Sie, dass der Agent maximiert?

Ihre Metrik für den Erfolg ist das Geschäftsergebnis, für das der Agent optimieren wird. Dies sollte sich direkt an Ihren Geschäftszielen orientieren - nicht an Metriken wie Klicks oder Öffnungen, sondern an echten Geschäftsergebnissen wie Umsatz, Konversionen, ARPU oder Lifetime-Value der Kund:in.

### Das "Wer": Wählen Sie Ihre Zielgruppe aus

> Wen wird der Entscheidungsträger engagieren?

Definieren Sie die Zielgruppe, die Ihr Agent bedienen soll. Das können alle Kunden sein, ein bestimmtes Segment (z.B. Mitglieder eines Kundenbindungs-Programms) oder Kunden in einer bestimmten Phase ihres Lebenszyklus (z.B. Neukunden oder gefährdete Abonnenten).

### Das "Was": Konfigurieren Sie Ihre Aktionsbank

> Aus welchen Optionen kann der Agent wählen, um das Ergebnis zu steuern?

Die Aktionsbank definiert alle Hebel, die der Agent betätigen kann - die Dimensionen (wie Kanal, Angebot, Zeitpunkt und Häufigkeit) und die spezifischen Optionen innerhalb jeder Dimension. Der Agent experimentiert mit verschiedenen Kombinationen dieser Optionen, um herauszufinden, was für jeden Kunden am besten funktioniert.

### Das "Wie": Konfigurieren Sie Ihre Beschränkungen

> Welche Regeln sollte der Agent befolgen?

Beschränkungen sind die Regeln, die der Agent befolgen muss. So können Sie z.B. verhindern, dass ein bestimmtes Angebot für Kund:in einer nicht zugelassenen Region ausgewählt wird, oder ein maximales Budget festlegen, das der Entscheidungsträger ausgeben darf.

## Bewährte Praktiken und Beispiele

Um die Wirkung Ihres Entscheidungsfindungsmittels zu maximieren, sollten Sie:

- Wählen Sie eine Metrik, die sich eng an Ihren Geschäftszielen orientiert, z.B. Umsatz, Konversion oder ARPU.
- Konzentrieren Sie sich auf die Dimensionen oder "Hebel", die Sie testen möchten, wie z.B. Angebot, Betreffzeile, Kreativität, Kanal oder Versandzeitpunkt, die am ehesten einen signifikanten Einfluss auf die Erfolgsmetrik haben.
- Wählen Sie für jede Dimension die Optionen aus, z.B. E-Mail versus SMS oder tägliche versus wöchentliche Häufigkeit, die am ehesten einen signifikanten Einfluss auf die Erfolgsmetrik haben.

Einige Beispiele für Entscheidungsagenten, die Sie erstellen können, sind:

{% tabs %}
{% tab Repeat purchase agent %}
Sie könnten einen Agenten für Wiederholungskäufe einrichten, um die Konversion nach einem Erstverkauf zu erhöhen:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet für jede Kund:in verschiedene Kombinationen von Produktangeboten, Zeitpunkt und Häufigkeit von Nachrichten.
- Mit der Zeit lernt BrazeAI™, was für jeden Kunden:in am besten funktioniert.
- Orchestrierung von personalisierten Sendungen über Braze zur Maximierung der Wiederkaufsraten
{% endtab %}
{% tab Cross-sell or upsell agent %}
Sie könnten einen Cross-Sell- oder Upsell-Agenten entwickeln, um den durchschnittlichen Umsatz pro Nutzer:innen (ARPU) aus Internet-Abonnements zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet für jede Kund:in verschiedene Kombinationen von Nachrichten, Sendezeiten, Rabatten und Tarifangeboten.
- BrazeAI™ lernt, welche Kund:innen für Leapfrog-Angebote empfänglich sind und welche Rabatte oder andere Anreize für ein upgraden benötigen.
- Orchestriert personalisierte Sendungen über Braze, um den ARPU zu maximieren
{% endtab %}
{% tab Renewal and retention agent %}
Sie könnten einen Agenten für Vertragsverlängerungen und Bindungen entwickeln, um Vertragsverlängerungen zu sichern und sowohl die Vertragsdauer als auch den Kapitalwert zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Verlängerungsangebote für jede Kund:in.
- BrazeAI™ identifiziert Kund:innen, die weniger preissensibel sind und weniger starke Rabatte für eine Verlängerung benötigen.
- Orchestrierung personalisierter Sendungen über Braze zur Maximierung von Vertragsverlängerungen und Kapitalwert
{% endtab %}
{% tab Winback agent %}
Sie könnten einen Winback-Agenten einrichten, um die Reaktivierung zu erhöhen, indem Sie frühere Abonnent:innen dazu ermutigen, sich erneut anzumelden:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet dabei Tausende von Variablen auf einmal, einschließlich Kreativität, Nachricht, Kanal und Kadenz.
- BrazeAI™ findet die beste Kombination für jede einzelne Kund:in
- Orchestriert personalisierte Sendungen über Braze, um die Reaktivierungsraten zu maximieren
{% endtab %}
{% tab Referral agent %}
Sie könnten einen Empfehlungsagenten einrichten, um die Zahl der durch Empfehlungen bestehender Kund:innen eröffneten neuen Konten zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet für jede Kund:in verschiedene E-Mails, Werbemittel, Sendezeiten und Kreditkartenangebote.
- BrazeAI™ bestimmt die ideale Kombination für bestimmte Kund:innen
- Orchestrierung von personalisierten Sendungen über Braze zur Maximierung der Konversionen von Empfehlungen
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Sie könnten einen Lead Nurturing- und Konversions-Agenten erstellen, um den Umsatz zu steigern und den richtigen Betrag für jede Kund:in zu zahlen:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Segmente, Gebotsmethoden, Gebotsstufen und kreative Elemente.
- BrazeAI™ nutzt robuste First-Party-Daten zur Optimierung der Performance von bezahlten Anzeigen bei sich ändernden Richtlinien zum Datenschutz
- Orchestrierung von personalisierten Sendungen über Braze zur Maximierung des Umsatzes bei gleichzeitiger Optimierung der Kosten pro Kund:in
{% endtab %}
{% tab Loyalty and engagement agent %}
Sie könnten einen Kundenbindungs- und Engagement-Agenten erstellen, um die Käufe neuer Kund:in in einem Kundenbindungs-Programm zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet für jede Kund:in verschiedene E-Mail-Angebote, Sendezeiten und -frequenzen.
- BrazeAI™ lernt, was für jeden neuen Teilnehmer des Kundenbindungs-Programms am besten funktioniert
- Orchestrierung von personalisierten Sendungen über Braze zur Maximierung der Kauf- und Wiederkaufsraten
{% endtab %}
{% endtabs %}

## Nächste Schritte

Sind Sie bereit, Ihren eigenen Entscheidungsagenten zu erstellen? Folgen Sie den nächsten Schritten für Ihre Decisioning Studio-Ebene:

- **Decisioning Studio Go**: [Decisioning Studio Go einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Decisioning Studio Pro einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Diese Anleitungen führen Sie durch die Verbindung von Datenquellen, die Einrichtung der Orchestrierung, das Design Ihres Agenten und den Start der Produktion.
