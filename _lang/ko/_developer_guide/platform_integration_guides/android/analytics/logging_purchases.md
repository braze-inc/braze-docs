---
nav_title: 구매 기록
article_title: Android 및 FireOS용 구매 기록
platform: 
  - Android
  - FireOS
page_order: 4
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 인앱 구매 및 매출을 추적하고 구매 속성정보를 할당하는 방법을 보여줍니다."

---
 
# 구매 기록

> 인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다. 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 인앱 구매 및 매출을 추적하고 구매 속성정보를 할당하는 방법을 보여줍니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

구현하기 전에 [분석 개요]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요.

## 구매 및 수익 추적

이 기능을 사용하려면 앱에서 구매한 후 [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html)를 호출합니다. 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않습니다.

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
`10 USD`의 가격과 `3`개의 수량을 전달하면 고객 프로필에 10 USD 항목의 3번 구매로 총 30 USD가 기록됩니다. 수량은 100보다 작거나 같아야 합니다. 구매 금액은 음수일 수 있습니다.
{% endalert %}

### 속성정보 추가

[이벤트 속성 배열]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) 또는 구매 정보와 함께 [Braze 속성](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) 개체를 전달하여 구매에 대한 메타데이터를 추가할 수 있습니다.

#### 브레이즈 속성 개체 서식 지정

속성은 키-값 쌍으로 정의됩니다. 키는 `String` 오브젝트이고 값은 `String`, `int`, `float`, `boolean` 또는 [`Date`](http://developer.android.com/reference/java/util/Date.html) 오브젝트일 수 있습니다.

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

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html)를 참조하세요.

### 주문 수준에서 구매 기록
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

### 예약 키

다음 키는 예약되어 있으며 구매 속성으로 사용할 수 없습니다:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

REST API를 사용하여 구매 내역을 기록할 수도 있습니다. 자세한 내용은 [사용자 API 설명서를]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 참조하세요.

