---
nav_title: Integration von Data Warehouses
article_title: Data Warehouse-Integrationen
alias: /partners/databricks/
description: "Auf dieser Seite erfahren Sie, wie Sie Braze Cloud Data Ingestion verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren."
page_order: 2
page_type: reference

---

# Data Warehouse-Speicherintegrationen

> Auf dieser Seite erfahren Sie, wie Sie Braze Cloud Data Ingestion (CDI) verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren.

## Einrichten von Data Warehouse-Integrationen

Cloud Data Ingestion-Integrationen erfordern einige Einstellungen auf der Seite von Braze und in Ihrer Data Warehouse-Instanz. Folgen Sie diesen Schritten, um die Integration einzurichten:

{% tabs %}
{% tab Snowflake %}
1. Richten Sie in Ihrer Snowflake-Instanz die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.
2. Erstellen Sie eine neue Integration im Braze-Dashboard.
3. Rufen Sie den im Braze-Dashboard bereitgestellten Public Key ab und [fügen Sie ihn zur Authentifizierung an die Snowflake-Nutzer:innen](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) an.
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert tip %}
Die [Snowflake-Schnellstartanleitung](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) enthält Beispielcode und führt Sie durch die erforderlichen Schritte zur Erstellung einer automatisierten Pipeline mit Snowflake Streams und CDI zur Synchronisierung von Daten zu Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Stellen Sie sicher, dass Braze Zugriff auf die Redshift-Tabellen hat, die Sie synchronisieren möchten. Braze stellt die Verbindung zu Redshift über das Internet her.
2. Richten Sie in Ihrer Redshift-Instanz die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.
3. Erstellen Sie eine neue Integration im Braze-Dashboard.
4. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% tab BigQuery %}
1. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf das/die BigQuery-Projekt(e) und den/die Datensatz/Datensätze, die die zu synchronisierenden Daten enthalten.  
2. Richten Sie in Ihrem BigQuery-Konto die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
3. Erstellen Sie eine neue Integration im Braze-Dashboard.  
4. Testen Sie die Integration und starten Sie die Synchronisierung.  
{% endtab %}
{% tab Databricks %}
1. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf das/die Databricks-Projekt(e) und den/die Datensatz/Datensätze, die die zu synchronisierenden Daten enthalten.  
2. Richten Sie in Ihrem Databricks-Konto die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
3. Erstellen Sie eine neue Integration im Braze-Dashboard.  
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert important %}
Wenn Braze eine Verbindung zu Classic- und Pro SQL-Instanzen herstellt, kann es zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Erstellen Sie einen Dienstprinzipal und gewähren Sie Zugriff auf Fabric-APIs.
2. Richten Sie einen gemeinsamen Workspace ein und gewähren Sie dem Dienstprinzipal Zugriff darauf.
3. Richten Sie im gemeinsamen Fabric-Workspace, den Sie in Schritt 2 erstellt haben, die Tabellen oder Ansichten ein, die Sie mit Braze synchronisieren möchten.   
4. Erstellen Sie eine neue Integration im Braze-Dashboard.  
5. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% endtabs %}

### 1. Schritt: Tabellen oder Ansichten einrichten

{% tabs %}
{% tab Snowflake %}

#### Schritt 1.1: Tabelle einrichten

```sql
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
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Sie können die Datenbank, das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` – Identifiziert die Nutzerin oder den Nutzer, die/den Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Die Braze-Nutzer:innen-Kennung. Diese wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert.
- `PAYLOAD` – Ein JSON-String mit den Feldern, die Sie mit der Nutzerin oder dem Nutzer in Braze synchronisieren möchten.

#### Schritt 1.2: Rolle und Datenbankberechtigungen einrichten

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Aktualisieren Sie die Namen nach Bedarf, aber die Berechtigungen sollten mit dem vorangegangenen Beispiel übereinstimmen.

#### Schritt 1.3: Warehouse einrichten und der Braze-Rolle Zugriff gewähren

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Das Warehouse muss die Option zur **automatischen Wiederaufnahme** aktiviert haben. Wenn dies nicht der Fall ist, müssen Sie Braze zusätzliche `OPERATE`-Privilegien für das Warehouse gewähren, damit wir es einschalten können, wenn es an der Zeit ist, die Abfrage auszuführen.
{% endalert %}

#### Schritt 1.4: Nutzer:in einrichten

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Nach diesem Schritt teilen Sie die Verbindungsinformationen mit Braze und erhalten einen Public Key, den Sie an die Nutzerin oder den Nutzer anhängen können.

{% alert note %}
Wenn Sie verschiedene Workspaces mit demselben Snowflake-Konto verbinden, müssen Sie für jeden Braze-Workspace, in dem Sie eine Integration erstellen, eine eigene Nutzerin oder einen eigenen Nutzer anlegen. Innerhalb eines Workspace können Sie dieselbe Nutzerin oder denselben Nutzer für verschiedene Integrationen wiederverwenden. Die Erstellung einer Integration schlägt jedoch fehl, wenn eine Nutzerin oder ein Nutzer mit demselben Snowflake-Konto in verschiedenen Workspaces dupliziert wird.
{% endalert %}

#### Schritt 1.5: Braze-IPs in der Snowflake-Netzwerkrichtlinie zulassen (optional)

Je nach Konfiguration Ihres Snowflake-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Snowflake-Netzwerkrichtlinie zulassen. Weitere Informationen dazu finden Sie in der entsprechenden Snowflake-Dokumentation zum [Ändern einer Netzwerkrichtlinie](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie eine neue Datenbank und ein neues Schema für Ihre Quelltabelle einrichten:
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Erstellen Sie eine Tabelle (oder Ansicht) für Ihre CDI-Integration:
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Sie können die Datenbank, das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` – Identifiziert die Nutzerin oder den Nutzer, die/den Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Die Braze-Nutzer:innen-Kennung. Diese wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert.
- `PAYLOAD` – Ein JSON-String mit den Feldern, die Sie mit der Nutzerin oder dem Nutzer in Braze synchronisieren möchten.
 
#### Schritt 1.2: Nutzer:in anlegen und Berechtigungen erteilen

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Dies sind die erforderlichen Mindestberechtigungen für diese Nutzerin oder diesen Nutzer. Wenn Sie mehrere CDI-Integrationen erstellen, möchten Sie möglicherweise Berechtigungen für ein Schema erteilen oder Berechtigungen über eine Gruppe verwalten. 

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen

Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Ein Beispiel für den Redshift-URL-Endpunkt ist „example-cluster.ap-northeast-2.redshift.amazonaws.com".

Einige wichtige Hinweise:
- Möglicherweise müssen Sie auch Ihre Sicherheitsgruppen ändern, damit Braze auf Ihre Daten in Redshift zugreifen kann.
- Stellen Sie sicher, dass Sie eingehenden Datenverkehr auf den IPs in der Tabelle und auf dem Port, der für die Abfrage Ihres Redshift-Clusters verwendet wird (Standard ist 5439), ausdrücklich zulassen. Sie sollten die Redshift-TCP-Verbindung an diesem Port ausdrücklich zulassen, auch wenn die Regeln für eingehende Verbindungen auf „Alle zulassen" eingestellt sind.
- Der Endpunkt für den Redshift-Cluster muss öffentlich zugänglich sein, damit Braze eine Verbindung zu Ihrem Cluster herstellen kann.
     - Wenn Sie nicht möchten, dass Ihr Redshift-Cluster öffentlich zugänglich ist, können Sie eine VPC und eine EC2-Instanz einrichten, die einen SSH-Tunnel für den Zugriff auf die Redshift-Daten verwenden. Weitere Informationen finden Sie in diesem [Beitrag im AWS Knowledge Center](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie ein neues Projekt oder einen neuen Datensatz einrichten, der Ihre Quelltabelle enthält.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
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
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Sie können das Projekt, den Datensatz und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` – Identifiziert die Nutzerin oder den Nutzer, die/den Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Die Braze-Nutzer:innen-Kennung. Diese wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert.
- `PAYLOAD` – Ein JSON-String mit den Feldern, die Sie mit der Nutzerin oder dem Nutzer in Braze synchronisieren möchten.

{% alert important %}
**BigQuery-Partitionierung**

CDI unterstützt Partitionen für BigQuery. Wenn Sie nach einer Funktion von `UPDATED_AT` partitionieren (beispielsweise nach Tages-, Wochen- oder Stundenauflösung, abhängig von der Größe Ihres Datensatzes), kann BigQuery die zu scannenden Daten reduzieren. Dies verbessert die Performance und Effizienz bei sehr großen Tabellen.

Partitionieren Sie nicht nach anderen Feldern. Testen Sie verschiedene Konfigurationen, um die optimale Einstellung für Ihre spezifischen Daten zu ermitteln.

Alle CDI-Abfragen filtern nach `UPDATED_AT`, jedoch kann sich dieses Verhalten ändern. Entwerfen Sie Ihr Tabellenschema so, dass Abfragen diese Klausel _nicht_ zwingend enthalten müssen.

Weitere Informationen finden Sie in der [Dokumentation zur Partitionierung in BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Schritt 1.2: Dienstkonto erstellen und Berechtigungen erteilen 

Erstellen Sie ein Dienstkonto in GCP, über das Braze eine Verbindung herstellen und Daten aus Ihrer/Ihren Tabelle(n) lesen kann. Das Dienstkonto sollte über die folgenden Berechtigungen verfügen: 

- **BigQuery Connection User:** Ermöglicht Braze, Verbindungen herzustellen.
- **BigQuery User:** Ermöglicht Braze, Abfragen auszuführen, Datensatz-Metadaten zu lesen und Tabellen aufzulisten.
- **BigQuery Data Viewer:** Ermöglicht Braze, Datensätze und deren Inhalt einzusehen.
- **BigQuery Job User:** Ermöglicht Braze, Aufträge auszuführen.

Wenn Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, erzeugen Sie einen JSON-Schlüssel. Weitere Informationen dazu finden Sie [hier](https://cloud.google.com/iam/docs/keys-create-delete). Sie werden diesen später im Braze-Dashboard hochladen. 

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen    

Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Schritt 1.1: Tabelle einrichten 

Optional können Sie einen neuen Katalog oder ein neues Schema für Ihre Quelltabelle einrichten.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:


```sql
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
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT oder MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Sie können das Schema und die Tabelle nach Belieben benennen, aber die Spaltennamen sollten mit der vorherigen Definition übereinstimmen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` – Identifiziert die Nutzerin oder den Nutzer, die/den Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Die Braze-Nutzer:innen-Kennung. Diese wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. 
    - `EMAIL` – Die E-Mail-Adresse der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert.
- `PAYLOAD` – Ein String oder Struct der Felder, die Sie mit der Nutzerin oder dem Nutzer in Braze synchronisieren möchten.

#### Schritt 1.2: Zugriffs-Token erstellen  

Damit Braze auf Databricks zugreifen kann, muss ein persönliches Zugriffs-Token erstellt werden.

1. Wählen Sie in Ihrem Databricks-Workspace Ihren Databricks-Nutzernamen in der oberen Leiste aus und wählen Sie dann **Nutzereinstellungen** aus dem Dropdown-Menü.
2. Wählen Sie auf dem Tab „Zugriffs-Token" die Option **Neues Token generieren**.
3. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze CDI", und ändern Sie die Lebensdauer des Tokens auf „keine Lebensdauer", indem Sie das Feld „Lebensdauer (Tage)" leer lassen.
4. Wählen Sie **Generieren**.
5. Kopieren Sie das angezeigte Token und wählen Sie dann **Fertig**.

Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es im Braze-Dashboard während des Schritts zur Erstellung der Zugangsdaten eingeben müssen.

#### Schritt 1.3: Zugriff auf Braze-IPs zulassen    

Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 1.1: Dienstprinzipal einrichten und Zugriff gewähren
Braze stellt die Verbindung zu Ihrem Fabric-Warehouse über einen Dienstprinzipal mit Entra-ID-Authentifizierung her. Sie erstellen einen neuen Dienstprinzipal, den Braze verwenden kann, und gewähren bei Bedarf Zugriff auf Fabric-Ressourcen. Braze benötigt für die Verbindung die folgenden Angaben:    

* Tenant-ID (auch Verzeichnis-ID genannt) für Ihr Azure-Konto 
* Principal-ID (auch Anwendungs-ID genannt) für den Dienstprinzipal 
* Client-Geheimnis für die Authentifizierung von Braze

1. Navigieren Sie im Azure-Portal zum Microsoft Entra Admin Center und dann zu „App-Registrierungen". 
2. Wählen Sie **+ Neue Registrierung** unter **Identität** > **Anwendungen** > **App-Registrierungen**.
3. Geben Sie einen Namen ein und wählen Sie dann `Accounts in this organizational directory only` als unterstützten Kontotyp aus. Wählen Sie dann **Registrieren**. 
4. Wählen Sie die soeben erstellte Anwendung (Dienstprinzipal) aus und navigieren Sie zu **Zertifikate & Geheimnisse** > **+ Neues Client-Geheimnis**.
5. Geben Sie eine Beschreibung für das Geheimnis ein und legen Sie einen Ablaufzeitraum fest. Wählen Sie dann **Hinzufügen**. 
6. Notieren Sie sich das erstellte Client-Geheimnis für die Einrichtung von Braze. 

{% alert note %}
Azure erlaubt keinen unbegrenzten Ablauf von Dienstprinzipal-Geheimnissen. Denken Sie daran, die Zugangsdaten zu aktualisieren, bevor sie ablaufen, um den Datenfluss zu Braze aufrechtzuerhalten.
{% endalert %}

#### Schritt 1.2: Zugang zu Fabric-Ressourcen gewähren 
Sie gewähren Braze den Zugang, um sich mit Ihrer Fabric-Instanz zu verbinden. Navigieren Sie in Ihrem Fabric-Administrationsportal zu **Einstellungen** > **Governance und Insights** > **Admin-Portal** > **Tenant-Einstellungen**.    

* Aktivieren Sie in den **Entwicklereinstellungen** die Option **Dienstprinzipale können Fabric-APIs verwenden**, damit Braze sich über Microsoft Entra ID verbinden kann.
* Aktivieren Sie in den **OneLake-Einstellungen** die Option **Nutzer:innen können mit Apps außerhalb von Fabric auf in OneLake gespeicherte Daten zugreifen**, damit der Dienstprinzipal auf Daten aus einer externen App zugreifen kann.

#### Schritt 1.3: Gemeinsamen Workspace einrichten und Zugriff gewähren

Alle Fabric-Ressourcen, die Sie mit Braze verbinden möchten, müssen in einem gemeinsamen Workspace platziert werden. Wenn Sie bisher nur den Standard-Workspace **Mein Workspace** verwendet haben, erstellen Sie einen neuen gemeinsamen Workspace:

1. Wählen Sie im Navigationsmenü **Workspaces** und dann **+ Neuer Workspace**.
2. Geben Sie einen **Namen** für den Workspace ein und wählen Sie **Übernehmen**.

Nachdem Sie einen gemeinsamen Workspace haben, gewähren Sie dem Dienstprinzipal Zugriff:

1. Wählen Sie den Workspace aus und dann **Zugriff verwalten**.
2. Wählen Sie **+ Personen oder Gruppen hinzufügen**.
3. Suchen Sie nach dem Namen des Dienstprinzipals, den Sie in Schritt 1.1 erstellt haben, und wählen Sie ihn aus. Wenn er nicht angezeigt wird, überprüfen Sie, ob Sie die Einstellung **Dienstprinzipale können Fabric-APIs verwenden** in Schritt 1.2 aktiviert haben.
4. Wählen Sie im Rollen-Dropdown **Mitwirkender** aus.

Der Dienstprinzipal kann nun über die SQL-Endpunkte auf Fabric-Warehouse-Ressourcen in diesem Workspace zugreifen, einschließlich des Warehouse, das Sie für Braze verwenden werden.

#### Schritt 1.4: Tabelle einrichten
Braze unterstützt sowohl Tabellen als auch Ansichten in Fabric Warehouses. Wenn Sie ein neues Warehouse erstellen müssen, erstellen Sie es innerhalb des gemeinsamen Workspace aus Schritt 1.3. Gehen Sie in der Fabric-Konsole zu **Erstellen > Data Warehouse > Warehouse**.

```sql
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
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Sie können das Warehouse, das Schema und die Tabelle oder Ansicht beliebig benennen, aber die Spaltennamen sollten mit der vorangegangenen Definition übereinstimmen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner-Typen enthalten.
    - `EXTERNAL_ID` – Identifiziert die Nutzerin oder den Nutzer, die/den Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Die Braze-Nutzer:innen-Kennung. Diese wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Updates priorisiert.
- `PAYLOAD` – Ein JSON-String mit den Feldern, die Sie mit der Nutzerin oder dem Nutzer in Braze synchronisieren möchten.


#### Schritt 1.5: Warehouse-Verbindungszeichenfolge abrufen
Sie benötigen den SQL-Endpunkt für Ihr Warehouse, damit Braze eine Verbindung herstellen kann. Um diesen abzurufen, gehen Sie zum **Workspace** in Fabric, bewegen Sie in der Liste der Elemente den Mauszeiger über den Warehouse-Namen und wählen Sie **SQL-Verbindungszeichenfolge kopieren**.

![Die Seite „Fabric Console" in Microsoft Azure, auf der Sie die SQL-Verbindungszeichenfolge abrufen.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Schritt 1.6: Braze-IPs in der Firewall zulassen (optional)

Je nach Konfiguration Ihres Microsoft Fabric-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Firewall zulassen, um den Datenverkehr von Braze zuzulassen. Weitere Informationen dazu finden Sie in der entsprechenden Dokumentation zu [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 2. Schritt: Neue Integration im Braze-Dashboard erstellen

{% alert important %}
Kund:innen, die ab Februar 2026 oder später onboarden, haben möglicherweise frühzeitigen Zugriff auf die CDI-Benutzeroberfläche mit separaten Quellen und Synchronisierungen. In dieser Benutzeroberfläche erstellen Sie zuerst eine Quelle, bevor Sie Synchronisierungen für diese Quelle erstellen. Mehrere Synchronisierungen können dieselbe Quelle verwenden.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud Data Ingestion**, wählen Sie **Neue Datensynchronisierung erstellen** und dann **Snowflake-Import**.

#### Schritt 2.1: Snowflake-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Snowflake Data Warehouse und die Quelltabelle ein und fahren Sie dann mit dem nächsten Schritt fort.

{% alert note %}
Geben Sie im Feld **Snowflake-Konto-Locator** Ihren Snowflake-[Kontobezeichner](https://docs.snowflake.com/en/user-guide/admin-account-identifier) ein, der in der Regel einem Format wie `xy12345.us-east-1.aws` entspricht. Dies ist nicht dasselbe wie ein Datenbankname oder Warehouse-Name.
{% endalert %}

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung und geben Sie Kontakt-E-Mail-Adressen ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder synchronisierungsbezogene Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Verbindungsprobleme
- Mangel an Ressourcen
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Der Katalog-Tier hat keinen Platz mehr

Sie wählen außerdem den Datentyp und die Synchronisierungshäufigkeit. Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze-Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind angepasste Attribute, angepasste Events und Kauf-Events. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

#### Public Key zur Braze-Nutzerin oder zum Braze-Nutzer hinzufügen

An dieser Stelle müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den im Dashboard angezeigten Public Key der Nutzerin oder dem Nutzer hinzu, die/den Sie für die Verbindung von Braze mit Snowflake erstellt haben.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt rotieren möchten, können wir ein neues Schlüsselpaar erzeugen und Ihnen den neuen Public Key zur Verfügung stellen.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud Data Ingestion**, wählen Sie **Neue Datensynchronisierung erstellen** und dann **Amazon Redshift-Import**.

#### Schritt 2.1: Redshift-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Redshift Data Warehouse und die Quelltabelle ein. Wenn Sie einen privaten Netzwerktunnel verwenden, aktivieren Sie den Schieberegler und geben Sie die Tunnelinformationen ein. Fahren Sie dann mit dem nächsten Schritt fort. 

{% alert note %}
Im Braze-Dashboard akzeptiert das Feld **Datenbankname** nur Buchstaben (A–Z, a–z), Zahlen (0–9) und Unterstriche (_), obwohl Amazon Redshift zusätzliche Zeichen in Datenbankbezeichnern unterstützt.
{% endalert %}

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung und geben Sie Kontakt-E-Mail-Adressen ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder synchronisierungsbezogene Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Verbindungsprobleme
- Mangel an Ressourcen
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Der Katalog-Tier hat keinen Platz mehr

Sie wählen außerdem den Datentyp und die Synchronisierungshäufigkeit. Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze-Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind angepasste Attribute, angepasste Events und Kauf-Events. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 
{% endtab %}
{% tab BigQuery %}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud Data Ingestion**, wählen Sie **Neue Datensynchronisierung erstellen** und dann **Google BigQuery-Import**.

#### Schritt 2.1: BigQuery-Verbindungsinformationen und Quelltabelle hinzufügen

Laden Sie den JSON-Schlüssel hoch und geben Sie einen Namen für das Dienstkonto an. Geben Sie anschließend die Details Ihrer Quelltabelle ein.

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung und geben Sie Kontakt-E-Mail-Adressen ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder synchronisierungsbezogene Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Verbindungsprobleme
- Mangel an Ressourcen
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Der Katalog-Tier hat keinen Platz mehr

Sie wählen außerdem den Datentyp und die Synchronisierungshäufigkeit. Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze-Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind angepasste Attribute, angepasste Events, Kauf-Events und Nutzer:innen-Löschungen. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

{% endtab %}
{% tab Databricks %}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud Data Ingestion**, wählen Sie **Neue Datensynchronisierung erstellen** und dann **Databricks-Import**.

#### Schritt 2.1: Databricks-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihr Databricks Data Warehouse und die Quelltabelle ein und fahren Sie dann mit dem nächsten Schritt fort.

#### Schritt 2.2: Synchronisierungsdetails konfigurieren

Wählen Sie als Nächstes einen Namen für Ihre Synchronisierung und geben Sie Kontakt-E-Mail-Adressen ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu informieren, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder synchronisierungsbezogene Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Fehler auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Verbindungsprobleme
- Mangel an Ressourcen
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Der Katalog-Tier hat keinen Platz mehr

Sie wählen außerdem den Datentyp und die Synchronisierungshäufigkeit. Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze-Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. Unterstützte Datentypen sind angepasste Attribute, angepasste Events, Kauf-Events und Nutzer:innen-Löschungen. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 2.1: Cloud Data Ingestion-Synchronisierung einrichten

Sie erstellen eine neue Datensynchronisierung für Microsoft Fabric. Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud Data Ingestion**, wählen Sie **Neue Datensynchronisierung erstellen** und dann **Microsoft Fabric-Import**.

#### Schritt 2.2: Microsoft Fabric-Verbindungsinformationen und Quelltabelle hinzufügen

Geben Sie die Informationen für Ihre Microsoft Fabric Warehouse-Zugangsdaten und die Quelltabelle ein und fahren Sie dann mit dem nächsten Schritt fort.

- „Zugangsdaten-Name" ist eine Bezeichnung für diese Zugangsdaten in Braze – Sie können hier einen hilfreichen Wert festlegen.
- Einzelheiten zum Abrufen von Tenant-ID, Principal-ID, Client-Geheimnis und Verbindungszeichenfolge finden Sie in den Schritten in Abschnitt 1.

#### Schritt 2.3: Synchronisierungsdetails konfigurieren

Konfigurieren Sie als Nächstes die folgenden Details für Ihre Synchronisierung: 

- Synchronisierungsname 
- Datentyp – Unterstützte Datentypen sind angepasste Attribute, angepasste Events, Kauf-Events, Kataloge und Nutzer:innen-Löschungen. Der Datentyp für eine Synchronisierung kann nach der Erstellung nicht mehr geändert werden. 
- Synchronisierungshäufigkeit – Die Häufigkeit kann zwischen alle 15 Minuten und einmal pro Monat liegen. Wir verwenden die in Ihrem Braze-Dashboard konfigurierte Zeitzone, um die wiederkehrende Synchronisierung zu planen. 
  - Nicht wiederkehrende Synchronisierungen können manuell oder über die [API]({{site.baseurl}}/api/endpoints/cdi) ausgelöst werden. 

#### Schritt 2.4: Benachrichtigungseinstellungen konfigurieren

Geben Sie als Nächstes Kontakt-E-Mail-Adressen ein. Wir verwenden diese Kontaktinformationen, um Sie über Integrationsfehler zu benachrichtigen, z. B. über die unerwartete Aufhebung des Zugriffs auf die Tabelle, oder um Sie zu warnen, wenn bestimmte Zeilen nicht aktualisiert werden können.

Kontakt-E-Mails erhalten standardmäßig nur Benachrichtigungen über globale oder synchronisierungsbezogene Fehler wie fehlende Tabellen, Berechtigungen und andere. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Verbindungsprobleme
- Mangel an Ressourcen
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Der Katalog-Tier hat keinen Platz mehr

Sie können auch Warnungen für Probleme auf Zeilenebene konfigurieren oder sich bei jeder erfolgreichen Synchronisierung eine Benachrichtigung senden lassen. 

{% endtab %}

{% endtabs %}

### 3. Schritt: Verbindung testen

{% tabs %}
{% tab Snowflake %}

Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.
{% endsubtab %}

{% subtab Private Network %}
Kehren Sie zum Braze-Dashboard zurück und wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.

{% endtab %}

{% tab Databricks %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.

{% endtab %}
{% tab Microsoft Fabric %}

Nachdem Sie alle Konfigurationsdetails für Ihre Synchronisierung eingegeben haben, wählen Sie **Verbindung testen**. Bei Erfolg sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht hergestellt werden kann, wird eine Fehlermeldung angezeigt, die Ihnen bei der Fehlerbehebung hilft.

{% endtab %}
{% endtabs %}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.  
{% endalert %}

## Zusätzliche Integrationen oder Nutzer:innen einrichten (optional)

{% tabs %}
{% tab Snowflake %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Snowflake-Konto verbinden.

Wenn Sie dieselbe Nutzerin oder denselben Nutzer und dieselbe Rolle bei verschiedenen Integrationen wiederverwenden, müssen Sie den Public Key **nicht** erneut hinzufügen.
{% endtab %}
{% tab Redshift %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Snowflake- oder Redshift-Konto verbinden.

Wenn Sie dieselbe Nutzerin oder denselben Nutzer bei verschiedenen Integrationen wiederverwenden, können Sie die Nutzerin oder den Nutzer im Braze-Dashboard erst löschen, wenn sie/er aus allen aktiven Synchronisierungen entfernt wurde.
{% endtab %}
{% tab BigQuery %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben BigQuery-Konto verbinden.

Wenn Sie dieselbe Nutzerin oder denselben Nutzer bei verschiedenen Integrationen wiederverwenden, können Sie die Nutzerin oder den Nutzer im Braze-Dashboard erst löschen, wenn sie/er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Databricks %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Databricks-Konto verbinden.

Wenn Sie dieselbe Nutzerin oder denselben Nutzer bei verschiedenen Integrationen wiederverwenden, können Sie die Nutzerin oder den Nutzer im Braze-Dashboard erst löschen, wenn sie/er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Microsoft Fabric %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass eine andere Tabelle synchronisiert wird. Wenn Sie zusätzliche Synchronisierungen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Fabric-Konto verbinden.

Wenn Sie dieselbe Nutzerin oder denselben Nutzer bei verschiedenen Integrationen wiederverwenden, können Sie die Nutzerin oder den Nutzer im Braze-Dashboard erst löschen, wenn sie/er aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% endtabs %}

## Ausführen der Synchronisierung

{% tabs %}
{% tab Snowflake %}
Nach der Aktivierung wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Zeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Redshift %}
Nach der Aktivierung wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Zeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab BigQuery %}

Nach der Aktivierung wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Zeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Databricks %}

Nach der Aktivierung wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Zeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Microsoft Fabric %}

Nach der Aktivierung wird Ihre Synchronisierung nach dem bei der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Zeitplans durchführen oder die neuesten Daten abrufen möchten, wählen Sie **Jetzt synchronisieren**. Dieser Lauf hat keine Auswirkungen auf regelmäßig geplante zukünftige Synchronisierungen.

{% endtab %}

{% endtabs %}