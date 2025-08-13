---
nav_title: Manuelle Integration
article_title: Manuelle Integration für iOS
platform: Swift
page_order: 3
description: "Dieser Referenzartikel zeigt, wie Sie das Braze Swift SDK mithilfe einer manuellen Installation integrieren."
toc_headers: "h2"
---

# Manuelle Integration

> Wenn Sie keinen Zugriff auf einen Paketmanager wie [Swift-Paketmanager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) oder [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/) haben, können Sie stattdessen das Swift SDK manuell integrieren.

## Schritt 1: Laden Sie das Braze SDK herunter

Rufen Sie die [Braze SDK Release-Seite auf GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) auf und laden Sie `braze-swift-sdk-prebuilt.zip` herunter.

!["Die Braze SDK Release-Seite auf GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Schritt 2: Wählen Sie Ihre Frameworks aus

Das Braze Swift SDK enthält eine Vielzahl von eigenständigen XCFrameworks, die Ihnen die Freiheit geben, nur die gewünschten Features zu integrieren. Verwenden Sie folgende Tabelle, um Ihre XCFrameworks auszuwählen:

| Paket                    | Erforderlich? | Beschreibung                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Ja       | Die SDK-Hauptbibliothek, die Unterstützung für Analytics und Push-Benachrichtigungen bietet                                                                                                                                                                                                                                             |
| `BrazeLocation`            | Kein:e        | Bibliothek für Standorte mit Unterstützung für Analytics und Geofence-Überwachung.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | Kein:e        | Die von Braze bereitgestellte Benutzeroberflächenbibliothek für In-App-Nachrichten und Content Cards.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | Kein:e        | Bibliothek zur Erweiterung des Benachrichtigungsdienstes mit Unterstützung für Rich-Push-Benachrichtigungen. Fügen Sie diese Bibliothek nicht direkt zum Hauptanwendungsziel hinzu, sondern [fügen Sie `BrazeNotificationService` separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).     |
| `BrazePushStory`           | Kein:e        | Bibliothek zur Erweiterung von Benachrichtigungsinhalten, die Push-Storys unterstützt. Fügen Sie diese Bibliothek nicht direkt zum Hauptanwendungsziel hinzu, sondern [fügen Sie `BrazePushStory` separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                     |
| `BrazeKitCompat`           | Kein:e        | Kompatibilitätsbibliothek mit allen `Appboy`- und `ABK*`-Klassen und -Methoden, die in der `Appboy-iOS-SDK` Version 4X.X. verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | Kein:e        | Kompatibilitätsbibliothek mit allen `ABK*`-Klassen und -Methoden, die in der Bibliothek `AppboyUI` in `Appboy-iOS-SDK` Version 4X.X. verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Kein:e        | Die Abhängigkeit wird nur von `BrazeUICompat` im minimalen Migrationsszenario verwendet. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 3: Bereiten Sie Ihre Dateien vor

Entscheiden Sie, ob Sie **statische** oder **dynamische** XCFrameworks verwenden möchten, und bereiten Sie dann Ihre Dateien vor:

{% tabs %}
{% tab dynamic %}
1. Erstellen Sie ein temporäres Verzeichnis für Ihre XCFrameworks.
2. Öffnen Sie in `braze-swift-sdk-prebuilt` das Verzeichnis `dynamic` und verschieben Sie `BrazeKit.xcframework` in Ihr Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Verschieben Sie jedes der von Ihnen [gewählten XCFrameworks](#step-2-choose-your-frameworks) in Ihr temporäres Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab static %}
### Schritt 3.1: Bereiten Sie Ihre Frameworks vor

1. Erstellen Sie ein temporäres Verzeichnis für Ihre XCFrameworks.
2. Öffnen Sie in `braze-swift-sdk-prebuilt` das Verzeichnis `static` und verschieben Sie `BrazeKit.xcframework` in Ihr Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. Verschieben Sie jedes der von Ihnen [gewählten XCFrameworks](#step-2-choose-your-frameworks) in Ihr temporäres Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### Schritt 3.2: Bereiten Sie Ihre Bundles vor

1. Erstellen Sie ein temporäres Verzeichnis für Ihre Bundles.
2. Öffnen Sie das Verzeichnis `bundles` und verschieben Sie `BrazeKit.bundle` in Ihr Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. Wenn Sie die XCFrameworks `BrazeLocation`, `BrazeUI`, `BrazeUICompat`, oder `SDWebImage` verwenden, verschieben Sie die entsprechenden Bundles in Ihr temporäres Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
Übertragen Sie nur Pakete für die [von Ihnen vorbereiteten Frameworks](#step-31-prepare-your-frameworks).
{% endalert %}
{% endtab %}
{% endtabs %}

## Schritt 4: Integrieren Sie Ihre Frameworks

Als Nächstes integrieren Sie die **dynamischen** oder **statischen** XCFrameworks, die Sie [zuvor vorbereitet haben](#step-3-prepare-your-files):

{% tabs %}
{% tab dynamic %}
Wählen Sie in Ihrem Xcode-Projekt Ihr Build-Target und dann **Allgemein**. Ziehen Sie die [Dateien, die Sie zuvor vorbereitet haben](#step-3-prepare-your-files), per Drag-and-Drop unter **Frameworks, Bibliotheken und eingebettete Inhalte**.

!["Ein Xcode-Beispielprojekt, bei dem jede Bibliothek von Braze auf 'Einbetten & Signieren' eingestellt ist."]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
Um die GIF-Unterstützung zu aktivieren, fügen Sie `SDWebImage.xcframework` hinzu, das sich unter `braze-swift-sdk-prebuilt/dynamic` befindet.
{% endalert %}
{% endtab %}

{% tab static %}
Wählen Sie in Ihrem Xcode-Projekt Ihr Build-Target und dann **Allgemein**. Unter **Frameworks, Bibliotheken und eingebettete Inhalte** ziehen Sie die [Frameworks, die Sie zuvor vorbereitet haben](#step-31-prepare-your-frameworks), per Drag-and-Drop. Wählen Sie neben jedem Framework die Option **Nicht einbetten**. 

!["Ein Xcode-Beispielprojekt, bei dem jede Bibliothek von Braze auf 'Nicht einbetten' gesetzt ist."]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
Um die GIF-Unterstützung zu aktivieren, fügen Sie `SDWebImage.xcframework` hinzu, das sich unter `braze-swift-sdk-prebuilt/static` befindet.
{% endalert %}

Während Sie sich in Ihrem Targeting befinden, wählen Sie **Bauphasen** aus. Platzieren Sie unter **Bundle-Ressourcen kopieren** per Drag-and-Drop die [Bundles, die Sie zuvor vorbereitet haben](#step-32-prepare-your-bundles).

!["Ein Xcode-Beispielprojekt mit Bundles, die unter 'Bundle-Ressourcen kopieren' hinzugefügt wurden."]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Häufige Fehler bei Objective-C Projekten

Wenn Ihr Xcode-Projekt nur Objective-C-Dateien enthält, erhalten Sie möglicherweise die Fehlermeldung "Fehlendes Symbol", wenn Sie versuchen, Ihr Projekt zu erstellen. Um diese Fehler zu beheben, öffnen Sie Ihr Projekt und fügen Sie eine leere Swift-Datei zu Ihrem Dateibaum hinzu. Dadurch wird Ihre Build-Toolchain gezwungen, [Swift Runtime](https://support.apple.com/kb/dl1998) einzubetten und während der Build-Zeit eine Verbindung zu den entsprechenden Frameworks herzustellen.

```bash
FILE_NAME.swift
```

Ersetzen Sie `FILE_NAME` durch einen beliebigen String ohne Leerzeichen. Ihre Datei sollte etwa so aussehen wie die folgende:

```bash
empty_swift_file.swift
```
