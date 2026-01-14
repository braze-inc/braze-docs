---
nav_title: Tangerine
article_title: Tangerine
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Tangerine Store360, einer Omnichannel-Plattform, die physische Geschäfte mit Online-Shops verbindet, um Verbrauchern:in und Mitarbeitern in den Geschäften ein besseres Erlebnis zu bieten. Durch diese Integration sind die Rohdaten der Kampagnen und Impressionen von Braze über Snowflake Secure Data Sharing auf Store360 verfügbar, und Marken können messen, wie sich ihre Kampagnen auf das Engagement im Laden und die Besucherzahlen im Shop auswirken."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine entwickelt, baut und betreibt eine Omnichannel-Plattform namens Store360. Store360 ist eine Omnichannel Enablement-Plattform, die physische Läden mit Online-Shops verbindet, um das Erlebnis für Verbraucher:in und Mitarbeiter in den Läden zu verbessern. Store360 verfolgt und analysiert den Besuchsverkehr in physischen Läden, einschließlich der Nutzer:innen mobiler Apps von Einzelhändlern und deren Engagement in den Läden.

Die Integration von Braze und Tangerine erlaubt es Ihnen, rohe Kampagnen- und Impressionsdaten von Braze über Snowflake Secure Data Sharing in Store360 zu integrieren. Marken können jetzt die Auswirkungen dieser Kampagnen auf die Besuche in den Geschäften und das Engagement in den Geschäften messen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Store360-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Store360-Konto. |
| Braze-Konto ID | Ihre Braze App-Gruppe ID. |
| Übereinstimmende Nutzer:innen IDs | Ihre Kundendaten in Store360 und Braze müssen übereinstimmende Nutzer:innen-IDs auf beiden Plattformen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Analysieren Sie die Auswirkungen von Kampagnen auf den Besuch von Geschäften

Marken nutzen Braze, um Kampagnen-Nachrichten an Verbraucher:in zu senden, um die Zahl der Besuche im Shop zu erhöhen. Während der Kampagne erfasst Store360 die Besuche von Nutzern:innen einer mobilen App, die durch ihre ID identifiziert werden.

Mit den Analysefunktionen von Store360 Insight können Marken die Wirkung von Kampagnen im Detail visualisieren - von gesendeten und gelesenen Nachrichten (Daten von Braze) bis hin zu der Frage, wer und wie viele Empfänger:innen physische Shops besucht haben (Daten von Store360).

## Integration

### Schritt 1: Enablement von Snowflake Secure Data Share

Arbeiten Sie mit Ihrem Braze Team zusammen, um Snowflake Secure Data Share zu aktivieren und zu konfigurieren.

### Schritt 2: Konfigurieren Sie Store360 für den Abruf von Braze Daten

Konfigurieren Sie die ID Ihrer App-Gruppe von Braze für Ihr Store360-Dienst-Konto über die Webkonsole des Store360 Admin Manager:in. Dies ist eine Anfrage an das Tangerine Admin Team, Braze Daten mit Store360 über Snowflake Data Sharing zu synchronisieren.

### Schritt 3: Store360 SDKs in die mobile App integrieren

Um die Besuche von Nutzern:innen im Shop und die Aktivitäten im Laden zusammen mit den Braze Kampagnen- und Impressionsdaten zu verfolgen und zu analysieren, müssen Sie das Store360 SDK in Ihre mobile App integrieren. Gehen Sie dazu wie in der Dokumentation zur Store360 SDK-Installation beschrieben vor. Diese Dokumentation wird Ihnen nach Unterzeichnung eines Client-Vertrags zwischen Tangerine Store 360 zur Verfügung gestellt.

## Analysieren Sie die Daten von Braze in Store360

Nutzen Sie die Vorteile des sicheren Datenaustauschs von Snowflake, um Ihre Braze-Rohdaten zu Kampagnen und Impressionen mit Store360 Insight Analytics auszutauschen. So erhalten Sie ein vollständiges Bild des Lebenszyklus und der Aktivitäten der Nutzer:innen - von online bis offline.

Zum Referenzieren finden Sie hier alle [Felder von Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df), die in Store360 Analytics integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Store360 Account Manager oder support@tangerine.io, um mehr zu erfahren.

## Wichtige Informationen und Einschränkungen

### Verfügbarkeit von Diensten

Derzeit ist der Dienst Store360 in Japan und Indonesien kommerziell verfügbar.

Tangerine plant die Einführung eines Store360 Produkts in den folgenden Ländern im Jahr 2023.
- Vereinigte Staaten von Amerika
- Thailand
- Singapur
- Vietnam
- Korea

### Datenaufbewahrung

Für den Datenaustausch mit Snowflake gilt eine Richtlinie zur Bindung Ihrer Braze Daten für zwei Jahre.

### Zeitverzögerung beim Auffüllen von Braze Ereignisdaten

Braze-Ereignisse werden mit Streaming-Technologie verarbeitet und sind nahezu in Realtime verfügbar. In der Regel werden die Ereignisse innerhalb von 30 Minuten nach ihrem Eintreten veröffentlicht.
