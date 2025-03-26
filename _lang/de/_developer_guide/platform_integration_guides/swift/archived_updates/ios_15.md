---
nav_title: Anleitung zum Upgrade für iOS 15
article_title: Upgrade-Leitfaden für das iOS 15 SDK
page_order: 7
platform: iOS
description: "Dieser Referenzartikel beschreibt die neuen Updates für iOS 15, die erforderlichen SDK-Updates und die neuen Features."
hidden: true
noindex: true
---

# Upgrade-Leitfaden für das iOS 15-SDK

> Dieser Leitfaden beschreibt die Änderungen, die mit iOS 15 (WWDC21) eingeführt wurden, und die erforderlichen Schritte für ein Upgrade Ihrer Braze iOS SDK-Integration. Eine vollständige Liste der neuen iOS 15 Updates finden Sie in den [iOS 15 Versionshinweisen](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) von Apple.


## Änderungen an der Transparenz der UI-Navigationen

Im Rahmen unserer jährlichen Tests von iOS-Betas haben wir eine von Apple vorgenommene Änderung festgestellt, die dazu führt, dass bestimmte UI-Navigationsleisten transparent statt undurchsichtig erscheinen. Dies wird unter iOS 15 sichtbar sein, wenn Sie die Standard UI von Braze für Content-Cards verwenden oder wenn Deeplinks im Internet innerhalb Ihrer App geöffnet werden, anstatt in einer separaten Browser-App.

Um diese visuelle Veränderung in iOS 15 zu vermeiden, empfehlen wir Ihnen dringend, so schnell wie möglich auf das [Braze iOS SDK v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) zu upgraden, bevor die Nutzer:innen ihr Telefon auf das neue Betriebssystem iOS 15 aktualisieren.

## Neue Benachrichtigungseinstellungen {#notification-settings}

Mit iOS 15 wurden neue Features für Benachrichtigungen eingeführt, die den Nutzer:innen helfen, sich zu konzentrieren und häufige Unterbrechungen während des Tages zu vermeiden. Wir freuen uns, Ihnen Unterstützung für diese neuen Features anbieten zu können. Diese Features erfordern keine zusätzlichen SDK-Upgrades und werden nur auf Nutzer von iOS 15-Geräten angewendet.

### Fokus-Modi {#focus-mode}

Nutzer:innen von iOS 15 können jetzt "Fokus-Modi" erstellen - angepasste Profile, mit denen sie festlegen, welche Benachrichtigungen ihren Fokus durchbrechen und prominent angezeigt werden sollen.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Unterbrechungsstufen {#interruption-levels}

In iOS 15 können Push-Benachrichtigungen mit einer von vier Unterbrechungsstufen gesendet werden:

* **Passiv** (neu): Kein Ton, keine Vibration, kein Aufwachen des Bildschirms, kein Durchbrechen der Fokuseinstellungen
* **Aktiv** (Standard) - Erlaubt Ton, Vibration, Aufwachen des Bildschirms, kein Durchbrechen der Fokuseinstellungen.
* **Zeitsensitiv** (neu): Erlaubt Ton, Vibration, Aufwachen des Bildschirms, kann die Systemsteuerung durchbrechen, falls zulässig
* **Kritisch**: Erlaubt Ton, Vibration, Aufwachen des Bildschirms, kann die Systemsteuerung durchbrechen und den Ruftonschalter umgehen

Unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level) erfahren Sie mehr darüber, wie Sie diese Option in iOS Push einstellen können.

### Zusammenfassung der Benachrichtigung {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

In iOS 15 können Nutzer(optional) bestimmte Zeiten am Tag auswählen, um eine Zusammenfassung der Benachrichtigungen zu erhalten. Benachrichtigungen, die keine unmittelbare Aufmerksamkeit erfordern (z.B. wenn sie als "passiv" gesendet werden oder während sich der Nutzer:innen im Fokusmodus befindet), werden gruppiert, um ständige Unterbrechungen während des Tages zu vermeiden.

Für jede Benachrichtigung, die Sie versenden, können Sie bald einen "Relevanzwert" angeben, um zu steuern, welche Benachrichtigung oben in der Zusammenfassung erscheinen soll.

Unter [iOS Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score) erfahren Sie mehr darüber, wie Sie den "Relevanzwert" einer Benachrichtigung festlegen.

## Standort Buttons {#location-buttons}

iOS 15 bietet Nutzern eine neue, bequeme Möglichkeit, den Zugriff auf Standorte innerhalb einer App vorübergehend zu gewähren. 

Der neue Standort-Button basiert auf der bestehenden Berechtigung "Einmalig zulassen", ohne dass Nutzer, die in der gleichen Sitzung mehrfach klicken, wiederholt aufgefordert werden.

Weitere Informationen finden Sie in Apples Video [Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102/) von der diesjährigen Worldwide Developer Conference (WWDC).

{% alert tip %}
Mit diesem Feature haben Sie die Möglichkeit, Nutzer um Erlaubnis zu fragen! Nutzer, die bereits vor iOS 15 Standortberechtigungen abgelehnt haben, erhalten beim Klick auf den Standort-Button eine Aufforderung mit der Möglichkeit, die Berechtigung ein letztes Mal aus dem abgelehnten Zustand zurückzusetzen.
{% endalert %}

### Verwendung von Standort-Buttons bei Braze

Für die Verwendung von Standort Buttons mit Braze ist keine zusätzliche Integration erforderlich. Ihre App sollte den Standort eines Nutzers:innen wie gewohnt weitergeben (sobald dieser seine Zustimmung gegeben hat).

Laut Apple wird für Nutzer:innen, die den Zugriff auf den Standort im Hintergrund bereits freigegeben haben, die Option "Während der Nutzung der App" diese Berechtigung auch nach dem Upgrade auf iOS 15 weiterhin gewähren.

## Apple Mail {#mail}

In diesem Jahr hat Apple zahlreiche Updates zum Tracking von E-Mails und zum Datenschutz angekündigt. Weitere Informationen finden Sie in unserem [Blogbeitrag](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Standort der Safari IP-Adresse

In iOS 15 werden Nutzer:in die Lage versetzt, Safari so zu konfigurieren, dass der anhand ihrer IP-Adressen ermittelte Standort anonymisiert oder verallgemeinert wird. Denken Sie daran, wenn Sie standortbasiertes Targeting oder Segmentierung verwenden.

