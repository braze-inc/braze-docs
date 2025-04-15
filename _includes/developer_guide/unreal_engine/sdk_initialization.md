{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Initializing the SDK

If you'd like precise control over when Braze initializes, you can disable `AutoInitialize` in your `DefaultEngine.ini` file. After `AutoInitialize` is disabled, you'll need to manually initialize Braze from native C++ or Blueprint.

{% tabs %}
{% tab C++ %}
In native C++, access the BrazeSubsystem and call `InitializeBraze()` optionally passing it a Config to override Engine.ini settings.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Blueprint %}
In Blueprint, the same functions are accessible as Blueprint nodes:  
Use the `GetBrazeSubsystem` Node to call its `Initialize` node.  
A BrazeConfig object can optionally be created in Blueprint and passed to `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
