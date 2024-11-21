---
nav_title: compatibilidad con visionOS
article_title: compatibilidad con visionOS
page_order: 7.2
platform: 
  - iOS
description: "Este artículo trata de las características compatibles con visionOS."
---

# compatibilidad con visionOS

> A partir de [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), puedes aprovechar Braze con [visionOS](https://developer.apple.com/visionos/), la plataforma de computación espacial de Apple para el Apple Vision Pro. Para ver una aplicación visionOS de ejemplo que utiliza Braze, consulta [Aplicaciones de ejemplo]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/).

## Características totalmente compatibles

La mayoría de las características disponibles en iOS también están disponibles en visionOS, entre ellas:

- Análisis (sesiones, eventos personalizados, compras, etc.)
- Mensajería dentro de la aplicación (modelos de datos e interfaz de usuario)
- Tarjetas de contenido (modelos de datos e interfaz de usuario)
- Notificaciones push (visibles para el usuario con botones de acción y notificaciones silenciosas)
- Conmutador de características
- Análisis de ubicación

## Características parcialmente compatibles

Algunas características solo son parcialmente compatibles con visionOS, pero es probable que Apple lo solucione en el futuro:

- Notificaciones push enriquecidas
  - Se admiten imágenes.
  - Los GIFs y videos muestran la miniatura de vista previa, pero no se pueden reproducir.
  - No se admite la reproducción de audio.
- Historias push
  - Se puede desplazar y seleccionar la página de historias push.
  - No es posible navegar entre páginas de historias push utilizando **Siguiente**.

## Funciones no compatibles

- No se admite la monitorización de geovallas. Apple no ha puesto a disposición de visionOS las API centrales de ubicación para el seguimiento de regiones.
- No se admiten Actividades en vivo. Actualmente, ActivityKit solo está disponible en iOS y iPadOS.
