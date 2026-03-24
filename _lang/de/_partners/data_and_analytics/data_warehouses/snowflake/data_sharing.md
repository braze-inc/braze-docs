---
nav_title: "Data Sharing"
article_title: Snowflake Data Sharing
page_order: 0
description: "Dieser Referenzartikel behandelt die Snowflake Secure Data Sharing-Integration, mit der Sie direkt in Ihrer Snowflake-Instanz auf Braze-Engagement- und Kampagnendaten zugreifen können."
page_type: partner
search_tag: Partner

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake Data Sharing

> Snowflake [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) ermöglicht es Braze, Ihnen sicheren Zugriff auf Daten in unserem Snowflake-Portal zu gewähren – ohne Reibungsverluste oder Verzögerungen im Workflow, Fehlerquellen und unnötige Kosten, die bei typischen Datenanbieter-Beziehungen entstehen. Data Sharing kann über die folgende Integration oder über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts) eingerichtet werden.

{% alert tip %}
**Sie möchten auf Snowflake-Daten zugreifen, ohne ein Snowflake-Konto zu benötigen?**<br>Informieren Sie sich über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). Mit Reader Accounts erstellt Braze ein Konto, teilt Ihre Daten darin und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich anmelden und auf Ihre Daten zugreifen können. Dabei werden sämtliche Kosten für Data Sharing und Nutzung vollständig von Braze übernommen.
{% endalert %}

## Über Secure Data Sharing

Beim Data Sharing werden keine tatsächlichen Daten zwischen Konten kopiert oder übertragen. Das gesamte Sharing erfolgt über Snowflakes einzigartige Service-Schicht und den Metadaten-Store. Dies ist ein wichtiges Konzept, da geteilte Daten keinen Speicherplatz in Ihrem Konto belegen und somit nicht zu Ihren monatlichen Datenspeicherkosten beitragen. Die **einzigen** Kosten entstehen durch die Rechenressourcen (z. B. virtuelle Warehouses), die zum Abfragen der geteilten Daten verwendet werden.

Darüber hinaus kann der Zugriff auf von Braze geteilte Daten mithilfe der integrierten Rollen- und Berechtigungsfunktionen von Snowflake über die bereits vorhandenen Zugriffskontrollen Ihres Snowflake-Kontos gesteuert und verwaltet werden. Der Zugriff kann auf die gleiche Weise eingeschränkt und überwacht werden wie bei Ihren eigenen Daten.

- **Verkürzen Sie die Zeit bis zu Insights**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Dank der einzigartigen Architekturen von Braze und Snowflake sind alle Customer-Engagement- und Kampagnendaten sofort zugänglich und abfragbar, sobald sie im Data Lake eintreffen. Es werden keine Daten kopiert oder verschoben, sodass Sie Kundenerlebnisse auf Basis der relevantesten und aktuellsten Informationen bereitstellen können.
- **Beseitigen Sie Datensilos**<br>Erstellen Sie eine ganzheitliche Sicht auf Ihre Kund:innen über alle Kanäle und Plattformen hinweg. Data Sharing macht es einfacher denn je, Ihre Braze-Customer-Engagement-Daten mit all Ihren anderen Snowflake-Daten zu verknüpfen – für umfassendere Insights aus einer einzigen, zuverlässigen Datenquelle.
- **Vergleichen Sie Ihr Engagement**<br>Optimieren Sie Ihre Customer-Engagement-Strategien mit Braze Benchmarks. Dieses interaktive Tool, betrieben von Braze und Snowflake, ermöglicht es Ihnen, die Engagement-Daten Ihrer Marke mit Benchmarks über Kanäle, Branchen und Geräteplattformen hinweg zu vergleichen.

Weitere Informationen zum Data Sharing von Snowflake finden Sie unter [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Kontaktieren Sie Ihren Braze-Konto- oder Customer-Success-Manager, um Data Sharing einzurichten. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Secure Data Sharing einrichten

Bei Snowflake erfolgt Data Sharing zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenkonsumenten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und sendet – während Ihr Snowflake-Konto der Datenkonsument ist, da es den Datashare nutzt, um eine Datenbank zu erstellen. Weitere Details finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### 1. Schritt: Datashare von Braze senden

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Data Sharing**.
2. Geben Sie Ihre Snowflake-Kontodetails und den Locator ein. Um Ihren Account-Locator zu erhalten, führen Sie `SELECT CURRENT_ACCOUNT()` im Zielkonto aus.
3. Wenn Sie einen CRR-Share verwenden, geben Sie den Cloud-Anbieter und die Region an.
4. Wenn Sie fertig sind, wählen Sie **Create Datashare**. Dadurch wird der Datashare an Ihr Snowflake-Konto gesendet.

### 2. Schritt: Datenbank in Snowflake erstellen

1. Nach einigen Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashares eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Vergeben Sie Berechtigungen zum Abfragen der neuen Datenbank.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank löschen und mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abfragen zu können.
Wenn Sie mehrere Workspaces haben, die Daten an dasselbe Snowflake-Konto teilen, lesen Sie die [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) für Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung

Nachdem der Data Share bereitgestellt wurde, erstellen Sie eine Datenbank aus dem eingehenden Data Share. Dadurch erscheinen alle geteilten Tabellen in Ihrer Snowflake-Instanz und können wie alle anderen in Ihrer Instanz gespeicherten Daten abgefragt werden. Beachten Sie jedoch, dass die geteilten Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Ihr Snowflake Secure Data Sharing nutzen, um:

- Komplexe Berichte zu erstellen
- Attribution-Modellierung durchzuführen
- Sicheres Sharing innerhalb Ihres eigenen Unternehmens zu ermöglichen
- Rohe Event- oder Nutzerdaten einem CRM (wie Salesforce) zuzuordnen
- Und vieles mehr

[Laden Sie hier die Rohtabellen-Schemas herunter.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Nutzer-ID-Schema

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von den Kund:innen festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wichtige Informationen und Einschränkungen

### Abwärtskompatible versus nicht abwärtskompatible Änderungen

#### Abwärtskompatible Änderungen (Non-breaking)

Abwärtskompatible Änderungen können jederzeit auftreten und bieten in der Regel zusätzliche Funktionalität. Beispiele für abwärtskompatible Änderungen:
- Hinzufügen einer neuen Tabelle oder View
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder View

{% alert important %}
Da neue Spalten als abwärtskompatible Änderungen gelten, empfiehlt Braze dringend, in jeder Abfrage die gewünschten Spalten explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Views erstellen, die Spalten explizit benennen, und dann diese Views anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Nicht abwärtskompatible Änderungen (Breaking)

Wenn möglich, werden nicht abwärtskompatible Änderungen durch eine Ankündigung und eine Migrationsphase eingeleitet. Beispiele für nicht abwärtskompatible Änderungen:
- Entfernen einer Tabelle oder View
- Entfernen einer Spalte aus einer bestehenden Tabelle oder View
- Ändern des Typs oder der Nullbarkeit einer bestehenden Spalte

### Snowflake-Regionen

Braze hostet derzeit alle Daten auf Nutzerebene in diesen Snowflake-AWS-Regionen:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)
 
Für Nutzer:innen außerhalb dieser Regionen kann Braze Data Sharing für gemeinsame Kund:innen bereitstellen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region betreiben.

### Datenaufbewahrung

#### Aufbewahrungsrichtlinie

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Events anonymisiert und alle personenbezogenen (PII) sensiblen Felder entfernt (dies umfasst auch optional PII-Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das nutzerbasierte Analytics über alle Event-Daten hinweg ermöglicht.

Sie können die aktuellsten zwei Jahre an Daten für jedes Event in der entsprechenden `USERS_*_SHARED`-View abfragen. Zusätzlich verfügt jedes Event über eine `USERS_*_SHARED_ALL`-View, die sowohl anonymisierte als auch nicht anonymisierte Daten zurückgibt.

#### Historische Daten

Das Archiv historischer Event-Daten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten leicht anders aussehen oder Nullwerte aufweisen (da zu diesem Zeitpunkt nicht alle verfügbaren Felder befüllt wurden). Es ist davon auszugehen, dass Ergebnisse, die Daten vor August 2019 enthalten, leicht von den Erwartungen abweichen können.

### Konformität mit der Datenschutz-Grundverordnung (DSGVO)

{% include partners/snowflake_pii_gdpr.md %}

### Geschwindigkeit, Performance und Kosten von Abfragen

Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie zum Abfragen der Daten verwenden. In einigen Fällen kann es je nach Datenmenge, auf die Sie für Analytics zugreifen, erforderlich sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ist. Snowflake bietet hervorragende Ressourcen zur Bestimmung der optimalen Größe, darunter [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Für eine Sammlung von Beispielabfragen, die Sie beim Einrichten von Snowflake als Referenz nutzen können, sehen Sie sich unsere [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/) und [ETL-Event-Pipeline-Einrichtung]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/) an.
{% endalert %}