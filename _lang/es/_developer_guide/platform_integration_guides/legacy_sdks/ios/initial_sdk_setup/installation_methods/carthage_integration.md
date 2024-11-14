---
nav_title: Carthage
article_title: Integración de Carthage para iOS
platform: iOS
page_order: 1
description: "En este artículo de referencia se muestra cómo integrar el SDK de Braze utilizando Carthage para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración en Cartago

## Importa el SDK

A partir de la versión `4.4.0`, el SDK de Braze es compatible con XCFrameworks cuando se integra a través de Carthage. Para importar el SDK completo, incluye estas líneas en tu `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Consulta la [guía de inicio rápido de Carthage](https://github.com/Carthage/Carthage#quick-start) para obtener más instrucciones sobre la importación del SDK.

Cuando migres desde una versión anterior a `4.4.0`, sigue la [guía de migración de Carthage para XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Para más detalles sobre la sintaxis de `Cartfile` o características como la fijación de versiones, visita la [documentación de Carthage](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Para conocer el uso específico de Carthage en cada plataforma, consulta su [guía del usuario](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Versiones anteriores

Para las versiones `3.24.0` a `4.3.4`, incluye lo siguiente en tu `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Para importar versiones anteriores a `3.24.0`, incluye lo siguiente en tu `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Asegúrate de sustituir `<BRAZE_IOS_SDK_VERSION>` por la [versión adecuada](https://github.com/Appboy/appboy-ios-sdk/releases) del SDK Braze para iOS en formato "x.y.z".

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Sólo integración del núcleo

Si quieres utilizar el SDK básico sin componentes de interfaz de usuario ni dependencias, instala la versión básica del marco de trabajo Braze Carthage incluyendo la siguiente línea en tu `Cartfile`:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

