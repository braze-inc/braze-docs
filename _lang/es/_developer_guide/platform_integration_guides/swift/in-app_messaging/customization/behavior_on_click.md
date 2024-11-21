---
nav_title: Comportamiento personalizado al hacer clic
article_title: Personalizar el comportamiento de los clics en los mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 5
description: "Este artículo de referencia trata sobre el comportamiento personalizado de la mensajería dentro de la aplicación de iOS al hacer clic para el SDK Swift."
channel:
  - in-app messages
---

# Comportamiento personalizado al hacer clic

> Cada objeto `Braze.InAppMessage` contiene un [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), que define el comportamiento al hacer clic. 

Para personalizar este comportamiento, puedes modificar la propiedad `clickAction` consultando el siguiente ejemplo:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}

El método `inAppMessage(_:prepareWith:)` no está disponible en Objective-C.

{% endtab %}
{% endtabs %}

## Tipos de acción clic

La propiedad `clickAction` de tu `Braze.InAppMessage` está predeterminada a `.none`, pero puede ajustarse a uno de los siguientes valores:

| `ClickAction` | Comportamiento al hacer clic |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Abre la URL dada en un navegador externo. Si `useWebView` está configurado en `true`, se abrirá en una vista Web. |
| `.newsFeed` | El canal de noticias se mostrará cuando se haga clic en el mensaje, y este se descartará.<br><br>**Nota:** El canal de noticias está en desuso. Consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) para más detalles. |
| `.none` | Al hacer clic en el mensaje, éste se cerrará. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Para los mensajes dentro de la aplicación que contengan botones, el mensaje `clickAction` también se incluirá en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

## Personaliza los mensajes dentro de la aplicación y los clics en los botones

Se llama el siguiente método delegado [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) cuando se hace clic en un mensaje dentro de la aplicación. Para los clics en los botones de mensajes dentro de la aplicación y en los botones de mensajes HTML dentro de la aplicación (enlaces), se proporciona un ID de botón como parámetro opcional.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Este método devuelve un valor booleano para indicar si Braze debe seguir ejecutando la acción de clic.

