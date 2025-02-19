---
nav_title: Bearbeiten Sie Ihre Kampagne nach dem Start
article_title: Bearbeiten Sie Ihre Kampagne nach dem Start
page_order: 1
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick über das Ergebnis der Bearbeitung bestimmter Aspekte einer Kampagne nach dem Start."

---

# Bearbeiten Sie Ihre Kampagne nach dem Start

> Dieser Artikel gibt einen Überblick über das Ergebnis der Bearbeitung bestimmter Aspekte einer Kampagne nach dem Start.

## Stoppen Sie Ihre Kampagne

Um eine Kampagne zu stoppen, öffnen Sie Ihre **Kampagnendetailseite** und wählen Sie die Schaltfläche **Kampagne stoppen** unten rechts auf der Seite. Wenn eine Kampagne gestoppt wird:
- Nachrichten, die für den Versand geplant sind, werden abgebrochen
- A/B-Tests, bei denen der ursprüngliche Test bereits versendet wurde, werden dauerhaft abgebrochen.
- Ereignisse für bereits gesendete Nachrichten (z. B. Klicks zum Öffnen) werden weiterhin verfolgt.
- Kampagnen können neu gestartet werden, indem Sie auf **Fortsetzen**

Sobald die Kampagne wieder aufgenommen wird, werden weiterhin Nachrichten und A/B-Tests versendet, aber verpasste Nachrichten werden nicht erneut versendet oder geplant.

## Ausgelöste Kampagnen

Alle Änderungen an aktionsbasierten Zustellungskampagnen und API-getriggerten Zustellungskampagnen werden sofort für Weiterleitungen wirksam.

Wenn diese Kampagnen ausgelöst, aber noch nicht versendet wurden (z. B. eine aktionsbasierte Zustellungskampagne mit einer 1-tägigen Verzögerung wird während des 1-tägigen Verzögerungszeitraums bearbeitet), beachten Sie die folgende Anleitung für geplante Kampagnen.

## Geplante Kampagnen

Wenn Sie nach dem Start Änderungen an einer Kampagne vornehmen müssen, sollten Sie bei der Bearbeitung Ihrer Kampagne die folgenden Punkte beachten, um sicherzustellen, dass Ihre Änderungen die gewünschten Auswirkungen haben.

### Nachrichteninhalt

Alle Änderungen am Inhalt der Nachrichten (einschließlich Titel, Textkörper, Bilder usw.) werden sofort nach dem Speichern für alle zukünftigen Nachrichten wirksam. Es ist nicht möglich, den Inhalt von Nachrichten zu ändern, die bereits versendet wurden.

### Zeitplan und Zielgruppe

Wenn Sie die geplante Sendezeit oder die Zielgruppe Ihrer Kampagne ändern, werden diese Änderungen sofort in der aktuellen Kampagne übernommen.

### Rate senden

Wenn Sie eine Sendegeschwindigkeitsbeschränkung verwenden, "plant" Braze Ihre Nachrichten in minutengroßen Zeitfenstern. Wenn Sie also die Sendegeschwindigkeit der Nachrichten ändern möchten, halten Sie sich an das folgende Verfahren, um sofortige Änderungen vorzunehmen.

## Sofortige Änderungen vornehmen

Wenn Sie möchten, dass Änderungen sofort wirksam werden, gehen Sie wie folgt vor:

1. Stoppen Sie die betroffene Kampagne.
2. Duplizieren Sie die Kampagne.
3. Nehmen Sie Änderungen an der doppelten Kampagne vor.

{% alert important %}
Dadurch wird die Teilnahmeberechtigung für Personen, die bereits die ursprüngliche Kampagne erhalten haben, zurückgesetzt. Sie müssen also möglicherweise die doppelte Kampagne für Personen filtern, die die ursprüngliche Kampagne nicht erhalten haben.
{% endalert %}
