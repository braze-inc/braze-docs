---
nav_title: Scuba
article_title: Tauchen Analytik
description: "Diese technische Referenz für Scuba und Braze beschreibt, wie Sie Scubas Echtzeit-Dateneinblick mit Braze-Segmenten aktivieren."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Tauchen Analytik

>[Scuba Analytics][1] ist eine umfassende, auf maschinellem Lernen basierende Plattform für die Zusammenarbeit mit Daten, die für schnelle Zeitreihendaten entwickelt wurde. Mit Scuba können Sie selektiv Benutzer (auch Akteure genannt) exportieren und in Ihre Braze-Plattform laden. In Scuba werden benutzerdefinierte Akteurseigenschaften verwendet, um Verhaltenstrends zu analysieren, Ihre Daten über verschiedene Plattformen hinweg zu aktivieren und mithilfe von maschinellem Lernen Vorhersagemodelle zu erstellen.



## Voraussetzungen

Um Scuba Analytics mit Braze zu verwenden, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
|---|---|
|Scuba API Token | Ein Scuba-API-Token, den Sie vom Endpunkt `https://{scuba_hostname}/api/create_token` abrufen können. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Hochladen Ihrer Scuba-Daten auf Braze

{% alert important %}
Die folgende Anfrage verwendet curl. Für eine bessere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients, wie z.B. Postman.
{% endalert %}

Um Ihre Scuba-Daten auf Braze hochzuladen, stellen Sie eine POST-Anfrage an `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` unter Verwendung des `application/json` content-type:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Ersetzen Sie Folgendes:

| Platzhalter             | Beschreibung                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | Die URL des Braze-REST-Endpunkts Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [Rest-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Ihr Braze REST API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `HOSTNAME`              | Der Hostname Ihrer aktuellen Scuba-Instanz.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Ihr Scuba API-Token.                                                                                                                                                                           |
| `TABLE_NAME`            | Die Tabelle, zu der Ihr Datensatz gehört. Weitere Informationen finden Sie unter [Glossar: Tabelle der Datensätze][3].                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | Die Akteurseigenschaft, zu der Ihr Datensatz gehört. Nur Daten, die diesem Namen entsprechen, werden zurückgegeben. Weitere Informationen finden Sie unter [Glossar: Actor-Eigenschaft][4].                                             |
| `ACTOR_PROPERTY_FILTER` | Der Publikums-Suchfilter für Ihre Schauspieler-Eigenschaft.                                                                                                                                             |
| `ACTOR_ID`              | Die ID der Akteurseigenschaft, zu der Ihr Datensatz gehört. Diese ID entspricht Ihrer `external_id` in Braze. Weitere Informationen finden Sie unter [Glossar: Schauspieler][5].                                              |
| `PERIOD_START`          | Der Startzeitraum in Form eines BQL-kompatiblen Datums. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung][6].                                                                                                 |
| `PERIOD_END`            | Die Endperiode als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung][6].                                                                                                   |
| `RECORD_LIMIT`          | **Optional**: Die maximale Anzahl von Datensätzen, die zurückgegeben werden sollen. Wenn Sie `scuba_record_limit` weglassen, gibt Scuba maximal 100 Datensätze zurück. Um dies zu ändern, weisen Sie `scuba_record_limit` eine beliebige nicht-negative Zahl zu.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Standardverhalten

Standardmäßig ist `update_existing_only` auf `false` eingestellt. Dadurch werden Ihre bestehenden Datensätze in Braze aktualisiert und neue Datensätze für noch nicht vorhandene Datensätze erstellt. Um Scuba daran zu hindern, neue Datensätze zu erstellen, setzen Sie `update_existing_only` auf `true`.

### Rate-Limit

Scuba wendet für diesen Endpunkt ein Ratenlimit von 50.000 Anfragen pro Minute an.

## Erstellen von Segmenten mit Scubas Verhaltensdaten

Nachdem Sie [Ihre Daten hochgeladen](#uploading-your-scuba-data-to-braze) haben, können Sie in Braze Benutzersegmente erstellen, indem Sie die Verhaltensdaten von Scuba verwenden.

### Schritt 1: Ein neues Segment erstellen

Gehen Sie in Braze zu **Audience** > **Segmente**, wählen Sie dann **Segment erstellen** und geben Sie einen Namen für Ihr Segment ein.

![Erstellen Sie ein neues Segment in Braze.][501]

### Schritt 2: Suchen und wählen Sie das Attribut Scuba

Wählen Sie unter **Segmentdetails** > **Filter** die Option **Benutzerdefinierte Attribute**.

![Wählen Sie den Filter 'Benutzerdefiniertes Attribut' unter 'Segmentdetails'.][502]

Wählen Sie **Benutzerdefinierte Attribute suchen** und wählen Sie dann den Namen der Akteurseigenschaft, den Sie in Ihrer vorherigen POST-Anfrage verwendet haben.

![Auswählen der Eigenschaft Akteur als benutzerdefiniertes Attribut.][503]

### Schritt 3: Konfigurieren Sie das Attribut

Wählen Sie neben dem Namen Ihrer Akteurseigenschaft einen Operator und einen Wert (falls zutreffend). Diese Werte werden von den Akteurseigenschaften bestimmt, die Sie in Scuba definiert haben. Wenn Sie fertig sind, wählen Sie **Speichern**.

![Wählen Sie eine Bedienung und einen Wert für die ausgewählte ][504]


[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
