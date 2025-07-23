{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Inicialização do SDK

Se desejar ter controle preciso sobre quando o Braze inicializa, é possível desativar o `AutoInitialize` no arquivo `DefaultEngine.ini`. Depois que o `AutoInitialize` for desativado, você precisará inicializar manualmente o Braze a partir do C++ nativo ou do Blueprint.

{% tabs %}
{% tab C++ %}
Em C++ nativo, acesse o BrazeSubsystem e chame `InitializeBraze()` passando a ele, opcionalmente, um Config para substituir as configurações de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Projeto %}
No Blueprint, as mesmas funções podem ser acessadas como nós do Blueprint:  
Use o nó `GetBrazeSubsystem` para chamar seu nó `Initialize`.  
Um objeto BrazeConfig pode ser criado opcionalmente no Blueprint e passado para `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
