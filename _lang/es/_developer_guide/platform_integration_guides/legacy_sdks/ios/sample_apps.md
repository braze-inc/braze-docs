---
nav_title: Ejemplos de aplicaciones
article_title: Ejemplos de aplicaciones para iOS
platform: iOS
page_order: 9
description: "Este artículo de referencia cubre aplicaciones de ejemplo para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ejemplos de aplicaciones

Para tu comodidad, los SDK de Braze incluyen aplicaciones de ejemplo en el repositorio. Cada una de estas aplicaciones es totalmente compilable, por lo que puedes probar las características de Braze a la vez que las implementas en tus propias aplicaciones. Probar el comportamiento dentro de tu propia aplicación en comparación con el comportamiento esperado y las rutas de código dentro de las aplicaciones de ejemplo es una forma excelente de depurar cualquier problema que puedas encontrarte.

## Construir aplicaciones de prueba
Hay varias aplicaciones de prueba disponibles en el [repositorio GitHub del SDK de](https://github.com/appboy/appboy-ios-sdk "iOSRepositorio GitHub de iOS de Appboy"). Sigue estas instrucciones para crear y ejecutar nuestras aplicaciones de prueba.

1. Crea un nuevo [espacio de trabajo]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) y anota la clave de API del identificador de la aplicación.
2. Coloca tu clave de API en el campo correspondiente del archivo `AppDelegate.m`.

Las notificaciones push para la aplicación de prueba iOS requieren una configuración adicional. Consulta nuestra [integración iOS Push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) para más detalles.

