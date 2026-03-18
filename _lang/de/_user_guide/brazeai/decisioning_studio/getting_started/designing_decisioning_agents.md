---
nav_title: Entwurf von Entscheidungsagenten
article_title: Entwurf von Entscheidungsagenten
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt wichtige Konzepte und bewährte Verfahren für die Gestaltung und Konfiguration Ihres Entscheidungsagenten."
---

# Entwurf von Entscheidungsagenten

> Dieser Referenzartikel behandelt wichtige Konzepte und bewährte Verfahren für die Gestaltung und Konfiguration Ihres Entscheidungsagenten.

## Über Entscheidungsträger

Die Gestaltung Ihres Entscheidungsagenten ist der erste Schritt bei der Einrichtung von Decisioning Studio. Damit der Entscheidungsagent Entscheidungen treffen kann, müssen Sie definieren, welches Ergebnis Sie maximieren möchten und welche Maßnahmen der Agent dazu ergreifen kann.

### Wichtige Konzepte

Die folgenden Begriffe werden im gesamten Decisioning Studio-Handbuch referenziert.

| Term | Definition |
| --- | --- |
| **Entscheidungsträger** | Ein Entscheidungsagent ist eine angepasste Konfiguration für BrazeAI Decisioning Studio™, die speziell auf ein bestimmtes Geschäftsziel zugeschnitten ist. Dies wird durch die von Ihnen gewählten Metriken, Dimensionen und Optionen bestimmt. |
| **Erfolgsmetriken** | Die spezifische Geschäftsmetrik, die Sie optimieren möchten, wie beispielsweise Umsatz, Konversionen oder durchschnittlicher Umsatz pro Nutzer:in (ARPU). Dies ist die Metrik, die der Entscheidungsträger durch seine Maßnahmen zu maximieren versucht. |
| **Format** | Dimensionen können als *Hebel* betrachtet werden, die der Entscheidungsträger betätigen kann, um die Erfolgsmetrik zu maximieren. Typische Dimensionen umfassen Angebot, Betreffzeile, Kreativkonzept, Kanal oder Versandzeitpunkt. |
| **Aktionsbank** | Die Aktionsbank definiert die *spezifischen Optionen*, auf die der Entscheidungsagent für jede Dimension „Hebel“ Zugriff hat. Für eine Kanal-Dimension würden Sie beispielsweise die spezifischen Kanäle definieren, auf die der Entscheidungsagent Zugriff hat. Für eine Angebotsdimension würden Sie die spezifischen Angebote definieren, die der Entscheidungsagent testen kann. 
| **Einschränkungen** | Im Allgemeinen kann der Entscheidungsagent jede beliebige Kombination von Aktionen ausführen, die Sie in der Aktionsbank hinterlegt haben. Sie können jedoch auch Einschränkungen definieren, um die Handlungen des Entscheidungsagenten zu begrenzen und wichtige Geschäftsregeln einzuhalten. Dies könnte beispielsweise bedeuten, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region nicht ausgewählt werden kann oder dass ein maximales Budget für den Entscheidungsträger festgelegt wird. 
{: .reset-td-br-1 .reset-td-br-2}

![Eine allgemeine Übersicht über einen Entscheidungsagenten]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
Der Entscheidungsagent kann nur Maßnahmen ergreifen, die *Sie* konfigurieren und zur Maßnahmenbank hinzufügen. Dies bedeutet, dass alle möglichen Aktionen durch die Kombinationen definiert werden, die Sie in die Aktionsbank einfügen.
{% endalert %}

## Wie Sie Ihren Entscheidungsagenten gestalten

Bei der Einrichtung eines Entscheidungsagenten müssen Sie vier wesentliche Designelemente berücksichtigen:

### Das Ziel: Definieren Sie Ihre Erfolgsmetrik

> Welches Ergebnis möchten Sie, dass der Agent maximiert?

Ihre Erfolgsmetrik ist das Geschäftsergebnis, das der Agent optimieren wird. Dies sollte direkt mit Ihren Geschäftszielen übereinstimmen – nicht mit Ersatz-Metriken wie Klicks oder Öffnungen, sondern mit tatsächlichen Geschäftsergebnissen wie Umsatz, Konversionen, ARPU oder Lifetime-Value.

### Das "Wer": Bitte wählen Sie Ihre Zielgruppe aus.

> Wen wird der Entscheidungsträger einbeziehen?

Definieren Sie die Zielgruppen, die Ihr Agent bedienen soll. Dies können alle Kund:innen, ein bestimmtes Segment (z. B. Mitglieder eines Kundenbindungs-Programms) oder Kund:innen in einer bestimmten Phase ihres Lebenszyklus (z. B. Neukunden:innen oder gefährdete Abonnent:innen) sein.

### Das "Was": Bitte konfigurieren Sie Ihre Aktionsbank.

> Welche Optionen stehen dem Agenten zur Verfügung, um das Ergebnis zu beeinflussen?

Die Aktionsbank definiert alle Hebel, die der Agent betätigen kann – die Dimensionen (wie Kanal, Angebot, Zeitpunkt und Häufigkeit) und die spezifischen Optionen innerhalb jeder Dimension. Der Mitarbeiter testet verschiedene Kombinationen dieser Optionen, um die für jeden Kunden optimale Lösung zu ermitteln.

### Das "Wie": Bitte konfigurieren Sie Ihre Einschränkungen.

> Welche Regeln sollte der Makler beachten?

Einschränkungen sind die Regeln, die der Agent befolgen muss. Dies könnte beispielsweise verhindern, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region ausgewählt wird, oder es könnte ein maximales Budget festgelegt werden, das der Entscheidungsagent ausgeben darf.

## Bewährte Verfahren und Beispiele

Um die Wirkung Ihres Entscheidungsagenten zu maximieren, sollten Sie Folgendes beachten:

- Wählen Sie eine Metrik, die eng mit Ihren Geschäftszielen und -vorgaben übereinstimmt, wie beispielsweise Umsatz, Konversionen oder ARPU.
- Konzentrieren Sie sich auf die zu testenden Dimensionen oder „Hebel“ wie Angebot, Betreffzeile, Kreativität, Kanal oder Versandzeitpunkt, die sich am ehesten signifikant auf die Erfolgskennzahl auswirken.
- Wählen Sie für jede Dimension die Optionen aus, die sich voraussichtlich am stärksten auf die Erfolgskennzahl auswirken, beispielsweise E-Mail oder SMS, tägliche oder wöchentliche Häufigkeit.

Beispiele für Entscheidungsagenten, die Sie erstellen könnten, sind:

{% tabs %}
{% tab Repeat purchase agent %}
Sie könnten einen Wiederholungskauf-Agenten erstellen, um die Folge-Konversionen nach einem ersten Verkauf zu steigern:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Das Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Kombinationen von Produktangeboten, Zeitpunkten für Nachrichten und Häufigkeit für jeden Kunden.
- Im Laufe der Zeit lernt BrazeAI™, was für jede Kund:in am besten geeignet ist.
- Durchführt die Orchestrierung von personalisierten Sendungen über Braze, um die Wiederkaufsraten zu maximieren.
{% endtab %}
{% tab Cross-sell or upsell agent %}
Sie könnten einen Cross-Selling- oder Upselling-Agenten entwickeln, um den durchschnittlichen Umsatz pro Nutzer:in (ARPU) aus Internet-Abo-Abonnements zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Das Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene Kombinationen von Nachrichten, Versandzeiten, Rabatten und Angeboten für jede Kund:in getestet werden.
- BrazeAI™ ermittelt, welche Kund:innen für Leapfrog-Angebote empfänglich sind und welche Kund:innen Rabatte oder andere Anreize benötigen, um zu upgraden.
- Orchestriert personalisierte Sendungen über Braze, um den ARPU zu maximieren.
{% endtab %}
{% tab Renewal and retention agent %}
Sie könnten einen Erneuerungs- und Bindung-Agenten entwickeln, um Vertragsverlängerungen zu sichern und sowohl die Vertragsdauer als auch den Barwert (NPV) zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Das Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Verlängerungsangebote für jeden Kunden.
- BrazeAI™ identifiziert Kund:innen, die weniger preissensibel sind und weniger hohe Rabatte benötigen, um ihren Vertrag zu verlängern.
- Koordiniert personalisierte Sendungen über Braze für die Orchestrierung, um Vertragsverlängerungen und den Nettogegenwartswert zu maximieren.
{% endtab %}
{% tab Winback agent %}
Sie könnten einen Rückgewinnungsagenten entwickeln, um die Reaktivierung zu erhöhen, indem Sie ehemalige Abonnent:innen dazu ermutigen, sich erneut anzumelden:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Decisioning Studio führt automatisch tägliche Experimente durch und testet dabei Tausende von Variablen gleichzeitig, darunter Kreativkonzepte, Nachrichten, Kanäle und Kadenz.
- BrazeAI™ ermittelt die optimale Kombination für jede einzelne Kund:in.
- Orchestriert personalisierte Sendungen über Braze, um die Reaktivierungsraten zu maximieren.
{% endtab %}
{% tab Referral agent %}
Sie könnten einen Empfehlungsagenten einrichten, um die Anzahl der neuen Konten zu maximieren, die durch Empfehlungen von Geschäftskreditkarten bestehender Kund:innen eröffnet werden:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene E-Mails, Werbemittel, Versandzeiten und Kreditkartenangebote für jeden Kunden getestet werden.
- BrazeAI™ ermittelt die optimale Kombination für bestimmte Kund:innen.
- Koordiniert personalisierte Sendungen über Braze, um die Konversion bei Empfehlungen zu maximieren.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Sie könnten einen Lead-Nurturing- und Konversion-Agenten entwickeln, um zusätzliche Einnahmen zu generieren und für jede Kund:in den angemessenen Betrag zu zahlen:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene Kundensegmente, Gebotsmethoden, Gebotsniveaus und kreative Inhalte getestet werden.
- BrazeAI™ nutzt zuverlässige First-Party-Daten, um die Performance bezahlter Anzeigen zu optimieren, wenn sich Datenschutzrichtlinien ändern.
- Koordiniert personalisierte Sendungen über Braze für die Orchestrierung, um den Umsatz zu maximieren und gleichzeitig die Kosten pro Kund:in zu optimieren.
{% endtab %}
{% tab Loyalty and engagement agent %}
Sie könnten einen Loyalitäts- und Engagement-Agenten entwickeln, um die Käufe von Neukunden in einem Kundenbindungs-Programm zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze.
- Decisioning Studio führt automatisch tägliche Experimente durch, testet verschiedene E-Mail-Angebote, Versandzeiten und Häufigkeiten für jeden Kunden.
- BrazeAI™ ermittelt, was für jeden neuen Teilnehmer des Kundenbindungs-Programms am besten geeignet ist.
- Koordiniert personalisierte Sendungen über Braze zur Orchestrierung der Kauf- und Wiederkaufsraten.
{% endtab %}
{% endtabs %}

## Nächste Schritte

Sind Sie bereit, Ihren eigenen Entscheidungsagenten zu erstellen? Bitte befolgen Sie die folgenden Schritte für Ihre Decisioning Studio-Stufe:

- **Entscheidungsstudio Go**: [Entscheidungstudio einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Entscheidungsstudio Pro**: [Entscheidungstool Pro einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Diese Anleitungen führen Sie durch die Verbindung von Datenquellen, die Einrichtung der Orchestrierung, die Gestaltung Ihres Agenten und die Inbetriebnahme in der Produktion.
