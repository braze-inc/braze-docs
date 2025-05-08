---
nav_title: Ejemplo - Mensaje de revisión de la App Store
article_title: Ejemplo - Mensaje de revisión de la App Store
platform: Swift
page_order: 8
description: "Este artículo de referencia proporciona un ejemplo para iOS de un mensaje dentro de la aplicación personalizado para pedir a los usuarios que hagan una valoración de tu aplicación."
channel:
  - in-app messages

---

# Ejemplo - Solicitud de revisión de la App Store

{% alert note %}
Dado que este aviso de ejemplo anula el comportamiento predeterminado de Braze, no podemos realizar un seguimiento automático de las impresiones si se implementa. Debes registrar tus propios [análisis]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

> Crear una campaña para pedir a los usuarios una reseña de la App Store es un uso popular de los mensajes dentro de la aplicación. Este ejemplo te guía a través de la creación de un mensaje dentro de la aplicación personalizado que pide a los usuarios que revisen tu aplicación.

## Paso 1: Configura el delegado de mensajes dentro de la aplicación
En primer lugar, configura el [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/) en tu aplicación. 

## Paso 2: Desactiva el mensaje predeterminado de revisión de la App Store
A continuación, implementa el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para desactivar el mensaje predeterminado de revisión de la App Store.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

## Paso 3: Crear un vínculo profundo
En tu código de gestión de vínculos profundos, añade el siguiente código para procesar el vínculo profundo `{YOUR-APP-SCHEME}:app-store-review`. Ten en cuenta que tendrás que importar `StoreKit` para utilizar `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

## Paso 4: Establece un comportamiento personalizado al hacer clic

A continuación, crea una campaña de mensajería dentro de la aplicación con lo siguiente:

- El par clave-valor `"AppStore Review" : "true"`
- El comportamiento al hacer clic configurado a "Vínculo profundo entro de la aplicación", utilizando el vínculo profundo `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limita las solicitudes de revisión de la App Store a un máximo de tres veces al año por cada usuario, por lo que tu campaña debe [tener una tasa limitada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) a tres veces al año por usuario.<br><br>Los usuarios pueden desactivar los avisos de revisión del App Store. En consecuencia, tu solicitud de revisión personalizada no debe prometer que aparecerá una solicitud de revisión nativa del App Store ni pedir directamente una revisión.
{% endalert %}

