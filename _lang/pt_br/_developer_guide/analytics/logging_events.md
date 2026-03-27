---
nav_title: Registre eventos personalizados
article_title: Registre eventos personalizados através do SDK Braze
page_order: 3.1
description: "Aprenda como registrar eventos personalizados através do SDK Braze."

---

# Registre eventos personalizados

> Aprenda como registrar eventos personalizados através do SDK Braze.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Registro de um evento personalizado

Para registrar um evento personalizado, use o seguinte método de registro de eventos.

{% tabs %}
{% tab web %}
Para uma implementação padrão do SDK Web, você pode usar o seguinte método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Se você preferir usar o Google Tag Manager, pode usar o tipo de tag **Evento Personalizado** para chamar o método [`logCustomEvent` método](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) e enviar eventos personalizados para o Braze, incluindo opcionalmente propriedades de eventos personalizados. Para fazer isso:

1. Digite o **nome do evento** usando uma variável ou digitando um nome de evento.
2. Use o botão **Adicionar linha** para adicionar propriedades de eventos.

![Uma caixa de diálogo mostrando as definições de configuração da tag de ação do Braze. As configurações incluídas são "tipo de tag" (evento personalizado), "nome do evento" (clique no botão) e "propriedades do evento".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
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

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Use o método do plugin Braze Cordova:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

A `logCustomEvent` API aceita:
- `eventName` (string obrigatória): Use até 255 caracteres. Não comece o nome com `$`. Use caracteres alfanuméricos e pontuação.
- `eventProperties` (objeto opcional): Adicione pares chave-valor para metadados do evento. Use chaves de até 255 caracteres e não comece as chaves com `$`.

Para valores de propriedade, use `string` (até 255 caracteres), `numeric`, `boolean`, arrays ou objetos JSON aninhados.

Para detalhes de implementação, veja a fonte do SDK Braze Cordova:
- [`www/BrazePlugin.js` `logCustomEvent` método (linhas 138-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [`www/BrazePlugin.js` JSDoc (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Manipulador Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Manipulador iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [Declaração de método iOS em `src/ios/BrazePlugin.h` (linha 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Se você integrou [Infillion Beacons](https://infillion.com/software/beacons/) em seu app Android, você pode opcionalmente usar `visit.getPlace()` para registrar eventos específicos de localização. `requestImmediateDataFlush` verifica se seu evento será registrado mesmo que seu app esteja em segundo plano.

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

## Adicionando propriedades de metadados

Quando você registra um evento personalizado, você tem a opção de adicionar metadados sobre esse evento personalizado passando um objeto de propriedades com o evento. As propriedades são definidas como pares de valores-chave. As chaves são strings e os valores podem ser `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objetos, arrays ou objetos JSON aninhados.

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

{% tab cordova %}
Registre eventos personalizados com um objeto de propriedades:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

Você também pode passar propriedades inline:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

O app de exemplo oficial do Cordova inclui propriedades de string, numéricas, booleanas, array e objetos aninhados:
- [`sample-project/www/js/index.js` (linhas 230-251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Trecho do projeto de exemplo:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

Para detalhes da API e da ponte nativa, veja:
- [`www/BrazePlugin.js` JSDoc (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Manipulador Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Manipulador iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
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

Existem três verificações importantes a serem realizadas para que as propriedades do seu evento personalizado sejam registradas conforme o esperado:

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
3. Para seu evento, selecione **Gerenciar Propriedades** para visualizar os nomes das propriedades associadas a um evento.

### Verifique os valores

Após [adicionar seu usuário como um usuário teste]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), siga estas etapas para verificar seus valores: 

1. Execute o evento personalizado dentro do app.
2. Aguarde cerca de 10 segundos para que os dados sejam liberados.
3. Atualize o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) para ver o evento personalizado e o valor da propriedade do evento que foi passado com ele.
