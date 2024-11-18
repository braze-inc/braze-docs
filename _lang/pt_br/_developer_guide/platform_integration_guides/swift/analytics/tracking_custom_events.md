---
nav_title: Rastreamento de Eventos Personalizados
article_title: Rastreamento de Eventos Personalizados para iOS
platform: Swift
page_order: 2
description: "Este artigo de referência relata como adicionar e rastrear eventos personalizados para o SDK SWIFT."

---

# Rastreamento de eventos personalizados

> Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e segmentar seus usuários por suas ações no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Adicionando um evento personalizado

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### Adicionando propriedades

Você pode adicionar metadados sobre eventos personalizados passando um `Dictionary` preenchido com `Int`, `Double`, `String`, `Bool` ou `Date` valores.

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab OBJECTIVE C %}

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

{% endtab %}
{% endtabs %}

### Chaves reservadas {#event-reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de evento personalizado:

- `time`
- `event_name`

## Recursos adicionais

- Consulte a [`logCustomEvent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "documentação de logcustomevent") para saber mais.

