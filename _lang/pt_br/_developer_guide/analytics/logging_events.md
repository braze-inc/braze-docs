---
nav_title: Registro de Eventos Personalizados
article_title: Registrando eventos personalizados através do SDK Braze
page_order: 3.1
description: "Aprenda como registrar eventos personalizados através do SDK Braze."

---

# Registro de eventos personalizados

> Aprenda como registrar eventos personalizados através do SDK Braze.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Registro de um evento personalizado

Para registrar um evento personalizado, use o seguinte método de registro de eventos.

{% tabs %}
{% tab Android %}
Para Android nativo, você pode usar o seguinte método:

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Se você quiser usar o Google Tag Manager em vez disso, pode usar o tipo de tag **Evento Personalizado** para chamar o [`logCustomEvent` método](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) e enviar eventos personalizados para o Braze, incluindo opcionalmente propriedades de eventos personalizados. Para fazer isso:

1. Digite o **nome do evento** usando uma variável ou digitando um nome de evento.
2. Use o botão **Adicionar linha** para adicionar propriedades de eventos.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (evento personalizado), "event name" (nome do evento) (clique no botão) e "event properties" (propriedades do evento).]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillion %}
Se você integrou [Infillion Beacons](https://infillion.com/software/beacons/) no seu aplicativo Android, você pode opcionalmente usar `visit.getPlace()` para registrar eventos específicos de localização. `requestImmediateDataFlush` verifica se seu evento será registrado mesmo que seu aplicativo esteja em segundo plano.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab unreal engine %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## Adicionando propriedades de metadados

Quando você registra um evento personalizado, você tem a opção de adicionar metadados sobre esse evento personalizado passando um objeto de propriedades com o evento. As propriedades são definidas como pares de valores-chave. As chaves são strings e os valores podem ser objetos `string`, `numeric`, `boolean` ou [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp).

Para adicionar propriedades de metadados, use o seguinte método de registro de eventos.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}

{% tab unreal engine %}
```cpp
TMap<FString, FString> Properties;
Properties.Add(TEXT("you"), TEXT("can"));
Properties.Add(TEXT("pass"), TEXT("false"));
Properties.Add(TEXT("orNumbers"), FString::FromInt(42));
Properties.Add(TEXT("orDates"), FDateTime::Now().ToString());
Properties.Add(TEXT("or"), TEXT("any,array,here")); // Arrays are stored as comma-separated strings
Properties.Add(TEXT("andEven"), TEXT("deeply:nested,json"));

UBraze->LogCustomEventWithProperties(TEXT("YOUR_EVENT_NAME"), Properties);
```
{% endtab %}
{% endtabs %}

{% alert important %}
As chaves `time` e `event_name` são reservadas e não podem ser usadas como propriedades de eventos personalizados.
{% endalert %}
