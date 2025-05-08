---
nav_title: Migration zu Firebase Cloud Messaging
article_title: Migration zur Firebase Cloud Messaging API
platform: Android
page_order: 29
description: "Dieser Artikel beschreibt, wie Sie von der veralteten Cloud Messaging API von Google zu Firebase Cloud Messaging (FCM) migrieren."
channel:
  - push
search_rank: 3
---

# Migration zur Firebase Cloud Messaging API

> Erfahren Sie, wie Sie von Googles veralteter Cloud Messaging API auf die vollständig unterstützte Firebase Cloud Messaging (FCM) API migrieren können. Weitere Informationen finden Sie in Googles [Firebase FAQ - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
Wenn Sie die Push Integration für Android zum ersten Mal einrichten, lesen Sie stattdessen [Standard Android Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration).
{% endalert %}

## Rate-Limit

Die Firebase Cloud Messaging (FCM) API hat ein standardmäßiges Rate-Limit von 600.000 Anfragen pro Minute. Wenn Sie dieses Limit erreichen, wird Braze es in einigen Minuten automatisch erneut versuchen. Um eine Erhöhung anzufordern, wenden Sie sich an den [Firebase Support](https://firebase.google.com/support).

## Migration zu FCM

### Schritt 1: Überprüfen Sie Ihre Project ID

Öffnen Sie zunächst Google Cloud. Überprüfen Sie auf der Startseite Ihres Projekts die Nummer im Feld **Project ID**, die Sie als nächstes mit der Nummer in Ihrem Firebase-Projekt vergleichen werden.

![Die Startseite des Google Cloud-Projekts mit hervorgehobener "Project ID".]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

Als nächstes öffnen Sie die Firebase-Konsole und wählen Sie <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü "Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Überprüfen Sie auf dem Tab **Allgemein**, ob die **Projekt ID** mit der in Ihrem Google Cloud Projekt aufgeführten ID übereinstimmt.

![Die Seite "Einstellungen" des Firebase-Projekts mit hervorgehobener "Projekt ID".]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### Schritt 2: Sender ID prüfen

Öffnen Sie zunächst Braze und wählen Sie dann <i class="fa-solid fa-gear"></i> **Einstellungen** > **App-Einstellungen**.

![Das Menü "Einstellungen" wird in Braze geöffnet und "App-Einstellungen" hervorgehoben.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Überprüfen Sie in den **Einstellungen für Push-Benachrichtigungen** Ihrer Android App die Nummer im Feld **Firebase Cloud Messaging Sender ID**, die Sie als Nächstes mit der Nummer in Ihrem Firebase-Projekt vergleichen werden.

![Das Formular für "Push-Benachrichtigung Einstellungen".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

Als nächstes öffnen Sie die Firebase-Konsole und wählen Sie <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü "Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messaging** auswählen Überprüfen Sie unter **Cloud Messaging API (Legacy)**, ob die **ID des Senders** mit der in Ihrem Braze-Dashboard aufgeführten ID übereinstimmt.

![Die Seite "Cloud Messaging" des Firebase-Projekts mit hervorgehobener "Sender-ID".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### Schritt 3: Firebase Cloud Messaging API aktivieren

Wählen Sie in Google Cloud das Projekt aus, das Ihre Android-App verwendet, und aktivieren Sie dann die [Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![Aktivierung der Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Schritt 4: Ein Dienst-Konto erstellen

Als nächstes erstellen Sie ein neues Dienst-Konto, damit Braze bei der Registrierung von FCM-Tokens autorisierte API-Aufrufe tätigen kann. Gehen Sie in Google Cloud zu **Servicekonten** und wählen Sie dann Ihr Projekt aus. Auf der Seite **Serviceleistungen; Dienste** wählen Sie **Servicekonto erstellen**.

![Die Startseite des Dienstkontos eines Projekts mit der Hervorhebung "Dienstkonto erstellen".]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Geben Sie einen Namen, eine ID und eine Beschreibung für das Dienstkonto ein und wählen Sie **Erstellen und fortfahren**.

![Das Formular für "Details zum Dienstkonto".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

Suchen Sie im Feld **Rolle** nach **Firebase Cloud Messaging API Admin** und wählen Sie es in der Liste der Rollen aus. Für einen restriktiveren Zugriff erstellen Sie eine [angepasste Rolle](https://cloud.google.com/iam/docs/creating-custom-roles) mit der Berechtigung `cloudmessaging.messages.create` und wählen diese dann aus der Liste aus. Wenn Sie fertig sind, wählen Sie **Fertig**.

{% alert warning %}
Stellen Sie sicher, dass Sie _Firebase Cloud Messaging **API** Admin_ auswählen, nicht _Firebase Cloud Messaging Admin_.
{% endalert %}

![Das Formular für "Diesem Dienstkonto Zugriff auf das Projekt gewähren", wobei "Firebase Cloud Messaging API Admin" als Rolle ausgewählt ist.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Schritt 5: Berechtigungen überprüfen (optional)

Um zu überprüfen, welche Berechtigungen Ihr Dienst-Konto hat, öffnen Sie Google Cloud, gehen Sie dann zu Ihrem Projekt und wählen Sie **IAM**. Wählen Sie unter **Ansicht nach Auftraggebern** die Option **Überschüssige Berechtigungen** aus.

![Der Tab "Ansicht nach Prinzipien" mit der Anzahl der überschüssigen Berechtigungen für jeden Prinzipal.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

Jetzt können Sie die aktuellen Berechtigungen überprüfen, die Ihrer ausgewählten Rolle zugewiesen sind.

![Die Liste der aktuellen Berechtigungen, die der ausgewählten Rolle zugewiesen sind.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### Schritt 6: JSON-Zugangsdaten generieren

Als nächstes generieren Sie JSON-Zugangsdaten für Ihr FCM Dienst-Konto. Gehen Sie in Google Cloud IAM & Admin auf **Dienstkonten** und wählen Sie Ihr Projekt aus. Suchen Sie das FCM Dienst-Konto [, das Sie zuvor erstellt haben](#step-4-create-a-service-account), und wählen Sie dann <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > Schlüssel verwalten.

![Die Startseite des Projektdienstkontos mit geöffnetem Menü "Aktionen".]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Wählen Sie **Schlüssel hinzufügen** > **Neuen Schlüssel erstellen**.

{% alert note %}
Wenn Sie einen neuen Schlüssel erstellen, werden Ihre alten nicht gelöscht. Wenn Sie Ihren neuen Schlüssel versehentlich löschen, indem Sie **Zugangsdaten zurücksetzen** auswählen, verwendet Braze Ihre alten Schlüssel als Backup.
{% endalert %}

![Das ausgewählte Dienstkonto mit dem geöffneten Menü "Schlüssel hinzufügen".]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Wählen Sie **JSON** und wählen Sie dann **Erstellen**. Wenn Sie Ihr Dienstkonto mit einer anderen Google Cloud Projekt ID als Ihrer FCM Projekt ID erstellt haben, müssen Sie den der `project_id` zugewiesenen Wert in Ihrer JSON-Datei manuell aktualisieren.

Merken Sie sich, wo Sie den Schlüssel heruntergeladen haben - Sie brauchen ihn im nächsten Schritt.

![Das Formular zur Erstellung eines Private Key mit "JSON" ausgewählt.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Private Keys können ein Sicherheitsrisiko darstellen, wenn sie kompromittiert werden. Speichern Sie Ihre JSON-Zugangsdaten vorerst an einem sicheren Standort - Sie werden Ihren Schlüssel löschen, nachdem Sie ihn auf Braze hochgeladen haben.
{% endalert %}

### Schritt 7: Laden Sie Ihre JSON Zugangsdaten zu Braze hoch

Wählen Sie in Braze <i class="fa-solid fa-gear"></i> **Einstellungen** > **App-Einstellungen**.

![Das Menü "Einstellungen" wird in Braze geöffnet und "App-Einstellungen" hervorgehoben.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Wählen Sie unter **Einstellungen für Push-Benachrichtigungen** die Option **JSON-Datei hochladen** und wählen Sie dann die Datei aus, [die Sie zuvor erstellt haben](#step-6-generate-json-credentials). Wenn Sie fertig sind, wählen Sie **Speichern**.

![Das Formular für "Push-Benachrichtigungseinstellungen" mit dem aktualisierten Private Key im Feld "Firebase Cloud Messaging Server Key".]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Private Keys können ein Sicherheitsrisiko darstellen, wenn sie kompromittiert werden. Jetzt, wo Ihr Schlüssel auf Braze hochgeladen ist, löschen Sie die Datei [, die Sie zuvor erzeugt haben](#step-6-generate-json-credentials), von Ihrem Computer.
{% endalert %}

### Schritt 8: Testen Sie Ihre neuen Zugangsdaten (optional)

Sobald Sie Ihre Zugangsdaten auf Braze hochgeladen haben, können Sie damit beginnen, Push-Benachrichtigungen mit Ihren neuen Zugangsdaten zu versenden. Um Ihre neuen Zugangsdaten zu testen, senden Sie mit FCM oder Braze eine echte oder eine Test-Push-Benachrichtigung an Ihre App. Wenn die Push-Benachrichtigung ankommt, ist alles in Ordnung. Wenn nicht:

- [Überprüfen Sie Ihre Sender-ID](#step-2-verify-your-sender-id)
- [Überprüfen Sie Ihre Berechtigungen](#step-5-verify-permissions-optional)
- Überprüfen Sie Fehler bei Push-Benachrichtigungen in Ihrem [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

Wenn Sie immer noch Probleme haben, lesen Sie den Abschnitt [Wiederherstellen Ihrer Zugangsdaten](#reverting-your-credentials).

## Zurücksetzen der Zugangsdaten

Sie können Ihre neuen Zugangsdaten jederzeit löschen und Ihre alten Zugangsdaten wiederherstellen. Sobald Ihre Zugangsdaten wiederhergestellt sind, können Sie stattdessen Push-Benachrichtigungen mit Ihren alten Zugangsdaten versenden.

Wählen Sie in Braze <i class="fa-solid fa-gear"></i> **Einstellungen** > **App-Einstellungen**. Wählen Sie unter **Einstellungen für Push-Benachrichtigungen** **Zugangsdaten wiederherstellen** aus.

{% alert warning %}
Wenn Sie Ihre neuen Zugangsdaten löschen, können Sie sie später nicht wiederherstellen. Sie müssen [neue Zugangsdaten erstellen](#step-6-generate-json-credentials) und diese erneut [in Braze hochladen](#step-7-upload-your-json-credentials-to-braze).
{% endalert %}

![Das Formular für "Einstellungen für Push-Benachrichtigungen" mit dem hervorgehobenen Button "Zugangsdaten wiederherstellen".]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## Häufig gestellte Fragen (FAQ) {#faq}

### Woher weiß ich, dass meine neuen Zugangsdaten funktionieren?

Ihre neuen Zugangsdaten funktionieren, sobald Sie sie in Braze hochgeladen haben. Um sie zu testen, wählen Sie **Zugangsdaten testen**. Wenn Sie einen Fehler erhalten, können Sie [Ihre Anmeldedaten jederzeit zurücksetzen](#reverting-your-credentials).

### Muss ich für meine nicht genutzten Apps oder Entwickler:innen zu FCM migrieren?

Nein. Ihre ungenutzten Apps und Entwicklungs-Apps werden jedoch weiterhin eine Warnung anzeigen, die Sie zur Migration auffordert. Um diese Nachricht zu entfernen, können Sie entweder neue Zugangsdaten hochladen oder diese Apps aus Ihrem Workspace löschen. Wenn Sie sich dafür entscheiden, diese Apps zu löschen, sollten Sie sich vorher bei Ihrem Team erkundigen, ob jemand diese Apps benutzt.

### Wo kann ich Fehlermeldungen überprüfen?

Sie können Fehler bei Push-Benachrichtigungen in Ihrem [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überprüfen.

### Muss ich vor der Migration meine App oder mein SDK aktualisieren?

Nein. Sie müssen nur Ihre neuen Zugangsdaten auf Braze hochladen.

### Muss ich zuerst meine alten Zugangsdaten löschen?

Nein. Sollten Sie Ihre neuen Zugangsdaten einmal löschen müssen, [können Sie stattdessen Ihre alten Zugangsdaten verwenden](#reverting-your-credentials).

### Warum erscheint nach der Migration immer noch eine Warnmeldung in Braze?

Diese Warnung wird weiterhin angezeigt, wenn sich in Ihrem Workspace mindestens eine Android App befindet, die noch migriert werden muss. Stellen Sie sicher, dass Sie alle Ihre Android Apps auf die vollständig unterstützte FCM API von Google migrieren.

### Wie lange dauert es nach der Migration, bis ich wieder Push-Benachrichtigungen versenden kann?

Nach der Migration können Sie sofort damit beginnen, Push-Benachrichtigungen mit Ihren neuen Zugangsdaten zu versenden.

### Was ist, wenn ich mein Dienst-Konto in einem anderen Projekt als meinem FCM-Projekt erstellt habe?

Wenn Sie Ihr Dienstkonto mit einer anderen Google Cloud Projekt ID als Ihrer FCM Projekt ID erstellt haben, müssen Sie den der `project_id` zugewiesenen Wert in Ihrer JSON-Datei manuell aktualisieren, [nachdem Sie einen neuen erstellt haben](#step-6-generate-json-credentials).
