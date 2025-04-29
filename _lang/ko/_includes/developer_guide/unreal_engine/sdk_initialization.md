{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## SDK 초기화하기

Braze 초기화 시점을 정밀하게 제어하고 싶다면 `DefaultEngine.ini` 파일에서 `AutoInitialize` 을 비활성화하면 됩니다. `AutoInitialize` 을 비활성화한 후에는 네이티브 C++ 또는 블루프린트에서 Braze를 수동으로 초기화해야 합니다.

{% tabs %}
{% tab C++ %}
네이티브 C++에서는 BrazeSubsystem에 액세스하여 `InitializeBraze()` 를 호출하고 선택적으로 Engine.ini 설정을 재정의하는 컨피규어를 전달합니다.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab 블루프린트 %}
블루프린트에서는 블루프린트 노드와 동일한 기능에 액세스할 수 있습니다:  
`GetBrazeSubsystem` 노드를 사용하여 `Initialize` 노드를 호출합니다.  
선택적으로 블루프린트에서 BrazeConfig 오브젝트를 생성하여 다음 주소로 전달할 수 있습니다. `Initialize`

![초기화브레이즈]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
