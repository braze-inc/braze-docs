---
nav_title: Übersicht
article_title: Übersicht Braze Cloud Data Ingestion 
page_order: 0
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über die Datenaufnahme in der Cloud, bewährte Verfahren und Produktbeschränkungen."

---

# Übersicht Braze Cloud Data Ingestion

> Mit Braze Cloud Data Ingestion können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Nutzer:in oder Katalogdaten zu synchronisieren. Wenn diese Daten mit Braze synchronisiert werden, können sie für Anwendungen wie Personalisierung, Triggern oder Segmentierung genutzt werden. 

## Funktionsweise

Mit Braze Cloud Data Ingestion (CDI) richten Sie eine Integration zwischen Ihrer Data Warehouse Instanz und dem Braze Workspace ein, um Daten auf einer wiederkehrenden Basis zu synchronisieren. Diese Synchronisierung läuft nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen anderen Zeitplan haben. Die Synchronisierung kann so häufig wie alle 15 Minuten oder so selten wie einmal im Monat erfolgen. Sie möchten häufiger als alle 15 Minuten synchronisieren? Dann wenden Sie sich bitte an den zuständigen Customer-Success-Manager oder ziehen Sie für die Datenaufnahme in Echtzeit die Verwendung von REST-API-Aufrufen in Betracht.

Wenn eine Synchronisierung ausgeführt wird, stellt Braze eine direkte Verbindung zu Ihrer Data Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten in Ihrem Braze-Dashboard. Bei jeder Synchronisierung werden alle geänderten Daten in Braze wiedergegeben.

## Unterstützte Datenquellen

Cloud Data Ingestion kann Daten aus den folgenden Quellen mit Braze synchronisieren:

- Data Warehouse-Quellen 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake

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

Nutzerdaten können über externe ID, Nutzer-Alias, Braze ID, E-Mail oder Telefonnummer aktualisiert werden. Nutzer:innen können über externe ID, Nutzer-Alias oder Braze ID gelöscht werden. 

## Was wird synchronisiert?

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Wir überprüfen dies anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht. Zeilen, bei denen `UPDATED_AT` nach der letzten synchronisierten Zeile liegt, werden ausgewählt und an Braze übertragen.

Fügen Sie in Ihrem Data Warehouse die folgenden Nutzer:innen und Attribute zu Ihrer Tabelle hinzu und setzen Sie den `UPDATED_AT` Zeitpunkt auf den Zeitpunkt, zu dem Sie diese Daten hinzufügen:

| UPDATED_AT | EXTERNE_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "Attribut_1": "abcdefg",<br>    "attribut_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "Attribut_1": "abcdefg",<br>    "attribut_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5": "testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "Attribut_1": "abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

Bei der nächsten geplanten Synchronisierung werden alle Zeilen mit einem `UPDATED_AT` Zeitstempel, der später als der jüngste Zeitstempel liegt, mit den Nutzerprofilen von Braze:innen synchronisiert. Die Felder werden aktualisiert oder hinzugefügt, so dass Sie nicht jedes Mal das komplette Nutzerprofil synchronisieren müssen. Nach der Synchronisierung werden die Nutzer:innen mit den neuen Updates versorgt:

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_2"
    },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Anwendungsfälle: Erstmalige Synchronisierung und nachfolgende Updates

Dieses Beispiel veranschaulicht die erstmalige Synchronisierung von Daten und die anschließende Aktualisierung geänderter Daten (Deltas) in den nachfolgenden Updates. Nehmen wir an, wir haben eine Tabelle `EXAMPLE_DATA` mit einigen Nutzerdaten. Am 1\. Tag enthält sie die folgenden Werte:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>Attribut_1</th>
            <th>Attribut_2</th>
            <th>Attribut_3</th>
            <th>Attribut_4</th>
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

Um diese Daten in das von CDI erwartete Format zu bringen, können Sie diese Abfrage ausführen:

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

Nichts davon wurde bisher mit Braze synchronisiert, also fügen Sie alles der CDI-Ausgangstabelle hinzu:

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
            <th>Attribut_1</th>
            <th>Attribut_2</th>
            <th>Attribut_3</th>
            <th>Attribut_4</th>
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

### Anwendungsfälle: Ein Feld in einem bestehenden Array von Objekten aktualisieren

Dieses Beispiel zeigt, wie Sie ein Feld in einem bereits vorhandenen Objekt-Array aktualisieren. Nehmen wir an, wir haben eine Quelltabelle mit der folgenden Definition:

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

In diesem Beispiel möchten wir ein Array der Haustiere hinzufügen, die jedem Nutzer:innen gehören, was `owner_id` entspricht. Insbesondere möchten wir die Identifikation, die Rasse, den Typ und den Namen angeben. Mit dieser Abfrage wird eine Tabelle zur Ansicht ausgefüllt:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

Die erwartete Ausgabe würde wie folgt aussehen:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

Um ein geändertes Namensfeld und ein neues Altersfeld für jeden Eigentümer zu versenden, können Sie mit folgender Abfrage eine Tabelle zur Ansicht ausfüllen:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

Die erwartete Ausgabe würde wie folgt aussehen:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## Datenpunkt-Nutzung

Die Abrechnung von Datenpunkten für Cloud Data Ingestion erfolgt genau wie bei Updates über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion wird auf das verfügbare Rate-Limit angerechnet. Wenn Sie also Daten mit einer anderen Methode senden, wird das Rate-Limit zwischen der Braze API und Cloud Data Ingestion kombiniert.
{% endalert %}

## Empfehlungen zur Einrichtung der Daten

### Verfassen Sie nur neue bzw. aktualisierte Attribute, um Ihren Verbrauch zu minimieren

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Wir überprüfen dies anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht. Alle Zeilen, bei denen `UPDATED_AT` nach der letzten synchronisierten Zeile liegt, werden ausgewählt und in Braze eingefügt, unabhängig davon, ob sie mit den aktuellen Daten im Nutzerprofil übereinstimmen. Synchronisieren Sie am besten nur diejenigen Attribute, die Sie hinzufügen oder aktualisieren möchten.

Der Verbrauch von Datenpunkten ist bei der Verwendung von CDI identisch mit dem anderer Aufnahmeverfahren wie REST APIs oder SDKs. Es liegt also an Ihnen, sicherzustellen, dass Sie nur neue oder aktualisierte Attribute in Ihre Quelltabellen aufnehmen.

### Verwenden Sie einen UTC-Zeitstempel für die Spalte `UPDATED_AT` 

Die Spalte `UPDATED_AT` sollte im UTC-Format geschrieben werden, um Probleme mit der Sommerzeit zu vermeiden. Bevorzugen Sie wenn möglich reine UTC-Funktionen wie `SYSDATE()` anstelle von `CURRENT_DATE()`.

### Vergewissern Sie sich, dass die Zeit von `UPDATED_AT` nicht mit der Zeit Ihrer Synchronisierung übereinstimmt.

Ihre CDI-Synchronisierung enthält möglicherweise doppelte Daten, wenn eines der Felder von `UPDATED_AT` zum exakt gleichen Zeitpunkt wie Ihre vorherige Synchronisierung stattfindet. Der Grund dafür ist, dass das CDI Zeilen, die mit der vorherigen Synchronisierung übereinstimmen, einschließt und diese dann ebenfalls synchronisiert werden. Das CDI nimmt sie also erneut auf und erstellt somit doppelte Daten. 

### Spalte `EXTERNAL_ID` und `PAYLOAD` trennen

Das Objekt `PAYLOAD` sollte keine externe ID oder einen anderen ID-Typ enthalten. 

### Ein Attribut entfernen

Wenn Sie ein Attribut aus dem Nutzerprofil weglassen möchten, können Sie es auf `null` setzen. Wenn Sie möchten, dass ein Attribut unverändert bleibt, senden Sie es nicht an Braze, solange es nicht aktualisiert worden ist. Um ein Attribut vollständig zu entfernen, verwenden Sie `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Inkrementelle Updates durchführen

Führen Sie inkrementelle Updates Ihrer Daten durch, um die unbeabsichtigte Überschreibung bei parallelen Updates zu verhindern.

Im folgenden Beispiel hat ein Nutzer:in zwei Attribute:
- Farbe: "Grün"
- Größe: "Groß"

Dann empfängt Braze die folgenden zwei Updates für diesen Nutzer:innen gleichzeitig:
- Anfrage 1: Farbe in "Rot" ändern
- Anfrage 2: Größe auf "Mittel" ändern

Da Anfrage 1 zuerst auftritt, werden die Attribute des Nutzers:innen wie folgt aktualisiert:
- Farbe: "Rot"
- Größe: "Groß"

Bei Anfrage 2 beginnt Braze jedoch mit den ursprünglichen Attributwerten ("Grün" und "Groß") und aktualisiert dann die Nutzerattribute wie folgt:
- Farbe: "Grün"
- Größe: "Mittel"

Wenn die Anfragen abgeschlossen sind, überschreibt Anfrage 2 die aktualisierte Anfrage 1. Aus diesem Grund sollten Sie Ihre Updates zeitlich staffeln, um zu verhindern, dass Anfragen überschrieben werden.

### JSON-String aus einer anderen Tabelle erstellen

Wenn Sie es vorziehen, jedes Attribut intern in einer eigenen Spalte zu speichern, müssen Sie diese Spalten für die Synchronisierung mit Braze in einen JSON-String konvertieren. Dazu können Sie eine Abfrage wie diese verwenden:

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

Mit dem Zeitstempel `UPDATED_AT` wird verfolgt, welche Daten mit Braze synchronisiert wurden. Wenn viele Zeilen mit demselben Zeitstempel geschrieben werden, während eine Synchronisierung läuft, kann dies zu doppelten Daten führen, die mit Braze synchronisiert werden. So können Sie Doubletten vermeiden:
- Wenn Sie eine Synchronisierung mit einer `VIEW` einrichten, verwenden Sie nicht `CURRENT_TIMESTAMP` als Standardwert. Dies führt dazu, dass alle Daten jedes Mal synchronisiert werden, wenn die Synchronisierung ausgeführt wird, da das Feld `UPDATED_AT` auf die Zeit ausgewertet wird, zu der unsere Abfragen ausgeführt werden. 
- Wenn Sie sehr lang laufende Pipelines oder Abfragen haben, die Daten in Ihre Quelltabelle schreiben, vermeiden Sie es, diese gleichzeitig mit einer Synchronisierung auszuführen oder denselben Zeitstempel für jede eingefügte Zeile zu verwenden.
- Verfassen Sie alle Zeilen, die den gleichen Zeitstempel aufweisen, per Transaktion.

### Konfiguration der Tabelle

Wir haben ein öffentliches [GitHub-Repository](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion), in dem Kund:in Best Practices oder Code-Snippets austauschen können. Wenn Sie Ihre eigenen Snippets beisteuern möchten, erstellen Sie eine Pull-Anfrage.

### Daten formatieren

Alle Vorgänge, die über den Endpunkt Braze `/users/track` möglich sind, werden auch in Cloud Data Ingestion unterstützt. Dies gilt auch für die Aktualisierung verschachtelter angepasster Attribute, die Aufnahme des Abo-Status und die Synchronisierung angepasster Events oder Käufe. 

Die Felder in der Payload sollten das gleiche Format haben wie der entsprechende Endpunkt `/users/track`. Detaillierte Formatierungsanforderungen finden Sie im Folgenden:

| Datentyp | Spezifikationen für die Formatierung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Siehe [Nutzerattributobjekte]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Siehe [Ereignisobjekte]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Siehe [Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/) |

Beachten Sie die besondere Anforderung für die [Erfassung von Daten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) in verschachtelten Attributen. 

{% tabs local %}
{% tab verschachtelte angepasste Attribute %}
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
Um Ereignisse synchronisieren zu können, ist ein Ereignisname erforderlich. Das Feld `time` sollte gemäß ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` formatiert sein. Wenn das Feld `time` nicht vorhanden ist, wird der Wert in Spalte `UPDATED_AT` als Ereigniszeitpunkt verwendet. Andere Felder wie `app_id` und `properties` sind optional. 
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
{% tab Käufe %}
Für die Synchronisierung von Kauf-Events sind der Ereignisname, `product_id`, `currency` und `price` erforderlich. Das optionale Feld `time` sollte gemäß ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` formatiert sein. Wenn das Feld `time` nicht vorhanden ist, wird der Wert in Spalte `UPDATED_AT` als Ereigniszeitpunkt verwendet. Andere Felder wie `app_id`, `quantity` und `properties` sind optional. 

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
{% tab Abo-Gruppen %}
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

### Vermeiden von Timeouts bei Data Warehouse-Abfragen

Wir empfehlen, Abfragen innerhalb einer Stunde abzuschließen, um eine optimale Performance zu erzielen und mögliche Fehler zu vermeiden. Wenn Sie diesen Zeitrahmen überschreiten, sollten Sie die Konfiguration Ihres Data Warehouse überprüfen. Die Optimierung Ihrer Warehouse-Ressourcen kann das Abfragetempo verbessern.

## Einschränkungen des Produkts

| Beschränkungen            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Sie können jedoch nur eine Integration pro Tabelle oder Ansicht einrichten.                                             |
| Anzahl der Zeilen         | Es gibt keine Begrenzung für die Anzahl der Zeilen, die Sie synchronisieren können. Jede Zeile wird nur einmal synchronisiert, basierend auf der Spalte `UPDATED`.                                                            |
| Attribute pro Zeile     | Jede Zeile sollte eine Nutzer-ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (ein Array zählt also als ein Attribut). |
| Payload-Größe           | Jede Zeile kann bis zu 1 MB Nutzlast enthalten. Payloads, die größer als 1 MB sind, werden abgelehnt, und der Fehler "Payload was greater than 1MB" wird zusammen mit der zugehörigen externen ID und den gekürzten Nutzdaten im Synchronisierungsprotokoll erfasst. |
| Datentyp              | Sie können Nutzerattribute, Events und Käufe per Cloud Data Ingestion synchronisieren.                                                                                                  |
| Braze Region           | Dieses Produkt ist in allen Braze Regionen erhältlich. Jede Braze-Region kann sich mit jeder Daten-Quellregion verbinden.                                                                              |
| Herkunftsregion       | Braze kann sich mit Data Warehouses und Clouds in allen Regionen und von sämtlichen Cloud-Anbieter verbinden.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
