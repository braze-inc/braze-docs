---
nav_title: iOS
article_title: SDK iOS Integration für Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "Dieser Referenzartikel beschreibt die iOS SDK-Integration für die Unity-Plattform."
search_rank: .9
---

# SDK iOS Integration

> Dieser Referenzartikel beschreibt die iOS SDK-Integration für die Unity-Plattform. Folgen Sie dieser Anleitung, um Braze in Ihrer Unity-Anwendung zum Laufen zu bringen. 

Wenn Sie von einer manuellen Integration zu einer automatisierten Integration wechseln, folgen Sie den Anweisungen unter [Übergang zu einer automatisierten Integration](#transitioning-from-manual-to-automated-integration-ios).

## Schritt 1: Wählen Sie Ihr Braze Unity-Paket

Das Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bündelt native Bindings für die Plattformen Android und iOS sowie eine C#-Schnittstelle.

Das Braze Unity-Paket steht auf der [Seite Braze Unity Releases](https://github.com/Appboy/appboy-unity-sdk/releases) mit zwei Integrationsoptionen zum Download bereit:

1. Nur `Appboy.unitypackage`
  - Dieses Paket bündelt die Braze Android und iOS SDKs ohne zusätzliche Abhängigkeiten. Mit dieser Integrationsmethode werden die In-App-Nachrichten von Braze und die Content Cards-Funktionen auf iOS nicht richtig funktionieren. Wenn Sie die volle Funktionalität von Braze ohne benutzerdefinierten Code nutzen möchten, verwenden Sie stattdessen die unten stehende Option.
  - Um diese Integrationsoption zu nutzen, stellen Sie sicher, dass das Kästchen neben `Import SDWebImage dependency` in der Unity-UI unter "Braze-Konfiguration" *deaktiviert* ist.
2. `Appboy.unitypackage` mit `SDWebImage`
  - Diese Integrationsoption bündelt die Braze Android- und iOS-SDKs und die [SDWebImage-Abhängigkeit](https://github.com/SDWebImage/SDWebImage) für das iOS-SDK, die für die ordnungsgemäße Funktionalität der In-App-Nachrichten von Braze und der Content Cards-Funktionen auf iOS erforderlich ist. Das Framework `SDWebImage` wird zum Herunterladen und Anzeigen von Bildern, einschließlich GIFs, verwendet. Wenn Sie die volle Funktionalität von Braze nutzen möchten, laden Sie dieses Paket herunter und importieren Sie es.
  - Um `SDWebImage` automatisch zu importieren, müssen Sie das Kästchen neben `Import SDWebImage dependency` in der Unity-UI unter "Braze-Konfiguration" *aktivieren*.

**iOS**: Um festzustellen, ob Sie die [SDWebImage-Abhängigkeit](https://github.com/SDWebImage/SDWebImage) für Ihr iOS-Projekt benötigen, besuchen Sie die [Dokumentation zu iOS In-App-Nachrichten]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: Ab Unity 2.6.0 benötigt das gebündelte Braze Android SDK-Artefakt [AndroidX-Abhängigkeiten](https://developer.android.com/jetpack/androidx). Wenn Sie zuvor ein `jetified unitypackage` verwendet haben, können Sie bedenkenlos auf das entsprechende `unitypackage` umsteigen.

## Schritt 2: Paket importieren

Importieren Sie das Paket in Ihr Unity-Projekt, indem Sie im Unity-Editor zu **Assets > Paket importieren > Angepasstes Paket** navigieren. Klicken Sie anschließend auf **Importieren**.

Alternativ folgen Sie den Anweisungen zum [Importieren von Unity-Assetpaketen](https://docs.unity3d.com/Manual/AssetPackages.html), um eine detailliertere Anleitung zum Importieren von benutzerdefinierten Unity-Paketen zu erhalten. 

{% alert note %}
Wenn Sie nur das iOS- oder Android-Plugin importieren möchten, heben Sie die Auswahl des Unterverzeichnisses `Plugins/Android` bzw. `Plugins/iOS` auf, wenn Sie das Braze `.unitypackage` importieren.
{% endalert %}

## Schritt 3: Legen Sie Ihren API-Schlüssel fest

Braze bietet eine native Unity-Lösung für die Automatisierung der Unity iOS-Integration. Bei dieser Lösung wird das erstellte Xcode-Projekt mit [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) von Unity modifiziert und `UnityAppController` mithilfe des Makros `IMPL_APP_CONTROLLER_SUBCLASS` unterteilt.

1. Öffnen Sie im Unity-Editor die Braze-Konfigurationseinstellungen, indem Sie zu **Braze > Braze-Konfiguration** navigieren.
2. Markieren Sie das Kästchen **Unity iOS-Integration automatisieren**.
3. Geben Sie in das Feld **Braze API-Schlüssel** den API-Schlüssel Ihrer Anwendung ein, den Sie unter **Einstellungen verwalten** finden.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Wenn Ihre Anwendung bereits eine andere `UnityAppController`-Unterklasse verwendet, müssen Sie die Implementierung Ihrer Unterklasse mit `AppboyAppDelegate.mm` zusammenführen.

## Grundlegende SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung erfassen und die grundlegende Integration sollte abgeschlossen sein. Weitere Informationen zur Integration von Push finden Sie in den folgenden Artikeln: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) und [Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Weitere Informationen zu den Optionen für die erweiterte SDK-Integration finden Sie unter [Fortgeschrittene Implementierung]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced).

