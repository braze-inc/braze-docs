---
nav_title: FAQ
article_title: Live-Aktivitäten FAQ
page_order: 20
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Live-Aktivitäten für das Swift SDK."
tool: Live Activities
platform:
  - iOS
---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Live-Aktivitäten.

## Funktionalität und Unterstützung

### Welche Plattformen unterstützen Live-Aktivitäten?

Live-Aktivitäten sind derzeit nur unter iOS als Feature verfügbar. Der Artikel "Live-Aktivitäten" beschreibt die [Voraussetzungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites) für die Verwaltung von Live-Aktivitäten über das Braze Swift SDK.

### Unterstützen React Native-Anwendungen Live-Aktivitäten?

Ja, React Native SDK 3.0.0+ unterstützt Live-Aktivitäten über das Braze Swift SDK. Das bedeutet, dass Sie React Native iOS Code direkt an den Anfang des Braze Swift SDK schreiben müssen. 

Es gibt keine React Native-spezifische JavaScript-API für Live-Aktivitäten, da die von Apple bereitgestellten Features für Live-Aktivitäten Sprachen verwenden, die nicht in JavaScript übersetzbar sind (z. B. Swift Concurrency, Generics, SwiftUI).

### Unterstützt Braze Live-Aktivitäten als eine Kampagne oder einen Canvas-Schritt?

Nein, dies wird derzeit nicht unterstützt.

## Push-Benachrichtigungen und Live-Aktivitäten

### Was passiert, wenn während einer aktiven Live-Aktivität eine Push-Benachrichtigung gesendet wird? 

![Ein Telefonbildschirm mit einem Live-Sportspiel der Bulls gegen die Bears in der Mitte des Bildschirms und einer Push-Benachrichtigung mit dem Text lorem ipsum am unteren Rand des Bildschirms.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Live-Aktivitäten und Push-Benachrichtigungen belegen unterschiedlichen Platz auf dem Bildschirm und stehen nicht im Konflikt mit dem Bildschirm des Benutzers.

### Wenn Live-Aktivitäten die Push-Nachrichtenfunktion nutzen, müssen dann Push-Benachrichtigungen aktiviert sein, um Live-Aktivitäten zu empfangen?

Während Live-Aktivitäten auf Push-Benachrichtigungen für Aktualisierungen angewiesen sind, werden diese durch unterschiedliche Benutzereinstellungen gesteuert. Nutzer haben die Möglichkeit, sich für Live-Aktivitäten anzumelden und für Push-Benachrichtigungen abzumelden und umgekehrt.

Live Activity Update-Token verfallen nach acht Stunden.

### Sind für Live-Aktivitäten Push-Primer erforderlich?

[Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) sind eine bewährte Methode, um Ihre Benutzer aufzufordern, sich für Push-Benachrichtigungen von Ihrer App zu entscheiden. Es gibt jedoch keine Systemaufforderung, um sich für Live-Aktivitäten anzumelden. Nutzer werden standardmäßig für eine einzelne App für Live-Aktivitäten angemeldet, wenn die betreffende App unter iOS 16.1 oder höher installiert wird. Diese Berechtigung kann in den Geräteeinstellungen für jede App einzeln deaktiviert oder wieder aktiviert werden.

## Technische Themen und Fehlerbehebung

### Wie erkenne ich, ob Live Activities Fehler aufweist?

Fehler in Bezug auf Live-Aktivitäten werden im Braze-Dashboard im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) protokolliert, das Sie nach "LiveActivity-Fehlern" filtern können.

### Warum habe ich nach dem Senden einer Push-to-Start-Benachrichtigung meine Live-Aktivität nicht erhalten?

Überprüfen Sie zunächst, ob die Nutzlast alle erforderlichen Felder enthält, die im Endpunkt [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) beschrieben sind. Die Felder `activity_attributes` und `content_state` sollten mit den im Code Ihres Projekts definierten Eigenschaften übereinstimmen. Ist die Nutzlast korrekt, kann es sein, dass ein Rate-Limit durch APNs vorliegt. Dieses Limit wird von Apple festgelegt und nicht von Braze.

Um zu überprüfen, ob Ihre Push-to-Start-Benachrichtigung erfolgreich auf dem Gerät angekommen ist, aber aufgrund von Ratenbeschränkungen nicht angezeigt wurde, können Sie Ihr Projekt mit der Konsolen-App auf Ihrem Mac debuggen. Hängen Sie den Aufzeichnungsprozess für Ihr gewünschtes Gerät an und filtern Sie dann die Protokolle nach `process:liveactivitiesd` in der Suchleiste.

### Ich erhalte die Antwort "Zugriff verweigert", wenn ich versuche, den Endpunkt `live_activity/update` zu verwenden. Und warum?

Die API-Schlüssel, die Sie verwenden, müssen mit den richtigen Berechtigungen für den Zugriff auf die verschiedenen Braze-API-Endpunkte ausgestattet sein. Wenn Sie einen zuvor erstellten API-Schlüssel verwenden, haben Sie möglicherweise versäumt, dessen Berechtigungen zu aktualisieren. Ausführlichere Informationen finden Sie in unserer [Übersicht zur Sicherheit von API-Schlüsseln]({{site.baseurl}}/api/basics/#rest-api-key-security).

### Hat der Endpunkt `messages/send` die gleichen Tarifgrenzen wie der Endpunkt `messages/live_activity/update`? 

Standardmäßig liegt das Rate-Limit für den Endpunkt `messages/live_activity/update` bei 250.000 Anfragen pro Stunde und Workspace und über mehrere Endpunkte hinweg. Weitere Informationen finden Sie in den [API-Tarifgrenzen]({{site.baseurl}}/api/api_limits/).

### Warum werden meine Push-to-Start-Token nicht generiert?

Apple hat seine in iOS 17.2 eingeführten APIs `pushToStartToken` und `pushToStartTokenUpdates` eingeschränkt. In der Praxis werden Push-to-Start-Token nur beim ersten Start der App in `application(_:didFinishLaunchingWithOptions:)` nach der Erstinstallation generiert. Wenn dieser Schritt wiederholt werden muss, können die Token nur durch die manuelle Erstellung einer neuen Instanz dieser Live-Aktivität oder nach einem Neustart und einer Neuinstallation der App erneut erzeugt werden.

### Wie viele Live-Aktivitäten kann ich für meine App starten?

Die Grenzen werden von Apple festgelegt und können je nach einer Reihe von Faktoren variieren. Sie können auch in Zukunft Änderungen unterliegen. In der Praxis gibt es ein Limit von fünf gleichzeitigen Aktivitäts-Instanzen, die zu einem bestimmten Zeitpunkt pro App gestartet werden können. Alle weiteren Versuche, eine neue Instanz über dieses Limit hinaus zu starten, werden vom System ignoriert.

### Auf welche anderen Dinge sollte ich bei der Fehlersuche achten?

- Vergewissern Sie sich, dass Sie einen `.p8`-Schlüssel zur Authentifizierung verwenden und keine `.p12`\- oder `.pem`-Datei.
- Vergewissern Sie sich, dass Ihr Push-Bereitstellungsprofil mit der Test-Umgebung übereinstimmt. Universelle Zertifikate können im Braze Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktionsumgebung des Apple Push Notification Service (APNs) gesendet werden. Die Verwendung eines Entwicklungszertifikats für eine Produktionsanwendung oder eines Produktionszertifikats für eine Entwicklungsanwendung wird nicht funktionieren.


