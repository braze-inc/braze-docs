---
nav_title: "Erweiterte Einstellungen für Push-Kampagnen"
article_title: Erweiterte Einstellungen für Push-Kampagnen
page_type: reference
page_order: 6
description: "Dieser Referenzartikel behandelt verschiedene erweiterte Einstellungen für Push-Kampagnen wie Benachrichtigungsoptionen, Flaggen, Töne, Ablaufdatum und mehr."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Erweiterte Einstellungen für Push-Kampagnen

> Dieser Referenzartikel behandelt verschiedene erweiterte Einstellungen für Push-Kampagnen wie Benachrichtigungsoptionen, Flaggen, Töne, Ablauf und mehr.

Wenn Sie eine Push-Mitteilung erstellen, können Sie im Schritt **Verfassen** das Zahnradsymbol <i class="fas fa-cog"></i> auswählen, um die erweiterten Einstellungen für Ihre Nachricht anzuzeigen.

![][1]

## Meldungsoptionen

Wenn Sie das Kontrollkästchen hier aktivieren, sehen Sie ein Dropdown-Menü mit Schlüsselwerten, mit denen Sie einstellen können, wie die Benachrichtigung auf den Geräten erscheinen soll.

## Hinzufügen eines Flags für verfügbaren Content

Das Flag `content-available` weist die Geräte an, neuen Content im Hintergrund herunterzuladen. Dies kann am häufigsten überprüft werden, wenn Sie daran interessiert sind, [stille Benachrichtigungen][2] zu senden.

## Hinzufügen eines Flags für veränderbaren Content

Das `mutable-content`-Flag ermöglicht eine erweiterte Empfängeranpassung in iOS-Geräten ab Version 10. Dieses Flag wird automatisch gesendet, wenn eine [Rich-Benachrichtigung][3] erstellt wird, unabhängig vom Wert dieses Kontrollkästchens.

## Töne

Hier können Sie einen Pfad zu einer Audiodatei in Ihrem App-Bundle eingeben, um einen Sound festzulegen, der beim Empfang der Push-Nachricht abgespielt wird. Wenn die angegebene Audiodatei nicht vorhanden ist oder das Schlüsselwort „default“ eingegeben werden soll, verwendet Braze den Standard-Gerätealarmton.

## Reduzierungs-ID
Geben Sie eine Reduzierungs-ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit der gleichen Reduzierungs-ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Weitere Informationen finden Sie in der [Dokumentation][4]] von Apple.

## Ablauf

Wenn Sie die Option **Ablauf** wählen, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät eines Benutzers die Verbindung verlieren, versucht Braze weiterhin, die Nachricht bis zur festgelegten Zeit zu senden. Wenn dieser Wert nicht eingestellt ist, wird die Plattform standardmäßig auf einen Ablauf von 30 Tagen eingestellt. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
