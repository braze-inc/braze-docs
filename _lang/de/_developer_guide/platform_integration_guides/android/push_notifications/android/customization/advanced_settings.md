---
nav_title: Erweiterte Einstellungen
article_title: Erweiterte Push-Benachrichtigungseinstellungen für Android
platform: Android
page_order: 40
description: "Dieser Artikel referenziert erweiterte Einstellungen für Android Push-Benachrichtigungen wie TTL, IDs für Benachrichtigungen, Priorität von Benachrichtigungen und mehr."
channel:
  - push

---

# Erweiterte Einstellungen

> Für Android- und FireOS-Push-Benachrichtigungen, die über das Braze-Dashboard gesendet werden, sind viele erweiterte Einstellungen verfügbar. Dieser Artikel beschreibt diese Funktionen und wie Sie sie erfolgreich nutzen können.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

## ID der Benachrichtigung {#notification-id}

Eine **Notification ID** ist ein eindeutiger Bezeichner für eine von Ihnen gewählte Nachrichtenkategorie, der dem Messaging-Dienst mitteilt, dass er nur die jüngste Nachricht mit dieser ID berücksichtigen soll. Wenn Sie eine ID für die Benachrichtigung festlegen, können Sie nur die aktuellste und relevante Nachricht versenden, anstatt einen Stapel veralteter, irrelevanter Nachrichten.

## Priorität der Firebase-Nachrichtenzustellung {#fcm-priority}

Mit dem Feld [Priorität der Firebase-Nachrichtenzustellung](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) können Sie festlegen, ob ein Push mit "normaler" oder "hoher" Priorität an Firebase Cloud Messaging gesendet wird.

## Lebenserwartung (TTL) {#ttl}

Im Feld **Time to Live** (TTL) können Sie eine benutzerdefinierte Zeitspanne für die Speicherung von Nachrichten mit dem Push-Messaging-Dienst festlegen. Die Standardwerte für die Time-To-Live betragen vier Wochen für FCM und 31 Tage für ADM.

## Zusammenfassender Text {#summary-text}

Mit dem Zusammenfassungstext können Sie zusätzlichen Text in der erweiterten Benachrichtigungsansicht einstellen. Es dient auch als Beschriftung für Benachrichtigungen mit Bildern.

![Android-Nachricht mit dem Titel "Grüße von Appboy!", der Nachricht "Dies ist der Nachrichtentext! Sie können sogar Emojis hinzufügen." und Zusammenfassungstext "Dies ist der Zusammenfassungstext."]({% image_buster /assets/img_archive/summary_text.png %})

Der Zusammenfassungstext wird in der erweiterten Ansicht unter dem Text der Nachricht angezeigt.

Bei Push-Benachrichtigungen, die Bilder enthalten, wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift angezeigt wird, wenn die Benachrichtigung erweitert wird. 

![Android-Nachricht mit dem Titel "Appboy!", der Nachricht "Dies ist der Nachrichtentext..." und dem Zusammenfassungstext "und dies ist der Zusammenfassungstext."]({% image_buster /assets/img_archive/messagesummary.gif %})

## Benutzerdefinierte URIs {#custom-uri}

Mit der Funktion **Benutzerdefinierte URI** können Sie eine Web-URL oder eine Android-Ressource angeben, zu der navigiert werden soll, wenn die Benachrichtigung angeklickt wird. Wenn kein benutzerdefinierter URI angegeben ist, gelangen Benutzer durch Klicken auf die Benachrichtigung zu Ihrer App. Sie können die angepasste URI verwenden, um Deeplinks in Ihrer App zu setzen und Nutzer zu Ressourcen außerhalb Ihrer App zu leiten. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) oder unser Dashboard unter **Erweiterte Einstellungen** im Push Composer wie abgebildet festgelegt werden:

![Erweiterte Einstellung für Deeplinking im Braze Push Composer.]({% image_buster /assets/img_archive/deep_link.png %})

## Benachrichtigungs-Anzeigepriorität {#notification-priority}

{% alert important %}
Die Einstellung für die Priorität der Benachrichtigungsanzeige wird auf Geräten mit Android O oder neuer nicht mehr verwendet. Bei neueren Geräten legen Sie die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) fest.
{% endalert %}

Die Prioritätsstufe einer Push-Benachrichtigung wirkt sich darauf aus, wie Ihre Benachrichtigung im Vergleich zu anderen Benachrichtigungen in der Benachrichtigungsleiste angezeigt wird. Dies kann sich auch auf die Geschwindigkeit und die Art der Zustellung auswirken, da normale Nachrichten und Nachrichten mit geringerer Priorität mit etwas höherer Latenz oder in Stapeln gesendet werden, um den Akku zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

In Android O wurde die Benachrichtigungspriorität eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungstöne senden. Für Geräte mit Android-Versionen vor O können Sie über das Braze Dashboard und die Nachrichten-API eine Prioritätsstufe für Android- und FireOS-Benachrichtigungen festlegen. 

Um Ihre gesamte Nutzerbasis mit einer bestimmten Priorität zu benachrichtigen, empfehlen wir Ihnen, die Priorität indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) festzulegen (um O+ Geräte zu adressieren) *und* die individuelle Priorität über das Dashboard zu senden (um <O Geräte zu adressieren).

Die Prioritätsstufen, die Sie bei Push-Benachrichtigungen für Android oder Fire OS einstellen können, sind:

| Priorität | Beschreibung/Verwendungszweck | `priority` Wert (für API-Nachrichten) |
|----------|--------------------------|-------------------------------------|
| Max.      | Dringende oder zeitkritische Nachrichten | `2` |
| Hoch     | Wichtige Mitteilungen, wie z.B. eine neue Nachricht von einem Freund | `1` |
| Standard  | Die meisten Benachrichtigungen - verwenden Sie diese Option, wenn Ihre Nachricht nicht ausdrücklich unter eine der anderen Prioritätsarten fällt. | `0` |
| Niedrig      | Informationen, die Sie Ihren Nutzern mitteilen möchten, die aber keine sofortige Aktion erfordern | `-1` |
| Min.      | Kontextuelle oder Hintergrundinformationen. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie in der [Android-Benachrichtigungsdokumentation](http://developer.android.com/design/patterns/notifications.html) von Google.

## Töne {#sounds}

In Android O wurden die Benachrichtigungstöne eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration zu definieren und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungen senden.

Für Geräte mit Android-Versionen vor O können Sie mit Braze den Ton einer einzelnen Push-Nachricht über den Dashboard Composer einstellen. Hierzu können Sie eine lokale Tonressource auf dem Gerät angeben (z. B. `android.resource://com.mycompany.myapp/raw/mysound`). Wenn Sie in diesem Feld "default" angeben, wird der standardmäßige Benachrichtigungston auf dem Gerät abgespielt. Dies kann über die [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) oder das Dashboard unter **Erweiterte Einstellungen** im Push-Composer festgelegt werden.

![Erweiterte Einstellung für Töne im Braze Push Composer.]({% image_buster /assets/img_archive/sound_android.png %})

Geben Sie die vollständige URI der Tonressource (z. B. `android.resource://com.mycompany.myapp/raw/mysound`) in die Eingabeaufforderung des Dashboards ein.

Wenn Sie Ihre gesamte Nutzerbasis mit einem bestimmten Ton benachrichtigen möchten, empfehlen wir Ihnen, den Ton indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels) festzulegen (um O+ Geräte zu adressieren) *und* den individuellen Ton über das Dashboard zu senden (um <O Geräte zu adressieren).

