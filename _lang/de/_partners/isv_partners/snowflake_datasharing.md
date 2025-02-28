---
nav_title: Snowflake Daten gemeinsam nutzen
hidden: true
---

# Integration der gemeinsamen Nutzung von Snowflake-Daten

> Wenn Snowflake Data Share als Integrationsmethode verwendet wird, stellt Braze im Namen des Kunden eine Freigabe für Ihre Snowflake-Instanz bereit. Diese Freigabe umfasst automatisch alle Ereignisse zur Einbindung von Nachrichten und zum Nutzerverhalten.

Anteile werden pro Kunde bereitgestellt, nachdem der Kunde eine Berechtigung für Snowflake Data Share erworben hat. Wenn ein Kunde eine Datenfreigabe anfordert, fügt Braze dem Arbeitsbereich des Kunden eine Freigabe hinzu, und der Kunde kann die Selbstbedienungsschnittstelle nutzen, um die entsprechenden Snowflake-Kontodaten des Partners hinzuzufügen.

![]({% image_buster /assets/img/snowflake.png %})

Sobald die Freigabe bereitgestellt ist, sind alle Daten sofort von der Snowflake-Instanz aus als eingehende Datenfreigabe zugänglich.

![]({% image_buster /assets/img/snowflake2.png %})

Innerhalb Ihrer Snowflake-Instanz sehen Sie eine Aktie pro Region. Jede Tabelle hat eine Spalte, `app_group_id`, die quasi ein Mieterschlüssel für Braze ist. Wenn neue Kunden zu einer Aktie innerhalb derselben Region hinzugefügt werden, erscheinen sie als unterschiedliche `app_group_ids` in den bestehenden Tabellen.

{% alert important %}
Braze hostet derzeit alle Daten auf Benutzerebene in den Snowflake AWS-Regionen US East-1 und EU-Central (Frankfurt). Obwohl Braze überregional teilen kann, ist es für die Kunden am kostengünstigsten, wenn wir mit `US-EAST-1` und/oder `EU-CENTRAL-1` teilen.
{% endalert %}

{% alert tip %}
Laden Sie die [Rohtabellenschemata]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) hier herunter oder verwenden Sie diesen Satz von [Beispiel-Ereignisdaten](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset), der auf dem Snowflake-Marktplatz verfügbar ist, um sich mit den gemeinsamen Ereignissen vertraut zu machen.
{% endalert %}

## Umgang mit doppelten Ereignissen

Duplikate sind zu erwarten, aber alle Ereignisse haben einen eindeutigen Bezeichner, die Spalte ID. Duplikate können mit `select distinct(id)` entfernt werden.

## Durchbrechende versus nicht-durchbrechende Änderungen

### Nicht-unterbrechende Änderungen

Nicht-unterbrechende Änderungen können jederzeit vorgenommen werden und bieten im Allgemeinen zusätzliche Funktionen. Beispiele für nicht-brechende Änderungen:
- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als nicht umbrechend betrachtet werden, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *` Abfragen zu verwenden. Alternativ können Sie auch Ansichten erstellen, die Spalten explizit benennen, und diese Ansichten dann anstelle der Tabellen direkt abfragen.
{% endalert %}

### Wechselnde Änderungen

Wenn es möglich ist, werden grundlegende Änderungen angekündigt und eine Umstellungsphase eingeleitet. Beispiele für bahnbrechende Änderungen sind:
- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer vorhandenen Spalte

## Einhaltung der Allgemeinen Datenschutzverordnung (GDPR)

Fast jeder Ereignisdatensatz, den Braze speichert, enthält einige Felder mit personenbezogenen Daten (PII) der Benutzer. Einige Ereignisse können E-Mail-Adressen, Telefonnummern, Geräte-IDs, Sprachen, Geschlechter und Standortinformationen enthalten. Wenn der Antrag eines Benutzers auf Vergessenwerden an Braze übermittelt wird, löschen wir diese PII-Felder für alle Ereignisse, die zu diesen Benutzern gehören. Auf diese Weise wird die historische Aufzeichnung des Ereignisses nicht gelöscht, aber das Ereignis kann nun nicht mehr mit einer bestimmten Person in Verbindung gebracht werden.
