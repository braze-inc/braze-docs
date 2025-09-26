{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## SDKを初期化する

Brazeが初期化されるタイミングを正確にコントロールしたい場合は、`DefaultEngine.ini` ファイルで`AutoInitialize` を無効にすることができる。`AutoInitialize` を無効にした後は、ネイティブC++またはBlueprintからBrazeを手動で初期化する必要がある。

{% tabs %}
{% tab C++ %}
ネイティブC++でBrazeSubsystemにアクセスし、`InitializeBraze()` を呼び出す。オプションでConfigを渡し、Engine.ini の設定を上書きする。

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab 青写真 %}
ブループリントでは、ブループリント・ノードと同じ機能にアクセスできる：  
`GetBrazeSubsystem` ノードを使って、その`Initialize` ノードを呼び出す。  
オプションで、BrazeConfigオブジェクトをBlueprintで作成し、以下に渡すことができる。 `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}
