---
nav_title: Zustellbarkeit für chinesische Android-Geräte
article_title: Push-Zustellbarkeit für chinesische Android-Geräte
page_order: 10

page_type: reference
description: "Dieser Artikel befasst sich mit den Nuancen der Push-Zustellbarkeit, die Sie beachten sollten, wenn Sie Nutzer auf Android-Geräten chinesischer OEMs ansprechen."
channel: push

---

# Push-Zustellbarkeit für chinesische Android-Geräte

> Einige Android-Geräte chinesischer OEMs (Original Equipment Manufacturers) wie Xiaomi, OPPO und Vivo optimieren ihre Akkulaufzeit durch aggressives App Lifecycle Management. Diese Optimierung kann die unbeabsichtigte Folge haben, dass die App-Verarbeitung im Hintergrund abgeschaltet wird, was die Zustellbarkeit Ihrer Push-Benachrichtigungen verringern kann.<br><br>Um sicherzustellen, dass die Messaging-Leistung Ihrer App auf diesen Geräten wie erwartet funktioniert, sollten Ihre Marketing- und Technikteams zusammenarbeiten und die in diesem Artikel beschriebenen Schritte befolgen.

## Schritte für Entwickler
Diese OEMs führen ihre Optimierungen durch, indem sie Hintergrundanwendungen aggressiv abschalten und sie daran hindern, selbständig Hintergrundaufgaben auszuführen. Als Entwickler müssen Sie Ihre App so konfigurieren, dass der Benutzer aufgefordert wird, diese Einschränkungen zu lockern, wann immer dies möglich ist.

Dies können Sie erreichen, indem Sie Ihre App automatisch auf dem Gerät Ihres Endbenutzers starten lassen. Dadurch erhält Ihre App die Erlaubnis, im Hintergrund zu laufen und auf Nachrichten von Braze zu warten. Da es sich hierbei um ein OEM-spezifisches Problem und nicht um ein Android-Problem handelt, gibt es leider keine dokumentierten APIs für die Abfrage der Autostart-Erlaubnis für jeden OEM.

Integrieren Sie dazu eine Bibliothek wie [AutoStarter](https://github.com/judemanutd/AutoStarter) in Ihre Anwendung. AutoStarter unterstützt mehrere Hersteller, so dass Sie auf einfache Weise den Manager für Startberechtigungen auf einer Vielzahl von Geräten aufrufen können. Nachdem Sie AutoStarter integriert haben, rufen Sie `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` auf, um den Manager für Startberechtigungen auf dem Gerät Ihres Endnutzers oder Ihrer Endnutzerin aufzurufen. Verbinden Sie diese Aktion mit einer Aufforderung an den Endnutzer:in, den "Autostart" für Ihre App zu aktivieren. Ihr Marketingteam wird diese Botschaft erstellen - siehe den nächsten Abschnitt!

## Schritte für Marketer
Nachdem sich Ihre Benutzer für den Empfang von Push-Benachrichtigungen entschieden haben, können sie weitere Schritte unternehmen, um die Zustellung von Nachrichten für diese Geräte zu verbessern. Wir empfehlen Ihnen, Ihrer [Push-Primer-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) eine In-App-Nachricht folgen zu lassen, die sich an Nutzer:innen von chinesischen OEM-Geräten richtet:

- Enablement des Autostarts für die App
- Deaktivieren Sie die Batterieoptimierung für die App

Um Ihre Botschaft weiter zu verstärken, fügen Sie andere Kanäle hinzu, um Informationen aus ungeöffneten Push-Benachrichtigungen über Out-of-App-Kanäle wie SMS, WhatsApp und LINE und In-App-Kanäle wie In-App-Nachrichten und Content Cards wieder aufzugreifen. Ihre Benutzer sehen alles, was sie übersehen haben könnten, wenn sie die App das nächste Mal öffnen.