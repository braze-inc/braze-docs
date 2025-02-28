---
nav_title: Anleitung zum Upgrade für iOS 17
article_title: Anleitung zum Upgrade für iOS 17
page_order: 7
platform: 
  - iOS
description: "Dieser Artikel enthält Informationen zum Release von iOS 17, damit Sie Ihr SDK nahtlos upgraden können."
hidden: true
noindex: true
---

# Anleitung zum Upgrade für  iOS 17

> Sind Sie neugierig, wie Braze sich auf die kommende iOS-Version vorbereitet? Dieser Artikel fasst unsere Insights zum iOS 17 Release zusammen, um Ihnen und Ihren Nutzer:innen ein nahtloses Erlebnis zu ermöglichen.

## Kompatibilität mit iOS 17 und Xcode 15

Das Braze Swift SDK und das Objective-C SDK sind beide rückwärtskompatibel mit Xcode 14 und Xcode 15 sowie mit iOS 17-Geräten.

## Änderungen in iOS 17

### Link Tracking und UTM-Parameter-Stripping

Eine der wichtigsten Änderungen in iOS 17 ist das Blockieren von UTM-Parametern in Safari. UTM-Parameter sind Codes, die zu URLs hinzugefügt werden. Sie werden häufig in Marketing-Kampagnen verwendet, um die Effektivität von E-Mail, SMS und anderen Messaging-Kanälen zu messen. 

Diese Änderung wirkt sich nicht auf das Tracking von E-Mail-Klicks und SMS-Linkverkürzungen aus.

### App Tracking-Transparenz

Apple kündigte an, den Anwendungsbereich von [Ad Tracking Transparency (ATT](https://support.apple.com/en-us/HT212025)) zu erweitern, mit dem Nutzer:innen kontrollieren können, ob eine App auf ihre Aktivitäten auf Apps und Websites anderer Unternehmen zugreifen kann. Die Version iOS 17 enthält zwei wichtige ATT-Features: Datenschutzmanifeste und Code Signing.

#### Datenschutz-Manifeste

Apple verlangt jetzt eine Datenschutzmanifest-Datei, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Methoden zur Datenerfassung beschreibt. Ab iOS 17.2 blockiert Apple alle deklarierten Tracking-Endpunkte in Ihrer App, bis der Endnutzer die ATT-Aufforderung akzeptiert.

Braze hat ein eigenes Datenschutzmanifest veröffentlicht, zusammen mit neuen flexiblen APIs, die angegebene Daten zum Tracking automatisch an spezielle `-tracking`-Endpunkte umleiten. Weitere Informationen finden Sie im [Datenschutzmanifest von Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

#### Code signieren

Code Signing erlaubt es Entwicklern, die ein SDK eines Drittanbieters in ihrer Anwendung verwenden, zu überprüfen, ob derselbe Entwickler diese Anwendung signiert hat wie frühere Versionen in Xcode. 

### Braze SDK und Datenschutz

Apple hat außerdem angekündigt, Ende 2023 eine Liste der SDKs von Drittanbietern zu veröffentlichen, die als "datenschutzrelevant" gelten. Es wird erwartet, dass diese SDKs von Apple einen besonders großen Einfluss auf die Privatsphäre der Nutzer haben werden.

Anders als herkömmliche Tracking-SDKs, die darauf ausgelegt sind, Nutzer über mehrere Websites und Anwendungen hinweg zu überwachen, konzentriert sich das Braze SDK auf First-Party-Daten-Messaging und Nutzererfahrungen.

Wir gehen zwar nicht davon aus, dass das Braze SDK in diese Liste aufgenommen wird, aber wir werden die Situation genau beobachten und gegebenenfalls Updates veröffentlichen.
