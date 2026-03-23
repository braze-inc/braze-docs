---
nav_title: Design your agent
article_title: Entwurf von Entscheidungsagenten
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt wichtige Konzepte und Best Practices für den Entwurf und die Konfiguration Ihres Entscheidungsagenten."
---

# Entwurf von Entscheidungsagenten

> Dieser Referenzartikel behandelt wichtige Konzepte und Best Practices für den Entwurf und die Konfiguration Ihres Entscheidungsagenten.

## Über Entscheidungsagenten

Der Entwurf Ihres Entscheidungsagenten ist der erste Schritt bei der Einrichtung von Decisioning Studio. Damit der Entscheidungsagent Entscheidungen treffen kann, müssen Sie definieren, welches Ergebnis Sie maximieren möchten und welche Aktionen der Agent dazu ergreifen kann.

### Wichtige Konzepte

Die folgenden Begriffe werden im gesamten Decisioning Studio-Handbuch referenziert.

| Begriff | Definition |
| --- | --- |
| **Entscheidungsagent** | Ein Entscheidungsagent ist eine angepasste Konfiguration für BrazeAI Decisioning Studio™, die speziell auf ein bestimmtes Geschäftsziel zugeschnitten ist. Dies wird durch die von Ihnen gewählte Erfolgsmetrik, Dimensionen und Optionen bestimmt. |
| **Erfolgsmetrik** | Die spezifische Geschäftsmetrik, die Sie optimieren möchten, wie beispielsweise Umsatz, Konversionen oder durchschnittlicher Umsatz pro Nutzer:in (ARPU). Dies ist die Metrik, die der Entscheidungsagent durch seine Aktionen zu maximieren versucht. |
| **Dimensionen** | Dimensionen können als die *Arten von Hebeln* betrachtet werden, die der Entscheidungsagent betätigen kann, um die Erfolgsmetrik zu maximieren. Typische Dimensionen umfassen Angebot, Betreffzeile, Kreativkonzept, Kanal oder Versandzeitpunkt. |
| **Aktionsbank** | Die Aktionsbank definiert die *spezifischen Optionen*, auf die der Entscheidungsagent für jeden Dimensions-„Hebel" Zugriff hat. Für eine Kanal-Dimension würden Sie beispielsweise die spezifischen Kanäle definieren, auf die der Entscheidungsagent Zugriff hat. Für eine Angebotsdimension würden Sie die spezifischen Angebote definieren, die der Entscheidungsagent testen kann. |
| **Einschränkungen** | Im Allgemeinen kann der Entscheidungsagent jede beliebige Kombination von Aktionen ausführen, die Sie in der Aktionsbank hinterlegt haben. Sie können jedoch auch Einschränkungen definieren, um die Aktionen des Entscheidungsagenten zu begrenzen und wichtige Geschäftsregeln einzuhalten. Dies könnte beispielsweise bedeuten, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region nicht ausgewählt werden kann, oder dass ein maximales Budget für den Entscheidungsagenten festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2}

![Eine allgemeine Übersicht über einen Entscheidungsagenten]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
Der Entscheidungsagent kann nur Aktionen ergreifen, die *Sie* konfigurieren und zur Aktionsbank hinzufügen. Das bedeutet, dass alle möglichen Aktionen durch die Kombinationen definiert werden, die Sie in die Aktionsbank einfügen.
{% endalert %}

## So entwerfen Sie Ihren Entscheidungsagenten

Bei der Einrichtung eines Entscheidungsagenten müssen Sie vier wesentliche Designelemente berücksichtigen:

### Das „Ziel": Definieren Sie Ihre Erfolgsmetrik

> Welches Ergebnis soll der Agent maximieren?

Ihre Erfolgsmetrik ist das Geschäftsergebnis, für das der Agent optimieren wird. Dies sollte direkt mit Ihren Geschäftszielen übereinstimmen – nicht mit Ersatz-Metriken wie Klicks oder Öffnungen, sondern mit tatsächlichen Geschäftsergebnissen wie Umsatz, Konversionen, ARPU oder Lifetime-Value.

### Das „Wer": Wählen Sie Ihre Zielgruppe aus

> Wen wird der Entscheidungsagent ansprechen?

Definieren Sie die Zielgruppe, die Ihr Agent bedienen soll. Dies können alle Kund:innen sein, ein bestimmtes Segment (z. B. Mitglieder eines Kundenbindungs-Programms) oder Kund:innen in einer bestimmten Phase ihres Lebenszyklus (z. B. Neukund:innen oder gefährdete Abonnent:innen).

### Das „Was": Konfigurieren Sie Ihre Aktionsbank

> Welche Optionen stehen dem Agenten zur Verfügung, um das Ergebnis zu beeinflussen?

Die Aktionsbank definiert alle Hebel, die der Agent betätigen kann – die Dimensionen (wie Kanal, Angebot, Zeitpunkt und Häufigkeit) und die spezifischen Optionen innerhalb jeder Dimension. Der Agent experimentiert mit verschiedenen Kombinationen dieser Optionen, um herauszufinden, was für jede Kund:in am besten funktioniert.

### Das „Wie": Konfigurieren Sie Ihre Einschränkungen

> Welche Regeln sollte der Agent befolgen?

Einschränkungen sind die Regeln, die der Agent befolgen muss. Dies könnte beispielsweise verhindern, dass ein bestimmtes Angebot für Kund:innen in einer nicht berechtigten Region ausgewählt wird, oder es könnte ein maximales Budget festgelegt werden, das der Entscheidungsagent ausgeben darf.

## Best Practices und Beispiele

Um die Wirkung Ihres Entscheidungsagenten zu maximieren, sollten Sie Folgendes beachten:

- Wählen Sie eine Erfolgsmetrik, die eng mit Ihren Geschäftszielen und -vorgaben übereinstimmt, wie beispielsweise Umsatz, Konversionen oder ARPU.
- Konzentrieren Sie sich auf die Dimensionen oder „Hebel", die getestet werden sollen – wie Angebot, Betreffzeile, Kreativkonzept, Kanal oder Versandzeitpunkt –, die sich voraussichtlich am stärksten auf die Erfolgsmetrik auswirken.
- Wählen Sie für jede Dimension die Optionen aus, die sich voraussichtlich am stärksten auf die Erfolgsmetrik auswirken, beispielsweise E-Mail versus SMS oder tägliche versus wöchentliche Häufigkeit.

Beispiele für Entscheidungsagenten, die Sie erstellen könnten:

{% tabs %}
{% tab Repeat purchase agent %}
Sie könnten einen Wiederholungskauf-Agenten erstellen, um die Folge-Konversionen nach einem ersten Kauf zu steigern:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Kombinationen von Produktangeboten, Nachrichtenzeitpunkten und Häufigkeiten für jede Kund:in
- Im Laufe der Zeit lernt BrazeAI<sup>TM</sup>, was für jede Kund:in am besten funktioniert
- Orchestriert personalisierte Sendungen über Braze, um die Wiederkaufsraten zu maximieren
{% endtab %}
{% tab Cross-sell or upsell agent %}
Sie könnten einen Cross-Selling- oder Upselling-Agenten entwickeln, um den durchschnittlichen Umsatz pro Nutzer:in (ARPU) aus Internet-Abos zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene Kombinationen von Nachrichten, Versandzeiten, Rabatten und Tarifangeboten für jede Kund:in getestet werden
- BrazeAI<sup>TM</sup> ermittelt, welche Kund:innen für Leapfrog-Angebote empfänglich sind und welche Rabatte oder andere Anreize benötigen, um zu upgraden
- Orchestriert personalisierte Sendungen über Braze, um den ARPU zu maximieren
{% endtab %}
{% tab Renewal and retention agent %}
Sie könnten einen Verlängerungs- und Bindungs-Agenten entwickeln, um Vertragsverlängerungen zu sichern und sowohl die Vertragsdauer als auch den Barwert (NPV) zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene Verlängerungsangebote für jede Kund:in
- BrazeAI<sup>TM</sup> identifiziert Kund:innen, die weniger preissensibel sind und weniger hohe Rabatte benötigen, um ihren Vertrag zu verlängern
- Orchestriert personalisierte Sendungen über Braze, um Vertragsverlängerungen und den NPV zu maximieren
{% endtab %}
{% tab Winback agent %}
Sie könnten einen Rückgewinnungsagenten entwickeln, um die Reaktivierung zu erhöhen, indem Sie ehemalige Abonnent:innen dazu ermutigen, sich erneut anzumelden:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet dabei Tausende von Variablen gleichzeitig, darunter Kreativkonzepte, Nachrichten, Kanäle und Kadenz
- BrazeAI<sup>TM</sup> ermittelt die optimale Kombination für jede einzelne Kund:in
- Orchestriert personalisierte Sendungen über Braze, um die Reaktivierungsraten zu maximieren
{% endtab %}
{% tab Referral agent %}
Sie könnten einen Empfehlungsagenten einrichten, um die Anzahl der neuen Konten zu maximieren, die durch Empfehlungen von Geschäftskreditkarten bestehender Kund:innen eröffnet werden:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene E-Mails, Kreativkonzepte, Versandzeiten und Kreditkartenangebote für jede Kund:in getestet werden
- BrazeAI<sup>TM</sup> ermittelt die optimale Kombination für bestimmte Kund:innen
- Orchestriert personalisierte Sendungen über Braze, um die Konversionen bei Empfehlungen zu maximieren
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Sie könnten einen Lead-Nurturing- und Konversions-Agenten entwickeln, um zusätzlichen Umsatz zu generieren und für jede Kund:in den angemessenen Betrag zu zahlen:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch, bei denen verschiedene Kundensegmente, Gebotsmethoden, Gebotsniveaus und Kreativkonzepte getestet werden
- BrazeAI<sup>TM</sup> nutzt zuverlässige First-Party-Daten, um die Performance bezahlter Anzeigen zu optimieren, wenn sich Datenschutzrichtlinien ändern
- Orchestriert personalisierte Sendungen über Braze, um den Umsatz zu maximieren und gleichzeitig die Kosten pro Kund:in zu optimieren
{% endtab %}
{% tab Loyalty and engagement agent %}
Sie könnten einen Loyalitäts- und Engagement-Agenten entwickeln, um die Käufe von Neuanmeldungen in einem Kundenbindungs-Programm zu maximieren:

- Definieren Sie die Zielgruppe und die Nachricht in Braze
- Decisioning Studio führt automatisch tägliche Experimente durch und testet verschiedene E-Mail-Angebote, Versandzeiten und Häufigkeiten für jede Kund:in
- BrazeAI<sup>TM</sup> ermittelt, was für jede neue Teilnehmer:in des Kundenbindungs-Programms am besten funktioniert
- Orchestriert personalisierte Sendungen über Braze, um Kauf- und Wiederkaufsraten zu maximieren
{% endtab %}
{% endtabs %}

## Nächste Schritte

Sind Sie bereit, Ihren eigenen Entscheidungsagenten zu erstellen? Befolgen Sie die nächsten Schritte für Ihre Decisioning Studio-Stufe:

- **Decisioning Studio Go**: [Decisioning Studio Go einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)

Diese Anleitungen führen Sie durch das Verbinden von Datenquellen, die Einrichtung der Orchestrierung, den Entwurf Ihres Agenten und den Start in die Produktion.