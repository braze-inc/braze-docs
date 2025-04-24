## Verwendung des Google Tag Managers:in {#initialization-tag}

### Schritt 1: Push-Einrichtung (optional)

Wenn Sie die Möglichkeit haben möchten, Push-Nachrichten über den Google Tag Manager zu senden, befolgen Sie zunächst die Richtlinien zur [Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web):
1. Konfigurieren Sie die Service Worker-Datei Ihrer Website und speichern Sie sie im Stammverzeichnis Ihrer Website.
2. Browserregistrierung einrichten - Nachdem der Service Worker konfiguriert ist, müssen Sie die Methode `braze.requestPushPermission()` entweder nativ in ihrer App oder über ein benutzerdefiniertes HTML-Tag (über das GTM-Dashboard) einrichten. Außerdem müssen Sie sicherstellen, dass das Tag nach der Initialisierung des SDK ausgelöst wird.

### Schritt 2: Initialisierungs-Tag auswählen

Suchen Sie in der Template-Galerie der Community nach Braze und wählen Sie das **Braze Initialisierungs-Tag** aus.

![Dialogfeld mit den Konfigurationseinstellungen des Braze Initialisierungs-Tags. Zu den Einstellungen gehören "Tag-Typ", "API-Schlüssel", "API-Endpunkt", "SDK-Version", "Externe Nutzer-ID" und "Safari Web-Push-ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Schritt 3: Einstellungen konfigurieren

Geben Sie Ihren Braze-API-App-Identifizierungsschlüssel und den SDK-Endpunkt ein, die Sie auf der Seite **Einstellungen verwalten** in Ihrem Dashboard finden. Geben Sie die neueste Version des Web SDK im Format `major.minor` ein. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.

### Schritt 4: Wählen Sie Initialisierungsoptionen

Wählen Sie aus den optionalen zusätzlichen Initialisierungsoptionen, die im Leitfaden [Ersteinrichtung]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) ) beschrieben sind, die gewünschten Optionen aus.

### Schritt 5: Überprüfen und QA durchführen

Nachdem Sie das Tag bereitgestellt haben, gibt es zwei Möglichkeiten, um die ordnungsgemäße Integration zu überprüfen:

1. Wenn Sie das [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager verwenden, sollten Sie sehen, dass das Braze Initialization Tag auf Ihren konfigurierten Seiten oder Ereignissen ausgelöst wurde.
2. Sie sollten sehen, dass Netzwerkanforderungen an Braze gestellt werden, und die globale Bibliothek `window.braze` sollte jetzt auf Ihrer Webseite definiert sein.
