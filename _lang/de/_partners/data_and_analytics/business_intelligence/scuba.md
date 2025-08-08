---
nav_title: Scuba
article_title: Scuba Analytics
description: "Diese technische Referenz von Scuba und Braze beschreibt, wie Sie die Realtime-Daten-Insights von Scuba mit Segmenten von Braze aktivieren."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) ist eine Stack-Plattform für die Zusammenarbeit mit maschinellem Lernen, die für schnelle Zeitreihendaten entwickelt wurde. Scuba erlaubt es Ihnen, Nutzer:innen (auch Akteure genannt) selektiv zu exportieren und in Ihre Braze-Plattform zu laden. In Scuba werden angepasste Eigenschaften von Akteuren verwendet, um Verhaltenstrends zu analysieren, Ihre Daten über verschiedene Plattformen hinweg zu aktivieren und mithilfe von maschinellem Lernen Prognosen zu erstellen.

_Diese Integration wird von Scuba Analytics gepflegt._

## Voraussetzungen

Um Scuba Analytics mit Braze zu verwenden, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
|---|---|
|Scuba API Token | Ein Scuba API Token, das Sie über den Endpunkt `https://{scuba_hostname}/api/create_token` abrufen können. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz](https://scuba.io) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Hochladen Ihrer Scuba-Daten auf Braze

{% alert important %}
Die folgende Anfrage verwendet curl. Für eine bessere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients, wie z.B. Postman.
{% endalert %}

Um Ihre Scuba-Daten auf Braze hochzuladen, stellen Sie eine POST-Anfrage an `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` unter Verwendung des Content-Typs `application/json`:

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
| `BRAZE_API_ENDPOINT`    | Die URL des Braze REST-Endpunkts Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [Rest-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Ihr Braze REST API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `HOSTNAME`              | Der Hostname Ihrer aktuellen Scuba-Instanz.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Ihr Scuba API-Token.                                                                                                                                                                           |
| `TABLE_NAME`            | Die Tabelle, zu der Ihr Datensatz gehört. Weitere Informationen finden Sie unter [Glossar: Tabelle der Datensätze](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | Die Eigenschaft des Akteurs, zu dem Ihr Datensatz gehört. Nur Daten, die diesem Namen entsprechen, werden zurückgegeben. Weitere Informationen finden Sie unter [Glossar: Eigenschaft des Schauspielers](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | Der Zielgruppen-Filter für die Eigenschaften Ihres Akteurs.                                                                                                                                             |
| `ACTOR_ID`              | Die ID der Eigenschaft des Akteurs, zu der Ihr Datensatz gehört. Diese ID entspricht Ihrer `external_id` in Braze. Weitere Informationen finden Sie unter [Glossar: Schauspieler](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | Der Startzeitraum in Form eines BQL-kompatiblen Datums. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | Der Endzeitraum als BQL-kompatibles Datum. Weitere Informationen finden Sie unter [BQL-Syntax und Verwendung](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Optional**: Die maximale Anzahl von Datensätzen, die zurückgegeben werden sollen. Wenn Sie `scuba_record_limit` weglassen, gibt Scuba maximal 100 Datensätze zurück. Um dies zu ändern, weisen Sie `scuba_record_limit` eine beliebige nicht-negative Zahl zu.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Standard-Verhalten

Standardmäßig ist `update_existing_only` auf `false` eingestellt. Dadurch werden Ihre bestehenden Datensätze in Braze aktualisiert und neue Datensätze für noch nicht vorhandene Datensätze erstellt. Um Scuba daran zu hindern, neue Datensätze zu erstellen, setzen Sie `update_existing_only` auf `true`.

### Rate-Limit

Scuba wendet ein Rate-Limits von 50.000 Anfragen pro Minute auf diesen Endpunkt an.

## Erstellen von Segmenten unter Verwendung der Verhaltensdaten von Scuba

Nachdem Sie [Ihre Daten hochgeladen](#uploading-your-scuba-data-to-braze) haben, können Sie in Braze mit den Verhaltensdaten von Scuba Nutzer:innen segmentieren.

### Schritt 1: Ein neues Segment erstellen

Gehen Sie in Braze zu **Zielgruppe** > **Segmente**, wählen Sie dann **Segment erstellen** und geben Sie einen Namen für Ihr Segment ein.

![Erstellen eines neuen Segments in Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Schritt 2: Suchen und wählen Sie das Attribut Scuba

Wählen Sie unter **Segmentdetails** > **Filter** die Option **Angepasste Attribute**.

![Auswählen des Filters 'Angepasstes Attribut' unter 'Segment Details'.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Wählen Sie **Angepasste Attribute suchen** und wählen Sie dann den Namen der Eigenschaft des Akteurs aus, die Sie in Ihrer vorherigen POST-Anfrage verwendet haben.

![Auswählen der Eigenschaft des Akteurs als angepasstes Attribut.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Schritt 3: Konfigurieren Sie das Attribut

Wählen Sie neben dem Namen der Eigenschaft Ihres Akteurs einen Operator und einen Wert (falls zutreffend). Diese Werte werden von den Eigenschaften der Akteure bestimmt, die Sie in Scuba definiert haben. Wenn Sie fertig sind, wählen Sie **Speichern**.

![Wählen Sie einen Operator und einen Wert für den ausgewählten ]({% image_buster /assets/img/scuba/analytics/operator_end.png %})


