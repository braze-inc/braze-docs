---
nav_title: 이벤트
article_title: 이벤트
page_order: 0
page_type: reference
description: "이 문서에서는 Braze의 다양한 이벤트(표준 이벤트, 구매 이벤트 및 커스텀 이벤트)와 그 목적에 대해 설명합니다."
---

# 이벤트 

> 이 페이지에서는 브레이즈의 다양한 이벤트와 그 목적에 대해 설명합니다.

Braze는 몇 가지 이벤트 유형을 사용하여 사용자 행동과 브랜드에 대한 참여를 종합적으로 파악할 수 있습니다. 각 유형의 이벤트는 고유한 목적을 가지고 있습니다:

- [표준 이벤트](#standard-events): 앱 또는 사이트에서 사용자 인게이지먼트에 대한 기본적인 이해를 제공합니다.
- [구매 이벤트](#purchase-events): 사용자 구매 행동을 이해하고 매출을 추적하는 데 중요합니다. 
- [커스텀 이벤트](#custom-events): 앱 또는 비즈니스에 고유한 사용자 행동에 대한 더 깊은 인사이트를 제공하세요.

이러한 다양한 유형의 이벤트를 추적함으로써 사용자에 대한 심층적인 이해를 바탕으로 마케팅 전략을 수립하고, 앱을 최적화하며, 보다 개인화된 사용자 경험을 제공할 수 있습니다. 자세히 알아봅시다!

## 표준 이벤트

Braze에서 표준 이벤트는 사용자가 앱 내에서 수행할 수 있는 미리 정의된 작업으로, Braze SDK를 통합한 후 Braze가 자동으로 추적합니다. 다음은 표준 이벤트의 몇 가지 예입니다:

- 앱 실행
- [구매](#purchase-events)
- 세션 시작
- 세션 종료
- 푸시 알림을 클릭함
- 이메일 열람됨

마케터로서, 이러한 표준 이벤트를 사용하여 사용자 행동 및 앱과의 인게이지먼트를 이해할 수 있습니다. 예를 들어 사용자가 앱을 얼마나 자주 실행하는지 또는 얼마나 많은 구매가 이루어지는지 확인할 수 있습니다. 이 정보는 타겟 마케팅 캠페인을 만들 때 매우 귀중할 수 있습니다.

표준 이벤트는 Braze에 의해 자동으로 추적되지만, 구매 이벤트, 커스텀 이벤트 및 커스텀 속성은 특정 요구와 목표에 따라 개발 팀이 설정해야 한다는 점을 유의하는 것이 중요합니다.

## 구매 이벤트

구매 이벤트는 사용자가 한 구매를 기록하고 추적하는 방법입니다. 기본적으로 Braze SDK를 통합한 후 사용할 수 있는 표준 이벤트 유형입니다. 이로 인해 구매 이벤트를 사용하여 구매를 추적할 때 Braze에서 직접 시간 경과에 따른 매출 및 다양한 매출 출처를 모니터링할 수 있습니다.

구매 이벤트는 구매에 대한 다음의 주요 정보를 기록합니다:

- 제품 ID (일반적으로 제품 이름 또는 카테고리)
- 통화
- 가격
- 수량

그런 다음 이 데이터를 사용하여 사용자의 생애주기 가치, 구매 빈도, 특정 구매 등을 기준으로 사용자를 세그먼트화할 수 있습니다.

Braze 또한 여러 통화로 구매를 지원합니다. 구매가 USD 이외의 통화로 보고된 경우, 보고된 날짜의 환율을 기준으로 Braze 대시보드에 USD로 표시됩니다.

자세한 내용을 보려면 전용 [구매 이벤트]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) 기사를 방문하세요.

{% details 구현 예시 %}

구매 이벤트를 실제로 구현하려면 Braze SDK를 앱과 통합해야 하므로 약간의 기술적 지식이 필요합니다. 고객 성공 매니저가 온보딩의 일환으로 이 과정을 귀하의 팀에게 안내할 것이지만, 일반적인 단계는 다음과 같습니다.

1. **Braze SDK를 통합하세요.** 이벤트를 로깅하기 전에 Braze SDK를 앱에 통합해야 합니다.
2. **구매 이벤트를 기록하세요.** SDK가 통합된 후 사용자가 앱에서 구매할 때마다 구매 이벤트를 기록할 수 있습니다. 이것은 일반적으로 구매가 완료될 때 호출되는 함수 또는 메서드에서 수행됩니다.

다음은 Swift를 사용하여 iOS 앱에서 구매 이벤트를 기록하는 방법의 예입니다:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

이 예에서 'product_name'은 구매한 제품의 이름, 'USD'는 구매 통화, '1.99'는 제품의 가격, '1'은 구매한 수량입니다.

{:start="3"}
3\. **구매 이벤트를 Braze 대시보드에서 보기:** 구매 이벤트가 기록된 후 Braze 대시보드에서 확인할 수 있습니다. 이 데이터를 사용하여 매출을 분석하고 사용자를 세그먼트화하는 등 다양한 작업을 수행할 수 있습니다.

기억하세요, 정확한 구현은 플랫폼(iOS, Android, 웹)과 앱의 특정 요구 사항에 따라 다를 수 있습니다. 

{% enddetails %}

## 사용자 지정 이벤트

커스텀 이벤트는 앱 또는 사이트 내에서 추적하려는 특정 작업을 기반으로 정의하는 이벤트입니다. Braze는 이러한 이벤트를 자동으로 추적하지 않으므로 Braze SDK 구현에서 이러한 이벤트를 수동으로 설정해야 합니다. 커스텀 이벤트는 사용자가 게임에서 레벨을 완료하는 것부터 고객 프로필 정보를 업데이트하는 것까지 무엇이든 될 수 있습니다.

다음은 Swift를 사용하여 iOS 앱에서 커스텀 이벤트를 기록하는 방법의 예입니다:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

이 예에서 "completed_level"은 사용자가 게임에서 레벨을 완료할 때 기록되는 커스텀 이벤트의 이름입니다. 그 커스텀 이벤트는 Braze의 고객 프로필에 기록되며, 이를 사용하여 캠페인을 트리거하고 메시징을 개인화할 수 있습니다.

자세한 내용을 보려면 전용 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 기사를 방문하세요.

{% details 구현 예시 %}

구매 이벤트와 마찬가지로, 커스텀 이벤트는 추가 설정이 필요합니다. 다음은 Braze에서 커스텀 이벤트를 구현하는 일반적인 프로세스입니다:

1. **Braze SDK를 통합하세요.** 이벤트를 기록하려면 먼저 Braze SDK를 앱에 통합해야 합니다.
2. **커스텀 이벤트를 정의하세요.** 앱에서 커스텀 이벤트로 추적하려는 작업을 결정하세요. 이것은 사용자가 게임에서 레벨을 완료하거나, 고객 프로필을 업데이트하거나, 사용자가 특정 유형의 구매를 하는 것과 같이 앱에 중요한 모든 것이 될 수 있습니다.
3. **커스텀 이벤트를 기록하세요.** 커스텀 이벤트를 정의한 후에는 앱의 코드에 기록할 수 있습니다. 이것은 일반적으로 작업이 발생할 때 호출되는 함수 또는 메서드에서 수행됩니다.

다음은 Swift를 사용하여 iOS 앱에서 커스텀 이벤트를 기록하는 방법의 예입니다:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

이 예에서, "updated_profile"은 사용자가 프로필을 업데이트할 때 기록되는 커스텀 이벤트의 이름입니다.

{:start="4"}
4\. **사용자 정의 이벤트에 속성 추가 (선택 사항):** 추가적인 세부 사항을 캡처하려면 커스텀 이벤트에 속성을 추가할 수 있습니다. 이것은 이벤트를 기록할 때 속성의 사전을 전달하여 수행됩니다.

다음은 Swift를 사용하여 iOS 앱에서 속성이 있는 커스텀 이벤트를 기록하는 예입니다.

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

이 예제에서 커스텀 이벤트에는 "속성정보 이름"이라는 속성정보가 있으며 값은 "속성정보 값"입니다.

{:start="5"}
5\. **커스텀 이벤트를 Braze 대시보드에서 보기:** 커스텀 이벤트가 기록된 후 Braze 대시보드에서 확인할 수 있습니다. 이 데이터를 사용하여 사용자 행동을 분석하고, 사용자를 세그먼트하는 등 다양한 작업을 수행할 수 있습니다.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


