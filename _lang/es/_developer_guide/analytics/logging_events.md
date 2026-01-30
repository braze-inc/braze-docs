---
nav_title: Registrar eventos personalizados
article_title: Registra eventos personalizados a través del SDK de Braze
page_order: 3.1
description: "Aprende a registrar eventos personalizados a través del SDK de Braze."

---

# Registrar eventos personalizados

> Aprende a registrar eventos personalizados a través del SDK de Braze.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente.
{% endalert %}

## Registro de un evento personalizado

Para registrar un evento personalizado, utiliza el siguiente método de registro de eventos.

{% tabs %}
{% tab web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si quieres utilizar Google Tag Manager en su lugar, puedes utilizar el tipo de etiqueta **Evento personalizado** para llamar al [método`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) y enviar eventos personalizados a Braze, incluyendo opcionalmente propiedades del evento personalizadas. Para ello:

1. Introduce el **Nombre del Evento** utilizando una variable o escribiendo un nombre de evento.
2. Utiliza el botón **Añadir Fila** para añadir propiedades del evento.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta" (evento personalizado), "nombre del evento" (clic del botón) y "propiedades del evento".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

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

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillion %}
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

## Añadir propiedades de metadatos

Cuando registras un evento personalizado, tienes la opción de añadir metadatos sobre ese evento personalizado pasando un objeto de propiedades con el evento. Las propiedades se definen como pares clave-valor. Las claves son cadenas y los valores pueden ser `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objetos, matrices u objetos JSON anidados.

Para añadir propiedades de metadatos, utiliza el siguiente método de registro de eventos.

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
Las claves `time` y `event_name` están reservadas y no pueden utilizarse como propiedades del evento personalizado.
{% endalert %}

## Buenas prácticas

Hay tres comprobaciones importantes que debes llevar a cabo para que las propiedades del evento personalizado se registren según lo esperado:

* [Establecer qué eventos se registran](#verify-events)
* [Verificar registro](#verify-log)
* [Verificar los valores](#verify-values)

Se pueden registrar varias propiedades cada vez que se registra un evento personalizado.

### Verificar eventos

Comprueba con tus desarrolladores qué propiedades del evento están siendo objeto de seguimiento. Ten en cuenta que todas las propiedades del evento distinguen entre mayúsculas y minúsculas. Para obtener información adicional sobre el seguimiento de eventos personalizados, consulta estos artículos basados en tu plataforma:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Verificar registro

Para confirmar que las propiedades del evento se han seguido correctamente, puedes ver todas las propiedades del evento desde la página **Eventos personalizados**.

1. Vaya a **Configuración de datos** > **Eventos personalizados**.
2. Localiza tu evento personalizado en la lista.
3. Para tu evento, selecciona **Gestionar propiedades** para ver los nombres de las propiedades asociadas a un evento.

### Verificar los valores

Después de [añadir tu usuario como usuario de prueba]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), sigue estos pasos para verificar tus valores: 

1. Realiza el evento personalizado dentro de la aplicación.
2. Espera unos 10 segundos a que se vacíen los datos.
3. Actualiza el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) para ver el evento personalizado y el valor de la propiedad del evento que se pasó con él.
