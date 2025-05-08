---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para Roku
platform: Roku
page_order: 2
page_type: reference
description: "Esta página cubre los métodos para grabar eventos personalizados para Roku a través del SDK de Braze."

---

# Seguimiento de eventos personalizados

> Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Añadir un evento personalizado

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### Añadir propiedades

Puedes añadir metadatos sobre eventos personalizados pasando un diccionario de propiedades con tu evento personalizado.

Las propiedades se definen como pares clave-valor.  Las claves son objetos `String` y los valores pueden ser `String` o `Integer`.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
