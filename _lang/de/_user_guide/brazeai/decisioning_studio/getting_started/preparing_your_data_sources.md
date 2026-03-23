---
nav_title: Vorbereitung Ihrer Datenquellen
article_title: Vorbereitung Ihrer Datenquellen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die kritischen Feedback-Datenbestände, die erforderlich sind, um den KI-Entscheidungszyklus zu schließen und Ihrem Agenten kontinuierliches Lernen und Verbessern zu ermöglichen."
---

# Vorbereitung Ihrer Datenquellen

> Dieser Referenzartikel behandelt die kritischen Feedback-Datenbestände, die erforderlich sind, um den KI-Entscheidungszyklus zu schließen und Ihrem Agenten kontinuierliches Lernen und Verbessern zu ermöglichen.

## Den KI-Entscheidungsprozess abschließen

Obwohl alle Kundendaten für den Mitarbeiter von Bedeutung sind (siehe [Datenquellen verbinden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), sind die wichtigsten Daten diejenigen, die dem Mitarbeiter Aufschluss darüber geben, was nach dem Versand der Customer-Engagement-Entscheidungen geschehen ist.

Diese Ressourcen bilden die Rückkopplungsschleife, die es dem Agenten ermöglicht, zu lernen.

{% alert note %}
Wenn der Agent nativ in die Customer-Engagement-Plattform (wie Braze, SFMC oder Klaviyo) integriert ist, sind möglicherweise keine zusätzlichen Konfigurationsschritte für Feedback-Daten erforderlich, da diese automatisch mit den Kundendaten gesendet werden können.
{% endalert %}

## Kritische Feedback-Datenbestände

Es gibt drei entscheidende Faktoren für die Schaffung einer Feedbackschleife:

1. Konversionsdaten
2. Engagement-Daten
3. Aktivierungsdaten

### Konversionsdaten

Der Wert der Konversion beschreibt, was mit der Kund:in nach der Orchestrierung geschehen ist. Angenommen, ein Agent optimiert den Nettobarwert (NPV) für Kund:innen, die optimierte Kampagnen erhalten, könnte das Conversion-Asset ein tägliches Update der Änderungen am NPV umfassen.

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für den Kunden, der mit allen Datenbeständen übereinstimmt. | Das Decisioning Studio muss die individuelle Customer Journey von der Empfehlung über die Aktivierung bis hin zur Konversion verfolgen. |
| Jeder Datensatz verfügt über einen zugehörigen Zeitstempel. | Das Verständnis der Zeitspanne zwischen der Kommunikation und der Abfolge der Aktionen der Kund:innen ist für die Trainierung der Mitarbeiter und die Berechnung der Metriken von entscheidender Bedeutung. |
| Bei Verwendung einer nicht binären Zielmetrik (z. B. konvertiert gegenüber nicht konvertiert) wird der Wert der Zielmetrik bei jedem Konversions-Event angegeben. | Decisioning Studio verwendet den Zielmetrikwert, um Trainingserfahrungen zu generieren, mit denen der Agent auf der Grundlage der Ergebnisse der empfohlenen Maßnahmen angemessen belohnt oder bestraft wird. |
| Wenn Konversionen eindeutig der Kommunikation zugeordnet werden können (e.gz. B. Einlösung von Gutscheinen), werden Felder bereitgestellt, die erforderlich sind, um Konversionen mit Aktivierungen abzugleichen. | Wenn ein Konversions-Event mit einer bestimmten Kommunikation verknüpft werden kann, ermöglicht dies eine klare und präzise Attribution. Die direkte Attribution liefert dem Agenten das eindeutigste Signal. Sollte dies jedoch nicht möglich sein (was häufig der Fall ist), wird die nachräumliche Attribution verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Engagement-Daten

Die Interaktionsdaten beschreiben Kundeninteraktionen, einschließlich Klicks, Öffnungen und anderer Impressionen. Engagement-Daten können in den Daten zur Konversion enthalten sein oder separat aufgeführt werden. Es erfüllt eine ähnliche Funktion wie Daten zur Konversion – es informiert den Mitarbeiter darüber, was nach dem Customer-Engagement geschehen ist.

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für den Kunden, der mit allen Datenbeständen übereinstimmt. | Das Decisioning Studio muss die Interaktionsereignisse für jeden einzelnen Kunden verfolgen. |
| Jeder Datensatz verfügt über einen zugehörigen Zeitstempel. | Das Verständnis der Zeitspanne zwischen der Kommunikation und der Abfolge der Aktionen der Kund:innen ist für die Trainierung der Mitarbeiter und die Berechnung der Metriken von entscheidender Bedeutung. |
| Wenn Klicks, Öffnungen oder andere Engagement-Daten eindeutig einer Kommunikation zugeordnet werden können, werden Felder bereitgestellt, die erforderlich sind, um das Engagement mit Aktivierungen abzugleichen. | Ähnlich wie bei den Daten zur Konversion ermöglicht es eine klare und präzise Attribution, wenn das Engagement mit einer bestimmten Kommunikation in Verbindung gebracht werden kann. Die direkte Attribution liefert dem Agenten das eindeutigste Signal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Aktivierungsdaten

Die Aktivierungsressource informiert den Agenten darüber, welche Mitteilungen versendet wurden. Dies ist häufig erforderlich, abhängig davon, wie die Orchestrierung konfiguriert ist. Wenn der Agent über eine direkte Integration mit Braze, SFMC oder Klaviyo für die Orchestrierung verwendet, kann er möglicherweise Aktivierungsdaten direkt abrufen.

{% alert note %}
Engagement-Daten und Aktivierungsdaten sind häufig in derselben Datenquelle zu finden.
{% endalert %}

| Anforderung | Grund |
|-------------|------|
| Jeder Datensatz enthält einen eindeutigen Bezeichner für den Kunden, der mit allen Datenbeständen übereinstimmt. | Das Decisioning Studio muss die individuelle Customer Journey von der Empfehlung über die Aktivierung bis hin zur Konversion verfolgen. |
| Jeder Datensatz verfügt über einen zugehörigen Zeitstempel. | Das Verständnis der Zeitspanne zwischen der Kommunikation und der Abfolge der Aktionen der Kund:innen ist für die Trainierung der Mitarbeiter und die Berechnung der Metriken von entscheidender Bedeutung. |
| Es werden Felder bereitgestellt, die erforderlich sind, um Kommunikationsinhalte mit Aktivierungsereignissen abzugleichen (z. B. `event_id`). | Die korrekte Zuordnung von Kommunikationsmerkmalen zu Sendungen ist für die Attribution von Agenten und zum Trainieren unerlässlich. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

