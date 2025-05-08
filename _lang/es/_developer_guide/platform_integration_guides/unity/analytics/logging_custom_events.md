---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "Este artículo de referencia explica cómo registrar eventos personalizados en la plataforma Unity."

---

# Seguimiento de eventos personalizados

> Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Mejores prácticas][4]. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze también admite añadir metadatos sobre eventos personalizados pasando un `Dictionary` de propiedades del evento:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## API REST

También puedes utilizar nuestra API REST para registrar eventos. Consulta la documentación de [la API de usuario][5] para más detalles.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
