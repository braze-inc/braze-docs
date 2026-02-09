---
nav_title: Registre eventos personalizados
article_title: Registre eventos personalizados por meio do SDK do Braze
page_order: 3.1
description: "Saiba como registrar eventos personalizados por meio do SDK do Braze."

---

# Registre eventos personalizados

> Saiba como registrar eventos personalizados por meio do SDK do Braze.

{% alert note %}
Para SDKs de wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Registro de um evento personalizado

Para registrar um evento personalizado, use o seguinte método de registro de eventos.

{% tabs %}
{% tab web %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Se, em vez disso, você quiser usar o Google Tag Manager, poderá usar o tipo de tag **Custom Event** para chamar o [método`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) e enviar eventos personalizados para o Braze, incluindo opcionalmente propriedades de eventos personalizados. Para isso:

1. Digite o **nome do evento** usando uma variável ou digitando um nome de evento.
2. Use o botão **Adicionar linha** para adicionar propriedades de eventos.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tag type" (evento personalizado), "event name" (nome do evento) (clique no botão) e "event properties" (propriedades do evento).]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Para o Android nativo, você pode usar o seguinte método:

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

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillion %}
Se tiver integrado o [Infillion Beacons](https://infillion.com/software/beacons/) ao seu aplicativo Android, você poderá usar opcionalmente o `visit.getPlace()` para registrar eventos específicos do local. O `requestImmediateDataFlush` verifica se o evento será registrado mesmo que o app esteja em segundo plano.

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

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Adição de propriedades de metadados

Ao registrar um evento personalizado, você tem a opção de adicionar metadados sobre esse evento personalizado passando um objeto de propriedades com o evento. As propriedades são definidas como pares de valores-chave. As chaves são strings e os valores podem ser `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objetos, vetores de objetos ou objetos JSON aninhados.

Para adicionar propriedades de metadados, use o seguinte método de registro de eventos.

{% tabs %}
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

{% tab android %}
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

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
As chaves `time` e `event_name` são reservadas e não podem ser usadas como propriedades de eventos personalizados.
{% endalert %}

## Melhores práticas

Há três verificações importantes a serem realizadas para que as propriedades do seu evento personalizado registrem o que é esperado:

* [Estabeleça quais eventos são registrados](#verify-events)
* [Verifique o registro](#verify-log)
* [Verifique os valores](#verify-values)

Várias propriedades podem ser registradas cada vez que um evento personalizado é registrado.

### Verificar eventos

Verifique com seus desenvolvedores quais propriedades de eventos estão sendo rastreadas. Lembre-se de que todas as propriedades do evento diferenciam maiúsculas de minúsculas. Para obter informações adicionais sobre rastreamento de eventos personalizados, confira estes artigos com base na sua plataforma:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Verificar registro

Para confirmar que as propriedades do evento são rastreadas com sucesso, você pode visualizar todas as propriedades do evento na página de **Eventos Personalizados**.

1. Acessar **Configurações de Dados** > **Eventos Personalizados**.
2. Localize seu evento personalizado na lista.
3. Para seu evento, selecione **Manage Properties (Gerenciar propriedades** ) para visualizar os nomes das propriedades associadas a um evento.

### Verifique os valores

Depois de [adicionar seu usuário como um usuário teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), siga estas etapas para verificar seus valores: 

1. Execute o evento personalizado dentro do app.
2. Aguarde cerca de 10 segundos para que os dados sejam liberados.
3. Atualize o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) para ver o evento personalizado e o valor da propriedade do evento que foi passado com ele.
