{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Initialisation du SDK

Si vous souhaitez contrôler précisément le moment où Braze s'initialise, vous pouvez désactiver `AutoInitialize` dans votre fichier `DefaultEngine.ini`. Une fois `AutoInitialize` désactivé, vous devrez initialiser Braze manuellement à partir de C++ natif ou de Blueprint.

{% tabs %}
{% tab C++ %}
En C++ natif, accédez au BrazeSubsystem et appelez `InitializeBraze()` en lui transmettant éventuellement un Config pour remplacer les paramètres de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Plan d'action %}
Dans Blueprint, les mêmes fonctions sont accessibles en tant que nœuds Blueprint :  
Utilisez le nœud `GetBrazeSubsystem` pour appeler son nœud `Initialize`.  
Un objet BrazeConfig peut éventuellement être créé dans Blueprint et transmis à `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
