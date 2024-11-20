---
nav_title: Ejemplos de aplicaciones
article_title: Ejemplos de aplicaciones para iOS
platform: Swift
page_order: 9
search_rank: 2
description: "En este artículo se cubren aplicaciones de ejemplo del SDK Swift de iOS."

---

# Ejemplos de aplicaciones

> Para tu comodidad, los SDK de Braze incluyen aplicaciones de ejemplo en el repositorio. Cada una de estas aplicaciones es totalmente compilable, por lo que puedes probar las características de Braze a la vez que las implementas en tus propias aplicaciones. 

Probar el comportamiento dentro de tu propia aplicación en comparación con el comportamiento esperado y las rutas de código dentro de las aplicaciones de ejemplo es una forma excelente de depurar cualquier problema que puedas encontrarte.

## Ejemplos de navegación

Hay varias aplicaciones de prueba disponibles en la carpeta `Examples` del [repositorio GitHub del SDK de Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples). En el documento LÉEME se describen todas las diferentes permutaciones de las integraciones de muestra, como por ejemplo:

1. Tipos de integración (Swift Package Manager, CocoaPods, Manual)
2. Lenguajes de codificación (Swift y Objective-C)
3. Plataformas (iOS, tvOS, Mac Catalyst, etc.)
4. Características (mensajes dentro de la aplicación, tarjetas de contenido, ubicación, notificaciones push enriquecidas, historias push, etc.)
5. Tipos de personalización (IU predeterminada, IU totalmente personalizada)

## Construir aplicaciones de prueba

Sigue estas instrucciones para crear y ejecutar nuestras aplicaciones de prueba.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) y anota la clave de API y el punto final del identificador de la aplicación.
2. Según tu método de integración (Swift Package Manager, CocoaPods, Manual), selecciona el archivo `xcodeproj` adecuado para abrirlo.
3. Coloca tu clave de API y tu punto final en el campo correspondiente del archivo `Credentials`.

