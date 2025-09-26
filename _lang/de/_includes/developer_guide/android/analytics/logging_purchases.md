 
# Einkäufe protokollieren

> Erfassen Sie In-App-Käufe, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg verfolgen und Ihre Nutzer nach ihrem Lifetime-Value segmentieren können. Dieser referenzierte Artikel zeigt, wie Sie In-App-Käufe und Umsätze tracken und Kauf-Details in Ihrer Android- oder FireOS-Anwendung zuweisen können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Vor der Implementierung sollten Sie sich in unserer [Analytics-Übersicht]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) Beispiele für die Segmentierungsoptionen ansehen, die angepasste Events, angepasste Attribute und Kauf-Events bieten.

## Verfolgung von Käufen und Einnahmen

Um dieses Feature zu nutzen, rufen Sie [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) nach einem erfolgreichen Kauf in Ihrer App an. Wenn der Bezeichner des Produkts leer ist, wird der Kauf nicht in Braze protokolliert.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie einen Wert von `10 USD` und eine Menge von `3` eingeben, wird dies im Profil des Nutzers:in als drei Käufe zu je 10 Dollar für insgesamt 30 Dollar gespeichert. Die Mengen müssen kleiner als oder gleich 100 sein. Die Werte von Käufen können negativ sein.
{% endalert %}

### Hinzufügen von Eigenschaften

Sie können Metadaten über Käufe hinzufügen, indem Sie entweder ein [Event-Eigenschaften-Array]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) oder ein [Braze Properties-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) mit Ihren Kaufinformationen übergeben.

#### Braze Eigenschaften Objektformatierung

Eigenschaften werden als Schlüssel-Werte-Paare definiert. Schlüssel sind `String`-Objekte und die Werte können `String`-, `int`-, `float`-, `boolean`- oder [`Date`](http://developer.android.com/reference/java/util/Date.html)-Objekte sein.

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in unserem [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html).

### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als Kaufeigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [Benutzer-API-Dokumentation]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

