---
nav_title: Swift Paket Manager
article_title: Swift Package Manager Integration für iOS
platform: Swift
page_order: 1
description: "Dieses Tutorial behandelt die Installation des Braze Swift SDK mit dem Swift-Paketmanager für iOS."

---

# Integration von Swift Package Manager

> Die Installation des Swift SDK über den [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatisiert den Großteil des Installationsprozesses für Sie. Überprüfen Sie die [Versionsinformationen](https://github.com/braze-inc/braze-swift-sdk#version-information), bevor Sie mit diesem Vorgang beginnen, um sicherzustellen, dass Ihre Umgebung von Braze unterstützt wird.

## Hinzufügen der Abhängigkeit zu Ihrem Projekt

### SDK-Version importieren

Öffnen Sie Ihr Projekt und navigieren Sie zu den Einstellungen Ihres Projekts. Wählen Sie die Registerkarte **Swift-Pakete** und klicken Sie auf die Schaltfläche <i class="fas fa-plus"></i> hinzufügen unterhalb der Paketliste.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen vom jeweiligen Repository.
{% endalert %}

Geben Sie die URL unseres iOS Swift SDK-Repository `https://github.com/braze-inc/braze-swift-sdk` in das Textfeld ein. Wählen Sie unter dem Abschnitt **Abhängigkeitsregel** die SDK-Version aus. Klicken Sie schließlich auf **Paket hinzufügen**.

![]({% image_buster /assets/img/importsdk_example.png %})

### Pakete auswählen

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwicklern mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten.

| Paket | Details |
| ------- | ------- |
| `BrazeKit` | Haupt-SDK-Bibliothek mit Unterstützung für Analysen und Push-Benachrichtigungen. |
| `BrazeLocation` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung. |
| `BrazeUI` | Die von Braze bereitgestellte Benutzeroberflächenbibliothek für In-App-Nachrichten und Content Cards. |
{: .ws-td-nw-1}

#### Erweiterungsbibliotheken

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Folgen Sie stattdessen den verlinkten Anleitungen, um sie separat in ihre jeweiligen Zielerweiterungen zu integrieren.
{% endalert %}

| Paket | Details |
| ------- | ------- |
| `BrazeNotificationService` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für umfangreiche Push-Benachrichtigungen. |
| `BrazePushStory` | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories. |
{: .ws-td-nw-1}

 Wählen Sie das Paket, das Ihren Anforderungen am besten entspricht, und klicken Sie auf **Paket hinzufügen**. Stellen Sie sicher, dass Sie mindestens `BrazeKit` auswählen.

![]({% image_buster /assets/img/add_package.png %})

## Nächste Schritte

Folgen Sie den Anweisungen, um [die Integration abzuschließen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

