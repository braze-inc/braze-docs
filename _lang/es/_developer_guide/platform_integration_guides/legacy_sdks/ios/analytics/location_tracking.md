---
nav_title: Seguimiento de ubicación
article_title: Seguimiento de ubicación para iOS
platform: iOS
page_order: 6
description: "Este artículo muestra cómo configurar el seguimiento de ubicación para tu aplicación iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Seguimiento de ubicación para iOS

De manera predeterminada, Braze desactiva el seguimiento de ubicación. Habilitamos el seguimiento de ubicación después de que la aplicación anfitriona haya optado por el seguimiento de ubicación y haya obtenido el permiso del usuario. Siempre que los usuarios hayan optado por el seguimiento de ubicación, Braze registrará una única ubicación para cada usuario al inicio de la sesión.

{% alert important %}
Para que el seguimiento de ubicación funcione de forma fiable en iOS 14 para los usuarios que den permiso de ubicación aproximada, debes actualizar tu versión del SDK al menos a `3.26.1`.
{% endalert %}

## Habilitación del seguimiento de ubicación automático

A partir del SDK para iOS de Braze `v3.17.0`, el seguimiento de ubicación está desactivado de manera predeterminada. Puedes habilitar el seguimiento de ubicación automático mediante el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada booleana `EnableAutomaticLocationCollection` y establece el valor `YES`. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

También puedes habilitar el seguimiento de ubicación automático al iniciar la aplicación mediante el método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, establece `ABKEnableAutomaticLocationCollectionKey` en `YES`. Por ejemplo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### Pasar datos de ubicación a Braze

Se pueden utilizar los dos métodos siguientes para configurar manualmente la última ubicación conocida del usuario.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

Consulta [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h) para más información.

