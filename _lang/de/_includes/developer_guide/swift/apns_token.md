Bevor Sie eine iOS Push-Benachrichtigung mit Braze versenden können, müssen Sie Ihre `.p8` Push-Benachrichtigungsdatei hochladen, wie beschrieben in der [Entwickler:in Dokumentation von Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns):

1. Gehen Sie in Ihrem Apple-Entwicklerkonto zu [**Zertifikate, Kennungen & Profile**](https://developer.apple.com/account/ios/certificate).
2. Wählen Sie unter **Schlüssel** die Option **Alle** und klicken Sie auf die Schaltfläche Hinzufügen (+) in der oberen rechten Ecke.
3. Geben Sie unter **Schlüsselbeschreibung** einen eindeutigen Namen für den Signierschlüssel ein.
4. Aktivieren Sie unter **Wichtige Dienste** das Kontrollkästchen **Apple Push Notification Service (APNs)** und klicken Sie dann auf **Weiter**. Klicken Sie auf **Bestätigen**.
5. Notieren Sie sich die ID des Schlüssels. Klicken Sie auf **Download**, um den Schlüssel zu generieren und herunterzuladen. Stellen Sie sicher, dass Sie die heruntergeladene Datei an einem sicheren Ort speichern, da Sie sie nur einmal herunterladen können.
6. Gehen Sie in Braze zu **Einstellungen** > **App-Einstellungen** und laden Sie die Datei `.p8` unter **Apple Push Certificate** hoch. Sie können entweder Ihr Entwicklungs- oder Ihr Produktions-Push-Zertifikat hochladen. Um Push-Benachrichtigungen zu testen, nachdem Ihre App live im App Store ist, empfiehlt es sich, einen separaten Arbeitsbereich für die Entwicklungsversion Ihrer App einzurichten.
7. Wenn Sie dazu aufgefordert werden, geben Sie die [Bundle ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), die [Key ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) und die [Team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) Ihrer App ein. Sie müssen auch angeben, ob die Benachrichtigungen an die Entwicklungs- oder die Produktionsumgebung Ihrer App gesendet werden sollen, die durch ihr Bereitstellungsprofil definiert ist. 
8. Wenn Sie fertig sind, wählen Sie **Speichern**.

