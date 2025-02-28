---
nav_title: Karthago
article_title: Carthage Integration für iOS
platform: iOS
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie das Braze SDK mit Carthage für iOS integrieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration von Karthago

## SDK importieren

Ab Version `4.4.0` werden bei der Integration über Carthage XCFrameworks vom Braze SDK unterstützt. Um das vollständige SDK zu importieren, fügen Sie diese Zeilen in `Cartfile` ein:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Ziehen Sie für weitere Anweisungen zum Importieren des SDK die [Schnellstartanleitung für Carthage](https://github.com/Carthage/Carthage#quick-start) zurate.

Wenn Sie von einer Version vor `4.4.0` migrieren, folgen Sie dem [Carthage Migrationsleitfaden für XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Weitere Informationen zur Syntax von `Cartfile` oder zu Features wie dem Version-Pinning finden Sie in der [Carthage-Dokumentation](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Informationen zur plattformspezifischen Verwendung von Carthage entnehmen Sie bitte dem [Benutzerhandbuch](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Frühere Versionen

Fügen Sie für die Versionen `3.24.0` bis `4.3.4` Folgendes in `Cartfile` ein:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Um Versionen vor `3.24.0` zu importieren, fügen Sie Folgendes in `Cartfile` ein:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Stellen Sie sicher, dass Sie `<BRAZE_IOS_SDK_VERSION>` durch die [entsprechende Version](https://github.com/Appboy/appboy-ios-sdk/releases) des Braze iOS SDK im Format "x.y.z" ersetzen.

## Nächste Schritte

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Nur-Core-Integration

Wenn Sie das Core SDK ohne UI-Komponenten oder Abhängigkeiten verwenden möchten, installieren Sie die Core-Version des Braze Carthage Frameworks, indem Sie die folgende Zeile in `Cartfile` einfügen:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

