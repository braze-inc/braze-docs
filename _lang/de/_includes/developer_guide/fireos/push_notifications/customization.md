{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Einstellungen

Für die Push-Benachrichtigungen von FireOS, die über das Braze-Dashboard versendet werden, sind viele fortschrittliche Einstellungen verfügbar. Dieser Artikel beschreibt diese Funktionen und wie Sie sie erfolgreich nutzen können.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Lebenserwartung (TTL) {#ttl}

Im Feld **Time to Live** (TTL) können Sie eine benutzerdefinierte Zeitspanne für die Speicherung von Nachrichten mit dem Push-Messaging-Dienst festlegen. Die Standardwerte für die Time-To-Live betragen vier Wochen für FCM und 31 Tage für ADM.

### Zusammenfassender Text {#summary-text}

Mit dem Zusammenfassungstext können Sie zusätzlichen Text in der erweiterten Benachrichtigungsansicht einstellen. Es dient auch als Beschriftung für Benachrichtigungen mit Bildern.

![Eine Android Nachricht mit dem Titel "Dies ist der Titel der Benachrichtigung." und dem Zusammenfassungstext "Dies ist der Zusammenfassungstext der Benachrichtigung."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Der Zusammenfassungstext wird in der erweiterten Ansicht unter dem Text der Nachricht angezeigt. 

![Eine Android Nachricht mit dem Titel "Dies ist der Titel der Benachrichtigung." und dem Zusammenfassungstext "Dies ist der Zusammenfassungstext der Benachrichtigung."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Bei Push-Benachrichtigungen, die Bilder enthalten, wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift angezeigt wird, wenn die Benachrichtigung erweitert wird. 

### Benutzerdefinierte URIs {#custom-uri}

Mit der Funktion **Benutzerdefinierte URI** können Sie eine Web-URL oder eine Android-Ressource angeben, zu der navigiert werden soll, wenn die Benachrichtigung angeklickt wird. Wenn kein benutzerdefinierter URI angegeben ist, gelangen Benutzer durch Klicken auf die Benachrichtigung zu Ihrer App. Sie können die angepasste URI verwenden, um Deeplinks in Ihrer App zu setzen und Nutzer zu Ressourcen außerhalb Ihrer App zu leiten. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder unser Dashboard unter **Erweiterte Einstellungen** im Push Composer wie abgebildet festgelegt werden:

![Erweiterte Einstellung für Deeplinking im Braze Push Composer.]({% image_buster /assets/img_archive/deep_link.png %})

### Benachrichtigungs-Anzeigepriorität

{% alert important %}
Die Einstellung für die Priorität der Benachrichtigungsanzeige wird auf Geräten mit Android O oder neuer nicht mehr verwendet. Bei neueren Geräten legen Sie die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) fest.
{% endalert %}

Die Prioritätsstufe einer Push-Benachrichtigung wirkt sich darauf aus, wie Ihre Benachrichtigung im Vergleich zu anderen Benachrichtigungen in der Benachrichtigungsleiste angezeigt wird. Sie kann sich auch auf die Geschwindigkeit und die Art der Zustellung auswirken, da normale Nachrichten und Nachrichten mit geringerer Priorität mit einer etwas höheren Latenzzeit oder in Stapeln gesendet werden, um die Batterie zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

In Android O wurde die Benachrichtigungspriorität eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungstöne senden. Bei Geräten mit Android-Versionen vor O können Sie über das Braze-Dashboard und die Messaging API eine Prioritätsstufe für FireOS-Benachrichtigungen festlegen. 

Um Ihrer gesamten Nutzerbasis Nachrichten mit einer bestimmten Priorität zukommen zu lassen, empfehlen wir Ihnen, die Priorität indirekt über die [Konfiguration des Messaging-Kanals](https://developer.android.com/training/notify-user/channels#importance) festzulegen (um O+ Geräte zu targetieren) *und* die individuelle Priorität über das Dashboard zu senden (um <O Geräte zu targetieren).

Die Prioritätsstufen, die Sie für Push-Benachrichtigungen von Fire OS festlegen können, sind:

| Priorität | Beschreibung/Verwendungszweck | `priority` Wert (für API-Nachrichten) |
|----------|--------------------------|-------------------------------------|
| Max.      | Dringende oder zeitkritische Nachrichten | `2` |
| Hoch     | Wichtige Mitteilungen, wie z.B. eine neue Nachricht von einem Freund | `1` |
| Standard  | Die meisten Benachrichtigungen - verwenden Sie diese Option, wenn Ihre Nachricht nicht ausdrücklich unter eine der anderen Prioritätsarten fällt. | `0` |
| Niedrig      | Informationen, die Sie Ihren Nutzern mitteilen möchten, die aber keine sofortige Aktion erfordern | `-1` |
| Min.      | Kontextuelle oder Hintergrundinformationen. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie in der Dokumentation zu [den Android-Benachrichtigungen](http://developer.android.com/design/patterns/notifications.html) von Google.

### Töne {#sounds}

In Android O wurden die Benachrichtigungstöne eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrem Entwickler zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration zu definieren und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungen senden.

Für Geräte mit Android-Versionen vor O können Sie mit Braze den Ton einer einzelnen Push-Nachricht über den Dashboard Composer einstellen. Hierzu können Sie eine lokale Tonressource auf dem Gerät angeben (z. B. `android.resource://com.mycompany.myapp/raw/mysound`). Wenn Sie in diesem Feld "default" angeben, wird der standardmäßige Benachrichtigungston auf dem Gerät abgespielt. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder das Dashboard unter **Einstellungen** im Push Composer festgelegt werden.

![Erweiterte Einstellung für Töne im Braze Push Composer.]({% image_buster /assets/img_archive/sound_android.png %})

Geben Sie die vollständige URI der Tonressource (z. B. `android.resource://com.mycompany.myapp/raw/mysound`) in die Eingabeaufforderung des Dashboards ein.

Um Ihre gesamte Nutzerbasis mit einem bestimmten Ton zu benachrichtigen, empfehlen wir Ihnen, den Ton indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels) festzulegen (um O+ Geräte zu targetieren) *und* den individuellen Ton über das Dashboard zu senden (um <O Geräte zu targetieren).
