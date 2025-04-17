---
nav_title: Unerwartetes Öffnen von Push-Klicks in der App
article_title: Unerwartetes Öffnen von Push-Klicks in der App
page_type: solution
description: "Dieser Hilfe-Artikel beschreibt die Fehlerbehebung, wenn ein Push-Link nicht in der App, sondern in einem Webbrowser geöffnet werden soll."
channel: push
---

# Push-Klicks öffnen unerwartet in der App

Wenn Sie Probleme damit haben, dass Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Internetbrowser geöffnet werden, liegt möglicherweise ein Problem mit der Konfiguration Ihrer Kampagne oder der Implementierung des SDK vor. Beziehen Sie sich auf diese Schritte für Hilfe.

## Überprüfen Sie das Verhalten bei einem Klick

Überprüfen Sie in Ihrer Kampagne oder im Canvas-Schritt, dass die Option **Internet-URL innerhalb der mobilen App öffnen** nicht ausgewählt ist. Ist dies der Fall, löschen Sie die Auswahl und starten Sie erneut. 

![Das Feld "Verhalten bei Klick" bei der Konfiguration eines Push-Sets ist auf "Web-URL öffnen" eingestellt, wobei "Web-URL innerhalb der mobilen App öffnen" nicht markiert ist.]({% image_buster /assets/img/push_on_click.png %})

Die Standard-Interaktion für das Klickverhalten "Internet-URL öffnen" unterscheidet sich je nach SDK-Version. Bei den SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und die Internet-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Internet-URLs werden im Standard Webbrowser des Geräts geöffnet.

Wenn dies nicht der Fall ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor. 

## Push-Integration doppelt prüfen

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit der Integration Ihrer Push-Benachrichtigungen oder mit den Anpassungseinstellungen liegen. Befolgen Sie diese Schritte zur Fehlerbehebung:

1. **Überprüfen Sie die Implementierung des Push-Delegaten:** Stellen Sie sicher, dass der Push-Delegat von Braze korrekt implementiert ist. Ausführliche Anweisungen finden Sie in der Integrationsanleitung für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home/).
2. **Prüfen Sie die angepasste Linkbehandlung:** Prüfen Sie, ob die App eine angepasste Handhabung für alle `https://` Links enthält. Angepasste Konfigurationen können die Standard-Verhaltensweisen außer Kraft setzen. Arbeiten Sie mit Ihrem Entwickler:in Team zusammen, um diese Einstellungen zu überprüfen und ggf. anzupassen.
3. **Überprüfen Sie die iOS Push-Registrierung:** Für iOS sehen Sie sich Schritt 1 der Anleitung zur Integration von [Push-Benachrichtigungen mit APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns) an. Stellen Sie sicher, dass Ihr Delegatenobjekt synchron zugewiesen wird, bevor die App den Start beendet. Diesen Schritt sollten Sie mit der Methode `application:didFinishLaunchingWithOptions:` durchführen.
4. **Testen Sie Ihre Integration:** Nachdem Sie die Anpassungen vorgenommen haben, testen Sie das Verhalten der Push-Benachrichtigung sowohl auf iOS- als auch auf Android-Geräten, um sicherzustellen, dass das Problem behoben ist.

Wenn das Problem persistiert, wenden Sie sich bitte an den [Braze Support]({{site.baseurl}}/support_contact), um weitere Unterstützung zu erhalten.


*Zuletzt aktualisiert am 6\. Dezember 2024*