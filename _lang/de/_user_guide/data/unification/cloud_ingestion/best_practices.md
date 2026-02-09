---
nav_title: Bewährte Praktiken
article_title: Best Practices für die Datenaufnahme in der Cloud
toc_headers: h2
page_order: 0
page_type: reference
description: "Diese Seite bietet eine Übersicht über die Datenaufnahme in der Cloud, bewährte Verfahren und Produktbeschränkungen."

---

# Bewährte Praktiken

> Mit Braze Cloud Data Ingestion können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Nutzer:in oder Katalogdaten zu synchronisieren. Wenn Sie diese Daten mit Braze synchronisieren, können Sie sie für Anwendungsfälle wie Personalisierung, Triggering oder Segmentierung nutzen. 

## Die Spalte `UPDATED_AT` verstehen

{% alert note %}
`UPDATED_AT` ist nur für Data Warehouse Integrationen relevant, nicht für S3-Synchronisationen.
{% endalert %}

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten auf Ihrem Braze-Dashboard. Jedes Mal, wenn die Synchronisierung ausgeführt wird, reflektiert Braze alle aktualisierten Daten.

{% alert important %}
Braze CDI synchronisiert Zeilen ausschließlich auf der Grundlage des Wertes `UPDATED_AT`, unabhängig davon, ob der Inhalt der Zeile mit dem aktuellen Wert in Braze übereinstimmt. Daher empfehlen wir, `UPDATED_AT` so zu verwenden, dass nur neue oder aktualisierte Daten synchronisiert werden, um eine unnötige Datenpunkt-Nutzung zu vermeiden.
{% endalert %}

### Beispiel: Wiederkehrende Synchronisation

Um zu veranschaulichen, wie `UPDATED_AT` in einer CDI-Synchronisation verwendet wird, betrachten Sie dieses Beispiel einer wiederkehrenden Synchronisation zum Update von Nutzer:innen-Attributen:

- Dateispeicher 
   - Amazon S3

## Unterstützte Datentypen 

Cloud Data Ingestion unterstützt die folgenden Datentypen: 
- Nutzer:innen-Attribute, einschließlich:
   - Verschachtelte angepasste Attribute
   - Arrays von Objekten
   - Abo-Status
- Angepasste Events
- Kauf-Events
- Artikel im Katalog
- Nutzeranfragen zur Löschung

Sie können Nutzerdaten nach externer ID, Nutzer-Alias, Braze ID, E-Mail oder Telefonnummer aktualisieren. Sie können Nutzer:innen nach externer ID, Nutzer-Alias oder Braze ID löschen. 

## Was wird synchronisiert?

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Wir überprüfen dies anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht. Braze wählt alle Zeilen aus und importiert sie, bei denen `UPDATED_AT` gleich oder größer ist als der letzte `UPDATED_AT` Zeitstempel des letzten erfolgreichen Synchronisierungsauftrags.

Fügen Sie in Ihrem Data Warehouse die folgenden Nutzer:innen und Attribute zu Ihrer Tabelle hinzu und setzen Sie den `UPDATED_AT` Zeitpunkt auf den Zeitpunkt, zu dem Sie diese Daten hinzufügen:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Bei der nächsten geplanten Synchronisierung synchronisiert Braze alle Zeilen mit einem `UPDATED_AT` Zeitstempel, der gleich oder später als der letzte Zeitstempel ist, mit den Nutzerprofilen. Braze aktualisiert oder fügt Felder hinzu, so dass Sie nicht jedes Mal das komplette Nutzerprofil synchronisieren müssen. Nach der Synchronisierung spiegeln die Nutzerprofile die neuen Updates wider:

**Wiederkehrende Synchronisation, zweite Folge am 20\. Juli 2022 um 12 Uhr**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Es wurde eine Zeile hinzugefügt, aber der Wert `UPDATED_AT` liegt vor `2022-07-19 09:07:23` (aus dem ersten Lauf gespeichert). Daher wird keine dieser Zeilen in diesem Lauf synchronisiert. Die letzte `UPDATED_AT` für die Synchronisierung bleibt bei diesem Lauf unverändert und lautet `2022-07-19 09:07:23`.

**Wiederkehrende Synchronisation, dritte Folge am 21\. Juli 2022 um 12 Uhr**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"xyz",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-21 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3”:”2019-07-20T19:20:30+1:00"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In diesem dritten Durchlauf wurde eine weitere neue Zeile hinzugefügt. Jetzt hat eine Zeile einen `UPDATED_AT` Wert, der später ist als `2022-07-19 09:07:23`, was bedeutet, dass nur eine Zeile synchronisiert wird. Die letzte `UPDATED_AT` ist jetzt als `2022-07-21 08:30:00` eingestellt.

{% alert note %}
`UPDATED_AT` Werte dürfen sogar später liegen als die Startzeit für eine bestimmte Synchronisierung. Dies ist jedoch nicht empfehlenswert, da es den letzten `UPDATED_AT` Zeitstempel "in die Zukunft" pusht und nachfolgende Synchronisierungen keine früheren Werte mehr synchronisieren.
{% endalert %}

## Verwenden Sie einen UTC-Zeitstempel für die Spalte `UPDATED_AT` 

Die Spalte `UPDATED_AT` sollte in UTC sein, um Probleme mit der Sommerzeit zu vermeiden. Bevorzugen Sie reine UTC-Funktionen, wie z.B. `SYSDATE()` anstelle von `CURRENT_DATE()`, wann immer dies möglich ist.

## Vergewissern Sie sich, dass die Zeit von `UPDATED_AT` nicht mit der Zeit Ihrer Synchronisierung übereinstimmt.

Ihre CDI-Synchronisierung enthält möglicherweise doppelte Daten, wenn eines der Felder von `UPDATED_AT` genau die gleiche Uhrzeit hat wie der letzte `UPDATED_AT` Zeitstempel des vorherigen erfolgreichen Synchronisierungsauftrags. Das liegt daran, dass CDI eine "inklusive Grenze" wählt, wenn es eine Zeile identifiziert, die mit der vorherigen Synchronisierung übereinstimmt, und die Zeilen synchronisieren kann. CDI testet diese Zeilen erneut und erstellt doppelte Daten.

Hier sind einige Vorschläge, um doppelte Daten zu vermeiden:

- Wenn Sie eine Synchronisierung mit einer `VIEW` einrichten, verwenden Sie nicht `CURRENT_TIMESTAMP` als Standardwert. Dies führt dazu, dass alle Daten jedes Mal synchronisiert werden, wenn die Synchronisierung ausgeführt wird, da das Feld `UPDATED_AT` die Zeit auswertet, zu der unsere Abfragen ausgeführt werden.
- Wenn Sie sehr lang laufende Pipelines oder Abfragen haben, die Daten in Ihre Quelltabelle schreiben, vermeiden Sie es, diese gleichzeitig mit einer Synchronisierung auszuführen oder denselben Zeitstempel für jede eingefügte Zeile zu verwenden.
- Verwenden Sie eine Transaktion, um alle Zeilen zu schreiben, die den gleichen Zeitstempel haben.

### Beispiel: Verwaltung späterer Updates

Dieses Beispiel zeigt den allgemeinen Prozess für die erste Synchronisierung von Daten und die anschließende Aktualisierung von sich ändernden Daten (Deltas) in den nachfolgenden Updates. Nehmen wir an, wir haben eine Tabelle `EXAMPLE_DATA` mit einigen Nutzerdaten. Am Tag 1 hat sie die folgenden Werte:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blau</td>
            <td>380</td>
            <td>FALSCH</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blau</td>
            <td>823</td>
            <td>WAHR</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blau</td>
            <td>384</td>
            <td>WAHR</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>rot</td>
            <td>349</td>
            <td>WAHR</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rot</td>
            <td>813</td>
            <td>FALSCH</td>
        </tr>
    </tbody>
</table>

Um diese Daten in das von CDI erwartete Format zu bringen, könnten Sie die folgende Abfrage ausführen:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nichts davon wurde bisher mit Braze synchronisiert, also fügen Sie alles der Quelltabelle für CDI hinzu:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Eine Synchronisierung wird durchgeführt und Braze hält fest, dass Sie alle verfügbaren Daten bis zum "2023-03-16 15:00:00" synchronisiert haben. Am Morgen des 2\. Tages wird dann ein ETL ausgeführt und einige Felder in Ihrer Nutzer:innen-Tabelle werden aktualisiert (hervorgehoben):

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">rot</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">WAHR</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">(15 %)</td>
            <td>blau</td>
            <td>823</td>
            <td>WAHR</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blau</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSCH</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">grün</td>
            <td>349</td>
            <td>WAHR</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>rot</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSCH</td>
        </tr>
    </tbody>
</table>

Jetzt müssen Sie nur noch die geänderten Werte in die CDI-Quelltabelle einfügen. Diese Zeilen können angehängt werden, anstatt die alten Zeilen zu aktualisieren. Die Tabelle sieht nun wie folgt aus:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

CDI synchronisiert nur die neuen Zeilen. Bei der nächsten Synchronisierung werden also nur die letzten fünf Zeilen synchronisiert.

## Zusätzliche Tipps

### Schreiben Sie nur neue oder aktualisierte Attribute, um den Verbrauch zu minimieren

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Wir überprüfen dies anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht. Braze wählt alle Zeilen aus und importiert sie, bei denen `UPDATED_AT` gleich oder größer ist als der letzte `UPDATED_AT` Zeitstempel des letzten erfolgreichen Synchronisierungsauftrags, unabhängig davon, ob sie mit dem übereinstimmen, was sich derzeit im Nutzerprofil befindet. Wir empfehlen daher, nur Attribute zu synchronisieren, die Sie hinzufügen oder aktualisieren möchten.

Die Datenpunkt-Nutzung ist bei der Verwendung von CDI identisch mit der anderer Ingestion-Methoden wie REST APIs oder SDKs. Sie müssen also sicherstellen, dass Sie nur neue oder aktualisierte Attribute in Ihre Quelltabellen einfügen.

### Trennen Sie `EXTERNAL_ID` von der Spalte `PAYLOAD` 

Das Objekt `PAYLOAD` sollte keine externe ID oder einen anderen ID-Typ enthalten. 

### Ein Attribut entfernen

Wenn Sie ein Attribut aus dem Profil eines Nutzers:in weglassen möchten, können Sie es auf `null` setzen. Wenn Sie möchten, dass ein Attribut unverändert bleibt, senden Sie es nicht an Braze, bevor es nicht aktualisiert worden ist. Um ein Attribut vollständig zu entfernen, verwenden Sie `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Inkrementelle Updates durchführen

Führen Sie inkrementelle Updates Ihrer Daten durch, um unbeabsichtigtes Überschreiben bei gleichzeitigen Updates zu verhindern.

Im folgenden Beispiel hat ein Nutzer:in zwei Attribute:
- Farbe: "Grün"
- Größe: "Groß"

Dann empfängt Braze die folgenden zwei Updates für diesen Nutzer:innen gleichzeitig:
- Anfrage 1: Farbe in "Rot" ändern
- Anfrage 2: Größe auf "Mittel" ändern

Da Anfrage 1 zuerst auftritt, werden die Attribute des Nutzers:innen wie folgt aktualisiert:
- Farbe: "Rot"
- Größe: "Groß"

Bei Anfrage 2 beginnt Braze jedoch mit den ursprünglichen Attributwerten ("Grün" und "Groß") und aktualisiert dann die Attribute des Nutzers:innen wie folgt:
- Farbe: "Grün"
- Größe: "Mittel"

Wenn die Anfragen abgeschlossen sind, überschreibt Anfrage 2 das Update von Anfrage 1\. Daher ist es am besten, wenn Sie Ihre Updates zeitlich staffeln, um zu verhindern, dass Anfragen überschrieben werden.

### Erstellen eines JSON-Strings aus einer anderen Tabelle

Wenn Sie es vorziehen, jedes Attribut intern in einer eigenen Spalte zu speichern, müssen Sie diese Spalten in einen JSON String konvertieren, um die Synchronisierung mit Braze zu befüllen. Dazu können Sie eine Abfrage wie die folgende verwenden:

{% tabs local %}
{% tab Snowflake %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Verwenden Sie den Zeitstempel `UPDATED_AT` 

Wir verwenden den Zeitstempel `UPDATED_AT`, um zu verfolgen, welche Daten erfolgreich mit Braze synchronisiert wurden. Wenn viele Zeilen mit demselben Zeitstempel geschrieben werden, während eine Synchronisierung läuft, kann dies zu doppelten Daten führen, die mit Braze synchronisiert werden. Einige Vorschläge, um doppelte Daten zu vermeiden:
- Wenn Sie eine Synchronisierung mit einer `VIEW` einrichten, verwenden Sie nicht `CURRENT_TIMESTAMP` als Standardwert. Dies führt dazu, dass alle Daten jedes Mal synchronisiert werden, wenn die Synchronisierung ausgeführt wird, da das Feld `UPDATED_AT` die Zeit auswertet, zu der unsere Abfragen ausgeführt werden. 
- Wenn Sie sehr lang laufende Pipelines oder Abfragen haben, die Daten in Ihre Quelltabelle schreiben, vermeiden Sie es, diese gleichzeitig mit einer Synchronisierung auszuführen oder denselben Zeitstempel für jede eingefügte Zeile zu verwenden.
- Verwenden Sie eine Transaktion, um alle Zeilen zu schreiben, die den gleichen Zeitstempel haben.

### Konfiguration der Tabelle

Wir haben ein öffentliches [GitHub-Repository](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion), in dem Kund:in Best Practices oder Code-Snippets austauschen können. Wenn Sie Ihre eigenen Snippets beisteuern möchten, erstellen Sie eine Pull-Anfrage!

### Daten formatieren

Alle Vorgänge, die über den Endpunkt Braze `/users/track` möglich sind, werden durch Cloud Data Ingestion unterstützt, einschließlich der Aktualisierung verschachtelter angepasster Attribute, dem Hinzufügen des Abo-Status und der Synchronisierung von angepassten Events oder Käufen. 

Die Felder in der Nutzlast sollten das gleiche Format haben wie der entsprechende `/users/track` Endpunkt. Detaillierte Formatierungsanforderungen finden Sie im Folgenden:

| Datentyp | Spezifikationen für die Formatierung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Siehe [Nutzer:innen Attribute Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Siehe [Objekt Ereignisse]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Beachten Sie die besondere Anforderung für die [Erfassung von Daten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) in verschachtelten Attributen. 

{% tabs local %}
{% tab Nested Custom Attributes %}
Sie können verschachtelte angepasste Attribute in die Payload-Spalte für eine Synchronisierung mit angepassten Attributen aufnehmen. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Event %}
Um Ereignisse zu synchronisieren, ist ein Ereignisname erforderlich. Formatieren Sie das Feld `time` als String nach ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das Feld `time` nicht vorhanden ist, verwendet Braze den Wert der Spalte `UPDATED_AT` als Ereigniszeit. Andere Felder wie `app_id` und `properties` sind optional. 

Beachten Sie, dass Sie nur ein Ereignis pro Zeile synchronisieren können.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Purchase %}
Um Kauf-Events zu synchronisieren, sind `product_id`, `currency` und `price` erforderlich. Formatieren Sie das Feld `time`, das optional ist, als ISO 8601 String oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das Feld `time` nicht vorhanden ist, verwendet Braze den Wert der Spalte `UPDATED_AT` als Ereigniszeit. Andere Felder, einschließlich `app_id`, `quantity` und `properties` sind optional.

Beachten Sie, dass Sie nur ein Kauf-Ereignis pro Zeile synchronisieren können.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
    }
}
```

{% endtab %}
{% tab Subscription Groups %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Vermeiden Sie Timeouts bei Data Warehouse-Abfragen

Wir empfehlen, die Abfragen innerhalb einer Stunde abzuschließen, um eine optimale Performance zu erzielen und mögliche Fehler zu vermeiden. Wenn Abfragen diesen Zeitrahmen überschreiten, sollten Sie die Konfiguration Ihres Data Warehouse überprüfen. Die Optimierung der Ihrem Warehouse zugewiesenen Ressourcen kann dazu beitragen, die Ausführungsgeschwindigkeit von Abfragen zu verbessern.

## Einschränkungen des Produkts

| Begrenzung            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Sie können jedoch nur eine Integration pro Tabelle oder Ansicht einrichten.                                             |
| Anzahl der Zeilen         | Standardmäßig können pro Lauf bis zu 500 Millionen Zeilen synchronisiert werden. Braze stoppt alle Synchronisierungen mit mehr als 500 Millionen neuen Zeilen. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren Customer-Success-Manager von Braze oder an den Braze Support. |
| Attribute pro Zeile     | Jede Zeile sollte eine einzelne Nutzer:innen ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d.h. ein Array zählt als ein Attribut). |
| Größe der Nutzlast           | Jede Zeile kann eine Nutzlast von bis zu 1 MB enthalten. Braze lehnt Nutzdaten, die größer als 1 MB sind, ab und protokolliert den Fehler "Payload was greater than 1MB" im Synchronisierungsprotokoll zusammen mit der zugehörigen externen ID und der abgeschnittenen Nutzdaten. |
| Datentyp              | Sie können Nutzer:innen-Attribute, Ereignisse und Käufe über die Datenaufnahme in der Cloud synchronisieren.                                                                                                  |
| Braze Region           | Dieses Produkt ist in allen Braze Regionen erhältlich. Jede Braze-Region kann sich mit jeder Daten-Quellregion verbinden.                                                                              |
| Quelle Region       | Braze stellt die Verbindung zu Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region und bei jedem Cloud-Anbieter her.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
