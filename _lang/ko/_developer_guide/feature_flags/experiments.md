---
nav_title: 피처 플래그 실험
article_title: 피처 플래그 실험
page_order: 40
description: "기능 플래그 실험을 통해 애플리케이션의 변경 사항을 A/B 테스트하여 전환율을 최적화할 수 있습니다."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 기능 플래그 실험 만들기

> 기능 플래그 실험을 통해 애플리케이션의 변경 사항을 A/B 테스트하여 전환율을 최적화할 수 있습니다. 마케터는 기능 플래그를 사용하여 새로운 기능이 전환율에 긍정적인 영향을 미치는지 부정적인 영향을 미치는지 또는 어떤 기능 플래그 속성 집합이 가장 적합한지 결정할 수 있습니다.

## 전제 조건

실험에서 사용자 데이터를 추적하려면 먼저 앱에서 사용자가 기능 플래그와 상호 작용하는 시점을 기록해야 합니다. 이를 기능 플래그 노출이라고 합니다. 사용자가 대조군에 속해 있더라도 테스트 중인 기능을 보았거나 볼 수 있었을 때마다 기능 플래그 노출 횟수를 기록해야 합니다.

기능 플래그 노출 횟수 로깅에 대해 자세히 알아보려면 [기능 플래그 생성]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions)을 참조하세요.

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## 1단계: 실험 만들기

1. **메시징** > **캠페인**으로 이동하여 **\+ 캠페인 만들기**를 클릭합니다.
2. **기능 플래그 실험**을 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.

## 2단계: 실험 변형 추가

다음으로 변형을 만듭니다. 각 이형 상품에 대해 켜거나 끄려는 기능 플래그를 선택하고 할당된 속성을 검토합니다.

기능의 영향을 테스트하려면 변형을 사용하여 트래픽을 두 개 이상의 그룹으로 분할하세요. 한 그룹의 이름을 'My control group'으로 지정하고 해당 그룹의 기능 플래그를 끕니다.

### 속성 덮어쓰기

처음 기능 플래그를 설정할 때 기본 속성을 지정했지만, 특정 캠페인 변형을 수신하는 사용자에 대해 해당 값을 덮어쓰도록 선택할 수 있습니다.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

추가 기본 속성을 편집, 추가 또는 제거하려면 **메시징** > **기능 플래그**에서 기능 플래그 자체를 편집하세요.

이형 상품이 비활성화되면 SDK는 지정된 기능 플래그에 대한 빈 속성 개체를 반환합니다. 

## 3단계: 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁혀야 합니다. 세그먼트 멤버십은 특정 사용자에 대한 기능 플래그가 새로 고쳐질 때 계산됩니다.

{% alert note %}
앱에서 기능 플래그를 새로 고치거나 새 세션을 시작할 때 변경 사항을 적용할 수 있습니다.
{% endalert %}

## 4단계: 배리언트 배포

실험의 백분율 분포를 선택합니다. 실험을 시작한 후에는 배포를 변경하지 않는 것이 모범 사례입니다.

## 5단계: 전환 할당

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환을 계산하는 기간을 최대 30일로 지정합니다.

## 6단계: 검토 및 실행

실험의 마지막 빌드를 완료한 후 세부 정보를 검토한 다음 **실험 시작**을 클릭합니다.



