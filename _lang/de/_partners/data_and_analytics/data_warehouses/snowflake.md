---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Snowflake und behandelt sowohl Data Sharing (Braze zu Snowflake) als auch Cloud-Datenaufnahme (Snowflake zu Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) ist ein speziell entwickeltes SQL Data Warehouse in der Cloud, das als Software-as-a-Service (SaaS) angeboten wird. Snowflake bietet ein Data Warehouse, das schneller, benutzerfreundlicher und wesentlich flexibler ist als herkömmliche Data-Warehouse-Angebote. Mit der einzigartigen und patentierten Architektur von Snowflake ist es ein Leichtes, all Ihre Daten zu sammeln, schnelle Analytics zu ermöglichen und datengestützte Insights für alle Ihre Nutzer:innen zu gewinnen.

Braze bietet zwei Integrationen mit Snowflake an. Zusammen ermöglichen sie eine vollständige, bidirektionale Datenpipeline zwischen Ihren Braze- und Snowflake-Umgebungen.

## Eine Integration auswählen

### Data Sharing (Braze zu Snowflake)

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) bietet Ihnen sicheren Realtime-Zugriff auf Braze-Engagement- und Kampagnendaten direkt in Ihrer Snowflake-Instanz. Es werden keine Daten zwischen Konten kopiert oder übertragen – die gesamte Freigabe erfolgt über die einzigartige Dienstebene und den Metadaten-Store von Snowflake.

**Verwenden Sie Data Sharing, wenn Sie Folgendes möchten:**
- Braze-Ereignis- und Kampagnendaten mit Snowflake SQL abfragen
- Komplexe Berichte erstellen und Attributionsmodellierung durchführen
- Braze-Daten mit anderen Daten in Ihrem Snowflake Data Warehouse verknüpfen
- Ihre Engagement-Daten über Kanäle, Branchen und Geräteplattformen hinweg vergleichen

Einrichtungsanweisungen finden Sie unter [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Cloud-Datenaufnahme (Snowflake zu Braze)

[Cloud-Datenaufnahme (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) ermöglicht es Ihnen, Daten aus Ihrer Snowflake-Instanz direkt mit Braze zu synchronisieren. So können Sie Nutzerattribute, Ereignisse und Käufe in Braze mit Ihrem Data Warehouse als Single Source of Truth auf dem neuesten Stand halten.

**Verwenden Sie die Cloud-Datenaufnahme, wenn Sie Folgendes möchten:**
- Nutzerattribute von Snowflake mit Braze-Nutzerprofilen synchronisieren
- Ereignis- oder Kaufdaten von Snowflake an Braze senden
- Braze mit Datentransformationen synchron halten, die in Ihrem Data Warehouse stattfinden
- Den Aufbau und die Wartung angepasster ETL-Pipelines von Snowflake zu Braze vermeiden

Mehr über Data Sharing bei Snowflake erfahren Sie unter [Einführung in Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen

Bevor Sie dieses Feature nutzen können, müssen Sie Folgendes abschließen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Um auf dieses Feature in Braze zuzugreifen, wenden Sie sich an Ihren Braze-Konto-Manager oder Customer-Success-Manager. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Secure Data Sharing einrichten

Bei Snowflake findet Data Sharing zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenverbraucher](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) statt. In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und versendet&#8212;während Ihr Snowflake-Konto der Datenverbraucher ist, da es den Datashare verwendet, um eine Datenbank zu erstellen. Weitere Einzelheiten finden Sie unter [Snowflake: Gemeinsame Daten nutzen](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### 1. Schritt: Senden Sie den Datashare von Braze

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Data Sharing**.
2. Geben Sie Ihre Snowflake-Kontodaten und Ihren Locator ein. Um Ihren Account-Locator zu ermitteln, führen Sie `SELECT CURRENT_ACCOUNT()` im Zielkonto aus.
3. Wenn Sie einen CRR-Share verwenden, geben Sie den Cloud-Anbieter und die Region an.
4. Wenn Sie fertig sind, wählen Sie **Datashare erstellen**. Dadurch wird der Datashare an Ihr Snowflake-Konto gesendet.

### 2. Schritt: Erstellen Sie die Datenbank in Snowflake

1. Nach ein paar Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashare eine Datenbank zum Anzeigen und Abfragen der Tabellen. Zum Beispiel:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Gewähren Sie die Berechtigungen zur Abfrage der neuen Datenbank.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank löschen und sie mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abzufragen.
Wenn Sie mehrere Workspaces haben, die Daten für dasselbe Snowflake-Konto freigeben, finden Sie in den [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) Hinweise zur Verwaltung von Konfigurationen mit mehreren Workspaces.
{% endalert %}

## Verwendung und Visualisierung

Nachdem der Data Share bereitgestellt wurde, müssen Sie aus dem eingehenden Data Share eine Datenbank erstellen, damit alle freigegebenen Tabellen in Ihrer Snowflake-Instanz erscheinen und wie alle anderen Daten, die Sie in Ihrer Instanz speichern, abgefragt werden können. Beachten Sie jedoch, dass die gemeinsam genutzten Daten schreibgeschützt sind und nur abgefragt, aber nicht verändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Snowflake Secure Data Sharing verwenden, um:

- Komplexe Berichte zu erstellen
- Attributionsmodellierung durchzuführen
- Sicheren Austausch innerhalb Ihres eigenen Unternehmens zu ermöglichen
- Rohe Ereignis- oder Nutzerdaten in einem CRM (wie Salesforce) abzubilden
- Und mehr

Eine vollständige Liste der verfügbaren Tabellen und Spalten finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Snowflake Data Sharing umfasst alle Tabellen in dieser Referenz sowie zusätzliche Snowflake-exklusive Tabellen für Snapshots, Kampagnen- und Canvas-Changelogs, Agent-Console-Ereignisse und Nachrichtenwiederholungsereignisse.

Sie können auch [die Rohtabellenschemata herunterladen]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) (als Textdatei).

### Nutzer-ID-Schema

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kundschaft festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wichtige Informationen und Einschränkungen

### Unterbrechende versus nicht-unterbrechende Änderungen

#### Nicht-unterbrechende Änderungen

Nicht-unterbrechende Änderungen können jederzeit vorgenommen werden und bieten im Allgemeinen zusätzliche Funktionalität. Beispiele für nicht-unterbrechende Änderungen:
- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als nicht-unterbrechend gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Ansichten erstellen, die Spalten explizit benennen, und dann diese Ansichten anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Unterbrechende Änderungen

Wenn möglich, werden unterbrechende Änderungen mit einer Ankündigung und einem Migrationszeitraum eingeleitet. Beispiele für unterbrechende Änderungen:
- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer vorhandenen Spalte

### Snowflake-Regionen

Braze hostet derzeit alle Nutzerdaten in den Snowflake-AWS-Regionen US East-1, EU-Central (Frankfurt), AP-Southeast-2 (Sydney) und AP-Southeast-3 (Jakarta). Für Nutzer:innen außerhalb dieser Regionen kann Braze Data Sharing für gemeinsame Kund:innen bereitstellen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region hosten.

### Datenaufbewahrung

#### Aufbewahrungsrichtlinie

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in einen Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Ereignisse anonymisiert und alle sensiblen Felder mit personenbezogenen Daten (PII) entfernt (dies schließt optional PII-Felder wie `properties` ein). Die archivierten Daten enthalten weiterhin das Feld `user_id`, das Analytics pro Nutzer:in über alle Ereignisdaten hinweg ermöglicht.

Sie können die Daten der letzten zwei Jahre für jedes Ereignis in der entsprechenden Ansicht `USERS_*_SHARED` abfragen. Zusätzlich gibt es für jedes Ereignis eine Ansicht `USERS_*_SHARED_ALL`, die sowohl anonymisierte als auch nicht-anonymisierte Daten liefert.

#### Historische Daten

Das Archiv der historischen Ereignisdaten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake speicherte, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten etwas anders aussehen oder Nullwerte enthalten (da zu diesem Zeitpunkt nicht in jedes verfügbare Feld Daten übertragen wurden). Am besten gehen Sie davon aus, dass alle Ergebnisse, die Daten vor August 2019 enthalten, etwas anders aussehen können als erwartet.

### Einhaltung der Datenschutz-Grundverordnung (DSGVO)

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Geschwindigkeit, Performance und Kosten der Abfragen

Die Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, hängen von der Warehouse-Größe ab, die Sie zur Abfrage der Daten verwenden. Je nachdem, auf wie viele Daten Sie für Analytics zugreifen, kann es vorkommen, dass Sie eine größere Warehouse-Größe verwenden müssen, damit die Abfrage erfolgreich ist. Snowflake verfügt über ausgezeichnete Ressourcen zur Bestimmung der richtigen Größe, darunter [Übersicht über Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Überlegungen zu Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Eine Reihe von Beispielabfragen, auf die Sie bei der Einrichtung von Snowflake zurückgreifen können, finden Sie in unseren [Beispielabfragen]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) und Beispielen für die [Einrichtung der ETL-Ereignis-Pipeline]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

Einrichtungsanweisungen finden Sie unter [Cloud-Datenaufnahme: Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).