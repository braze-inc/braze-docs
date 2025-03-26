---
nav_title: Unerwartetes Öffnen von Push-Klicks in der App
article_title: Unerwartetes Öffnen von Push-Klicks in der App
page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie das Problem beheben, wenn ein Push-Link in einem Webbrowser und nicht in der App geöffnet werden soll."
channel: push
---

# Unerwartetes Öffnen von Push-Klicks in der App

Wenn Sie Probleme damit haben, dass Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Webbrowser geöffnet werden, liegt möglicherweise ein Problem mit Ihrer Kampagnenkonfiguration oder SDK-Implementierung vor. Die folgenden Schritte helfen Ihnen dabei.

## Überprüfen Sie das Verhalten beim Anklicken

Vergewissern Sie sich in Ihrer Kampagne oder in Ihrem Canvas-Schritt, dass **Web-URL in mobiler App öffnen** nicht ausgewählt ist. Wenn dies der Fall ist, löschen Sie die Auswahl und starten Sie erneut. 

![Das Feld "Verhalten bei Klick" bei der Konfiguration eines Push-Sets wurde auf "Web-URL öffnen" gesetzt, wobei "Web-URL innerhalb der mobilen App öffnen" nicht markiert war.]({% image_buster /assets/img/push_on_click.png %})

Die Standardinteraktion für das On-Click-Verhalten "Web-URL öffnen" unterscheidet sich je nach SDK-Version. Bei den SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig aktiviert und Web-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Web-URLs werden im Standard-Webbrowser des Geräts geöffnet.

Wenn dies nicht der Fall ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor. 

## Überprüfen Sie die Push-Integration

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit Ihrer Push-Benachrichtigungsintegration oder Ihren Anpassungseinstellungen liegen. Folgen Sie diesen Schritten zur Fehlerbehebung:

1. **Überprüfen Sie die Implementierung des Push-Delegaten:** Stellen Sie sicher, dass der Braze Push-Delegat korrekt implementiert ist. Detaillierte Anweisungen finden Sie in der Integrationsanleitung für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home/).
2. **Überprüfen Sie die benutzerdefinierte Linkbehandlung:** Prüfen Sie, ob die App eine benutzerdefinierte Handhabung für alle `https://` Links enthält. Benutzerdefinierte Konfigurationen können das Standardverhalten außer Kraft setzen. Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um diese Einstellungen zu überprüfen und ggf. anzupassen.
3. **Überprüfen Sie die iOS Push-Registrierung:** Für iOS gehen Sie noch einmal zu Schritt 1 der Anleitung zur Push-Integration, um [Push-Benachrichtigungen bei APNs zu registrieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Stellen Sie sicher, dass Ihr Delegate-Objekt synchron zugewiesen wird, bevor die App den Start beendet. Diesen Schritt sollten Sie mit der Methode `application:didFinishLaunchingWithOptions:` durchführen.
4. **Testen Sie Ihre Integration:** Nachdem Sie die Anpassungen vorgenommen haben, testen Sie das Verhalten der Push-Benachrichtigung sowohl auf iOS- als auch auf Android-Geräten, um sicherzustellen, dass das Problem behoben ist.

Wenn das Problem weiterhin besteht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/support_contact), um weitere Unterstützung zu erhalten.


*Zuletzt aktualisiert am 6\. Dezember 2024*