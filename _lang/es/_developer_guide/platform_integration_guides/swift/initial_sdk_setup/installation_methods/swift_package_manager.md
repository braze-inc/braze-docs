---
nav_title: Swift Package Manager
article_title: Integración de Swift Package Manager para iOS
platform: Swift
page_order: 1
description: "Este tutorial cubre la instalación del SDK Swift de Braze utilizando Swift Package Manager para iOS."

---

# Integración con Swift Package Manager

> La instalación del SDK de Swift mediante [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatiza la mayor parte del proceso de instalación por ti. Antes de iniciar este proceso, comprueba la [información de la versión](https://github.com/braze-inc/braze-swift-sdk#version-information) para asegurarte de que tu entorno es compatible con Braze.

## Añadir la dependencia a tu proyecto

### Importar versión del SDK

Abre tu proyecto y ve a la configuración del mismo. Selecciona la pestaña **Paquetes Swift** y haz clic en el botón <i class="fas fa-plus"></i> añadir debajo de la lista de paquetes.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
A partir de la versión 7.4.0, el SDK Swift de Braze tiene canales de distribución adicionales como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) y [XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si quieres utilizar cualquiera de estos formatos en su lugar, sigue las instrucciones de instalación de su repositorio respectivo.
{% endalert %}

Introduce la URL de nuestro repositorio del SDK Swift para iOS `https://github.com/braze-inc/braze-swift-sdk` en el campo de texto. En la sección **Regla de dependencia**, selecciona la versión del SDK. Por último, haz clic en **Añadir paquete**.

![]({% image_buster /assets/img/importsdk_example.png %})

### Seleccionar paquetes

El SDK de Swift de Braze separa las características en bibliotecas independientes para proporcionar a los desarrolladores un mayor control sobre qué características importar a sus proyectos.

| Paquete | Detalles |
| ------- | ------- |
| `BrazeKit` | Biblioteca principal del SDK que proporciona soporte para análisis y notificaciones push. |
| `BrazeLocation` | Biblioteca de ubicación que proporciona soporte para el análisis de la ubicación y la supervisión del geovallado. |
| `BrazeUI` | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación y tarjetas de contenido. |
{: .ws-td-nw-1}

#### Bibliotecas de extensión

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) y [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) son módulos de extensión que proporcionan funcionalidad adicional y no deben añadirse directamente al objetivo principal de tu aplicación. En su lugar, sigue las guías enlazadas para integrarlos por separado en sus respectivas extensiones de destino.
{% endalert %}

| Paquete | Detalles |
| ------- | ------- |
| `BrazeNotificationService` | Biblioteca de extensión de servicios de notificación que proporciona soporte para notificaciones push enriquecidas. |
| `BrazePushStory` | Biblioteca de extensión de contenido de notificaciones que ofrece soporte para historias push. |
{: .ws-td-nw-1}

 Selecciona el paquete que mejor se adapte a tus necesidades y haz clic en **Añadir paquete**. Asegúrate de seleccionar `BrazeKit` como mínimo.

![]({% image_buster /assets/img/add_package.png %})

## Próximos pasos

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

