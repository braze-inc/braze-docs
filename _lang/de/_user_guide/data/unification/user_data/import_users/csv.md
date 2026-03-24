---
nav_title: CSV-Import
article_title: "CSV-Import"
description: "Erfahren Sie, wie Sie Nutzer:innen-Attribute und angepasste Events mithilfe des CSV-Imports erfassen und aktualisieren können."
page_order: 1.2
---

# CSV-Import

> Erfahren Sie, wie Sie Nutzer:innen-Attribute und angepasste Events mithilfe des CSV-Imports erfassen und aktualisieren können.

## Über den CSV-Import

Mit dem CSV-Import können Sie die folgenden Nutzer:innen-Attribute und angepassten Events erfassen und aktualisieren.

|Typ|Definition|Beispiel|Maximale Dateigröße|
|---|---|---|---|
|Standardattribute|Reservierte Nutzer:innen-Attribute, die von Braze erkannt werden.|`first_name`, `email`|500 MB|
|Angepasste Attribute|Eindeutige Nutzer:innen-Attribute für Ihr Unternehmen.|`last_destination_searched`|500 MB|
|Angepasste Events|Eindeutige Events in Ihrem Unternehmen, die Aktionen von Nutzer:innen darstellen.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSV-Import verwenden

### 1. Schritt: CSV-Template herunterladen

Um den CSV-Import zu öffnen, navigieren Sie zu **Zielgruppen** > **Nutzerimport**. Hier finden Sie eine Tabelle mit Details zu den letzten Importvorgängen, wie beispielsweise das Datum des Uploads, den Namen der hochladenden Person, den Dateinamen, die Targeting-Verfügbarkeit, die Anzahl der importierten Zeilen und den Status des Imports.

Um mit Ihrer CSV-Datei zu beginnen, laden Sie ein Template für Attribute oder Events herunter.

![Die Seite „Nutzer:innen importieren" im Braze-Dashboard.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### 2. Schritt: Bezeichner auswählen {#choose-an-identifier}

Die CSV-Datei, die Sie importieren, benötigt einen dedizierten Bezeichner. Sie haben die Wahl zwischen folgenden Optionen:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Beim Importieren Ihrer Kundendaten können Sie eine `external_id` als eindeutigen Bezeichner für jede Kund:in verwenden. Wenn Sie in Ihrem Import eine `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit derselben `external_id` oder erstellt eine:n neu identifizierte:n Nutzer:in mit dieser `external_id`, falls keine:r gefunden wird.

- Download: [CSV-Attribut-Import-Template: Externe ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Download: [CSV-Event-Import-Template: Externe ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %} 
Wenn Sie eine Mischung aus Nutzer:innen mit einer `external_id` und Nutzer:innen ohne hochladen, müssen Sie für jeden Import eine eigene CSV-Datei erstellen. Eine CSV-Datei kann nicht sowohl `external_ids` als auch Nutzer-Aliase enthalten.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Um Nutzer:innen anzusprechen, die keine `external_id` besitzen, können Sie eine Liste mit Nutzer-Aliasen importieren. Ein Alias dient als alternativer eindeutiger Bezeichner und kann hilfreich sein, wenn Sie anonyme Nutzer:innen ansprechen möchten, die sich nicht bei Ihrer App registriert oder ein Konto erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur Aliase enthalten, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `user_alias_name`: Ein eindeutiger Bezeichner für Nutzer:innen; eine Alternative zur `external_id`  
- `user_alias_label`: Ein gemeinsames Label, mit dem Nutzer-Aliase gruppiert werden können

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Schmidt | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Wenn Sie in Ihrem Import sowohl einen `user_alias_name` als auch ein `user_alias_label` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wenn keine:r gefunden wird, erstellt Braze eine:n neu identifizierte:n Nutzer:in mit diesem `user_alias_name`.

{% alert important %}
Es ist nicht möglich, per CSV-Import eine:n bestehende:n Nutzer:in mit einem `user_alias_name` zu aktualisieren, wenn diese:r bereits eine `external_id` besitzt. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um reine Alias-Nutzer:innen mit einer `external_id` zu verknüpfen, verwenden Sie den [Endpunkt „Nutzer:innen identifizieren"]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Download: [CSV-Attribut-Import-Template: Nutzer-Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Um bestehende Nutzerprofile in Braze zu aktualisieren, indem Sie einen internen Braze-ID-Wert anstelle einer `external_id` oder eines `user_alias_name` und `user_alias_label` verwenden, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über die CSV-Exportoption im Rahmen der Segmentierung exportiert haben und ein neues angepasstes Attribut zu diesen bestehenden Nutzer:innen hinzufügen möchten.

{% alert important %}
Es ist nicht möglich, per CSV-Import eine:n neue:n Nutzer:in mit `braze_id` zu erstellen. Diese Methode kann nur zum Aktualisieren bereits bestehender Nutzer:innen innerhalb der Braze-Plattform verwendet werden.  
{% endalert %}

{% alert tip %}
Der Wert `braze_id` kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` gekennzeichnet sein. Diese ID entspricht der `braze_id` für eine:n Nutzer:in, sodass Sie diese Spalte in `braze_id` umbenennen können, wenn Sie die CSV erneut importieren.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Sie können eine externe ID oder einen Nutzer-Alias weglassen und stattdessen eine E-Mail-Adresse oder eine Telefonnummer verwenden, um Nutzer:innen zu importieren. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, überprüfen Sie Folgendes:

- Stellen Sie sicher, dass Sie keine externen IDs oder Nutzer-Aliase für diese Profile in Ihrer CSV-Datei haben. Falls doch, verwendet Braze zur Identifizierung von Profilen vorrangig die externe ID oder den Nutzer-Alias vor der E-Mail-Adresse.  
- Vergewissern Sie sich, dass Ihre CSV-Datei korrekt formatiert ist.  

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihre CSV-Datei aufnehmen, wird die E-Mail-Adresse bei der Suche nach Profilen gegenüber der Telefonnummer bevorzugt.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail-Adresse oder Telefonnummer enthält, wird dieses Profil aktualisiert, und Braze erstellt kein neues Profil. Sind mehrere Profile mit derselben E-Mail-Adresse vorhanden, verwendet Braze dieselbe Logik wie der [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), wobei das zuletzt aktualisierte Profil geändert wird.

Sollte kein Profil mit dieser E-Mail-Adresse oder Telefonnummer vorhanden sein, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) verwenden, um dieses Profil später zu identifizieren. Um ein Nutzerprofil zu löschen, können Sie auch den [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)-Endpunkt verwenden.
{% endtab %}
{% endtabs %}

### 3. Schritt: CSV-Datei erstellen

Sie können einen der folgenden Datentypen als einzelne CSV-Datei hochladen. Um mehrere Datentypen hochzuladen, laden Sie bitte mehrere CSV-Dateien hoch.

- **Nutzer:innen-Attribute:** Dies umfasst sowohl Standard- als auch angepasste Nutzer:innen-Attribute. Standardattribute sind reservierte Schlüssel in Braze (wie z. B. `first_name` oder `email`), und angepasste Attribute sind für Ihr Unternehmen eindeutige Nutzer:innen-Attribute (wie z. B. `last_destination_searched`).  
- **Angepasste Events:** Diese sind für Ihr Unternehmen eindeutig und spiegeln die Aktionen wider, die Nutzer:innen durchgeführt haben, wie beispielsweise `trip_booked` für eine Reisebuchungs-App.

Wenn Sie bereit sind, mit der Erstellung Ihrer CSV-Datei zu beginnen, beachten Sie bitte die folgenden Informationen:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Erforderliche Bezeichner {#required-identifiers-attributes}

Obwohl `external_id` nicht erforderlich ist, **müssen** Sie **einen** der folgenden Bezeichner als Kopfzeile in Ihre CSV-Datei aufnehmen. Für weitere Informationen zu den einzelnen Optionen lesen Sie bitte [Bezeichner auswählen](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Angepasste Attribute

Die folgenden Datentypen können als angepasste Attribute für den CSV-Import verwendet werden. Spaltenüberschriften, die nicht genau mit einem [Standardattribut](#default-attributes) übereinstimmen, werden in Braze als angepasste Attribute importiert.

| Datentyp | Beschreibung |
|---|---|
| Datetime | Muss im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format gespeichert werden. |
| Boolescher Wert | Akzeptiert `true` oder `false`. |
| Zahl | Muss eine ganze Zahl oder eine Gleitkommazahl ohne Leerzeichen oder Kommas sein. Gleitkommazahlen müssen einen Punkt (`.`) als Dezimaltrennzeichen verwenden. |
| String | Kann Kommas enthalten, wenn der Wert in doppelte Anführungszeichen (`""`) gesetzt ist. |
| Leer | Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und es ist nicht erforderlich, alle vorhandenen Nutzer:innen-Attribute in Ihre CSV-Datei aufzunehmen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Arrays, Push-Token und Datentypen für angepasste Events werden beim Nutzerimport nicht unterstützt, da Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert werden und beim Parsen Ihrer Datei zu Fehlern führen können.<br><br>Um diese Art von Werten hochzuladen, verwenden Sie stattdessen den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Standardattribute

{% alert important %}
Beim Importieren von Standardattributen müssen die von Ihnen verwendeten Spaltenüberschriften genau mit der Schreibweise und Groß-/Kleinschreibung der Standard-Nutzer:innen-Attribute übereinstimmen. Andernfalls erkennt Braze diese stattdessen als [angepasste Attribute](#custom-attributes).
{% endalert %}

Die folgenden Standardattribute stehen für den Nutzerimport zur Verfügung.

| Nutzerprofil-Feld | Datentyp | Beschreibung | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Bezeichner für Ihre Kund:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_name` | String | Ein eindeutiger Bezeichner für anonyme Nutzer:innen, der eine Alternative zur `external_id` darstellt. Muss in Verbindung mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_label` | String | Ein gemeinsames Label, mit dem Nutzer-Aliase gruppiert werden können. Muss in Verbindung mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z. B. `Jane`). | Nein |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie sie ihn angegeben haben (z. B. `Doe`). | Nein |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie sie sie angegeben haben (z. B. `jane.doe@braze.com`). | Nein |
| `country` | String | Ländercodes müssen an Braze im ISO-3166-1-alpha-2-Standard übergeben werden (z. B. `GB`). | Nein |
| `dob` | String | Muss im Format „JJJJ-MM-TT" übergeben werden (z. B. `1980-12-21`). Dadurch werden die Geburtsdaten Ihrer Nutzer:innen importiert, und Sie können Nutzer:innen ansprechen, die „heute" Geburtstag haben. | Nein |
| `gender` | String | „M", „F", „O" (Sonstiges), „N" (nicht zutreffend), „P" (möchte ich nicht sagen) oder nil (unbekannt). | Nein |
| `home_city` | String | Der Wohnort Ihrer Nutzer:innen, wie sie ihn angegeben haben (z. B. `London`). | Nein |
| `language` | String | Die Sprache muss gemäß ISO-639-1 an Braze übergeben werden (z. B. `en`). Sehen Sie sich unsere [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/) an. | Nein |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im `E.164`-Format (z. B. `+442071838750`). Hinweise zur Formatierung finden Sie unter [Telefonnummern von Nutzer:innen]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). | Nein |
| `email_open_tracking_disabled` | Boolescher Wert | Akzeptiert true oder false. Setzen Sie diese Option auf true, um zu verhindern, dass das Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails an diese:n Nutzer:in hinzugefügt wird. Nur für SparkPost und SendGrid verfügbar. | Nein |
| `email_click_tracking_disabled` | Boolescher Wert | Akzeptiert true oder false. Setzen Sie diese Option auf true, um das Klick-Tracking für alle Links in zukünftigen E-Mails an diese:n Nutzer:in zu deaktivieren. Nur für SparkPost und SendGrid verfügbar. | Nein |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Erhalt von E-Mail-Nachrichten registriert), `unsubscribed` (explizit vom Erhalt von E-Mail-Nachrichten abgemeldet) und `subscribed` (weder Opt-in noch Opt-out). | Nein |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von Push-Nachrichten abgemeldet) und `subscribed` (weder Opt-in noch Opt-out). | Nein |
| `time_zone` | String | Die Zeitzone muss an Braze im gleichen Format wie die IANA-Zeitzonendatenbank übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`). | Nein |
| `date_of_first_session`  `date_of_last_session` | String | Kann in einem der folgenden ISO-8601-Formate übermittelt werden: „JJJJ-MM-TT" „JJJJ-MM-TTTHH:MM:SS+00:00" „JJJJ-MM-TTTHH:MM:SSZ" „JJJJ-MM-TTTHH:MM:SS" (z. B. 2019-11-20T18:38:57) | Nein |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Diesen Bezeichner finden Sie auf der Seite der Abo-Gruppe in Ihrem Dashboard. | Nein |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Update des Abo-Gruppenstatus (optional)

Darüber hinaus können Sie über den Nutzerimport Nutzer:innen zu E-Mail- oder SMS-Abo-Gruppen hinzufügen. Dies ist besonders für SMS nützlich, da Nutzer:innen in einer SMS-Abo-Gruppe eingeschrieben sein müssen, um über den SMS-Kanal Nachrichten zu erhalten. Weitere Informationen finden Sie unter [SMS-Abo-Gruppen](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Wenn Sie den Status von Abo-Gruppen aktualisieren, müssen Sie die folgenden beiden Spalten in Ihrer CSV-Datei haben:

- `subscription_group_id`: Die `id` der [Abo-Gruppe](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Im Nutzerimport kann nur eine einzige `subscription_group_id` pro Zeile eingestellt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id`-Werte haben. Sollten Sie jedoch dieselben Nutzer:innen in mehrere Abo-Gruppen aufnehmen müssen, ist es erforderlich, mehrere Importe durchzuführen.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Erforderliche Bezeichner {#required-identifiers-custom-events}

Obwohl `external_id` nicht erforderlich ist, **müssen** Sie **einen** der folgenden Bezeichner als Kopfzeile in Ihre CSV-Datei aufnehmen. Für weitere Informationen zu den einzelnen Optionen lesen Sie bitte [Bezeichner auswählen](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Felder für angepasste Events

Zusätzlich zu den folgenden Angaben kann Ihre CSV-Datei auch weitere Spaltenüberschriften für Event-Eigenschaften enthalten. Diese Eigenschaften sollten eine Spaltenüberschrift im Format `<event_name>.properties.<property name>.` haben.

Beispielsweise kann das angepasste Event `trip_booked` die Eigenschaften `destination` und `duration` aufweisen. Diese können importiert werden, indem die Spaltenüberschriften `trip_booked.properties.destination` und `trip_booked.properties.duration` verwendet werden.

| Nutzerprofil-Feld | Datentyp | Informationen | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Bezeichner für Ihre:n Nutzer:in. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `braze_id` | String | Ein von Braze zugewiesener Bezeichner für Ihre:n Nutzer:in. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_name` | String | Ein eindeutiger Bezeichner für anonyme Nutzer:innen, der eine Alternative zur `external_id` darstellt. Muss in Verbindung mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_label` | String | Ein gemeinsames Label, mit dem Nutzer-Aliase gruppiert werden können. Muss in Verbindung mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie sie sie angegeben haben (z. B. `jane.doe@braze.com`). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Bitte beachten Sie den folgenden Hinweis. |
| `phone` | String | Eine Telefonnummer, wie sie von Ihren Nutzer:innen angegeben wurde, im `E.164`-Format (z. B. `+442071838750`). Hinweise zur Formatierung finden Sie unter [Telefonnummern von Nutzer:innen]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Bitte beachten Sie den folgenden Hinweis. |
| `name` | String | Ein angepasstes Event Ihrer Nutzer:innen. | Ja |
| `time` | String | Der Zeitpunkt des Events. Kann in einem der folgenden ISO-8601-Formate übermittelt werden: „JJJJ-MM-TT" „JJJJ-MM-TTTHH:MM:SS+00:00" „JJJJ-MM-TTTHH:MM:SSZ" „JJJJ-MM-TTTHH:MM:SS" (z. B. 2019-11-20T18:38:57) | Ja |
| `<event name>.properties.<property name>` | Mehrere | Eine Event-Eigenschaft, die mit einem angepassten Event verknüpft ist. Ein Beispiel ist `trip_booked.properties.destination` | Nein |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### 4. Schritt: Datei hochladen

Um Ihre Datei hochzuladen, wählen Sie **Attribute** oder **Events**, klicken Sie auf **Dateien durchsuchen** und laden Sie Ihre CSV-Datei hoch. Braze zeigt eine Vorschau der ersten Zeilen und eine Zusammenfassung der erkannten Felder an.

![Das Modal „Upload abgeschlossen" zeigt eine Dateivorschau, ein Feld für den Importnamen, Targeting-Einstellungen und ein Kontrollkästchen für die Dateivalidierung an.]({% image_buster /assets/img/csv_import/upload_completed.png %})

Im Feld **Importname** können Sie Ihren Import umbenennen. Standardmäßig wird der Dateiname verwendet.

{% alert note %}
Die Dateivorschau zeigt nur die ersten Zeilen Ihrer Datei an. Um jede Zeile vor dem Import zu überprüfen, verwenden Sie die [Dateivalidierung](#file-validation).
{% endalert %}

### 5. Schritt: Datei validieren (optional) {#file-validation}

Bevor Sie mit dem Import beginnen, können Sie eine Dateivalidierung durchführen, um jede Zeile auf Fehler und Warnungen zu überprüfen. Um Ihre Datei zu validieren, wählen Sie **Datei vor dem Import validieren** und klicken Sie anschließend auf **Import starten**.

Die Validierung kann bei Dateien mit der maximal zulässigen Größe bis zu 2 Minuten dauern. Während die Validierung läuft, können Sie **Validierung überspringen** auswählen, um sie zu umgehen und sofort fortzufahren.

#### Validierungsergebnisse

Nach Abschluss der Validierung wird eines der folgenden Ergebnisse angezeigt.

| Ergebnis | Was es bedeutet | Nächster Schritt |
|---|---|---|
| **Validierung abgeschlossen** | Es wurden keine Probleme festgestellt. | Wählen Sie **Daten importieren**. |
| **Probleme festgestellt** | Einige Zeilen enthalten Fehler oder Warnungen. | Laden Sie den Fehlerbericht herunter, um ihn zu überprüfen. Wählen Sie anschließend **Trotzdem importieren**, um fortzufahren, oder **Abbrechen**, um Ihre Datei zunächst zu korrigieren. |
| **Validierung abgelaufen** | Die Validierung ist abgelaufen. Die überprüften Zeilen wiesen keine Probleme auf. | Wählen Sie **Daten importieren**. Ein vollständiger Bericht wird in wenigen Minuten verfügbar sein. |
| **Validierung mit Problemen abgelaufen** | Die Validierung wurde nicht rechtzeitig abgeschlossen und es wurden Fehler in einigen der überprüften Zeilen festgestellt. | Laden Sie den Teilbericht herunter, um die Ergebnisse zu überprüfen, und wählen Sie anschließend **Trotzdem importieren** oder **Abbrechen**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![Das Dialogfeld „Probleme festgestellt" zeigt die Anzahl der Zeilen mit Fehlern und Warnungen an und bietet Optionen zum Abbrechen, Herunterladen des Fehlerberichts oder zum Importieren.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### Den Fehlerbericht verstehen

Der Fehlerbericht ist eine CSV-Datei, die jede markierte Zeile zusammen mit den Originaldaten und einer Beschreibung des Problems enthält.

| Problemtyp | Beschreibung |
|---|---|
| **Fehler** | Die Zeile wird beim Import vollständig übersprungen. |
| **Warnung** | Die Zeile wird importiert, jedoch werden einige Werte nicht übernommen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Nachdem Sie den Bericht überprüft haben, können Sie die Probleme in Ihrer Originaldatei korrigieren und erneut hochladen oder mit dem Import fortfahren und die Teilergebnisse akzeptieren.

### 6. Schritt: Targeting-Einstellungen auswählen

Sie können auch aus den folgenden Targeting-Einstellungen auswählen. Wenn Sie keinen neuen Targeting-Filter oder kein neues Segment aus Ihrem Import erstellen müssen, wählen Sie **Diese Liste nicht als Targeting-Filter verfügbar machen**.

| Option | Beschreibung |
|---|---|
| Targeting-Filter | Um Ihre CSV-Datei beim Erstellen von Nutzersegmenten in eine Retargeting-Option umzuwandeln, wählen Sie Ihre Datei aus dem Dropdown-Menü **Aktualisiert/Aus CSV importiert** aus und wählen Sie anschließend **Targeting-Filter erstellen**. |
| Neue Segmente | Um auch ein neues Segment aus Ihrem neuen Targeting-Filter zu erstellen, wählen Sie **Targeting-Filter erstellen und zu neuem Segment hinzufügen**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Eine Filtergruppe mit dem Filter „Aktualisiert/Aus CSV importiert", die eine CSV-Datei mit dem Titel „Halloween season fun" enthält.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### 7. Schritt: CSV-Import starten

Wenn Sie bereit sind, wählen Sie **Import starten**. Sie können den aktuellen Fortschritt auf der Seite **Nutzerimport** verfolgen, die alle 5 Sekunden automatisch aktualisiert wird.

{% alert note %}
Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe erfolgen parallel, sodass die Reihenfolge der Aktualisierungen nicht garantiert sequenziell ist. Wenn Sie möchten, dass die CSV-Importe nacheinander ausgeführt werden, warten Sie, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.
{% endalert %}

#### Importstatus

Nachdem Sie den Import gestartet haben, können Sie dessen Status auf der Seite **Nutzerimport** überprüfen.

| Status | Beschreibung |
|---|---|
| **Fertig** | Alle Zeilen wurden erfolgreich importiert. |
| **Teilerfolg** | Einige Zeilen sind fehlgeschlagen. Wählen Sie das Drei-Punkte-Menü neben dem Import aus, um einen Fehlerbericht oder die ursprünglich hochgeladene CSV-Datei herunterzuladen. |
| **In Arbeit** | Der Import wird derzeit durchgeführt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Die Seite „Nutzerimport" zeigt den Status „Teilerfolg" an, wobei das Kontextmenü geöffnet ist und die Optionen „Fehlerbericht herunterladen" und „Hochgeladene CSV-Datei herunterladen" angezeigt werden.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Der Fehlerbericht nach dem Import enthält Zeilen, die aus Gründen fehlgeschlagen sind, die nicht durch die Validierung abgedeckt werden, beispielsweise wenn eine:r Nutzer:in in Braze nicht vorhanden ist.

{% alert important %}
Zuvor hochgeladene CSV-Dateien stehen auf der Seite **Nutzerimport** 14 Tage nach dem Upload-Datum zum Download bereit. Nach 14 Tagen wird die Datei dauerhaft gelöscht und ist nicht mehr zugänglich.
{% endalert %}

## Überlegungen zu Datenpunkten

Jeder aus einer CSV-Datei importierte Kundendatensatz überschreibt den bestehenden Wert in den Nutzerprofilen und protokolliert einen Datenpunkt, mit Ausnahme von externen IDs und leeren Werten. Sollten Sie Fragen zu den Besonderheiten der Braze-Datenpunkte haben, steht Ihnen Ihr Account Manager gerne zur Verfügung.

| Betrachtung | Details |
|---|---|
| Externe IDs | Das Hochladen einer CSV-Datei, die nur `external_id` enthält, führt nicht zur Protokollierung von Datenpunkten. Auf diese Weise können Sie bestehende Braze-Nutzer:innen segmentieren, ohne die Datenlimits zu beeinträchtigen. Die Einbeziehung von Feldern wie `email` oder `phone` überschreibt jedoch vorhandene Nutzerdaten und protokolliert **Datenpunkte**. <br><br>CSV-Importe, die ausschließlich zur Segmentierung verwendet werden, protokollieren keine Datenpunkte, wie beispielsweise solche, die nur `external_id`, `braze_id` oder `user_alias_name` enthalten. |
| Leere Werte | Leere Werte in Ihrer CSV-Datei überschreiben keine vorhandenen Daten im Nutzerprofil. Es ist nicht erforderlich, beim Importieren alle Nutzer:innen-Attribute oder angepassten Events einzubeziehen. |
| Abo-Status | Das Aktualisieren von `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` wird **nicht** zur Datenpunkt-Nutzung hinzugerechnet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Wenn Sie `language` oder `country` für eine:n Nutzer:in über CSV-Import oder API festlegen, verhindert dies, dass Braze diese Informationen automatisch über das SDK erfasst.
{% endalert %}

## Fehlerbehebung

Wenn Sie die [Dateivalidierung](#file-validation) verwendet haben, beginnen Sie mit dem Fehlerbericht – er enthält das spezifische Problem für jede markierte Zeile und eine Beschreibung, wie Sie es beheben können. Für Zeilen, die während des Imports und nicht während der Validierung fehlgeschlagen sind, laden Sie den Fehlerbericht herunter, indem Sie auf der Seite **Nutzerimport** mit dem Mauszeiger über die Zeile fahren und den <i class="fas fa-download" title="Download"></i>-Button auswählen.

Sollten Sie Schwierigkeiten beim CSV-Import haben, überprüfen Sie bitte die folgenden häufig auftretenden Probleme.

### Probleme bei der Dateiformatierung

#### Fehlerhafte Zeile

Sollte der Upload mit Fehlern abgeschlossen worden sein, könnte es sein, dass Ihre CSV-Datei eine fehlerhafte Zeile enthält. 

Um Daten korrekt zu importieren, muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl von Zellen haben wie die Kopfzeile. Zeilen mit mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen. Außerdem müssen alle Daten in UTF-8 kodiert sein.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert werden als die Gesamtzahl der Zeilen in der CSV-Datei, stellt dies möglicherweise kein Problem beim Import dar, da die leeren Zeilen nicht importiert werden müssen. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie importieren möchten.

#### Fehlende Zeile

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen könnte:

| Problem | Lösung |
|---|---|
| Doppelte externe IDs, Nutzer-Aliase, Braze-IDs, E-Mail-Adressen oder Telefonnummern | Wenn es doppelte externe ID-Spalten gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, selbst wenn die Zeilen korrekt formatiert sind. In einigen Fällen wird kein spezifischer Fehler gemeldet. Überprüfen Sie auf Duplikate und entfernen Sie diese, bevor Sie erneut hochladen. |
| Akzentuierte Zeichen | Ihre CSV-Datei kann Namen oder Attribute mit Akzenten enthalten. Stellen Sie sicher, dass die Datei UTF-8-kodiert ist, um Probleme beim Import zu vermeiden. |
| Braze-ID gehört zu verwaisten Nutzer:innen | Wenn Nutzer:innen mit anderen zusammengeführt wurden und Braze die Braze-ID nicht mit dem verbleibenden Profil verknüpfen kann, wird die Zeile nicht importiert. |
| Leere Zeile | Leere Zeilen in der CSV-Datei können zu fehlerhaften Daten führen. Überprüfen Sie dies mit einem einfachen Texteditor, nicht mit Excel oder Sheets. |
| Nicht maskierte oder unausgeglichene doppelte Anführungszeichen (`"`) | Doppelte Anführungszeichen umschließen String-Werte, die Kommas enthalten. Wenn ein Wert selbst ein doppeltes Anführungszeichen enthält, muss es durch Verdoppeln (`""`) maskiert werden. Nicht maskierte oder unausgeglichene doppelte Anführungszeichen führen zu einer fehlerhaften Zeile. |
| Uneinheitliche Zeilenumbrüche | Gemischte Zeilenumbrüche (z. B. `\n` und `\r\n`) können dazu führen, dass die erste Datenzeile als Teil der Kopfzeile behandelt wird. Verwenden Sie einen Hex-Editor oder einen erweiterten Texteditor, um die Datei zu überprüfen und zu korrigieren. |
| Falsch kodierte Datei | Auch wenn Akzente zulässig sind, muss die Datei in UTF-8 kodiert sein. Andere Kodierungen können teilweise funktionieren, werden jedoch nicht vollständig unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### String-Anführungszeichen

Werte, die in einfache (`''`) oder doppelte (`""`) Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

#### Falsch formatierte Datumsangaben

Datumsangaben, die nicht im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format vorliegen, werden beim Import nicht als `datetimes` gelesen.

### Probleme mit der Datenstruktur

#### Ungültige E-Mail-Adressen

Sollte der Upload mit Fehlern abgeschlossen worden sein, könnte es sein, dass eine oder mehrere verschlüsselte E-Mail-Adressen ungültig sind. Vergewissern Sie sich, dass alle E-Mail-Adressen ordnungsgemäß verschlüsselt sind, bevor Sie sie in Braze importieren.

- **Wenn Sie [E-Mail-Adressen in Braze aktualisieren oder importieren]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)**, verwenden Sie den gehashten E-Mail-Wert, wenn eine E-Mail enthalten ist. Diese gehashten E-Mail-Werte werden von Ihrem internen Team bereitgestellt. 
- **Wenn Sie neue Nutzer:innen anlegen**, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert hinzufügen. Andernfalls wird Braze die Nutzer:innen nicht erstellen. Ebenso müssen Sie beim Hinzufügen einer E-Mail-Adresse zu bestehenden Nutzer:innen, die noch keine E-Mail haben, `email_encrypted` hinzufügen. Andernfalls wird Braze die Nutzer:innen nicht aktualisieren.

#### Als angepasstes Attribut importierte Daten

Wenn ein Teil der Standard-Nutzerdaten (wie `email` oder `first_name`) als angepasstes Attribut importiert wird, überprüfen Sie die Groß-/Kleinschreibung und die Abstände in Ihrer CSV-Datei. Beispielsweise wird `First_name` als angepasstes Attribut importiert, während `first_name` korrekt in das Feld „Vorname" im Nutzerprofil importiert wird.

#### Datentyp eines angepassten Attributs ändern

Wenn Sie den Datentyp eines bestehenden angepassten Attributs ändern müssen (z. B. von String zu Boolescher Wert), aktualisieren Sie den Datentyp auf der Seite [**Angepasste Attribute**]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) im Dashboard, bevor Sie Ihre CSV-Datei importieren. Wenn der Datentyp in Ihrer CSV-Datei nicht mit dem aktuell definierten Datentyp des Attributs übereinstimmt, schlägt der Import mit einem Fehler fehl.

#### Mehrere Datentypen

Braze erwartet, dass alle Werte in einer Spalte denselben Datentyp haben. Werte, die nicht mit dem Datentyp ihres Attributs übereinstimmen, führen zu Fehlern bei der Segmentierung.

Wenn ein Zahlenattribut mit einer Null beginnt, kann es außerdem zu Problemen kommen, da Zahlen, die mit Nullen beginnen, als Strings betrachtet werden. Wenn Braze diesen String konvertiert, kann er wie ein Oktalwert (der Ziffern von null bis sieben verwendet) behandelt werden, was bedeutet, dass er in den entsprechenden Dezimalwert konvertiert wird. Wenn beispielsweise der Wert in der CSV-Datei 0130 lautet, wird im Braze-Profil 88 angezeigt. Um dieses Problem zu vermeiden, verwenden Sie Attribute mit String-Datentypen. Dieser Datentyp ist jedoch im Zahlenvergleich der Segmentierung nicht verfügbar.

#### Standardattribut-Typen

Einige Standardattribute akzeptieren nur bestimmte Werte als gültig für Nutzer:innen-Updates. Eine Anleitung dazu finden Sie unter [Erstellen Ihrer CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Nachfolgende Leerzeichen und Unterschiede in der Groß-/Kleinschreibung können dazu führen, dass ein Wert als ungültig interpretiert wird. In der folgenden CSV-Datei wurden beispielsweise nur die E-Mail- und Push-Status der Nutzer:innen in der ersten Zeile (`brazetest1`) erfolgreich aktualisiert, da die akzeptierten Werte `unsubscribed`, `subscribed` und `opted_in` sind. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### „CSV-Datei auswählen" funktioniert nicht

Es gibt mehrere Gründe, warum der Button **CSV-Datei auswählen** nicht funktioniert:

| Problem | Lösung |
|---|---|
| Popup-Blocker | Dies kann dazu führen, dass die Seite nicht angezeigt wird. Vergewissern Sie sich, dass Ihr Browser Pop-ups auf der Braze-Dashboard-Website zulässt. |
| Veralteter Browser | Stellen Sie sicher, dass Ihr Browser auf dem neuesten Stand ist; falls nicht, aktualisieren Sie ihn auf die neueste Version. |
| Hintergrundprozesse | Schließen Sie alle Browser-Instanzen und starten Sie Ihren Computer neu. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}