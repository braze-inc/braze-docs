---
nav_title: Übliche Push-Fehlermeldungen
article_title: Allgemeine Push-Fehlermeldungen
page_order: 22
page_type: reference
description: "Dieser Artikel behandelt häufige Push-Fehlermeldungen für iOS und Android und zeigt Ihnen mögliche Lösungen auf."
channel: push
platform:
- iOS
- Android
---

# Übliche Push-Fehlermeldungen

> Auf dieser Seite finden Sie häufige Fehlermeldungen für Push-Messaging.

{% tabs %}
{% tab Android %} 
### Push-Absprung: MismatchSenderId
`MismatchSenderId` weist auf eine fehlgeschlagene Authentifizierung hin. Firebase Cloud Messaging (FCM) authentifiziert sich mit einigen wichtigen Daten: der Sender-ID und dem FCM-API-Schlüssel. Beide sollten auf ihre Richtigkeit überprüft werden. Weitere Informationen finden Sie in der [Android-Dokumentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) zu diesem Problem.

Häufige Fehler können sein:
- Fehlerhafte [Sender-ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Mehrfache Registrierung, wenn sich Nutzer:innen bei einem anderen Push-Dienst mit einer anderen Sender-ID registrieren

### Push-Absprung: InvalidRegistration
`InvalidRegistration` kann auftreten, wenn ein Push-Token fehlerhaft formatiert ist. Häufige Fehler können auftreten, wenn:
- Nutzer:innen die Token für die Braze-Registrierung manuell übergeben, aber nicht `getToken()` aufrufen. Sie können zum Beispiel die gesamte Instanz-ID übergeben. Das Token in der Fehlermeldung sieht dann aus wie `&#124;ID&#124;1&#124;:[regular token]`.  
- Nutzer:innen sich bei mehreren Diensten registrieren. Wir erwarten derzeit, dass Push-Registrierungsabsichten im alten Stil ankommen. Wenn sich also Nutzer:innen an mehreren Stellen registrieren und wir Absichten von anderen Diensten abfangen, können fehlerhafte Push-Token entstehen.

### Push-Absprung: NotRegistered {#notregistered}
`NotRegistered` bedeutet in der Regel, dass die App vom Gerät gelöscht wurde (z. B. als Signal für eine Deinstallation). Dies kann auch auftreten, wenn eine Mehrfachregistrierung stattfindet und eine zweite Registrierung das Push-Token, das Braze erhält, ungültig macht.

### DEVICE_UNREGISTERED {#device-unregistered}

Dieser Fehler erscheint im Nachrichtenaktivitätsprotokoll als:

`Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Dies tritt in der Regel aus einem der folgenden Gründe auf:

- Die Nutzer:innen haben die App deinstalliert. Dies ist die häufigste Ursache. Wenn die App von einem Gerät entfernt wird, wird das Push-Token ungültig.
- Die Push-Zugangsdaten wurden in der App aktualisiert. Wenn Ihr Team die FCM-Zugangsdaten oder die in der App gebündelten Zertifikate geändert hat, haben Nutzer:innen, die sich mit den vorherigen Zugangsdaten registriert haben, ungültige Token, bis die App sie erneut registriert.
- Benutzerdefinierte Logik meldet Nutzer:innen von Push ab. Dies ist selten, aber es ist technisch möglich, ein Gerät programmatisch über das Firebase/Android SDK von Push abzumelden.

{% alert note %}
Dieser Fehler bedeutet nicht, dass Push für die Nutzer:innen deaktiviert ist – nur, dass ein bestimmtes Token aus ihrem Profil entfernt wurde. Dies ist häufig bei Nutzer:innen, die Funktionen testen und die App regelmäßig installieren und deinstallieren. Um zu prüfen, ob die Nutzer:innen noch gültige Token haben, gehen Sie zur **Nutzersuche** und überprüfen Sie den Abschnitt **Kontakteinstellungen** auf dem Tab **Engagement**.
{% endalert %}

{% endtab %}
{% tab iOS %}

### Fehler beim Senden der Push-Benachrichtigung, da die Payload ungültig war

Diese Nachricht kann im Nutzerprofil auf dem Tab **Engagement** unter **Kontakteinstellungen** > **Push-Changelog** angezeigt werden, wenn der Apple Push Notification Service (APNs) die Push-Anfrage aufgrund einer ungültigen Payload ablehnt.

In Braze kann diese Dashboard-Nachricht einem der folgenden APNs-Fehlergründe zugeordnet werden:

- `PayloadEmpty`: Die Payload enthielt nicht die erforderlichen Inhalte für die Art der gesendeten Push-Nachricht.
- `PayloadTooLarge`: Die Payload hat die maximale Payload-Größe von APNs überschritten.

Häufige Ursachen sind:

- Angepasste Schlüssel (und deren Werte), die die Payload zu groß machen (dies kann unerwartet große Liquid-gerenderte Werte umfassen).
- Ein leerer oder fehlender Alert oder Body, wo erforderlich (oder eine anderweitig fehlerhafte `aps`-Payload).

Nächste Schritte:

- Reduzieren Sie die Payload-Größe, indem Sie angepasste Schlüssel entfernen und große dynamische Werte verkürzen.
- Wenn Sie über die API senden, überprüfen Sie die endgültige JSON-Payload (einschließlich Größe) vor dem Senden.

### Push-Absprung: BadToken

Der Fehler `BadToken` kann aus verschiedenen Gründen auftreten:
- Das Push-Token wird nicht korrekt an Braze gesendet (z. B. in `registerDeviceToken:` oder dem Äquivalent Ihrer Plattform).
	- Prüfen Sie das Token im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Es sollte im Allgemeinen wie ein langer String aus Buchstaben und Zahlen aussehen (z. B. `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Wenn dies nicht der Fall ist, überprüfen Sie den Code, der für das Senden des Push-Tokens an Braze verantwortlich ist.<br><br>
- Nicht übereinstimmende Bereitstellungsumgebung:
	- Wenn Sie sich mit einem Entwicklungszertifikat registrieren und versuchen, mit einem Produktionszertifikat zu senden, kann dieser Fehler auftreten.  
	- Braze unterstützt nur universelle Zertifikate für Produktionsumgebungen. Das Testen von Push in Entwicklungsumgebungen mit einem universellen Zertifikat funktioniert nicht. 
	- Dieses Reporting meldet Absprünge in der Produktion, aber nicht in der Entwicklung.<br><br>
- Nicht übereinstimmendes Bereitstellungsprofil:
	- Das kann passieren, wenn Ihr Zertifikat nicht mit dem übereinstimmt, das zum Abrufen des Tokens verwendet wurde. Wenn dies vermutet wird, sind die nächsten Schritte:
		- Stellen Sie sicher, dass das Push-Zertifikat, das zum Senden von Push aus dem Braze-Dashboard verwendet wird, und das Bereitstellungsprofil korrekt konfiguriert sind.
		- Erstellen Sie das APNS-Zertifikat neu und erstellen Sie dann das Bereitstellungsprofil neu, nachdem das APNS-Zertifikat auf die `app_id` konfiguriert wurde. Dies kann manchmal einige offensichtlichere Probleme lösen.

### Bundle-ID nicht zulässig

Der Fehler `TopicDisallowed` bedeutet, dass APNs die Push-Nachricht abgelehnt hat, weil das Topic (Bundle-ID) in der Anfrage für die verwendeten Authentifizierungs-Zugangsdaten nicht zulässig ist. Um dies zu beheben:

1. **Überprüfen Sie die Bundle-ID.** Stellen Sie sicher, dass die in Ihren Braze-App-Einstellungen konfigurierte Bundle-ID exakt mit der Bundle-ID Ihrer App übereinstimmt. Dies schließt alle Suffix-Varianten ein (z. B. `.debug`, `.staging`).
2. **Überprüfen Sie Ihre APNs-Authentifizierungseinrichtung.** Stellen Sie sicher, dass Ihre App mit dem richtigen APNs-`.p8`-Schlüssel konfiguriert ist und dass der Schlüssel mit demselben Apple Developer Team verknüpft ist wie die App, an die Sie senden.
3. **Bestätigen Sie die App-Umgebung.** Wenn Sie in Braze separate App-IDs für Entwicklungs- und Produktions-Builds haben, überprüfen Sie, ob jede mit den richtigen Push-Zugangsdaten und der richtigen Umgebung konfiguriert ist.

### Unregistered {#ios-unregistered}

Dieser Fehler erscheint im Nachrichtenaktivitätsprotokoll als:

`Received 'Unregistered' sending to '[Token String]'`

Dies ist das iOS-Äquivalent des Android-Fehlers [DEVICE_UNREGISTERED](#device-unregistered). Er tritt in der Regel aus einem der folgenden Gründe auf:

- Die Nutzer:innen haben die App deinstalliert. Dies ist die häufigste Ursache.
- Die Push-Zertifikate wurden aktualisiert. Wenn Ihr Team die APNs-Zertifikate geändert oder erneuert hat, haben Nutzer:innen, die sich mit den vorherigen Zertifikaten registriert haben, möglicherweise ungültige Token, bis die App sie erneut registriert.
- Benutzerdefinierte Logik meldet Nutzer:innen von Push ab. Dies ist selten, aber es ist technisch möglich, sich programmatisch über das iOS SDK von Remote-Benachrichtigungen abzumelden.

{% alert note %}
Dieser Fehler bedeutet nicht, dass Push für die Nutzer:innen deaktiviert ist – nur, dass ein bestimmtes Token aus ihrem Profil entfernt wurde. Um zu prüfen, ob die Nutzer:innen noch gültige Token haben, gehen Sie zur **Nutzersuche** und überprüfen Sie den Abschnitt **Kontakteinstellungen** auf dem Tab **Engagement**.
{% endalert %}

### InvalidProviderToken

Der Fehler `InvalidProviderToken` bedeutet, dass APNs die Anfrage abgelehnt hat, weil das Authentifizierungs-Token (von einem `.p8`-Schlüssel) oder das Push-Zertifikat (`.p12`) nicht mit der Bundle-ID oder Team-ID der App übereinstimmt. Um dies zu beheben:

1. **Überprüfen Sie Ihre Team-ID und Key-ID:** Wenn Sie einen `.p8`-Authentifizierungsschlüssel verwenden, stellen Sie sicher, dass die im Braze-Dashboard konfigurierte **Team-ID** und **Key-ID** (**Einstellungen** > **App-Einstellungen** > wählen Sie Ihre iOS-App aus) mit den Werten in Ihrem Apple Developer-Konto übereinstimmen.
2. **Überprüfen Sie die Bundle-ID:** Stellen Sie sicher, dass die in Braze registrierte Bundle-ID mit der Bundle-ID Ihrer App übereinstimmt. Eine Abweichung, wie z. B. eine andere Groß-/Kleinschreibung oder ein `.debug`-Suffix, verursacht diesen Fehler.
3. **Laden Sie den Schlüssel oder das Zertifikat erneut hoch:** Wenn der `.p8`-Schlüssel oder das `.p12`-Zertifikat kürzlich neu generiert oder widerrufen wurde, laden Sie den neuen Schlüssel in Braze hoch und entfernen Sie den alten.
4. **Bestätigen Sie die APNs-Umgebung:** Wenn Sie ein `.p12`-Zertifikat verwenden, überprüfen Sie, ob Sie beim Hochladen die richtige Umgebung (Entwicklung versus Produktion) ausgewählt haben. Für `.p8`-Schlüssel wird dies automatisch gehandhabt.

### Push-Absprung: APNS-Feedback-Dienst hat Token entfernt

Dies geschieht in der Regel, wenn jemand die App deinstalliert. Braze fragt jede Nacht den APNS Feedback Service ab, um eine Liste der ungültigen Token zu erhalten. Weitere Informationen finden Sie in Apples Dokumentation [Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}