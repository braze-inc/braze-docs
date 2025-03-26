---
nav_title: Push-Einstellungen
article_title: Push-Einstellungen für iOS
platform: Swift
page_order: 7
description: "Dieser Referenzartikel behandelt die fortgeschrittenen Einstellungen für iOS Push-Benachrichtigungen, wie z. B. Alarmoptionen, Töne, Ablauf und mehr, für das Swift SDK."
channel:
  - push

---

# Push-Einstellungen

> Wenn Sie eine Push-Kampagne über das Dashboard erstellen, klicken Sie im Schritt **Verfassen** auf den Tab **Einstellungen**, um die verfügbaren fortschrittlichen Einstellungen anzuzeigen.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Schlüssel-Wert-Paare

Braze erlaubt Ihnen, angepasste String-Schlüssel-Wert-Paare, bekannt als `extras`, zusammen mit einer Push-Benachrichtigung an Ihre Anwendung zu senden. Extras können über das Dashboard oder die API definiert werden und stehen dann als Schlüssel-Wert-Paare im Wörterbuch `notification` zur Verfügung, das an Ihre Push-Delegate-Implementierungen weitergegeben wird.

## Meldungsoptionen

Wählen Sie das Kontrollkästchen **Benachrichtigungsoptionen** aus, um eine Dropdown-Liste mit Schlüsselwerten anzuzeigen, mit denen Sie die Anzeige der Benachrichtigung auf den Geräten anpassen können.

## Hinzufügen eines Flags für verfügbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für verfügbaren Content hinzufügen**, um die Geräte anzuweisen, neue Inhalte im Hintergrund herunterzuladen. In der Regel können Sie diese Option aktivieren, wenn Sie [stille Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) versenden möchten.

## Hinzufügen eines Flags für veränderbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für veränderbare Inhalte hinzufügen**, um die erweiterte Empfängeranpassung zu aktivieren. Dieses Flag wird automatisch gesendet, wenn Sie eine [Rich-Benachrichtigung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/) verfassen, unabhängig vom Wert dieses Kontrollkästchens.

## App-Badge-Zähler aktualisieren

Geben Sie die Zahl ein, auf die Sie die Anzahl Ihrer Badges aktualisieren möchten, oder verwenden Sie die Liquid-Syntax, um angepasste Bedingungen festzulegen. Sie können die Anzahl der Nachrichten-Badges auch programmatisch aktualisieren: referenzieren Sie dazu unseren Artikel über [die Anzahl der Badges]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/).

## Töne

Wenn Sie möchten, dass Ihre Push-Benachrichtigung beim Empfang von einem angepassten Sound begleitet wird, verwenden Sie das Feld **Sound**, um die Protokoll-URL Ihrer Sounddatei anzugeben. Weitere Informationen zur Anpassung von [Sounds]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/) finden Sie in unserem Artikel über [angepasste Sounds]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/).

## Reduzierungs-ID

Geben Sie eine ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit der gleichen Collapse ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Lesen Sie die Dokumentation von Apple über [zusammengefasste Benachrichtigungen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Ablauf

Wenn Sie das Kontrollkästchen **Ablauf** aktivieren, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät eines Nutzers:innen die Verbindung verlieren, wird Braze weiterhin versuchen, die Nachricht bis zur angegebenen Zeit zu senden. Wenn dieser Wert nicht eingestellt ist, wird die Plattform standardmäßig auf einen Ablauf von 30 Tagen eingestellt. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.

