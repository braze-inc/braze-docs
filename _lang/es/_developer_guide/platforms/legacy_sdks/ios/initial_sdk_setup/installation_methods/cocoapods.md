---
nav_title: CocoaPods
article_title: Integración de CocoaPods para iOS
platform: iOS
page_order: 2
description: "Este artículo de referencia muestra cómo integrar el SDK de Braze utilizando CocoaPods para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de CocoaPods

## Paso 1: Instalar CocoaPods

La instalación del SDK de iOS a través de [CocoaPods](http://cocoapods.org/) automatiza la mayor parte del proceso de instalación por ti. Antes de comenzar este proceso, asegúrate de que utilizas [la versión 2.0.0 de Ruby](https://www.ruby-lang.org/en/installation/) o superior. No te preocupes, no es necesario conocer la sintaxis de Ruby para instalar este SDK.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

Si tienes problemas relacionados con CocoaPods, consulta la [guía de solución de problemas de](http://guides.cocoapods.org/using/troubleshooting.html) CocoaPods.

{% alert note %}
Si se te pide que sobrescribas el ejecutable `rake`, consulta las instrucciones [para empezar](http://guides.cocoapods.org/using/getting-started.html) en CocoaPods.org para más detalles.
{% endalert %}

## Paso 2: Construir el archivo de bibliotecas

Ahora que has instalado la Gema de Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto Xcode llamado `Podfile`.

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

Te sugerimos que versiones Braze para que las actualizaciones de vainas cojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto parece `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'Appboy-iOS-SDK'` en tu archivo de bibliotecas.

#### Subespecies

Recomendamos a los integradores que importen nuestro SDK completo. Sin embargo, si estás seguro de que sólo vas a integrar una característica concreta de Braze, puedes importar sólo la subespecífica de interfaz de usuario deseada en lugar del SDK completo.

| Subespecie | Detalles |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | La subespecificación `InAppMessage` contiene la interfaz de usuario de mensajes dentro de la aplicación de Braze y el SDK central.|
| `pod 'Appboy-iOS-SDK/ContentCards'` | La subespecificación `ContentCards` contiene la interfaz de usuario de la tarjeta de contenido de Braze y el SDK central. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | La subespecífica `NewsFeed` contiene el SDK del núcleo de Braze. |
| `pod 'Appboy-iOS-SDK/Core'` | La subespecificación `Core` contiene soporte para análisis, como eventos y atributos personalizados. |
{: .ws-td-nw-1}

## Paso 3: Instalación del SDK de Braze

Para instalar los SDK de Braze CocoaPods, ve al directorio de tu proyecto de aplicación Xcode en tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode. 

![Una carpeta de ejemplo de Appboy ampliada para mostrar el nuevo `AppbpyExample.workspace`.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Actualizar el SDK de Braze mediante CocoaPods

Para actualizar un CocoaPod, simplemente ejecuta el siguiente comando dentro del directorio de tu proyecto:

```
pod update
```

