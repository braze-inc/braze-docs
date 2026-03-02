---
nav_title: Agenten konzipieren
article_title: Agenten konzipieren
page_order: 3
description: "Lernen Sie, wie Sie einen BrazeAI Decisioning Studio Go-Agenten entwerfen, einschließlich der Definition von Zielgruppen, Dimensionen und Go-spezifischen Einschränkungen."
---

# Agenten konzipieren

> In diesem Artikel erfahren Sie, wie Sie Ihren Go-Agenten in Decisioning Studio gestalten, einschließlich der Definition Ihrer Zielgruppe, des Auswählens von Dimensionen und des Verständnisses der Go-spezifischen Möglichkeiten und Einschränkungen.

Grundlegende Konzepte zu Entscheidungsagenten - einschließlich Metriken für den Erfolg, Dimensionen, Aktionsbanken und Einschränkungen - finden Sie unter [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Go versus Pro Fähigkeiten

Decisioning Studio Go ist eine Selbstbedienungsplattform mit optimierten Funktionen im Vergleich zu Decisioning Studio Pro. Wenn Sie diese Unterschiede verstehen, können Sie einen effektiven Agenten im Rahmen von Go entwickeln.

| Fähigkeit | Entscheidungsfindung Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Erfolgsmetrik** | Nur Klicks | Beliebige geschäftliche Metriken (Umsatz, Konversionen oder ARPU) |
| **Format** | Begrenzte Aktionsbank | Unbegrenzte Dimensionen |
| **Unterstützte CEPs** | Braze, SFMC | Jeder CEP (nativ und angepasst) |
| **Kundendaten** | Nur Engagement | Alle 1P Daten |
| **Einrichtung** | Selbstbedienung | KI Entscheidungsfindung; Dienste unterstützen |
| **Experiment Gruppen** | Go + Zufallssteuerung + optional BAU | Vollständig anpassbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Gestalten Sie Ihren Go-Agenten

Wenn Sie einen Decisioning Studio Go-Agenten entwerfen, treffen Sie Entscheidungen in den folgenden Bereichen:

### Schritt 1: Definieren Sie Ihre Zielgruppe

Ihre Zielgruppe ist die Gruppe von Kund:in, die der Agent ansprechen soll. In Go werden die Zielgruppen in Ihrem CEP definiert:

{% tabs %}
{% tab Braze %}

**Definition der Zielgruppe in Braze:**

1. Erstellen Sie in Braze ein Segment, das die Kunden definiert, die der Agent ansprechen soll.
2. Wenn Sie Ihr Experimentiergerät im Portal Decisioning Studio Go konfigurieren, wählen Sie dieses Segment als Ihre Zielgruppe aus.

{% alert tip %}
Ziehen Sie in Erwägung, ein eigenes Segment für Ihren Decisioning Studio Go Experimenter zu erstellen, um Ihre Tests isoliert und messbar zu halten.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definition der Zielgruppe in SFMC:**

1. Konfigurieren Sie eine Datenerweiterung, die Ihre Zielgruppe enthält.
2. Stellen Sie sicher, dass diese Datenerweiterung täglich mit den neuesten Kundendaten aktualisiert wird.
3. Referenzieren Sie diese Datenerweiterung im Portal Decisioning Studio Go, wenn Sie Ihren Experimenter konfigurieren.

{% endtab %}
{% endtabs %}

### Schritt 2: Wählen Sie Ihre Abmessungen aus

Dimensionen sind die "Hebel", die der Agent betätigen kann, um das Kundenerlebnis zu personalisieren. Dazu gehören kreative Dimensionen wie Betreffzeile und Heldenbild sowie sendetypische Dimensionen wie die Häufigkeit der E-Mails oder die Tageszeit. 

{% alert note %}
Welche Dimensionen zur Verfügung stehen, hängt von Ihrem CEP und der Konfiguration Ihrer Kampagnen ab. Arbeiten Sie mit den Templates und Inhalten, die Sie in Ihrem CEP eingerichtet haben.
{% endalert %}

### Schritt 3: Konfigurieren Sie Ihre Aktionsbank

Die Aktionsbank definiert die spezifischen Optionen, die der Agent für jede Dimension wählen kann. Zum Beispiel:

- **E-Mail Templates**: Wählen Sie aus, welche Templates der Agent verwenden kann (diese müssen zuerst in Ihrem CEP konfiguriert werden)
- **Betreffzeilen**: Definieren Sie die Varianten der Betreffzeile, die der Agent testen kann
- **Sendezeiten**: Geben Sie die Zeitfenster an, aus denen der Agent wählen kann

### Schritt 4: Experimentiergruppen einrichten

Decisioning Studio Go erstellt automatisch Versuchsgruppen, um die Performance zu messen:

| Gruppe | Beschreibung |
|-------|-------------|
| **Entscheidungsfindung Studio Go** | Kunden, die KI-optimierte Empfehlungen erhalten |
| **Zufallssteuerung** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Basislinienvergleich) |
| **Business as Usual (optional)** | Kund:innen, die Ihre bestehende Kampagne erhalten (bei Vergleich mit der aktuellen Performance) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Stellen Sie für einen genauen Vergleich sicher, dass kein Kunde zu mehr als einer Versuchsgruppe gehören kann und dass die Kunden nach dem Zufallsprinzip den Gruppen zugewiesen werden, ohne dass es zu Verzerrungen kommt.
{% endalert %}

## Zu berücksichtigende Beschränkungen

Wenn Sie Ihren Go-Agenten entwerfen, sollten Sie diese Einschränkungen im Hinterkopf behalten:

- **Nur Klicks**: Go optimiert für Click-through-Raten. Wenn Sie Ihre Einnahmen, Konversionen oder andere Metriken optimieren müssen, sollten Sie Decisioning Studio Pro in Betracht ziehen.
- **Begrenzte Abmessungen**: Go unterstützt einen vordefinierten Satz von Dimensionen. Wenn Sie angepasste Dimensionen oder eine komplexe Personalisierung benötigen, sollten Sie Decisioning Studio Pro in Betracht ziehen.
- **Begrenzte CEP-Unterstützung**: Go lässt sich nur mit Braze und Salesforce Marketing Cloud integrieren. Für andere Plattformen empfehlen wir Decisioning Studio Pro.

## Bewährte Praktiken

- **Fangen Sie einfach an**: Beginnen Sie mit 2-3 Templates oder Varianten für die Betreffzeile. Dies gibt dem Agenten genügend Möglichkeiten zu lernen, während das Experiment überschaubar bleibt.
- **Geben Sie ihm Zeit**: Der Agent benötigt ausreichend Daten, um zu lernen. Lassen Sie sich mindestens 2-4 Wochen Zeit, bevor Sie Rückschlüsse auf die Performance ziehen.
- **Halten Sie den Inhalt abwechslungsreich**: Stellen Sie sicher, dass sich Ihre Optionen sinnvoll unterscheiden. Das Testen geringfügiger Variationen führt möglicherweise nicht zu signifikanten Insights.
- **Überwachen Sie regelmäßig**: Überprüfen Sie das Decisioning Studio Go Portal, um den Fortschritt des Experiments und die Metriken für das Engagement zu überwachen.

## Nächste Schritte

Sobald Sie Ihren Agenten entworfen und im Decisioning Studio Go Portal konfiguriert haben, können Sie ihn starten:

- [Starten Sie Ihren Agenten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
