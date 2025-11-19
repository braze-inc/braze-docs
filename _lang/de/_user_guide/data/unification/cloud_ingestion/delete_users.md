---
nav_title: "Nutzer:innen mit CDI löschen"
article_title: Benutzer mit Cloud Data Ingestion löschen
page_order: 30
page_type: reference
description: "Diese Pgae bietet eine Übersicht über den Prozess zum Löschen von Nutzer:innen mit Cloud Datenaufnahme."

---

# Nutzer:innen mit Cloud-Datenaufnahme löschen

> Auf dieser Seite wird das Verfahren zum Löschen von Nutzer:innen mit Cloud Datenaufnahme beschrieben.

Nutzer:innen-Löschsynchronisationen werden für alle verfügbaren Datenquellen von Cloud Data Ingestion unterstützt. 

## Konfigurieren der Integration 

Folgen Sie dem Standardverfahren zur [Erstellung einer neuen Integration im Braze-Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) für das Data Warehouse, mit dem Sie sich verbinden möchten. Stellen Sie sicher, dass Sie eine Rolle angeben, die Zugriff auf die Löschtabelle hat. Stellen Sie auf der Seite **Import-Synchronisation erstellen** den **Datentyp** auf **Nutzer:innen löschen** ein, damit während des Integrationslaufs die richtigen Aktionen zum Löschen von Nutzer:innen durchgeführt werden.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Konfigurieren der Datenquelle

Die Quelltabellen für die Löschung von Nutzer:innen sollten einen oder mehrere Typen von Bezeichnern und einen `UPDATED_AT`-Zeitstempel enthalten. Payload-Spalten werden für Nutzer:in-Daten nicht unterstützt.

### `UPDATED_AT`

Fügen Sie einen `UPDATED_AT` Zeitstempel zu Ihrer Quelltabelle hinzu. Dieser Zeitstempel gibt die Zeit an, zu der diese Zeile aktualisiert oder der Tabelle hinzugefügt wurde. Braze synchronisiert nur Zeilen, die seit der letzten Synchronisierung hinzugefügt oder aktualisiert wurden.

### Nutzerbezeichner-Spalten

Ihre Tabelle kann eine oder mehrere Spalten mit Benutzerkennungen enthalten. Jede Zeile sollte nur einen Bezeichner enthalten: entweder `external_id`, die Kombination aus `alias_name` und `alias_label` oder `braze_id`. Eine Quelltabelle kann Spalten für einen, zwei oder alle drei Bezeichner-Typen enthalten.
- `EXTERNAL_ID` – Dies ist der Bezeichner des Nutzers oder der Nutzerin, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
- `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
- `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze-SDK generiert und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe ID oder einen Nutzer-Alias an. 

{% alert important %}
Nehmen Sie keine `PAYLOAD` Spalte in Ihre Tabelle auf, um Nutzer:in zu entfernen. Um ein versehentliches, dauerhaftes Entfernen von Benutzern zu verhindern, schlägt eine Synchronisierung fehl, wenn eine Payload-Spalte in der Quelltabelle vorhanden ist. Alle anderen Spalten sind zulässig, werden aber von Braze ignoriert.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```json
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
Erstellen Sie eine Tabelle mit den folgenden Feldern:

| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| ZEITSTEMPEL | PFLICHTANGABE |
| `EXTERNAL_ID`| STRING | LÖSCHBAR |
| `ALIAS_NAME`| STRING | LÖSCHBAR |
| `ALIAS_LABEL`| STRING | LÖSCHBAR |
| `BRAZE_ID`| STRING | LÖSCHBAR |
{% endtab %}

{% tab Databricks %}
Erstellen Sie eine Tabelle mit den folgenden Feldern:

| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| ZEITSTEMPEL | PFLICHTANGABE |
| `EXTERNAL_ID`| STRING | LÖSCHBAR |
| `ALIAS_NAME`| STRING | LÖSCHBAR |
| `ALIAS_LABEL`| STRING | LÖSCHBAR |
| `BRAZE_ID`| STRING | LÖSCHBAR |
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### Funktionsweise

Mit Braze Cloud Data Ingestion richten Sie eine Integration zwischen Ihrer Data Warehouse-Instanz und dem Braze Workspace ein, um Daten auf einer wiederkehrenden Basis zu synchronisieren. Diese Synchronisierung erfolgt nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen anderen Zeitplan haben. Die Synchronisierung kann so häufig wie alle 15 Minuten oder so selten wie einmal im Monat erfolgen. Für Kund:innen, die häufiger als 15 Minuten synchronisiert werden müssen, sprechen Sie mit Ihrem Customer-Success-Manager oder ziehen Sie die Verwendung von REST API-Aufrufen für die Datenaufnahme in Echtzeit in Betracht.

Wenn eine Synchronisierung ausgeführt wird, stellt Braze eine direkte Verbindung zu Ihrer Data Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und löscht die entsprechenden Benutzerprofile auf Ihrem Braze-Dashboard. 

{% alert warning %}
Das Löschen von Benutzerprofilen kann nicht rückgängig gemacht werden. Es entfernt dauerhaft Benutzer, die Unstimmigkeiten in Ihren Daten verursachen könnten. Weitere Informationen finden Sie unter [Löschen eines Benutzerprofils]({{site.baseurl}}/help/help_articles/api/delete_user/).
{% endalert %}

<br><br>