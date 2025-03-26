---
nav_title: Häufige Push-Fehlermeldungen
article_title: Häufige Push-Fehlermeldungen
page_order: 2

page_type: solution
description: "Dieser Hilfeartikel behandelt häufige Push-Fehlermeldungen für iOS und Android und führt Sie durch mögliche Lösungen."
channel: push
platform:
- iOS
- Android
---

# Häufige Push-Fehlermeldungen

Sehen Sie sich diese häufigen Fehlermeldungen für Push-Nachrichten an:

{% tabs %}
{% tab Android %} 
### Push prallte ab: MismatchSenderId
`MismatchSenderId` weist auf eine fehlgeschlagene Authentifizierung hin. Firebase Cloud Messaging (FCM) authentifiziert sich mit einigen Schlüsseldaten: Absender-ID und FCM API-Schlüssel.  Diese sollten beide auf ihre Genauigkeit überprüft werden. Weitere Informationen finden Sie in der [Android-Dokumentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) zu diesem Thema.

Häufige Fehler können sein:
- Schlechte [AbsenderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Mehrfache Registrierung, wenn sie sich bei einem anderen Push-Dienst mit einer anderen Absender-ID registrieren

### Push prallte ab: InvalidRegistration
`InvalidRegistration` kann passieren, wenn ein Push-Token falsch geformt ist. Häufige Fehler können sein, wenn:
- Die Leute geben Braze-Registrierungstoken manuell weiter, rufen aber nicht `getToken()` auf. Sie können zum Beispiel die gesamte Instanz-ID übergeben. Das Token in der Fehlermeldung sieht aus wie `&#124;ID&#124;1&#124;:[regular token]`.  
- Die Menschen registrieren sich bei mehreren Diensten. Wir erwarten derzeit, dass Push-Registrierungsintentionen im alten Stil ankommen. Wenn sich also Leute an mehreren Stellen registrieren und wir Intents von anderen Diensten abfangen, können wir missgebildete Push-Token erhalten.

### Push prallte ab: NichtRegistriert
`NotRegistered` bedeutet in der Regel, dass die App vom Gerät gelöscht wurde (wie unser Signal für die Deinstallation). Dies kann auch vorkommen, wenn eine Mehrfachregistrierung stattfindet und eine zweite Registrierung das Push-Token, das Braze erhält, ungültig macht.

{% endtab %}
{% tab iOS %}

### Push prallte ab: Fehler beim Senden an falsches Push-Token

Dieser Fehler kann aus verschiedenen Gründen auftreten:
- Das Push-Token wird nicht korrekt an uns gesendet in `[[Appboy sharedInstance] registerPushToken:]`
	- Prüfen Sie das Token im **Nachrichten-Aktivitätsprotokoll**. Sie sollte im Allgemeinen wie eine lange Reihe von Buchstaben und Zahlen aussehen. (e.g `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`) Wenn dies nicht der Fall ist, überprüfen Sie den Code, der für das Senden von Braze Push-Token-Fehlern verantwortlich ist.<br><br>
- Ungeeignete Bereitstellungsumgebung:
	- Wenn Sie sich mit einem Entwicklungszertifikat registrieren und versuchen, mit einem Produktionszertifikat zu senden, können Sie diesen Fehler sehen.  
	- Braze unterstützt nur universelle Zertifikate für Produktionsumgebungen. Das Testen von Push in Entwicklungsumgebungen mit einem universellen Zertifikat wird nicht funktionieren. 
	- Dieser Bericht sendet Bouncing in der Produktion, aber nicht in der Entwicklung.<br><br>
- Unpassendes Bereitstellungsprofil:
	- Das kann passieren, wenn Ihr Zertifikat nicht mit dem Zertifikat übereinstimmt, das zum Abrufen des Tokens verwendet wurde. Wenn dies vermutet wird, sind die nächsten Schritte:
		- Stellen Sie sicher, dass das Push-Zertifikat, das zum Senden von Push-Nachrichten aus dem Braze-Dashboard verwendet wird, und das Bereitstellungsprofil korrekt konfiguriert sind.
		- Erstellen Sie das APNS-Zertifikat neu und erstellen Sie dann das Bereitstellungsprofil neu, nachdem das APNS-Zertifikat auf `app_id` konfiguriert wurde. Dies kann manchmal einige sichtbare Probleme lösen.

### Push prallte ab: APNS Feedback-Dienst entfernt

Dies geschieht in der Regel, wenn jemand das Programm deinstalliert. Braze fragt jede Nacht den APNS Feedback Service ab, um eine Liste der ungültigen Token zu erhalten. Weitere Informationen finden Sie in Apples [Kommunikation mit APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).


{% endtab %}
{% endtabs %}

_Zuletzt aktualisiert am 24\. Januar 2021_
