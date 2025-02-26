---
nav_title: Integración de balizas
article_title: Integración de balizas para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Este artículo de referencia explica cómo registrar eventos personalizados utilizando Gimbal Beacons para Android o FireOS."

---

# Integración de balizas

> Este artículo te explicará cómo integrar tipos específicos de balizas con Braze para permitir la segmentación y la mensajería.

## Balizas Gimbal

Una vez que tengas tus balizas Gimbal configuradas e integradas en tu aplicación, puedes registrar eventos personalizados para cosas como el inicio o el fin de una visita, o el avistamiento de una baliza. También puedes registrar propiedades de estos eventos, como el nombre del lugar o el tiempo de permanencia.

Para registrar un evento personalizado cuando un usuario entra en un lugar, incluye este código en el método `onVisitStart`:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

La página `requestImmediateDataFlush` verifica que tu evento se registrará aunque la aplicación esté en segundo plano, y el mismo proceso puede aplicarse para abandonar una ubicación. Ten en cuenta que la actividad y el contexto en el que trabajes pueden cambiar exactamente la forma de integrar las líneas `logCustomEvent` y `requestImmediateDataFlush`. Además, ten en cuenta que este código creará e incrementará un evento personalizado único para cada nuevo lugar en el que entre el usuario. Como tal, si anticipas que crearás más de 50 lugares, te recomendamos que crees un evento personalizado genérico llamado «Lugar al que ingresó» y que incluyas el nombre del lugar como propiedad del evento.
