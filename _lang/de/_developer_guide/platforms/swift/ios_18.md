---
nav_title: Auf iOS 18 upgraden
article_title: Auf iOS 18 upgraden
page_order: 7.1
platform: 
  - iOS
description: "Dieser Artikel enthält Informationen zum Release von iOS 18, damit Sie Ihr SDK nahtlos upgraden können."
---

# Auf iOS 18 upgraden

> Sind Sie neugierig, wie Braze sich auf die kommende iOS-Version vorbereitet? Dieser Artikel fasst unsere Insights zum iOS 18 Release zusammen, um Ihnen und Ihren Nutzer:innen ein nahtloses Erlebnis zu ermöglichen.

Die [WWDC](https://developer.apple.com/wwdc24/) von Apple fand vom 9\. bis 11\. Juni 2024 statt. Erfahren Sie mehr über ihre Ankündigungen in unserem [Blogbeitrag](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18) oder lesen Sie weiter, um zu erfahren, wie Sie iOS 18 mit Braze nutzen können.

## Änderungen in iOS 18

### Live-Aktivitäten auf der Apple Watch

[Live-Aktivitäten](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift) werden von watchOS 11 unterstützt. Es ist keine zusätzliche Einrichtung erforderlich. Apple bietet jedoch die Möglichkeit, die Schnittstelle der Uhr anzupassen.

### Apple Vision Pro

Der Vision Pro ist jetzt in China, Japan, Singapur, Australien, Kanada, Frankreich, Deutschland und Großbritannien erhältlich. Lesen Sie in unserem Blog, wie [Braze visionOS unterstützt](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### iPhone-Benachrichtigungen unter macOS

Apples neues Feature [zur iPhone-Spiegelung](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) erlaubt es Nutzer:innen, iPhone-Benachrichtigungen auf ihren macOS Geräten zu empfangen. Beachten Sie, dass einige Medientypen wie Push Story-Bilder und GIFs nicht unterstützt werden, da sie nicht als macOS-Benachrichtigung dargestellt werden können.

### Apple Intelligenz

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) ist jetzt für Geräte mit iOS 18.1 und höher verfügbar.

Als Nutzer:innen von Braze sollten Sie vor allem das neue Feature [Benachrichtigungszusammenfassungen](https://support.apple.com/en-us/108781) kennen, das die Verarbeitung auf dem Gerät nutzt, um Push-Benachrichtigungen automatisch zu gruppieren und Textzusammenfassungen für zusammenhängende Push-Benachrichtigungen zu erstellen, die von einer einzelnen App gesendet wurden. Endnutzer:innen können auf eine Zusammenfassung tippen, um jede Push-Benachrichtigung so zu sehen, wie sie ursprünglich gesendet wurde.

Aufgrund der Art und Weise, wie diese Zusammenfassungen generiert werden, haben Sie keine Kontrolle über ihr spezifisches Verhalten oder den generierten Text. Dies hat jedoch keine Auswirkungen auf Analytics- oder Reporting-Features, wie z.B. das Push-Klick Tracking.

![Ein Beispiel für einen Screenshot der Vorschau einer Push-Benachrichtigung.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
