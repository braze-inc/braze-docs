# Rastreamento de eventos personalizados

> Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e segmentar seus usuários por suas ações no dashboard. Este artigo de referência aborda como adicionar e rastrear eventos personalizados para seu aplicativo Android ou FireOS.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossa [visão geral da análise de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Adição de um evento personalizado

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

Consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) para obter mais informações.

### Adição de propriedades

Você pode adicionar metadados sobre eventos personalizados passando um [objeto de propriedades do Braze](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) com seu evento personalizado.

As propriedades são definidas como pares de valores-chave. As chaves são objetos `String` e os valores podem ser `String`, `int`, `float`, `boolean`, ou [`Date`](http://developer.android.com/reference/java/util/Date.html) objetos.

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

### Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de eventos personalizados:

- `time`
- `event_name`

Consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html) para obter mais informações.

