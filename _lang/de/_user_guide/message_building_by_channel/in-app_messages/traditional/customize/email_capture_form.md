---
nav_title: Formular zur E-Mail-Erfassung
article_title: Formular zur E-Mail-Erfassung
page_order: 3
page_type: reference
description: "Dieser Artikel bietet einen Überblick über den Nachrichtentyp E-Mail-Erfassung in der App."
channel:
  - in-app messages
---

# Formular zur E-Mail-Erfassung {#email-capture-form}

> Mit E-Mail-Capture-Nachrichten können Sie die Benutzer Ihrer Website ganz einfach auffordern, ihre E-Mail-Adresse zu übermitteln, die dann in ihrem Benutzerprofil für alle Ihre Messaging-Kampagnen zur Verfügung steht.

Wenn ein Endbenutzer seine E-Mail-Adresse in dieses Formular eingibt, wird die E-Mail-Adresse zu seinem Benutzerprofil hinzugefügt.

- Für [anonyme Benutzer]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles), die noch kein Konto haben, wird die E-Mail-Adresse im anonymen Benutzerprofil gespeichert, das mit dem Gerät des Benutzers verbunden ist.
- Wenn im Benutzerprofil bereits eine E-Mail-Adresse vorhanden ist, wird die vorhandene E-Mail-Adresse durch die neu eingegebene E-Mail-Adresse überschrieben.
- Wenn die E-Mail-Adresse des oder der bekannten Nutzer:in als [Hard Bounce]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces) gekennzeichnet ist, prüfen wir, ob die neu eingegebene E-Mail-Adresse vom entsprechenden Braze-Profil abweicht. Wenn die angegebene E-Mail-Adresse abweicht, wird die E-Mail-Adresse aktualisiert und der "Hard Bounce"-Status wird entfernt. 
- Wenn ein:e Nutzer:in eine ungültige E-Mail-Adresse eingibt, wird eine Fehlermeldung angezeigt: "Bitte geben Sie eine gültige E-Mail ein."
    - Ungültige E-Mail-Adressen: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Gültige E-Mail-Adressen: 
        - `example@gmail.com`
        - `example@gnail.com` (mit einem Tippfehler)
    - Weitere Informationen zur E-Mail-Validierung in Braze finden Sie in den [technischen Richtlinien und Hinweisen zu E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% details Mehr über identifizierte versus anonyme Benutzer %}

Im Allgemeinen ist die Logik hinter dem Formular zur E-Mail-Erfassung ganz einfach. Damit wird die E-Mail-Adresse im Benutzerprofil in Braze für den derzeit aktiven Benutzer festgelegt. Das bedeutet jedoch, dass sich das Verhalten unterscheidet, je nachdem, ob der oder die Nutzer:in identifiziert ist (angemeldet, über `changeUser` aufgerufen) oder nicht.

Wenn ein anonymer Benutzer seine E-Mail-Adresse in das Formular eingibt und es abschickt, fügt Braze die E-Mail-Adresse zu seinem Profil hinzu. Wenn `changeUser` zu einem späteren Zeitpunkt aufgerufen wird und eine neue `external_id` zugewiesen wird (z. B. wenn sich ein:e neue:r Nutzer:in bei dem Dienst registriert), werden alle anonymen Nutzerprofildaten zusammengeführt, einschließlich der E-Mail-Adresse.

Wenn `changeUser` mit einem existierenden `external_id` aufgerufen wird, wird das anonyme Benutzerprofil verwaist und [bestimmte Datenfelder des Benutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior), die noch nicht für den identifizierten Benutzer existieren, werden zusammengeführt, aber alle Felder, die bereits existieren, gehen verloren, einschließlich der E-Mail-Adresse.

Weitere Informationen finden Sie im [Lebenszyklus des Benutzerprofils]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Schritt 1: In-App-Kampagne erstellen

Um zu dieser Option zu navigieren, müssen Sie eine In-App-Messaging-Kampagne erstellen. Stellen Sie dort je nach Anwendungsfall **Senden an** auf **Webbrowser**, **Mobile Apps** oder **Mobile Apps und Webbrowser** und wählen Sie dann **E-Mail-Erfassungsformular** als **Nachrichtentyp**.

![][4]

{% alert note %}
Um HTML in In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies dient der Sicherheit, da HTML-In-App-Nachrichten JavaScript ausführen können. Daher muss ein Website-Administrator sie aktivieren.
{% endalert %}

## Schritt 2: Formular anpassen {#customizable-features}

Als nächstes passen Sie Ihr Formular nach Bedarf an. Sie können die folgenden Funktionen für Ihr E-Mail-Erfassungsformular anpassen:

- Überschrift, Textkörper und Text des Buttons „Senden“
- Ein optionales Bild
- Ein optionaler Link zu den "Nutzungsbedingungen
- Verschiedene Farben für die Kopfzeile und den Text, die Schaltflächen und den Hintergrund
- Schlüssel-Wert-Paare
- Stil für Kopf- und Fließtext, Schaltflächen, Rahmenfarbe der Schaltflächen, Hintergrund und Overlay

![Composer für Formulare zur E-Mail-Erfassung.][5]

Wenn Sie weitere Anpassungen vornehmen möchten, wählen Sie **Benutzerdefinierter Code** für Ihren **Nachrichtentyp**. Sie können diese [modale Vorlage für die E-Mail-Erfassung](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) aus dem GitHub-Repository [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) als Startcode verwenden.

## Schritt 3: Entry-Zielgruppe festlegen

Wenn Sie dieses Formular nur an Nutzer:innen ohne bestehende E-Mail-Adressen senden möchten, verwenden Sie den Filter `Email Available is false`.

![Filter nach „E-Mail-Adresse verfügbar“ ist falsch][10]{: style="max-width:50%"}

Wenn Sie dieses Formular nur an Nutzer:innen ohne externe IDs (anonyme Nutzer:innen) senden möchten, verwenden Sie den Filter `External User ID is blank`.

![Filter nach externer Benutzer-ID ist leer][11]{: style="max-width:50%"}

Sie können die beiden Filter auch mit der Logik von `AND` kombinieren, falls gewünscht.

## Schritt 4: Zielbenutzer, die das Formular ausgefüllt haben (optional)

Nachdem Sie das Formular zur E-Mail-Erfassung gestartet und E-Mail-Adressen von Ihren Nutzer:innen gesammelt haben, können Sie diese Nutzer:innen mit dem Filter `Clicked/Opened Campaign` ansprechen. 

Setzen Sie den Filter auf `Has clicked in-app message button 1` für die Kampagne `<CAMPAIGN_NAME>`. Ersetzen Sie `<CAMPAIGN_NAME>` durch den Namen Ihrer E-Mail-Capture-Formular-Kampagne.

![Filter für die In-App-Nachrichten-Button 1 für Ihre Web-Kampagne „Formular zur E-Mail-Erfassung“][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}
