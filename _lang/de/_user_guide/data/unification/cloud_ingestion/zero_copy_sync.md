---
nav_title: Personalisierung ohne Kopien
article_title: Personalisierung ohne Kopien mit CDI
page_order: 4
page_type: reference
description: "Diese Seite bietet eine Übersicht darüber, wie Sie Braze Canvase mit CDI triggern können."
---

# Personalisierung ohne Kopien mit CDI

> Lernen Sie, wie Sie Canvas-Trigger mit CDI für eine Personalisierung ohne Kopien synchronisieren können. Dieses Feature greift auf benutzerspezifische Daten aus Ihrer Lösung zur Datenspeicherung zu und gibt sie an ein Ziel-Canvas weiter. Canvas-Schritte können optional Personalisierungsfelder enthalten, die nicht auf Braze Nutzerprofilen persistent sind.

{% alert important %}
CDI Canvas Trigger befinden sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Synchronisierung von Canvas-Triggern

### Schnellstart-Schritte

Wenn Sie bereits mit Braze CDI vertraut sind, beachten Sie bitte, dass die Einrichtung einer Canvas-Trigger-Synchronisierung eng an den Prozess für [Nutzerdaten-CDI-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) angelehnt ist, allerdings mit den folgenden Einschränkungen:

- Es werden nur externe ID- oder Nutzer-Alias-Bezeichner unterstützt. E-Mails und Telefonnummern werden als Bezeichner nicht unterstützt.  
- Nur bestehende Nutzer:innen von Braze können synchronisiert werden. Es können keine neuen Nutzer:innen angelegt werden.  
- `properties` ersetzt die Spalte `payload`. Dies ist ein JSON String mit den Feldern, die Sie als Eigenschaften des Canvas-Eingangs für die Personalisierung verwenden möchten.

Wählen Sie zunächst den Datentyp **Canvas Triggers** aus, wenn Sie eine neue Synchronisierung erstellen.

### Canvas-Trigger verwenden 

#### Schritt 1: Datenquelle für Canvas-Trigger einrichten

{% tabs %}
{% tab Snowflake %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Snowflake ein

Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

Sie können die Datenbank, das Schema und die Tabelle benennen, wie Sie möchten, aber die Spaltennamen sollten mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder der Tabelle hinzugefügt wurde. Nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden, werden synchronisiert.  
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:in. Diese identifizieren die Nutzer:innen, für die Sie Canvas Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:innen, der in den Canvas eintreten soll. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen alias_name pro `alias_label`.  
* `PROPERTIES`: Ein JSON String mit Feldern, die als Eigenschaften für die Personalisierung in Ihrem Canvas zur Verfügung stehen sollen. Diese sollte Nutzer:innen-spezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder Nutzer:in erforderlich. Die Eigenschaften-Werte müssen jedoch ein gültiger JSON-String sein. Geben Sie einen leeren `{}` String ein, wenn es keine Eigenschaften für die Zeile gibt.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten

Richten Sie eine Rolle, ein Lager und einen Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden, aber stellen Sie sicher, dass Sie den Zugriff auf die Quellentabelle der Canvas-Trigger erweitern.  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### Schritt 1.3: Konfigurieren Sie Netzwerkrichtlinien

Wenn Ihr Konto über Netzwerkrichtlinien verfügt, lassen Sie die IPs von Braze auflisten, um die Verbindung zum CDI-Dienst zu aktivieren. Die Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Redshift ein

Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

Sie können die Datenbank, das Schema und die Tabelle benennen, wie Sie möchten, aber die Spaltennamen sollten mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder der Tabelle hinzugefügt wurde. Nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden, werden synchronisiert.  
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:in. Diese identifizieren die Nutzer:innen, für die Sie Canvas Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:innen, der in den Canvas eintreten soll. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und alias_label gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`.  
* `PROPERTIES`: Ein JSON String mit Feldern, die als Eigenschaften für die Personalisierung in Ihrem Canvas zur Verfügung stehen sollen. Diese sollte Nutzer:innen-spezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder Nutzer:in erforderlich. Die Eigenschaften-Werte müssen jedoch ein gültiger JSON String sein. Geben Sie einen leeren `{}` String ein, wenn es keine Eigenschaften für die Zeile gibt.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten

Richten Sie eine Rolle, ein Lager und einen Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden, aber stellen Sie sicher, dass Sie den Zugriff auf die Quellentabelle der Canvas-Trigger erweitern.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Schritt 1.3: Konfigurieren Sie Netzwerkrichtlinien 

Wenn Ihr Konto über Netzwerkrichtlinien verfügt, lassen Sie die IPs von Braze auflisten, um die Verbindung zum CDI-Dienst zu aktivieren. Die Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Schritt 1.1: Erstellen Sie ein neues Projekt oder Dataset für Ihre Quelltabelle (optional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Schritt 1.2: Richten Sie Ihre Quelltabelle in BigQuery ein
Beziehen Sie sich beim Erstellen Ihrer Quelltabelle auf Folgendes:  

| Feldname | Typ | Erforderlich? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Zeitstempel | Ja | 
| **`PROPERTIES`** | JSON | Ja | 
| **`EXTERNAL_ID`** | STRING | LÖSCHBAR | 
| **`ALIAS_NAME`** | STRING | LÖSCHBAR | 
| **`ALIAS_LABEL`** | STRING | LÖSCHBAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder Nutzer:in erforderlich. Die Eigenschaften-Werte müssen jedoch ein gültiger JSON String sein. Geben Sie einen leeren `{}` String ein, wenn es keine Eigenschaften für die Zeile gibt.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### Schritt 1.3: Zugangsdaten einrichten

Erstellen Sie einen Nutzer:in und erteilen Sie Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer anderen Synchronisierung verfügen, können Sie diese wiederverwenden, solange sie Zugriff auf die Tabelle der Canvas-Trigger haben.

| Berechtigung | Zweck |
| :---- | :---- |
| BigQuery-Verbindung Nutzer:in | Erlaubt Braze, eine Verbindung herzustellen. |
| BigQuery Nutzer:in | Erlaubt es Braze, Abfragen auszuführen, Metadaten zu lesen und Tabellen aufzulisten. |
| BigQuery Daten Betrachter | Ermöglicht Braze die Anzeige von Datensätzen und Inhalten. |
| BigQuery Job Nutzer:in | Erlaubt es Braze, Aufträge auszuführen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nachdem Sie die Berechtigungen erteilt haben, erzeugen Sie einen JSON-Schlüssel. Siehe [Schlüssel erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete) für Anweisungen. Sie werden es später im Braze-Dashboard hochladen.

##### Schritt 1.4: Konfigurieren Sie Netzwerkrichtlinien 
Wenn Ihr Konto über Netzwerkrichtlinien verfügt, lassen Sie die IPs von Braze auflisten, um die Verbindung zum CDI-Dienst zu aktivieren. Die Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Schritt 1.1: Erstellen Sie einen Katalog oder ein Schema für Ihre Quelltabelle.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Schritt 1.2: Richten Sie Ihre Quelltabelle in Databricks ein

Beziehen Sie sich beim Erstellen Ihrer Quelltabelle auf Folgendes:

| Feldname | Typ | Erforderlich |
| :---- | :---- | :---- |
| `UPDATED_AT` | Zeitstempel | Ja |
| `PROPERTIES` | JSON | Ja |
| `EXTERNAL_ID` | STRING |  LÖSCHBAR |
| `ALIAS_NAME` | STRING | LÖSCHBAR |
| `ALIAS_LABEL` | STRING | LÖSCHBAR |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sie können das Schema und die Tabelle benennen, wie Sie möchten, aber die Spaltennamen sollten mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder der Tabelle hinzugefügt wurde. Nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden, werden synchronisiert.  
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:in. Diese identifizieren die Nutzer:innen, für die Sie Canvas Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:innen, der in den Canvas eintreten soll. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen alias_name pro `alias_label`.  
* `PROPERTIES`: Ein String oder eine Struktur von Feldern, die als Eigenschaften für die Personalisierung in Ihrem Canvas zur Verfügung stehen sollen. Diese sollte Nutzer:innen-spezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder Nutzer:in erforderlich. Die Eigenschaften-Werte müssen jedoch gültige JSON-Strings sein. Geben Sie einen leeren `{}` String ein, wenn es keine Eigenschaften für die Zeile gibt.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### Schritt 1.3: Zugangsdaten einrichten 

Erstellen Sie ein persönliches Token für den Zugriff in Databricks:

1. Wählen Sie Ihren Benutzernamen und dann **Nutzer:innen aus.**  
2. Auf dem Tab **Zugriffstoken** wählen Sie **Neues Token generieren.**  
3. Fügen Sie einen Kommentar zur Identifizierung des Tokens hinzu, z. B. "Braze CDI".  
4. Lassen Sie **Lifetime (Tage)** leer, wenn Sie kein Ablaufdatum wünschen, und wählen Sie dann **Generieren**.  
5. Kopieren Sie den Token und speichern Sie ihn sicher zur Verwendung im Braze-Dashboard.

##### Schritt 1.4: Konfigurieren Sie Netzwerkrichtlinien 

Wenn Ihr Konto über Netzwerkrichtlinien verfügt, lassen Sie die IPs von Braze auflisten, um die Verbindung zum CDI-Dienst zu aktivieren. Die Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Fabric ein

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### Schritt 1.2: Zugangsdaten einrichten 

Erstellen Sie einen Dienstprinzipal und erteilen Sie Berechtigungen. Wenn Sie bereits Zugangsdaten von einer anderen Synchronisierung haben, können Sie diese wiederverwenden - stellen Sie nur sicher, dass sie Zugriff auf die Konten-Tabelle haben.

##### Schritt 1.3: Konfigurieren Sie Netzwerkrichtlinien 

Wenn Ihr Konto über Netzwerkrichtlinien verfügt, lassen Sie die IPs von Braze auflisten, um die Verbindung zum CDI-Dienst zu aktivieren. Die Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Um Canvas-Trigger aus einem Dateispeicher zu synchronisieren, erstellen Sie eine Quelldatei mit den folgenden Feldern.

| Feld | Erforderlich | Beschreibung |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Ja, eine von `external_id` oder `alias_name`, und `alias_label` | Dies ist der Bezeichner des Nutzers:innen, den Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Ja, eine von `external_id` oder `alias_name` und `alias_label` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
| `PROPERTIES` | Ja | JSON String mit Feldern, die als Eigenschaften für die Personalisierung in Ihrem Canvas zur Verfügung stehen sollen. Diese sollte Nutzer:innen-spezifische Informationen enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Dateinamen müssen den AWS Regeln entsprechen und eindeutig sein. Fügen Sie Zeitstempel hinzu, um die Eindeutigkeit zu gewährleisten. Mehr über die Synchronisierung mit Amazon S3 erfahren Sie unter [Integration von Dateispeichern](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Schritt 2: Konfigurieren Sie Ihr Ziel Canvas

1. Richten Sie Ihr Ziel Canvas für Canvas-Trigger ein. Erstellen Sie ein neues oder wählen Sie ein bestehendes API-getriggertes Canvas aus. Wie Sie einen Canvas mit einem API-getriggerten Zeitplan für die Zustellung erstellen, erfahren Sie unter [Zeitplanarten für Eingänge]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types).
2. Nachdem Sie den Typ des API-getriggerten Zeitplans für die Zustellung ausgewählt haben, fahren Sie mit der Einrichtung von Canvas fort und erstellen Ihren Canvas. Canvase können von einfachen Nachrichten bis hin zu komplexen Kunden:in-Workflows mit mehreren Schritten reichen.
3. Verwenden Sie innerhalb Ihrer Canvas-Schritte die [Eingangs-Eigenschaften von Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), um Nachrichten mit den Eigenschaften zu personalisieren, die Sie aus Ihrer Quelltabelle synchronisieren möchten.
  * Wenn Sie beispielsweise in Schritt 1 ein Eigenschaftsfeld für `account_balance` instrumentiert haben, würden Sie die folgende Liquid-Vorlage verwenden, um Ihre Nachricht zu personalisieren: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Nachdem Sie Ihr Canvas erstellt haben, starten Sie es und fahren Sie mit [Schritt 3](#step-3-create-your-zero-copy-sync) fort.

#### Schritt 3: Erstellen Sie Ihre Nullkopie-Synchronisation

Wenn die Einrichtung Ihrer Datenquelle abgeschlossen ist und der Ziel-Canvas gestartet wurde, erstellen Sie eine neue Datensynchronisation:

1. Gehen Sie in Braze zu **Dateneinstellungen** > **Cloud-Datenaufnahme**.
1. Richten Sie die Verbindung ein, indem Sie Verbindungsdaten (oder vorhandene Zugangsdaten) und die Quelltabelle aus [Schritt 1](#step-1-set-up-data-source-for-canvas-triggers) eingeben.
2. Geben Sie der Integration einen Namen.
3. Wählen Sie den Datentyp des **Canvas-Triggers** aus.
4. Wählen Sie Ihr Ziel Canvas (aus [Schritt 2](#step-2-configure-your-destination-canvas)).
5. Wählen Sie eine Synchronisationsfrequenz.
6. Richten Sie Benachrichtigungseinstellungen ein.
7. Wählen Sie **Verbindung testen**, um zu bestätigen, dass alles wie erwartet funktioniert. Wenn Sie eine Verbindung zu Snowflake herstellen, fügen Sie zunächst den öffentlichen Schlüssel, der auf dem Dashboard angezeigt wird, dem Nutzer:innen hinzu, der für Braze erstellt wurde, um eine Verbindung zu Snowflake herzustellen. Um diesen Schritt auszuführen, benötigen Sie in Snowflake den **SECURITYADMIN-Zugang** oder höher. 
8. Speichern Sie die Synchronisierung, um mit der Synchronisierung von Canvas-Triggern zu beginnen.

Wenn die Synchronisierung läuft, beginnen die Nutzer:innen in Ihrer Quelltabelle, den Canvas zu betreten. Verwenden Sie Canvas Analytics und die Seite mit den Sync-Protokollen für die Datenaufnahme in der Cloud, um die Performance zu überwachen.

{% alert tip %}  
Überprüfen Sie Ihre gesamte Konfiguration (vom Synchronisationsverhalten bis zur Einrichtung von Canvas), um unerwartete Sendungen zu vermeiden. Canvas-Einstellungen wie Rate-Limiting, Frequency-Capping und Segmentierungsfilter können die Zustellung von Nachrichten weiter verfeinern.<br><br>Wir empfehlen die Durchführung eines Testlaufs mit einer kleinen Zielgruppe oder einer Testgruppe, bevor Sie Anwendungsfälle für die Produktion implementieren.
{% endalert %}

### Überlegungen

CDI Canvas-Trigger nutzen Ihr REST API Rate-Limits für `/canvas/trigger/send`. Wenn Sie diesen Endpunkt gleichzeitig mit CDI Canvas-Triggern und Ihrer REST API Integration verwenden, wird die kombinierte Nutzung auf Ihr Rate-Limit angerechnet.

CDI Canvas Trigger befinden sich zwar noch im Anfangsstadium, aber beachten Sie die folgenden Details:

* Bis zu 5 aktive Canvas Trigger-Synchronisationen pro Workspace  
* Jeder Synchronisierungslauf wird Nutzer:innen mit einer maximalen Rate von ca. 3,75 Millionen Nutzern:innen pro Stunde in das jeweilige Ziel Canvas eintragen.  
  * Stellen Sie sich auf längere Zeiten für den Eingang in den Canvas ein, wenn:  
    * Synchronisierung von mehr als 3,75 Millionen Nutzer:innen pro Synchronisierungslauf.  
    * Die Verwendung von CDI Canvas triggert, wenn das Rate-Limit Ihrer REST API für [ `/canvas/trigger/send` bereits gesättigt ist.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)