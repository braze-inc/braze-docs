---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Snowflake, einem speziell entwickelten SQL Data Warehouse in der Cloud für alle Ihre Daten und Nutzer:innen."
page_type: partner
search_tag: Partner

---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) ist ein speziell entwickeltes SQL Data Warehouse in der Cloud, das als Software-as-a-Service (SaaS) angeboten wird. Snowflake bietet ein Data Warehouse, das schneller, benutzerfreundlicher und wesentlich flexibler ist als herkömmliche Data Warehouse-Angebote. Mit der eindeutigen und patentierten Architektur von Snowflake ist es ein Leichtes, all Ihre Daten zu sammeln, schnelle Analytics zu ermöglichen und datengestützte Insights für alle Ihre Nutzer:innen zu gewinnen.

Personalisierte und relevante Kampagnen erfordern einen sofortigen Zugriff auf Daten. Deshalb hat sich Braze mit Snowflake zusammengetan, um die gemeinsame Nutzung von Daten zu ermöglichen. Dieses gemeinsame Angebot ermöglicht es Marketern, das Potenzial ihrer Customer-Engagement- und Kampagnendaten schneller als je zuvor zu erschließen.

Die [Integration von Braze und Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) nutzt den Datenaustausch von Snowflake, um eine Präsenz aufzubauen, neue Kunden zu finden und die Reichweite durch den ständig wachsenden Snowflake-Kundenstamm zu erweitern.

{% alert tip %}
**Sind Sie daran interessiert, auf Daten auf Snowflake-Ebene zuzugreifen, ohne dass Sie ein Snowflake-Konto benötigen?**<br>Sehen Sie sich die [Snowflake Leserkonten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts) an. Mit den Reader-Konten erstellt Braze ein Konto und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich anmelden und auf Ihre Daten zugreifen können. Dies führt dazu, dass die gemeinsame Nutzung von Daten und die Abrechnung der Nutzung vollständig von Braze übernommen wird.
{% endalert %}

## Was ist Data Sharing?

Die Snowflake-Funktionalität für [die sichere gemeinsame Nutzung von Daten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) erlaubt es Braze, Ihnen einen sicheren Zugriff auf die Daten in unserem Snowflake-Portal zu ermöglichen, ohne dass Sie sich Gedanken über Reibungen oder Verlangsamungen im Workflow, über Fehlerpunkte und unnötige Kosten machen müssen, die mit typischen Beziehungen zu Datenanbietern verbunden sind. Die gemeinsame Nutzung von Daten kann über die folgende Integration oder über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts) eingerichtet werden.

- **Reduzieren Sie die Zeit bis zu Insights**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Die eindeutigen Architekturen von Braze und Snowflake machen alle Daten zum Customer-Engagement und zu Kampagnen sofort zugänglich und abfragbar, sobald sie im Data Lake ankommen. Es werden keine Daten kopiert oder verschoben, so dass Sie Kundenerlebnisse nur auf der Grundlage der relevantesten und aktuellsten Informationen zustellen können.
- **Keine Datensilos mehr**<br>Schaffen Sie eine ganzheitliche Sicht auf Ihre Kund:innen über alle Kanäle und Plattformen hinweg. Durch die gemeinsame Nutzung von Daten ist es einfacher als je zuvor, Ihre Braze Customer-Engagement-Daten mit all Ihren anderen Snowflake-Daten zu verbinden. So erhalten Sie umfassendere Insights aus einer einzigen, zuverlässigen Quelle der Wahrheit.
- **Sehen Sie, wie Ihr Engagement im Vergleich abschneidet**<br>Optimieren Sie Ihre Customer-Engagement-Strategien mit Braze Benchmarks. Dieses interaktive Tool, das von Braze und Snowflake unterstützt wird, lässt Sie die Daten zum Engagement Ihrer Marke mit Benchmarks über Kanäle, Branchen und Geräteplattformen hinweg vergleichen.

Bei der gemeinsamen Nutzung von Daten werden keine tatsächlichen Daten zwischen Konten kopiert oder übertragen. Die gemeinsame Nutzung erfolgt über die eindeutige Ebene der Dienste und den Shop für Metadaten von Snowflake. Dies ist ein wichtiges Konzept, da gemeinsam genutzte Daten keinen Speicherplatz in einem Verbraucherkonto beanspruchen und daher nicht zu den monatlichen Gebühren für die Datenspeicherung des Verbrauchers beitragen. Den Verbrauchern:in entstehen **lediglich** Kosten für die Computer-Ressourcen (z.B. virtuelle Warehouses), die zur Abfrage der gemeinsam genutzten Daten verwendet werden.

Darüber hinaus kann der Zugriff auf die von Braze freigegebenen Daten mithilfe der in Snowflake integrierten Rollen- und Berechtigungsfunktionen kontrolliert und geregelt werden, und zwar mit den Zugriffskontrollen, die bereits für Ihr Snowflake-Konto und die darin enthaltenen Daten eingerichtet wurden. Der Zugriff kann genauso eingeschränkt und überwacht werden wie bei Ihren eigenen Daten.

Um mehr über die gemeinsame Nutzung von Daten durch Snowflake zu erfahren, lesen Sie [Einführung in die sichere gemeinsame Nutzung von Daten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen

Bevor Sie dieses Feature nutzen können, müssen Sie die folgenden Schritte ausführen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze Zugang | Um auf dieses Feature in Braze zuzugreifen, müssen Sie sich an Ihren Braze-Konto oder Customer-Success-Manager:in wenden. |
| Snowflake Konto | Ein Snowflake-Konto mit `admin` Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Sicheren Datenaustausch einrichten

Bei Snowflake findet die gemeinsame Nutzung von Daten zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Verbraucher](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers):in statt. In diesem Zusammenhang ist Ihr Braze-Konto der Datenanbieter, da es die Datenfreigabe erstellt und versendet, während Ihr Snowflake-Konto der Verbraucher:in ist, da es die Datenfreigabe verwendet, um eine Datenbank zu erstellen. Weitere Einzelheiten finden Sie unter [Snowflake: Gemeinsame Daten verbrauchen](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Senden Sie die Datenfreigabe von Braze

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenfreigabe**.
2. Geben Sie Ihre Snowflake Kontodaten und Ihren Standort ein. Um den Standort Ihres Kontos zu ermitteln, führen Sie `SELECT CURRENT_ACCOUNT()` im Zielkonto aus.
3. Wenn Sie eine CRR-Freigabe verwenden, geben Sie den Cloud-Anbieter und die Region an.
4. Wenn Sie fertig sind, wählen Sie **Datashare erstellen**. Dadurch wird die Datenfreigabe an Ihr Snowflake-Konto gesendet.

### Schritt 2: Erstellen Sie die Datenbank in Snowflake

1. Nach ein paar Minuten sollten Sie die eingehende Datenfreigabe in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mit Hilfe der eingehenden Datenfreigabe eine Datenbank zum Anzeigen und Abfragen der Tabellen. Zum Beispiel:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Gewähren Sie die Berechtigung zur Abfrage der neuen Datenbank.

{% alert warning %}
Wenn Sie eine Freigabe im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank löschen und sie mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um die eingehende Freigabe abzufragen.
{% endalert %}

## Verwendung und Visualisierung

Nachdem die Datenfreigabe bereitgestellt wurde, müssen Sie aus der eingehenden Datenfreigabe eine Datenbank erstellen, damit alle freigegebenen Tabellen in Ihrer Snowflake Instanz erscheinen und wie alle anderen Daten, die Sie in Ihrer Instanz speichern, abgefragt werden können. Beachten Sie jedoch, dass die gemeinsam genutzten Daten schreibgeschützt sind und nur abgefragt, aber nicht verändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Ihre Snowflake Secure Data Sharing verwenden, um:

- Komplexe Berichte erstellen
- Attributionsmodellierung durchführen
- Sicherer Austausch innerhalb Ihres eigenen Unternehmens
- Abbildung roher Ereignis- oder Nutzerdaten in einem CRM (wie Salesforce)
- Und mehr

[Laden Sie die rohen Tabellenschemata hier herunter.]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})

### Schema der Nutzer:innen ID

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer:innen.

| Braze Schema | Snowflake Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner des Profils eines Nutzers:in, der vom Kunden festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wichtige Informationen und Einschränkungen

### Durchbrechende versus nicht-durchbrechende Änderungen

#### Unwesentliche Änderungen

Nicht-unterbrechende Änderungen können jederzeit vorgenommen werden und bieten im Allgemeinen zusätzliche Funktionen. Beispiele für nicht-brechende Änderungen:
- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als nicht umbrechend gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *` Abfragen zu verwenden. Alternativ können Sie auch Ansichten erstellen, die Spalten explizit benennen, und dann diese Ansichten anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Wesentliche Änderungen

Wenn es möglich ist, werden Änderungen mit einer Ankündigung und einem Zeitraum für die Migration eingeleitet. Beispiele für bahnbrechende Änderungen sind:
- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer vorhandenen Spalte

### Snowflake Regionen

Braze hostet derzeit alle Nutzer:innen-Daten in den Snowflake AWS Regionen US East-1 und EU-Central (Frankfurt). Für Nutzer:innen außerhalb dieser Regionen kann Braze Daten für gemeinsame Kunden bereitstellen, die ihre Snowflake Infrastruktur in einer beliebigen AWS, Azure oder GCP Region hosten.

### Datenaufbewahrung

#### Richtlinie zur Bindung

Alle Daten, die älter als zwei Jahre sind, werden archiviert und auf einen Langzeitspeicher übertragen. Als Teil des Archivierungsprozesses werden alle Ereignisse anonymisiert und alle sensiblen Felder mit personenbezogenen Daten (PII) werden entfernt (dies schließt optional PII-Felder wie `properties` ein). Die archivierten Daten enthalten immer noch das Feld `user_id`, das Analytics pro Nutzer:in für alle Ereignisdaten zulässig macht.

Sie können die Daten der letzten zwei Jahre für jedes Ereignis in der entsprechenden Ansicht `USERS_*_SHARED` abfragen. Außerdem gibt es für jedes Ereignis eine Ansicht `USERS_*_SHARED_ALL`, die sowohl anonymisierte als auch nicht-anonymisierte Daten liefert.

#### Historische Daten

Das Archiv der historischen Ereignisdaten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake speicherte, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten etwas anders aussahen oder einige Nullwerte enthielten (da wir zu diesem Zeitpunkt nicht in jedes verfügbare Feld Daten übertragen haben). Am besten gehen Sie davon aus, dass alle Ergebnisse, die Daten vor August 2019 enthalten, etwas anders aussehen können als erwartet.

### Einhaltung der allgemeinen Datenschutzverordnung (DSGVO)

Nahezu jeder Ereignisdatensatz, den Braze speichert, enthält einige Felder, die Nutzer:innen persönlich identifizierbare Informationen (PII) liefern. Einige Ereignisse können E-Mail Adresse, Telefonnummer, ID des Geräts, Sprache, Geschlecht und Standortinformationen enthalten. Wenn die Anfrage eines Nutzers auf Vergessenwerden an Braze übermittelt wird, löschen wir diese PII-Felder für alle Ereignisse, die diesen Nutzer:innen gehören. Auf diese Weise wird die historische Aufzeichnung des Ereignisses nicht gelöscht, aber das Ereignis kann nun nicht mehr mit einer bestimmten Person in Verbindung gebracht werden.

### Geschwindigkeit, Performance, Kosten der Abfragen

Die Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, hängen von der Größe des Data Warehouse ab, das Sie zur Abfrage der Daten verwenden. Je nachdem, auf wie viele Daten Sie für Analytics zugreifen, kann es vorkommen, dass Sie ein größeres Data Warehouse verwenden müssen, damit die Abfrage erfolgreich ist. Snowflake verfügt über ausgezeichnete Ressourcen zur Bestimmung der richtigen Größe, darunter [Übersicht über Lagerhäuser](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Überlegungen zum Lagerhaus](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Eine Reihe von Beispielabfragen, auf die Sie bei der Einrichtung von Snowflake referenzieren können, finden Sie in unseren [Beispielabfragen]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) und Beispielen [für die Einrichtung der ETL-Ereignis-Pipeline]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

