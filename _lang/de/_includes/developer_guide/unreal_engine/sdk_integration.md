## Über das Unreal Engine Braze SDK

Mit dem Braze Unreal SDK Plugin können Sie:

* Sitzungen innerhalb Ihrer App oder Ihres Spiels messen und tracken
* Verfolgen Sie In-App-Käufe und benutzerdefinierte Ereignisse
* Benutzerprofile mit Standard- und benutzerdefinierten Attributen aktualisieren
* Push-Benachrichtigungen senden
* Integrieren Sie Ihre Unreal-Anwendungen in größere Canvas-Journeys
* Kanalübergreifendes Messaging wie E-Mails oder SMS auf Basis des In-App-Verhaltens senden.

## Integration des Unreal Engine SDK

### Schritt 1: Fügen Sie das Braze Plugin hinzu

Klonen Sie in Ihrem Terminal das [Unreal Engine Braze SDK GitHub-Repository](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

Kopieren Sie dann das Verzeichnis `BrazeSample/Plugins/Braze` und fügen Sie es in den Plugin-Ordner Ihrer App ein.

### Schritt 2: Aktivieren Sie das Plugin

Aktivieren Sie das Plugin für Ihr C++- oder Blueprint-Projekt.

{% tabs %}
{% tab C++ %}
Für C++-Projekte konfigurieren Sie Ihr Modul so, dass es das Braze-Modul referenziert. Fügen Sie in Ihrem `\*.Build.cs file` `"Braze"` zu Ihrem `PublicDependencyModuleNames` hinzu.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Blaupause %}
Für Blueprint-Projekte gehen Sie zu **Einstellungen** > **Plugins** und markieren Sie neben **Braze** die Option **Enablement**.

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Schritt 3: Legen Sie Ihren API-Schlüssel und Endpunkt fest

Legen Sie Ihren API-Schlüssel und den Endpunkt in Ihrem Projekt fest: `DefaultEngine.ini`.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Für Projekte, die auf Android SDK 31+ zielen, erzeugt Unreal Builds, die bei der Installation auf Android 12+ Geräten mit dem Fehler INSTALL_PARSE_FAILED_MANIFEST_MALFORMED fehlschlagen. Um dies zu beheben, suchen Sie die `UE4_Engine_AndroidSDK_31_Build_Fix.patch` git-Patch-Datei im Stammverzeichnis dieses Repositorys und wenden Sie sie auf Ihren Unreal-Quellcode-Build an.
{% endalert %}

## Optionale Konfigurationen

### Protokollieren

{% tabs local %}
{% tab Android %}
Sie können die Protokollstufe zur Laufzeit mit C++ oder in einem Blueprint-Knoten festlegen.

{% subtabs %}
{% subtab C++ %}
Um die Protokollstufe zur Laufzeit einzustellen, rufen Sie `UBrazeSubsystem::AndroidSetLogLevel` auf.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
In Blueprint können Sie den Knoten **Android Set Log Level** verwenden:

![Der Android Set Log Level Knoten im Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Um sicherzustellen, dass die Protokollierung gesetzt ist, wenn das Braze SDK Initialize aufgerufen wird, wird empfohlen, dies vor `InitializeBraze` aufzurufen.
{% endtab %}

{% tab iOS %}
Um die Protokollebene in `info.plist` zu aktivieren, gehen Sie zu **Einstellungen** > **Projekteinstellungen** und wählen Sie dann **iOS** unter **Plattformen**. Suchen Sie unter **Extra PList Data** nach **Additional Plist Data** und geben Sie dann Ihre Protokollstufe ein:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

Der Standard-Protokollierungsgrad ist 8, was einer minimalen Protokollierung entspricht. Lesen Sie mehr über Protokollstufen: [Andere SDK-Anpassungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
