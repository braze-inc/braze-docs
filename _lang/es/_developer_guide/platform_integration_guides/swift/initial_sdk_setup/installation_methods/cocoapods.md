---
nav_title: CocoaPods
article_title: Integración de CocoaPods para iOS
platform: Swift
page_order: 2
description: "Este artículo de referencia muestra cómo integrar el SDK Swift de Braze utilizando CocoaPods para iOS."

---

# Integración de CocoaPods

## Paso 1: Instalar CocoaPods

La instalación del SDK de iOS a través de [CocoaPods](http://cocoapods.org/) automatiza la mayor parte del proceso de instalación por ti. Para instalar CocoaPods, consulta la [guía de inicio de](https://guides.cocoapods.org/using/getting-started.html) CocoaPods.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

Si tienes problemas relacionados con CocoaPods, consulta la [guía de solución de problemas de de CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "CocoaPodsGuía de solución de problemas").

## Paso 2: Construir el archivo de bibliotecas

Ahora que has instalado la Gema de Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto Xcode llamado `Podfile`.

{% alert note %}
A partir de la versión 7.4.0, el SDK Swift de Braze tiene canales de distribución adicionales como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) y [XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si quieres utilizar cualquiera de estos formatos en su lugar, sigue las instrucciones de instalación de su repositorio respectivo.
{% endalert %}

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contiene la biblioteca principal del SDK, que proporciona soporte para análisis y notificaciones push.

Te sugerimos que versiones Braze para que las actualizaciones de vainas cojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto parece `pod 'BrazeKit' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'BrazeKit'` en tu archivo de bibliotecas.

#### Bibliotecas adicionales

El SDK de Swift de Braze separa las características en bibliotecas independientes para proporcionar a los desarrolladores un mayor control sobre qué características importar a sus proyectos. Además de `BrazeKit`, puedes añadir las siguientes bibliotecas a tu archivo de bibliotecas:

| Biblioteca | Detalles |
| ------- | ------- |
| `pod 'BrazeLocation'` | Biblioteca de ubicación que proporciona soporte para el análisis de la ubicación y la supervisión del geovallado. |
| `pod 'BrazeUI'` | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación y tarjetas de contenido. |
{: .ws-td-nw-1}

##### Bibliotecas de extensión

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) y [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) son módulos de extensión que proporcionan funcionalidad adicional y no deben añadirse directamente al objetivo principal de tu aplicación. En su lugar, tendrás que crear objetivos de extensión independientes para cada uno de estos módulos e importar los módulos Braze en sus objetivos correspondientes.

| Biblioteca | Detalles |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | Biblioteca de extensión de servicios de notificación que proporciona soporte para notificaciones push enriquecidas. |
| `pod 'BrazePushStory'` | Biblioteca de extensión de contenido de notificaciones que ofrece soporte para historias push. |
{: .ws-td-nw-1}

## Paso 3: Instalación del SDK de Braze

Para instalar el SDK de Braze CocoaPod, navega hasta el directorio del proyecto de tu aplicación en Xcode dentro de tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode.

![Una carpeta de Ejemplo de Braze ampliada para mostrar el nuevo `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Actualizar el SDK de Braze mediante CocoaPods

Para actualizar un CocoaPod, simplemente ejecuta el siguiente comando dentro del directorio de tu proyecto:

```
pod update
```

