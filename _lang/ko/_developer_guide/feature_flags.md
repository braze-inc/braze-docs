---
page_order: 2.5
nav_title: 피처 플래그
article_title: Braze SDK의 기능 플래그
description: "이 참조 문서에서는 전제 조건 및 사용 사례를 포함한 기능 플래그에 대한 개요를 다룹니다."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
  - Unity
  - Cordova
  - React Native
  - Flutter
  - Roku

---

# 기능 플래그

> 기능 플래그를 사용하면 특정 사용자나 무작위로 선택한 사용자에 대해 원격으로 기능을 활성화 또는 비활성화할 수 있습니다. 중요한 점은 추가 코드 배포나 앱 스토어 업데이트 없이 프로덕션 환경에서 기능을 켜고 끌 수 있다는 점입니다. 이를 통해 새로운 기능을 안심하고 안전하게 롤아웃할 수 있습니다.

{% alert tip %}
나만의 기능 플래그를 만들 준비가 되었다면 [기능 플래그 만들기를]({{site.baseurl}}/developer_guide/feature_flags/create/) 참조하세요.
{% endalert %}

## 필수 조건

기능 플래그 사용을 시작하는 데 필요한 최소 SDK 버전입니다:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## 사용 사례

### 점진적 롤아웃

기능 플래그를 사용하여 샘플 모집단에서 기능을 점진적으로 활성화합니다. 예를 들어 VIP 사용자에게 먼저 새 기능을 소프트 출시할 수 있습니다. 이 전략은 모든 사람에게 새로운 기능을 한번에 배포할 때 발생하는 위험을 완화하고 버그를 조기에 발견하는 데 도움이 됩니다.

![롤아웃 트래픽 슬라이더가 0%에서 100%로 이동하는 이미지.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

예를 들어 더 빠른 고객 서비스를 위해 앱에 새로운 '실시간 채팅 지원' 링크를 추가하기로 결정했다고 가정해 보겠습니다. 이 기능을 모든 고객에게 한 번에 출시할 수 있습니다. 그러나 광범위한 릴리스에는 다음과 같은 위험이 따릅니다: 

* 지원팀은 아직 교육 중이며, 고객은 출시 후 지원 티켓을 시작할 수 있습니다. 이렇게 하면 지원팀에 시간이 더 필요한 경우에 대비할 수 있는 여유가 없습니다.
* 실제 신규 지원 사례의 양을 확신할 수 없으므로 적절한 인력을 배치하지 못할 수도 있습니다.
* 지원팀에 과부하가 걸리면 이 기능을 다시 빠르게 해제할 수 있는 전략이 없습니다.
* 채팅 위젯에 버그가 있을 수 있으며, 고객이 부정적인 경험을 하는 것은 원치 않습니다.

Braze 기능 플래그를 사용하면 대신 점진적으로 기능을 롤아웃하고 이러한 모든 위험을 완화할 수 있습니다.

* 지원팀에서 준비가 되었다고 하면 '실시간 채팅 지원' 기능을 켭니다.
* 적절한 인력 배치 여부를 판단할 수 있도록 이 새로운 기능은 10%의 사용자만 사용할 수 있도록 설정합니다.
* 버그가 발견되면 서둘러 새 버전을 출시하는 대신 해당 기능을 신속하게 비활성화할 수 있습니다.

이 기능을 점진적으로 출시하려면 "실시간 채팅 위젯"이라는 [기능 플래그를 만들면]({{site.baseurl}}/developer_guide/feature_flags/create/) 됩니다.

![실시간 채팅 위젯이라는 예제에서 기능 플래그 세부 정보. ID는 enable_live_chat입니다. 이 기능 플래그 설명에 따르면 실시간 채팅 위젯이 지원 페이지에 표시됩니다.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

앱 코드에서는 Braze 기능 플래그가 활성화된 경우에만 **라이브 채팅 시작** 버튼이 표시됩니다:

{% tabs %}
{% tab 자바스크립트 %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% endtabs %}

### 앱 변수 원격 제어

기능 플래그를 사용하여 프로덕션 환경에서 앱의 기능을 수정합니다. 이는 App Store 승인으로 인해 모든 사용자에게 변경 사항을 신속하게 롤아웃할 수 없는 모바일 앱에서 특히 중요할 수 있습니다.

예를 들어 마케팅 팀이 앱의 탐색에 현재 세일 및 프로모션을 나열하고 싶다고 가정합니다. 일반적으로 엔지니어는 변경 사항에 대해 1주일의 리드 타임이 필요하고 App Store 검토에 3일이 걸립니다. 하지만 추수감사절, 블랙 프라이데이, 사이버 먼데이, 하누카, 크리스마스, 새해 첫날이 모두 두 달 안에 몰려 있어 이 촉박한 기한을 맞추기란 쉽지 않습니다.

기능 플래그를 사용하면 Braze가 앱 탐색 링크의 콘텐츠를 강화하여 마케팅 관리자가 며칠이 아닌 몇 분 만에 변경할 수 있습니다.

이 기능을 원격으로 구성하려면 `navigation_promo_link`라는 새 기능 플래그를 생성하고 다음과 같은 초기 속성정보를 정의합니다.

![일반 판매 페이지로 연결되는 링크 및 텍스트 속성이 있는 기능 플래그.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

앱에서는 Braze의 getter 메서드를 사용하여 이 기능 플래그의 속성정보를 검색하고 해당 값을 기반으로 탐색 링크를 빌드합니다.

{% tabs %}
{% tab 자바스크립트 %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% endtabs %}

이제 추수감사절 전날에는 Braze 대시보드에서 해당 속성정보 값만 변경하면 됩니다.

![감사제 판매 페이지로 연결되는 링크 및 텍스트 속성이 있는 기능 플래그.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

따라서 다음에 누군가 앱을 로드할 때 새로운 추수감사절 프로모션을 볼 수 있습니다.

### 메시지 조정

기능 플래그를 사용하여 기능의 롤아웃과 메시징을 동기화합니다. 이렇게 하면 사용자 경험 및 관련 메시지에 대한 소스로 Braze를 사용할 수 있습니다. 이를 달성하려면 새 기능을 특정 세그먼트 또는 필터링된 오디언스의 일부로 타겟팅합니다. 그런 다음 해당 세그먼트만 타겟팅하는 캠페인 또는 캔버스를 만듭니다. 

사용자를 위한 새로운 로열티 리워드 프로그램을 시작한다고 가정합니다. 마케팅팀과 제품팀이 기능 출시와 홍보 메시지의 타이밍을 완벽하게 조율하는 것은 어려울 수 있습니다. 캔버스의 기능 플래그를 사용하면 특정 오디언스에 대해 기능을 활성화하고 해당 사용자에 대한 관련 메시징을 제어할 때 정교한 로직을 적용할 수 있습니다.

기능 롤아웃과 메시징을 효과적으로 조정하기 위해 `show_loyalty_program`이라는 새로운 기능 플래그를 생성합니다. 초기 단계별 출시에서 캔버스가 기능 플래그가 활성화되는 시기와 대상을 제어할 수 있습니다. 지금은 롤아웃 비율을 0%로 유지하고 대상 세그먼트를 선택하지 않겠습니다.

![Loyalty Rewards Program이라는 이름의 기능 플래그. ID는 show_loyalty_program이며, 홈 화면과 프로필 페이지에 새로운 로열티 보상 프로그램을 표시한다는 설명이 표시됩니다.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

그런 다음, 캔버스 흐름에서 'High Value Customers' 세그먼트에 대해 `show_loyalty_program` 기능 플래그를 활성화하는 [기능 플래그 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)를 생성합니다.

![고가치 고객 세그먼트가 show_loyalty_program 기능 플래그를 켜는 대상 분할 단계가 있는 캔버스의 예입니다.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

이제 이 세그먼트의 사용자에게 새로운 로열티 프로그램이 표시되기 시작하며, 활성화된 후에는 이메일과 설문조사가 자동으로 발송되어 팀에서 피드백을 수집하는 데 도움이 됩니다.

### 기능 실험

기능 플래그를 사용하여 새로운 기능에 대한 가설을 실험하고 확인합니다. 트래픽을 두 개 이상의 그룹으로 분할하여 그룹 간에 기능 플래그의 영향을 비교하고 그 결과에 따라 최선의 조치를 결정할 수 있습니다.

[A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)는 여러 버전의 변수에 대한 사용자 응답을 비교할 수 있는 강력한 툴입니다.

이 예제에서는 이커머스 앱의 새로운 결제 플로우를 구축했습니다. 사용자 경험을 개선한다는 확신은 있지만, 앱 매출에 미치는 영향을 측정하기 위해 A/B 테스트를 실행하려고 합니다.

먼저 `enable_checkout_v2` 라는 새 기능 플래그를 만들겠습니다. 대상 또는 출시 비율을 추가하지 않습니다. 대신 기능 플래그 실험을 사용하여 트래픽을 분할하고 기능을 활성화한 다음 결과를 측정해 보겠습니다.

앱에서 기능 플래그가 활성화되어 있는지 여부를 확인하고 응답에 따라 결제 흐름을 교체합니다:

{% tabs %}
{% tab 자바스크립트 %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

[기능 플래그 실험에서]({{site.baseurl}}/developer_guide/feature_flags/experiments/) A/B 테스트를 설정하겠습니다.

이제 50%의 사용자에게는 이전 환경이 표시되고 나머지 50%에게는 새로운 환경이 표시됩니다. 그런 다음 두 가지 변형을 분석하여 어떤 결제 흐름이 더 높은 전환율을 가져왔는지 확인할 수 있습니다. {% multi_lang_include metrics.md metric='Conversion Rate' %}

![트래픽을 두 개의 50% 그룹으로 분할하는 기능 플래그 실험.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

승자가 결정되면 이 캠페인을 중단하고 엔지니어링 팀이 다음 앱 출시에 이를 하드코딩하는 동안 모든 사용자에 대한 기능 플래그의 롤아웃 비율을 100%로 높일 수 있습니다.

### 세분화

**기능** 플래그 필터를 사용하여 기능 플래그 활성화 여부에 따라 세그먼트를 만들거나 사용자에게 메시지를 타겟팅할 수 있습니다. 예를 들어 앱에서 프리미엄 콘텐츠를 제어하는 기능 플래그가 있다고 가정합니다. 기능 플래그를 활성화하지 않은 사용자를 필터링하는 세그먼트를 만든 다음, 프리미엄 콘텐츠를 보도록 계정을 업그레이드하라는 메시지를 해당 세그먼트에 보낼 수 있습니다.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

세그먼트 필터링에 대한 자세한 내용은 [세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)을 참조하세요.

{% alert note %}
재귀 세그먼트를 방지하기 위해 다른 기능 플래그를 참조하는 세그먼트를 생성할 수 없습니다.
{% endalert %}

## 요금제 제한 사항

다음은 무료 및 유료 요금제에 대한 기능 플래그 제한 사항입니다.

| 기능                                                                                                   | 무료 버전     | 유료 버전      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [활성 기능 플래그](#active-feature-flags)                                                                     | 워크스페이스당 10개 | 워크스페이스당 110개 |
| [활발한 캠페인 실험]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 워크스페이스당 1개  | 워크스페이스당 100개 |
| [기능 플래그 캔버스 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | 무제한        | 무제한         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다음 중 하나라도 해당하면 기능 플래그가 활성화된 것으로 간주되며 한도에 포함됩니다:

- 롤아웃이 0% 이상입니다.
- 활성 캔버스에서 사용
- 현재 진행 중인 실험에 사용

동일한 기능 플래그가 여러 기준과 일치하더라도(예: 캔버스에서 사용되고 롤아웃이 50%인 경우) 사용량 제한과 관련해 활성 기능 플래그 1개로만 계산됩니다.

{% alert note %}
유료 버전의 기능 플래그를 구매하려면 Braze 계정 매니저에게 문의하거나 Braze 대시보드에서 업그레이드를 요청합니다.
{% endalert %}
