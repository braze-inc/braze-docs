---
nav_title: 구매 기록
article_title: Braze SDK를 통해 구매를 기록하기
page_order: 3.2
description: "Braze SDK를 통해 구매를 기록하는 방법을 배우세요."

---

# 구매 기록

> Braze SDK를 통해 인앱 구매를 기록하는 방법을 배우세요. 이를 통해 시간 경과에 따른 수익과 출처를 파악할 수 있습니다. 이를 통해 커스텀 이벤트, 커스텀 속성 및 구매 이벤트를 사용하여 사용자를 [생애주기 가치]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking)에 따라 세그먼트화할 수 있습니다.

{% alert note %}
나열되지 않은 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 구매 및 수익 기록하기

구매 및 수익을 기록하려면 앱에서 성공적인 구매 후 `logPurchase()`를 호출하세요. 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않습니다.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
표준 웹 SDK 구현을 위해 다음 메서드를 사용할 수 있습니다:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

대신 Google Tag Manager를 사용하려면 **구매** 태그 유형을 사용하여 [`logPurchase` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)를 호출할 수 있습니다. 이 태그를 사용하여 선택적으로 구매 속성정보를 포함한 Braze에 대한 구매를 추적합니다. 그렇게 하려면:

1. **제품 ID** 및 **가격** 필드는 필수 입력 사항입니다.
2. **행 추가** 버튼을 사용하여 구매 속성을 추가합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형', '외부 ID', '가격', '통화 코드', '수량', '구매 속성' 등입니다.]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab 유니티 %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}

{% tab 언리얼 엔진 %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID`는 최대 255자만 가질 수 있습니다. 또한, 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않습니다.
{% endalert %}

### 속성정보 추가

`Int`, `Double`, `String`, `Bool` 또는 `Date` 값으로 채워진 사전을 전달하여 구매에 대한 메타데이터를 추가할 수 있습니다.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
표준 웹 SDK 구현을 위해 다음 메서드를 사용할 수 있습니다:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

사이트가 표준 [이커머스 이벤트](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) 데이터 레이어 항목을 사용하여 Google Tag Manager에 구매를 기록하는 경우, **이커머스 구매** 태그 유형을 사용할 수 있습니다. 이 작업 유형은 `items`의 목록에 전송된 각 항목에 대한 별도의 '구매'를 Braze에 기록합니다.

구매 속성정보 목록에서 키를 지정하여 구매 속성정보로 포함할 추가 속성정보 이름을 지정할 수도 있습니다. Braze는 목록에 추가하는 모든 구매 자산에 대해 기록 중인 개별 `item` 내에서 확인합니다.

예를 들어, 다음 전자상거래 페이로드가 주어졌습니다:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand` 및 `item_name`만 구매 속성정보로 전달하려면 구매 속성정보 테이블에 이 두 필드를 추가하면 됩니다. 속성을 제공하지 않으면 구매 속성이 전송되지 않습니다. [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) 호출로 전송되지 않습니다.
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab 유니티 %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}

{% tab 언리얼 엔진 %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### 수량 추가

기본값으로, `quantity`은 `1`로 설정됩니다. 그러나 고객이 단일 체크아웃에서 동일한 구매를 여러 번 하는 경우 구매에 수량을 추가할 수 있습니다. 수량을 추가하려면 `[0, 100]`의 범위 내에 있는 `quantity`에 `Int` 값을 전달하십시오.

### REST API 사용

REST API를 사용하여 구매 내역을 기록할 수도 있습니다. 자세한 정보는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하십시오.

## 주문 기록

제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

## 예약 키

다음 키는 예약되어 있으며 구매 속성으로 사용할 수 없습니다:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## 지원되는 통화

이들은 지원되는 통화 기호입니다. 제공하는 다른 통화 기호는 경고를 기록하고 구매는 Braze에 기록되지 않습니다.

- `USD`
- `CAD`
- `EUR`
- `GBP`
- `JPY`
- `AUD`
- `CHF`
- `NOK`
- `MXN`
- `NZD`
- `CNY`
- `RUB`
- `TRY`
- `INR`
- `IDR`
- `ILS`
- `SAR`
- `ZAR`
- `AED`
- `SEK`
- `HKD`
- `SPD`
- `DKK`
