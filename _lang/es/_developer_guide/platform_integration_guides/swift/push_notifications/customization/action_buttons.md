---
nav_title: Botones de acción
article_title: Botones de acción push para iOS
platform: Swift
page_order: 1
description: "Este artículo explica cómo implementar botones de acción en tus notificaciones push de iOS para el SDK Swift."
channel:
  - push

---

# Botones de acción {#push-action-buttons-integration}

> El SDK Swift de Braze proporciona soporte de gestión de URL para botones de acción push. 

Hay cuatro conjuntos de botones de acción para notificación push predeterminados para las categorías de notificación push predeterminadas de Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, y `More`. 

![Un GIF de un mensaje push que se tira hacia abajo para mostrar dos botones de acción personalizables.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

Si quieres crear tus propias categorías de notificación personalizadas, consulta [Personalización del botón de acción](#push-category-customization).

## Integración automática (recomendada)

Al integrar push mediante la opción de configuración `configuration.push.automation`, Braze registra automáticamente los botones de acción para las categorías predeterminadas de push y gestiona el análisis de clics del botón de acción push y el enrutamiento de URL.

## Integración manual

Para habilitar manualmente estos botones de acción para notificación push, primero regístrate en las categorías push predeterminadas. A continuación, utiliza el método delegado `didReceive(_:completionHandler:)` para habilitar los botones de acción para notificación push.

### Paso 1: Añadir categorías push predeterminadas Braze {#registering}

Utiliza el siguiente código para registrarte en las categorías predeterminadas de [push cuando te registres en push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Al hacer clic en los botones de acción para push con modo de activación en segundo plano, sólo se descartará la notificación y no se abrirá la aplicación. La próxima vez que el usuario abra la aplicación, el análisis de los clics en el botón de estas acciones se enviará al servidor.
{% endalert %}

### Paso 2: Habilitar la gestión interactiva de push {#enable-push-handling}

Para habilitar la gestión de nuestro botón de acción push, incluidos los análisis de clics y el enrutamiento de URL, añade el siguiente código al método delegado `didReceive(_:completionHandler:)` de tu aplicación:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Si utilizas el framework `UNNotification` y has implementado los [métodos de notificación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) Braze, ya deberías tener integrado este método. 

## Personalización de la categoría push

Además de proporcionar un conjunto de categorías push predeterminadas, Braze admite categorías y acciones de notificación personalizadas. Después de registrar las categorías en tu aplicación, puedes utilizar el panel de Braze para enviar estas categorías de notificación personalizadas a tus usuarios.

A continuación, estas categorías pueden asignarse a notificaciones push a través de nuestro panel para desencadenar las configuraciones del botón de acción de tu diseño. 

### Ejemplo de categoría push personalizada

Aquí tienes un ejemplo que aprovecha la dirección `LIKE_CATEGORY` que aparece en el dispositivo:

![Un mensaje push que muestra dos botones de acción para push "a diferencia de" y "me gusta".]({% image_buster /assets/img_archive/push_example_category.png %})

#### Paso 1: Registrar una categoría

Para registrar una categoría en tu aplicación, utiliza un método similar al siguiente:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Cuando creas un `UNNotificationAction`, puedes especificar una lista de opciones de acción. Por ejemplo, `UNNotificationActionOptions.foreground` permite a tus usuarios abrir tu aplicación tras pulsar el botón de acción. Esto es necesario para los comportamientos de navegación al hacer clic, como "Abrir aplicación" y "Vínculo profundo dentro de la aplicación". Para más información, consulta [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

#### Paso 2: Selecciona tus categorías

Después de registrar una categoría, utiliza el panel de Braze para enviar notificaciones de ese tipo a los usuarios.

{% alert tip %}
Sólo tienes que definir categorías de notificación personalizadas para los botones de acción con _acciones especiales_, como la vinculación en profundidad a tu aplicación o la apertura de una URL. No es necesario definirlos para los botones de acción que sólo rechazan una notificación.
{% endalert %}

1. En el panel de Braze, selecciona **Mensajería** > **Notificaciones push** y, a continuación, elige tu [campaña push]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message) de iOS.
2. En **Redactar notificación push**, activa **los Botones de acción**.
3. En el desplegable **Categoría de notificación de iOS**, selecciona **Introducir categoría personalizada de iOS previamente registrada**.
4. Por último, introduce una de las categorías que creaste anteriormente. El siguiente ejemplo, utiliza la categoría personalizada: `LIKE_CATEGORY`.

![El panel de la campaña de notificaciones push con la configuración de categorías personalizadas.]({% image_buster /assets/img_archive/ios-notification-category.png %})

