---
nav_title: Aviso personalizado de revisión de la App Store
article_title: Aviso personalizado de revisión de la App Store
platform: iOS
page_order: 4
description: "Este artículo de referencia muestra cómo configurar un aviso de revisión personalizado de la App Store de iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Aviso personalizado de revisión de la App Store

{% alert note %}
Una vez que implementes esta indicación, Braze dejará de hacer un seguimiento automático de las impresiones, y deberás registrar tus propios [análisis]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

Crear una campaña para pedir a los usuarios una reseña de la App Store es un uso popular de los mensajes dentro de la aplicación.

Empieza por configurar el [delegado de mensajes dentro de la](#in-app-message-controller-delegate) aplicación. A continuación, implementa el siguiente método delegado para desactivar el mensaje predeterminado de revisión de la App Store:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage.uri options:@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage.uri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice.discardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

En tu código de gestión de vínculos profundos, añade el siguiente código para procesar el vínculo profundo `{YOUR-APP-SCHEME}:appstore-review`. Ten en cuenta que tendrás que importar `StoreKit` para utilizar `SKStoreReviewController`:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

A continuación, crea una campaña de mensajería dentro de la aplicación con lo siguiente:

- El par clave-valor `"Appstore Review" : "true"`
- El comportamiento al hacer clic configurado a "Vínculo profundo entro de la aplicación", utilizando el vínculo profundo `{YOUR-APP-SCHEME}:appstore-review`.

{% endraw %}

{% alert tip %}
Apple limita las solicitudes de revisión de la App Store a un máximo de tres (3) veces al año por cada usuario, por lo que tu campaña debe [tener una tasa limitada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) a tres veces al año por usuario.<br><br>Los usuarios pueden desactivar los avisos de revisión del App Store. En consecuencia, tu solicitud de revisión personalizada no debe prometer que aparecerá una solicitud de revisión nativa del App Store ni pedir directamente una revisión.
{% endalert %}

