---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Tracking von angepassten Events für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Dieser referenzierende Artikel beschreibt, wie Sie angepasste Events für Ihre Android- oder FireOS-Anwendung hinzufügen und tracken können."

---

# Tracking von angepassten Events

> Sie können angepasste Events in Braze aufzeichnen, um mehr über das Nutzungsverhalten Ihrer App zu erfahren und Ihre Nutzer:innen nach ihren Aktionen auf dem Dashboard zu segmentieren. Dieser referenzierende Artikel beschreibt, wie Sie angepasste Events für Ihre Android- oder FireOS-Anwendung hinzufügen und tracken können.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsmöglichkeiten durch angepasste Events, angepasste Attribute und Kauf-Events in unserer [Analytics-Übersicht]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Hinzufügen eines angepassten Events

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

Weitere Informationen finden Sie in unserem [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html).

### Hinzufügen von Eigenschaften

Sie können Metadaten zu angepassten Events hinzufügen, indem Sie ein [Braze-Eigenschaften-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) mit Ihrem angepassten Event übergeben.

Eigenschaften werden als Schlüssel-Werte-Paare definiert. Schlüssel sind `String`-Objekte und die Werte können `String`-, `int`-, `float`-, `boolean`- oder [`Date`](http://developer.android.com/reference/java/util/Date.html)-Objekte sein.

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

### Reservierte Schlüssel

Die folgenden Schlüssel sind reserviert und können nicht als benutzerdefinierte Ereigniseigenschaften verwendet werden:

- `time`
- `event_name`

Weitere Informationen finden Sie in unserem [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html).

