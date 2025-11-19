---
nav_title: "Optionen für Benachrichtigungen"
article_title: Android-Benachrichtigungsoptionen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt verschiedene Android-Benachrichtigungsoptionen und wie Sie diese am besten in Kampagnen von Braze einsetzen."

platform: Android
channel:
  - Push

---

# Optionen für Benachrichtigungen

> Dies sind einige der Android-spezifischen Optionen für Push-Benachrichtigungen, die über Braze verfügbar sind.

## Stille Benachrichtigungen

Wenn Sie [Ihre Push-Benachrichtigung verfassen]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), **können** Sie eine Android-Push-Nachricht **nicht** ohne Titel versenden - Sie können stattdessen ein einzelnes Leerzeichen eingeben. Denken Sie daran: Wenn Ihre Nachricht nur ein einziges Leerzeichen enthält, wird sie als stille Push-Benachrichtigung gesendet. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Benachrichtigungsgruppen

Wenn Sie Ihre Nachrichten kategorisieren und in der Benachrichtigungsleiste Ihres Benutzers gruppieren möchten, können Sie über Braze die Funktion Benachrichtigungskanäle von Android nutzen.

Erstellen Sie zunächst Ihre Android-Push-Kampagne und suchen Sie dann oben auf der Registerkarte **Verfassen** nach dem Dropdown-Menü **Benachrichtigungskanal**.

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Wählen Sie Ihren Benachrichtigungskanal aus der Dropdown-Liste. Sie müssen auch einen Fallback-Kanal auswählen, für den Fall, dass Ihre Einstellungen für den Benachrichtigungskanal nicht funktionieren.

Wenn hier keine [Benachrichtigungskanäle]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) aufgelistet sind, können Sie einen mit Hilfe der ID des Benachrichtigungskanals hinzufügen. Wenden Sie sich an Ihre Entwickler, um herauszufinden, wie Ihre Benachrichtigungskanal-IDs lauten, oder um bei Bedarf neue IDs zu erstellen. 

Um eine Benachrichtigungs-ID zu Ihrem Benachrichtigungskanal hinzuzufügen, klicken Sie im Dropdown-Menü des **Benachrichtigungskanals** auf **Benachrichtigungskanal verwalten** und füllen Sie die erforderlichen Felder aus. Benachrichtigungskanäle müssen in der App definiert werden, bevor sie in der Braze-Plattform verwendet werden können.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


