---
nav_title: Uninstall-Tracking
article_title: Tracking für iOS deinstallieren
platform: iOS
page_order: 7
description: "Dieser Artikel beschreibt die Konfiguration des Uninstall-Trackings für Ihre iOS-App."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uninstall-Tracking für iOS

> In diesem Artikel erfahren Sie, wie Sie das Uninstall-Tracking für Ihre iOS-Anwendung konfigurieren und wie Sie testen können, damit Ihre App keine unerwünschten automatischen Aktionen ausführt, wenn Sie einen Push zum Uninstall-Tracking von Braze erhalten.

Das Uninstall-Tracking verwendet Push-Benachrichtigungen im Hintergrund mit einem Braze-Flag in der Payload. Weitere Informationen finden Sie unter [Uninstall-Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) in unserem Benutzerhandbuch.

## Schritt 1: Background Push aktivieren

Vergewissern Sie sich, dass Sie die Option **Remote-Benachrichtigungen** im Abschnitt **Hintergrundmodi** auf dem Tab **Fähigkeiten** Ihres Xcode-Projekts aktiviert haben. Weitere Einzelheiten finden Sie in unserer Dokumentation zur [stillen Push-Benachrichtigung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/).

## Schritt 2: Braze Background Push prüfen

Braze verwendet Push-Benachrichtigungen im Hintergrund, um Analytics für das Tracking von Deinstallationen zu sammeln. Stellen Sie sicher, dass Ihre Anwendung [keine unerwünschten Aktionen durchführt]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/ignoring_internal_push/), wenn Sie unsere Benachrichtigungen zum Uninstall-Tracking erhalten.

## Schritt 3: Im Dashboard testen

Als Nächstes senden Sie sich selbst einen Test-Push vom Dashboard aus. Dieser Push-Test wird Ihr Nutzerprofil nicht aktualisieren.

1. Erstellen Sie auf der Seite **Kampagnen** eine Push-Benachrichtigungskampagne und wählen Sie **iOS Push** als Plattform.<br><br>
2. Fügen Sie auf der Seite **Einstellungen** den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu und markieren Sie **Add Content-Available Flag**.<br><br>
3. Verwenden Sie die Seite **Vorschau**, um sich selbst einen Test-Push für das Tracking zu senden.<br><br>
4. Vergewissern Sie sich, dass Ihre App beim Empfang des Push keine unerwünschten automatischen Aktionen ausführt.

{% alert important %}
Diese Testschritte sind ein Proxy für das Senden eines Uninstall-Tracking-Push von Braze. Wenn Sie die Badge-Zählung aktiviert haben, wird eine Badge-Nummer zusammen mit dem Push für den Test gesendet, aber die Uninstall-Tracking-Pushes von Braze setzen keine Badge-Nummer in Ihrer Anwendung.
{% endalert %}

## Schritt 4: Uninstall-Tracking aktivieren

Folgen Sie den Anweisungen zur [Aktivierung der Deinstallationsverfolgung]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

