---
nav_title: Formular zur Erfassung von E-Mails
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

{% details More on identified versus anonymous users %}

Im Allgemeinen ist die Logik hinter dem Formular zur E-Mail-Erfassung ganz einfach. Damit wird die E-Mail-Adresse im Benutzerprofil in Braze für den derzeit aktiven Benutzer festgelegt. Das bedeutet jedoch, dass sich das Verhalten unterscheidet, je nachdem, ob der oder die Nutzer:in identifiziert ist (angemeldet, über `changeUser` aufgerufen) oder nicht.

Wenn ein anonymer Benutzer seine E-Mail-Adresse in das Formular eingibt und es abschickt, fügt Braze die E-Mail-Adresse zu seinem Profil hinzu. Wenn `changeUser` zu einem späteren Zeitpunkt aufgerufen wird und eine neue `external_id` zugewiesen wird (z. B. wenn sich ein:e neue:r Nutzer:in bei dem Dienst registriert), werden alle anonymen Nutzerprofildaten zusammengeführt, einschließlich der E-Mail-Adresse.

Wenn `changeUser` mit einem existierenden `external_id` aufgerufen wird, wird das anonyme Benutzerprofil verwaist und [bestimmte Datenfelder des Benutzerprofils]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior), die noch nicht für den identifizierten Benutzer existieren, werden zusammengeführt, aber alle Felder, die bereits existieren, gehen verloren, einschließlich der E-Mail-Adresse.

Weitere Informationen finden Sie im [Lebenszyklus des Benutzerprofils]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Schritt 1: In-App-Kampagne erstellen

Um zu dieser Option zu navigieren, müssen Sie eine In-App-Messaging-Kampagne erstellen. Stellen Sie dort je nach Anwendungsfall **Senden an** entweder **Webbrowser**, **Mobile Apps** oder **Beide Mobile Apps & Webbrowser** ein und wählen Sie dann als **Nachrichtentyp** **E-Mail-Erfassungsformular** aus.

{% alert note %}
**Targeting von Nutzer:innen im Internet?** <br>Um HTML in In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies dient der Sicherheit, da HTML-In-App-Nachrichten JavaScript ausführen können. Daher muss ein Website-Administrator sie aktivieren.
{% endalert %}

## Schritt 2: Formular anpassen {#customizable-features}

Als nächstes passen Sie Ihr Formular nach Bedarf an. Sie können die folgenden Funktionen für Ihr E-Mail-Erfassungsformular anpassen:

- Überschrift, Textkörper und Text des Buttons „Senden“
- Ein optionales Bild
- Ein optionaler Link zu den "Nutzungsbedingungen
- Verschiedene Farben für die Kopfzeile und den Text, die Schaltflächen und den Hintergrund
- Schlüssel-Wert-Paare
- Stil für Kopf- und Fließtext, Schaltflächen, Rahmenfarbe der Schaltflächen, Hintergrund und Overlay

![Composer für E-Mail-Erfassungsformular.]({% image_buster /assets/img/email_capture.png %})

Wenn Sie weitere Anpassungen vornehmen möchten, wählen Sie **Benutzerdefinierter Code** für Ihren **Nachrichtentyp**. Sie können diese [modale Vorlage für die E-Mail-Erfassung](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) aus dem GitHub-Repository [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) als Startcode verwenden.

## Schritt 3: Entry-Zielgruppe festlegen

Wenn Sie eine In-App-Nachricht verwenden, um die E-Mails der Nutzer zu erfassen, sollten Sie die Zielgruppe auf Nutzer:innen beschränken, die diese Informationen noch nicht angegeben haben.

- **Um Nutzer:innen ohne E-Mail Adresse zusammenzustellen:** Verwenden Sie den Filter `Email Available` ist `false`. Dadurch wird das Formular nur Nutzern:in angezeigt, die keine E-Mail hinterlegt haben. So vermeiden Sie überflüssige Abfragen für bekannte Nutzer:innen.
- **Um anonyme Nutzer:innen ohne externe IDs zusammenzustellen:** Verwenden Sie den Filter `External User ID` `is blank`. Dies ist nützlich, wenn Sie Nutzer:innen identifizieren möchten, die noch nicht authentifiziert oder registriert sind.

Sie können die beiden Filter auch mit der Logik von `AND` kombinieren, falls gewünscht. Dadurch wird das Formular nur Nutzern:innen angezeigt, denen sowohl eine E-Mail Adresse als auch eine externe ID fehlt - ideal für die Erfassung neuer Leads oder die Aufforderung zur Kontoerstellung.

## Schritt 4: Zielbenutzer, die das Formular ausgefüllt haben (optional)

Nachdem Sie das E-Mail-Erfassungsformular gestartet und die E-Mail-Adressen Ihrer Nutzer:innen gesammelt haben, können Sie die Nutzer:innen, die das Formular ausgefüllt haben, als Zielgruppe zusammenstellen.

1. Wählen Sie in jedem Segmente-Filter in Braze den Filter `Clicked/Opened Campaign` aus. 
2. Wählen Sie aus der Dropdown-Liste `clicked in-app message button 1`
3. Wählen Sie Ihre E-Mail-Erfassungsformular-Kampagne aus.

