---
nav_title: Seguimiento de ubicación
article_title: Seguimiento de ubicación para Windows Universal
platform: Windows Universal
page_order: 6
description: "Este artículo de referencia explica cómo añadir el seguimiento de ubicación a tu aplicación Windows Universal."
tool: Location
hidden: true
---

# seguimiento de ubicación
{% multi_lang_include archive/windows_deprecation.md %}

1. Asegúrate de que en tu archivo `Package.appxmanifest` está marcada la casilla `location`.
2. Si quieres desactivar el seguimiento de ubicación automático, configura `<DisableLocationCollection>false</DisableLocationCollection>` en `true` en tu `AppboyConfiguration.xml`.
