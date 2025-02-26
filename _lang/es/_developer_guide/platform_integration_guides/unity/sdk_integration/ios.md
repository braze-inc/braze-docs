---
nav_title: iOS
article_title: Integración de SDK iOS para Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "En este artículo de referencia se cubre la integración del SDK de iOS para la plataforma Unity."
search_rank: .9
---

# Integración de SDK iOS

> En este artículo de referencia se cubre la integración del SDK de iOS para la plataforma Unity. Sigue esta guía para hacer que Braze funcione en tu aplicación Unity. 

Si estás pasando de una integración manual, lee las instrucciones sobre [Transición a una integración automatizada](#transitioning-from-manual-to-automated-integration-ios).

## Paso 1: Elige tu paquete Braze Unity

El [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) de Braze incluye enlaces nativos para las plataformas Android e iOS, junto con una interfaz en C#.

El paquete Braze Unity está disponible para su descarga en la [página de versiones de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) con dos opciones de integración:

1. `Appboy.unitypackage` solo
  - Este paquete incluye los SDK de Braze para Android e iOS sin dependencias adicionales. Con este método de integración, no funcionarán correctamente las características de mensajería dentro de la aplicación de Braze ni las tarjetas de contenido en iOS. Si quieres utilizar todas las funciones de Braze sin código personalizado, utiliza la opción siguiente.
  - Para utilizar esta opción de integración, asegúrate de que la casilla junto a `Import SDWebImage dependency` *no está marcada* en la interfaz de usuario de Unity, en "Configuración de Braze".
2. `Appboy.unitypackage` con `SDWebImage`
  - Esta opción de integración incluye los SDK de Braze para Android e iOS y la dependencia de [SDWebImage](https://github.com/SDWebImage/SDWebImage) para el SDK de iOS, que es necesaria para el correcto funcionamiento de la mensajería dentro de la aplicación de Braze y las características de las tarjetas de contenido en iOS. El framework `SDWebImage` se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar todas las funciones de Braze, descarga e importa este paquete.
  - Para importar automáticamente `SDWebImage`, asegúrate de *marcar* la casilla junto a `Import SDWebImage dependency` en la interfaz de usuario de Unity, en "Configuración de Braze".

**iOS**: Para ver si necesitas la dependencia [SDWebImage](https://github.com/SDWebImage/SDWebImage) para tu proyecto iOS, visita la [documentación de mensajes dentro de la aplicación iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: A partir de Unity 2.6.0, el artefacto incluido Braze Android SDK requiere dependencias de [AndroidX](https://developer.android.com/jetpack/androidx). Si antes utilizabas un `jetified unitypackage`, puedes pasar sin problemas al `unitypackage` correspondiente.

## Paso 2: Importa el paquete

En el editor de Unity, importa el paquete a tu proyecto de Unity yendo a **Assets (Activos) > Import Package (Importar paquete) > Custom Package (Paquete personalizado).** A continuación, haz clic en **Importar**.

También puedes seguir las instrucciones de [importación de paquetes de activos de](https://docs.unity3d.com/Manual/AssetPackages.html) Unity para obtener una guía más detallada sobre la importación de paquetes de Unity personalizados. 

{% alert note %}
Si solo deseas importar el plugin para iOS o Android, anula la selección del subdirectorio `Plugins/Android` o `Plugins/iOS` al importar `.unitypackage` de Braze.
{% endalert %}

## Paso 3: Configura tu clave de API

Braze proporciona una solución nativa de Unity para automatizar la integración de Unity en iOS. Esta solución modifica el proyecto creado en Xcode utilizando [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) de Unity y subclasifica el `UnityAppController` utilizando la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. En el editor de Unity, abre los Ajustes de configuración de Braze navegando hasta **Braze > Braze Configuration (Configuración de Braze)**.
2. Marca la casilla **Automatizar la integración de Unity iOS**.
3. En el campo **Clave de API de Braze**, introduce la clave de API de tu aplicación que se encuentra en **Administrar configuración**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si tu aplicación ya está utilizando otra subclase de `UnityAppController`, tendrás que fusionar la implementación de tu subclase con `AppboyAppDelegate.mm`.

## Integración de SDK básica completa

Ahora Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Para obtener más información sobre la integración de push, consulta los siguientes artículos: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) y [tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Para conocer las opciones avanzadas de integración de SDK, consulta [Implementación avanzada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced).

