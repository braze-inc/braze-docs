---
nav_title: Nutzerimport
article_title: Nutzerimport
page_order: 4
page_type: reference
description: "Dieser Artikel referenziert den Import von Nutzer:innen in Ihr Braze-Dashboard mit Hilfe der REST API, Cloud Data Ingestion, CSV und bewährten Verfahren für den Import."

---
# Nutzer:in importieren

> Braze bietet verschiedene Möglichkeiten, Nutzer:innen-Daten in die Plattform zu importieren: SDKs, APIs, Datenaufnahme in der Cloud, Partnerintegrationen und CSV-Dateien.

Bevor Sie fortfahren, beachten Sie bitte, dass Braze die HTML-Daten während des Imports nicht bereinigt (validiert oder richtig formatiert). Das bedeutet, dass Script Tags für alle importierten Daten, die für die Personalisierung im Internet bestimmt sind, entfernt werden müssen.

Wenn Sie Daten in Braze importieren, die speziell für die Personalisierung in einem Webbrowser bestimmt sind, stellen Sie sicher, dass sie frei von HTML-, JavaScript- oder anderen Skript-Tags sind, die bei der Darstellung in einem Webbrowser möglicherweise böswillig genutzt werden könnten.  

Alternativ können Sie für HTML auch die Braze Liquid Filter (`strip_html`) verwenden, um gerenderten Text in HTML umzuwandeln. Zum Beispiel:

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## REST API

Verwenden Sie den [`/users/track` Endpunkt][12], um angepasste Events, Nutzer-Attribute und Käufe für Nutzer:innen zu erfassen.

## Cloud-Datenaufnahme

Verwenden Sie Braze [Cloud Data Ingestion][14] zum Importieren und Verwalten von Nutzer:innen-Attributen. 

## CSV-Import

Sie können Nutzerprofile über CSV-Dateien hochladen und aktualisieren unter **Zielgruppe** > Nutzer importieren.

Der CSV-Nutzerimport unterstützt die Erfassung und das Update von Nutzer:innen-Attributen wie Vorname und E-Mail sowie angepasste Attribute wie Schuhgröße. Sie können eine CSV-Datei importieren, indem Sie einen von zwei eindeutigen Bezeichnern angeben: einen `external_id` oder einen Nutzer-Alias.

{% alert note %}
Wenn Sie eine Mischung aus Nutzern:innen mit `external_id` und Nutzern:innen ohne hochladen, müssen Sie für jeden Import eine CSV-Datei erstellen. Eine CSV-Datei kann nicht sowohl `external_ids` als auch Nutzer:innen-Aliase enthalten.
{% endalert %}

### Aufbau Ihrer CSV

In Braze gibt es mehrere Datentypen. Beim Importieren oder Aktualisieren von Nutzerprofilen mit einer CSV-Datei können Sie Standard Nutzerattribute oder angepasste Attribute erstellen oder aktualisieren.

- Standardattribute für Nutzer:innen sind reservierte Schlüssel in Braze. Zum Beispiel: `first_name` oder `email`.
- Angepasste Attribute sind an Ihr Unternehmen angepasst. Eine App für Reisebuchungen kann zum Beispiel ein angepasstes Attribut namens `last_destination_searched` haben.

{% alert important %}
Wenn Sie Kundendaten importieren, müssen die von Ihnen verwendeten Spaltenüberschriften genau mit der Schreibweise und Großschreibung der Standardattribute der Nutzer:innen übereinstimmen. Andernfalls erstellt Braze automatisch ein angepasstes Attribut im Profil des Nutzers:in.
{% endalert %}

Braze akzeptiert Nutzerdaten im Standard-CSV-Format aus Dateien mit einer Größe von bis zu 500 MB. Die herunterladbaren CSV-Templates finden Sie in den vorangegangenen Abschnitten zum Importieren.

#### Überlegungen zu Datenpunkten

Jede aus einer CSV-Datei importierte Kundendaten überschreibt den vorhandenen Wert in den Nutzerprofilen und zählt als Datenpunkt, mit Ausnahme von externen IDs und leeren Werten. 

- Externe IDs, die aus einer CSV-Datei hochgeladen werden, verbrauchen keine Datenpunkte. Wenn Sie eine CSV-Datei hochladen, um bestehende Braze Nutzer:innen zu segmentieren, indem Sie nur externe IDs hochladen, können Sie dies tun, ohne Datenpunkte zu verbrauchen. Wenn Sie zusätzliche Daten wie E-Mails oder Telefonnummern von Nutzern:innen in Ihren Import einfügen würden, würde dies die vorhandenen Nutzerdaten überschreiben und Ihre Datenpunkte verbrauchen.
  - Bei CSV-Importen zum Zwecke der Segmentierung (Importe mit `external_id`, `braze_id` oder `user_alias_name` als einzigem Feld) werden keine Datenpunkte verbraucht.
- Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Attribute der Nutzer:innen in Ihre CSV-Datei aufnehmen.
- Das Update von `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` wird nicht auf den Verbrauch von Datenpunkten angerechnet.

{% alert important %}
Wenn Sie `language` oder `country` für einen Nutzer:innen über den CSV-Import oder die API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden.
{% endalert %}

#### Standard Nutzerdaten Spaltenüberschriften

| FELD NUTZERPROFIL | DATENTYP | INFORMATIONEN | PFLICHTANGABE |
|---|---|---|---|
| `external_id` | String | Ein eindeutiger Bezeichner für Ihre Nutzer:innen. | Ja, siehe die folgende Notiz |
| `user_alias_name` | String | Ein eindeutiger Bezeichner für anonyme Nutzer:innen. Eine Alternative zum `external_id`. | Nein, siehe die folgende Notiz |
| `user_alias_label` | String | Eine allgemeine Bezeichnung, mit der Nutzer:in gruppiert werden können. | Ja, wenn `user_alias_name` verwendet wird. |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z.B. `Jane`). | Kein:e |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z.B. `Doe`). | Kein:e |
| `email` | String | Die E-Mail Ihrer Nutzer:innen, wie sie sie angegeben haben (z.B. `jane.doe@braze.com`). | Kein:e |
| `country` | String | Ländercodes müssen an Braze im ISO-3166-1 alpha-2 Standard übergeben werden (z.B. `GB`). | Kein:e |
| `dob` | String | Muss im Format "JJJJ-MM-TT" übergeben werden (zum Beispiel `1980-12-21`). Dadurch wird das Geburtsdatum Ihrer Nutzer:innen importiert und Sie können Nutzer:innen, die "heute" Geburtstag haben, als Zielgruppe zusammenstellen. | Kein:e |
| `gender` | String | "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen) oder Null (unbekannt). | Kein:e |
| `home_city` | String | Der Ort, den Ihre Nutzer:innen angegeben haben (z.B. `London`). | Kein:e |
| `language` | String | Die Sprache muss im ISO-639-1-Standard an Braze übergeben werden (z.B. `en`). <br>Sehen Sie sich unsere [Liste der akzeptierten Sprachen][1] an. | Kein:e |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im Format `E.164` (z.B. `+442071838750`). <br> Hinweise zur Formatierung finden Sie unter [Nutzer:innen-Telefonnummern][2]. | Kein:e |
| `email_open_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert.  Setzen Sie diese Option auf true, um zu verhindern, dass das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails, die an diese Nutzer:innen gesendet werden, hinzugefügt wird.   | Kein:e |
| `email_click_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert.  Setzen Sie diese Option auf true, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen zu deaktivieren. | Kein:e |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Erhalt von E-Mail-Nachrichten registriert), `unsubscribed` (explizit gegen den Erhalt von E-Mail-Nachrichten) und `subscribed` (weder opt-in noch opt-out). | Kein:e |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit gegen Push-Nachrichten) und `subscribed` (weder Opt-in noch Opt-out). | Kein:e |
| `time_zone` | String | Die Zeitzone muss Braze im gleichen Format wie die IANA-Zeitzonendatenbank übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`).  | Kein:e |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Kann in einem der folgenden ISO 8601-Formate übergeben werden: {::nomarkdown} <ul> <li> "JJJJ-MM-TT" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "JJJJ-MM-TTH:MM:SSZ" </li> <li> "JJJJ-MM-TTTHH:MM:SS" (zum Beispiel 2019-11-20T18:38:57) </li> </ul> {:/} | Kein:e |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Diesen Bezeichner finden Sie auf der Seite der Abo-Gruppe in Ihrem Dashboard. | Kein:e |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Während `external_id` selbst kein Pflichtfeld ist, **müssen** Sie eines dieser Felder angeben:
- `external_id`: Ein eindeutiger Bezeichner für Ihre Nutzer:innen <br> \- ODER -
- `braze_id`: Ein eindeutiger Bezeichner für bestehende Nutzer:innen von Braze <br> \- ODER -
- `user_alias_name`: Ein eindeutiger Bezeichner für einen anonymen Nutzer:in
{% endalert %}

### Importieren einer CSV-Datei

Um Ihre CSV-Datei zu importieren, gehen Sie zu **Zielgruppen** > Nutzer:innen-Import. Hier finden Sie eine Tabelle, in der die letzten Importe aufgelistet sind. Sie enthält Details wie das Upload-Datum, den Namen des Uploaders, den Dateinamen, die Targeting-Verfügbarkeit, die Anzahl der importierten Zeilen und den Status der einzelnen Importe.

![Die Seite 'Nutzer:innen importieren' im Braze-Dashboard.][3]

Wählen Sie **Dateien durchsuchen** und Ihre Datei. Braze lädt Ihre Datei hoch und überprüft die Spaltenüberschriften und die Datentypen der einzelnen Spalten.

Um eine CSV-Vorlage herunterzuladen, lesen Sie bitte die Abschnitte [Importieren mit externer ID](#importing-with-external-id) oder [Importieren mit Nutzer-Alias](#importing-with-user-alias) auf dieser Seite.

{% alert important %}
Beim CSV-Import wird zwischen Groß- und Kleinschreibung unterschieden. Das bedeutet, dass Großbuchstaben in CSV-Importen das Feld als angepasstes Attribut anstelle eines Standardattributs schreiben. Zum Beispiel ist "E-Mail" korrekt, aber "E-Mail" würde als angepasstes Attribut geschrieben werden.
{% endalert %}

Nachdem der Upload abgeschlossen ist, sehen Sie ein Modal mit einer Vorschau auf den Inhalt Ihrer Datei. Alle Informationen in dieser Tabelle beruhen auf den Werten in den oberen Zeilen Ihrer CSV-Datei. Bei Spaltenüberschriften werden Standardattribute in normalem Text geschrieben, während angepasste Attribute kursiv geschrieben sind und ihr Typ in Klammern angegeben wird. Im oberen Teil des Popup-Fensters finden Sie außerdem eine Zusammenfassung Ihrer Datei.

Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe laufen gleichzeitig ab, so dass die Reihenfolge der Updates nicht garantiert seriell ist. Wenn Sie möchten, dass die CSV-Importe nacheinander ausgeführt werden, warten Sie, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.

Wenn Braze während des Hochladens einen Fehler in Ihrer Datei feststellt, werden diese Fehler in der Zusammenfassung angezeigt. Wenn Ihre Datei beispielsweise eine fehlerhafte Zeile enthält, wird dieser Fehler in der Vorschau angezeigt, wenn Sie die Datei importieren. Eine Datei kann also mit Fehlern importiert werden, aber ein Import kann nicht abgebrochen oder rückgängig gemacht werden, nachdem er gestartet wurde. Überprüfen Sie die Vorschau, und wenn Sie Fehler finden, brechen Sie den Import ab und ändern Sie Ihre Datei. 

{% alert important %}
Prüfen Sie die vollständige CSV-Datei vor dem Hochladen, da Braze nicht jede Zeile der Eingabedatei für die Vorschau durchsucht. Das bedeutet, dass es Fehler geben kann, die Braze bei der Erstellung dieser Vorschau nicht erkennt.
{% endalert %}

Fehlerhafte Zeilen und Zeilen, die keine externe ID haben, werden nicht importiert. Alle anderen Fehler können importiert werden, stören aber möglicherweise die Filterung bei der Erstellung eines Segments. Weitere Informationen finden Sie im Abschnitt [Fehlerbehebung](#troubleshooting).

![CSV-Upload mit Fehlern bei gemischten Datentypen in einer einzelnen Spalte abgeschlossen][4]{: style="max-width:70%"}

{% alert warning %}
Die Fehler basieren ausschließlich auf dem Datentyp und der Dateistruktur. Eine schlecht formatierte E-Mail Adresse würde beispielsweise trotzdem importiert werden, da sie immer noch als String geparst werden kann.
{% endalert %}

Wenn Sie mit dem Upload zufrieden sind, starten Sie den Import. Das Popup-Fenster wird geschlossen und der Import beginnt im Hintergrund. Sie können den Fortschritt auf der Seite **Nutzerimport** verfolgen, die alle fünf Sekunden aktualisiert wird, oder wenn Sie auf den Button Aktualisieren im Feld **Letzte Importe** klicken.

Unter **Verarbeitete Zeilen** sehen Sie den Fortschritt des Imports; der Status ändert sich zu **Vollständig**, wenn er abgeschlossen ist. Sie können den Rest des Braze-Dashboards während des Imports weiterhin nutzen und Sie erhalten Benachrichtigungen, wenn der Import beginnt und endet.

Wenn der Importvorgang auf einen Fehler stößt, wird neben der Gesamtzahl der Zeilen in der Datei ein gelbes Warnsymbol angezeigt. Sie können mit dem Mauszeiger über das Symbol fahren, um Details darüber zu sehen, warum bestimmte Zeilen fehlgeschlagen sind. Nach Abschluss des Imports werden alle Daten zu den bestehenden Profilen hinzugefügt oder es werden neue Profile erstellt.

### Importieren mit externer ID

Wenn Sie Ihre Kundendaten importieren, müssen Sie den eindeutigen Bezeichner für jede Kund:in angeben (`external_id`). Bevor Sie mit dem CSV-Import beginnen, sollten Sie mit Ihrem Entwicklerteam klären, wie die Nutzer:innen in Braze identifiziert werden sollen. In der Regel handelt es sich dabei um eine interne Datenbank-ID. Dies sollte mit der Art und Weise übereinstimmen, wie Nutzer:innen durch das Braze SDK auf dem Handy und im Internet identifiziert werden, und ist so konzipiert, dass jeder Kund:in ein einziges Nutzerprofil innerhalb von Braze auf allen Geräten hat. Lesen Sie mehr über den Braze [Nutzerprofil-Lebenszyklus][13].

Wenn Sie in Ihrem Import einen `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `external_id` oder erstellt einen neu identifizierten Nutzer:in mit diesem `external_id` Satz, wenn kein solcher gefunden wird.

**Herunterladen:** [CSV-Importvorlage][template]

### Importieren mit Nutzer:innen-Alias

Um Nutzer:innen zusammenzustellen, die keinen `external_id` haben, können Sie eine Liste von Nutzer:innen mit User-Aliasing importieren. Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:in und kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:in zu vermarkten, die sich nicht bei Ihrer App angemeldet oder ein Konto erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur Alias sind, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `user_alias_name`: Ein eindeutiger Bezeichner für Nutzer:innen; eine Alternative zum `external_id`
- `user_alias_label`: Ein gemeinsames Label, mit dem Nutzer:in gruppiert werden können.

| user_alias_name | user_alias_label | last_name | E-Mail | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Schmidt | smith@user.com | WAHR |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSCH |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Wenn Sie in Ihrem Import sowohl `user_alias_name` als auch `user_alias_label` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wenn ein Nutzer:innen nicht gefunden wird, erstellt Braze einen neu identifizierten Nutzer:innen mit dem Satz `user_alias_name`.

{% alert important %}
Sie können keinen CSV-Import verwenden, um einen bestehenden Nutzer:in mit einer `user_alias_name` zu aktualisieren, wenn dieser bereits eine `external_id` hat. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um einen reinen Alias-Benutzer mit einem `external_id` zu verknüpfen, verwenden Sie den [Endpunkt Nutzer:innen identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

**Herunterladen:** [CSV Alias Import Template][template_alias]

### Importieren mit Braze ID

Um bestehende Nutzerprofile in Braze zu aktualisieren, indem Sie einen internen ID-Wert von Braze anstelle eines `external_id` oder `user_alias_name` und `user_alias_label` Wertes verwenden, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über unsere CSV-Exportoption im Rahmen der Segmentierung exportiert haben und ein neues angepasstes Attribut zu diesen bestehenden Nutzer:innen hinzufügen möchten.

{% alert important %}
Sie können keinen CSV-Import verwenden, um mit `braze_id` einen neuen Nutzer:innen anzulegen. Diese Methode kann nur zum Update bereits bestehender Nutzer:innen innerhalb der Braze-Plattform verwendet werden.
{% endalert %}

{% alert tip %}
Der Wert `braze_id` kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` gekennzeichnet sein. Diese ID entspricht der `braze_id` für einen Nutzer:innen, so dass Sie diese Spalte in `braze_id` umbenennen können, wenn Sie die CSV erneut importieren.
{% endalert %}

### Importieren mit E-Mail-Adressen und Telefonnummern

Sie können eine externe ID oder einen Nutzer-Alias weglassen und entweder eine E-Mail Adresse oder eine Telefonnummer verwenden, um Nutzer:innen zu importieren. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, überprüfen Sie Folgendes:

- Überprüfen Sie, dass Sie keine externen IDs oder User-Aliases für diese Profile in Ihrer CSV-Datei haben. Wenn Sie dies tun, verwendet Braze zur Identifizierung von Profilen vorrangig die externe ID oder den Nutzer-Alias vor der E-Mail Adresse.
- Vergewissern Sie sich, dass Ihre CSV-Datei richtig formatiert ist.

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihre CSV-Datei aufnehmen, wird die E-Mail-Adresse bei der Suche nach Profilen gegenüber der Telefonnummer bevorzugt behandelt.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail Adresse oder Telefonnummer hat, wird dieses Profil aktualisiert und Braze erstellt kein neues Profil. Wenn es mehrere Profile mit der gleichen E-Mail Adresse gibt, verwendet Braze die gleiche Logik wie der [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), wobei das zuletzt aktualisierte Profil aktualisiert wird.

Wenn ein Profil mit dieser E-Mail Adresse oder Telefonnummer nicht existiert, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [Endpunkt`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) verwenden, um dieses Profil später zu identifizieren. Um ein Nutzerprofil zu löschen, können Sie auch den [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) Endpunkt verwenden.

### Importieren angepasster Daten

Bei Kopfzeilen, die nicht genau mit den Standard Nutzerdaten übereinstimmen, wird in Braze ein angepasstes Attribut erstellt.

Die folgenden Datentypen werden beim Nutzer:innen-Import akzeptiert:
- **Datum:** Muss im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) gespeichert werden
- **Boolesch:** `true` oder `false`
- **Nummer:** Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommas, bei Gleitkommazahlen muss ein Punkt (`.`) als Dezimaltrennzeichen verwendet werden
- **String:** Kann Kommas enthalten, wenn der Spaltenwert von doppelten Anführungszeichen (`""`) umgeben ist.
- **Blank:** Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Attribute der Nutzer:innen in Ihre CSV-Datei aufnehmen.

{% alert important %}
Arrays, Push-Token und angepasste Event-Datentypen werden beim Nutzerimport nicht unterstützt.
Insbesondere bei Arrays werden Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert, so dass jegliche Kommas in Werten zu Fehlern beim Parsen der Datei führen.<br><br>Um diese Art von Werten hochzuladen, verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %}

### Lambda Nutzer:innen-CSV-Nutzerimport

Sie können unser serverloses S3 Lambda CSV-Import-Skript verwenden, um Nutzer:innen-Attribute auf die Plattform hochzuladen. Diese Lösung funktioniert wie ein CSV-Uploader, bei dem Sie Ihre CSV-Dateien in einem S3-Bucket ablegen und die Skripte sie über unsere API hochladen.

Die geschätzte Ausführungszeit für eine Datei mit 1.000.000 Zeilen sollte etwa fünf Minuten betragen. Weitere Informationen finden Sie unter [Nutzer:innen-Attribute CSV-Nutzerimport]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

### Update des Abo-Gruppenstatus

Sie können Nutzer:innen durch Nutzerimport zu E-Mail- oder SMS-Abo-Gruppen hinzufügen. Dies ist vor allem für SMS nützlich, da ein Nutzer:innen in einer Abo-Gruppe für SMS eingeschrieben sein muss, um über den Messaging-Kanal Nachrichten zu erhalten. Weitere Informationen finden Sie unter [SMS Abo-Gruppen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Wenn Sie den Status von Abo-Gruppen aktualisieren, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `subscription_group_id`: Die `id` der [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">abonniert</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">abonniert</td>
  </tr>
</tbody>
</table>

{% alert important %}
Im Nutzerimport kann nur eine einzige `subscription_group_id` pro Zeile eingestellt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id` Werte haben. Wenn Sie jedoch dieselben Nutzer:innen in mehreren Abo-Gruppen anmelden möchten, müssen Sie mehrere Importe durchführen.
{% endalert %}

## Erstellen eines Retargeting-Filters aus einem Nutzer:in-Import

Mit dem Nutzerimport können Sie die CSV-Datei in einen Retargeting-Filter umwandeln, indem Sie **Nutzer:innen in dieser CSV-Datei** auswählen **und es ermöglichen, diese bestimmte Gruppe von Nutzern als Retargeting** zu verwenden. Um nach der Datei in einem Segment oder überall dort zu filtern, wo eine Filterung möglich ist, wählen Sie den Filter **Aktualisiert/Importiert aus CSV** und suchen dann nach dem genauen Namen der Datei.

![Eine Filtergruppe mit dem Filter "Aktualisiert/Importiert aus CSV" einschließlich einer CSV-Datei mit dem Titel "Halloween-Saisonspaß".][5]

## Segmente aus einem Nutzer:in-Import erstellen

Der Nutzerimport kann auch zur Erstellung von Segmenten verwendet werden, indem Sie **Nutzer:innen aus dieser CSV-Datei** auswählen **und das Retargeting dieser speziellen Gruppe von Nutzern ermöglichen**. Aktivieren Sie dazu die Option **Automatisch ein Segment aus den Nutzern:innen erstellen,** bevor Sie den Import starten.

Sie können den Namen des Segments festlegen oder den Standard akzeptieren, der der Name Ihrer Datei ist. Dateien, die zur Erstellung eines Segments verwendet wurden, haben einen Link, über den Sie das Segment nach Abschluss des Imports ansehen können.

Der Filter, der zur Erstellung des Segments verwendet wird, wählt Nutzer:innen aus, die bei einem ausgewählten Import erstellt oder aktualisiert wurden, und ist mit allen anderen Filtern auf der Seite Segmentierung bearbeiten verfügbar.

## Überlegungen

{% multi_lang_include email-via-sms-warning.md %}

## Fehlerbehebung

###  Upload mit Fehlern abgeschlossen

#### Deformierte Zeile

Um Daten korrekt zu importieren, muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl von Zellen haben wie die Kopfzeile. Zeilen mit einer Länge von mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen. Außerdem müssen alle Daten in UTF-8 kodiert sein.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert werden, als insgesamt in der CSV-Datei enthalten sind, deutet dies möglicherweise nicht auf ein Problem mit dem Import hin, da die leeren Zeilen nicht importiert werden müssten. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie zu importieren versuchen.

#### Ungültige E-Mail-Adressen

Braze hat ungültige verschlüsselte E-Mail-Adressen entdeckt. Vergewissern Sie sich, dass alle E-Mail-Adressen ordnungsgemäß verschlüsselt sind, bevor Sie sie in Braze importieren.

- **Wenn Sie eine [E-Mail-Adresse in Braze aktualisieren oder importieren]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)**, verwenden Sie den gehashten E-Mail-Wert, wenn eine E-Mail enthalten ist. Diese Hash-E-Mail-Werte werden von Ihrem internen Team bereitgestellt. 
- **Wenn Sie einen neuen Nutzer:innen anlegen**, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert des Nutzers hinzufügen. Andernfalls wird der Nutzer:in nicht erstellt. Ähnlich verhält es sich, wenn Sie einem Nutzer:innen, der noch keine E-Mail hat, eine E-Mail-Adresse hinzufügen, müssen Sie `email_encrypted` hinzufügen. Andernfalls wird der Nutzer:innen nicht aktualisiert.

### Fehlende Zeilen

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen könnte:

- **Doppelte externe IDs, User-Aliasing, Braze IDs, E-Mail-Adressen oder Telefonnummern:** Wenn es doppelte externe ID-Spalten gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, selbst wenn die Zeilen korrekt formatiert sind. In einigen Fällen kann es vorkommen, dass kein bestimmter Fehler gemeldet wird. Prüfen Sie, ob es doppelte externe IDs in Ihrer CSV-Datei gibt. Wenn ja, entfernen Sie die Duplikate und versuchen Sie, sie erneut hochzuladen.
- **Akzentuierte Zeichen:** Ihre CSV-Datei kann Namen oder Attribute haben, die Akzente enthalten. Stellen Sie sicher, dass Ihre Datei UTF-8 kodiert ist, um Probleme zu vermeiden.
- **Braze ID gehört zu einem verwaisten Nutzer:innen:** Wenn ein Nutzer:innen verwaist ist, kann der verbleibende Nutzer, mit dem der Waise zusammengelegt wurde, die Braze ID des verwaisten Nutzers nicht mit dem Profil verknüpfen. In diesem Fall findet Braze keinen Nutzer:in zum Update, so dass die Zeile nicht als importiert gilt.
- **Leere Zeile:** Es gibt eine leere Zeile in der CSV-Datei. Sie können dies überprüfen, indem Sie die CSV-Datei in einem Texteditor öffnen (verwenden Sie nicht Excel oder Sheets). Wenn Sie die CSV-Datei mit einer leeren Zeile hochladen, erhalten Sie eine Fehlermeldung, die besagt, dass es Zeilen mit fehlerhaften Daten gibt.
- **Einschließlich doppelter Anführungszeichen (`"`):** Dieses Zeichen ist nicht gültig und macht die Zeile fehlerhaft. Verwenden Sie stattdessen einfache Anführungszeichen (`'`).
- **Inkonsistente Zeilenumbrüche:** Wenn die CSV-Datei beispielsweise `\n` für die erste Zeile und `\r\n` für jede weitere Zeile verwendet, wird die erste Zeile der Daten als Teil der Kopfzeile verarbeitet, und diese Daten werden nicht wie erwartet importiert. Sie können dies in einem Hex-Editor oder einem speziellen Texteditor, der Leerzeichen unterscheidet, überprüfen.
- **Falsch kodierte Datei:** Die CSV-Datei kann Namen oder Attribute mit Akzenten enthalten, aber die Datei muss in UTF-8 kodiert sein, um sie korrekt zu importieren. Andere Zeichenkodierungen können in manchen Instanzen funktionieren, aber nur UTF-8 ist vollständig kompatibel.

### Falsch formatierte Daten

Daten, die nicht im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) vorliegen, werden beim Import nicht als `datetimes` gelesen.

### String Zitat

Werte, die in einfache (`''`) oder doppelte (`""`) Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

### Als angepasstes Attribut importierte Daten

Wenn ein Teil der Standard Nutzerdaten (wie `email` oder `first_name`) als angepasstes Attribut importiert wird, überprüfen Sie die Groß- und Kleinschreibung Ihrer CSV-Datei. Zum Beispiel würde `First_name` als angepasstes Attribut importiert werden, während `first_name` korrekt in das Feld "Vorname" im Profil eines Nutzers importiert werden würde.

### Mehrere Datentypen

Braze erwartet, dass jeder Wert in einer Spalte vom gleichen Datentyp ist. Werte, die nicht mit dem Datentyp ihres Attributs übereinstimmen, führen zu Fehlern bei der Segmentierung.

Wenn Sie ein Zahlenattribut mit einer Null beginnen, gibt es außerdem Probleme, da Zahlen, die mit Nullen beginnen, als Strings betrachtet werden. Wenn Braze diesen String konvertiert, kann er wie ein Oktalwert behandelt werden (der Ziffern von null bis sieben verwendet), d.h. er wird in den entsprechenden Dezimalwert umgewandelt. Wenn der Wert in der CSV-Datei z.B. 0130 lautet, zeigt das Profil Braze 88 an. Um dieses Problem zu vermeiden, verwenden Sie Attribute mit String-Datentypen. Dieser Datentyp ist jedoch im Nummernvergleich der Segmentierung nicht verfügbar.

### Standardattribut-Typen

Einige Standardattribute akzeptieren nur bestimmte Werte als gültig für Nutzer:innen-Updates. Eine Anleitung dazu finden Sie unter [Erstellen Ihrer CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Nachfolgende Leerzeichen und Unterschiede in der Großschreibung können dazu führen, dass ein Wert als ungültig interpretiert wird. In der folgenden CSV-Datei werden beispielsweise nur die E-Mail- und Push-Status der Nutzer:innen in der ersten Zeile (`brazetest1`) erfolgreich aktualisiert, da die akzeptierten Werte `unsubscribed`, `subscribed` und `opted_in` sind. 

```
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### Der Button "CSV-Datei auswählen" funktioniert nicht

Es gibt mehrere Gründe, warum der Button **CSV-Datei auswählen** nicht funktioniert:

- **Popup-Blocker:** Dies kann dazu führen, dass die Seite nicht angezeigt wird. Vergewissern Sie sich, dass Ihr Browser Pop-ups auf der Braze-Dashboard Website zulässt. 
- **Veralteter Browser:** Vergewissern Sie sich, dass Ihr Browser auf dem neuesten Stand ist; falls nicht, aktualisieren Sie ihn auf die neueste Version.
- **Hintergrundprozesse:** Schließen Sie alle Instanzen des Browsers und starten Sie Ihren Computer neu.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/csvfilter.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[Fehler]:#common-errors
[Template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
