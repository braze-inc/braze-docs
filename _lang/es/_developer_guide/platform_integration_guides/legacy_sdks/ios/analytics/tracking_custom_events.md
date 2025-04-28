---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para iOS
platform: iOS
page_order: 2
description: "Este artículo de referencia explica cómo añadir y seguir eventos personalizados para tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Seguimiento de eventos personalizados para iOS

Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Añadir un evento personalizado

{% tabs %}
{% tab OBJETIVO-C %}

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

### Añadir propiedades

Puedes añadir metadatos sobre eventos personalizados pasando un `NSDictionary` rellenado con los valores `NSNumber`, `NSString` o `NSDate`.

{% tabs %}
{% tab OBJETIVO-C %}

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

Consulta la [documentación de nuestra clase](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 " logcustomevent:withproperties") para obtener más información.

### Claves reservadas {#event-reserved-keys}

Las siguientes claves están reservadas y no pueden utilizarse como propiedades del evento personalizado:

- `time`
- `event_name`

## Recursos adicionales

- Consulta la declaración del método en el [archivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`. 
- Consulta la documentación [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "documentación de logcustomevent") para obtener más información.

