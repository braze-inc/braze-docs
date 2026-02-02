---
nav_title: Snowflake Data Sharing
hidden: true
---

# Snowflake Integration zur gemeinsamen Nutzung von Daten

> Wenn Snowflake Data Share als Integrationsmethode verwendet wird, stellt Braze im Namen des Kunden eine Freigabe für Ihre Snowflake-Instanz bereit. Diese Freigabe umfasst automatisch alle Ereignisse zum Engagement in Nachrichten und zum Verhalten der Nutzer:innen.

Anteile werden pro Kund:in bereitgestellt, nachdem der Kunde eine Berechtigung für Snowflake Data Share erworben hat. Wenn ein Kunde eine Datenfreigabe anfragt, fügt Braze dem Workspace des Kunden eine Freigabe hinzu, und der Kunde kann die Selbstbedienungs-UI verwenden, um die entsprechenden Daten des Partner-Snowflake-Kontos hinzuzufügen.

![]({% image_buster /assets/img/snowflake.png %})

Sobald die Freigabe bereitgestellt ist, sind alle Daten sofort von der Snowflake Instanz aus als eingehende Datenfreigabe zugänglich.

![]({% image_buster /assets/img/snowflake2.png %})

Innerhalb Ihrer Snowflake Instanz sehen Sie eine Aktie pro Region. Jede Tabelle hat eine Spalte, `app_group_id`, die quasi ein Mieterschlüssel für Braze ist. Wenn neue Kund:innen innerhalb derselben Region zu einer Aktie hinzugefügt werden, erscheinen sie als unterschiedliche `app_group_ids` in den bestehenden Tabellen.

{% alert important %}
Braze hostet derzeit alle Nutzer:innen-Daten in den Snowflake AWS Regionen US East-1 und EU-Central (Frankfurt). Obwohl Braze sich überregional austauschen kann, ist es für die Kund:innen am kostengünstigsten, wenn wir uns mit `US-EAST-1` und/oder `EU-CENTRAL-1` austauschen.
{% endalert %}

{% alert tip %}
Laden Sie die [Rohtabellenschemata]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) hier herunter oder verwenden Sie diesen Satz von [Beispiel-Ereignisdaten](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset), der auf dem Snowflake-Marktplatz verfügbar ist, um sich mit den gemeinsamen Ereignissen vertraut zu machen.
{% endalert %}

## Umgang mit doppelten Ereignissen

Duplikate sind zu erwarten, aber alle Ereignisse haben einen eindeutigen Bezeichner, die Spalte ID. Duplikate können mit `select distinct(id)` entfernt werden.

## Durchbrechende versus nicht-durchbrechende Änderungen

### Unwesentliche Änderungen

Nicht-unterbrechende Änderungen können jederzeit vorgenommen werden und bieten im Allgemeinen zusätzliche Funktionen. Beispiele für nicht-brechende Änderungen:
- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als nicht umbrechend gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *` Abfragen zu verwenden. Alternativ können Sie auch Ansichten erstellen, die Spalten explizit benennen, und diese Ansichten dann anstelle der Tabellen direkt abfragen.
{% endalert %}

### Wesentliche Änderungen

Wenn es möglich ist, werden Änderungen mit einer Ankündigung und einem Zeitraum für die Migration eingeleitet. Beispiele für bahnbrechende Änderungen sind:
- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer vorhandenen Spalte

## Einhaltung der allgemeinen Datenschutzverordnung (DSGVO)

Nahezu jeder Ereignisdatensatz, den Braze speichert, enthält einige Felder, die Nutzer:innen persönlich identifizierbare Informationen (PII) liefern. Einige Ereignisse können E-Mail Adresse, Telefonnummer, ID des Geräts, Sprache, Geschlecht und Standortinformationen enthalten. Wenn die Anfrage eines Nutzers auf Vergessenwerden an Braze übermittelt wird, löschen wir diese PII-Felder für alle Ereignisse, die diesen Nutzer:innen gehören. Auf diese Weise wird die historische Aufzeichnung des Ereignisses nicht gelöscht, aber das Ereignis kann nun nicht mehr mit einer bestimmten Person in Verbindung gebracht werden.
