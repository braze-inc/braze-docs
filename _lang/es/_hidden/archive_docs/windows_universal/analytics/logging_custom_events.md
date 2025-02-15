---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para Windows Universal
platform: Windows Universal
page_order: 2
description: "Este artículo de referencia explica cómo realizar el seguimiento de eventos personalizados en la plataforma Windows Universal."
hidden: true
---

# Seguimiento de eventos personalizados
{% multi_lang_include archive/windows_deprecation.md %}

Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

Todos los eventos se registran utilizando `EventLogger`, que es una propiedad expuesta en IAppboy. Para obtener una referencia a `EventLogger`, llama a `Appboy.SharedInstance.EventLogger`. Puedes utilizar los siguientes métodos para hacer un seguimiento de las acciones importantes de los usuarios y de los eventos personalizados:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
