---
nav_title: visionOS-Unterstützung
article_title: visionOS-Unterstützung
page_order: 7.2
platform: 
  - iOS
description: "Dieser Artikel behandelt die Features, die von visionOS unterstützt werden."
---

# visionOS-Unterstützung

> Ab [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) können Sie Braze mit [visionOS](https://developer.apple.com/visionos/) nutzen, der Raumfahrt-Computerplattform von Apple für den Apple Vision Pro. Ein Beispiel für eine visionOS-App, die Braze verwendet, finden Sie unter [Beispiel-Apps]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/).

## Vollständig unterstützte Features

Die meisten Features, die unter iOS verfügbar sind, stehen auch unter visionOS zur Verfügung, darunter:

- Analytics (Sitzungen, angepasste Events, Käufe, etc.)
- In-App Messaging (Datenmodelle und UI)
- Content-Cards (Datenmodelle und UI)
- Push-Benachrichtigungen (für Nutzer:innen sichtbar mit Aktions-Buttons und stillen Benachrichtigungen)
- Feature-Flags
- Standort-Analytics

## Teilweise unterstützte Features

Einige Features werden von visionOS nur teilweise unterstützt, aber Apple wird sich wahrscheinlich in Zukunft um diese kümmern:

- Rich-Push-Benachrichtigungen
  - Bilder werden unterstützt.
  - GIFs und Videos zeigen die Vorschau-Miniaturansicht an, können aber nicht abgespielt werden.
  - Die Audiowiedergabe wird nicht unterstützt.
- Push-Storys
  - Das Blättern und Auswählen der Push-Story-Seite wird unterstützt.
  - Das Navigieren zwischen Push Story Seiten mit **Weiter** wird nicht unterstützt.

## Nicht unterstützte Features

- Geofences Monitoring wird nicht unterstützt. Apple hat die Core Location APIs für die Überwachung von Standorten in visionOS nicht zur Verfügung gestellt.
- Live-Aktivitäten werden nicht unterstützt. Derzeit ist ActivityKit nur auf iOS und iPadOS verfügbar.
