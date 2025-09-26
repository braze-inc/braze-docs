---
nav_title: "Attribute des Nutzerprofils"
article_title: "Nutzer:innen-Ansichten für Attribute in Snowflake" 
page_order: 10
page_type: partner
search_tag: Partner
---

# Attribute des Nutzerprofils

> Diese Seite dient als Referenz für die Standard- und angepassten Attribut-Ansichten in Snowflake. Es gibt drei Ansichten für Standardattribute und drei Ansichten für angepasste Attribute, die jeweils für einen bestimmten Anwendungsfall mit seinen eigenen Performance-Überlegungen entwickelt wurden.

{% alert important %}
Die Attribute der Nutzerprofile befinden sich derzeit in der Beta-Phase für Snowflake Data Sharing Kunden. Wenn Sie Snowflake Data Sharing verwenden und Zugang zu dieser Beta-Version wünschen, wenden Sie sich an Ihren Customer-Success-Manager oder den Braze Support.
{% endalert %}

# Verfügbare Ansichten

<table>
  <thead>
    <tr>
      <th>Typ</th>
      <th>Anzeigen</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Standardattribut</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Schnappschüsse von Nutzerprofilen:in</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Nutzer:innen-Profile in Realtime</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historische Änderungsprotokolle</td>
    </tr>
    <tr>
      <td rowspan="3">Angepasstes Attribut</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Schnappschüsse von Nutzerprofilen:in</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Nutzer:innen-Profile in Realtime</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historische Änderungsprotokolle</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Schnappschüsse von Nutzerprofilen:in

Diese Ansichten bieten regelmäßige Schnappschüsse der Attribute des Nutzerprofils. Die Daten werden um bis zu 12 Stunden verzögert, was für Abfragen, die keine Realtime-Updates erfordern, nützlich ist. 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### Schnappschüsse von Nutzerprofilen - Nutzungshinweise

* Liefert eine Momentaufnahme der Attribute von Nutzer:innen mit einer **Verzögerung von bis zu 12 Stunden**.
* Gute Performance bei Abfragen, die keine Realtime-Genauigkeit erfordern.
* Schnellere Abfrageausführung, insbesondere beim Filtern nach anderen Attributen als `USER_ID`.
* **Einschränkung:** Die Daten sind nicht in Realtime auf dem neuesten Stand.

## Echtzeit-Ansichten des Nutzerprofils

Diese Ansichten bieten nahezu Realtime-Updates der Attribute des Nutzerprofils, wobei die Daten bis zu 10 Minuten nach einem Update in Braze verzögert werden.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`
#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJEKT |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### Realtime Ansichten des Nutzerprofils - Nutzungshinweise

* Liefert aktuelle Attribute der Nutzer:innen mit minimaler Verzögerung (~10 Minuten).
* Nützlich für Realtime-Analysen und Szenarien, in denen aktuelle Daten benötigt werden.
* **Überlegungen zur Performance:**
    * Abfragen zu einzelnen Nutzer:innen sind schneller (unter einer Minute bei einem großen Lagerhaus).
    * Abfragen ohne USER_ID-Filter erfordern eine Aggregation über alle Nutzer:innen, was zu deutlich längeren Ausführungszeiten führt.
    * Abfragen eines großen Datensatzes (z.B. über 100 Millionen Nutzer:innen) können viele Minuten dauern.

## Historische Änderungsprotokolle

Diese Ansichten speichern historische Änderungsprotokolle von Nutzer:innen-Attributen, wobei Änderungen mit einer Granularität von 12 Stunden erfasst werden.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schema

| Name der Spalte     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | ZAHL |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTE |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### Historische Änderungsprotokolle - Verwendungshinweise

* Bietet eine Aufzeichnung historischer Änderungen an Nutzer:innen-Attributen.
* Die Daten werden alle 12 Stunden in einem Snapshot festgehalten, d.h. mehrere Updates in diesem Fenster werden zu einem einzigen Datensatz zusammengefasst. Einzelne Änderungen innerhalb dieses Zeitraums werden nicht separat gespeichert.
* `EFF_DT` und `END_DT` markieren den Beginn und das Ende des Attribut-Status eines Nutzers:innen.

# Bewährte Praktiken

## Empfohlene Verwendung der Abfrage

| Anwendungsfall                                               | Empfohlene Ansichten                                   | Anmerkungen                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Allgemeine Abfragen**, die keine aktuellen Updates erfordern | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Schnelle Ausführung, mit Daten, die bis zu 12 Stunden alt sind.                          |
| Abfragen, die die **neuesten Attribute der Nutzer:innen** erfordern       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Bietet Updates nahezu in Realtime, kann aber bei großen Datenmengen langsamer sein. |
| **Historisches Tracking** von Attribut-Änderungen           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Speichert Attribut-Änderungen mit einer Granularität von 12 Stunden.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## Überlegungen zur Performance

* Abfragen auf `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` sollten bei großen Datensätzen (~1 Milliarde Nutzer:innen) in einem großen Lagerhaus in weniger als 10 Sekunden zum Ergebnis führen.
* Abfragen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` für einzelne Nutzer:innen kommen in weniger als einer Minute zurück, skalieren aber schlecht ohne `USER_ID` Filterung.
* Abfragen bei über 100 Millionen Nutzer:innen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` können aufgrund der Aggregation pro Nutzer:in mehrere Minuten dauern.


