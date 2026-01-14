---
nav_title: Tealium für Currents
article_title: Tealium für Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Tealium, einer Kundendaten-Plattform, die Informationen zwischen Quellen in Ihrem Marketing Stack sammelt und weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium für Currents

> [Tealium](https://www.tealium.com) ist eine Customer Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Tealium erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit Currents können Sie auch Daten mit Tealium verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium EventStream oder Tealium AudienceStream | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/). |
| Currents | Um Daten zurück nach Tealium zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Tealium URL | Diese erhalten Sie, indem Sie zu Ihrem Tealium Dashboard navigieren und die Ingestion-URL kopieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Braze in Tealium

Eine Anleitung zur Erstellung einer Datenquelle finden Sie auf der [Tealium-Website](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Wenn Sie fertig sind, stellt Tealium eine URL der Datenquelle zum Kopieren bereit, die Sie im nächsten Schritt verwenden werden.

### Schritt 2: Currents erzeugen

Navigieren Sie in Braze zu **Currents > + Create Current > Tealium Export**. Geben Sie einen Namen für die Integration, eine E-Mail an Ihren Ansprechpartner und Ihre Tealium URL an. Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie tracken möchten. Klicken Sie abschließend auf **Launch Current**

Alle Ereignisse, die an Tealium gesendet werden, enthalten die `external_user_id` des Nutzers:innen. Zur Zeit sendet Braze keine Ereignisdaten an Tealium für Nutzer:innen, die ihre `external_user_id` nicht eingestellt haben.

{% alert important %}
Es ist wichtig, dass Sie Ihre Tealium URL auf dem neuesten Stand halten. Wenn die URL Ihres Konnektors falsch ist, kann Braze keine Ereignisse senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Details zur Integration

Braze unterstützt den Export aller Daten, die in den [Currents Event-Glossaren]({{site.baseurl}}/user_guide/data/braze_currents/) aufgeführt sind (einschließlich aller Eigenschaften in [Messaging-Engagement-]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) und [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ), nach Tealium.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.