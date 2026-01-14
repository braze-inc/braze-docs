---
nav_title: Data Warehouse Integrationen
article_title: Data Warehouse-Integrationen
description: "Auf dieser Seite erfahren Sie, wie Sie Braze Cloud Data Ingestion verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren."
page_order: 2
page_type: reference

---

# Data Warehouse-Speicherintegrationen

> Auf dieser Seite erfahren Sie, wie Sie Braze Cloud Data Ingestion (CDI) verwenden, um relevante Daten mit Ihrer Snowflake, Redshift, BigQuery und Databricks Integration zu synchronisieren.

## Einrichten von Data Warehouse Integrationen

Cloud Data Ingestion-Integrationen erfordern einige Einstellungen auf der Seite von Braze und in Ihrer Data Warehouse-Instanz. Folgen Sie diesen Schritten, um die Integration einzurichten:

{% tabs %}
{% tab Snowflake %}
1. Richten Sie in Ihrer Snowflake-Instanz die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.
2. Erstellen Sie eine neue Integration im Braze Dashboard.
3. Rufen Sie den im Braze-Dashboard bereitgestellten Public Key ab und [fügen Sie ihn zur Authentifizierung an die Nutzer:innen von Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) an.
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert tip %}
Die [Snowflake Schnellstartanleitung](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) enthält Beispielcode und führt Sie durch die erforderlichen Schritte zur Erstellung einer automatisierten Pipeline mit Snowflake Streams und CDI zur Synchronisierung von Daten zu Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Stellen Sie sicher, dass Braze Zugriff auf die Redshift-Tabellen hat, die Sie synchronisieren möchten. Braze wird sich über das Internet mit Redshift verbinden.
2. Richten Sie in Ihrer Redshift-Instanz die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.
3. Erstellen Sie eine neue Integration im Braze Dashboard.
4. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% tab BigQuery %}
1. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf das/die BigQuery-Projekt(e) und den/die Datensatz(e), die die zu synchronisierenden Daten enthalten.  
2. Richten Sie in Ihrem BigQuery-Konto die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
3. Erstellen Sie eine neue Integration im Braze Dashboard.  
4. Testen Sie die Integration und starten Sie die Synchronisierung.  
{% endtab %}
{% tab Databricks %}
1. Erstellen Sie ein Dienst-Konto und erlauben Sie den Zugriff auf das/die Databricks-Projekt(e) und den/die Datensatz(e), die die zu synchronisierenden Daten enthalten.  
2. Richten Sie in Ihrem Databricks-Konto die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
3. Erstellen Sie eine neue Integration im Braze Dashboard.  
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert important %}
Wenn Braze eine Verbindung zu Classic- und Pro SQL-Instanzen herstellt, kann es zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Erstellen Sie einen Dienst-Prinzipal und erlauben Sie den Zugriff auf den Fabric Workspace, der für Ihre Integration verwendet werden soll.   
2. Richten Sie in Ihrem Fabric-Arbeitsbereich die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
3. Erstellen Sie eine neue Integration im Braze Dashboard.  
4. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% endtabs %}

### Schritt 1: Tabellen oder Ansichten einrichten

{% tabs %}
{% tab Snowflake %}

#### Schritt 1.1: Tabelle einrichten

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Sie können die Datenbank, das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` - Die Zeit, zu der diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Wir synchronisieren nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.
- **Nutzer:innen-Spalten** \- Ihre Tabelle kann eine oder mehrere Nutzer:innen-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. 
- `PAYLOAD` – Dies ist ein JSON-String mit den Feldern, die Sie mit dem oder der Nutzer:in in Braze synchronisieren möchten.

#### Schritt 1.2: Einrichten der Rolle und der Datenbankberechtigungen

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Aktualisieren Sie die Namen nach Bedarf, aber die Berechtigungen sollten mit dem vorangegangenen Beispiel übereinstimmen.

#### Schritt 1.3: Richten Sie das Lager ein und geben Sie der Rolle Braze Zugriff

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Das Lagerhaus muss die Option zur **automatischen Wiederaufnahme** aktiviert haben. Wenn dies nicht der Fall ist, müssen Sie Braze zusätzliche `OPERATE` Privilegien für das Warehouse gewähren, damit wir es einschalten können, wenn es an der Zeit ist, die Abfrage auszuführen.
{% endalert %}

#### Schritt 1.4: Einrichten der Nutzer:in

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Nach diesem Schritt teilen Sie die Verbindungsinformationen mit Braze und erhalten einen öffentlichen Schlüssel, den Sie an den Benutzer anhängen können.

{% alert note %}
Wenn Sie verschiedene Arbeitsbereiche mit demselben Snowflake-Konto verbinden, müssen Sie für jeden Braze-Arbeitsbereich, in dem Sie eine Integration erstellen, einen eigenen Benutzer anlegen. Innerhalb eines Arbeitsbereichs können Sie denselben Benutzer für verschiedene Integrationen wiederverwenden. Die Erstellung einer Integration schlägt jedoch fehl, wenn ein Benutzer mit demselben Snowflake-Konto in verschiedenen Arbeitsbereichen dupliziert wird.
{% endalert %}

#### Schritt 1.5: Zulassen von Braze-IPs in der Snowflake-Netzwerkrichtlinie (optional)

Je nach Konfiguration Ihres Snowflake-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Snowflake-Netzwerkrichtlinie zulassen. Weitere Informationen zum Enablement finden Sie in der entsprechenden Snowflake Dokumentation zum [Ändern einer Netzwerkrichtlinie](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie eine neue Datenbank und ein neues Schema für Ihre Quelltabelle einrichten
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Erstellen Sie eine Tabelle (oder Ansicht), die Sie für Ihre CDI-Integration verwenden
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Sie können die Datenbank, das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` - Die Zeit, zu der diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Wir synchronisieren nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.
- **Nutzer:innen-Spalten** \- Ihre Tabelle kann eine oder mehrere Nutzer:innen-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. 
- `PAYLOAD` – Dies ist ein JSON-String mit den Feldern, die Sie mit dem oder der Nutzer:in in Braze synchronisieren möchten.
 
#### Schritt 1.2: Nutzer:in anlegen und Berechtigungen erteilen 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Dies sind die erforderlichen Mindestberechtigungen für diesen Benutzer. Wenn Sie mehrere CDI-Integrationen erstellen, möchten Sie möglicherweise Berechtigungen für ein Schema erteilen oder Berechtigungen über eine Gruppe verwalten. 

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen

Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Ein Beispiel für den Redshift-URL-Endpunkt ist "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Einige wichtige Dinge zu wissen:
- Möglicherweise müssen Sie auch Ihre Sicherheitsgruppen ändern, damit Braze auf Ihre Daten in Redshift zugreifen kann.
- Stellen Sie sicher, dass Sie eingehenden Datenverkehr auf den IPs in der Tabelle und auf dem Port, der für die Abfrage Ihres Redshift-Clusters verwendet wird (Standard ist 5439), ausdrücklich zulassen. Sie sollten die Redshift-TCP-Verbindung an diesem Port ausdrücklich zulassen, auch wenn die Regeln für eingehende Verbindungen auf „Alle zulassen“ eingestellt sind.
- Der Endpunkt für den Redshift-Cluster muss öffentlich zugänglich sein, damit Braze eine Verbindung zu Ihrem Cluster herstellen kann.
     - Wenn Sie nicht möchten, dass Ihr Redshift-Cluster öffentlich zugänglich ist, können Sie eine VPC und eine EC2-Instanz einrichten, die einen SSH-Tunnel für den Zugriff auf die Redshift-Daten verwenden. Weitere Informationen finden Sie in diesem [Beitrag im AWS Knowledge Center](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie ein neues Projekt oder einen neuen Datensatz einrichten, der Ihre Quelltabelle enthält.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen, die Sie für Ihre CDI-Integration verwenden möchten, mit den folgenden Feldern:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| ZEITSTEMPEL | PFLICHTANGABE |
| `PAYLOAD`| JSON | PFLICHTANGABE |
| `EXTERNAL_ID`| STRING | LÖSCHBAR |
| `ALIAS_NAME`| STRING | LÖSCHBAR |
| `ALIAS_LABEL`| STRING | LÖSCHBAR |
| `BRAZE_ID`| STRING | LÖSCHBAR |
| `EMAIL`| STRING | LÖSCHBAR |
| `PHONE`| STRING | LÖSCHBAR |

Sie können das Projekt, den Datensatz und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` - Die Zeit, zu der diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Wir synchronisieren nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.
- **Nutzer:innen-Spalten** \- Ihre Tabelle kann eine oder mehrere Nutzer:innen-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt.
   email varchar,
   phone_number varchar,
- `PAYLOAD` - Dies ist ein JSON String mit den Feldern, die Sie mit dem Nutzer:innen in Braze synchronisieren möchten.

#### Schritt 1.2: Dienstkonto erstellen und Berechtigungen erteilen 

Erstellen Sie ein Service-Konto in GCP, über das Braze eine Verbindung herstellen und Daten aus Ihrer(n) Tabelle(n) lesen kann. Das Konto für den Dienst sollte über die folgenden Berechtigungen verfügen: 

- **Nutzer:in der BigQuery-Verbindung:** Dies ermöglicht Braze, Verbindungen herzustellen
- **BigQuery-Nutzer:innen:** So kann Braze Abfragen ausführen, Datensatz-Metadaten lesen und Tabellen auflisten.
- **BigQuery Daten Betrachter:** So kann Braze auf Datensätze und deren Inhalt zugreifen.
- **Nutzer:in von BigQuery-Jobs:** Dadurch erhält Braze Zugriff auf die Ausführung von Aufträgen

Wenn Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, erzeugen Sie einen JSON-Schlüssel. Weitere Informationen dazu finden Sie [hier](https://cloud.google.com/iam/docs/keys-create-delete). Sie werden dies später auf dem Braze-Dashboard aktualisieren. 

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen    

Wenn Sie über Netzwerkrichtlinien verfügen, müssen Sie Braze Netzwerkzugriff auf Ihre Big Query-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie einen neuen Katalog oder ein neues Schema für Ihre Quelltabelle einrichten.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen, die Sie für Ihre CDI-Integration verwenden möchten, mit den folgenden Feldern:


```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| ZEITSTEMPEL | PFLICHTANGABE |
| `PAYLOAD`| STRING, STRUCT, oder MAP | PFLICHTANGABE |
| `EXTERNAL_ID`| STRING | LÖSCHBAR |
| `ALIAS_NAME`| STRING | LÖSCHBAR |
| `ALIAS_LABEL`| STRING | LÖSCHBAR |
| `BRAZE_ID`| STRING | LÖSCHBAR |
| `EMAIL`| STRING | LÖSCHBAR |
| `PHONE`| STRING | LÖSCHBAR |

Sie können das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` - Die Zeit, zu der diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Wir synchronisieren nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.
- **Nutzer:innen-Spalten** \- Ihre Tabelle kann eine oder mehrere Nutzer:innen-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. 
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. 
- `PAYLOAD` – Dies ist ein String oder Struct der Felder, die Sie mit dem oder der Nutzer:in in Braze synchronisieren möchten.

#### Schritt 1.2: Zugriffs-Token erstellen  

Damit Braze auf Databricks zugreifen kann, muss ein persönliches Token für den Zugriff erstellt werden.

1. Wählen Sie in Ihrem Databricks-Workspace Ihren Databricks-Nutzernamen in der oberen Leiste aus und wählen Sie dann **Nutzereinstellungen** aus der Dropdown-Liste aus.
2. Auf dem Tab Zugriffstoken wählen Sie **Neues Token generieren**.
3. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze-CDI“, und ändern Sie die Lebensdauer des Tokens auf „keine Lebensdauer“, indem Sie das Feld „Lebensdauer (Tage)“ leer lassen.
4. Wählen Sie **Erzeugen**.
5. Kopieren Sie das angezeigte Token, und wählen Sie dann **Fertig**.

Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es im Braze-Dashboard während des Schritts zur Erstellung der Zugangsdaten eingeben müssen.

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen    

Wenn Sie Netzwerkrichtlinien aufgestellt haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 1.1: Dienstprinzipal einrichten und Zugriff gewähren
Braze stellt die Verbindung zu Ihrem Fabric-Warehouse über einen Dienstprinzipal mit Entra ID-Authentifizierung her. Sie erstellen einen neuen Dienstprinzipal, den Braze verwenden kann, und gewähren bei Bedarf Zugriff auf Fabric-Ressourcen. Braze benötigt für die Verbindung die folgenden Angaben:    

* Tenant ID (auch Verzeichnis genannt) für Ihr Azure-Konto 
* Principal ID (auch Anwendungs-ID genannt) für den Auftraggeber des Dienstes 
* Client-Geheimnis für Braze zur Authentifizierung

1. Navigieren Sie im Azure-Portal zu Microsoft Entra Admin Center und dann zu „App-Registrierungen“. 
2. Wählen Sie **\+ Neue Registrierung** unter **Identität** > **Anwendungen** > **App-Registrierungen**.
3. Geben Sie einen Namen ein, und wählen Sie dann `Accounts in this organizational directory only` als unterstützten Kontotyp aus. Wählen Sie dann **Registrieren**. 
4. Wählen Sie die Anwendung (Dienstprinzipal) aus, die Sie gerade erstellt haben, und navigieren Sie dann zu **Zertifikate & secrets** > **\+ New client secret**.
5. Geben Sie eine Beschreibung für das Geheimnis ein und legen Sie einen Ablauf für das Geheimnis fest. Wählen Sie dann **Hinzufügen**. 
6. Notieren Sie sich das Client-Geheimnis, das Sie bei der Einrichtung von Braze verwenden. 

{% alert note %}
Azure erlaubt keinen unbegrenzten Ablauf von Dienst-Prinzipalgeheimnissen. Denken Sie daran, die Zugangsdaten zu aktualisieren, bevor sie ablaufen, um den Fluss der Daten zu Braze aufrechtzuerhalten.
{% endalert %}

#### Schritt 1.2: Zugang zu Fabric-Ressourcen gewähren 
Sie werden Braze den Zugang zu Ihrer Fabric-Instanz ermöglichen. Navigieren Sie in Ihrem Fabric-Administrationsportal zu **Einstellungen** > **Governance und Insights** > **Admin-Portal** > **Tenant-Einstellungen**.    

* Aktivieren Sie in den **Einstellungen für Entwickler:innen** die Option „Dienstprinzipale können Fabric-APIs verwenden“, damit Braze sich über die Microsoft Entra-ID verbinden kann.
* Aktivieren Sie in den **OneLake-Einstellungen** "Nutzer:innen können mit Apps außerhalb von Fabric auf in OneLake gespeicherte Daten zugreifen", damit der Dienstherr auf Daten aus einer externen App zugreifen kann.


#### Schritt 1.3: Tabelle einrichten
Braze unterstützt sowohl Tabellen als auch Ansichten in Fabric Warehouses. Wenn Sie ein neues Data Warehouse erstellen möchten, gehen Sie in der Fabric-Konsole zu **Erstellen > Data Warehouse > Warehouse**. 

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Sie können das Warehouse, das Schema und die Tabelle oder den View beliebig benennen, aber die Spaltennamen sollten mit der vorangegangenen Definition übereinstimmen.

- `UPDATED_AT` - Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Wir synchronisieren nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.
- **Nutzer:innen-Spalten** \- Ihre Tabelle kann eine oder mehrere Nutzer:innen-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. 
- `PAYLOAD` – Dies ist ein JSON-String mit den Feldern, die Sie mit dem oder der Nutzer:in in Braze synchronisieren möchten.


#### Schritt 1.4: Warehouse Connection String abrufen 
Sie benötigen den SQL-Endpunkt für Ihr Warehouse, damit Braze eine Verbindung herstellen kann. Um diese abzurufen, gehen Sie zum **Arbeitsbereich** in Fabric und wählen Sie in der Liste der Elemente mit dem Mauszeiger den Lagernamen aus und wählen Sie **SQL-Verbindungszeichenfolge kopieren**.

![Die Seite "Fabric Console" in Microsoft Azure, auf der Nutzer:innen den SQL Connection String abrufen sollten.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Schritt 1.5: Zulassen von Braze IPs in der Firewall (Optional)

Je nach Konfiguration Ihres Microsoft Fabric-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Firewall zulassen, um den Datenverkehr von Braze zuzulassen. Weitere Informationen zum Enablement finden Sie in der entsprechenden Dokumentation zu [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Schritt 2: Erstellen Sie eine neue Integration im Braze Dashboard

{% tabs %}
{% tab Snowflake %}

Gehen Sie im Braze Dashbord zu **Dateneinstellungen** > **Cloud-Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und dann **Snowflake Import**.

#### Schritt 2.1: Snowflake-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Snowflake Data Warehouse und die Quelltabelle ein und fahren Sie dann mit dem nächsten Schritt fort.

![Die Seite "Neue Importsynchronisation erstellen" für Snowflake im Braze-Dashboard mit den in Schritt 1 eingegebenen Beispieldaten: "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie dann einen Namen für Ihre Synchronisierung und geben Sie die E-Mail-Adressen Ihrer Kontakte ein. Wir verwenden diese Kontaktinformationen, um Sie über Fehler bei der Integration zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungsfehler wie fehlende Tabellen, Berechtigungen und andere. Sie empfangen keine Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können folgende sein:

- Probleme mit der Konnektivität
- Mangel an Ressourcen
- Probleme mit Berechtigungen
- (Nur für Katalogsynchronisationen) Der Katalogträger hat keinen Platz mehr

![Die Seite "Neue Importsynchronisation erstellen" für Snowflake im Braze-Dashboard mit den in Schritt 2 hinzugefügten Beispieldaten: "Synchronisierungsdetails einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

Sie wählen auch den Datentyp und die Synchronisierungsfrequenz. Die Häufigkeit kann zwischen „alle 15 Minuten“ und „einmal pro Monat“ liegen. Wir verwenden die in Ihrem Braze Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind „Angepasste Attribute“, „Angepasste Events“ und „Kauf-Events“, und der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

#### Fügen Sie der Nutzer:in Braze einen Public Key hinzu

An dieser Stelle müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den öffentlichen Schlüssel, der auf dem Dashboard angezeigt wird, dem oder der Nutzer:in hinzu, den oder die Sie für Braze erstellt haben, um sich mit Snowflake zu verbinden.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt austauschen möchten, können wir ein neues Schlüsselpaar erzeugen und Ihnen den neuen öffentlichen Schlüssel zur Verfügung stellen.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Gehen Sie im Braze Dashbord zu **Dateneinstellungen** > **Cloud-Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und dann **Amazon Redshift Import**.

#### Schritt 2.1: Redshift-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Redshift Data Warehouse und die Quelltabelle ein. Wenn Sie einen privaten Netzwerktunnel verwenden, schalten Sie den Schieberegler um und geben Sie die Tunnelinformationen ein. Fahren Sie dann mit dem nächsten Schritt fort.

![Die Seite "Neue Importsynchronisation erstellen" für Redshift im Braze-Dashboard, eingestellt auf Schritt 1: "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie dann einen Namen für Ihre Synchronisierung und geben Sie die E-Mail-Adressen Ihrer Kontakte ein. Wir verwenden diese Kontaktinformationen, um Sie über Fehler bei der Integration zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungsfehler wie fehlende Tabellen, Berechtigungen und andere. Sie empfangen keine Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können folgende sein:

- Probleme mit der Konnektivität
- Mangel an Ressourcen
- Probleme mit Berechtigungen
- (Nur für Katalogsynchronisationen) Der Katalogträger hat keinen Platz mehr

![Die Seite "Neue Importsynchronisation erstellen" für Redshift im Braze-Dashboard mit einigen Beispieldaten, die in Schritt 2 hinzugefügt wurden: "Synchronisierungsdetails einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

Sie wählen auch den Datentyp und die Synchronisierungsfrequenz. Die Häufigkeit kann zwischen „alle 15 Minuten“ und „einmal pro Monat“ liegen. Wir verwenden die in Ihrem Braze Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind „Angepasste Attribute“, „Angepasste Events“ und „Kauf-Events“, und der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden.
{% endtab %}
{% tab BigQuery %}

Gehen Sie im Braze Dashbord zu **Dateneinstellungen** > **Cloud-Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und dann **Google BigQuery Import**.

#### Schritt 2.1: BigQuery-Verbindungsinformationen und Quelltabelle hinzufügen

Laden Sie den JSON-Schlüssel hoch und geben Sie einen Namen für das Dienstkonto an. Geben Sie anschließend die Details Ihrer Quelltabelle ein.

![Die Seite "Neue Importsynchronisation erstellen" für BigQuery im Braze-Dashboard, eingestellt auf Schritt 1: "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie dann einen Namen für Ihre Synchronisierung und geben Sie die E-Mail-Adressen Ihrer Kontakte ein. Wir verwenden diese Kontaktinformationen, um Sie über Fehler bei der Integration zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungsfehler wie fehlende Tabellen, Berechtigungen und andere. Sie werden keine Ausgaben auf Zeilenebene erhalten. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können folgende sein:

- Probleme mit der Konnektivität
- Mangel an Ressourcen
- Probleme mit Berechtigungen
- (Nur für Katalogsynchronisationen) Der Katalogträger hat keinen Platz mehr

![Die Seite "Neue Importsynchronisation erstellen" für BigQuery im Braze-Dashboard, eingestellt auf Schritt 2: "Synchronisierungsdetails einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Sie wählen auch den Datentyp und die Synchronisierungsfrequenz. Die Häufigkeit kann zwischen „alle 15 Minuten“ und „einmal pro Monat“ liegen. Wir verwenden die in Ihrem Braze Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind „Angepasste Attribute“, „Angepasste Events“, „Kauf-Events“ und „Nutzer-Löschvorgänge“. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

{% endtab %}
{% tab Databricks %}

Gehen Sie im Braze Dashbord zu **Dateneinstellungen** > **Cloud-Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und dann **Databricks Import**.

#### Schritt 2.1: Databricks-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Databricks Data Warehouse und die Quelltabelle ein und fahren Sie mit dem nächsten Schritt fort.

![Die Seite "Neue Importsynchronisation erstellen" für Databricks im Braze-Dashboard, eingestellt auf Schritt 1: "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie dann einen Namen für Ihre Synchronisierung und geben Sie die E-Mail-Adressen Ihrer Kontakte ein. Wir verwenden diese Kontaktinformationen, um Sie über Fehler bei der Integration zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungsfehler wie fehlende Tabellen, Berechtigungen und andere. Sie empfangen keine Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können folgende sein:

- Probleme mit der Konnektivität
- Mangel an Ressourcen
- Probleme mit Berechtigungen
- (Nur für Katalogsynchronisationen) Der Katalogträger hat keinen Platz mehr

![Die Seite "Neue Importsynchronisation erstellen" für Databricks im Braze-Dashboard, eingestellt auf Schritt 2: "Synchronisierungsdetails einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

Sie wählen auch den Datentyp und die Synchronisierungsfrequenz. Die Häufigkeit kann zwischen „alle 15 Minuten“ und „einmal pro Monat“ liegen. Wir verwenden die in Ihrem Braze Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind „Angepasste Attribute“, „Angepasste Events“, „Kauf-Events“ und „Nutzer-Löschvorgänge“. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 2.1: Einrichten einer Cloud Data Ingestion-Synchronisation

Sie erstellen eine neue Daten-Synchronisierung für Microsoft Fabric. Gehen Sie im Dashbord von Braze zu **Dateneinstellungen** > **Cloud-Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und dann **Microsoft Fabric Import**.

#### Schritt 2.2: Microsoft Fabric-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihre Microsoft Fabric Warehouse-Zugangsdaten und die Quelltabelle ein und fahren Sie mit dem nächsten Schritt fort.

- „Zugangsdaten-Name“ ist eine Bezeichnung für diese Zugangsdaten in Braze, Sie können hier einen hilfreichen Wert festlegen
- Einzelheiten zum Abrufen von Mandanten-ID, Haupt-ID, Client-Geheimschlüssel und Verbindungs-String finden Sie in Abschnitt 1.

![Die Seite "Neue Importsynchronisation erstellen" für Microsoft im Braze-Dashboard, eingestellt auf Schritt 1: "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### Schritt 2.3: Synchronisierungsdetails konfigurieren

Als nächstes konfigurieren Sie die folgenden Details für Ihre Synchronisierung: 

- Synchronisationsname 
- Datentyp - Unterstützte Datentypen sind angepasste Attribute, angepasste Events, Kauf-Events, Kataloge und Nutzer:innen-Löschungen. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 
- Synchronisierungshäufigkeit - Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. 
  - Nicht wiederkehrende Synchronisierungen können manuell oder über die [API]({{site.baseurl}}/api/endpoints/cdi) ausgelöst werden. 

![Die Seite "Neue Importsynchronisation erstellen" für Microsoft Fabric im Braze-Dashboard, eingestellt auf Schritt 2: "Synchronisierungsdetails einrichten".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### Schritt 2.4: Benachrichtigungseinstellungen konfigurieren

Als nächstes geben Sie die E-Mails der Kontakte ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu benachrichtigen, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle, oder um Sie zu warnen, wenn bestimmte Zeilen nicht aktualisiert werden können.

Kontakt-E-Mails erhalten standardmäßig nur Benachrichtigungen über globale oder Synchronisierungsfehler wie fehlende Tabellen, Berechtigungen und andere. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können folgende sein:

- Probleme mit der Konnektivität
- Mangel an Ressourcen
- Probleme mit Berechtigungen
- (Nur für Katalogsynchronisationen) Der Katalogträger hat keinen Platz mehr

Sie können auch Warnungen für Probleme auf Zeilenebene konfigurieren oder sich bei jeder erfolgreichen Synchronisierung eine Warnung schicken lassen. 

![Die Seite "Neue Importsynchronisation erstellen" für Microsoft Fabric im Braze-Dashboard, eingestellt auf Schritt 3: "Benachrichtigungseinstellungen einrichten".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### Schritt 3: Verbindung testen

{% tabs %}
{% tab Snowflake %}

Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für Snowflake im Braze-Dashboard mit Schritt 3: "Testverbindung" mit Anzeige eines öffentlichen RSA-Schlüssels.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für Redshift im Braze-Dashboard, eingestellt auf Schritt 3: "Verbindung testen".]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für Redshift Private Network im Braze-Dashboard, mit Schritt 4: "Testverbindung" mit Anzeige eines öffentlichen RSA-Schlüssels.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für BigQuery im Braze-Dashboard, eingestellt auf Schritt 3: "Verbindung testen".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für Databricks im Braze-Dashboard, eingestellt auf Schritt 3: "Verbindung testen".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn wir aus irgendeinem Grund keine Verbindung herstellen können, zeigen wir eine Fehlermeldung an, um Ihnen bei der Fehlersuche zu helfen.

![Die Seite "Neue Importsynchronisation erstellen" für Microsoft Fabric im Braze-Dashboard, eingestellt auf Schritt 4: "Verbindung testen".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.  
{% endalert %}

## Zusätzliche Integrationen oder Benutzer einrichten (optional)

{% tabs %}
{% tab Snowflake %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie die vorhandenen Anmeldedaten wiederverwenden, wenn Sie sich mit dem Snowflake-Konto verbinden.

![Die Seite "Neue Importsynchronisation erstellen" für Snowflake im Braze-Dashboard, mit dem in Schritt 1 geöffneten Dropdown "Zugangsdaten auswählen": "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Wenn Sie denselben Benutzer und dieselbe Rolle bei verschiedenen Integrationen wiederverwenden, müssen Sie den öffentlichen Schlüssel **nicht** erneut hinzufügen.
{% endtab %}
{% tab Redshift %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie die vorhandenen Anmeldeinformationen wiederverwenden, wenn Sie sich mit demselben Snowflake- oder Redshift-Konto verbinden.

![Die Seite "Neue Importsynchronisation erstellen" für Redshift im Braze-Dashboard, mit dem in Schritt 1 geöffneten Dropdown "Zugangsdaten auswählen": "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Wenn Sie denselben Nutzer:in verschiedenen Integrationen wiederverwenden, können Sie den Nutzer:in im Braze-Dashboard erst löschen, wenn er aus allen aktiven Synchronisierungen entfernt wurde.
{% endtab %}
{% tab BigQuery %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie die vorhandenen Anmeldeinformationen wiederverwenden, wenn Sie sich mit demselben BigQuery-Konto verbinden.

![Die Seite "Neue Importsynchronisation erstellen" für BigQuery im Braze-Dashboard, mit dem in Schritt 1 geöffneten Dropdown "Zugangsdaten auswählen": "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Wenn Sie denselben Nutzer:in verschiedenen Integrationen wiederverwenden, können Sie den Nutzer:in im Braze-Dashboard erst löschen, wenn er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Databricks %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Bei der Erstellung zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Databricks-Konto verbinden.

![Die Seite "Neue Importsynchronisation erstellen" für Databricks im Braze-Dashboard, mit der in Schritt 1 geöffneten Dropdown-Liste "Zugangsdaten auswählen": "Verbindung einrichten".]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Wenn Sie denselben Nutzer:in verschiedenen Integrationen wiederverwenden, können Sie den Nutzer:in im Braze-Dashboard erst löschen, wenn er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Microsoft Fabric %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Fabric-Konto verbinden.

Wenn Sie denselben Nutzer:in verschiedenen Integrationen wiederverwenden, können Sie den Nutzer:in im Braze-Dashboard erst löschen, wenn er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% endtabs %}

## Ausführen der Synchronisation

{% tabs %}
{% tab Snowflake %}
Wenn diese Funktion aktiviert ist, wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan durchgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

![Die Seite "Datenimport" für Snowflake im Braze-Dashboard zeigt die Option "Jetzt synchronisieren" aus dem vertikalen Ellipsenmenü an.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Wenn diese Funktion aktiviert ist, wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan durchgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

![Die Seite "Datenimport" für Redshift im Braze-Dashboard zeigt die Option "Jetzt synchronisieren" aus dem vertikalen Ellipsenmenü an.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Wenn diese Funktion aktiviert ist, wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan durchgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

![Die Seite "Datenimport" für BigQuery im Braze-Dashboard zeigt die Option "Jetzt synchronisieren" aus dem vertikalen Ellipsenmenü an.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Wenn diese Funktion aktiviert ist, wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan durchgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

![Die Seite "Datenimport" für Databricks im Braze-Dashboard, die die Option "Jetzt synchronisieren" aus dem vertikalen Ellipsenmenü anzeigt.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Wenn diese Funktion aktiviert ist, wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan durchgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}

{% endtabs %}

