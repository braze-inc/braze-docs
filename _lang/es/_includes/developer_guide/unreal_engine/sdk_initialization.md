{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Inicializar el SDK

Si quieres tener un control preciso sobre cuándo se inicializa Braze, puedes desactivar `AutoInitialize` en tu archivo `DefaultEngine.ini`. Después de desactivar `AutoInitialize`, tendrás que inicializar manualmente Braze desde C++ nativo o Blueprint.

{% tabs %}
{% tab C++ %}
En C++ nativo, accede al BrazeSubsystem y llama a `InitializeBraze()` pasándole opcionalmente un Config para anular la configuración de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Plano %}
En Blueprint, las mismas funciones son accesibles como nodos Blueprint:  
Utiliza el nodo `GetBrazeSubsystem` para llamar a su nodo `Initialize`.  
Opcionalmente, se puede crear un objeto BrazeConfig en Blueprint y pasarlo a `Initialize`

![InicializarBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
