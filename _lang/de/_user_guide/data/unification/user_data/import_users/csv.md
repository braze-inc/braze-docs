---
nav_title: Eine CSV verwenden
article_title: "CSV-Import"
description: "Erfahren Sie, wie Sie Nutzer-Attribute und angepasste Events mit Hilfe des CSV-Imports erfassen und aktualisieren können."
page_order: 1.2
---

# CSV-Import

> Erfahren Sie, wie Sie Nutzer-Attribute und angepasste Events mit Hilfe des CSV-Imports erfassen und aktualisieren können.

## Über CSV-Import

Mit dem CSV-Nutzerimport können Sie die folgenden Nutzer:innen-Attribute und angepassten Events erfassen und aktualisieren.

|Typ|Definition|Beispiel|Maximale Dateigröße|
|---|---|---|---|
|Standardattribute|Reservierte Nutzer:innen-Attribute, die von Braze erkannt werden.|`first_name`, `email`|500 MB|
|Angepasste Attribute|Eindeutige Attribute der Nutzer:innen für Ihr Unternehmen.|`last_destination_searched`|500 MB|
|Benutzerdefinierte Ereignisse|Eindeutige Ereignisse in Ihrem Unternehmen, die Nutzer:in darstellen.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSV-Import verwenden

### Schritt 1: CSV-Vorlage herunterladen

Um den CSV-Nutzerimport zu öffnen, gehen Sie zu **Zielgruppen** > Nutzer:innen importieren. Hier finden Sie eine Tabelle mit Details zu den letzten Importen, wie z.B. das Datum des Uploads, den Namen des Uploaders, den Dateinamen, die Verfügbarkeit des Targetings, die Anzahl der importierten Zeilen und den Status des Imports.

Um mit Ihrer CSV zu beginnen, laden Sie ein Template für Attribute oder Ereignisse herunter.

![Die Seite 'Nutzer:innen importieren' im Braze-Dashboard.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Schritt 2: Wählen Sie einen Bezeichner {#choose-an-identifier}

Die CSV-Datei, die Sie importieren, benötigt einen speziellen Bezeichner. Sie können aus den folgenden Angeboten wählen:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Wenn Sie Ihre Kundendaten importieren, können Sie eine `external_id` als eindeutigen Bezeichner für jede Kund:in verwenden. Wenn Sie in Ihrem Import einen `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `external_id` oder erstellt einen neu identifizierten Nutzer:in mit diesem `external_id` Satz, wenn kein solcher gefunden wird.

- Herunterladen: [CSV Attribute Import Vorlage: Externe ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Herunterladen: [CSV Events Import Template: Externe ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Wenn Sie eine Mischung aus Nutzern:innen mit `external_id` und Nutzern:innen ohne hochladen, müssen Sie für jeden Import eine CSV-Datei erstellen. Eine CSV-Datei kann nicht sowohl `external_ids` als auch Nutzer:innen-Aliase enthalten.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Um Nutzer:innen zusammenzustellen, die keinen `external_id` haben, können Sie eine Liste von Nutzer:innen mit User-Aliasing importieren. Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:in und kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:in zu vermarkten, die sich nicht bei Ihrer App angemeldet oder ein Konto erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur Alias sind, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `user_alias_name`: Ein eindeutiger Bezeichner für Nutzer:innen; eine Alternative zum `external_id`  
- `user_alias_label`: Ein gemeinsames Label, mit dem Nutzer:in gruppiert werden können.

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Schmidt | smith@user.com | WAHR |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSCH |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Wenn Sie in Ihrem Import sowohl `user_alias_name` als auch `user_alias_label` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wenn ein Nutzer:innen nicht gefunden wird, erstellt Braze einen neu identifizierten Nutzer:innen mit dem Satz `user_alias_name`.

{% alert important %}
Sie können keinen CSV-Import verwenden, um einen bestehenden Nutzer:in mit einer `user_alias_name` zu aktualisieren, wenn dieser bereits eine `external_id` hat. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um reine Alias-Nutzer mit einer `external_id` zu verknüpfen, verwenden Sie den [Endpunkt Nutzererkennung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Herunterladen: [CSV Attribute Import Vorlage: Nutzer:in Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Um bestehende Nutzerprofile in Braze zu aktualisieren, indem Sie einen internen ID-Wert von Braze anstelle eines `external_id` oder `user_alias_name` und `user_alias_label` Wertes verwenden, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über unsere CSV-Exportoption im Rahmen der Segmentierung exportiert haben und ein neues angepasstes Attribut zu diesen bestehenden Nutzer:innen hinzufügen möchten.

{% alert important %}
Sie können keinen CSV-Import verwenden, um mit `braze_id` einen neuen Nutzer:innen anzulegen. Diese Methode kann nur zum Update bereits bestehender Nutzer:innen innerhalb der Braze-Plattform verwendet werden.  
{% endalert %}

{% alert tip %}
Der Wert `braze_id` kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` gekennzeichnet sein. Diese ID entspricht der `braze_id` für einen Nutzer:innen, so dass Sie diese Spalte in `braze_id` umbenennen können, wenn Sie die CSV erneut importieren.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Sie können eine externe ID oder einen Nutzer-Alias weglassen und entweder eine E-Mail Adresse oder eine Telefonnummer verwenden, um Nutzer:innen zu importieren. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, überprüfen Sie Folgendes:

- Überprüfen Sie, dass Sie keine externen IDs oder User-Aliases für diese Profile in Ihrer CSV-Datei haben. Wenn Sie dies tun, verwendet Braze zur Identifizierung von Profilen vorrangig die externe ID oder den Nutzer-Alias vor der E-Mail Adresse.  
- Vergewissern Sie sich, dass Ihre CSV-Datei richtig formatiert ist.  

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihre CSV-Datei aufnehmen, wird die E-Mail-Adresse bei der Suche nach Profilen gegenüber der Telefonnummer bevorzugt behandelt.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail Adresse oder Telefonnummer hat, wird dieses Profil aktualisiert und Braze erstellt kein neues Profil. Sind mehrere Profile mit derselben E-Mail Adresse vorhanden, verwendet Braze dieselbe Logik wie der [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), wobei das zuletzt aktualisierte Profil geändert wird.

Wenn ein Profil mit dieser E-Mail Adresse oder Telefonnummer nicht existiert, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [Endpunkt`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) verwenden, um dieses Profil später zu ermitteln. Um Nutzerprofile zu löschen, können Sie auch den [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) Endpunkt verwenden.
{% endtab %}
{% endtabs %}

### Schritt 3: Erstellen Sie Ihre CSV-Datei

Sie können jeden der folgenden Datentypen als eine einzige CSV-Datei hochladen. Wenn Sie mehr als einen Datentyp hochladen möchten, laden Sie mehrere CSV-Dateien hoch.

- **Nutzer:innen Attribute:** Dazu gehören sowohl Standard- als auch angepasste Attribute der Nutzer:innen. Standard Benutzerattribute sind reservierte Schlüssel in Braze (z.B. `first_name` oder `email`) und angepasste Attribute sind eindeutige Benutzerattribute für Ihr Unternehmen (z.B. `last_destination_searched`).  
- **Angepasste Events:** Diese sind eindeutig auf Ihr Unternehmen bezogen und spiegeln die Aktionen wider, die ein Nutzer:innen durchgeführt hat, wie z.B. `trip_booked` für eine App zur Reisebuchung.

Wenn Sie bereit sind, mit der Erstellung Ihrer CSV-Datei zu beginnen, lesen Sie die folgenden Informationen:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Erforderliche Bezeichner {#required-identifiers-attributes}

`external_id` ist zwar nicht erforderlich, aber Sie **müssen** **einen** der folgenden Bezeichner als Kopfzeile in Ihre CSV-Datei einfügen. Einzelheiten zu den einzelnen [Bezeichnern](#choose-an-identifier) finden Sie unter [Wählen Sie einen Bezeichner](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Angepasste Attribute

Die folgenden Datenarten können als angepasste Attribute für den CSV-Import verwendet werden. Spaltenüberschriften, die nicht genau mit einem [Standardattribut](#default-attributes) übereinstimmen, werden in Braze mit einem angepassten Attribut versehen.

| Datentyp | Beschreibung |
|---|---|
| Datetime | Muss im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) gespeichert werden. |
| Boolesch | Akzeptiert `true` oder `false`. |
| Zahl | Muss eine Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommas sein. Gleitkommazahlen müssen einen Punkt (`.`) als Dezimaltrennzeichen verwenden. |
| String | Kann Kommas enthalten, wenn der Wert in doppelte Anführungszeichen eingeschlossen ist (`""`). |
| Leer | Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Attribute der Nutzer:innen in Ihre CSV-Datei aufnehmen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Arrays, Push-Tokens und angepasste Event-Datentypen werden beim Nutzerimport nicht unterstützt, da Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert werden und beim Parsen Ihrer Datei Fehler verursachen.<br><br>Um diese Art von Daten hochzuladen, verwenden Sie stattdessen den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Standardattribute

{% alert important %}
Wenn Sie Standardattribute importieren, müssen die von Ihnen verwendeten Spaltenüberschriften genau mit der Schreibweise und Großschreibung der Standardattribute der Nutzer:innen übereinstimmen. Andernfalls erkennt Braze diese stattdessen als [angepasste Attribute](#custom-attributes).
{% endalert %}

| Feld Nutzer:in | Datentyp | Beschreibung | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Bezeichner für Ihre Nutzer:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_name` | String | Ein eindeutiger Bezeichner für anonyme Nutzer:innen, der eine Alternative zu `external_id` darstellt. Muss mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_label` | String | Eine allgemeine Bezeichnung, mit der Nutzer:in gruppiert werden können. Muss mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z.B. `Jane`). | Kein:e |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z.B. `Doe`). | Kein:e |
| `email` | String | Die E-Mail Ihrer Nutzer:innen, wie sie sie angegeben haben (z.B. `jane.doe@braze.com`). | Kein:e |
| `country` | String | Ländercodes müssen an Braze im ISO-3166-1 alpha-2 Standard übergeben werden (z.B. `GB`). | Kein:e |
| `dob` | String | Muss im Format "JJJJ-MM-TT" übergeben werden (zum Beispiel `1980-12-21`). Dadurch wird das Geburtsdatum Ihrer Nutzer:innen importiert und Sie können Nutzer:innen, die "heute" Geburtstag haben, als Zielgruppe zusammenstellen. | Kein:e |
| `gender` | String | "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen) oder Null (unbekannt). | Kein:e |
| `home_city` | String | Der Ort, den Ihre Nutzer:innen angegeben haben (z.B. `London`). | Kein:e |
| `language` | String | Die Sprache muss gemäß ISO-639-1 an Braze übergeben werden (z.B. `en`). Sehen Sie sich unsere [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/) an. | Kein:e |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im Format `E.164` (z.B. `+442071838750`). Hinweise zur Formatierung finden Sie unter [Nutzer:innen-Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). | Kein:e |
| `email_open_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert. Setzen Sie diese Option auf true, um zu verhindern, dass das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails, die an diese Nutzer:innen gesendet werden, hinzugefügt wird. Nur für SparkPost und SendGrid verfügbar. | Kein:e |
| `email_click_tracking_disabled` | Boolesch | wahr oder falsch akzeptiert. Setzen Sie diese Option auf true, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen zu deaktivieren. Nur für SparkPost und SendGrid verfügbar. | Kein:e |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Erhalt von E-Mail-Nachrichten registriert), `unsubscribed` (explizit gegen den Erhalt von E-Mail-Nachrichten) und `subscribed` (weder opt-in noch opt-out). | Kein:e |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit gegen Push-Nachrichten) und `subscribed` (weder Opt-in noch Opt-out). | Kein:e |
| `time_zone` | String | Die Zeitzone muss Braze im gleichen Format wie die IANA-Zeitzonendatenbank übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`). | Kein:e |
| `date_of_first_session`  `date_of_last_session` | String | Kann in einem der folgenden ISO 8601-Formate übergeben werden: "JJJJ-MM-TT" "JJJJ-MM-TTTHH:MM:SS+00:00" "JJJJ-MM-TTTHH:MM:SSZ" "JJJJ-MM-TTTHH:MM:SS" (zum Beispiel 2019-11-20T18:38:57) | Kein:e |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Diesen Bezeichner finden Sie auf der Seite der Abo-Gruppe in Ihrem Dashboard. | Kein:e |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Update des Abo-Gruppenstatus (optional)

Außerdem können Sie Nutzer:innen durch Nutzerimport zu E-Mail- oder SMS-Abo-Gruppen hinzufügen. Dies ist vor allem für SMS nützlich, da ein Nutzer:innen in einer Abo-Gruppe für SMS eingeschrieben sein muss, um über den Messaging-Kanal Nachrichten zu erhalten. Weitere Informationen finden Sie unter [SMS Abo-Gruppen](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Wenn Sie den Status von Abo-Gruppen aktualisieren, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `subscription_group_id`: Die `id` der [Abo-Gruppe](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | abonniert |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | abonniert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Im Nutzerimport kann nur eine einzige `subscription_group_id` pro Zeile eingestellt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id` Werte haben. Wenn Sie jedoch dieselben Nutzer:innen in mehreren Abo-Gruppen anmelden möchten, müssen Sie mehrere Importe durchführen.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Erforderliche Bezeichner {#required-identifiers-custom-events}

`external_id` ist zwar nicht erforderlich, aber Sie **müssen** **einen** der folgenden Bezeichner als Kopfzeile in Ihre CSV-Datei einfügen. Einzelheiten zu den einzelnen [Bezeichnern](#choose-an-identifier) finden Sie unter [Wählen Sie einen Bezeichner](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Angepasste Event-Felder

Zusätzlich zu den folgenden Angaben kann Ihre CSV-Datei auch zusätzliche Spaltenüberschriften für Event-Eigenschaften enthalten. Diese Eigenschaften sollten eine Spaltenüberschrift haben von `<event_name>.properties.<property name>.`

Das angepasste Event `trip_booked` kann zum Beispiel die Eigenschaften `destination` und `duration` haben. Diese können importiert werden, indem Sie die Spaltenüberschriften `trip_booked.properties.destination` und `trip_booked.properties.duration` verwenden.

| Feld Nutzer:in | Datentyp | Informationen | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Bezeichner für Ihren Nutzer:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `braze_id` | String | Ein von Braze zugewiesener Bezeichner für Ihre Nutzer:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_name` | String | Ein eindeutiger Bezeichner für anonyme Nutzer:innen, der eine Alternative zu `external_id` darstellt. Muss mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_label` | String | Eine allgemeine Bezeichnung, mit der Nutzer:in gruppiert werden können. Muss mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `email` | String | Die E-Mail Ihrer Nutzer:innen, wie sie sie angegeben haben (z.B. `jane.doe@braze.com`). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe die folgende Anmerkung. |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im Format `E.164` (z.B. `+442071838750`). Hinweise zur Formatierung finden Sie unter [Nutzer:innen-Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe die folgende Anmerkung. |
| `name` | String | Ein angepasstes Event für Ihre Nutzer:innen. | Ja |
| `time` | String | Die Uhrzeit des Ereignisses. Kann in einem der folgenden ISO-8601-Formate übergeben werden: "JJJJ-MM-TT" "JJJJ-MM-TTTHH:MM:SS+00:00" "JJJJ-MM-TTTHH:MM:SSZ" "JJJJ-MM-TTTHH:MM:SS" (zum Beispiel 2019-11-20T18:38:57) | Ja |
| `<event name>.properties.<property name>` | Mehrere | Eine Eigenschaft, die mit einem angepassten Event verbunden ist. Ein Beispiel ist `trip_booked.properties.destination` | Kein:e |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Schritt 4: Hochladen und Vorschau Ihrer Daten

Bevor Braze Ihre CSV-Datei verarbeitet, generiert es eine Vorschau der ersten Zeilen, damit Sie diese auf eventuelle Probleme überprüfen können. Um Ihre Vorschau zu erstellen, wählen Sie **Attribute** oder **Ereignisse**, dann wählen Sie **Dateien durchsuchen** und laden Ihre CSV-Datei hoch. 

<!-- old image -->
![CSV-Upload abgeschlossen mit Fehlern bei gemischten Datentypen in einer einzelnen Spalte]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
Die Vorschau des Nutzerimports scannt nicht jede Zeile der Eingabedatei. Fehler nach den ersten paar Zeilen werden möglicherweise nicht erkannt, daher sollten Sie die CSV-Datei vollständig überprüfen.
{% endalert %}

### Schritt 5: Wählen Sie Targeting-Einstellungen

Sie können auch zwischen den folgenden Targeting-Einstellungen wählen. Wenn Sie keinen neuen Targeting-Filter oder ein neues Segment aus Ihrem Import erstellen müssen, wählen Sie **Diese Liste nicht als Targeting-Filter verfügbar machen**.

| Option | Beschreibung |
|---|---|
| Targeting Filter | Um Ihre CSV-Datei in eine Retargeting-Option für die Erstellung von Nutzersegmenten umzuwandeln, wählen Sie Ihre Datei aus dem Dropdown-Menü **Aktualisiert/Importiert aus CSV** aus und wählen dann **Targeting-Filter erstellen**. |
| Neue Segmente | Um auch ein neues Segment aus Ihrem neuen Targeting Filter zu erstellen, wählen Sie **Targeting Filter erstellen und zu neuem Segment hinzufügen**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine Filtergruppe mit dem Filter "Aktualisiert/Importiert aus CSV", die eine CSV-Datei mit dem Titel "Halloween-Saisonspaß" enthält.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Schritt 6: Starten Sie Ihren CSV-Import

Wenn Sie bereit sind, wählen Sie **Import starten**. Sie können den aktuellen Fortschritt auf der Seite **Nutzerimport** verfolgen, die automatisch alle fünf Sekunden aktualisiert wird.

Wenn es keine Probleme gibt, wird der Status auf **Vollständig** aktualisiert und die Anzahl der verarbeiteten Zeilen wird angezeigt. Alle Daten aus verarbeiteten Zeilen werden entweder zu bestehenden Profilen oder zu neu erstellten Profilen hinzugefügt.

{% alert note %}
Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe erfolgen parallel zueinander, sodass die Aktualisierungen nicht unbedingt nacheinander erfolgen. Wenn Sie möchten, dass die CSV-Importe nacheinander ausgeführt werden, warten Sie, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.
{% endalert %}

## Überlegungen zu Datenpunkten

Jede aus einer CSV-Datei importierte Kundendaten überschreibt den bestehenden Wert in den Nutzerprofilen und protokolliert einen Datenpunkt, außer bei externen IDs und leeren Werten. Wenn Sie Fragen zu den Datenpunkten von Braze haben, kann Ihr Braze-Konto Manager:in sie beantworten.

| Betrachtung | Details |
|---|---|
| Externe IDs | Wenn Sie eine CSV-Datei hochladen, die nur `external_id` enthält, werden keine Datenpunkte aufgezeichnet. Damit können Sie bestehende Nutzer:innen von Braze segmentieren, ohne die Daten zu beeinträchtigen. Wenn Sie jedoch Felder wie `email` oder `phone` hinzufügen, **werden** bestehende Nutzerdaten überschrieben und Datenpunkte protokolliert. <br><br>CSV-Importe, die nur zur Segmentierung verwendet werden, protokollieren keine Datenpunkte, wie z.B. solche, die nur `external_id`, `braze_id`, oder `user_alias_name` enthalten. |
| Leere Werte | Leere Werte in Ihrer CSV-Datei überschreiben keine bestehenden Nutzerprofil-Daten. Sie müssen nicht alle Nutzer:in-Attribute oder angepasste Events beim Importieren mit einbeziehen. |
| Abo-Status | Das Update von `email_subscribe`, `push_subscribe`, `subscription_group_id`, oder `subscription_state` zählt **nicht** zur Datenpunkt-Nutzung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Wenn Sie `language` oder `country` für einen Nutzer:innen über den CSV-Import oder die API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden.
{% endalert %}

## Fehlersuche

Prüfen Sie diese häufigen Probleme, wenn Sie Probleme mit dem CSV-Import haben. Brauchen Sie noch Hilfe? Wenden Sie sich an [support@braze.com](mailto:support@braze.com).

### Probleme bei der Dateiformatierung

#### Deformierte Zeile

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, enthält Ihre CSV-Datei möglicherweise eine fehlerhafte Zeile. 

Um Daten korrekt zu importieren, muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl von Zellen haben wie die Kopfzeile. Zeilen mit einer Länge von mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen. Außerdem müssen alle Daten in UTF-8 kodiert sein.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert werden, als insgesamt in der CSV-Datei enthalten sind, deutet dies möglicherweise nicht auf ein Problem mit dem Import hin, da die leeren Zeilen nicht importiert werden müssten. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie zu importieren versuchen.

#### Fehlende Zeile

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen könnte:

| Fehler | Auflösung |
|---|---|
| Doppelte externe IDs, User-Aliasing, Braze IDs, E-Mail-Adressen oder Telefonnummern | Wenn es doppelte externe ID-Spalten gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, selbst wenn die Zeilen korrekt formatiert sind. In einigen Fällen kann es vorkommen, dass kein bestimmter Fehler gemeldet wird. Prüfen Sie auf Duplikate und entfernen Sie diese vor dem erneuten Hochladen. |
| Akzentuierte Zeichen | Ihre CSV-Datei kann Namen oder Attribute mit Akzenten enthalten. Stellen Sie sicher, dass die Datei UTF-8 kodiert ist, um Importprobleme zu vermeiden. |
| Braze ID gehört zu einem verwaisten Nutzer:innen | Wenn ein Nutzer:innen mit einem anderen zusammengelegt wurde und Braze die ID des Nutzers nicht mit dem verbleibenden Profil verknüpfen kann, wird die Zeile nicht importiert. |
| Leere Zeile | Leere Zeilen in der CSV-Datei können zu Fehlern in den Daten führen. Prüfen Sie mit einem einfachen Texteditor, nicht mit Excel oder Sheets. |
| Einschließlich doppelter Anführungszeichen (`"` ) | Dieses Zeichen ist ungültig und führt zu einer fehlerhaften Zeile. Verwenden Sie stattdessen einfache Anführungszeichen (`'`). |
| Inkonsistente Zeilenumbrüche | Gemischte Zeilenumbrüche (e.g., `\n` und `\r\n`) können dazu führen, dass die erste Zeile der Daten als Teil der Kopfzeile behandelt wird. Verwenden Sie einen Hexadezimal- oder voranbringenden Texteditor zur Überprüfung und Korrektur. |
| Falsch kodierte Datei | Auch wenn Akzente zulässig sind, muss die Datei UTF-8 kodiert sein. Andere Kodierungen können teilweise funktionieren, werden aber nicht vollständig unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### String Zitat

Werte, die in einfache (`''`) oder doppelte (`""`) Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

#### Falsch formatierte Daten

Datumsangaben, die nicht im [ISO-8601-Format](https://en.wikipedia.org/wiki/ISO_8601) vorliegen, werden beim Import nicht als `datetimes` gelesen.

### Probleme mit der Datenstruktur

#### Ungültige E-Mail-Adressen

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, gibt es möglicherweise eine oder mehrere ungültige verschlüsselte E-Mail-Adressen. Vergewissern Sie sich, dass alle E-Mail-Adressen ordnungsgemäß verschlüsselt sind, bevor Sie sie in Braze importieren.

- **Wenn Sie eine [E-Mail-Adresse in Braze aktualisieren oder importieren]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)**, verwenden Sie den gehashten E-Mail-Wert, wenn eine E-Mail enthalten ist. Diese Hash-E-Mail-Werte werden von Ihrem internen Team bereitgestellt. 
- **Wenn Sie einen neuen Nutzer:innen anlegen**, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert des Nutzers hinzufügen. Andernfalls wird der Nutzer:in nicht erstellt. Ähnlich verhält es sich, wenn Sie einem Nutzer:innen, der noch keine E-Mail hat, eine E-Mail-Adresse hinzufügen, müssen Sie `email_encrypted` hinzufügen. Andernfalls wird der Nutzer:innen nicht aktualisiert.

#### Als angepasstes Attribut importierte Daten

Wenn ein Teil der Standard Nutzerdaten (wie `email` oder `first_name`) als angepasstes Attribut importiert wird, überprüfen Sie die Groß- und Kleinschreibung Ihrer CSV-Datei. Zum Beispiel würde `First_name` als angepasstes Attribut importiert werden, während `first_name` korrekt in das Feld "Vorname" im Profil eines Nutzers importiert werden würde.

#### Mehrere Datentypen

Braze erwartet alle Werte in einer Spalte in demselben Datentyp. Werte, die nicht mit dem Datentyp des jeweiligen Attributs übereinstimmen, führen zu Segmentierungsfehlern.

Wenn Sie ein Zahlenattribut mit einer Null beginnen, gibt es außerdem Probleme, da Zahlen, die mit Nullen beginnen, als Strings betrachtet werden. Wenn Braze diesen String konvertiert, kann er wie ein Oktalwert behandelt werden (der Ziffern von null bis sieben verwendet), d.h. er wird in den entsprechenden Dezimalwert umgewandelt. Wenn der Wert in der CSV-Datei z.B. 0130 lautet, zeigt das Profil Braze 88 an. Um dieses Problem zu vermeiden, verwenden Sie Attribute mit String-Datentypen. Dieser Datentyp ist jedoch im Nummernvergleich der Segmentierung nicht verfügbar.

#### Standardattribut-Typen

Einige Standardattribute akzeptieren nur bestimmte Werte als gültig für Nutzer:innen-Updates. Eine Anleitung dazu finden Sie unter [Erstellen Ihrer CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Nachfolgende Leerzeichen und Unterschiede in der Großschreibung können dazu führen, dass ein Wert als ungültig interpretiert wird. In der folgenden CSV-Datei werden beispielsweise nur die E-Mail- und Push-Status der Nutzer:innen in der ersten Zeile (`brazetest1`) erfolgreich aktualisiert, da die akzeptierten Werte `unsubscribed`, `subscribed` und `opted_in` sind. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "CSV-Datei auswählen" funktioniert nicht

Es gibt mehrere Gründe, warum der Button **CSV-Datei auswählen** nicht funktioniert:

| Fehler | Auflösung |
|---|---|
| Popup-Blocker | Dies kann dazu führen, dass die Seite nicht angezeigt wird. Vergewissern Sie sich, dass Ihr Browser Pop-ups auf der Braze-Dashboard Website zulässt. |
| Veralteter Browser | Vergewissern Sie sich, dass Ihr Browser auf dem neuesten Stand ist; falls nicht, aktualisieren Sie ihn auf die neueste Version. |
| Hintergrundprozesse | Schließen Sie alle Instanzen des Browsers und starten Sie Ihren Computer neu. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
