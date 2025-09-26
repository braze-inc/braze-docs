---
nav_title: Registro de eventos personalizados
article_title: Registro de eventos personalizados a través del SDK de Braze
page_order: 3.1
description: "Aprende a registrar eventos personalizados a través del SDK de Braze."

---

# Registro de eventos personalizados

> Aprende a registrar eventos personalizados a través del SDK de Braze.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente.
{% endalert %}

## Registro de un evento personalizado

Para registrar un evento personalizado, utiliza el siguiente método de registro de eventos.

{% tabs %}
{% tab android %}
Para Android nativo, puedes utilizar el siguiente método:

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

{% tab Web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si quieres utilizar Google Tag Manager en su lugar, puedes utilizar el tipo de etiqueta **Evento personalizado** para llamar al [método`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) y enviar eventos personalizados a Braze, incluyendo opcionalmente propiedades del evento personalizadas. Para ello:

1. Introduce el **Nombre del Evento** utilizando una variable o escribiendo un nombre de evento.
2. Utiliza el botón **Añadir Fila** para añadir propiedades del evento.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta" (evento personalizado), "nombre del evento" (clic del botón) y "propiedades del evento".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab Flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillón %}
Si has integrado [Infillion Beacons](https://infillion.com/software/beacons/) en tu aplicación Android, puedes utilizar opcionalmente `visit.getPlace()` para registrar eventos específicos de ubicación. `requestImmediateDataFlush` verifica que tu evento se registrará incluso si tu aplicación está en segundo plano.

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

{% tab nativo de react %}
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

{% tab motor unreal engine %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## Añadir propiedades de metadatos

Cuando registras un evento personalizado, tienes la opción de añadir metadatos sobre ese evento personalizado pasando un objeto de propiedades con el evento. Las propiedades se definen como pares clave-valor. Las claves son cadenas y los valores pueden ser `string`, `numeric`, `boolean`, u [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objetos.

Para añadir propiedades de metadatos, utiliza el siguiente método de registro de eventos.

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

{% tab Web %}
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

{% tab Flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab nativo de react %}
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

{% tab motor unreal engine %}
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
Las claves `time` y `event_name` están reservadas y no pueden utilizarse como propiedades del evento personalizado.
{% endalert %}
