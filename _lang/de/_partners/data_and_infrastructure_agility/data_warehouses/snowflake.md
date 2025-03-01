---
nav_title: Schneeflocke
article_title: Schneeflocke
alias: /partners/snowflake/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Snowflake, einem speziell entwickelten SQL-Cloud-Datawarehouse für alle Ihre Daten und Benutzer."
page_type: partner
search_tag: Partner

---

# [![Braze Learning Kurs]](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Schneeflocke

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) ist ein speziell entwickeltes SQL Cloud Data Warehouse, das als Software-as-a-Service (SaaS) angeboten wird. Snowflake bietet ein Data Warehouse, das schneller, benutzerfreundlicher und wesentlich flexibler ist als herkömmliche Data Warehouse-Angebote. Mit der einzigartigen und patentierten Architektur von Snowflake ist es ein Leichtes, alle Ihre Daten zu sammeln, schnelle Analysen zu ermöglichen und datengestützte Erkenntnisse für alle Ihre Benutzer zu gewinnen.

Personalisierte und relevante Marketingkampagnen erfordern einen sofortigen Zugriff auf Daten. Deshalb hat sich Braze mit Snowflake zusammengetan, um die gemeinsame Nutzung von Daten zu ermöglichen. Dieses gemeinsame Angebot ermöglicht es Marketingfachleuten, das Potenzial ihrer Kundenbindungs- und Kampagnendaten schneller als je zuvor zu erschließen.

Die [Integration von Braze und Snowflake](https://www.braze.com/perspectives/article/snowflake-partner-announcement) nutzt den Datenaustausch von Snowflake, um eine Präsenz aufzubauen, neue Kunden zu finden und die Reichweite durch die ständig wachsende Kundenbasis von Snowflake zu vergrößern.

{% alert tip %}
**Sind Sie an einem Zugriff auf Daten auf Snowflake-Ebene interessiert, ohne dass Sie ein Snowflake-Konto benötigen?**<br>Sehen Sie sich die [Snowflake Leserkonten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts) an. Mit den Lesekonten erstellt Braze ein Konto für Sie und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich einloggen und auf Ihre Daten zugreifen können. Dies führt dazu, dass die gemeinsame Nutzung von Daten und die Abrechnung der Nutzung vollständig von Braze übernommen wird.
{% endalert %}

## Was ist Data Sharing?

Mit der Snowflake-Funktion für [die sichere gemeinsame Nutzung von Daten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) kann Braze Ihnen einen sicheren Zugriff auf die Daten in unserem Snowflake-Portal bieten, ohne dass Sie sich Gedanken über Reibungsverluste oder Verlangsamung des Arbeitsablaufs, Fehlerquellen und unnötige Kosten machen müssen, die mit typischen Beziehungen zu Datenanbietern verbunden sind. Die gemeinsame Nutzung von Daten kann über die folgende Integration oder über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts) eingerichtet werden.

- **Reduzieren Sie die Zeit bis zur Erkenntnis**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Dank der einzigartigen Architekturen von Braze und Snowflake sind alle Kundenbindungs- und Kampagnendaten sofort zugänglich und abfragbar, sobald sie im Data Lake ankommen. Es werden keine Daten kopiert oder verschoben, so dass Sie Kundenerlebnisse nur auf der Grundlage der relevantesten und aktuellsten Informationen bieten können.
- **Datensilos aufbrechen**<br>Schaffen Sie eine ganzheitliche Sicht auf Ihre Kunden über alle Kanäle und Plattformen hinweg. Die gemeinsame Nutzung von Daten macht es einfacher als je zuvor, Ihre Braze-Kundenbindungsdaten mit all Ihren anderen Snowflake-Daten zu verknüpfen. So erhalten Sie umfassendere Einblicke über eine einzige, zuverlässige Quelle der Wahrheit.
- **Sehen Sie, wie es um Ihr Engagement bestellt ist**<br>Optimieren Sie Ihre Strategien zur Kundenbindung mit Braze Benchmarks. Mit diesem interaktiven Tool, das von Braze und Snowflake unterstützt wird, können Sie die Engagement-Daten Ihrer Marke mit Benchmarks für verschiedene Kanäle, Branchen und Geräteplattformen vergleichen.

Bei der gemeinsamen Nutzung von Daten werden keine tatsächlichen Daten zwischen Konten kopiert oder übertragen. Die gesamte gemeinsame Nutzung erfolgt über die einzigartige Dienste-Ebene und den Metadatenspeicher von Snowflake. Dies ist ein wichtiges Konzept, da die gemeinsam genutzten Daten keinen Speicherplatz in einem Verbraucherkonto beanspruchen und daher nicht zu den monatlichen Gebühren für den Datenspeicher des Verbrauchers beitragen. Die **einzigen** Kosten, die den Verbrauchern entstehen, sind die für die Abfrage der gemeinsam genutzten Daten verwendeten Rechenressourcen (z. B. virtuelle Lager).

Darüber hinaus kann der Zugriff auf die von Braze freigegebenen Daten mithilfe der in Snowflake integrierten Rollen und Berechtigungen kontrolliert und geregelt werden, wobei die Zugriffskontrollen für Ihr Snowflake-Konto und die darin enthaltenen Daten bereits vorhanden sind. Der Zugriff kann auf die gleiche Weise wie Ihre eigenen Daten eingeschränkt und überwacht werden.

Lesen Sie [Einführung in die sichere Datenfreigabe](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work), um mehr darüber zu erfahren, wie die Datenfreigabe von Snowflake funktioniert.

## Voraussetzungen

Wenn Sie an dieser Integration interessiert sind, wenden Sie sich an Ihren Braze Account- oder Customer Success Manager und bitten Sie ihn, die Braze Datenstrategie-Services für die sichere gemeinsame Nutzung von Daten mit Snowflake zu konsultieren. So kommen die Rädchen in Braze in Gang, und wir werden Ihre Ansichten im Handumdrehen einrichten!

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Schneeflocken-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Snowflake-Konto mit Admin-Rechten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Secure Data Sharing mit Ihrem Braze-Konto einzurichten, folgen Sie diesen Schritten.

1. Navigieren Sie im Braze Dashboard zu **Partner-Integrationen** > **Data Sharing**.
2. Geben Sie Ihre Snowflake-Kontodaten ein. Sie können Ihre Snowflake-Konto-ID finden, indem Sie `SELECT CURRENT_ACCOUNT()` im Zielkonto ausführen.
3. Wenn Sie eine CRR-Freigabe verwenden, geben Sie den Cloud-Anbieter und die Region an.
4. Wählen Sie **Datashare erstellen**.

Innerhalb weniger Augenblicke sollte Ihre Datenfreigabe in Ihrer Snowflake-Instanz sichtbar sein. Erstellen Sie eine Datenbank aus der Freigabe, damit Sie die Tabellen sehen und abfragen können. Beachten Sie, dass Sie ein Konto-Administrator sein müssen, um die Datenfreigabe zu sehen.

![Eingehende Datenfreigabe]({% image_buster /assets/img/inbound-data-share.png %})

Im Zusammenhang mit der gemeinsamen Nutzung von Daten ist Braze ein [Datenanbieter, d.h. ein](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)Snowflake-Konto, das Freigaben erstellt und sie anderen Snowflake-Konten zur Nutzung zur Verfügung stellt. Sie sind ein [Datenkonsument, d.h. ein](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)Konto, das eine Datenbank aus einer von einem Datenanbieter zur Verfügung gestellten Aktie erstellen möchte.

## Verwendung und Visualisierung

Sobald die Datenfreigabe eingerichtet ist, müssen Sie aus der eingehenden Datenfreigabe eine Datenbank erstellen, so dass alle freigegebenen Tabellen in Ihrer Snowflake-Instanz erscheinen und genauso wie alle anderen Daten, die Sie in Ihrer Instanz speichern, abgefragt werden können. Beachten Sie jedoch, dass die gemeinsam genutzten Daten schreibgeschützt sind und nur abgefragt, aber nicht verändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Ihre Snowflake Secure Data Sharing verwenden, um:
- Komplexe Berichte erstellen
- Attributionsmodellierung durchführen
- Sicherer Austausch innerhalb Ihres eigenen Unternehmens
- Zuordnung von Ereignis- oder Benutzerrohdaten zu einem CRM (wie Salesforce)
- Und mehr

[Laden Sie die rohen Tabellenschemata hier herunter.][Schemata]

### Schema der Benutzer-ID

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Benutzer-IDs.

| Braze Schema | Schneeflocken-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der von Braze automatisch zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Die eindeutige Kennung eines Benutzerprofils, die vom Kunden festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wichtige Informationen und Einschränkungen

### Durchbrechende versus nicht-durchbrechende Änderungen

#### Nicht-unterbrechende Änderungen
Nicht-unterbrechende Änderungen können jederzeit vorgenommen werden und bieten im Allgemeinen zusätzliche Funktionen. Beispiele für nicht-brechende Änderungen:
- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als nicht umbrechend betrachtet werden, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *` Abfragen zu verwenden. Alternativ können Sie auch Ansichten erstellen, die Spalten explizit benennen, und dann diese Ansichten anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Wechselnde Änderungen
Wenn es möglich ist, werden grundlegende Änderungen angekündigt und eine Umstellungsphase eingeleitet. Beispiele für bahnbrechende Änderungen sind:
- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer vorhandenen Spalte

### Schneeflocken Regionen
Braze hostet derzeit alle Daten auf Benutzerebene in den Snowflake AWS-Regionen US East-1 und EU-Central (Frankfurt). Für Benutzer außerhalb dieser Regionen kann Braze die gemeinsame Nutzung von Daten für gemeinsame Kunden ermöglichen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region hosten.

### Aufbewahrung von Daten

#### Aufbewahrungspolitik
Alle Daten, die älter als zwei Jahre sind, werden archiviert und auf einen Langzeitspeicher übertragen. Als Teil des Archivierungsprozesses werden alle Ereignisse anonymisiert und alle sensiblen Felder mit personenbezogenen Daten (PII) entfernt (dies schließt optional PII-Felder wie `properties` ein). Die archivierten Daten enthalten immer noch das Feld `user_id`, das eine Analyse pro Benutzer über alle Ereignisdaten hinweg ermöglicht.

Sie können die Daten der letzten zwei Jahre für jedes Ereignis in der entsprechenden Ansicht `USERS_*_SHARED` abfragen. Außerdem gibt es für jedes Ereignis eine Ansicht `USERS_*_SHARED_ALL`, die abgefragt werden kann, um sowohl anonymisierte als auch nicht-anonymisierte Daten zurückzugeben.

#### Historische Daten
Das Archiv der historischen Ereignisdaten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake speicherte, wurden Produktänderungen vorgenommen, die dazu geführt haben könnten, dass einige dieser Daten etwas anders aussahen oder einige Nullwerte enthielten (da wir zu diesem Zeitpunkt nicht in jedes verfügbare Feld Daten eingegeben haben). Am besten gehen Sie davon aus, dass alle Ergebnisse, die Daten vor August 2019 enthalten, etwas anders aussehen können als erwartet.

### Einhaltung der Allgemeinen Datenschutzverordnung (GDPR)
Fast jeder Ereignisdatensatz, den Braze speichert, enthält einige Felder mit personenbezogenen Daten (PII) der Benutzer. Einige Ereignisse können E-Mail-Adressen, Telefonnummern, Geräte-IDs, Sprachen, Geschlechter und Standortinformationen enthalten. Wenn der Antrag eines Benutzers auf Vergessenwerden an Braze übermittelt wird, löschen wir diese PII-Felder für alle Ereignisse, die zu diesen Benutzern gehören. Auf diese Weise wird die historische Aufzeichnung des Ereignisses nicht gelöscht, aber das Ereignis kann nun nicht mehr mit einer bestimmten Person in Verbindung gebracht werden.

### Geschwindigkeit, Leistung, Kosten der Abfragen
Die Geschwindigkeit, die Leistung und die Kosten jeder Abfrage, die auf den Daten ausgeführt wird, hängen von der Größe des Warehouses ab, das Sie für die Abfrage der Daten verwenden. Je nachdem, auf wie viele Daten Sie für Analysen zugreifen, kann es vorkommen, dass Sie eine größere Warehouse-Größe verwenden müssen, damit die Abfrage erfolgreich ist. Snowflake verfügt über ausgezeichnete Ressourcen zur Bestimmung der richtigen Größe, darunter [Übersicht über Lagerhäuser](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Überlegungen zum Lagerhaus](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

## Braze Benchmarks

Benchmarks, [ein von Braze entwickeltes Datentool](https://www.braze.com/perspectives/benchmarks), ermöglicht es Interessenten und Kunden von Braze zu sehen, wie sie im Vergleich zu den Top-Playern in ihrer Branche abschneiden, indem sie ihre Kennzahlen mit den Branchen-Benchmarks von Braze vergleichen.

Zu den ersten Branchen gehören:
- Lieferdienste
- E-Commerce
- Bildungswesen
- Unterhaltung
- Finanzen
- Gaming
- Gesundheit
- Lebensstil
- Restaurants
- Einzelhandel
- Technologie
- Transport
- Reisen

Unsere Benchmarking-Daten sind auch direkt im [Snowflake Data Exchange](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR) verfügbar.

> Eine Reihe von Beispielabfragen, auf die Sie sich bei der Einrichtung von Snowflake beziehen können, finden Sie in unseren [Beispielabfragen][SQ] und Beispielen [für die Einrichtung der ETL-Ereignis-Pipeline][ETL].

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
