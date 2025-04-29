---
nav_title: "Attribute des Nutzerprofils"
article_title: "Nutzer:innen-Ansichten für Attribute in Snowflake" 
page_order: 10
page_type: partner
search_tag: Partner
---

# Standardattribute des Nutzerprofils

> Diese Seite dient als Referenz für die Standardattribut-Ansichten in Snowflake. Es gibt drei Ansichten, die jeweils für einen bestimmten Anwendungsfall mit seinen eigenen Performance-Überlegungen entwickelt wurden.

{% alert important %}
Die Attribute der Nutzerprofile befinden sich derzeit in der Beta-Phase für Snowflake Data Sharing Kunden. Wenn Sie Snowflake Data Sharing verwenden und Zugang zu dieser Beta-Version wünschen, wenden Sie sich an Ihren Customer-Success-Manager oder den Braze Support.
{% endalert %}

## Verfügbare Ansichten

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Diese Ansicht bietet einen periodischen Schnappschuss der Standardattribute des Nutzerprofils. Die Daten werden um bis zu 8 Stunden verzögert, was für Abfragen, die keine Realtime-Updates erfordern, nützlich ist.

#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | ZAHL        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Anmerkungen zur Verwendung

* Liefert eine Momentaufnahme der Attribute von Nutzer:innen mit einer **Verzögerung von bis zu 8 Stunden**.
* Gute Performance bei Abfragen, die keine Realtime-Genauigkeit erfordern.
* Schnellere Abfrageausführung, insbesondere beim Filtern nach anderen Attributen als `USER_ID`.
* **Einschränkung:** Die Daten sind nicht in Realtime auf dem neuesten Stand.

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Diese Ansicht bietet nahezu Realtime-Updates der Attribute des Nutzerprofils, wobei die Daten bis zu 10 Minuten nach einem Update in Braze verzögert werden.

#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | ZAHL        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Anmerkungen zur Verwendung

* Liefert aktuelle Attribute der Nutzer:innen mit minimaler Verzögerung (~10 Minuten).
* Nützlich für Realtime-Analysen und Szenarien, in denen aktuelle Daten benötigt werden.
* **Überlegungen zur Performance:**
    * Abfragen zu einzelnen Nutzer:innen sind schneller (unter einer Minute bei einem großen Lagerhaus).
    * Abfragen ohne USER_ID-Filter erfordern eine Aggregation über alle Nutzer:innen, was zu deutlich längeren Ausführungszeiten führt.
    * Abfragen eines großen Datensatzes (z.B. über 100 Millionen Nutzer:innen) können viele Minuten dauern.

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

Diese Ansicht speichert historische Änderungsprotokolle von Nutzer:innen-Attributen, wobei Änderungen mit einer Granularität von 8 Stunden erfasst werden.

#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | ZAHL        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Anmerkungen zur Verwendung

* Bietet eine Aufzeichnung historischer Änderungen an Nutzer:innen-Attributen.
* Die Daten werden alle acht Stunden in einem Snapshot festgehalten, d.h. mehrere Updates in diesem Fenster werden zu einem einzigen Datensatz zusammengefasst. Einzelne Änderungen innerhalb dieses Zeitraums werden nicht separat gespeichert.
* `EFF_DT` und `END_DT` markieren den Beginn und das Ende des Attribut-Status eines Nutzers:innen.

## Bewährte Praktiken

### Empfohlene Verwendung der Abfrage

| Anwendungsfall                                               | Empfohlene Ansicht                                   | Anmerkungen                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Allgemeine Abfragen**, die keine aktuellen Updates erfordern | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | Schnelle Ausführung, mit Daten, die bis zu 8 Stunden alt sind.                          |
| Abfragen, die die **neuesten Attribute der Nutzer:innen** erfordern       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | Bietet Updates nahezu in Realtime, kann aber bei großen Datenmengen langsamer sein. |
| **Historisches Tracking** von Attribut-Änderungen           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Speichert Attribut-Änderungen mit einer Granularität von 8 Stunden.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### Überlegungen zur Performance

* Abfragen auf `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` sollten bei großen Datensätzen (~1 Milliarde Nutzer:innen) in einem großen Lagerhaus in weniger als 10 Sekunden zum Ergebnis führen.
* Abfragen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` für einen einzelnen Nutzer:innen kommen in weniger als einer Minute zurück, skalieren aber schlecht ohne `USER_ID` Filterung.
* Abfragen bei über 100 Millionen Nutzer:innen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` können aufgrund der Aggregation pro Nutzer:in mehrere Minuten dauern.


