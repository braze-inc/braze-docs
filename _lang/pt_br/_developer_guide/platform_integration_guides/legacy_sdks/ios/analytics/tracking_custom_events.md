---
nav_title: Rastreamento de Eventos Personalizados
article_title: Rastreamento de eventos personalizados para iOS
platform: iOS
page_order: 2
description: "Este artigo de referência aborda como adicionar e rastrear eventos personalizados para seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rastreamento de eventos personalizados para iOS

Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Adicionando um evento personalizado

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Adicionando propriedades

Você pode adicionar metadados sobre eventos personalizados passando um `NSDictionary` preenchido com `NSNumber`, `NSString` ou `NSDate` valores.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
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

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
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

{% endtab %}
{% endtabs %}

Para saber mais, consulte a [documentação de nossa classelogcustomevent](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 ":withproperties").

### Chaves reservadas {#event-reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de evento personalizado:

- `time`
- `event_name`

## Recursos adicionais

- Consulte a declaração do método no [arquivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`. 
- Consulte a [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa " documentação de logcustomevent") para saber mais.

