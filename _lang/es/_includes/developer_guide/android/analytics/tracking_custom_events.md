# Seguimiento de eventos personalizados

> Puedes grabar eventos personalizados en Braze para conocer mejor los patrones de uso de tu aplicación y segmentar a tus usuarios por sus acciones en el panel. Este artículo de referencia explica cómo añadir y seguir eventos personalizados para tu aplicación Android o FireOS.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro [resumen de análisis]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Añadir un evento personalizado

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```

{% endtab %}
{% endtabs %}

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) para más información.

### Añadir propiedades

Puedes añadir metadatos sobre eventos personalizados pasando un [objeto de propiedades Braze](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) con tu evento personalizado.

Las propiedades se definen como pares clave-valor. Las claves son objetos de `String`, y los valores pueden ser objetos `String`, `int`, `float`, `boolean` o [`Date`](http://developer.android.com/reference/java/util/Date.html).

{% tabs %}
{% tab JAVA %}

```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```

{% endtab %}
{% endtabs %}

### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades del evento personalizado:

- `time`
- `event_name`

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) para más información.

