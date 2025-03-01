---
nav_title: CocoaPods
article_title: CocoaPods Integration für iOS
platform: Swift
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie das Braze Swift SDK mit CocoaPods für iOS integrieren."

---

# Integration von CocoaPods

## Schritt 1: CocoaPods installieren

Die Installation des iOS SDK über [CocoaPods](http://cocoapods.org/) automatisiert den Großteil des Installationsprozesses für Sie. Um CocoaPods zu installieren, lesen Sie bitte die [Ersten Schritte zu CocoaPods](https://guides.cocoapods.org/using/getting-started.html).

Führen Sie den folgenden Befehl aus:

```bash
$ sudo gem install cocoapods
```

Wenn Sie Probleme mit CocoaPods haben, lesen Sie die [Anleitung zur FehlerbehebungCocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "Troubleshooting Guide").

## Schritt 2: Erstellen der Poddatei

Nachdem Sie den CocoaPods Ruby Gem installiert haben, müssen Sie in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile` erstellen.

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen vom jeweiligen Repository.
{% endalert %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` enthält die wichtigste SDK-Bibliothek mit Unterstützung für Analytics und Push-Benachrichtigungen.

Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als eine kleine Versionsaktualisierung ist. Dies sieht folgendermaßen aus: `pod 'BrazeKit' ~> Major.Minor.Build`. Wenn Sie die neueste Version des Braze SDK auch bei größeren Änderungen automatisch integrieren möchten, können Sie `pod 'BrazeKit'` in Ihrem Podfile verwenden.

#### Zusätzliche Bibliotheken

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwicklern mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten. Zusätzlich zu `BrazeKit` können Sie die folgenden Bibliotheken zu Ihrem Podfile hinzufügen:

| Bibliothek | Details |
| ------- | ------- |
| `pod 'BrazeLocation'` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung. |
| `pod 'BrazeUI'` | Die von Braze bereitgestellte Benutzeroberflächenbibliothek für In-App-Nachrichten und Content Cards. |
{: .ws-td-nw-1}

##### Erweiterungsbibliotheken

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Stattdessen müssen Sie für jedes dieser Module eigene Erweiterungs-Targets erstellen und die Braze-Module in ihre entsprechenden Targets importieren.

| Bibliothek | Details |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für umfangreiche Push-Benachrichtigungen. |
| `pod 'BrazePushStory'` | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories. |
{: .ws-td-nw-1}

## Schritt 3: Installieren des Braze SDK

Um die Braze SDK CocoaPod zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den von CocoaPods erstellten neuen Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.

![Ein Braze-Beispielordner, der erweitert wurde, um die neue `BrazeExample.workspace` zu zeigen.]({% image_buster /assets/img/braze_example_workspace.png %})

## Nächste Schritte

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Aktualisieren des Braze SDK über CocoaPods

Um einen CocoaPod zu aktualisieren, führen Sie einfach den folgenden Befehl in Ihrem Projektverzeichnis aus:

```
pod update
```

