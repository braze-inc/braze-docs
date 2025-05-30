# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord. Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application Android ou FireOS.

Avant la mise en œuvre, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans notre [aperçu de l'analyse/analytique]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions d'appellation des événements]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

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

Pour plus d’informations, reportez-vous à notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html).

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en transmettant un [objet de propriétés Braze](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des objets de type `String` et les valeurs peuvent être des objets de type `String`, `int`, `float`, `boolean` ou [`Date`](http://developer.android.com/reference/java/util/Date.html).

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

### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’événement personnalisé :

- `time`
- `event_name`

Pour plus d’informations, reportez-vous à notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html).

