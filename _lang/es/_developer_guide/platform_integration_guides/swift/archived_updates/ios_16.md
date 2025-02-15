---
nav_title: Guía de actualización a iOS 16
article_title: Guía de actualización a iOS 16
page_order: 7
platform: 
  - iOS
description: "Este artículo de referencia trata sobre iOS 16, cómo actualizar versiones, actualizaciones del SDK y mucho más."
hidden: true
noindex: true
---

# Guía de actualización del SDK de iOS 16

> En esta guía se describen los cambios relevantes introducidos en iOS 16 (2022) y el impacto en tu integración del SDK de Braze para iOS. Consulta [las notas de la versión de iOS](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes) 16 para obtener una guía completa de migración.

## Cambios en iOS 16

### Notificación push web de Safari {#safari-web-push}

Apple ha anunciado dos cambios en su funcionalidad de notificación push web.

#### Notificación push web de escritorio (MacOS) {#macos-push}

Anteriormente, Apple admitía notificaciones push en macOS (escritorio) utilizando sus propias API push de Safari.

A partir de macOS Ventura (publicado el 24 de octubre de 2022), [Safari ha añadido compatibilidad](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) con las API de notificación push web, además de las notificaciones push de Safari. Se trata de un estándar de API entre navegadores que se utiliza en otros navegadores populares.

Si ya estás enviando notificaciones push web para Safari a través de Braze, no es necesario que realices ningún cambio.

#### Notificación push web móvil (iOS y iPadOS) {#ios-push}

Anteriormente, Safari en iPhone y iPad no permitía recibir notificaciones push.

En 2023, Apple añadirá soporte para notificación push web en dispositivos iPhone y iPad a través de Safari.

Braze admitirá esta nueva notificación push web de iOS y iPadOS sin necesidad de aplicar cambios ni actualizaciones adicionales.

## Preparación para iOS 16 {#next-steps}

Aunque no necesitas actualizar tu SDK de Braze para iOS a la versión iOS 16, hay otras dos actualizaciones interesantes:

1. Braze ha lanzado un [nuevo SDK Swift](https://github.com/braze-inc/braze-swift-sdk). Esto aporta un mayor rendimiento, nuevas características y muchas mejoras.
2. ¡Nuestro SDK Swift de Braze admite una nueva [ característica push primer "sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)"!

