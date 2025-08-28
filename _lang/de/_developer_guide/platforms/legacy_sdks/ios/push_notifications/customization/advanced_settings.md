---
nav_title: Erweiterte Einstellungen
article_title: Erweiterte Push-Einstellungen
platform: iOS
page_order: 5
description: "Dieser Artikel referenziert die fortschrittlichen Einstellungen für iOS Push-Benachrichtigungen wie Alarmoptionen, Töne, Ablauf und mehr."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Erweiterte Einstellungen

Wenn Sie eine Push Kampagne erstellen, wählen Sie im Schritt Verfassen die Option **Einstellungen**, um die verfügbaren erweiterten Einstellungen anzuzeigen.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extrahieren von Daten aus Push-Schlüssel-Wert-Paaren

Braze erlaubt Ihnen, angepasste String-Schlüssel-Wert-Paare, bekannt als `extras`, zusammen mit einer Push-Benachrichtigung an Ihre Anwendung zu senden. Extras können über das Dashboard oder die API definiert werden und stehen dann als Schlüssel-Wert-Paare im Wörterbuch `notification` zur Verfügung, das an Ihre Push-Delegate-Implementierungen weitergegeben wird.

## Meldungsoptionen

Aktivieren Sie das Kontrollkästchen **Benachrichtigungsoptionen**, um eine Dropdown-Liste mit Schlüsselwerten anzuzeigen, mit denen Sie die Anzeige der Benachrichtigung auf den Geräten anpassen können.

## Hinzufügen eines Flags für verfügbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für verfügbaren Content hinzufügen**, um die Geräte anzuweisen, neue Inhalte im Hintergrund herunterzuladen. In der Regel können Sie diese Option aktivieren, wenn Sie [stille Benachrichtigungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/) versenden möchten.

## Hinzufügen eines Flags für veränderbaren Content

Aktivieren Sie das Kontrollkästchen **Flag für veränderbare Inhalte hinzufügen**, um die erweiterte Empfängeranpassung auf Geräten mit iOS 10+ zu aktivieren. Dieses Flag wird automatisch gesendet, wenn Sie eine [Rich-Benachrichtigung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications/) verfassen, unabhängig vom Wert dieses Kontrollkästchens.

## App-Badge-Zähler aktualisieren

Geben Sie die Zahl ein, auf die Sie die Anzahl Ihrer Badges aktualisieren möchten, oder verwenden Sie die Liquid-Syntax, um Ihre angepassten Bedingungen festzulegen. Sie können die Anzahl Ihrer Badges auch manuell über die Eigenschaft `applicationIconBadgeNumber` Ihrer Anwendung oder die Payload der Push-Benachrichtigung aktualisieren. Wenn Sie mehr darüber erfahren möchten, lesen Sie unseren Artikel über [die Anzahl der Badges]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges/).

## Töne

Hier können Sie einen Pfad zu einer Tondatei in Ihrem App-Bundle eingeben, um einen Sound festzulegen, der beim Empfang der Push-Nachricht abgespielt wird. Wenn die angegebene Audiodatei nicht vorhanden ist oder das Schlüsselwort "default" eingegeben werden soll, verwendet Braze den Standard-Gerätealarmton. Weitere Informationen zur Anpassung von Sounds finden Sie in unserem Artikel über [angepasste Sounds]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds/).

## Reduzierungs-ID

Geben Sie eine ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit der gleichen Collapse ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Lesen Sie die Dokumentation von Apple über [zusammengefasste Benachrichtigungen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Ablauf

Wenn Sie das Kontrollkästchen **Ablauf** aktivieren, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät eines Nutzers:innen die Verbindung verlieren, wird Braze weiterhin versuchen, die Nachricht bis zur angegebenen Zeit zu senden. Wenn dieser Wert nicht eingestellt ist, wird die Plattform standardmäßig auf einen Ablauf von 30 Tagen eingestellt. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.

