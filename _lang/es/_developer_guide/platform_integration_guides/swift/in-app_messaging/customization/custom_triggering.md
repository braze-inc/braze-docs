---
nav_title: Desencadenar personalizado
article_title: Personalizar el desencadenamiento de mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 6
description: "Este artículo de referencia trata sobre el desencadenamiento personalizado de la mensajería dentro de la aplicación de iOS para el SDK Swift."
channel:
  - in-app messages
---

# Desencadenado personalizado

> Por defecto, los mensajes dentro de la aplicación se desencadenan por eventos registrados por el SDK. También puedes desencadenar mensajes dentro de la aplicación mediante eventos enviados por el servidor.

Para desencadenar mensajes dentro de la aplicación utilizando eventos del lado del servidor, envía un push silencioso al dispositivo para que éste registre un evento basado en SDK. Este evento SDK puede desencadenar posteriormente el mensaje dentro de la aplicación dirigido al usuario.

## Paso 1: Manejar el push silencioso y los pares clave-valor

Implementa la siguiente función y llámala dentro del [método`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)::

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Cuando se reciba el push silencioso, se registrará un evento "desencadenado de mensaje dentro de la aplicación" registrado en el SDK contra el perfil de usuario. 

{% alert important %}
Debido a que se utiliza un mensaje push para registrar un evento personalizado registrado en SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario para habilitar esta solución. Para los usuarios de iOS, Braze sólo almacenará un token a partir del momento en que un usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.
{% endalert %}

## Paso 2: Crea una campaña push silenciosa

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) que se desencadene a través del evento enviado por el servidor. 

![Una campaña de mensajería dentro de la aplicación basada en acciones que se entregará a los usuarios cuyos perfiles de usuario tengan el evento personalizado "evento_servidor".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campaña push debe incluir extras de par clave-valor, que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Una campaña de mensajería dentro de la aplicación de entrega basada en acciones que tiene dos pares clave-valor. "CAMPAIGN_NAME" configurado como "Ejemplo de nombre de mensaje dentro de la aplicación", y "IS_SERVER_EVENT" configurado como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si hay una clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si la hay.

Puedes modificar el nombre o las propiedades del evento enviando el valor deseado dentro de los extras del par clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como propiedad del evento.

## Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de mensajes dentro de la aplicación de entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "Desencadenante de mensajes dentro de la aplicación" donde "nombre_campaña" es igual a "Ejemplo de nombre de campaña de IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Ten en cuenta que estos mensajes dentro de la aplicación sólo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.
{% endalert %}

