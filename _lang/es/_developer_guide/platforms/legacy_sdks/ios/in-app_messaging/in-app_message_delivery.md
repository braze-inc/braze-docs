---
nav_title: Entrega de mensajes dentro de la aplicación
article_title: Entrega de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia trata sobre la entrega de mensajes dentro de la aplicación de iOS, enumerando los distintos tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Entrega de mensajes dentro de la aplicación

## Tipos de desencadenantes

Nuestro producto de mensajes dentro de la aplicación te permite desencadenar la visualización de mensajes dentro de la aplicación como resultado de varios tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Además, los desencadenantes `Specific Purchase` y `Custom Event` contienen filtros de propiedades sólidos.

{% alert note %}
Los mensajes desencadenados dentro de la aplicación sólo funcionan con eventos personalizados registrados a través del SDK de Braze. Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API o por eventos de la API (como eventos de compra). Si trabajas con iOS, visita nuestro artículo sobre [seguimiento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift) para obtener más información.
{% endalert %}

## Semántica de la entrega

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan al dispositivo del usuario al inicio de la sesión. Si un evento desencadena dos mensajes dentro de la aplicación, se mostrará el mensaje con mayor prioridad. Para más información sobre la semántica de inicio de sesión del SDK, lee sobre nuestro [ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle). Tras la entrega, el SDK precargará los activos para que estén disponibles inmediatamente en el momento del desencadenamiento, minimizando la latencia de visualización.

Cuando un evento desencadenante tiene asociado más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje dentro de la aplicación con la prioridad más alta.

Puede haber cierta latencia en los mensajes dentro de la aplicación que se muestran inmediatamente después de la entrega (inicio de sesión, clic push) debido a que los activos no se han precargado.

## Intervalo de tiempo mínimo entre desencadenamientos

De forma predeterminada, limitamos la tasa de mensajes dentro de la aplicación a una vez cada 30 segundos para facilitar una experiencia de usuario de calidad.

Puedes anular este valor a través de `ABKMinimumTriggerTimeIntervalKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece en `ABKMinimumTriggerTimeIntervalKey` el valor entero que desees como tiempo mínimo en segundos entre mensajes dentro de la aplicación:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## No se encuentra un desencadenante adecuado

Cuando Braze no encuentre un desencadenante que coincida con un evento determinado, llamará al método [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) del método [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html). Implementa este método en tu clase adoptando el protocolo de delegado para manejar este escenario. 

## Entrega local de mensajes dentro de la aplicación

### La pila de mensajes dentro de la aplicación

#### Mostrar mensajes dentro de la aplicación

Cuando un usuario sea elegible para recibir un mensaje dentro de la aplicación, se ofrecerá a `ABKInAppMessageController` el último mensaje dentro de la aplicación de la pila de mensajes dentro de la aplicación. La pila solo conserva los mensajes dentro de la aplicación almacenados en la memoria y se borra entre los lanzamientos de la aplicación desde el modo suspendido.

{% alert important %}
No muestres mensajes dentro de la aplicación cuando el teclado se muestra en pantalla, ya que la representación no está definida en esta circunstancia.
{% endalert %}

#### Añadir mensajes dentro de la aplicación a la pila

Los usuarios son elegibles para recibir un mensaje dentro de la aplicación en las siguientes situaciones:

- Se dispara un evento desencadenador de mensajes dentro de la aplicación
- Evento de inicio de sesión
- La aplicación se abre desde una notificación push

Los mensajes desencadenados dentro de la aplicación se colocan en la pila cuando se dispara su evento desencadenante. Si hay varios mensajes dentro de la aplicación en la pila y esperando a ser mostrados, Braze mostrará primero el mensaje dentro de la aplicación recibido más recientemente (último en entrar, primero en salir).

#### Devolver mensajes dentro de la aplicación a la pila

Un mensaje dentro de la aplicación desencadenado puede volver al stack en las siguientes situaciones:

- El mensaje dentro de la aplicación se desencadena cuando la aplicación está en segundo plano.
- Actualmente hay visible otro mensaje dentro de la aplicación.
- No se ha implementado el [método delegado de interfaz de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` obsoleto, y se está mostrando el teclado.
- El [método delegado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` o el [método delegado de interfaz de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` devuelven `ABKDisplayInAppMessageLater`.

#### Descartar mensajes dentro de la aplicación

Un mensaje dentro de la aplicación desencadenado se descartará en las siguientes situaciones:

- El [método delegado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` o el [método delegado de interfaz de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` devuelven `ABKDiscardInAppMessage`.
- No se ha podido descargar el activo (imagen o archivo ZIP) del mensaje dentro de la aplicación.
- El mensaje dentro de la aplicación está listo para mostrarse, pero ya ha pasado el tiempo de espera.
- La orientación del dispositivo no coincide con la orientación del mensaje dentro de la aplicación desencadenado.
- El mensaje dentro de la aplicación es un mensaje completo dentro de la aplicación, pero no tiene imagen.
- El mensaje dentro de la aplicación es un mensaje modal dentro de la aplicación sólo con imagen, pero no tiene imagen.

#### Cola manualmente la visualización de mensajes dentro de la aplicación

Si quieres mostrar un mensaje dentro de la aplicación en otro momento, puedes mostrar manualmente el mensaje más alto de la pila llamando al método siguiente:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Creación y visualización de mensajes dentro de la aplicación en tiempo real

Los mensajes dentro de la aplicación también pueden crearse localmente dentro de la aplicación y mostrarse a través de Braze. Esto es especialmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real. Braze no admite análisis de mensajes dentro de la aplicación creados localmente.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

