---
nav_title: Fortschrittliche Implementierung
article_title: Fortschrittliche SDK-Implementierung
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Dieser Referenzartikel behandelt die erweiterte SDK-Implementierung für die Unity-Plattform."
---

# Erweiterte Implementierung

> Dieser Referenzartikel behandelt die erweiterte SDK-Implementierung für die Unity-Plattform.

## Anpassen des Unity-Pakets

Sie können das Braze Unity-Paket mithilfe der mitgelieferten Skripte anpassen und exportieren.

1. Klonen Sie das [Braze Unity SDK GitHub Projekt](https://github.com/appboy/appboy-unity-sdk):

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. Gehen Sie in das Verzeichnis `braze-unity-sdk/scripts` und führen Sie `./generate_package.sh` aus, um die Unity-Pakete zu exportieren. Unity muss geöffnet sein, während Sie `generate_package.sh` ausführen.
3. Die Pakete werden nach `braze-unity-sdk/unity-package/` exportiert.
4. Importieren Sie im Unity-Editor das gewünschte Paket in Ihr Unity-Projekt, indem Sie zu **Assets** > **Paket importieren** > Benutzerdefiniertes Paket navigieren.
5. (optional) Heben Sie die Markierung der Dateien auf, die Sie nicht importieren möchten.

Sie können das exportierte Unity-Paket anpassen, indem Sie sowohl `generate_package.sh` als auch das Exportskript unter `Assets/Editor/Build.cs` bearbeiten.

## Prime 31 Kompatibilität

Um das Braze Unity-Plugin mit Prime31-Plugins zu verwenden, bearbeiten Sie die `AndroidManifest.xml` Ihres Projekts, um die mit Prime31 kompatiblen Activity-Klassen zu verwenden. Ändern Sie alle Referenzen von
`com.braze.unity.BrazeUnityPlayerActivity` bis `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Amazon ADM Push

Braze unterstützt die Integration von [Amazon ADM Push](https://developer.amazon.com/public/apis/engage/device-messaging) in Unity Apps. Wenn Sie Amazon ADM Push integrieren möchten, erstellen Sie eine Datei mit dem Namen `api_key.txt`, die Ihren ADM API-Schlüssel enthält, und legen Sie sie im Ordner `Plugins/Android/assets/` ab.  Weitere Informationen zur Integration von Amazon ADM mit Braze finden Sie in unserer [Anleitung zur ADM Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Android SDK vorgebrachte Implementierungsoptionen {#android-sdk-advanced}

### Enablement der ausführlichen Protokollierung im Unity-Editor
Um die ausführliche Protokollierung im Unity-Editor zu aktivieren, gehen Sie wie folgt vor:

1. Öffnen Sie die Einstellungen für die Braze-Konfiguration, indem Sie zu **Braze** > **Braze-Konfiguration** navigieren.
2. Klicken Sie auf das Dropdown-Menü **Braze Android-Einstellungen anzeigen**.
3. Geben Sie im Feld **SDK Log Level** den Wert "0" ein.

### Erweitern des Braze Unity Players (Android) {#extending-braze-unity-player}

In der mitgelieferten Beispieldatei `AndroidManifest.xml` ist eine Activity-Klasse registriert, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Diese Klasse ist in das Braze SDK integriert und erweitert `UnityPlayerActivity` um Sitzungsverarbeitung, In-App-Nachricht-Registrierung, Push-Benachrichtigungs-Analytics-Protokollierung und mehr. Weitere Informationen zur Erweiterung der Klasse `UnityPlayerActivity` finden Sie in [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html).

Wenn Sie Ihre eigene angepasste `UnityPlayerActivity` in einer Bibliothek oder einem Plugin-Projekt erstellen, müssen Sie unsere `BrazeUnityPlayerActivity` erweitern, um Ihre angepasste Funktionalität mit Braze zu integrieren. Bevor Sie mit der Erweiterung von `BrazeUnityPlayerActivity` beginnen, befolgen Sie unsere Anweisungen zur Integration von Braze in Ihr Unity-Projekt.
1. Fügen Sie das Braze Android SDK als Abhängigkeit zu Ihrer Bibliothek oder Ihrem Plugin-Projekt hinzu, wie in den [Anweisungen zur Braze Android SDK-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) beschrieben.
2. Integrieren Sie unsere `.aar`-Datei, die unsere Unity-spezifische Funktionalität enthält, in Ihr Android-Bibliothek-Projekt. Die `appboy-unity.aar` ist in unserem [öffentlichen repo](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android) verfügbar. Nachdem unsere Unity Bibliothek erfolgreich integriert wurde, ändern Sie Ihre `UnityPlayerActivity`, um `BrazeUnityPlayerActivity` zu erweitern.
3. Exportieren Sie Ihre Bibliothek oder Ihr Plugin-Projekt und legen Sie es wie gewohnt in `/<your-project>/Assets/Plugins/Android` ab. Fügen Sie keinen Braze-Quellcode in Ihre Bibliothek oder Ihr Plugin ein, da dieser bereits in `/<your-project>/Assets/Plugins/Android` vorhanden ist.
4. Bearbeiten Sie Ihre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml`, um Ihre Unterklasse `BrazeUnityPlayerActivity` als Hauptaktivität anzugeben.

Sie sollten nun in der Lage sein, eine `.apk` aus der Unity IDE zu verpacken, die vollständig in Braze integriert ist und Ihre angepasste `UnityPlayerActivity`-Funktionalität enthält.

## iOS SDK vorgebrachte Implementierungsoptionen {#ios-sdk-advanced}

### Enablement der ausführlichen Protokollierung im Unity-Editor
Um die ausführliche Protokollierung im Unity-Editor zu aktivieren, gehen Sie wie folgt vor:

1. Öffnen Sie die Einstellungen für die Braze-Konfiguration, indem Sie zu **Braze** > **Braze-Konfiguration** navigieren.
2. Klicken Sie auf das Dropdown-Menü **Braze iOS-Einstellungen anzeigen**.
3. Geben Sie im Feld **SDK Log Level** den Wert "0" ein.

### Erweitern des SDK (iOS)

Um das Verhalten des SDK zu erweitern, forken Sie das [Braze Unity SDK GitHub Projekt](https://github.com/appboy/appboy-unity-sdk) und nehmen Sie die gewünschten Änderungen vor.

Um Ihren modifizierten Code als Unity-Paket zu veröffentlichen, lesen Sie unsere [erweiterten Anwendungsfälle]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/).

### Der Übergang von manueller zu automatisierter Integration (iOS)

Um die Vorteile der automatisierten iOS-Integration zu nutzen, die das Braze Unity SDK bietet, befolgen Sie diese Schritte für den Übergang von einer manuellen zu einer automatisierten Integration.

1. Entfernen Sie den gesamten Braze-bezogenen Code aus der Unterklasse `UnityAppController` Ihres Xcode-Projekts.
2. Entfernen Sie die iOS-Bibliotheken von Braze aus Ihrem Unity- oder Xcode-Projekt (z. B. `Appboy_iOS_SDK.framework` und `SDWebImage.framework`) und [importieren Sie das Braze Unity-Paket](#step-1-importing-the-braze-unity-package) in Ihr Unity-Projekt.
3. Folgen Sie den Anweisungen zur Integration, um [Ihren API-Schlüssel über Unity festzulegen](#step-2-setting-your-api-key).

