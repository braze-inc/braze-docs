---
nav_title: FAQs
article_title: Häufig gestellte Fragen zu Cloud Data Ingestion
page_order: 100
page_type: FAQ
description: "Dieser Artikel beantwortet häufig gestellte Fragen zu Cloud Data Ingestion."
toc_headers: h2
---

# Häufig gestellte Fragen (FAQ)

> Hier finden Sie die Antworten auf einige häufig gestellte Fragen zum Thema Cloud Data Ingestion.

## Warum habe ich eine E-Mail erhalten: "Fehler in der CDI-Synchronisation"?

Diese Art von E-Mail bedeutet normalerweise, dass es ein Problem mit Ihrer CDI-Einrichtung gibt. Hier sind einige häufige Probleme und wie Sie sie beheben können:

### CDI kann mit Ihren Zugangsdaten nicht auf das Data Warehouse oder die Tabelle zugreifen

Dies könnte bedeuten, dass die Zugangsdaten in CDI falsch sind oder im Data Warehouse falsch konfiguriert wurden. Weitere Informationen finden Sie unter [Data Warehouse-Integrationen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/).

### Die Tabelle kann nicht gefunden werden

Versuchen Sie, Ihre Integration mit der richtigen Datenbankkonfiguration zu aktualisieren, oder erstellen Sie passende Ressourcen im Data Warehouse, z. B. `database/table`.

### Der Katalog kann nicht gefunden werden

Der Katalog, der in der Integration eingerichtet wurde, existiert nicht im Braze-Katalog. Ein Katalog kann entfernt werden, nachdem die Integration eingerichtet wurde. Um das Problem zu beheben, aktualisieren Sie entweder die Integration, um einen anderen Katalog zu verwenden, oder erstellen Sie einen neuen Katalog, der dem Katalognamen in der Integration entspricht.

## Warum habe ich eine E-Mail erhalten: "Zeilenfehler in Ihrer CDI-Synchronisation"?

Diese Art von E-Mail bedeutet, dass einige Ihrer Daten während der Synchronisierung nicht verarbeitet werden konnten. Um den spezifischen Fehler herauszufinden, können Sie die Protokolle in Braze einsehen, indem Sie zu **CDI** > **Sync Log** gehen.

## Wie behebe ich Fehler bei Test Connection und Support E-Mails?

{% tabs %}
{% tab Snowflake %}
### Test Verbindung läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, so dass eine Erhöhung der Data Warehouse-Kapazität dessen Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Fehler bei der Verbindung zur Snowflake Instanz: Eingehende Anfrage mit IP ist für den Zugriff auf Snowflake nicht zulässig

Versuchen Sie, die offiziellen IPs von Braze zu Ihrer IP-Zulassungsliste hinzuzufügen. Weitere Informationen finden Sie unter [Data Warehouse-Integrationen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/).

### Fehler bei der Ausführung von SQL aufgrund der Kundenkonfiguration: 002003 (42S02): SQL Kompilierungsfehler: existiert nicht oder ist nicht autorisiert

Wenn die Tabelle nicht existiert, erstellen Sie die Tabelle. Wenn die Tabelle existiert, überprüfen Sie, ob die:der Nutzer:in und die Rolle die Berechtigung haben, aus der Tabelle zu lesen.

### Konnte Schema nicht verwenden

Wenn Sie diesen Fehler erhalten, gewähren Sie dem angegebenen Nutzer:in oder der angegebenen Rolle Zugriff auf dieses Schema.

### Konnte Rolle nicht verwenden

Wenn Sie diese Fehlermeldung erhalten, erlauben Sie diesem Nutzer:in die angegebene Rolle zu wechseln.

### Nutzer:in deaktiviert

Wenn Sie diesen Fehler erhalten, erlauben Sie diesem Nutzer:innen den Zugriff auf Ihr Snowflake-Konto.

### Fehler bei der Verbindung zur Snowflake-Instanz mit aktuellem und altem Schlüssel

Wenn Sie diese Fehlermeldung erhalten, vergewissern Sie sich, dass die:der Nutzer:in den aktuellen Public Key verwendet, der in Ihrem Braze-Dashboard angezeigt wird.
{% endtab %}

{% tab Redshift %}
### Test Verbindung läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, so dass eine Erhöhung der Data Warehouse-Kapazität dessen Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Berechtigung verweigert für Relation {table_name}

Wenn Sie diesen Fehler erhalten:

  - Erteilen Sie die Berechtigung `usage` für das Schema dieses Nutzers:in.
  - Erteilen Sie dem Nutzer:in das Recht `select` für die Tabelle.

### Fehler beim Erstellen der Verbindung

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der Endpunkt und der Port von Redshift korrekt sind.

### SSH-Tunnel erstellen Fehler

Wenn Sie diesen Fehler erhalten:

  - Überprüfen Sie den Public Key auf Ihrem Braze-Dashboard auf dem für das SSH-Tunneling verwendeten ec2-Host.
  - Überprüfen Sie, ob Ihr Benutzername korrekt ist.
  - Überprüfen Sie, ob der SSH-Tunnel korrekt ist.
{% endtab %}

{% tab BigQuery %}
### Test Verbindung läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, so dass eine Erhöhung der Data Warehouse-Kapazität dessen Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Benutzer hat keine Berechtigung zur Abfrage der Tabelle

Wenn Sie diesen Fehler erhalten, fügen Sie Nutzer:innen die Berechtigung zur Abfrage der Tabelle hinzu.

### Ihre Nutzung hat die angepasste Quote überschritten

Wenn Sie diese Fehlermeldung erhalten, muss Ihr Kontingent aktualisiert werden, damit Sie die Synchronisierung mit Ihrer aktuellen Rate fortsetzen können.

### Tabelle wurde am Standort {region} nicht gefunden Standort

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob sich Ihre Tabelle im richtigen Projekt und Datensatz befindet.

### Ungültige JWT Signatur

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der BigQuery API Dienst für Ihr Konto aktiviert ist.
{% endtab %}

{% tab Databricks %}
### Test Verbindung läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, so dass eine Erhöhung der Data Warehouse-Kapazität dessen Geschwindigkeit verbessern kann. Bei Databricks kann es zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, wenn Braze eine Verbindung zu Classic und Pro SQL-Instanzen herstellt, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Befehl fehlgeschlagen, da Lagerhaus gestoppt wurde

Wenn Sie diese Fehlermeldung erhalten, stellen Sie sicher, dass Databricks Warehouse läuft.

### Dienste: Amazon S3; Status Code: 403; Fehlercode: 403 Verboten

Wenn Sie diesen Fehler erhalten, lesen Sie [Databricks: Unzulässiger Fehler beim Zugriff auf S3 Daten](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Wie aktualisiere ich meine E-Mail-Benachrichtigungseinstellungen für CDI-Integrationen?

Jede Integration hat ihre eigene Benachrichtigungspräferenz. Gehen Sie auf die CDI-Seite und wählen Sie den Namen der Integration aus, die Sie aktualisieren möchten. Im Bereich **Benachrichtigungseinstellungen** können Sie aktualisieren, wie Sie Benachrichtigungen über die ausgewählte Integration erhalten.

## Was passiert, wenn ein zukünftiger UPDATED_AT mit einer Integration synchronisiert wird?

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Daten neu sind. Nachdem ein zukünftiges `UPDATED_AT` synchronisiert wurde, werden Daten, die vor diesem zukünftigen Datum und Zeitpunkt liegen, nicht mehr verarbeitet. Um dies zu beheben:

1. Richtig `UPDATED_AT`.
2. Entfernen Sie alle alten Daten, die bereits mit Braze synchronisiert wurden
3. Erstellen Sie eine neue Integration, um diese Tabelle erneut zu verarbeiten.

## Warum stimmt "Synchronisierte Zeilen" nicht mit der Anzahl in meinem Lager überein?

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Datensätze bei einer Synchronisierung übernommen werden sollen. Sehen Sie sich [diese Illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) an, um zu sehen, wie es funktioniert. Zu Beginn eines Synchronisierungslaufs fragt CDI Ihr Lagerhaus ab, um alle Datensätze zu erhalten, deren `UPDATED_AT` später als der zuvor verarbeitete Wert ist. Jeder Datensatz, der zum Zeitpunkt der Ausführung der Abfrage erfasst wird, wird mit Braze synchronisiert. Hier sind die häufigsten Fälle, in denen ein Datensatz nicht synchronisiert werden kann:

- Sie fügen der Tabelle Datensätze mit einem `UPDATED_AT` Wert hinzu, der bereits verarbeitet wurde.
- Sie aktualisieren die Werte von Datensätzen, nachdem sie durch eine Synchronisierung verarbeitet wurden, lassen aber `UPDATED_AT` unverändert. 
- Sie fügen Datensätze hinzu oder aktualisieren sie, während eine Synchronisierung läuft. Je nachdem, wann die CDI-Abfrage ausgeführt wird, kann es Race-Conditions geben, die dazu führen, dass Datensätze nicht abgeholt werden.

{% alert tip %}
Um dieses Verhalten in Zukunft zu vermeiden, empfehlen wir, monoton ansteigende `UPDATED_AT` Werte zu verwenden und die Tabelle während Ihres Zeitplans nicht zu aktualisieren.
{% endalert %}

## Wird bei einer Synchronisierung die Reihenfolge beibehalten, wenn mehrere Datensätze dieselbe ID haben?

Die Reihenfolge der Bearbeitung ist nicht 100%ig vorhersehbar. Wenn zum Beispiel während einer Synchronisierung mehrere Zeilen mit demselben `EXTERNAL_ID` in der Tabelle vorhanden sind, können wir nicht garantieren, welcher Wert im endgültigen Profil landet. 

## Welche Sicherheitsmaßnahmen gibt es für CDI?

### Die Maßnahmen von Braze

Braze hat die folgenden Maßnahmen gegen CDI ergriffen:

- Alle Zugangsdaten werden in unserer Datenbank verschlüsselt, und nur bestimmte Mitarbeiter haben authentifizierten Zugang zu ihnen.
- Wir verwenden verschlüsselte Verbindungen, um Daten an die Data Warehouses der Kund:innen zu senden.
- Wir stellen Anfragen an die API-Endpunkte von Braze mit denselben API-Schlüsseln und TLS-Verbindungen, die wir unseren Kund:innen zu verwenden empfehlen.
- Wir aktualisieren unsere Bibliotheken regelmäßig und holen uns alle Sicherheits-Patches.

### Ihre Maßnahmen

Wir empfehlen Ihnen und Ihrem Team, die folgenden Sicherheitsmaßnahmen auf Ihrer Seite einzurichten: 

- Beschränken Sie den Zugriff auf Zugangsdaten auf das für den Betrieb von CDI erforderliche Minimum. Das liegt daran, dass wir in der Lage sein müssen, select (und count) auf den spezifischen Tabellen und Ansichten auszuführen.
- Beschränken Sie die IPs, die auf die Tabellen zugreifen können, auf offiziell veröffentlichte [Braze IPs]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).
