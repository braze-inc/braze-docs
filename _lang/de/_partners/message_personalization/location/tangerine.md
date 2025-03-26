---
nav_title: Mandarine
article_title: Mandarine
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Tangerine Store360, einer Omnichannel-Plattform, die physische Geschäfte mit Online-Shops verbindet, um Verbrauchern und Mitarbeitern in den Geschäften ein besseres Einkaufserlebnis zu bieten. Durch diese Integration sind Braze-Rohdaten zu Kampagnen und Impressionen über Snowflake Secure Data Sharing auf Store360 verfügbar, und Marken können messen, wie sich ihre Kampagnen auf das Engagement in den Geschäften und die Besucherzahlen auswirken."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine entwickelt, baut und betreibt eine Omnichannel-Plattform namens Store360. Store360 ist eine Omnichannel-Plattform, die physische Geschäfte mit Online-Shops verbindet, um das Einkaufserlebnis für Kunden und Mitarbeiter in den Geschäften zu verbessern. Store360 verfolgt und analysiert den Besuchsverkehr in physischen Geschäften, einschließlich der Nutzer der mobilen App von Einzelhändlern und deren Engagement in den Geschäften.

Die Integration von Braze und Tangerine ermöglicht Ihnen die Integration von Rohdaten zu Kampagnen und Impressionen von Braze in Store360 über Snowflake Secure Data Sharing. Marken können jetzt die Auswirkungen dieser Kampagnen auf die Besuche in den Geschäften und das Engagement in den Geschäften messen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Store360-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Store360-Konto. |
| Braze Konto-ID | Ihre Braze App Gruppen-ID. |
| Übereinstimmende Benutzer-IDs | Ihre Kundendaten in Store360 und Braze müssen übereinstimmende Benutzer-IDs auf den beiden Plattformen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Analysieren Sie die Auswirkungen der Kampagne auf den Besuch von Geschäften

Marken nutzen Braze, um Kampagnenbotschaften an Verbraucher zu senden und so die Zahl der Besuche in den Geschäften zu erhöhen. Während der Kampagne erfasst Store360 die Besuche von Benutzern der mobilen App, die anhand ihrer Benutzer-ID identifiziert werden.

Mit der Analysefunktion von Store360 Insight können Marken die Auswirkungen ihrer Kampagnen detailliert darstellen - von gesendeten und gelesenen Nachrichten (Daten von Braze) bis hin zu der Frage, wer und wie viele Empfänger physische Geschäfte besucht haben (Daten von Store360).

## Integration

### Schritt 1: Aktivieren Sie Snowflake Secure Data Share

Arbeiten Sie mit Ihrem Braze-Team zusammen, um Snowflake Secure Data Share zu aktivieren und zu konfigurieren.

### Schritt 2: Konfigurieren Sie Store360 für den Abruf von Braze-Daten

Konfigurieren Sie Ihre Braze-App-Gruppen-ID mit Ihrem Store360-Servicekonto über die Webkonsole des Store360-Admin-Managers. Dadurch wird das Tangerine-Administrationsteam aufgefordert, Braze-Daten mit Store360 über Snowflake Data Sharing zu synchronisieren.

### Schritt 3: Store360 SDKs in die mobile App integrieren

Um die Besuche der Benutzer der mobilen App in den Geschäften und die Aktivitäten in den Geschäften zusammen mit den Braze-Kampagnen- und Impressionsdaten zu verfolgen und zu analysieren, müssen Sie das Store360 SDK in Ihre mobile App integrieren, indem Sie die in der Store360 SDK-Installationsdokumentation beschriebenen Schritte durchführen. Diese Dokumentation wird Ihnen nach Unterzeichnung eines Kundenvertrags zwischen Tangerine Store 360 zur Verfügung gestellt.

## Analysieren Sie Braze-Daten in Store360

Nutzen Sie die Vorteile des sicheren Datenaustauschs mit Snowflake, um Ihre Braze-Rohdaten zu Kampagnen und Impressionen mit Store360 Insight-Analysen auszutauschen. So erhalten Sie ein vollständiges Bild des Lebenszyklus und der Aktivitäten der Nutzer von online bis offline.

Als Referenz finden Sie hier alle [Braze-Felder](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df), die in Store360-Analysen integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Store360-Kundenbetreuer oder support@tangerine.io, um mehr zu erfahren.

## Wichtige Informationen und Einschränkungen

### Service-Verfügbarkeit

Derzeit ist der Store360-Service in Japan und Indonesien erhältlich.

Tangerine plant eine Store360 Produkteinführung in den folgenden Ländern im Jahr 2023.
- Vereinigte Staaten von Amerika
- Thailand
- Singapur
- Vietnam
- Korea

### Aufbewahrung von Daten

Es gibt eine zweijährige Aufbewahrungsfrist für Ihre Braze-Daten für den Datenaustausch mit Snowflake.

### Zeitverzögerung beim Auffüllen der Braze-Ereignisdaten

Braze-Ereignisse werden mit Streaming-Technologie verarbeitet und sind nahezu in Echtzeit verfügbar. In der Regel werden die Ereignisse innerhalb von 30 Minuten nach ihrem Eintreten veröffentlicht.
