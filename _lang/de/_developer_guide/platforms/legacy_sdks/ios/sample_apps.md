---
nav_title: Beispiel-Apps
article_title: Beispiel-Apps für iOS
platform: iOS
page_order: 9
description: "Dieser referenzierte Artikel behandelt iOS Beispiel Apps."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Beispiel-Apps

Die SDKs von Braze enthalten jeweils Beispielanwendungen im Repository, die Ihnen zur Verfügung stehen. Jede dieser Apps ist vollständig bearbeitbar, sodass Sie die Features von Braze testen und gleichzeitig in Ihre eigenen Anwendungen implementieren können. Das Testen des Verhaltens Ihrer eigenen Anwendung im Vergleich zum erwarteten Verhalten und zu den Codepfaden in den Beispielanwendungen ist eine hervorragende Möglichkeit zur Fehlersuche bei Problemen.

## Erstellen von Testanwendungen
Mehrere Testanwendungen sind im [iOS SDK GitHub Repository](https://github.com/appboy/appboy-ios-sdk) verfügbar. Folgen Sie diesen Anweisungen, um unsere Testanwendungen zu erstellen und auszuführen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) und notieren Sie sich den Bezeichner des API-Schlüssels für die App.
2. Geben Sie Ihren API-Schlüssel in das entsprechende Feld in der Datei `AppDelegate.m` ein.

Push-Benachrichtigungen für die iOS-Testanwendung erfordern eine zusätzliche Konfiguration. Einzelheiten finden Sie in unserer [iOS Push Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/).

