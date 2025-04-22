{% multi_lang_include developer_ %}

## Initialisierung des SDK

Wenn Sie genau kontrollieren möchten, wann Braze initialisiert wird, können Sie `AutoInitialize` in Ihrer `DefaultEngine.ini` Datei deaktivieren. Nachdem `AutoInitialize` deaktiviert wurde, müssen Sie Braze manuell über C++ oder Blueprint initialisieren.

{% tabs %}
{% tab C++ %}
In nativem C++ greifen Sie auf das BrazeSubsystem zu und rufen `InitializeBraze()` auf, wobei Sie optional eine Config übergeben, um die Einstellungen von Engine.ini außer Kraft zu setzen.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Blaupause %}
In Blueprint sind dieselben Funktionen als Blueprint-Knoten zugänglich:  
Verwenden Sie den `GetBrazeSubsystem` Knoten, um seinen `Initialize` Knoten aufzurufen.  
Ein BrazeConfig-Objekt kann optional in Blueprint erstellt und an `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
