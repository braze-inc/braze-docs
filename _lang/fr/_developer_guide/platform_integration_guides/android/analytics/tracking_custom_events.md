---
nav_title: Suivre les événements personnalisés
article_title: Suivre des événements personnalisés pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application Android ou FireOS."

---

# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord. Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application Android ou FireOS.

Avant l’implémentation, assurez-vous d’étudier des exemples d’options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans notre [aperçu d’analytique][0] ainsi que nos remarques sur les [conventions de dénominations des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

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

Consultez notre [KDoc][2] pour plus d’informations.

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en transmettant un [objet de propriétés Braze][4] avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des objets `String` et les valeurs peuvent être des objets `String`, `int`, `float`, `boolean`, ou [`Date`][3].

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

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés de l’événement personnalisées :

- `time`
- `event_name`

Consultez notre [KDoc][2] pour plus d’informations.

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html
[3]: http://developer.android.com/reference/java/util/Date.html
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
