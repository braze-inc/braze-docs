---
nav_title: Ubicaciones y geovallas
article_title: Ubicaciones y geovallas para iOS
platform: iOS
page_order: 6
description: "Este artículo de referencia explica cómo implementar ubicaciones y geovallas en tu aplicación de iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ubicaciones y geovallas

Para habilitar geovallas en iOS:

1. Tu integración debe admitir notificaciones push en segundo plano.
2. Las geovallas de Braze [deben habilitarse]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking) a través del SDK, ya sea habilitando implícitamente la recopilación de ubicaciones o habilitando explícitamente la recopilación de geovallas. No están habilitadas de forma predeterminada.

{% alert important %}
A partir de iOS 14, las geovallas no funcionan de forma fiable para los usuarios que deciden dar permiso de ubicación aproximada.
{% endalert %}

## Paso 1: Habilitar el push en segundo plano

Para aprovechar al máximo nuestra estrategia de sincronización de geovallas, debes tener habilitado el [push en segundo plano]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work), además de completar la integración push estándar.

## Paso 2: Habilitar geovallas

De forma predeterminada, las geovallas se habilitan en función de si está habilitada la recopilación automática de ubicaciones. Puedes habilitar las geovallas utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada Booleano `EnableGeofences` y establece el valor en `YES`. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

También puedes habilitar las geovallas al iniciar la aplicación utilizando el método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, establece `ABKEnableGeofencesKey` en `YES`. Por ejemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Paso 3: Comprobar las notificaciones push en segundo plano de Braze

Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. Sigue el artículo de [personalización de iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) para asegurarte de que tu aplicación no realiza ninguna acción no deseada al recibir notificaciones de sincronización de geovallas de Braze.

## Paso 4: Añadir NSLocationAlwaysUsageDescription a tu Info.plist

Añade las claves `NSLocationAlwaysUsageDescription` y `NSLocationAlwaysAndWhenInUseUsageDescription` a tu `info.plist` con un valor `String` que contenga una descripción de por qué tu aplicación necesita hacer seguimiento de ubicación. Ambas claves son necesarias para iOS 11 o posterior.
Esta descripción se mostrará cuando el aviso de ubicación del sistema solicite autorización y debe explicar claramente a tus usuarios las ventajas del seguimiento de ubicación.

## Paso 5: Solicitar autorización al usuario

La característica de geovallas solo funciona cuando se concede la autorización de ubicación `Always`.

Para solicitar la autorización de ubicación `Always`, usa el siguiente código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Paso 6: Habilitar geovallas en el dashboard

iOS solo permite almacenar hasta 20 geovallas para una aplicación determinada. El uso de ubicaciones ocupará algunos de estos 20 espacios disponibles para geovallas. Para evitar interrupciones accidentales o no deseadas de otras funciones relacionadas con geovallas en tu aplicación, las geovallas de ubicación deben habilitarse para aplicaciones individuales en el dashboard.

Para que las ubicaciones funcionen correctamente, también debes confirmar que tu aplicación no está utilizando todos los espacios de geovalla disponibles.

### Habilitar las geovallas desde la página de ubicaciones:

![Las opciones de geovalla en la página de ubicaciones de Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Habilitar las geovallas desde la página de configuración:

![La casilla de verificación de geovalla situada en las páginas de configuración de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desactivar las solicitudes automáticas de geovallas

A partir de la versión 3.21.3 del SDK de iOS, puedes desactivar la solicitud automática de geovallas. Puedes hacerlo utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada Booleano `DisableAutomaticGeofenceRequests` y establece el valor en `YES`.

También puedes desactivar las solicitudes automáticas de geovallas al iniciar la aplicación mediante el método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, establece `ABKDisableAutomaticGeofenceRequestsKey` en `YES`. Por ejemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Si decides utilizar esta opción, tendrás que solicitar manualmente las geovallas para que la característica funcione.

## Solicitar geovallas manualmente

Cuando el SDK de Braze solicita geovallas para monitorizar desde el backend, informa de la ubicación actual del usuario y recibe geovallas que se determinan como óptimamente relevantes en función de la ubicación comunicada. Hay un límite de velocidad de una actualización de geovalla por sesión.

Para controlar la ubicación que informa el SDK con el fin de recibir las geovallas más relevantes, a partir de la versión 3.21.3 del SDK de iOS, puedes solicitar manualmente geovallas proporcionando la latitud y longitud de una ubicación. Se recomienda desactivar las solicitudes automáticas de geovallas cuando utilices este método. Para ello, utiliza el siguiente código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}