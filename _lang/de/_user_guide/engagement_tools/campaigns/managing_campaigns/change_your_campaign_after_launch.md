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

Um eine Kampagne zu beenden, öffnen Sie Ihre **Kampagnendetailseite** und wählen Sie **Kampagne beenden**. Wenn eine Kampagne gestoppt wird:

- Nachrichten, die für den Versand geplant sind, werden abgebrochen.
- A/B-Tests, bei denen der erste Test bereits versendet wurde, werden dauerhaft abgebrochen.
- Ereignisse für bereits gesendete Nachrichten (z.B. geöffnete Klicks) werden weiterhin getrackt.

Um Ihre Kampagne neu zu starten, wählen Sie **Fortsetzen**. Ihre Kampagne versendet weiterhin Nachrichten und A/B-Tests, aber verpasste Nachrichten werden nicht erneut versendet oder neu geplant.

## Ausgelöste Kampagnen

Alle Änderungen an aktionsbasierten Zustellungskampagnen und API-getriggerten Zustellungskampagnen werden bei Weiterleitungen sofort wirksam. 

Wenn diese Kampagnen ausgelöst, aber noch nicht versendet wurden (z.B. eine aktionsbasierte Zustellung mit einer 1-tägigen Verzögerung wird während des 1-tägigen Verzögerungszeitraums bearbeitet), beachten Sie die folgende Anleitung für geplante Kampagnen.

### Geplante Kampagnen

Wenn Sie nach dem Start Änderungen an einer Kampagne vornehmen müssen, sollten Sie bei der Bearbeitung Ihrer Kampagne die folgenden Punkte beachten, um sicherzustellen, dass Ihre Änderungen die gewünschten Auswirkungen haben.

### Nachrichteninhalt

Alle Änderungen am Inhalt der Nachrichten (einschließlich Titel, Textkörper und Bilder) werden sofort nach dem Speichern für alle zukünftigen Nachrichten wirksam. Es ist nicht möglich, den Inhalt von Nachrichten zu ändern, die bereits versendet wurden.

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

## Entwürfe für aktive Kampagnen speichern {#campaign-drafts}

Entwürfe eignen sich hervorragend, um umfangreiche Änderungen an aktiven Kampagnen vorzunehmen. Wenn Sie einen Entwurf erstellen, können Sie geplante Änderungen vor der nächsten Veröffentlichung testen.

{% alert note %}
Eine Kampagne kann immer nur einen Entwurf haben. Außerdem sind keine Analytics verfügbar, da die entworfenen Änderungen noch nicht eingeführt wurden.
{% endalert %}

Um einen Entwurf zu erstellen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrer aktiven Kampagne.
2. Nehmen Sie Ihre Änderungen vor.
3. Wählen Sie **Als Entwurf speichern**. Beachten Sie, dass Sie nach dem Erstellen eines Entwurfs die aktive Kampagne erst bearbeiten können, wenn Sie die Kampagne entweder starten oder den Entwurf verwerfen.

![Ein Entwurf einer aktiven Kampagne mit einer Option zum Anzeigen der aktiven Kampagne.]({% image_buster /assets/img/campaign_draft.png %})

Wenn Sie den Entwurf bearbeiten, können Sie die aktive Kampagne auch in der Kopfzeile des Kampagnenentwurfs oder in der Fußzeile der Kampagnen Analytics referenzieren. 

Um zu einer aktiven Kampagne zurückzukehren, wählen Sie in der Analytics-Ansicht oder in der Ansicht der aktiven Kampagne **Entwurf bearbeiten** aus.

### Priorisierung von In-App-Nachrichten

Die Priorität der In-App-Nachricht wird sofort aktualisiert (bevor der Entwurf gestartet wird), wenn Sie **Genaue Priorität festlegen** auswählen und die Priorität im Verhältnis zu anderen Kampagnen oder Canvase angeben.
