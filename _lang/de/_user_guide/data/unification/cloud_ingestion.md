---
nav_title: Cloud-Datenaufnahme
article_title: Cloud-Datenaufnahme von Braze
alias: /cloud_ingestion/
description: "Dieser Referenzartikel behandelt die Quellen der Braze Cloud Data Ingestion und Empfehlungen zum Daten-Setup."
page_order: 0.1
toc_headers: h2
---

# Cloud-Datenaufnahme von Braze

> Mit Braze Cloud Datenaufnahme (CDI) können Sie eine direkte Verbindung von Ihrer Datenspeicherlösung einrichten, um relevante Nutzerdaten und andere Nicht-Nutzerdaten mit Braze zu synchronisieren. Diese Daten können anschließend für die Personalisierung oder Segmentierung verwendet werden, um Ihre Marketing-Anwendungsfälle zu optimieren. Die flexible Integration der Datenaufnahme unterstützt komplexe Datenstrukturen, einschließlich verschachtelter JSON-Dateien und Objekt-Arrays.

## Funktionsweise

Mit Braze Cloud Data Ingestion (CDI) richten Sie eine Integration zwischen Ihrer Data Warehouse Instanz und dem Braze Workspace ein, um Daten auf einer wiederkehrenden Basis zu synchronisieren. Diese Synchronisierung läuft nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen anderen Zeitplan haben. Die Synchronisierung kann so häufig wie alle 15 Minuten oder so selten wie einmal im Monat erfolgen. Wenn Sie Synchronisierungen häufiger als 15 Minuten benötigen, wenden Sie sich an Ihren Customer-Success-Manager oder ziehen Sie die Verwendung von REST API-Aufrufen für die Datenaufnahme in Echtzeit in Betracht.

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten auf Ihrem Braze-Dashboard. Bei jeder Synchronisierung werden alle Updates der Daten in Braze übernommen.

### Ihre ID für die Integration finden

Sie finden Ihre Integrations-ID in der URL, wenn Sie eine Integration im Braze-Dashboard anzeigen. Bitte navigieren Sie zu **„Dateneinstellungen“** > **„Cloud-Datenaufnahme“** und wählen Sie eine Integration aus. Die ID der Integration wird in der URL im Format angezeigt`https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Wenn Ihre URL beispielsweise lautet`https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, lautet Ihre ID für die`abc123xyz` Integration . Sie können diese ID verwenden, wenn Sie API-Aufrufe durchführen, um Synchronisierungen zu triggern oder den Synchronisierungsstatus zu überprüfen.

## Anwendungsfälle

Mit den Funktionen zur Datenaufnahme von Braze Cloud können Sie:

- Erstellen Sie in wenigen Minuten eine einfache Integration direkt von Ihrer Data-Warehouse- oder Dateispeicher-Lösung zu Braze.
- Synchronisieren Sie Nutzerdaten, einschließlich Attributen, Ereignissen und Käufen, sicher von Ihrem Data Warehouse mit Braze.
- Schließen Sie die Datenschleife mit Braze, indem Sie die Datenaufnahme aus der Cloud mit Currents oder Snowflake Data Sharing kombinieren.

Darüber hinaus stellen [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) eine Zero-Copy-Alternative dar. Sie können Braze direkt Ihre Data Warehouse- oder Dateispeicher-Lösung abfragen lassen, um CDI-Segmente zu erstellen – ohne die zugrunde liegenden Daten nach Braze zu kopieren.

## Unterstützte Datenquellen

Cloud Datenaufnahme kann Daten synchronisieren aus:

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Unterstützte Datentypen 

Cloud Data Ingestion unterstützt die folgenden Datentypen:

### Nutzerdaten
- Nutzer:innen-Attribute, einschließlich:
   - Verschachtelte angepasste Attribute
   - Arrays von Objekten
   - Abo-Status
- Angepasste Events
- Kauf-Events
- Anfragen zur Löschung von Benutzerkonten

### Nicht verwendete Objekte
- Artikel im Katalog

### Zero-Copy-Messaging
- Verbundene Quellen

## Bezeichner für die Datenaufnahme

Bei der Synchronisierung von Nutzerdaten über die Datenaufnahme können Sie Nutzer:innen anhand eines oder mehrerer der folgenden Bezeichner identifizieren. Jede Zeile in Ihrer Quelltabelle sollte jeweils nur einen Wert für einen Bezeichner enthalten, jedoch kann Ihre Tabelle Spalten für einen, zwei, drei, vier oder alle fünf Bezeichner enthalten.

| Bezeichner | Beschreibung |
|------------|-------------|
| `EXTERNAL_ID` | Die externe ID, die das zu erstellende oder zu aktualisierende Nutzerprofil identifiziert. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der vom Braze SDK generierte Braze-Bezeichner für Nutzer:innen. Neue Nutzer:innen können nicht mithilfe einer Braze-ID über die Datenaufnahme erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail Adresse des Nutzers:innen. Sollten mehrere Profile mit derselben E-Mail-Adresse vorhanden sein, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Sollten mehrere Profile mit derselben Telefonnummer vorhanden sein, wird das zuletzt aktualisierte Profil für Updates bevorzugt behandelt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ausführliche Informationen zum Einrichten von Tabellen mit diesen Bezeichnern finden Sie in der Dokumentation [zu Data Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Datenpunkt-Nutzung

Für Kunden mit datenpunktbasierter Abrechnung entspricht die Abrechnung von Datenpunkten für Cloud Data Ingestion der Abrechnung von Updates über den[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)[Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion wird auf das verfügbare Rate-Limit angerechnet. Wenn Sie also Daten mit einer anderen Methode senden, wird das Rate-Limit zwischen der Braze API und Cloud Data Ingestion kombiniert.
{% endalert %}

## Einschränkungen des Produkts

| Begrenzung            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Es ist jedoch nur eine Integration pro Tabelle oder Ansicht möglich.                                             |
| Anzahl der Zeilen         | Standardmäßig können pro Lauf bis zu 500 Millionen Zeilen synchronisiert werden. Synchronisierungen mit mehr als 500 Millionen neuen Zeilen werden unterbrochen. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren Customer-Success-Manager von Braze oder an den Braze Support. |
| Attribute pro Zeile     | Jede Zeile sollte eine einzelne Nutzer:innen ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d.h. ein Array zählt als ein Attribut). |
| Größe der Nutzlast           | Jede Zeile kann eine Nutzlast von bis zu 1 MB enthalten. Nutzdaten, die größer als 1 MB sind, werden abgelehnt, und der Fehler „Nutzdaten waren größer als 1 MB” wird zusammen mit der zugehörigen externen ID und den gekürzten Nutzdaten im Synchronisierungsprotokoll vermerkt. |
| Datentyp              | Sie können Nutzer:innen-Attribute, Ereignisse und Käufe über die Datenaufnahme in der Cloud synchronisieren.                                                                                                  |
| Braze Region           | Dieses Produkt ist in allen Braze Regionen erhältlich. Jede Braze-Region kann sich mit jeder Daten-Quellregion verbinden.                                                                              |
| Quelle Region       | Braze stellt eine Verbindung zu Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region und bei jedem Cloud-Anbieter her.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
