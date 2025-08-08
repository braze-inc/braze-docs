---
nav_title: Comprobación de los datos de ubicación
article_title: Comprobación de los datos de ubicación
page_order: 1
page_type: solution
description: "Este artículo de ayuda te guía a través de comprobaciones rápidas que pueden ayudarte si no hay usuarios con ubicaciones disponibles."
tool: Location
---

# Comprobación de los datos de ubicación

Braze captura la ubicación más reciente de un usuario de forma predeterminada a través de su SDK. Esto suele significar que la "ubicación reciente" es la ubicación desde la que tu usuario utilizó tu aplicación más recientemente. Si envías a Braze datos de ubicación en segundo plano, es posible que dispongas de datos más granulares.

Si no hay usuarios con ubicaciones disponibles, dos comprobaciones rápidas pueden ayudarte a confirmar la recopilación de datos y la transferencia de fechas.

## Recopilación de datos

Confirma que tu aplicación está recopilando datos de ubicación:

- Para iOS, esto significa que los usuarios optan por compartir sus datos de ubicación a través de un aviso en algún punto del recorrido del usuario. 
- Para Android, confirma que tu aplicación pide permisos de ubicación fina o gruesa en la instalación.

Para ver si los datos de ubicación del usuario se envían a Braze, utiliza el filtro **Ubicación disponible**. Este filtro te permite ver el porcentaje de usuarios con una "ubicación más reciente".

![]({% image_buster /assets/img_archive/trouble7.png %})

## Transferencia de datos

Confirma que tus desarrolladores pasan datos de ubicación a Braze. Normalmente, el SDK gestiona automáticamente la transmisión de datos de ubicación después de que el usuario dé sus permisos, pero es posible que tus desarrolladores hayan desactivado el seguimiento de ubicación en Braze. Puedes encontrar más información sobre el seguimiento de ubicación en:
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 16 de noviembre de 2022_

