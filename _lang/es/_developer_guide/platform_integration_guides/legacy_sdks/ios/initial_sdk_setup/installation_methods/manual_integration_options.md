---
nav_title: Manual
article_title: Opciones de integración manual para iOS
platform: iOS
page_order: 4
description: "En este artículo de referencia se muestra cómo integrar manualmente el SDK de Braze para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración manual

{% alert tip %}
Te recomendamos encarecidamente que implementes el SDK mediante un administrador de paquetes como [Swift Package Manager](../swift_package_manager/), [CocoaPods](../cocoapods/) o [Carthage](../carthage_integration/). Te ahorrará mucho tiempo y automatizará gran parte del proceso. Sin embargo, si no puedes hacerlo, puedes completar la integración manualmente siguiendo las instrucciones.
{% endalert %}

## Paso 1: Descarga del SDK de Braze

### Opción 1: XCFramework dinámico

1. Descarga `Appboy_iOS_SDK.xcframework.zip` de la [página de la versión](https://github.com/appboy/appboy-ios-sdk/releases) y extrae el archivo.
2. En Xcode, arrastra y suelta este `.xcframework` en tu proyecto.
3. En la pestaña **General** del proyecto, selecciona **Incrustar y firmar** para `Appboy_iOS_SDK.xcframework`.

### Opción 2: XCFramework estático para integración estática

1. Descarga `Appboy_iOS_SDK.zip` desde la [página de la versión](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. En Xcode, desde el navegador de proyectos, selecciona el proyecto o grupo de destino para Braze<br><br>
3. Ve a **Archivo > Añadir archivos > Nombre_proyecto**.<br><br>
4. Añade las carpetas `AppboyKit` y `AppboyUI` a tu proyecto como un grupo.
	- Asegúrate de que la opción **Copiar elementos en la carpeta del grupo de destino** está seleccionada si es la primera vez que realizas la integración. Amplía **Opciones** en el selector de archivos para seleccionar **Copiar elementos si es necesario** y **Crear grupos**.
	- Elimina los directorios `AppboyKit/include` y `AppboyUI/include`.<br><br>
5. (Opcional) Si se te aplica una de las siguientes opciones:
  - Sólo quieres las características principales de análisis del SDK y no utilizas ninguna característica de la interfaz de usuario (por ejemplo, mensajes dentro de la aplicación o tarjetas de contenido).
  - Dispones de una interfaz de usuario personalizada para las características de Braze UI y te encargas tú mismo de la descarga de imágenes.<br><br>Puedes utilizar la versión básica del SDK eliminando el archivo `ABKSDWebImageProxy.m` y `Appboy.bundle`. Esto eliminará la dependencia del framework `SDWebImage` y todos los recursos relacionados con la interfaz de usuario (por ejemplo, archivos Nib, imágenes, archivos de localización) del SDK.

{% alert warning %}
Si intentas utilizar la versión básica del SDK sin las características de la interfaz de usuario de Braze, los mensajes dentro de la aplicación no se mostrarán. Si intentas mostrar la interfaz de usuario de las tarjetas de contenido Braze con la versión básica, se producirá un comportamiento impredecible.
{% endalert %}

## Paso 2: Añadir bibliotecas iOS necesarias

1. Haz clic en el objetivo de tu proyecto (utilizando la navegación de la izquierda), y selecciona la pestaña **Fases de construcción**.<br><br>
2. Haz clic en el botón <i class="fas fa-plus"></i> situado debajo de **Vincular binarios con bibliotecas**.<br><br>
3. En el menú, selecciona `SystemConfiguration.framework`.<br><br>
4. Marca esta biblioteca como necesaria utilizando el menú desplegable situado junto a `SystemConfiguration.framework`.<br><br>
5. Repite la operación para añadir a tu proyecto cada uno de los siguientes frameworks necesarios, marcando cada uno como "necesario".
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Añade los siguientes marcos y márcalos como opcionales:
	- `CoreTelephony.framework`<br><br>
7. Selecciona la pestaña **Configuración de construcción**. En la sección **Enlazar**, localiza la configuración **Otros indicadores del enlazador** y añade el indicador `-ObjC`.<br><br>
8. El framework `SDWebImage` es necesario para que las tarjetas de contenido y la mensajería dentro de la aplicación funcionen correctamente. `SDWebImage` se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar tarjetas de contenido o mensajes dentro de la aplicación, sigue los pasos de integración de SDWebImage.

### Integración de SDWebImage

Para instalar `SDWebImage`, sigue sus [instrucciones](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) y luego arrastra y suelta el `XCFramework` resultante en tu proyecto.

### Seguimiento de ubicación opcional

1. Añade `CoreLocation.framework` para habilitar el seguimiento de ubicación.
2. Debes autorizar la ubicación de tus usuarios utilizando `CLLocationManager` en tu aplicación.

## Paso 3: Cabecera de puente Objective-C

{% alert note %}
Si tu proyecto sólo utiliza Objective-C, sáltate este paso.
{% endalert %}

Si tu proyecto utiliza Swift, necesitarás un archivo de encabezado puente.

Si no tienes un archivo de cabecera puente, crea uno y nómbralo `your-product-module-name-Bridging-Header.h` eligiendo **Archivo > Nuevo > Archivo > (iOS u OS X) > Fuente > Archivo de cabecera**. A continuación, añade la siguiente línea de código al principio de tu archivo de cabecera puente:
```
#import "AppboyKit.h"
```

En la **configuración de compilación** de tu proyecto, añade la ruta relativa de tu archivo de cabecera a la configuración de compilación de `Objective-C Bridging Header` en `Swift Compiler - Code Generation`.

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
