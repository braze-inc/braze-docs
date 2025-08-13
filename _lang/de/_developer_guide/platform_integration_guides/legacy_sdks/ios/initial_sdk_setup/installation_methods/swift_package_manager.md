---
nav_title: Swift Paket Manager
article_title: Swift Package Manager Integration für iOS
platform: iOS
page_order: 3
description: "Dieses Tutorial behandelt die Installation des Braze SDK mit dem Swift-Paketmanager für iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration von Swift Package Manager

Die Installation des iOS SDK über den [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie mit diesem Vorgang beginnen, stellen Sie sicher, dass Sie Xcode 12 oder höher verwenden.

{% alert note %}
tvOS ist derzeit nicht über den Swift Package Manager verfügbar.
{% endalert %}

## Schritt 1: Hinzufügen der Abhängigkeit zu Ihrem Projekt

### SDK-Version importieren

Öffnen Sie Ihr Projekt und navigieren Sie zu den Einstellungen Ihres Projekts. Wählen Sie die Registerkarte **Swift-Pakete** und klicken Sie auf die Schaltfläche <i class="fas fa-plus"></i> hinzufügen unterhalb der Paketliste.

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Wenn Sie SDK-Version `3.33.1` oder höher importieren, geben Sie die URL unseres iOS-SDK-Repository (`https://github.com/braze-inc/braze-ios-sdk`) in das Textfeld ein und klicken Sie auf **Weiter**. 

Für die Versionen `3.29.0` bis `3.32.0` verwenden Sie die URL `https://github.com/Appboy/Appboy-ios-sdk`.

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

Wählen Sie auf dem nächsten Bildschirm die SDK-Version aus und klicken Sie auf **Weiter**. Die Versionen `3.29.0` und höher sind mit dem Swift-Paketmanager kompatibel.

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### Pakete auswählen

Wählen Sie das Paket, das Ihren Anforderungen am besten entspricht, und klicken Sie auf **Fertig stellen**. Stellen Sie sicher, dass Sie entweder `AppboyKit` oder `AppboyUI` auswählen. Die Einbeziehung beider Pakete kann zu unerwünschtem Verhalten führen:

- `AppboyUI`
  - Am besten geeignet, wenn Sie die von Braze bereitgestellten UI-Komponenten verwenden möchten.
  - Enthält `AppboyKit` automatisch.
- `AppboyKit`
  - Am besten geeignet, wenn Sie keine der von Braze bereitgestellten UI-Komponenten (z. B. Content-Cards, In-App-Nachrichten usw.) verwenden müssen.
- `AppboyPushStory`
  - Fügen Sie dieses Paket hinzu, wenn Sie Push Stories in Ihre App integriert haben. Dies wird ab der Version `3.31.0` unterstützt.
  - Wählen Sie in der Dropdown-Liste unter `Add to Target` das Ziel für `ContentExtension` anstelle des Ziels Ihrer Hauptanwendung aus. 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## Schritt 2: Ihr Projekt konfigurieren

Als nächstes navigieren Sie zu den **Build-Einstellungen** Ihres Projekts und fügen das `-ObjC` Flag zur Einstellung **Andere Linker-Flags** hinzu. Dieses Flag muss hinzugefügt und eventuelle [Fehler](https://developer.apple.com/library/archive/qa/qa1490/_index.html) müssen behoben werden, um das SDK weiter integrieren zu können.

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Wenn Sie das Flag `-ObjC` nicht hinzufügen, können Teile der API fehlen und das Verhalten ist nicht definiert. Es kann zu unerwarteten Fehlern (z. B. "nicht erkannter Selektor an Klasse gesendet"), Abstürzen der Anwendung und anderen Problemen kommen.
{% endalert %}

## Schritt 3: Schema des Ziels bearbeiten
{% alert important %}
Wenn Sie Xcode 12.5 oder eine neuere Version verwenden, überspringen Sie diesen Schritt.
{% endalert %}

Wenn Sie Xcode 12.4 oder eine ältere Version verwenden, bearbeiten Sie das Schema des Ziels, einschließlich des Appboy-Pakets ( Menüpunkt **Produkt > Schema > Schema bearbeiten**):
1. Erweitern Sie das Menü **Erstellen** und wählen Sie **Post-Aktionen**. Drücken Sie auf das Pluszeichen (+) und wählen Sie **Neue Skriptaktion ausführen**.
2. Wählen Sie in der Dropdown-Liste **Build-Einstellungen bereitstellen von** das Ziel Ihrer App aus.
3.  Kopieren Sie dieses Skript in das offene Feld:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Nächste Schritte

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

