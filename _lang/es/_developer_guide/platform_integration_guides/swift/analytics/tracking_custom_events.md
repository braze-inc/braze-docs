---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para iOS
platform: Swift
page_order: 2
description: "Este artículo de referencia explica cómo añadir y seguir eventos personalizados para el SDK de Swift."

---

# Seguimiento de eventos personalizados

> Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Añadir un evento personalizado

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### Añadir propiedades

Puedes añadir metadatos sobre eventos personalizados pasando un `Dictionary` rellenado con los valores `Int`, `Double`, `String`, `Bool`, o `Date`.

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
{% tab OBJETIVO-C %}

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

### Claves reservadas {#event-reserved-keys}

Las siguientes claves están reservadas y no pueden utilizarse como propiedades del evento personalizado:

- `time`
- `event_name`

## Recursos adicionales

- Consulta la documentación [`logCustomEvent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "documentación de logcustomevent") para obtener más información.

