---
nav_title: Registrar compras
article_title: Registro de compras para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Este artículo de referencia muestra cómo hacer un seguimiento de las compras e ingresos dentro de la aplicación y asignar propiedades de la compra en tu aplicación Android o FireOS."

---
 
# Registrar compras

> Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida. Este artículo de referencia muestra cómo hacer un seguimiento de las compras e ingresos dentro de la aplicación y asignar propiedades de la compra en tu aplicación Android o FireOS.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro [resumen de análisis]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

## Seguimiento de compras e ingresos

Para utilizar esta característica, llama a [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) después de realizar una compra con éxito en tu aplicación. Si el identificador del producto está vacío, la compra no se registrará en Braze.

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
Si pasas un valor de `10 USD` y una cantidad de `3`, eso se registrará en el perfil del usuario como tres compras de 10 dólares por un total de 30 dólares. Las cantidades deben ser inferiores o iguales a 100. Los valores de las compras pueden ser negativos.
{% endalert %}

### Añadir propiedades

Puedes añadir metadatos sobre las compras pasando una [matriz de propiedades del evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) o un objeto [Braze Properties](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) con la información de tu compra.

#### Formateo de objetos de propiedades Braze

Las propiedades se definen como pares clave-valor. Las claves son objetos de `String`, y los valores pueden ser objetos `String`, `int`, `float`, `boolean` o [`Date`](http://developer.android.com/reference/java/util/Date.html).

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

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) para más información.

### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la [documentación de la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

