---
nav_title: Integración manual
article_title: Integración manual para iOS
platform: Swift
page_order: 3
description: "Este artículo de referencia muestra cómo integrar el SDK de Braze Swift mediante instalación manual."
toc_headers: "h2"
---

# Integración manual

> Si no tienes acceso a un administrador de paquetes, como [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) o [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/), puedes integrar manualmente el SDK de Swift.

## Paso 1: Descargar el SDK de Braze

Ve a [la página de lanzamiento del SDK de Braze en GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) y descarga `braze-swift-sdk-prebuilt.zip`.

!["La página de lanzamiento del SDK de Braze en GitHub"]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Paso 2: Elige tus marcos

El SDK Swift de Braze contiene diversos XCFrameworks independientes, lo que te da libertad para integrar las características que desees, sin necesidad de integrarlos todos. Consulta la tabla siguiente para elegir tus XCFrameworks:

| Paquete                    | ¿Es necesario? | Descripción                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Sí       | Biblioteca principal del SDK que proporciona soporte para análisis y notificaciones push.                                                                                                                                                                                                                                             |
| `BrazeLocation`            | No        | Biblioteca de ubicación que proporciona soporte para análisis de ubicación y control de geovallas.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | No        | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación y tarjetas de contenido.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | No        | Biblioteca de extensión del servicio de notificaciones que proporciona soporte para notificaciones push enriquecidas. No añadas esta biblioteca directamente al objetivo principal de tu aplicación, [añade en su lugar la biblioteca `BrazeNotificationService` por separado](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).     |
| `BrazePushStory`           | No        | Biblioteca de extensión de contenido de notificaciones que proporciona soporte para historias push. No añadas esta biblioteca directamente al objetivo principal de tu aplicación, [añade en su lugar la biblioteca `BrazePushStory` por separado](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                     |
| `BrazeKitCompat`           | No        | Biblioteca de compatibilidad que contiene todas las clases y métodos de `Appboy` y `ABK*` que estaban disponibles en la versión 4 de `Appboy-iOS-SDK`.X.X. Para conocer los detalles de uso, consulta el escenario de migración mínima en la [guía de migración](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | No        | Biblioteca de compatibilidad que contiene todas las clases y métodos de `ABK*` que estaban disponibles en la biblioteca `AppboyUI` a partir de la versión 4 de `Appboy-iOS-SDK`.X.X. Para conocer los detalles de uso, consulta el escenario de migración mínima en la [guía de migración](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | No        | Dependencia utilizada sólo por `BrazeUICompat` en el escenario de migración mínima. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Prepara tus archivos

Decide si quieres utilizar XCFrameworks **estáticos** o **dinámicos**, y luego prepara tus archivos:

{% tabs %}
{% tab dinámico %}
1. Crea un directorio temporal para tus XCFrameworks.
2. En `braze-swift-sdk-prebuilt`, abre el directorio `dynamic` y mueve `BrazeKit.xcframework` a tu directorio. Tu directorio debe ser similar al siguiente
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Mueve cada uno de los [XCFrameworks que hayas elegido](#step-2-choose-your-frameworks) a tu directorio temporal. Tu directorio debe ser similar al siguiente
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab estático %}
### Paso 3.1: Prepara tus marcos

1. Crea un directorio temporal para tus XCFrameworks.
2. En `braze-swift-sdk-prebuilt`, abre el directorio `static` y mueve `BrazeKit.xcframework` a tu directorio. Tu directorio debe ser similar al siguiente
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. Mueve cada uno de los [XCFrameworks que hayas elegido](#step-2-choose-your-frameworks) a tu directorio temporal. Tu directorio debe ser similar al siguiente
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### Paso 3.2: Prepara tus paquetes

1. Crea un directorio temporal para tus paquetes.
2. Abre el directorio `bundles` y mueve `BrazeKit.bundle` a tu directorio. Tu directorio debe ser similar al siguiente
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. Si utilizas los XCFrameworks `BrazeLocation`, `BrazeUI`, `BrazeUICompat`, o `SDWebImage`, mueve sus paquetes correspondientes a tu directorio temporal. Tu directorio debe ser similar al siguiente
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
Mueve sólo los paquetes para los [marcos que hayas preparado](#step-31-prepare-your-frameworks).
{% endalert %}
{% endtab %}
{% endtabs %}

## Paso 4: Integra tus marcos de trabajo

A continuación, integra los XCFrameworks **dinámicos** o **estáticos** que [preparaste anteriormente](#step-3-prepare-your-files):

{% tabs %}
{% tab dinámico %}
En tu proyecto Xcode, selecciona tu objetivo de compilación y, a continuación, **General**. En **Frameworks, Bibliotecas y Contenido incrustado**, arrastra y suelta los [archivos que preparaste anteriormente](#step-3-prepare-your-files).

!["Un proyecto Xcode de ejemplo con cada biblioteca Braze configurada como 'Incrustar y firmar'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
Para habilitar la compatibilidad con GIF, añade `SDWebImage.xcframework`, situado en `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}
{% endtab %}

{% tab estático %}
En tu proyecto Xcode, selecciona tu objetivo de compilación y, a continuación, **General**. En **Marcos, Bibliotecas y Contenido incrustado**, arrastra y suelta los [marcos que preparaste anteriormente](#step-31-prepare-your-frameworks). Junto a cada marco, elige **No incrustar**. 

!["Un proyecto Xcode de ejemplo con cada biblioteca Braze configurada como 'No incrustar'"]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
Para habilitar la compatibilidad con GIF, añade `SDWebImage.xcframework`, situado en `braze-swift-sdk-prebuilt/static`.
{% endalert %}

En tu objetivo de construcción, selecciona **Fases de construcción**. En **Copiar recursos de paquetes** arrastra y suelta los [paquetes que preparaste anteriormente](#step-32-prepare-your-bundles).

!["Un proyecto Xcode de ejemplo con bundles añadidos en 'Copiar recursos de bundle'."]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Errores comunes de los proyectos Objective-C

Si tu proyecto Xcode sólo contiene archivos Objective-C, es posible que aparezcan errores de "símbolo ausente" cuando intentes compilar tu proyecto. Para solucionar estos errores, abre tu proyecto y añade un archivo Swift vacío a tu árbol de archivos. Esto forzará a tu cadena de herramientas de compilación a incrustar [Swift Runtime](https://support.apple.com/kb/dl1998) y enlazar con los frameworks apropiados durante el tiempo de compilación.

```bash
FILE_NAME.swift
```

Sustituye `FILE_NAME` por cualquier cadena no espaciada. Tu archivo debe tener un aspecto similar al siguiente

```bash
empty_swift_file.swift
```
