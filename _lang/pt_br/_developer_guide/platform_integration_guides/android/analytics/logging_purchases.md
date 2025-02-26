---
nav_title: Registro de compras
article_title: Registro de compras para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Este artigo de referência mostra como rastrear compras e receitas in-app e atribuir propriedades de compra em seu aplicativo Android ou FireOS."

---
 
# Registro de compras

> Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles. Este artigo de referência mostra como rastrear compras e receitas in-app e atribuir propriedades de compra em seu aplicativo Android ou FireOS.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossa [visão geral da análise de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

## Rastreamento de compras e receitas

Para usar esse recurso, ligue para [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) após uma compra bem-sucedida em seu app. Se o identificador do produto estiver vazio, a compra não será registrada no Braze.

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
Se você passar um valor de `10 USD` e uma quantidade de `3`, isso será registrado no perfil do usuário como três compras de 10 dólares, totalizando 30 dólares. As quantidades devem ser menores ou iguais a 100. Os valores das compras podem ser negativos.
{% endalert %}

### Adicionando propriedades

Você pode adicionar metadados sobre as compras passando um [vetor de objeto de propriedade de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) ou um objeto [Braze Properties](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) com as informações da compra.

#### Formatação de objetos de propriedades do Braze

As propriedades são definidas como pares de valores-chave. As chaves são objetos `String` e os valores podem ser `String`, `int`, `float`, `boolean`, ou [`Date`](http://developer.android.com/reference/java/util/Date.html) objetos.

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

Consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) para obter mais informações.

### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

Também é possível usar nossa API REST para registrar compras. Consulte a [documentação da API do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

