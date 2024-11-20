---
nav_title: Seguimiento de eventos personalizados
article_title: Seguimiento de eventos personalizados para Web
platform: Web
page_order: 2
page_type: reference
description: "Este artículo explica cómo hacer un seguimiento de los eventos personalizados y añadir propiedades a esos eventos para la Web."

---

# Seguimiento de eventos personalizados

> Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios según sus acciones en el panel.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices). También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

Consulta la documentación [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) para más información.

## Añadir propiedades {#properties-events}

Opcionalmente, puedes añadir metadatos sobre eventos personalizados pasando un objeto de propiedades con tu evento personalizado.

Las propiedades se definen como pares clave-valor. Las claves son cadenas y los valores pueden ser `string`, `numeric`, `boolean`, u [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) objetos.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

Consulta la [documentación de`logCustomEvent()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) para obtener más información.

