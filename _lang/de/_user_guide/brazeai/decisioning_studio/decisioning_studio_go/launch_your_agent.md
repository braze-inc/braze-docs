---
nav_title: Starten Sie Ihren Agenten
article_title: Starten Sie Ihren Agenten
page_order: 4
description: "Erfahren Sie, wie Sie Ihren BrazeAI Decisioning Studio Go-Agenten starten und das Business-as-Usual-Reporting (BAU) für die Performance-Vergleiche einrichten."
---

# Starten Sie Ihren Agenten

> Nachdem Sie Ihre Datenquellen verbunden, die Orchestrierung eingerichtet und Ihren Agenten entworfen haben, können Sie mit dem Start fortfahren. Dieser Artikel behandelt die Aktivierung Ihres Agenten und die Einrichtung der optionalen BAU-Berichterstattung.

## Ihren Agenten starten

Nachdem Sie alle Konfigurationsschritte im Decisioning Studio Go-Portal abgeschlossen haben:

1. Bitte überprüfen Sie Ihre Agent-Konfiguration, um sicherzustellen, dass alle Einstellungen korrekt sind.
2. Bitte überprüfen Sie, ob Ihre CEP-Integration aktiv ist und die Orchestrierung bereitsteht.
3. Wählen Sie im Decisioning Studio Go-Portal **die Option „Starten“** (oder eine entsprechende Aktion), um Ihren Agenten zu aktivieren.

Nach dem Start wird Ihr Agent:
- Beginnen Sie mit dem Empfang von Daten zur Zielgruppe aus Ihrem CEP.
- Beginnen Sie damit, personalisierte Empfehlungen für jeden Kunden zu erstellen.
- Die Orchestrierung sendet über Ihr konfiguriertes CEP.
- Sammeln Sie Engagement-Daten, um daraus zu lernen und sich im Laufe der Zeit zu verbessern.

## Einrichtung der BAU-Berichterstattung

Standardmäßig vergleicht das Decisioning Studio Go-Portal die Decisioning Studio Go-Gruppe mit der Random Kontrollgruppe. Wenn Sie eine bestehende Business-as-usual-Kampagne (BAU) haben, mit der Sie einen Vergleich durchführen möchten, können Sie die BAU-Berichterstellung einrichten, um alle drei Gruppen an einem Ort anzuzeigen.

### Vorteile der BAU-Berichterstattung

Der Hauptvorteil der Einrichtung der BAU-Berichterstattung besteht in der Anwendung der Filterung ungültiger Klicks durch Decisioning Studio Go. Bei Anwendung auf alle drei Versuchsgruppen ermöglicht dies einen äußerst präzisen und fairen Vergleich der Klick-Performance („Äpfel mit Äpfeln“), indem Störfaktoren aus folgenden Bereichen eliminiert werden:
- Verdächtige Klicks an Maschinen
- Klicks auf den Link zum Abmelden

### Anforderungen an die BAU-Berichterstattung

Bevor Sie das BAU-Reporting einrichten, stellen Sie bitte sicher, dass ein Vergleich zwischen der BAU-Behandlungsgruppe, der Decisioning Studio Go-Gruppe und der Kontrollgruppe möglich ist:

- **Keine Überschneidung**: Kein Empfänger:in darf während der gesamten Dauer des Experiments mehr als einer Gruppe angehören.
- **Zufällige Zuweisung**: Die Empfänger:innen werden ohne Verzerrung zufällig Gruppen zugeordnet.
- **Gleiche Optionen**: Alle Optionen, die der BAU-Gruppe zur Verfügung stehen (kreativ, Häufigkeit, Zeit, Anreiz oder Angebot), stehen auch den Gruppen „Decisioning Studio Go“ und „Random Control“ zur Verfügung.

{% alert warning %}
Ohne ein Experimentdesign, das einen direkten Vergleich ermöglicht, kann die BAU-Berichterstattung verwirrend oder irreführend sein.
{% endalert %}

### Erforderliche Informationen

Nachdem Sie Ihr Versuchsdesign validiert haben, erfassen Sie bitte die folgenden Details, um die BAU-Berichterstattung einzurichten:

**Kampagnen-IDs aus Ihrem CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Kampagnen und Canvase |
| **Salesforce Marketing Cloud** | Nur Reisen |
| **Klaviyo** | Nur Flüsse |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**Zielgruppen-ID aus Ihrem CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Nur Segmente |
| **Salesforce Marketing Cloud** | Nur Datenerweiterungen |
| **Klaviyo** | Nur Segmente |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Sollten Sie noch keine Zielgruppe haben, die Ihre BAU-Zielgruppe trackt, müssen Sie eine solche erstellen.

### Überlegungen

- **Bitte nur auf KPIs klicken**: Ähnlich wie bei Decisioning Studio Go im Allgemeinen umfasst das BAU-Reporting nur Klick-KPIs, nicht jedoch KPIs der Konversion.
- **Einschränkungen der Canvas**: Derzeit unterstützen wir keine Filterung nach bestimmten Canvas-Schritten. Alle Ereignisse aus den Canvas-Schritten werden in die BAU-Daten aufgenommen. Dies kann Vergleiche mit BAU ungültig machen, wenn nur bestimmte Canvas-Schritte berücksichtigt werden sollen.

### Einrichtung der BAU-Berichterstattung

Bitte befolgen Sie die Anweisungen in Ihrem Decisioning Studio Go-Portal. Sie müssen Folgendes vorweisen können:
- Eine oder mehrere IDs für Kampagnen, bei denen es sich bei allen Mitteilungen um BAU-Mitteilungen handelt
- Eine Zielgruppen-ID, die die Empfänger:innen in der BAU-Zielgruppe täglich verfolgt.

## Überwachung Ihres Vertreters

Überwachen Sie nach dem Start die Performance Ihres Agenten im Decisioning Studio Go-Portal:

- **Engagement-Metriken**: Klickraten über Versuchsgruppen hinweg verfolgen
- **Lernfortschritt**: Beobachten Sie, wie sich die Empfehlungen des Beraters im Laufe der Zeit entwickeln.
- **Gruppenvergleiche**: Vergleichen Sie die Performance von Decisioning Studio Go mit Random Control und BAU (sofern konfiguriert).

{% alert tip %}
Bitte warten Sie mindestens 2 bis 4 Wochen, bis die Datenerfassung abgeschlossen ist, bevor Sie Schlussfolgerungen zur Performance ziehen. Der Agent benötigt ausreichend Interaktionen, um effektiv zu lernen und sich zu optimieren.
{% endalert %}

## Fehlersuche

Sollte Ihr Vertreter nicht die erwartete Performance erbringen:

1. **Orchestrierung überprüfen**: Bitte überprüfen Sie, ob Ihre CEP-Integration aktiv ist, Kampagnen und Journeys ausgeführt werden und keine globalen Obergrenzen oder ähnliche Regeln die Orchestrierung beeinträchtigen.
2. **Datenfluss überprüfen**: Bitte bestätigen Sie, dass die Daten zur Zielgruppe und zum Engagement korrekt erfasst werden.
3. **Überprüfen Sie die Versuchsgruppen**: Bitte stellen Sie eine ordnungsgemäße zufällige Zuordnung sicher und vermeiden Sie Überschneidungen zwischen den Gruppen.
4. **Bitte wenden Sie sich an den Support**: Bitte wenden Sie sich an den Braze-Support, um weitere Unterstützung zu erhalten.
