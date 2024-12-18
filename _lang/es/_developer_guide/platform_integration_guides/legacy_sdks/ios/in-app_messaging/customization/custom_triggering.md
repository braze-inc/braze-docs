---
nav_title: Desencadenar personalizado
article_title: Personalizar el desencadenamiento de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 7
description: "Este artículo de referencia trata de la mensajería personalizada dentro de la aplicación para tu aplicación de iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Desencadenar mensajes dentro de la aplicación personalizados

Por defecto, los mensajes dentro de la aplicación se desencadenan por tipos de eventos registrados por el SDK. Si quieres desencadenar mensajes dentro de la aplicación mediante eventos enviados por el servidor, también puedes conseguirlo.

Para habilitar esta característica, enviarías un push silencioso al dispositivo, que permitiría a este registrar un evento basado en el SDK. Este evento SDK desencadenaría posteriormente el mensaje dentro de la aplicación dirigido al usuario.

## Paso 1: Manejar el push silencioso y los pares clave-valor

Añade el siguiente código dentro del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Cuando se reciba el push silencioso, se registrará un evento "desencadenado de mensaje dentro de la aplicación" registrado en el SDK contra el perfil de usuario. Ten en cuenta que estos mensajes dentro de la aplicación sólo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.

## Paso 2: Crear una campaña push

Crea una campaña push silenciosa que se desencadene a través del evento enviado por el servidor. Para más detalles sobre cómo crear una campaña push silenciosa, consulta las [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/).

![Una campaña de mensajes dentro de la aplicación de entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "evento_servidor".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campaña push debe incluir extras de par clave-valor, que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación:

![n campaña de mensajería dentro de la aplicación de entrega basada en acciones que tiene dos pares clave-valor. "CAMPAIGN_NAME" configurado como "Ejemplo de nombre de mensaje dentro de la aplicación", y "IS_SERVER_EVENT" configurado como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si hay una clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si la hay.

Puedes modificar el nombre o las propiedades del evento enviando el valor deseado dentro de los extras del par clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como propiedad del evento.

## Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación, visible para el usuario, desde el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de entrega basada en acciones de mensajes dentro de la aplicación que se entregará a los usuarios que realicen el evento personalizado "Desencadenante de mensaje dentro de la aplicación" donde "nombre_campaña" es igual a "Ejemplo de nombre de mensaje dentro de la aplicación".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Debido a que se utiliza un mensaje push para registrar un evento personalizado registrado en SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario para habilitar esta solución. Tanto para iOS como para Android, Braze sólo almacenará un token a partir del momento en que un usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.

