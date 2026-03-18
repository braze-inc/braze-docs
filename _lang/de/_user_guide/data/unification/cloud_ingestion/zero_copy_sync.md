---
nav_title: Zero-Copy-Personalisierung
article_title: Zero-Copy-Personalisierung mit CDI
page_order: 4
page_type: reference
description: "Diese Seite bietet eine Übersicht darüber, wie Sie Braze Canvases mithilfe von CDI triggern können."
---

# Zero-Copy-Personalisierung mit CDI

> Erfahren Sie, wie Sie Canvas-Trigger mithilfe von CDI für eine kopierfreie Personalisierung synchronisieren können. Dieses Feature greift auf benutzerspezifische Informationen aus Ihrer Datenspeicher-Lösung zu und überträgt diese an einen Ziel-Canvas. Canvas-Schritte können optional Felder der Personalisierung enthalten, die nicht in den Braze-Nutzerprofilen persistent gespeichert werden.

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Canvas-Trigger synchronisieren

### Schnellstart-Schritte

Falls Sie bereits mit Braze CDI vertraut sind, beachten Sie bitte, dass die Einrichtung für eine Canvas-Trigger-Synchronisierung weitgehend dem Prozess für [CDI-Integrationen von Nutzerdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) entspricht, mit folgenden Einschränkungen:

- Es werden ausschließlich externe IDs oder Nutzer-Alias-Bezeichner unterstützt. E-Mail-Adressen und Telefonnummern werden nicht als Bezeichner unterstützt.  
- Es können nur bestehende Braze-Nutzer:innen synchronisiert werden. Es können keine neuen Nutzer:innen angelegt werden.  
- `properties` ersetzt die`payload`Spalte. Dies ist ein JSON-String der Felder, die Sie als Canvas-Eingangs-Eigenschaften für die Personalisierung verwenden möchten.

Um zu beginnen, wählen Sie beim Erstellen einer neuen Synchronisierung den Datentyp **„Canvas Triggers“** aus.

### Verwendung von Canvas-Triggern 

#### Schritt 1: Datenquelle für Canvas-Trigger einrichten

{% tabs %}
{% tab Snowflake %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Snowflake ein.

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

Sie können die Datenbank, das Schema und die Tabelle nach Ihren Wünschen benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt des Updates dieser Zeile oder ihres Hinzufügens zur Tabelle. Es werden nur die Zeilen synchronisiert, die seit der letzten Synchronisierung hinzugefügt oder mit einem Update versehen wurden.  
* Entweder`external_id`  oder`alias_name`  und`alias_label`  als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:in, der sich bei Canvas anmelden möchte. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und`ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt.`alias_name`  sollte ein eindeutiger Bezeichner sein, und`alias_label`  gibt den Alias-Typ an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen alias_name pro `alias_label`.  
* `PROPERTIES`: Ein JSON-String mit Feldern, die als Eigenschaften der Personalisierung in Ihrem Canvas verfügbar gemacht werden sollen. Dies sollte Informationen für Nutzer:innen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jeden Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch eine gültige JSON-Zeichenkette sein. Bitte geben Sie einen leeren`{}`String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten

Richten Sie eine Rolle, ein Lager und eine Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits Zugangsdaten aus einer bestehenden Synchronisierung haben, können Sie diese wiederverwenden. Stellen Sie jedoch sicher, dass Sie den Zugriff auf die Quelltabelle der Canvas-Trigger erweitern.  

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

##### Schritt 1.3: Netzwertrichtlinien konfigurieren

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Whitelist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter[ Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Redshift ein.

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

Sie können die Datenbank, das Schema und die Tabelle nach Ihren Wünschen benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt des Updates dieser Zeile oder ihres Hinzufügens zur Tabelle. Es werden nur die Zeilen synchronisiert, die seit der letzten Synchronisierung hinzugefügt oder mit einem Update versehen wurden.  
* Entweder`external_id`  oder`alias_name`  und`alias_label`  als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:in, der sich bei Canvas anmelden möchte. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und`ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt.`alias_name`  sollte ein eindeutiger Bezeichner sein, undalias_label  gibt den Alias-Typ an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`.  
* `PROPERTIES`: Ein JSON-String mit Feldern, die als Eigenschaften der Personalisierung in Ihrem Canvas verfügbar gemacht werden sollen. Dies sollte Informationen für Nutzer:innen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jeden Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch eine gültige JSON-Zeichenfolge sein. Bitte geben Sie einen leeren`{}`String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten

Richten Sie eine Rolle, ein Lager und einen Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits Zugangsdaten aus einer bestehenden Synchronisierung haben, können Sie diese wiederverwenden. Stellen Sie jedoch sicher, dass Sie den Zugriff auf die Quelltabelle der Canvas-Trigger erweitern.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Schritt 1.3: Netzwertrichtlinien konfigurieren 

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Whitelist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter[ Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Schritt 1.1: Erstellen Sie ein neues Projekt oder einen neuen Datensatz für Ihre Quelltabelle (optional).

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Schritt 1.2: Richten Sie Ihre Quelltabelle in BigQuery ein.
Bitte referenzieren Sie bei der Erstellung Ihrer Quelltabelle Folgendes:  

| Feldname | Typ | Erforderlich? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Zeitstempel | Ja | 
| **`PROPERTIES`** | JSON | Ja | 
| **`EXTERNAL_ID`** | STRING | LÖSCHBAR | 
| **`ALIAS_NAME`** | STRING | LÖSCHBAR | 
| **`ALIAS_LABEL`** | STRING | LÖSCHBAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jeden Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch eine gültige JSON-Zeichenfolge sein. Bitte geben Sie einen leeren`{}`String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
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

Erstellen Sie einen Nutzer:in und erteilen Sie Berechtigungen. Sollten Sie bereits Zugangsdaten aus einer anderen Synchronisierung besitzen, können Sie diese wiederverwenden, sofern sie Zugriff auf die Canvas-Trigger-Tabelle haben.

| Berechtigung | Zweck |
| :---- | :---- |
| Nutzer:innen der BigQuery-Verbindung | Ermöglicht Braze die Verbindung. |
| BigQuery-Nutzer:innen | Es ist zulässig, dass Braze Abfragen ausführt, Metadaten liest und Tabellen auflistet. |
| BigQuery-Datenanzeige | Es ist zulässig, dass Braze Datensätze und Inhalte anzeigen kann. |
| BigQuery-Job-Nutzer:innen | Es ist zulässig, dass Braze Aufträge ausführt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Bitte generieren Sie nach der Erteilung der Berechtigungen einen JSON-Schlüssel. Anweisungen finden Sie unter [„Schlüssel erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete)“. Sie werden es später im Braze-Dashboard hochladen.

##### Schritt 1.4: Netzwertrichtlinien konfigurieren 
Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Whitelist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter[ Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Schritt 1.1: Erstellen Sie einen Katalog oder ein Schema für Ihre Quelltabelle.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Schritt 1.2: Richten Sie Ihre Quelltabelle in Databricks ein.

Bitte referenzieren Sie bei der Erstellung Ihrer Quelltabelle Folgendes:

| Feldname | Typ | Erforderlich |
| :---- | :---- | :---- |
| `UPDATED_AT` | Zeitstempel | Ja |
| `PROPERTIES` | JSON | Ja |
| `EXTERNAL_ID` | STRING |  LÖSCHBAR |
| `ALIAS_NAME` | STRING | LÖSCHBAR |
| `ALIAS_LABEL` | STRING | LÖSCHBAR |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sie können das Schema und die Tabelle nach Belieben benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt des Updates dieser Zeile oder ihres Hinzufügens zur Tabelle. Es werden nur die Zeilen synchronisiert, die seit der letzten Synchronisierung hinzugefügt oder mit einem Update versehen wurden.  
* Entweder`external_id`  oder`alias_name`  und`alias_label`  als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.  
  * `EXTERNAL_ID`: Identifiziert den Nutzer:in, der sich bei Canvas anmelden möchte. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen.  
  * `ALIAS_NAME` und`ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt.`alias_name`  sollte ein eindeutiger Bezeichner sein, und`alias_label`  gibt den Alias-Typ an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen alias_name pro `alias_label`.  
* `PROPERTIES`: Ein String oder eine Struktur von Feldern, die als Eigenschaften der Personalisierung in Ihrem Canvas verfügbar gemacht werden sollen. Dies sollte Informationen für Nutzer:innen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jeden Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch gültige JSON-Strings sein. Bitte geben Sie einen leeren`{}`String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
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

Erstellen Sie einen persönlichen Token in Databricks:

1. Bitte wählen Sie Ihren Benutzernamen aus und anschließend die Option **„Benutzereinstellungen“.**  
2. Wählen Sie auf dem Tab **„Zugriffstoken“** **die Option „Neues Token generieren**“ aus**.**  
3. Fügen Sie einen Kommentar hinzu, um den Bezeichner zu identifizieren, beispielsweise „Braze CDI“.  
4. Bitte lassen Sie **das Feld „Lifetime (Tage)“** leer, wenn keine Ablaufzeit festgelegt werden soll, und wählen Sie anschließend **„Generieren**“.  
5. Bitte kopieren Sie das Token und bewahren Sie es sicher auf, um es im Braze-Dashboard zu verwenden.

##### Schritt 1.4: Netzwertrichtlinien konfigurieren 

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Whitelist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter[ Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Schritt 1.1: Richten Sie Ihre Quelltabelle in Fabric ein.

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

Erstellen Sie einen Dienstprinzipal und erteilen Sie Berechtigungen. Falls Sie bereits Zugangsdaten aus einer anderen Synchronisierung besitzen, können Sie diese wiederverwenden. Bitte stellen Sie sicher, dass diese Zugriff auf die Kontentabelle haben.

##### Schritt 1.3: Netzwertrichtlinien konfigurieren 

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Whitelist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter[ Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Um Canvas-Trigger aus dem Dateispeicher zu synchronisieren, erstellen Sie bitte eine Quelldatei mit den folgenden Feldern.

| Feld | Erforderlich | Beschreibung |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Ja, eines von`external_id`  oder `alias_name`, und `alias_label` | Dies ist der Bezeichner des Nutzers:innen, den Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Ja, eines von`external_id`  oder`alias_name`  und `alias_label` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
| `PROPERTIES` | Ja | JSON-String von Feldern, die als Eigenschaften der Personalisierung in Ihrem Canvas verfügbar gemacht werden sollen. Dies sollte Informationen für Nutzer:innen enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Dateinamen müssen den AWS-Regeln entsprechen und eindeutig sein. Fügen Sie Zeitstempel hinzu, um die Eindeutigkeit sicherzustellen. Weitere Informationen zur Synchronisierung mit Amazon S3 finden Sie unter [Dateispeicherintegrationen](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Schritt 2: Bitte konfigurieren Sie Ihr Ziel-Canvas.

1. Richten Sie Ihr Ziel-Canvas für Canvas-Trigger ein. Erstellen Sie eine neue oder wählen Sie eine vorhandene API-triggertes Canvas aus. Anweisungen zum Erstellen einer Leinwand mit einem API-gesteuerten Zeitplan für die Zustellung finden Sie unter [„Eintragstypen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types)“.
2. Nachdem Sie den API-gesteuerten Zeitplan für die Zustellung ausgewählt haben, fahren Sie mit der Einrichtung von Canvas fort und erstellen Sie Ihr Canvas. Canvases können von einfachen Einzelnachrichten bis hin zu komplexen Kunden-Workflows mit mehreren Schritten reichen.
3. Verwenden Sie innerhalb Ihrer Canvas-Schritte [die Canvas-Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), um Nachrichten mit Eigenschaftsfeldern zu personalisieren, die Sie aus Ihrer Quelltabelle synchronisieren möchten.
  * Wenn Sie beispielsweise in Schritt 1 ein Eigenschaftenfeld für instrumentiert haben, würden Sie die`account_balance` folgende Liquid-Vorlage verwenden, um Ihre Nachricht zu personalisieren: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Nachdem Sie Ihre Canvas erstellt haben, starten Sie sie und fahren Sie mit [Schritt 3](#step-3-create-your-zero-copy-sync) fort.

#### Schritt 3: Erstellen Sie Ihre Zero-Copy-Synchronisierung

Nachdem Sie die Quellkonfiguration abgeschlossen und die Ziel-Canvas gestartet haben, erstellen Sie eine neue Datensynchronisierung:

1. Bitte navigieren Sie in Braze zu **„Dateneinstellungen“** > **„Cloud-Datenaufnahme**“.
1. Richten Sie die Verbindung ein, indem Sie die Verbindungsdetails eingeben (oder vorhandene Zugangsdaten wiederverwenden) und die Quelltabelle aus [Schritt 1](#step-1-set-up-data-source-for-canvas-triggers) auswählen.
2. Bitte geben Sie der Integration einen Namen.
3. Bitte wählen Sie den Datentyp **„Canvas-Trigger“** aus.
4. Bitte wählen Sie Ihr Ziel Canvas (aus [Schritt 2](#step-2-configure-your-destination-canvas)).
5. Bitte wählen Sie eine Synchronisierungsfrequenz aus.
6. Bitte stellen Sie Ihre Benachrichtigungseinstellungen ein.
7. Bitte wählen Sie **„Verbindung testen“,** um zu bestätigen, dass alles wie erwartet funktioniert. Wenn Sie eine Verbindung zu Snowflake herstellen möchten, fügen Sie bitte zunächst den auf dem Dashboard angezeigten Public Key zu dem für Braze erstellten Benutzer:in hinzu, um eine Verbindung zu Snowflake herzustellen. Um diesen Schritt abzuschließen, benötigen Sie in Snowflake mindestens die Berechtigung **„SECURITYADMIN**“. 
8. Bitte speichern Sie die Synchronisierung, um mit der Synchronisierung der Canvas-Trigger zu beginnen.

Wenn die Synchronisierung ausgeführt wird, werden die Nutzer:innen in Ihrer Quelltabelle in den Canvas aufgenommen. Nutzen Sie die Canvas-Analytics und die Seite „Cloud Datenaufnahme Sync Logs“, um die Performance zu überwachen.

{% alert tip %}  
Bitte überprüfen Sie Ihre gesamte Konfiguration (vom Synchronisierungsverhalten bis zur Canvas-Einrichtung), um unerwartete Sendungen zu vermeiden. Canvas-Einstellungen wie Rate-Limiting, Frequency-Capping und Segmentierungs-Filter können die Zustellung von Nachrichten weiter verfeinern.<br><br>Wir empfehlen, vor der Implementierung von Produktionsanwendungsfällen einen Probelauf mit einer kleinen oder Test-Zielgruppe durchzuführen.
{% endalert %}

### Überlegungen

CDI Canvas-Trigger nutzen Ihr REST API-Rate-Limit für `/canvas/trigger/send`. Wenn Sie diesen Endpunkt gleichzeitig mit CDI Canvas-Triggern und Ihrer REST API-Integration verwenden, beachten Sie bitte, dass die kombinierte Nutzung auf Ihre Rate-Limits angerechnet wird.

Da die Canvas-Trigger von CDI noch in der Early-Access-Phase sind, beachten Sie bitte die folgenden Details:

* Bis zu 5 aktive Canvas-Trigger-Synchronisierungen pro Workspace  
* Bei jedem Synchronisierungslauf werden Nutzer:innen mit einer maximalen Rate von etwa 3,75 Millionen Nutzer:innen pro Stunde in die jeweiligen Ziele der Canvas-Umgebung übertragen.  
  * Bitte beachten Sie, dass es zu längeren Wartezeiten zwischen dem Eingang in die Quelle und der Darstellung auf Canvas kommen kann, wenn:  
    * Synchronisierung von mehr als 3,75 Millionen Nutzer:innen pro Synchronisierungslauf.  
    * Verwendung von CDI Canvas-Triggern, wenn [die]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) [Rate-Limits]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) Ihrer REST API bereits ausgeschöpft sind[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).