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

> Auf dieser Seite finden Sie häufige Fehlermeldungen für Push Messaging.

{% tabs %}
{% tab Android %} 
### Push prallte ab: MismatchSenderId
`MismatchSenderId` weist auf eine fehlgeschlagene Authentifizierung hin. Firebase Cloud Messaging (FCM) authentifiziert sich mit ein paar wichtigen Daten: Absender-ID und FCM API-Schlüssel.  Diese sollten beide auf ihre Genauigkeit überprüft werden. Weitere Informationen finden Sie in der [Android-Dokumentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) zu diesem Problem.

Häufige Fehler können sein:
- Schlechte [AbsenderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Mehrfache Registrierung, wenn sie sich bei einem anderen Push Dienst mit einer anderen Absender-ID registrieren

### Push prallte ab: InvalidRegistration
`InvalidRegistration` kann vorkommen, wenn ein Push-Token falsch geformt ist. Häufige Fehler können sein, wenn:
- Die Benutzer geben die Token für die Braze-Registrierung manuell weiter, rufen aber nicht `getToken()` auf. Sie können zum Beispiel die gesamte ID der Instanz übergeben. Das Token in der Fehlermeldung sieht aus wie `&#124;ID&#124;1&#124;:[regular token]`.  
- Die Menschen melden sich bei mehreren Diensten an. Wir erwarten derzeit, dass Push-Registrierungsabsichten im alten Stil ankommen. Wenn sich also Leute an mehreren Stellen registrieren und wir Absichten von anderen Diensten abfangen, können wir missgebildete Push-Token erhalten.

### Push prallte ab: NotRegistered
`NotRegistered` bedeutet in der Regel, dass die App vom Gerät gelöscht wurde (wie unser Signal für die Deinstallation). Dies kann auch vorkommen, wenn eine Mehrfachregistrierung stattfindet und eine zweite Registrierung das Push-Token, das Braze erhält, ungültig macht.

{% endtab %}
{% tab iOS %}

### Push prallte ab: BadToken

Der Fehler `BadToken` kann aus verschiedenen Gründen auftreten:
- Der Push-Token wird nicht korrekt an uns gesendet in `[[Appboy sharedInstance] registerPushToken:]`
	- Prüfen Sie das Token im [Protokoll der Nachrichtenaktivität]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Er sollte im Allgemeinen wie ein langer String aus Buchstaben und Zahlen aussehen (z. B. `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Wenn dies nicht der Fall ist, überprüfen Sie den Code, der für das Senden von Braze Push-Token-Fehlern verantwortlich ist.<br><br>
- Ungeeignete Bereitstellungsumgebung:
	- Wenn Sie sich mit einem Entwickler:in-Zertifikat registrieren und versuchen, mit einem Produktionszertifikat zu senden, können Sie diesen Fehler sehen.  
	- Braze unterstützt nur universelle Zertifikate für Produktionsumgebungen. Das Testen von Push in Entwicklungsumgebungen mit einem universellen Zertifikat wird nicht funktionieren. 
	- Dieses Reporting sendet Bouncing in der Produktion, aber nicht in der Entwicklung.<br><br>
- Unpassendes Profil für die Bereitstellung:
	- Das kann passieren, wenn Ihr Zertifikat nicht mit dem übereinstimmt, das zum Abrufen des Tokens verwendet wurde. Wenn dies vermutet wird, sind die nächsten Schritte:
		- Stellen Sie sicher, dass das Push-Zertifikat, das zum Senden von Push aus dem Braze-Dashboard verwendet wird, und das Profil für die Bereitstellung korrekt konfiguriert sind.
		- Erstellen Sie das APNS-Zertifikat neu und erstellen Sie dann das Profil neu, nachdem das APNS-Zertifikat auf `app_id` konfiguriert wurde. Dies kann manchmal einige sichtbare Probleme lösen.

### Push prallte ab: APNS Feedback Dienst entfernt

Dies geschieht in der Regel, wenn jemand das Programm deinstalliert. Braze fragt jede Nacht den APNS Feedback Service ab, um eine Liste der ungültigen Token zu erhalten. Weitere Informationen finden Sie in Apples [Kommunikation mit APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}
