---
nav_title: 동작
article_title: 콘텐츠 카드의 동작 사용자 지정
page_order: 2
description: "이 구현 가이드에서는 콘텐츠 카드의 동작 변경, 페이로드에 키-값 페어와 같은 추가 항목 추가, 일반적인 사용자 지정에 대한 레시피에 대해 설명합니다."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 콘텐츠 카드의 동작 사용자 지정

> 이 구현 가이드에서는 콘텐츠 카드의 동작 변경, 페이로드에 키-값 페어와 같은 추가 항목 추가, 일반적인 사용자 지정에 대한 레시피에 대해 설명합니다. 콘텐츠 카드 유형 전체 목록은 [콘텐츠 카드 정보를]({{site.baseurl}}/developer_guide/content_cards/) 참조하세요. 

## 키-값 쌍

Braze를 사용하면 키-값 페어를 사용하여 콘텐츠 카드를 통해 사용자 기기에 추가 데이터 페이로드를 전송할 수 있습니다. 이를 통해 내부 지표를 추적하고, 앱 콘텐츠를 업데이트하고, 속성을 사용자 지정할 수 있습니다. [대시보드를 사용하여 키-값 쌍을 추가합니다]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional). 
 
{% alert note %}
중첩된 JSON 값을 키-값 페어로 전송하는 것은 권장하지 않습니다. 대신 JSON을 보내기 전에 평탄화하세요.
{% endalert %}

{% tabs %}
{% tab Android %}

키-값 쌍은 <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> 객체에 `extras` 로 저장됩니다. 애플리케이션에서 추가 처리를 위해 카드와 함께 데이터를 전송하는 데 사용할 수 있습니다. <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a>를 호출하여 이러한 값에 액세스합니다.

{% endtab %}
{% tab iOS %}

키-값 쌍은 <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> 객체에 `extras` 로 저장됩니다. 애플리케이션에서 추가 처리를 위해 카드와 함께 데이터를 전송하는 데 사용할 수 있습니다. <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a>를 호출하여 이러한 값에 액세스합니다.

{% endtab %}
{% tab 웹 %}

키-값 쌍은 <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> 객체에 `extras` 로 저장됩니다. 애플리케이션에서 추가 처리를 위해 카드와 함께 데이터를 전송하는 데 사용할 수 있습니다. `card.extras`를 호출하여 이러한 값에 액세스합니다.

{% endtab %}
{% endtabs %}

{% alert tip %}
마케팅 팀과 개발자 팀이 어떤 키-값 페어를 사용할지 조율하는 것이 중요합니다(예: `feed_type = brand_homepage`). 마케터가 Braze 대시보드에 입력하는 키-값 페어는 개발자가 앱 로직에 빌드하는 키-값 페어와 정확히 일치해야 하기 때문입니다.
{% endalert %}

## 보조 콘텐츠로서의 콘텐츠 카드

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

콘텐츠 카드를 기존 피드에 원활하게 혼합하여 여러 피드의 데이터를 동시에 로드할 수 있습니다. 이렇게 하면 Braze 콘텐츠 카드와 기존 피드 콘텐츠가 일관된 조화로운 환경을 만들 수 있습니다.

오른쪽 예제는 로컬 데이터와 Braze에서 제공하는 콘텐츠 카드를 통해 채워지는 하이브리드 항목 목록이 포함된 피드를 보여줍니다. 이를 통해 콘텐츠 카드를 기존 콘텐츠와 구분할 수 있습니다.

### API 트리거 키-값 쌍

[API 트리거 캠페인은]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 카드의 값이 외부 요인에 따라 사용자에게 표시할 콘텐츠를 결정할 때 사용할 수 있는 좋은 전략입니다. 예를 들어 보충 콘텐츠를 표시하려면 Liquid를 사용하여 키-값 페어를 설정합니다. 설정 시 `class_type`을 알아야 합니다.

![추가 콘텐츠 카드 사용 사례에 대한 키-값 쌍입니다. 이 예시에서는 Liquid를 사용하여 "tile_id", "tile_deeplink", "tile_title" 등 카드의 다양한 측면을 설정했습니다.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## 대화형 콘텐츠로서의 콘텐츠 카드
![화면 왼쪽 하단에 50% 프로모션을 표시하는 대화형 콘텐츠 카드가 나타납니다. 클릭하면 프로모션이 장바구니에 적용됩니다.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

콘텐츠 카드를 활용하여 사용자를 위한 역동적이고 인터랙티브한 경험을 만들 수 있습니다. 오른쪽 예제에서는 결제 시 콘텐츠 카드 팝업이 표시되어 사용자에게 막바지 프로모션을 제공합니다. 이와 같은 카드를 잘 배치하면 특정 사용자 작업을 '유도'할 수 있습니다. 

이 사용 사례의 키-값 쌍에는 원하는 할인 금액으로 설정된 `discount_percentage` 과 `coupon_code` 로 설정된 `class_type` 이 포함됩니다. 이러한 키-값 페어를 사용하여 결제 화면에서 유형별 콘텐츠 카드를 필터링하고 표시할 수 있습니다. 키-값 쌍을 사용하여 여러 피드를 관리하는 방법에 대한 자세한 내용은 [기본 콘텐츠 카드 피드 사용자 지정을]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) 참조하세요.
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"} 

## 콘텐츠 카드 배지

![숫자 7이 표시된 빨간색 배지와 함께 Swifty라는 이름의 Braze 샘플 앱이 표시된 iPhone 홈 화면]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

배지는 사용자의 관심을 끌기에 적합한 작은 아이콘입니다. 배지를 사용하여 새로운 콘텐츠 카드 콘텐츠를 사용자에게 알리면 사용자를 앱으로 다시 유도하고 세션을 늘릴 수 있습니다.

### 미열람 콘텐츠 카드 수를 배지로 표시

미열람 콘텐츠 카드 수를 앱 아이콘에 배지로 표시할 수 있습니다. 

{% tabs %}
{% tab Android %}

언제든지 전화로 읽지 않은 카드의 수를 요청할 수 있습니다:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

그런 다음 이 정보를 사용하여 읽지 않은 콘텐츠 카드의 수를 나타내는 배지를 표시할 수 있습니다. 자세한 내용은 <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK 참조 설명서</a>를 참조하세요.


{% endtab %}
{% tab iOS %}

다음 샘플은 `braze.contentCards`를 사용하여 미열람 콘텐츠 카드 수를 요청하고 표시합니다. 앱이 닫히고 사용자 세션이 종료된 후 이 코드는 카드 수를 요청하여 `viewed` 속성정보를 기준으로 카드 수를 필터링합니다.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

이 메서드 내에서 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현합니다.

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

이 메서드 내에서 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현합니다.

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

언제든지 전화로 읽지 않은 카드의 수를 요청할 수 있습니다:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

그런 다음 이 정보를 사용하여 읽지 않은 콘텐츠 카드의 수를 나타내는 배지를 표시할 수 있습니다. 자세한 내용은 <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK 참조 설명서</a>를 참조하세요.

{% endtab %}
{% endtabs %}


