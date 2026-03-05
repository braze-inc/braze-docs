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

## Wenn die Tabellen SNAPSHOTS und CHANGELOGS aktualisiert werden

Die Tabellen SNAPSHOTS und CHANGELOGS verfolgen Änderungen an Kampagnen und Canvase. Zu wissen, wann diese Tabellen aktualisiert werden, ist wichtig für die Abfrage der neuesten Nachrichtenvariationen und Canvas-Konfigurationen.

### CHANGELOGS_CAMPAIGN_SHARED

Eine Zeile wird zu `CHANGELOGS_CAMPAIGN_SHARED` hinzugefügt, wenn:
- Die Kampagne wird gestartet, ODER
- Eines der folgenden snapshottable Felder wird geändert:
  - Name
  - Aktionen (einschließlich Änderungen des Inhalts von Nachrichten)
  - Verhalten bei Konversion

{% alert important %}
Das Speichern oder Aktualisieren des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie die Kampagne starten oder die Änderungen des Entwurfs nach dem Start auf die aktive Kampagne anwenden.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` wird von `CHANGELOGS_CAMPAIGN_SHARED` abgeleitet. Diese Tabelle extrahiert die Spalte "Aktionen" aus `CHANGELOGS_CAMPAIGN_SHARED` und fasst sie zu einzelnen Datensätzen für Nachrichtenvariationen zusammen. Sie wird entsprechend aktualisiert, wenn `CHANGELOGS_CAMPAIGN_SHARED` aktualisiert wird.

### CHANGELOGS_CANVAS_SHARED

Eine Zeile wird zu `CHANGELOGS_CANVAS_SHARED` hinzugefügt, wenn:
- Der Canvas wird gestartet, ODER
- Eines der folgenden snapshottable Felder wird geändert:
  - Name
  - Verhalten bei Konversion
  - Variationen (Prozentsatz, Zuordnungen der ersten Stufe, Variationsnamen)

{% alert important %}
Das Speichern oder Aktualisieren des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` wird von `CHANGELOGS_CANVAS_SHARED` abgeleitet. Diese Tabelle verwendet das gleiche Extraktionsmuster wie `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` und wird entsprechend aktualisiert, wenn `CHANGELOGS_CANVAS_SHARED` aktualisiert wird.

### SNAPSHOTS_CANVAS_STEP_SHARED

Eine Zeile wird zu `SNAPSHOTS_CANVAS_STEP_SHARED` hinzugefügt, wenn:
- Der Canvas wird gestartet, ODER
- Der aktive Canvas wird aktualisiert (Entwurf nach dem Start angewendet) ODER
- Eines der folgenden snapshottable Felder wird geändert:
  - Name
  - Aktionen (einschließlich Änderungen des Inhalts von Nachrichten innerhalb von Nachrichtenvariationen)

{% alert important %}
Das Speichern des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Eine Zeile wird zu `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` hinzugefügt, wenn:
- Der Canvas wird gestartet, ODER
- Der aktive Canvas wird aktualisiert (Entwurf nach dem Start angewendet) ODER
- Eines der folgenden snapshottable Felder wird geändert:
  - Name

{% alert important %}
Das Speichern des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

## Einhaltung der allgemeinen Datenschutzverordnung (DSGVO)

{% include partners/snowflake_pii_gdpr.md %}