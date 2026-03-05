---
nav_title: Vorbereiten Ihrer Datenquellen
article_title: Vorbereiten Ihrer Datenquellen
page_order: 4
page_type: reference
description: "Dieser referenzierte Artikel behandelt die entscheidenden Daten, die Sie benötigen, um die KI-Entscheidungsschleife zu schließen und Ihren Agenten in die Lage zu versetzen, kontinuierlich zu lernen und sich zu verbessern."
---

# Vorbereiten Ihrer Datenquellen

> Dieser referenzierte Artikel behandelt die entscheidenden Daten, die Sie benötigen, um die KI-Entscheidungsschleife zu schließen und Ihren Agenten in die Lage zu versetzen, kontinuierlich zu lernen und sich zu verbessern.

## Schließen des KI-Entscheidungskreislaufs

Zwar sind alle Kundendaten für den Agenten wichtig (siehe [Datenquellen verbinden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), aber die wichtigsten Daten sind diejenigen, die dem Agenten mitteilen, was nach dem Versenden der Customer-Engagement-Entscheidungen passiert ist.

Diese Vermögenswerte bilden die Feedback-Schleife, die es dem Agenten erlaubt, zu lernen.

{% alert note %}
Wenn der Agent nativ mit der Customer-Engagement-Plattform (wie Braze, SFMC oder Klaviyo) integriert ist, sind möglicherweise keine zusätzlichen Konfigurationsschritte für Feedback-Daten erforderlich, da diese automatisch mit den Kundendaten gesendet werden.
{% endalert %}

## Kritische Daten für Feedback

Es gibt drei entscheidende Faktoren für die Erstellung der Feedbackschleife:

1. Daten zu Konversionen
2. Daten zum Engagement
3. Daten zu Aktivierungen

### Daten zu Konversionen

Das Konversions-Asset beschreibt, was mit dem Kunden nach der Orchestrierung geschehen ist. Angenommen, ein Agent optimiert den Nettogegenwartswert (NPV) für Kund:innen, die optimierte Kampagnen erhalten, dann könnte das Konversions-Asset ein tägliches Update der Änderungen des NPV enthalten.

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für Kund:in, der mit allen Daten konsistent ist. | Decisioning Studio muss die individuelle Customer Journey von der Empfehlung über die Aktivierung bis hin zur Konversion verfolgen. |
| Jeder Datensatz hat einen zugehörigen Zeitstempel | Das Verständnis der Zeit zwischen der Kommunikation und der Abfolge der Kund:in ist extrem wichtig für das Training der Agenten und die Berechnung von Metriken. |
| Wenn Sie eine nicht-binäre Targeting-Metrik verwenden (z.B. konvertiert versus nicht konvertiert), wird der Wert der Targeting-Metrik bei jedem Konversions-Event angegeben. | Decisioning Studio verwendet den Wert der Targeting Metriken, um Trainingserfahrungen zu generieren und den Agenten auf der Grundlage der Ergebnisse der empfohlenen Aktionen angemessen zu belohnen/bestrafen. |
| Wenn Konversionen eindeutig der Kommunikation zugeordnet werden können (e.g., Einlösung eines Coupons), werden Felder bereitgestellt, die für die Zuordnung von Konversionen zu Aktivierungen erforderlich sind. | Wenn ein Konversions-Event mit einer bestimmten Kommunikation verknüpft werden kann, ist eine saubere und präzise Attribution zulässig. Die direkte Attribution gibt dem Agenten das deutlichste Signal, aber wenn dies nicht möglich ist (was häufig der Fall ist), wird die Attribution auf Basis der Nähe verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Daten zum Engagement

Das Engagement-Asset beschreibt Kundeninteraktionen, einschließlich Klicks, Öffnungen und andere Impressionen. Die Daten zum Engagement können in den Daten zur Konversion enthalten oder separat sein. Sie spielen eine ähnliche Rolle wie Konversionsdaten - sie sagen dem Agenten, was nach dem Customer-Engagement passiert ist.

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für Kund:in, der mit allen Daten konsistent ist. | Decisioning Studio muss Engagement-Events für jede einzelne Kund:in verfolgen. |
| Jeder Datensatz hat einen zugehörigen Zeitstempel | Das Verständnis der Zeit zwischen der Kommunikation und der Abfolge der Kund:in ist extrem wichtig für das Training der Agenten und die Berechnung von Metriken. |
| Wenn Klicks, Öffnungen oder andere Daten zum Engagement eindeutig der Kommunikation zugeordnet werden können, werden Felder bereitgestellt, die benötigt werden, um das Engagement den Aktivierungen zuzuordnen. | Wie bei den Daten zur Konversion ist eine saubere und präzise Attribution zulässig, wenn das Engagement mit einer bestimmten Kommunikation verknüpft werden kann. Die direkte Attribution ist das deutlichste Signal für den Agenten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Daten zu Aktivierungen

Das Asset Aktivierungen teilt dem Agenten mit, welche Mitteilungen gesendet wurden. Je nachdem, wie die Orchestrierung konfiguriert ist, ist dies oft notwendig. Wenn der Agent die Orchestrierung über eine direkte Integration mit Braze, SFMC oder Klaviyo durchführt, kann der Agent möglicherweise direkt Aktivierungsdaten abrufen.

{% alert note %}
Engagement-Daten und Aktivierungsdaten sind sehr häufig im selben Datenbestand zu finden.
{% endalert %}

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für Kund:in, der mit allen Daten konsistent ist. | Decisioning Studio muss die individuelle Customer Journey von der Empfehlung über die Aktivierung bis hin zur Konversion verfolgen. |
| Jeder Datensatz hat einen zugehörigen Zeitstempel | Das Verständnis der Zeit zwischen der Kommunikation und der Abfolge der Kund:in ist extrem wichtig für das Training der Agenten und die Berechnung von Metriken. |
| Felder, die benötigt werden, um Kommunikationsinhalte mit Aktivierungsereignissen abzugleichen, werden bereitgestellt (z.B. `event_id`) | Die korrekte Zuordnung von Kommunikationsmerkmalen zu Sendungen ist für die Attribution und das Training von Agenten notwendig. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
