# Beispiel-Apps

> Die Braze SDKs werden jeweils mit einer Beispielanwendung im Repository geliefert. Jede dieser Apps ist vollständig bearbeitbar, sodass Sie die Features von Braze testen und gleichzeitig in Ihre eigenen Anwendungen implementieren können. 

Das Testen des Verhaltens Ihrer eigenen Anwendung im Vergleich zum erwarteten Verhalten und zu den Codepfaden in den Beispielanwendungen ist eine hervorragende Möglichkeit zur Fehlersuche bei Problemen.

## Erstellung der Droidboy Testanwendung
Unsere Testanwendung im [Android SDK GitHub Repository](https://github.com/braze-inc/braze-android-sdk) heißt Droidboy. Folgen Sie diesen Anweisungen, um eine voll funktionsfähige Kopie davon zusammen mit Ihrem Projekt zu erstellen.

1. Erstellen Sie einen neuen [Arbeitsbereich]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) und notieren Sie sich den Braze-API-Kennungsschlüssel.<br><br>
2. Kopieren Sie Ihre FCM-Absender-ID und Ihren Braze-API-Kennungsschlüssel an die entsprechenden Stellen in `/droidboy/res/values/braze.xml` (zwischen den Tags für die Strings mit den Namen `com_braze_push_fcm_sender_id` bzw. `com_braze_api_key`).<br><br>
3. Kopieren Sie Ihren FCM-Serverschlüssel und Ihre Server-ID in die Einstellungen Ihres Arbeitsbereichs unter **Einstellungen verwalten**.<br><br>
4. Führen Sie zum Assemblieren der Droidboy APK `./gradlew assemble` im SDK-Verzeichnis aus. Verwenden Sie `gradlew.bat` unter Windows.<br><br>
5. Führen Sie für die automatische Installation der Droidboy APK auf einem Testgerät `./gradlew installDebug` im SDK-Verzeichnis aus:

## Erstellung der Hello Braze Testanwendung
Die Testanwendung "Hello Braze" beschränkt sich auf einen minimalen Anwendungsfall des Braze SDK und demonstriert außerdem, wie Sie das Braze SDK auf einfache Weise in ein Gradle-Projekt integrieren können.

1. Kopieren Sie Ihren API-Kennungsschlüssel von der Seite **Einstellungen verwalten** in Ihre Datei `braze.xml` im Ordner `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Um die Beispiel-App auf einem Gerät oder Emulator zu installieren, führen Sie den folgenden Befehl im SDK-Verzeichnis aus:
```
./gradlew installDebug
```
Wenn Sie die Variable `ANDROID_HOME` nicht richtig gesetzt haben oder keinen `local.properties` Ordner mit einem gültigen `sdk.dir` Ordner haben, wird dieses Plugin auch das Basis-SDK für Sie installieren. Weitere Informationen finden Sie im [Plugin-Repository](https://github.com/JakeWharton/sdk-manager-plugin).

Weitere Informationen zum Build-System des Android SDK finden Sie unter[GitHub Repository README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).

