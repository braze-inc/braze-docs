---
nav_title: Uninstall-Tracking
article_title: Tracking für iOS deinstallieren
platform: Swift
page_order: 7
description: "Dieser Artikel beschreibt die Konfiguration des Uninstall-Trackings für das Swift SDK."

---

# Uninstall-Tracking

> Erfahren Sie, wie Sie das Uninstall-Tracking für Ihre iOS-Anwendung einrichten, um sicherzustellen, dass Ihre App beim Empfang eines Uninstall-Tracking-Push von Braze keine unerwünschten automatischen Aktionen durchführt. Das Uninstall-Tracking verwendet Push-Benachrichtigungen im Hintergrund mit einem Braze-Flag in der Nutzlast. Allgemeine Informationen finden Sie unter [uninstall tracking][6].

{% alert important %}
Denken Sie daran, dass das Uninstall-Tracking ungenau sein kann. Die Metriken, die Sie auf Braze sehen, können verzögert oder ungenau sein.
{% endalert %}

## Schritt 1: Push im Hintergrund aktivieren

Gehen Sie in Ihrem Xcode-Projekt zu **Fähigkeiten** und stellen Sie sicher, dass die **Hintergrundmodi** aktiviert sind. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Schritt 2: Auf Braze Background-Push prüfen

Braze verwendet Push-Benachrichtigungen im Hintergrund, um Uninstall-Tracking-Analysen zu erfassen. Stellen Sie sicher, dass Ihre Anwendung beim Empfang unserer Benachrichtigungen zum Uninstall-Tracking [keine unerwünschten Aktionen durchführt]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/).

## Schritt 3: Test aus dem Braze Dashboard

Als nächstes senden Sie sich selbst einen Test-Push aus dem Braze-Dashboard. Denken Sie daran, dass Ihr Nutzerprofil durch diesen Test-Push nicht aktualisiert wird.

1. Erstellen Sie auf der Seite **Kampagnen** eine Push-Benachrichtigungskampagne und wählen Sie **iOS Push** als Plattform.
2. Fügen Sie auf der Seite **Einstellungen** den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu und markieren Sie **Add Content-Available Flag**.
3. Verwenden Sie die Seite **Vorschau**, um sich selbst einen Test-Push für das Uninstall-Tracking zu senden.
4. Vergewissern Sie sich, dass Ihre App beim Empfang des Push keine unerwünschten automatischen Aktionen ausführt.

{% alert important %}
Diese Testschritte sind ein Proxy für das Senden eines Uninstall-Tracking-Push von Braze. Wenn Sie die Badge-Zählung aktiviert haben, wird eine Badge-Nummer zusammen mit dem Push für den Test gesendet, aber die Uninstall-Tracking-Pushes von Braze setzen keine Badge-Nummer in Ihrer Anwendung.
{% endalert %}

## Schritt 4: Uninstall-Tracking aktivieren

Folgen Sie den Anweisungen zur [Aktivierung der Deinstallationsverfolgung]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

