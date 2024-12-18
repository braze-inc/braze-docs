---
nav_title: 구매 기록
article_title: iOS 구매 기록
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS 애플리케이션에서 인앱 구매 및 매출을 추적하고 구매 속성정보를 할당하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 구매 기록

인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

구현하기 전에 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)의 참고 사항과 함께 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션 예제를 검토하세요.

## 구매 및 수익 추적

이 기능을 사용하려면 앱에서 구매에 성공한 후 이 메서드 호출을 추가합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- 지원되는 통화 기호는 다음과 같습니다: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK 등을 지원합니다.
  - 제공된 다른 통화 기호를 사용하면 경고가 기록되고, SDK에서 다른 조치를 취하지 않습니다.
- 제품 ID는 최대 255자까지 입력할 수 있습니다.
- 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않는다는 점에 유의하세요.

### 속성정보 추가 {#properties-purchases}

구매에 대한 메타데이터는 [이벤트 속성정보 배열]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects)을 전달하거나 `NSNumber`, `NSString` 또는 `NSDate` 값을 채운 `NSDictionary`를 전달하여 추가할 수 있습니다.

자세한 내용은 [iOS 클래스 문서로그구매](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc "w/프로퍼티 클래스 문서를") 참조하세요.

### 수량 추가
고객이 한 번의 결제에서 동일한 제품을 여러 번 구매하는 경우 구매에 수량을 추가할 수 있습니다. 수량을 `NSUInteger` 으로 전달하면 됩니다.

* SDK가 구매를 기록하려면 수량을 [0, 100] 범위로 입력해야 합니다.
* 수량 입력이 없는 메서드에서 기본 수량 값은 1입니다.
* 수량 입력이 있는 메서드에는 기본값이 없으며, **반드시** SDK가 구매를 기록할 수 있도록 수량 입력을 수신해야 합니다.

자세한 내용은 [iOS 클래스 문서로그구매](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa "w/수량 클래스 문서를") 참조하세요.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
10 USD의 가격과 3개의 수량을 전달하면 고객 프로필에 10 USD 항목의 3번 구매로 총 30 USD가 기록됩니다.
{% endalert %}

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

