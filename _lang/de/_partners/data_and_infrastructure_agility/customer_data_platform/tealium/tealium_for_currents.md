---
nav_title: Tealium für Currents
article_title: Tealium für Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Tealium, einer Plattform für Kundendaten, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium für Currents

> [Tealium](https://www.tealium.com) ist eine Plattform für Kundendaten, die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl von anderen Stellen in Ihrem Marketing-Stack weiterleitet.

Die Integration von Braze und Tealium ermöglicht Ihnen die nahtlose Steuerung des Informationsflusses zwischen den beiden Systemen. Mit Currents können Sie auch Daten mit Tealium verbinden, um sie über den gesamten Wachstumsbereich hinweg nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium EventStream oder Tealium AudienceStream | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/). |
| Currents | Um Daten zurück in Tealium zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Tealium URL | Diese können Sie erhalten, indem Sie zu Ihrem Tealium-Dashboard navigieren und die Ingestion-URL kopieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Braze in Tealium

Eine Anleitung zum Erstellen einer Datenquelle finden Sie auf der [Tealium-Website](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Wenn Sie fertig sind, stellt Ihnen Tealium eine URL für die Datenquelle zur Verfügung, die Sie im nächsten Schritt verwenden.

### Schritt 2: Aktuell erstellen

Navigieren Sie in Braze zu **Ströme > + Strom erstellen > Tealium Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail und Ihre Tealium-URL an. Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie verfolgen möchten. Klicken Sie abschließend auf **Aktuelles starten**

Alle Ereignisse, die an Tealium gesendet werden, enthalten die `external_user_id` des Benutzers. Zur Zeit sendet Braze keine Ereignisdaten an Tealium für Benutzer, die ihre `external_user_id` nicht eingestellt haben.

{% alert important %}
Es ist wichtig, dass Sie Ihre Tealium-URL auf dem neuesten Stand halten. Wenn die URL Ihres Connectors nicht korrekt ist, kann Braze keine Ereignisse senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Details zur Integration

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) aufgeführt sind (einschließlich aller Eigenschaften in den Ereignissen [zur Nachrichteneinbindung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) und zum [Kundenverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) ) in Tealium.

Die Payload-Struktur für exportierte Daten ist die gleiche wie die Payload-Struktur für benutzerdefinierte HTTP-Konnektoren, die Sie im [Repository für Beispiele für benutzerdefinierte HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.