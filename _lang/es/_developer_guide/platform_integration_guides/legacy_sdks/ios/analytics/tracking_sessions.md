---
nav_title: Seguimiento de sesiones
article_title: Seguimiento de sesiones para iOS
platform: iOS
page_order: 0
description: "Este artículo de referencia muestra cómo suscribirte a las actualizaciones de sesión de tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Seguimiento de sesión para iOS

El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. Nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y el recuento de sesiones visibles dentro del panel Braze, basándose en la siguiente semántica de sesión.

## Ciclo de vida de la sesión

Una sesión se inicia cuando llamas a `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, tras lo cual, por defecto, las sesiones comienzan cuando se dispara la notificación de `UIApplicationWillEnterForegroundNotification` (como cuando la aplicación entra en primer plano) y terminan cuando la aplicación abandona el primer plano (como cuando se dispara la notificación de `UIApplicationDidEnterBackgroundNotification` o cuando la aplicación muere).

{% alert note %}
Si necesitas forzar una nueva sesión, puedes hacerlo cambiando de usuario.
{% endalert %}

## Personalizar el tiempo de espera de la sesión

A partir de Braze iOS SDK v3.14.1, puedes configurar el tiempo de espera de la sesión utilizando el archivo Info.plist. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada número `SessionTimeout` y establece el valor de tu tiempo de espera de sesión personalizado. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

Alternativamente, puedes establecer la clave `ABKSessionTimeoutKey` al valor entero deseado en tu objeto `appboyOptions` pasado a [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9).

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

Si has establecido un tiempo de espera de la sesión, toda la semántica de la sesión se extiende a ese tiempo de espera personalizado.

{% alert note %}
El valor mínimo de `sessionTimeoutInSeconds` es 1 segundo. El valor predeterminado es 10 segundos.
{% endalert %}

## Probar el seguimiento de la sesión

Para detectar sesiones a través de tu usuario, busca a tu usuario en el panel y navega hasta **Uso de la aplicación** en el perfil de usuario. Puedes confirmar que el seguimiento de sesiones funciona comprobando que la métrica "Sesiones" aumenta cuando esperas que lo haga.

![La sección de uso de la aplicación de un perfil de usuario que muestra el número de sesiones, la última fecha de uso y la primera fecha de uso.]({% image_buster /assets/img_archive/test_session.png %})

