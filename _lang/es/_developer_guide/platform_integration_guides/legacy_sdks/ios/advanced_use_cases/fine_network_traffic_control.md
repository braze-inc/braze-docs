---
nav_title: Control fino del tráfico en la red
article_title: Control fino del tráfico de red para iOS
platform: iOS
page_order: 1
description: "Este artículo trata sobre la implementación de un buen control del tráfico de red para tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Control fino del tráfico en la red

## Políticas de tramitación de solicitudes

Braze permite al usuario la opción de controlar el tráfico de red utilizando los siguientes protocolos:

### Procesamiento automático de solicitudes

***Valor de enumeración de `ABKRequestProcessingPolicy`: `ABKAutomaticRequestProcessing`***

- Este es el valor **predeterminado de la política de peticiones**.
- El SDK de Braze gestionará automáticamente toda la comunicación con el servidor, que incluye lo siguiente:
    - Transmisión de datos de eventos y atributos personalizados a servidores Braze
    - Actualización de tarjetas de contenido y geovallas
    - Solicitar nuevos mensajes dentro de la aplicación
- Las solicitudes inmediatas al servidor se realizan cuando se necesitan datos orientados al usuario para las características de Braze, como los mensajes dentro de la aplicación.
- Para minimizar la carga del servidor, Braze realiza descargas periódicas de nuevos datos de usuario cada pocos segundos.

Los datos pueden vaciarse manualmente en los servidores de Braze en cualquier momento utilizando el siguiente método:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### Tramitación manual de solicitudes

***Valor de enumeración de `ABKRequestProcessingPolicy`: `ABKManualRequestProcessing`***

- Este protocolo es igual que el procesamiento automático de solicitudes, excepto que:
    - Los atributos personalizados y los datos de eventos personalizados no se envían automáticamente al servidor durante toda la sesión de usuario.
- Braze seguirá realizando solicitudes de red automáticas para características internas, como la solicitud de mensajes dentro de la aplicación, la plantilla Liquid en los mensajes dentro de la aplicación, las geovallas y el seguimiento de ubicación. Para más detalles, consulta la declaración `ABKRequestProcessingPolicy` en [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h). Cuando se realizan estas solicitudes internas, los atributos personalizados almacenados localmente y los datos de eventos personalizados pueden enviarse al servidor Braze, dependiendo del tipo de solicitud.

Los datos pueden vaciarse manualmente en los servidores de Braze en cualquier momento utilizando el siguiente método:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## Configuración de la política de procesamiento de solicitudes

### Establecer la política de solicitudes al inicio

Estas políticas pueden establecerse al iniciar la aplicación mediante el método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, configura `ABKRequestProcessingPolicyOptionKey` como se muestra en el siguiente fragmento de código:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Establecer la política de peticiones en tiempo de ejecución

La política de procesamiento de solicitudes también puede establecerse durante el tiempo de ejecución a través de la propiedad `requestProcessingPolicy` en `Appboy`:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Desconexión manual de la comunicación con el servidor en vuelo

Si en algún momento hay que interrumpir una comunicación "en vuelo" con un servidor, debes llamar al método siguiente:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

Después de llamar a este método, debes restablecer el modo de procesamiento de solicitudes a automático. Por esta razón, sólo recomendamos llamarlo si el SO te obliga a detener tareas en segundo plano o algo similar.

