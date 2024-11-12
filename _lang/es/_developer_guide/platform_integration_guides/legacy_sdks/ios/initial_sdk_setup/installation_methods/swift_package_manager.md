---
nav_title: Swift Package Manager
article_title: Integración de Swift Package Manager para iOS
platform: iOS
page_order: 3
description: "En este tutorial se cubre la instalación del SDK de Braze utilizando Swift Package Manager para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración con Swift Package Manager

La instalación del SDK de iOS mediante [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatiza la mayor parte del proceso de instalación. Antes de comenzar este proceso, asegúrate de que utilizas Xcode 12 o superior.

{% alert note %}
tvOS no está disponible actualmente a través de Swift Package Manager.
{% endalert %}

## Paso 1: Añadir la dependencia a tu proyecto

### Importar versión del SDK

Abre tu proyecto y ve a la configuración del mismo. Selecciona la pestaña **Paquetes Swift** y haz clic en el botón <i class="fas fa-plus"></i> añadir debajo de la lista de paquetes.

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Al importar la versión del SDK `3.33.1` o posterior, introduce la URL de nuestro repositorio del SDK de iOS (`https://github.com/braze-inc/braze-ios-sdk`) en el campo de texto y haz clic en **Siguiente**. 

Para las versiones `3.29.0` a `3.32.0`, utiliza la URL `https://github.com/Appboy/Appboy-ios-sdk`.

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

En la siguiente pantalla, selecciona la versión del SDK y haz clic en **Siguiente**. Las versiones `3.29.0` y posteriores son compatibles con Swift Package Manager.

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### Seleccionar paquetes

Selecciona el paquete que mejor se adapte a tus necesidades y haz clic en **Finalizar**. Asegúrate de seleccionar `AppboyKit` o `AppboyUI`. Incluir ambos paquetes puede provocar un comportamiento no deseado:

- `AppboyUI`
  - Es el más adecuado si piensas utilizar componentes de interfaz de usuario proporcionados por Braze.
  - Incluye `AppboyKit` automáticamente.
- `AppboyKit`
  - Es el más adecuado si no necesitas utilizar ninguno de los componentes de interfaz de usuario proporcionados por Braze (por ejemplo, tarjetas de contenido, mensajes dentro de la aplicación, etc.).
- `AppboyPushStory`
  - Incluye este paquete si has integrado Historias push en tu aplicación. Esto se admite a partir de la versión `3.31.0`.
  - En el menú desplegable de `Add to Target`, selecciona tu destino `ContentExtension` en lugar del destino de tu aplicación principal. 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## Paso 2: Configurar tu proyecto

A continuación, ve a **la configuración de compilación** de tu proyecto y añade el indicador `-ObjC` a la opción **Otros indicadores del enlazador**. Hay que añadir esta bandera y resolver cualquier [error](https://developer.apple.com/library/archive/qa/qa1490/_index.html) para poder seguir integrando el SDK.

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Si no añades la flag `-ObjC`, pueden faltar partes de la API y el comportamiento será indefinido. Puedes encontrarte con errores inesperados como "selector no reconocido enviado a la clase", fallos de la aplicación y otros problemas.
{% endalert %}

## Paso 3: Editar el esquema del objetivo
{% alert important %}
Si utilizas Xcode 12.5 o posterior, omite este paso.
{% endalert %}

Si utilizas Xcode 12.4 o anterior, edita el esquema del objetivo incluyendo el paquete Appboy (elemento del menú **Producto > Esquema > Editar esquema**):
1. Despliega el menú **Construir** y selecciona **Acciones posteriores**. Pulsa el botón más (+) y selecciona **Nueva acción de script de ejecución**.
2. En el desplegable **Proporcionar configuración de compilación desde**, selecciona el destino de tu aplicación.
3.  Copia este guión en el campo abierto:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

