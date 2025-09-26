## Verwendung der Push-Fehlerprotokolle

Braze stellt Fehler bei Push-Benachrichtigungen im Nachrichten-Aktivitätsprotokoll bereit. Dieses Fehlerprotokoll enthält eine Reihe von Warnungen, die sehr hilfreich sein können, um festzustellen, warum Ihre Kampagnen nicht wie erwartet funktionieren. Wenn Sie auf eine Fehlermeldung klicken, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Sie bei der Fehlerbehebung unterstützt.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## Fehlerszenarien

### Keine Anzeige von "push-registrierten" Nutzern im Dashboard (vor dem Senden von Nachrichten)

- Stellen Sie sicher, dass Ihre App richtig konfiguriert ist, um Push-Benachrichtigungen zuzulassen.
- Vergewissern Sie sich, dass die in Ihrem Braze-Dashboard konfigurierte Client-ID und das Client-Geheimnis korrekt sind.

### Push-Benachrichtigungen werden auf den Geräten der Benutzer nicht angezeigt

Es gibt einige Gründe, warum dies der Fall sein könnte:

- Wenn Sie Ihre Anwendung zwangsbeenden, werden Ihre Push-Benachrichtigungen nicht angezeigt, wenn die App nicht läuft.
- Vergewissern Sie sich, dass die Einstellung [Benachrichtigungspriorität]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) ] in Ihrer Kampagne auf `HIGH` gesetzt ist.
- Der ADM API-Schlüssel in Ihrem `api_key.txt` ist falsch oder enthält ungültige Zeichen.
- Die `BrazeAmazonDeviceMessagingReceiver` ist nicht richtig in `AndroidManifest.xml` mit Absichtsfiltern für `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` und `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />` registriert.

### "Push-registrierte" Benutzer werden nach dem Senden von Nachrichten nicht mehr aktiviert

Dies ist in der Regel der Fall, wenn Nutzer die Anwendung deinstalliert haben, da die ADM-Registrierungs-ID durch die Deinstallation ungültig wird.
