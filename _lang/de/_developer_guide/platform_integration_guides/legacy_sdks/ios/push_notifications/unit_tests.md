---
nav_title: Einheitstests (optional)
article_title: Push-Benachrichtigung Unit Tests für iOS
platform: iOS
page_order: 29.5
description: "Dieser Referenzartikel beschreibt, wie Sie optionale Unit-Tests für Ihre iOS Push-Implementierung implementieren."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Einheitstests {#unit-tests}

Diese optionale Anleitung beschreibt, wie Sie einige Unit-Tests implementieren, mit denen Sie überprüfen können, ob Ihr App-Delegierter die in unseren [Anweisungen zur Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) beschriebenen Schritte korrekt ausführt. 

Wenn alle Tests erfolgreich sind, bedeutet dies im Allgemeinen, dass der Code-basierte Teil Ihrer Push-Einrichtung funktionsfähig ist. Wenn ein Test fehlschlägt, kann dies bedeuten, dass Sie einen Schritt falsch befolgt haben, oder es kann das Ergebnis einer gültigen Anpassung sein, die nicht genau mit unseren Standardanweisungen übereinstimmt.

In jedem Fall können Sie auf diese Weise überprüfen, ob Sie die Schritte der Integration befolgt haben und ob es zu Regressionen gekommen ist.

## Schritt 1: Erstelle Sie ein Unit-Tests-Ziel

Überspringen Sie diesen Schritt, wenn Ihr App-Projekt in Xcode bereits ein Unit Testing Bundle enthält.

Wählen Sie in Ihrem App-Projekt das Menü **File > New > Target** und fügen Sie ein neues "Unit Testing Bundle" hinzu. Dieses Bundle kann entweder Objective-C oder Swift verwenden und einen beliebigen Namen haben. Setzen Sie das "Target to be Tested" auf Ihr App-Hauptziel.

## Schritt 2: Fügen Sie das Braze SDK zu Ihren Unit-Tests hinzu

Stellen Sie mit der gleichen Methode, mit der Sie [das Braze SDK installiert]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) haben, sicher, dass die gleiche SDK-Installation auch für das Targeting Ihrer Unit-Tests verfügbar ist. Zum Beispiel mit CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Schritt 3: Fügen Sie OCMock zu Ihren Unit-Tests hinzu

Fügen Sie [OCMock](https://ocmock.org/) über CocoaPods, Carthage oder seine statische Bibliothek zu Ihrem Targeting hinzu. Zum Beispiel mit CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Schritt 4: Beenden Sie die Installation der hinzugefügten Bibliotheken

Beenden Sie die Installation von Braze SDK und OCMock. Wenn Sie zum Beispiel CocoaPods verwenden, gehen Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode App-Projekts und führen Sie den folgenden Befehl aus:

```
pod install
```

Jetzt sollten Sie in der Lage sein, den von CocoaPods erstellten Workspace des Xcode-Projekts zu öffnen.

## Schritt 5: Hinzufügen von Push-Tests

Erstellen Sie eine neue Objective-C Datei in Ihrem Unit Tests Targeting. 

Wenn das Target der Unit-Tests in Swift ist, fragt Xcode möglicherweise, ob Sie einen Objective-C Bridging Header konfigurieren möchten. Der Bridging Header ist optional. Sie können also auf **Don't Create** klicken und die Unit-Tests trotzdem durchführen.

Fügen Sie den Inhalt der HelloSwift Beispiel App [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) in die neue Datei ein.

## Schritt 6: Test-Suite ausführen

Führen Sie die Unit-Tests Ihrer App aus. Dies kann ein einmaliger Überprüfungsschritt sein, oder Sie können ihn unbegrenzt in Ihre Suite aufnehmen, um eventuelle Regressionen abzufangen.

