---
nav_title: Botones de acción
article_title: Botones de acción push para iOS
platform: iOS
page_order: 1
description: "Este artículo de referencia explica cómo implementar botones de acción en tus notificaciones push de iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Botones de acción {#push-action-buttons-integration}

El SDK de Braze para iOS es compatible con las categorías push predeterminadas, incluida la compatibilidad con la gestión de URL para cada botón de acción push. Actualmente, las categorías predeterminadas tienen cuatro conjuntos de botones de acción para push: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, y `More`. 

![Un GIF de un mensaje push que se tira hacia abajo para mostrar dos botones de acción personalizables.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Para registrar nuestras categorías push predeterminadas, sigue las instrucciones de integración:

## Paso 1: Añadir categorías push predeterminadas Braze

Utiliza el siguiente código para registrarte en nuestras categorías predeterminadas de push cuando te [registres en push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Al hacer clic en los botones de acción para push con modo de activación en segundo plano, sólo se descartará la notificación y no se abrirá la aplicación. La próxima vez que el usuario abra la aplicación, el análisis de los clics en el botón de estas acciones se enviará al servidor.

Si quieres crear tus propias categorías de notificación personalizadas, consulta [Personalización del botón de acción]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization).

## Paso 2: Habilitar la gestión interactiva de push

Si utilizas el marco `UNNotification` y has implementado [delegados]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) Braze, ya deberías tener integrado este método. 

Para habilitar la gestión de nuestro botón de acción push, incluidos los análisis de clics y el enrutamiento de URL, añade el siguiente código al método delegado `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Si no utilizas UNNotification Framework, tendrás que añadir el siguiente código a la página `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` de tu aplicación para habilitar la gestión de nuestro botón de acción para notificación push:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Recomendamos encarecidamente que las personas que utilicen `handleActionWithIdentifier` empiecen a usar un framework `UNNotification`. Recomendamos esto debido a la obsolescencia de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personalización de la categoría push

Además de proporcionar un conjunto de [categorías push predeterminadas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), Braze admite categorías y acciones de notificación personalizadas. Después de registrar categorías en tu aplicación, puedes utilizar el panel de Braze para enviar categorías de notificación a tus usuarios.

Si no utilizas el marco `UserNotifications`, consulta la documentación [sobre categorías alternativas](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

A continuación, estas categorías pueden asignarse a notificaciones push a través de nuestro panel para desencadenar las configuraciones del botón de acción de tu diseño. Aquí tienes un ejemplo que aprovecha la dirección `LIKE_CATEGORY` que aparece en el dispositivo:

![Un mensaje push que muestra dos botones de acción para push "a diferencia de" y "me gusta".]({% image_buster /assets/img_archive/push_example_category.png %})


