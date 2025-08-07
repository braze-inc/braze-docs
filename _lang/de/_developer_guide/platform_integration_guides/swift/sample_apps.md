---
nav_title: Beispiel-Apps
article_title: Beispiel-Apps für iOS
platform: Swift
page_order: 9
search_rank: 2
description: "Dieser Artikel behandelt iOS Swift SDK Beispielanwendungen."

---

# Beispiel-Apps

> Die Braze SDKs werden jeweils mit Beispielanwendungen im Repository geliefert. Jede dieser Apps ist vollständig bearbeitbar, sodass Sie die Features von Braze testen und gleichzeitig in Ihre eigenen Anwendungen implementieren können. 

Das Testen des Verhaltens Ihrer eigenen Anwendung im Vergleich zum erwarteten Verhalten und zu den Codepfaden in den Beispielanwendungen ist eine hervorragende Möglichkeit zur Fehlersuche bei Problemen.

## Navigieren durch die Beispiele

Der Ordner `Examples` des [Swift SDK GitHub Repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples) enthält mehrere Testanwendungen. In der README werden alle verschiedenen Permutationen von Beispiel-Integrationen beschrieben, wie z. B.:

1. Integrationsarten (Swift-Paketmanager, CocoaPods, Manuell)
2. Programmiersprachen (Swift und Objective-C)
3. Plattformen (iOS, tvOS, Mac Catalyst, usw.)
4. Funktionen (In-App-Nachrichten, Inhaltskarten, Standort, Rich Push, Push Stories usw.)
5. Anpassungsarten (Standard-Benutzeroberfläche, vollständig angepasste Benutzeroberfläche)

## Erstellen von Testanwendungen

Folgen Sie diesen Anweisungen, um unsere Testanwendungen zu erstellen und auszuführen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) und notieren Sie sich den App-Bezeichner, den API-Schlüssel und den Endpunkt.
2. Wählen Sie auf der Grundlage Ihrer Integrationsmethode (Swift-Paketmanager, CocoaPods, manuell) die entsprechende `xcodeproj`-Datei aus und öffnen Sie sie.
3. Setzen Sie Ihren API-Schlüssel und Ihren Endpunkt in das entsprechende Feld in der Datei `Credentials`.

