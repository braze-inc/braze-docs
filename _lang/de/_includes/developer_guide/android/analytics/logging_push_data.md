## Protokollierung von Daten mit der Braze API (empfohlen)

Sie können Analytics in Realtime protokollieren, indem Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) anrufen. Um Analytics zu protokollieren, senden Sie den Wert `braze_id` aus dem Braze-Dashboard, um das zu aktualisierende Nutzerprofil zu identifizieren.

![Personalisiertes Push Dashboard Beispiel]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Manuelles Aufzeichnen von Daten

Je nach den Details Ihrer Nutzlast können Sie Analytics manuell innerhalb Ihrer `FirebaseMessagingService.onMessageReceived` Implementierung oder Ihrer Startaktivitäten protokollieren. Denken Sie daran, dass Ihre `FirebaseMessagingService` Unterklasse die Ausführung innerhalb von 9 Sekunden nach dem Aufruf beenden muss, um zu vermeiden, dass sie vom Android-System [markiert oder beendet](https://firebase.google.com/docs/cloud-messaging/android/receive) wird.
