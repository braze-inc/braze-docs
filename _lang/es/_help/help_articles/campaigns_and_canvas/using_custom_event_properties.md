---
nav_title: Registro de propiedades del evento personalizadas
article_title: Registro de propiedades del evento personalizadas
page_order: 3
page_type: solution
description: "Este artículo de ayuda te guía a través de tres comprobaciones importantes para asegurarte de que tus eventos personalizados se registran como esperas."
tool: 
- Campaigns
- Canvas
---

# Registro de propiedades del evento personalizado

Hay tres comprobaciones importantes que debes llevar a cabo para asegurarte de que tus eventos personalizados se registran como esperas:

* [Establecer qué eventos se registran](#verify-events)
* [Verificar registro](#verify-log)
* [Verificar los valores](#verify-values)

## Verificar propiedades del evento personalizado

[Las propiedades del evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) son metadatos que describen eventos personalizados. Se pueden registrar varias propiedades cada vez que se registra un evento personalizado.

### Verificar eventos

Comprueba con tus desarrolladores qué propiedades del evento están siendo objeto de seguimiento. Ten en cuenta que todas las propiedades del evento distinguen entre mayúsculas y minúsculas. Para obtener información adicional sobre el seguimiento de eventos personalizados, consulta estos artículos basados en tu plataforma:

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Verificar registro

Para confirmar que las propiedades del evento se han seguido correctamente, puedes ver todas las propiedades del evento desde la página **Eventos personalizados**.

1. Navegando hasta **Configuración de datos** > **Eventos personalizados**.
2. Localiza tu evento personalizado en la lista.
3. Para tu evento, haz clic en **Gestionar propiedades**. Esto te mostrará los nombres de las propiedades asociadas a un evento.

### Verificar los valores

Después de añadir tu usuario como usuario de prueba, sigue estos pasos para verificar tus valores: 

1. Realiza el evento personalizado dentro de la aplicación.
2. Espera unos 10 segundos a que se vacíen los datos.
3. Actualiza el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para ver el evento personalizado y el valor de la propiedad del evento que se pasó con él.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 10 de abril de 2023_

