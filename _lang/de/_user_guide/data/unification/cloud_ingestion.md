---
nav_title: Cloud-Datenaufnahme
article_title: Cloud-Datenaufnahme von Braze
alias: /cloud_ingestion/
description: "Dieser Referenzartikel behandelt die Quellen der Braze Cloud Data Ingestion und Empfehlungen zum Daten-Setup."
page_order: 0.1
toc_headers: h2
---

# Cloud-Datenaufnahme von Braze

> Braze Cloud Data Ingestion (CDI) ermöglicht es Ihnen, eine direkte Verbindung von Ihrer Datenspeicherlösung einzurichten, um relevante Nutzerdaten und andere Nicht-Nutzerdaten mit Braze zu synchronisieren. Diese Daten können dann für die Personalisierung oder Segmentierung verwendet werden, um Ihre Marketing-Anwendungsfälle zu unterstützen. Die flexible Integration von Cloud Data Ingestion unterstützt komplexe Datenstrukturen, einschließlich verschachtelter JSON und Arrays von Objekten.

## Funktionsweise

Mit Braze Cloud Data Ingestion (CDI) richten Sie eine Integration zwischen Ihrer Data Warehouse Instanz und dem Braze Workspace ein, um Daten auf einer wiederkehrenden Basis zu synchronisieren. Diese Synchronisierung läuft nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen anderen Zeitplan haben. Die Synchronisierung kann so häufig wie alle 15 Minuten oder so selten wie einmal im Monat erfolgen. Wenn Sie Synchronisierungen häufiger als 15 Minuten benötigen, wenden Sie sich an Ihren Customer-Success-Manager oder ziehen Sie die Verwendung von REST API-Aufrufen für die Datenaufnahme in Echtzeit in Betracht.

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten auf Ihrem Braze-Dashboard. Jedes Mal, wenn die Synchronisierung ausgeführt wird, werden alle aktualisierten Daten in Braze angezeigt.

### Finden Sie Ihre Integration ID

Sie finden Ihre Integration ID in der URL, wenn Sie eine Integration im Braze-Dashboard anzeigen. Navigieren Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** und wählen Sie eine Integration aus. Die ID der Integration erscheint in der URL im Format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Wenn Ihre URL zum Beispiel `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz` lautet, ist Ihre Integration ID `abc123xyz`. Sie können diese ID verwenden, wenn Sie APIs aufrufen, um Synchronisierungen zu triggern oder den Synchronisierungsstatus zu überprüfen.

## Anwendungsfälle

Mit den Funktionen von Braze Cloud Data Ingestion können Sie:

- Erstellen Sie in wenigen Minuten eine einfache Integration direkt von Ihrer Data-Warehouse- oder Dateispeicher-Lösung zu Braze.
- Synchronisieren Sie Nutzerdaten, einschließlich Attribute, Ereignisse und Käufe aus Ihrem Data Warehouse sicher mit Braze.
- Schließen Sie den Datenkreislauf mit Braze, indem Sie die Datenaufnahme in der Cloud mit Currents oder Snowflake Data Sharing kombinieren.

Darüber hinaus sind [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) eine Null-Kopie-Alternative. Sie können Ihre Data Warehouse- oder Dateispeicherlösung direkt von Braze abfragen lassen, um CDI-Segmente zu erstellen - und zwar ohne die zugrunde liegenden Daten nach Braze zu kopieren.

## Unterstützte Datenquellen

Cloud Data Ingestion kann Daten von:

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
- Anfragen zur Löschung von Nutzer:in

### Nicht-Nutzer:in-Objekte
- Artikel im Katalog

### Null-Kopie Messaging
- Verbundene Quellen

## Nutzer:innen-Bezeichner für die Datenaufnahme

Wenn Sie Nutzerdaten über die Datenaufnahme in der Cloud synchronisieren, können Sie Nutzer:innen mit einem oder mehreren der folgenden Bezeichner identifizieren. Jede Zeile in Ihrer Quelltabelle sollte jeweils nur einen Wert für einen Bezeichnertyp enthalten, aber Ihre Tabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen enthalten.

| Bezeichner | Beschreibung |
|------------|-------------|
| `EXTERNAL_ID` | Die externe ID, die das zu erstellende oder zu aktualisierende Nutzerprofil identifiziert. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der vom Braze SDK generierte Bezeichner für Braze Nutzer:innen. Neue Nutzer:innen können nicht mit einer Braze ID über die Cloud-Datenaufnahme erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail Adresse des Nutzers:innen. Wenn mehrere Profile mit der gleichen E-Mail Adresse existieren, wird das zuletzt aktualisierte Profil bei Updates bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird E-Mail als primärer Bezeichner verwendet. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei Updates bevorzugt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ausführliche Informationen zum Einrichten von Tabellen mit diesen Bezeichnern finden Sie in der Dokumentation zu [Data Warehouse Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Datenpunkt-Nutzung

Für Kund:inen mit cloudbasierter Abrechnung entspricht die Abrechnung der Datenpunkte für die Datenaufnahme in der Cloud der Abrechnung von Updates über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion wird auf das verfügbare Rate-Limit angerechnet. Wenn Sie also Daten mit einer anderen Methode senden, wird das Rate-Limit zwischen der Braze API und Cloud Data Ingestion kombiniert.
{% endalert %}

## Einschränkungen des Produkts

| Begrenzung            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Sie können jedoch nur eine Integration pro Tabelle oder Ansicht einrichten.                                             |
| Anzahl der Zeilen         | Standardmäßig können pro Lauf bis zu 500 Millionen Zeilen synchronisiert werden. Alle Synchronisierungen mit mehr als 500 Millionen neuen Zeilen werden gestoppt. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren Customer-Success-Manager von Braze oder an den Braze Support. |
| Attribute pro Zeile     | Jede Zeile sollte eine einzelne Nutzer:innen ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d.h. ein Array zählt als ein Attribut). |
| Größe der Nutzlast           | Jede Zeile kann eine Nutzlast von bis zu 1 MB enthalten. Nutzdaten, die größer als 1 MB sind, werden zurückgewiesen, und der Fehler "Payload was greater than 1MB" wird zusammen mit der zugehörigen externen ID und der abgeschnittenen Nutzdaten im Synchronisierungsprotokoll protokolliert. |
| Datentyp              | Sie können Nutzer:innen-Attribute, Ereignisse und Käufe über die Datenaufnahme in der Cloud synchronisieren.                                                                                                  |
| Braze Region           | Dieses Produkt ist in allen Braze Regionen erhältlich. Jede Braze-Region kann sich mit jeder Daten-Quellregion verbinden.                                                                              |
| Quelle Region       | Braze stellt eine Verbindung zu Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region oder bei jedem Cloud-Anbieter her.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
