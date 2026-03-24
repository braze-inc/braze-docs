---
nav_title: FAQs
article_title: FAQs zur Cloud-Datenaufnahme
page_order: 100
page_type: FAQ
description: "Diese Seite beantwortet häufig gestellte Fragen zur Cloud-Datenaufnahme."
toc_headers: h2
---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zur Cloud-Datenaufnahme.

## Warum habe ich eine E-Mail erhalten: „Fehler in der CDI-Synchronisation"?

Diese Art von E-Mail bedeutet normalerweise, dass es ein Problem mit Ihrer CDI-Einrichtung gibt. Hier sind einige häufige Probleme und wie Sie sie beheben können:

### CDI kann mit Ihren Zugangsdaten nicht auf das Data Warehouse oder die Tabelle zugreifen

Dies könnte bedeuten, dass die Zugangsdaten in CDI falsch sind oder im Data Warehouse falsch konfiguriert wurden. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### Die Tabelle kann nicht gefunden werden

Versuchen Sie, Ihre Integration mit der richtigen Datenbankkonfiguration zu aktualisieren, oder erstellen Sie passende Ressourcen im Data Warehouse, z. B. `database/table`.

### Der Katalog kann nicht gefunden werden

Der in der Integration eingerichtete Katalog ist im Braze-Katalog nicht vorhanden. Ein Katalog kann entfernt werden, nachdem die Integration eingerichtet wurde. Um das Problem zu beheben, aktualisieren Sie entweder die Integration, um einen anderen Katalog zu verwenden, oder erstellen Sie einen neuen Katalog, der dem Katalognamen in der Integration entspricht.

## Warum habe ich eine E-Mail erhalten: „Zeilenfehler in Ihrer CDI-Synchronisation"?

Diese Art von E-Mail bedeutet, dass einige Ihrer Daten während der Synchronisierung nicht verarbeitet werden konnten. Um den spezifischen Fehler herauszufinden, können Sie die Protokolle in Braze einsehen, indem Sie zu **CDI** > **Sync Log** gehen.

## Wie behebe ich Fehler bei Test Connection und Support-E-Mails?

{% tabs %}
{% tab Snowflake %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Fehler bei der Verbindung zur Snowflake-Instanz: Eingehende Anfrage mit IP ist für den Zugriff auf Snowflake nicht zulässig

Versuchen Sie, die offiziellen Braze-IPs zu Ihrer IP-Zulassungsliste hinzuzufügen. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), oder erlauben Sie die entsprechenden IPs:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Fehler bei der Ausführung von SQL aufgrund der Kund:innen-Konfiguration: 002003 (42S02): SQL-Kompilierungsfehler: existiert nicht oder ist nicht autorisiert

Wenn die Tabelle nicht existiert, erstellen Sie die Tabelle. Wenn die Tabelle existiert, überprüfen Sie, ob Nutzer:in und Rolle die Berechtigung haben, aus der Tabelle zu lesen.

### Schema konnte nicht verwendet werden

Wenn Sie diesen Fehler erhalten, gewähren Sie der angegebenen Nutzer:in oder Rolle Zugriff auf dieses Schema.

### Rolle konnte nicht verwendet werden

Wenn Sie diese Fehlermeldung erhalten, erlauben Sie der Nutzer:in, die angegebene Rolle zu verwenden.

### Nutzer:innen-Zugriff deaktiviert

Wenn Sie diesen Fehler erhalten, erlauben Sie der Nutzer:in den Zugriff auf Ihr Snowflake-Konto.

### Fehler bei der Verbindung zur Snowflake-Instanz mit aktuellem und altem Schlüssel

Wenn Sie diese Fehlermeldung erhalten, vergewissern Sie sich, dass die Nutzer:in den aktuellen Public Key verwendet, der in Ihrem Braze-Dashboard angezeigt wird.
{% endtab %}

{% tab Redshift %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Zugriff auf die Relation verweigert {table_name}

Wenn Sie diesen Fehler erhalten:

  - Erteilen Sie der Nutzer:in die Berechtigung `usage` für das Schema.
  - Erteilen Sie der Nutzer:in die Berechtigung `select` für die Tabelle.

### Fehler beim Erstellen der Verbindung

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der Redshift-Endpunkt und der Port korrekt sind.

### Fehler beim Erstellen des SSH-Tunnels

Wenn Sie diesen Fehler erhalten:

  - Überprüfen Sie, ob der Public Key in Ihrem Braze-Dashboard auf dem für das SSH-Tunneling verwendeten EC2-Host vorhanden ist.
  - Überprüfen Sie, ob Ihr Benutzername korrekt ist.
  - Überprüfen Sie, ob der SSH-Tunnel korrekt ist.
{% endtab %}

{% tab BigQuery %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Nutzer:in hat keine Berechtigung, die Tabelle abzufragen

Wenn Sie diesen Fehler erhalten, fügen Sie der Nutzer:in die Berechtigung zur Abfrage der Tabelle hinzu.

### Ihre Nutzung hat das angepasste Kontingent überschritten

Wenn Sie diese Fehlermeldung erhalten, muss Ihr Kontingent aktualisiert werden, damit Sie die Synchronisierung mit Ihrer aktuellen Rate fortsetzen können.

### Tabelle wurde am Standort {region} nicht gefunden

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob sich Ihre Tabelle im richtigen Projekt und Datensatz befindet.

### Ungültige JWT-Signatur

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der BigQuery-API-Dienst für Ihr Konto aktiviert ist.
{% endtab %}

{% tab Databricks %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Bei Databricks kann es zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Befehl fehlgeschlagen, da das Warehouse gestoppt wurde

Wenn Sie diese Fehlermeldung erhalten, stellen Sie sicher, dass das Databricks-Warehouse läuft.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

Wenn Sie diesen Fehler erhalten, lesen Sie [Databricks: Forbidden-Fehler beim Zugriff auf S3-Daten](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Wie aktualisiere ich meine E-Mail-Benachrichtigungseinstellungen für CDI-Integrationen?

Jede Integration hat ihre eigene Benachrichtigungspräferenz. Gehen Sie auf die CDI-Seite und wählen Sie den Namen der Integration aus, die Sie aktualisieren möchten. Im Abschnitt **Benachrichtigungseinstellungen** können Sie festlegen, wie Sie Benachrichtigungen über die ausgewählte Integration erhalten.

## Was passiert, wenn ein zukünftiger UPDATED_AT-Wert mit einer Integration synchronisiert wird?

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Daten neu sind. Nachdem ein zukünftiger `UPDATED_AT`-Wert synchronisiert wurde, werden Daten, die vor diesem zukünftigen Datum und Zeitpunkt liegen, nicht mehr verarbeitet. Um dies zu beheben:

1. Korrigieren Sie `UPDATED_AT`.
2. Entfernen Sie alle alten Daten, die bereits mit Braze synchronisiert wurden.
3. Erstellen Sie eine neue Integration, um diese Tabelle erneut zu verarbeiten.

## Warum stimmt „Synchronisierte Zeilen" nicht mit der Anzahl in meinem Warehouse überein?

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Datensätze bei einer Synchronisierung übernommen werden sollen. Sehen Sie sich [diese Illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) an, um zu verstehen, wie es funktioniert. Zu Beginn eines Synchronisierungslaufs fragt CDI Ihr Warehouse ab, um alle Datensätze zu erhalten, deren `UPDATED_AT`-Zeitstempel später als der zuvor verarbeitete `UPDATED_AT`-Wert ist. Datensätze an der exakten Grenz-Zeitstempel-Marke können ebenfalls erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel haben. Jeder Datensatz, der zum Zeitpunkt der Abfrageausführung erfasst wird, wird mit Braze synchronisiert. Hier sind häufige Fälle, in denen ein Datensatz möglicherweise nicht synchronisiert wird:

- Sie fügen der Tabelle Datensätze mit einem `UPDATED_AT`-Wert hinzu, der bereits verarbeitet wurde.
- Sie aktualisieren Datensatzwerte, nachdem sie durch eine Synchronisierung verarbeitet wurden, lassen aber `UPDATED_AT` unverändert. 
- Sie fügen Datensätze hinzu oder aktualisieren sie, während eine Synchronisierung läuft. Je nachdem, wann die CDI-Abfrage ausgeführt wird, kann es zu Race-Conditions kommen, die dazu führen, dass Datensätze nicht erfasst werden.

{% alert tip %}
Um dieses Verhalten in Zukunft zu vermeiden, empfehlen wir, monoton ansteigende `UPDATED_AT`-Werte zu verwenden und die Tabelle während Ihres geplanten Synchronisierungslaufs nicht zu aktualisieren.
{% endalert %}

## Wird bei einer Synchronisierung die Reihenfolge beibehalten, wenn mehrere Datensätze dieselbe ID haben?

Die Verarbeitungsreihenfolge ist nicht zu 100 % vorhersehbar. Wenn zum Beispiel während einer Synchronisierung mehrere Zeilen mit derselben `EXTERNAL_ID` in der Tabelle vorhanden sind, können wir nicht garantieren, welcher Wert im endgültigen Profil landet. Wenn Sie dieselbe `EXTERNAL_ID` mit verschiedenen Attributen in der Nutzlastspalte aktualisieren, werden alle Änderungen übernommen, wenn die Synchronisierung abgeschlossen ist.

## Warum werden bei meiner CDI-Synchronisierung keine neuen Nutzer:innen angelegt?

Wenn in Ihrer CDI-Integration die Option **Nur vorhandene Nutzer:innen aktualisieren** aktiviert ist, werden nur Nutzer:innen aktualisiert, die bereits in Braze vorhanden sind, und es werden keine neuen Nutzer:innen erstellt. Das bedeutet, dass eine Zeile in Ihrer Synchronisierungstabelle, die eine `EXTERNAL_ID` referenziert, die mit keiner vorhandenen Braze-Nutzer:in übereinstimmt, übersprungen wird.

Um über CDI neue Nutzer:innen anzulegen, deaktivieren Sie die Option **Nur vorhandene Nutzer:innen aktualisieren** in Ihren Integrationseinstellungen. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** und wählen Sie eine Integration aus.

## Welche Sicherheitsmaßnahmen gibt es für CDI?

### Unsere Maßnahmen

Braze hat die folgenden Maßnahmen für CDI implementiert:

- Alle Zugangsdaten werden in unserer Datenbank verschlüsselt, und nur bestimmte Mitarbeitende haben authentifizierten Zugang zu ihnen.
- Wir verwenden verschlüsselte Verbindungen, um Daten aus Kund:innen-Warehouses abzurufen.
- Wir stellen Anfragen an die Braze-API-Endpunkte mit denselben API-Schlüsseln und TLS-Verbindungen, die wir unseren Kund:innen empfehlen.
- Wir aktualisieren unsere Bibliotheken regelmäßig und beziehen alle Sicherheits-Patches.

### Ihre Maßnahmen

Wir empfehlen Ihnen und Ihrem Team, die folgenden Sicherheitsmaßnahmen auf Ihrer Seite einzurichten: 

- Beschränken Sie den Zugriff auf Zugangsdaten auf das für den Betrieb von CDI erforderliche Minimum. Das liegt daran, dass wir in der Lage sein müssen, select (und count) auf den spezifischen Tabellen und Views auszuführen.
- Beschränken Sie die IPs, die auf die Tabellen zugreifen können, auf offiziell veröffentlichte [Braze-IPs]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).