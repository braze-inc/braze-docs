---
nav_title: Nutzerimport
article_title: Nutzerimport
page_order: 4
page_type: reference
description: "Dieser Artikel referenziert den Import von Nutzer:innen in Ihr Braze-Dashboard mit Hilfe der REST API, Cloud Data Ingestion, CSV und bewährten Verfahren für den Import."

---
# Nutzer:in importieren

> Braze bietet verschiedene Möglichkeiten, Nutzerdaten in die Plattform zu importieren: SDKs, APIs, Datenaufnahme in die Cloud, Partnerintegrationen und CSV.

Bevor Sie fortfahren, beachten Sie bitte, dass Braze die HTML-Daten beim Import nicht bereinigt (validiert oder korrekt formatiert). Das bedeutet, dass Script-Tags der importierten Daten für die Web-Personalisierung entfernt werden müssen.

Wenn Sie Daten in Braze importieren, die ausdrücklich für die Personalisierung in einem Webbrowser bestimmt sind, entfernen Sie alle HTML-, JavaScript- und sonstigen Tags, da diese bei der Darstellung im Webbrowser für böse Absichten genutzt werden könnten.  

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

Verwenden Sie den [`/users/track` Endpunkt][12], um nutzerspezifische angepasste Events, Nutzerattribute und Käufe zu erfassen.

## Cloud-Datenaufnahme

Verwenden Sie Braze [Cloud Data Ingestion][14], um Nutzerattribute zu importieren und zu verwalten. 

## CSV-Import

Sie können Nutzerprofile über CSV-Dateien hochladen und aktualisieren unter **Zielgruppe** > Nutzer importieren.

Der CSV-Nutzerimport unterstützt die Erfassung und das Update von Nutzer:innen-Attributen wie Vorname und E-Mail sowie angepasste Attribute wie Schuhgröße. Sie können eine CSV-Datei importieren, indem Sie eine eindeutige `external_id` oder einen Nutzer-Alias angeben.

{% alert note %}
Wenn Sie eine Mischung aus Nutzern:innen mit `external_id` und Nutzern:innen ohne hochladen, müssen Sie für jeden Import eine CSV-Datei erstellen. Eine CSV-Datei kann nicht sowohl `external_ids` als auch Nutzer:innen-Aliase enthalten.
{% endalert %}

### CSV-Datei erstellen

In Braze gibt es mehrere Datentypen. Beim Importieren oder Aktualisieren von Nutzerprofilen mit einer CSV-Datei können Sie Standard Nutzerattribute oder angepasste Attribute erstellen oder aktualisieren.

- Standardattribute für Nutzer:innen sind reservierte Schlüssel in Braze. Zum Beispiel: `first_name` oder `email`.
- Angepasste Attribute sind an Ihr Unternehmen angepasst. Eine App für Reisebuchungen kann zum Beispiel ein angepasstes Attribut namens `last_destination_searched` haben.

{% alert important %}
Wenn Sie Kundendaten importieren, müssen die von Ihnen verwendeten Spaltenüberschriften genau mit der Schreibweise und Großschreibung der Standardattribute der Nutzer:innen übereinstimmen. Andernfalls erstellt Braze automatisch ein angepasstes Attribut im Profil des Nutzers:in.
{% endalert %}

Braze akzeptiert Nutzerdateien im CSV-Format bis 500 MB. Die herunterladbaren CSV-Templates finden Sie in den vorangegangenen Abschnitten zum Importieren.

#### Überlegungen zu Datenpunkten

Jede aus einer CSV-Datei importierte Kundendaten überschreibt den vorhandenen Wert in den Nutzerprofilen und zählt als Datenpunkt, mit Ausnahme von externen IDs und leeren Werten. 

- Externe IDs, die aus einer CSV-Datei hochgeladen werden, verbrauchen keine Datenpunkte. Wenn Sie eine CSV-Datei hochladen, um bestehende Braze Nutzer:innen zu segmentieren, indem Sie nur externe IDs hochladen, können Sie dies tun, ohne Datenpunkte zu verbrauchen. Wenn Sie zusätzliche Daten wie E-Mails oder Telefonnummern von Nutzern:innen in Ihren Import einfügen würden, würde dies die vorhandenen Nutzerdaten überschreiben und Ihre Datenpunkte verbrauchen.
  - Bei CSV-Importen zum Zwecke der Segmentierung (Importe mit `external_id`, `braze_id` oder `user_alias_name` als einzigem Feld) werden keine Datenpunkte verbraucht.
- Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Attribute der Nutzer:innen in Ihre CSV-Datei aufnehmen.
- Änderungen an `email_subscribe`, `push_subscribe`, `subscription_group_id` und `subscription_state` werden nicht auf den Verbrauch von Datenpunkten angerechnet.

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
| `country` | String | Ländercodes müssen an Braze gemäß ISO-3166-1 alpha-2 übergeben werden (z.B. `GB`). | Kein:e |
| `dob` | String | Muss im Format "JJJJ-MM-TT" übergeben werden (zum Beispiel `1980-12-21`). Dadurch wird das Geburtsdatum Ihrer Nutzer:innen importiert und Sie können Nutzer:innen, die "heute" Geburtstag haben, als Zielgruppe zusammenstellen. | Kein:e |
| `gender` | String | "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (keine Angabe gewünscht) oder Null (unbekannt). | Kein:e |
| `home_city` | String | Der Ort, den Ihre Nutzer:innen angegeben haben (z.B. `London`). | Kein:e |
| `language` | String | Die Sprache muss gemäß ISO-639-1 an Braze übergeben werden (z.B. `en`). <br>Sehen Sie sich unsere [Liste der akzeptierten Sprachen][1] an. | Kein:e |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im Format `E.164` (z.B. `+442071838750`). <br> Hinweise zur Formatierung finden Sie unter [Nutzer:innen-Telefonnummern][2]. | Kein:e |
| `email_open_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert.  Setzen Sie diese Option auf true, um zu verhindern, dass das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails, die an diese Nutzer:innen gesendet werden, hinzugefügt wird.   | Kein:e |
| `email_click_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert.  Setzen Sie diese Option auf true, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen zu deaktivieren. | Kein:e |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (ausdrücklich für den Empfang von E-Mails angemeldet), `unsubscribed` (ausdrücklich keine E-Mails erwünscht) und `subscribed` (weder noch). | Kein:e |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (ausdrücklich für den Empfang von Push-Nachrichten angemeldet), `unsubscribed` (ausdrücklich keine Push-Nachrichten erwünscht) und `subscribed` (weder noch). | Kein:e |
| `time_zone` | String | Die Zeitzone muss Braze im gleichen Format wie die IANA-Zeitzonendatenbank übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`).  | Kein:e |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Kann in einem der folgenden ISO 8601-Formate übergeben werden: {::nomarkdown} <ul> <li> "JJJJ-MM-TT" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "JJJJ-MM-TTH:MM:SSZ" </li> <li> "JJJJ-MM-TTTHH:MM:SS" (zum Beispiel 2019-11-20T18:38:57) </li> </ul> {:/} | Kein:e |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Diesen Bezeichner finden Sie auf der Seite der Abo-Gruppe in Ihrem Dashboard. | Kein:e |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Während `external_id` selbst kein Pflichtfeld ist, **müssen** Sie eines der folgenden Felder angeben:
- `external_id`: Ein eindeutiger Bezeichner für Ihre Nutzer:innen <br> \- ODER -
- `braze_id`: Ein eindeutiger Bezeichner für bestehende Nutzer:innen von Braze <br> \- ODER -
- `user_alias_name`: Ein eindeutiger Bezeichner für einen anonymen Nutzer:in
{% endalert %}

### Importieren einer CSV-Datei

Um Ihre CSV-Datei zu importieren, gehen Sie auf **Zielgruppen** > Nutzerimport. Hier finden Sie eine Tabelle, in der die letzten Importe aufgelistet sind. Sie enthält Details wie das Upload-Datum, den Namen des Uploaders, den Dateinamen, die Targeting-Verfügbarkeit, die Anzahl der importierten Zeilen und den Status der einzelnen Importe.

![Die Seite 'Nutzer:innen importieren' im Braze-Dashboard.][3]

Wählen Sie **Dateien durchsuchen** und Ihre Datei. Braze lädt Ihre Datei hoch und überprüft die Spaltenüberschriften und die Datentypen der einzelnen Spalten.

Um eine CSV-Vorlage herunterzuladen, lesen Sie bitte die Abschnitte [Importieren mit externer ID](#importing-with-external-id) oder [Importieren mit Nutzer-Alias](#importing-with-user-alias) auf dieser Seite.

{% alert important %}
Beim CSV-Import wird zwischen Groß- und Kleinschreibung unterschieden. Das bedeutet, dass Großbuchstaben in CSV-Importen das Feld als angepasstes Attribut anstelle eines Standardattributs schreiben. Zum Beispiel ist "email" korrekt, aber "E-Mail" würde als angepasstes Attribut geschrieben.
{% endalert %}

Nach dem Upload sehen Sie ein Modal mit einer Inhaltsvorschau. Alle Informationen in dieser Tabelle beruhen auf den Werten in den ersten Zeilen der CSV-Datei. Bei Spaltenüberschriften werden Standardattribute in normalem Text geschrieben, während angepasste Attribute kursiv geschrieben sind und ihr Typ in Klammern angegeben wird. Im oberen Teil des Popup-Fensters finden Sie außerdem eine Zusammenfassung Ihrer Datei.

Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe erfolgen parallel zueinander, sodass die Aktualisierungen nicht unbedingt nacheinander erfolgen. Wenn Sie die CSV-Importe nacheinander ausgeführt werden sollen, warten Sie mit dem nächsten Upload ab, bis vorangegangene CSV-Import abgeschlossen ist.

Wenn Braze beim Upload Dateifehler feststellt, werden diese in der Zusammenfassung angezeigt. Wenn eine Datei beispielsweise eine fehlerhafte Zeile enthält, wird dieser Fehler in der Vorschau angezeigt, wenn Sie die Datei importieren. Dateien können also mit Fehlern importiert werden, aber Importe können nach dem Start nicht abgebrochen oder rückgängig gemacht werden. Überprüfen Sie die Vorschau, und wenn Sie Fehler finden, brechen Sie den Import ab und ändern Sie die Datei. 

{% alert important %}
Prüfen Sie die komplette CSV-Datei vor dem Upload, da Braze für die Vorschau nicht alle Zeilen der Eingabedatei durchsucht. Es kann also Fehler geben, die Braze bei der Erstellung der Vorschau nicht erkennt.
{% endalert %}

Fehlerhafte Zeilen und Zeilen, die keine externe ID haben, werden nicht importiert. Alle anderen Fehler können importiert werden, stören aber möglicherweise die Filterung bei der Erstellung eines Segments. Weitere Informationen finden Sie unter [Fehlerbehebung](#troubleshooting).

![CSV-Upload mit Fehlern bei gemischten Datentypen in einer einzelnen Spalte abgeschlossen][4]{: style="max-width:70%"}

{% alert warning %}
Die Fehler basieren ausschließlich auf dem Datentyp und der Dateistruktur. Eine schlecht formatierte E-Mail Adresse würde beispielsweise trotzdem importiert werden, da sie immer noch als String geparst werden kann.
{% endalert %}

Wenn Sie der Upload in Ordnung ist, starten Sie den Import. Das Popup-Fenster wird geschlossen und der Import beginnt im Hintergrund. Sie können den Fortschritt auf der Seite **Nutzerimport** verfolgen, die alle fünf Sekunden aktualisiert wird, oder wenn Sie auf den Button Aktualisieren im Feld **Letzte Importe** klicken.

Unter **Verarbeitete Zeilen** sehen Sie den Fortschritt des Imports; der Status ändert sich zu **Vollständig**, wenn er abgeschlossen ist. Sie können den Rest des Braze-Dashboards während des Imports weiterhin nutzen und Sie erhalten Benachrichtigungen, wenn der Import beginnt und endet.

Wenn der Importvorgang auf einen Fehler stößt, wird neben der Gesamtzahl der Zeilen in der Datei ein gelbes Warnsymbol angezeigt. Sie können mit dem Mauszeiger über das Symbol fahren, um Details darüber zu sehen, warum bestimmte Zeilen fehlgeschlagen sind. Nach Abschluss des Imports werden alle Daten zu den bestehenden Profilen hinzugefügt oder es werden neue Profile erstellt.

### Mit externer ID importieren

Wenn Sie Kundendaten importieren, müssen Sie immer einen eindeutigen Bezeichner angeben (`external_id`). Bevor Sie mit dem CSV-Import beginnen, sollten Sie mit Ihrem Entwicklerteam klären, wie die Nutzer:innen in Braze identifiziert werden sollen. In der Regel handelt es sich dabei um eine interne Datenbank-ID. Dies sollte mit der Art und Weise übereinstimmen, wie Nutzer:innen durch das Braze SDK auf dem Handy und im Internet identifiziert werden, und ist so konzipiert, dass jeder Kund:in ein einziges Nutzerprofil innerhalb von Braze auf allen Geräten hat. Lesen Sie mehr über [Nutzerprofile][13]] in Braze.

Wenn Sie in Ihrem Import einen `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `external_id` oder erstellt einen neu identifizierten Nutzer:in mit diesem `external_id` Satz, wenn kein solcher gefunden wird.

**Herunterladen:** [CSV-Importvorlage][template]

### Importieren mit Nutzer:innen-Alias

Um Nutzer:innen zusammenzustellen, die keinen `external_id` haben, können Sie eine Liste von Nutzer:innen mit User-Aliasing importieren. Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:in und kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:in zu vermarkten, die sich nicht bei Ihrer App angemeldet oder ein Konto erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur ein Alias enthalten, muss die CSV-Datei diese beiden Spalten enthalten:

- `user_alias_name`: Ein eindeutiger Bezeichner für Nutzer:innen; eine Alternative zum `external_id`
- `user_alias_label`: Ein gemeinsames Label, mit dem Nutzer:in gruppiert werden können.

| user_alias_name | user_alias_label | last_name | E-Mail | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Schmidt | smith@user.com | WAHR |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSCH |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Wenn Sie in Ihrem Import sowohl `user_alias_name` als auch `user_alias_label` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wenn ein Nutzer:innen nicht gefunden wird, erstellt Braze einen neu identifizierten Nutzer:innen mit dem Satz `user_alias_name`.

{% alert important %}
Der CSV-Import kann nicht zur Aktualisierung bestehender Nutzer:innen mit `user_alias_name` verwendet werden, wenn diese bereits eine `external_id` haben. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um reine Alias-Nutzer mit einer `external_id` zu verknüpfen, verwenden Sie den [Endpunkt Nutzererkennung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

**Herunterladen:** [CSV Alias Import Template][template_alias]

### Importieren mit Braze ID

Um bestehende Nutzerprofile mit einer Braze-ID statt mit `external_id` oder `user_alias_name` und `user_alias_label` zu aktualisieren, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über unsere CSV-Exportoption im Rahmen der Segmentierung exportiert haben und ein neues angepasstes Attribut zu diesen bestehenden Nutzer:innen hinzufügen möchten.

{% alert important %}
Sie können keinen CSV-Import verwenden, um mit `braze_id` einen neuen Nutzer:innen anzulegen. Diese Methode kann nur zum Update bereits bestehender Nutzer:innen innerhalb der Braze-Plattform verwendet werden.
{% endalert %}

{% alert tip %}
Der Wert `braze_id` ist in CSV-Exporten aus dem Braze-Dashboard u. U. mit `Appboy ID` gekennzeichnet. Diese ID entspricht der `braze_id` für einen Nutzer:innen, so dass Sie diese Spalte in `braze_id` umbenennen können, wenn Sie die CSV erneut importieren.
{% endalert %}

### Importieren mit E-Mail-Adressen und Telefonnummern

Sie können eine externe ID oder einen Benutzer-Alias weglassen und nur eine E-Mail-Adresse oder eine Telefonnummer zum Importieren von Benutzern verwenden. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, überprüfen Sie Folgendes:

- Stellen Sie sicher, dass keine externen IDs oder User-Aliase für diese Profile vorhanden sind.
- Stellen Sie sicher, dass Ihre CSV-Datei richtig formatiert ist.

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihre CSV-Datei aufnehmen, wird die E-Mail-Adresse bei der Suche nach Profilen gegenüber der Telefonnummer bevorzugt behandelt.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail Adresse oder Telefonnummer hat, wird dieses Profil aktualisiert und Braze erstellt kein neues Profil. Sind mehrere Profile mit derselben E-Mail Adresse vorhanden, verwendet Braze dieselbe Logik wie der [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), wobei das zuletzt aktualisierte Profil geändert wird.

Wenn ein Profil mit dieser E-Mail Adresse oder Telefonnummer nicht existiert, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [Endpunkt`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) verwenden, um dieses Profil später zu ermitteln. Um Nutzerprofile zu löschen, können Sie auch den [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) Endpunkt verwenden.

### Importieren angepasster Daten

Bei Kopfzeilen, die nicht genau mit den Standard Nutzerdaten übereinstimmen, wird in Braze ein angepasstes Attribut erstellt.

Die folgenden Datentypen werden beim Nutzer:innen-Import akzeptiert:
- **Datum:** Muss im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) gespeichert werden
- **Boolesch:** `true` oder `false`
- **Nummer:** Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommas, bei Gleitkommazahlen muss ein Punkt (`.`) als Dezimaltrennzeichen verwendet werden
- **String:** Kann Kommas enthalten, wenn der Spaltenwert von doppelten Anführungszeichen (`""`) umgeben ist.
- **Blank:** Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Attribute der Nutzer:innen in Ihre CSV-Datei aufnehmen.

{% alert important %}
Arrays, Push-Token und benutzerdefinierte Ereignisdatentypen werden beim Benutzerimport nicht unterstützt.
Insbesondere bei Arrays werden Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert, so dass alle Kommas in Werten zu Fehlern beim Parsen der Datei führen.<br><br>Um derartige Werte hochzuladen, verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Lambda Nutzer:innen-CSV-Nutzerimport

Mit unserem serverlosen Skript S3 Lambda für den CSV-Import können Sie Nutzerattribute auf die Plattform hochladen. Diese Lösung funktioniert wie ein CSV-Uploader, bei dem Sie Ihre CSV-Dateien in einem S3-Bucket ablegen und die Skripte sie über unsere API hochladen.

Die geschätzte Ausführungszeit für eine Datei mit 1.000.000 Zeilen sollte etwa fünf Minuten betragen. Weitere Informationen finden Sie unter [Nutzer:innen-Attribute CSV-Nutzerimport]({{site.baseurl}}/user_csv_lambda/).

### Status der Abonnementgruppe aktualisieren

Sie können Benutzer über den Benutzerimport zu E-Mail- oder SMS-Abonnementgruppen hinzufügen. Dies ist besonders nützlich für SMS, da ein Benutzer in einer SMS-Abonnementgruppe eingeschrieben sein muss, um über den SMS-Kanal benachrichtigt zu werden. Weitere Informationen finden Sie unter [SMS-Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Wenn Sie den Status einer Abo-Gruppe ändern, muss die CSV-Datei diese beiden Spalten enthalten:

- `subscription_group_id`: Die `id` der [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abonnementgruppe) oder `subscribed` (in der Abonnementgruppe).

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

## Erstellen von Segmenten aus einem Benutzerimport

Der Benutzerimport kann auch zur Erstellung von Segmenten verwendet werden, indem Sie vor dem Start des Imports die Option **Automatisch ein Segment aus den Benutzern erstellen, die aus dieser CSV importiert werden**, auswählen.

Sie können einen Segmentnamen festlegen oder den Standard übernehmen, der mit dem Dateinamen identisch ist. Bei Dateien, die zur Erstellung eines Segments verwendet worden sind, können Sie dieses Segment nach dem Import über einen Link ansehen.

Der Filter, der zur Erstellung des Segments verwendet wird, wählt Nutzer:innen aus, die bei einem ausgewählten Import erstellt oder aktualisiert wurden, und ist mit allen anderen Filtern auf der Seite Segmentierung bearbeiten verfügbar.

## Überlegungen

{% multi_lang_include email-via-sms-warning.md %}

## Fehlerbehebung

### Fehlende Zeilen

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen könnte:

- **Doppelte externe IDs:** Wenn es doppelte externe ID-Spalten gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, selbst wenn die Zeilen korrekt formatiert sind. In einigen Fällen kann es vorkommen, dass dies nicht als Fehler gemeldet wird. Prüfen Sie, ob die CSV-Datei doppelte externe IDs enthält. Falls ja, entfernen Sie die Doubletten und versuchen Sie den Upload erneut.
- **Akzentzeichen:** Ihre CSV-Datei kann Namen oder Attribute haben, die Akzente enthalten. Stellen Sie sicher, dass Ihre Datei UTF-8-kodiert ist, um Probleme zu vermeiden.

### Deformierte Zeilen

Um Daten korrekt zu importieren, muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl von Zellen haben wie die Kopfzeile. Zeilen mit einer Länge von mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen. Außerdem müssen alle Daten in UTF-8 kodiert sein.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert werden, als insgesamt in der CSV-Datei enthalten sind, deutet dies möglicherweise nicht auf ein Problem mit dem Import hin, da die leeren Zeilen nicht importiert werden müssten. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie zu importieren versuchen.

### Mehrere Datentypen

Braze erwartet alle Werte in einer Spalte in demselben Datentyp. Werte, die nicht mit dem Datentyp des jeweiligen Attributs übereinstimmen, führen zu Segmentierungsfehlern.

### Falsch formatierte Daten

Datumsangaben, die nicht im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) vorliegen, werden beim Import nicht als `datetimes` gelesen.

### Strings zitieren

Werte in einfachen (`''`) oder doppelten (`""`) Anführungszeichen werden beim Import als Strings erkannt.

### Als angepasstes Attribut importierte Daten

Wenn ein Teil der Standard Nutzerdaten (wie `email` oder `first_name`) als angepasstes Attribut importiert wird, überprüfen Sie die Groß- und Kleinschreibung Ihrer CSV-Datei. Zum Beispiel würde `First_name` als angepasstes Attribut importiert werden, während `first_name` korrekt in das Feld "Vorname" im Profil eines Nutzers importiert werden würde.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[Fehler]:#common-errors
[Template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
