---
nav_title: Starten Sie Ihren Agenten
article_title: Starten Sie Ihren Agenten
page_order: 4
description: "Erfahren Sie, wie Sie Ihren BrazeAI Decisioning Studio Go-Agenten starten und Business as Usual (BAU)-Berichte zum Performance-Vergleich einrichten."
---

# Starten Sie Ihren Agenten

> Sobald Sie Ihre Datenquellen verbunden, die Orchestrierung eingerichtet und Ihren Agenten entworfen haben, können Sie loslegen. Dieser Artikel behandelt die Aktivierung Ihres Agenten und die Einrichtung der optionalen BAU-Berichterstattung.

## Starten Sie Ihren Agenten

Nachdem Sie alle Konfigurationsschritte im Portal Decisioning Studio Go abgeschlossen haben:

1. Überprüfen Sie Ihre Agentenkonfiguration, um sicherzustellen, dass alle Einstellungen korrekt sind.
2. Überprüfen Sie, ob Ihre CEP Integration aktiv ist und die Orchestrierung bereit ist.
3. Wählen Sie **Starten** (oder eine entsprechende Aktion) im Portal Decisioning Studio Go, um Ihren Agenten zu aktivieren.

Sobald Sie gestartet sind, wird Ihr Agent:
- Beginnen Sie mit dem Empfang von Zielgruppen-Daten von Ihrem CEP
- Beginnen Sie damit, für jede Kund:in personalisierte Empfehlungen auszusprechen.
- Orchestrierung von Sendungen über Ihre konfigurierte CEP
- Sammeln Sie Daten zum Engagement, um zu lernen und sich im Laufe der Zeit zu verbessern

## Einrichten von BAU-Berichten

Standardmäßig wird in der Berichterstattung des Decisioning Studio Go-Portals die Decisioning Studio Go-Gruppe mit der Zufalls-Kontrollgruppe verglichen. Wenn Sie eine bestehende Business as Usual (BAU)-Kampagne haben, mit der Sie vergleichen möchten, können Sie BAU-Berichte einrichten, um alle drei Gruppen an einem Ort zu sehen.

### Vorteile der BAU-Berichterstattung

Der Hauptvorteil bei der Erstellung von BAU-Berichten ist die Anwendung des Filters für ungültige Klicks von Decisioning Studio Go. Bei Anwendung auf alle drei Versuchsgruppen ist ein möglichst genauer und fairer ("Äpfel zu Äpfeln") Vergleich der Klick Performance zulässig, da das Rauschen entfernt wird:
- Verdächtige Klicks der Maschine
- Klicks auf den Link zum Abmelden

### Anforderungen für BAU-Berichte

Bevor Sie die BAU-Berichterstattung einrichten, stellen Sie sicher, dass ein Vergleich zwischen der BAU-Behandlungsgruppe, der Decisioning Studio Go-Gruppe und der Zufalls-Kontrollgruppe möglich ist:

- **Keine Überschneidung**: Kein Empfänger:in kann während der gesamten Dauer des Experiments zu mehr als einer Gruppe gehören
- **Zufällige Zuweisung**: Die Empfänger:innen werden nach dem Zufallsprinzip den Gruppen zugewiesen, ohne dass es zu Verzerrungen kommt.
- **Gleiche Optionen**: Alle Optionen, die der BAU-Gruppe zur Verfügung stehen (Kreativität, Häufigkeit, Zeit, Anreiz oder Angebot), stehen auch den Gruppen Decisioning Studio Go und Random Control zur Verfügung.

{% alert warning %}
Ohne ein "Äpfel mit Äpfeln"-Experiment kann die BAU-Berichterstattung verwirrend oder irreführend sein.
{% endalert %}

### Erforderliche Informationen

Nachdem Sie Ihren Versuchsplan validiert haben, sammeln Sie die folgenden Details, um die BAU-Berichterstattung einzurichten:

**Kampagnen IDs aus Ihrer CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Kampagnen und Canvase |
| **Salesforce Marketing Cloud** | Nur Fahrten |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**Zielgruppe ID aus Ihrer CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Nur Segmente |
| **Salesforce Marketing Cloud** | Nur Daten Erweiterungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Wenn Sie keine bestehende Zielgruppe haben, die Ihr BAU-Publikum trackt, müssen Sie eine erstellen.

### Überlegungen

- **Klicken Sie nur auf KPIs**: Ähnlich wie bei Decisioning Studio Go deckt das BAU-Reporting nur Klick-KPIs ab, nicht aber Konversions-KPIs.
- **Canvas Einschränkungen**: Das Filtern nach bestimmten Canvas-Schritt IDs wird derzeit nicht unterstützt. Ereignisse aus allen Canvas-Schritten werden in die BAU-Daten aufgenommen. Dies kann Vergleiche mit BAU ungültig machen, wenn nur bestimmte Canvas-Schritte berücksichtigt werden sollen.

### Einrichten von BAU-Berichten

Folgen Sie den Anweisungen in Ihrem Decisioning Studio Go Portal. Das müssen Sie haben:
- Eine oder mehrere Kampagnen IDs, bei denen alle Mitteilungen BAU Mitteilungen sind
- Eine Zielgruppen ID, die Empfänger:in der Zielgruppe BAU jeden Tag trackt

## Überwachung Ihres Agenten

Nach dem Start überwachen Sie die Performance Ihres Agenten im Portal Decisioning Studio Go:

- **Metriken für das Engagement**: Tracking von Klickraten in verschiedenen Experimentiergruppen
- **Lernangebote**: Beobachten Sie, wie sich die Empfehlungen des Agenten im Laufe der Zeit entwickeln
- **Gruppenvergleiche**: Vergleichen Sie die Performance von Decisioning Studio Go mit der von Random Control und BAU (falls konfiguriert).

{% alert tip %}
Lassen Sie mindestens 2-4 Wochen der Datenerfassung zu, bevor Sie Rückschlüsse auf die Performance ziehen. Der Agent braucht genügend Interaktionen, um effektiv zu lernen und zu optimieren.
{% endalert %}

## Fehlersuche

Wenn Ihr Agent nicht die erwartete Performance zeigt:

1. **Überprüfen Sie die Orchestrierung**: Vergewissern Sie sich, dass Ihre CEP Integration aktiv ist, Kampagnen und Journeys laufen und dass keine globalen Caps oder ähnliche Regeln die Orchestrierung behindern.
2. **Prüfen Sie den Datenfluss**: Bestätigen Sie, dass die Daten der Zielgruppe und des Engagements korrekt erfasst werden.
3. **Überprüfen Sie die Experimentiergruppen**: Stellen Sie sicher, dass die Zuweisung nach dem Zufallsprinzip erfolgt und es keine Überschneidungen zwischen den Gruppen gibt.
4. **Kontaktieren Sie den Support**: Wenden Sie sich an den Braze-Support für weitere Unterstützung.
