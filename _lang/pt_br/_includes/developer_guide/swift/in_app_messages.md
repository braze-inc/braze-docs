{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará ativar as mensagens no app.

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Ativação de mensagens no app

### Etapa 1: Criar uma implementação de `BrazeInAppMessagePresenter`

Para permitir que o Braze exiba mensagens no app, crie uma implementação do protocolo `BrazeInAppMessagePresenter` e atribua-o ao `inAppMessagePresenter` opcional em sua instância do Braze. Você também pode usar o apresentador padrão do Braze UI instanciando um objeto `BrazeInAppMessageUI`.

Será necessário importar a biblioteca `BrazeUI` para acessar a classe `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### Etapa 2: Manusear gatilhos não correspondentes

Implementar [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) na classe `BrazeDelegate` relevante. Quando o Braze não conseguir encontrar um disparador correspondente para um determinado evento, ele chamará esse método automaticamente.
