---
nav_title: Referenzen &amp; Beispiel-Apps
article_title: "Braze SDK Referenzen, Repositories und Beispiel-Apps"
page_order: 5.5
description: "Dies ist eine Liste der referenzierten Dokumentationen, GitHub-Repositories und Beispiel-Apps, die zu jedem Braze SDK gehören."
toc_headers: h2
---

# Referenzen, Repositories und Beispiel-Apps

> Dies ist eine Liste der referenzierten Dokumentationen, GitHub-Repositories und Beispiel-Apps, die zu jedem Braze SDK gehören. In der referenzierenden Dokumentation eines SDKs finden Sie die verfügbaren Klassen, Typen, Funktionen und Variablen. Das GitHub-Repository bietet Insights zu den Funktions- und Attribut-Deklarationen, Code-Änderungen und der Versionierung des SDKs. Jedes Repository enthält außerdem vollständig kompilierbare Beispielanwendungen, mit denen Sie die Features von Braze testen oder neben Ihren eigenen Anwendungen implementieren können.

## Liste der Ressourcen

{% alert note %}
Derzeit haben einige SDKs keine spezielle referenzierte Dokumentation - aber wir arbeiten aktiv daran.
{% endalert %}

| Plattform          | Referenzieren                                                                                                                                    | Repository                                                                 | Beispiel-App                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [Dokumentation referenzieren](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHub-Repository](https://github.com/braze-inc/braze-android-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [Dokumentation referenzieren](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHub-Repository](https://github.com/braze-inc/braze-swift-sdk)            | [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [Dokumentation referenzieren](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHub-Repository](https://github.com/braze-inc/braze-web-sdk)              | [Beispiel-App](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [Deklarationsdatei](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHub-Repository](https://github.com/braze-inc/braze-cordova-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [Dokumentation referenzieren](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHub-Repository](https://github.com/braze-inc/braze-flutter-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Deklarationsdatei](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk) | [Beispiel-App](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | --                                                                                                                                                         | [GitHub-Repository](https://github.com/braze-inc/braze-roku-sdk)            | [Beispiel-App](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [Deklarationsdatei](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHub-Repository](https://github.com/braze-inc/braze-unity-sdk)          | [Beispiel-App](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| Unreal Engine SDK | --                                                                                                                                                         | [GitHub-Repository](https://github.com/braze-inc/braze-unreal-sdk)        | [Beispiel-App](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK       | --                                                                                                                                                         | [GitHub-Repository](https://github.com/braze-inc/braze-xamarin-sdk)      | [Beispiel-App](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Eine App als Beispiel erstellen

{% tabs %}
{% tab android %}
### Gebäude "Droidboy"

Unsere Testanwendung im [Android SDK GitHub Repository](https://github.com/braze-inc/braze-android-sdk) heißt Droidboy. Folgen Sie diesen Anweisungen, um eine voll funktionsfähige Kopie davon zusammen mit Ihrem Projekt zu erstellen.

1. Erstellen Sie einen neuen [Arbeitsbereich]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) und notieren Sie sich den Braze-API-Kennungsschlüssel.<br><br>
2. Kopieren Sie Ihre FCM-Absender-ID und Ihren Braze-API-Kennungsschlüssel an die entsprechenden Stellen in `/droidboy/res/values/braze.xml` (zwischen den Tags für die Strings mit den Namen `com_braze_push_fcm_sender_id` bzw. `com_braze_api_key`).<br><br>
3. Kopieren Sie Ihren FCM-Serverschlüssel und Ihre Server-ID in die Einstellungen Ihres Arbeitsbereichs unter **Einstellungen verwalten**.<br><br>
4. Führen Sie zum Assemblieren der Droidboy APK `./gradlew assemble` im SDK-Verzeichnis aus. Verwenden Sie `gradlew.bat` unter Windows.<br><br>
5. Führen Sie für die automatische Installation der Droidboy APK auf einem Testgerät `./gradlew installDebug` im SDK-Verzeichnis aus:

### Gebäude "Hallo Braze"

Die Testanwendung "Hello Braze" beschränkt sich auf einen minimalen Anwendungsfall des Braze SDK und demonstriert außerdem, wie Sie das Braze SDK auf einfache Weise in ein Gradle-Projekt integrieren können.

1. Kopieren Sie Ihren API-Kennungsschlüssel von der Seite **Einstellungen verwalten** in Ihre Datei `braze.xml` im Ordner `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Um die Beispiel-App auf einem Gerät oder Emulator zu installieren, führen Sie den folgenden Befehl im SDK-Verzeichnis aus:
```
./gradlew installDebug
```
Wenn Sie die Variable `ANDROID_HOME` nicht richtig gesetzt haben oder keinen `local.properties` Ordner mit einem gültigen `sdk.dir` Ordner haben, wird dieses Plugin auch das Basis-SDK für Sie installieren. Weitere Informationen finden Sie im [Plugin-Repository](https://github.com/JakeWharton/sdk-manager-plugin).

Weitere Informationen zum Build-System des Android SDK finden Sie unter[GitHub Repository README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab schnell %}
### Erstellen von Swift-Test-Apps

Folgen Sie diesen Anweisungen, um unsere Testanwendungen zu erstellen und auszuführen.

1. Erstellen Sie einen neuen [Workspace]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) und notieren Sie sich den App-Bezeichner, den API-Schlüssel und den Endpunkt.
2. Wählen Sie auf der Grundlage Ihrer Integrationsmethode (Swift-Paketmanager, CocoaPods, manuell) die entsprechende `xcodeproj`-Datei aus und öffnen Sie sie.
3. Setzen Sie Ihren API-Schlüssel und Ihren Endpunkt in das entsprechende Feld in der Datei `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Verwenden Sie bei der QA Ihrer SDK-Integration den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um Fehlerbehebungen durchzuführen, ohne die ausführliche Protokollierung für Ihre App zu aktivieren.
{% endalert %}
