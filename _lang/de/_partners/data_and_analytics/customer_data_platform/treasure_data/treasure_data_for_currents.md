---
nav_title: Treasure Data für Currents
article_title: Treasure Data für Currents
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze Currents und Treasure Data, einer Customer Data Platform (CDP) für Unternehmen, die es Ihnen erlaubt, Auftragsergebnisse direkt in Braze zu schreiben."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data für Currents

> [Treasure Data](https://www.treasuredata.com/) ist eine Customer Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Treasure Data erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit Currents können Sie Daten auch mit Treasure Data verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data Konto](https://console.treasuredata.com/users/sign_in). |
| Currents | Um Daten zurück in Treasure Data zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto einrichten lassen. |
| Treasure Data URL | Diese erhalten Sie, indem Sie zu Ihrem Treasure Data Dashboard navigieren und die Datenaufnahme-URL kopieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Treasure Data protokolliert jedes Ereignis in Stapeln. Weitere Informationen zur Abfrage von Treasure Data, um Ereigniszählungen zu erhalten, finden Sie unter [Braze Currents Import Integration](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration).
{% endalert %}

## Integration

Die empfohlene Methode zur Verbindung mit Treasure Data ist die Postback API. Für diese Methode ist kein Standard Konnektor erforderlich und die Daten können über einen Push-Ansatz empfangen werden. Alle in einem Datenstapel gesendeten Ereignisse befinden sich in einem Feld einer Zeile in einem JSON-Array, das geparst werden muss, um die gewünschten Daten zu erhalten.

{% alert important %}
Die Datenaufnahme in Treasure Data über den Event-Collector erfolgt derzeit nicht in Realtime und kann bis zu fünf Minuten dauern.
{% endalert %}

### Schritt 1: Treasure Data Postback API mit Braze einrichten

Eine Anleitung zur Erstellung einer Postback API finden Sie auf der [Website von Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). Braze sendet die aktualisierten Daten direkt und in Realtime an Treasure Data, mit Ausnahme der Datenaufnahme durch den Event-Collector. Wenn Sie fertig sind, stellt Treasure Data eine URL der Datenquelle zur Verfügung, die Sie für den nächsten Schritt kopieren können.

### Schritt 2: Currents erzeugen

Navigieren Sie in Braze zu **Currents** > **\+ Create Current** > **Treasure Data Export**. Geben Sie einen Namen für die Integration, eine E-Mail an Ihren Kontakt und die URL von Treasure Data an. Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie tracken möchten, und klicken Sie auf **Aktuell starten**.

Alle Ereignisse, die an Treasure Data gesendet werden, enthalten die Daten des Nutzers:in `external_user_id`. Zur Zeit sendet Braze keine Ereignisdaten an Treasure Data für Nutzer:innen, die ihre `external_user_id` nicht eingestellt haben.

{% alert important %}
Halten Sie Ihre Treasure Data URL auf dem neuesten Stand. Wenn die URL Ihres Konnektors falsch ist, kann Braze keine Ereignisse senden. Wenn dieser Zustand länger als 48 Stunden anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

#### Beispiel Ereignisfeldwert
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Beispiel für die aufgenommene Ansicht

![4]{: style="max-width:70%;"}

## Details zur Integration

Braze unterstützt den Export aller Daten, die in den [Currents Event-Glossaren]({{site.baseurl}}/user_guide/data/braze_currents/) aufgeführt sind (einschließlich aller Eigenschaften von [Customer-Engagement-]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) und [Customerverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ) in Treasure Data.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
