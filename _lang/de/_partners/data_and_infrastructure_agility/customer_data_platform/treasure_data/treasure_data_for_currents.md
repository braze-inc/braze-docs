---
nav_title: Schatzdaten für Ströme
article_title: Schatzdaten für Ströme
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Treasure Data, einer Plattform für Unternehmenskundendaten, mit der Sie Auftragsergebnisse direkt in Braze schreiben können."
page_type: partner
tool: Currents
search_tag: Partner


---


# Schatzdaten für Ströme

> [Treasure Data][1] ist eine Kundendatenplattform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl von anderen Stellen in Ihrem Marketing-Stack weiterleitet.

Die Integration von Braze und Treasure Data ermöglicht Ihnen die nahtlose Kontrolle des Informationsflusses zwischen den beiden Systemen. Mit Currents können Sie die Daten auch mit Treasure Data verbinden, um sie über den gesamten Wachstumsbereich hinweg nutzbar zu machen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data-Konto][0]. |
| Currents | Um Daten zurück in Treasure Data zu exportieren, müssen Sie [Braze Currents][2] für Ihr Konto eingerichtet haben. |
| Schatzdaten-URL | Diese können Sie erhalten, indem Sie zu Ihrem Treasure Data-Dashboard navigieren und die Ingestion-URL kopieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Treasure Data protokolliert jedes Ereignis in Stapeln. Weitere Informationen darüber, wie Sie Treasure Data abfragen können, um die Anzahl der Ereignisse zu ermitteln, finden Sie unter [Braze Currents Import Integration](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration).
{% endalert %}

## Integration

Die empfohlene Methode zur Verbindung mit Treasure Data ist die Postback-API. Diese Methode erfordert keinen Standard-Connector und die Daten können über einen Push-Ansatz empfangen werden. Alle in einem Datenstapel gesendeten Ereignisse befinden sich in einem Feld einer Zeile in einem JSON-Array, das geparst werden muss, um die erforderlichen Daten zu erhalten.

{% alert important %}
Die Aufnahme in Treasure Data durch den Event-Collector erfolgt derzeit nicht in Echtzeit und kann bis zu fünf Minuten dauern.
{% endalert %}

### Schritt 1: Treasure Data Postback API mit Braze einrichten

Eine Anleitung zur Erstellung einer Postback-API finden Sie auf der [Treasure Data-Website][3]. Braze sendet die aktualisierten Ereignisse direkt und in Echtzeit an Treasure Data, mit Ausnahme der Aufnahme durch Event-Collector. Wenn Sie fertig sind, stellt Treasure Data eine URL der Datenquelle zur Verfügung, die Sie für den nächsten Schritt kopieren können.

### Schritt 2: Aktuell erstellen

Navigieren Sie in Braze zu **Strömungen** > **\+ Strömung erstellen** > **Schatzdatenexport**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail und Ihre Treasure Data-URL an. Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie verfolgen möchten, und klicken Sie auf **Aktuell starten**.

Alle Ereignisse, die an Treasure Data gesendet werden, enthalten die `external_user_id` des Benutzers. Zur Zeit sendet Braze keine Ereignisdaten an Treasure Data für Benutzer, die ihre `external_user_id` nicht eingestellt haben.

{% alert important %}
Halten Sie Ihre Treasure Data URL auf dem neuesten Stand. Wenn die URL Ihres Connectors falsch ist, kann Braze keine Ereignisse senden. Wenn dies länger als 48 Stunden andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
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

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) aufgeführt sind (einschließlich aller Eigenschaften in den Ereignissen [zur Nachrichteneinbindung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) und zum [Kundenverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) ) in Treasure Data.

Die Payload-Struktur für exportierte Daten ist die gleiche wie die Payload-Struktur für benutzerdefinierte HTTP-Konnektoren, die Sie im [Repository für Beispiele für benutzerdefinierte HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.


[0]: https://console.treasuredata.com/users/sign_in
[1]: https://www.treasuredata.com/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents
[3]: https://docs.treasuredata.com/display/public/PD/Postback+API
[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
