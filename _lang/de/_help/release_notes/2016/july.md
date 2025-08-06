---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2016."
---

# Juli 2016

## Filterung des Fehlerprotokolls der Entwickler:in nach Fehlertyp

Dieses Upgrade erleichtert Ihnen die Verwendung des Nachrichten-Fehlerprotokolls in der Entwicklungskonsole, um Fehlerbehebungen bei ihren Braze Integrationen durchzuführen. Dies ist ein Update für die Benutzerfreundlichkeit, das es Ihnen erlaubt, das Nachrichten-Fehlerprotokoll nach Typ zu filtern und das Auffinden und die Identifizierung spezifischer Probleme bei der Integration wesentlich zu erleichtern.

## Zeitstempel für den letzten gesendeten Push für das Tracking der Deinstallation hinzugefügt

Braze erkennt Deinstallationen, indem es einen stillen Push an die Apps eines Kunden sendet, um zu sehen, welche Geräte reagieren. Dieses Feature fügt einen unauffälligen Zeitstempel hinzu, der anzeigt, wann das Tracking zur Deinstallation zuletzt ausgeführt wurde. Diesen Zeitstempel finden Sie auf Ihrer Einstellungsseite, auf der das Tracking der Deinstallation konfiguriert ist. Erfahren Sie mehr über [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

![Uninstall-Tracking Kontrollkästchen]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Verbesserungen der Webhook-Tests hinzugefügt

Sie können jetzt eine Live-Webhook-Nachricht von Braze senden, bevor Sie eine Kampagne in Betrieb nehmen. Durch das Senden einer Testnachricht können Sie überprüfen, ob Ihre Nachrichten und Server-Endpunkte in einer sicheren Sandbox-Umgebung richtig konfiguriert wurden. Erfahren Sie mehr über [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## CSV-Export für Empfänger:in der Kampagne wurde eine Variation der empfangenen Nachrichten hinzugefügt

Wir haben dem CSV-Export für Kampagnen-Empfänger:innen eine Spalte hinzugefügt, die die Variation der erhaltenen Nachricht angibt. Erfahren Sie mehr über den [Export von Daten]({{site.baseurl}}/user_guide/data/export_braze_data/) aus Braze.

## Ungefähres Limit für die Anzahl der Impressionen

Sobald eine In-App-Nachricht eine bestimmte Anzahl von Impressionen erhalten hat, erlaubt Braze den Nutzer:innen nicht mehr, diese Nachricht zu erhalten. Erfahren Sie mehr darüber, wie Sie ungefähre [Grenzen für Impressionen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap) festlegen.

![IAM impression cap]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})

