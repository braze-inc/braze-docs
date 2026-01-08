# 기능 플래그 실험

> 기능 플래그 실험을 통해 애플리케이션의 변경 사항을 A/B 테스트하여 전환율을 최적화할 수 있습니다. 마케터는 기능 플래그를 사용하여 새로운 기능이 전환율에 긍정적인 영향을 미치는지 부정적인 영향을 미치는지 또는 어떤 기능 플래그 속성 집합이 가장 적합한지 결정할 수 있습니다.

## 전제 조건

실험에서 사용자 데이터를 추적하려면 먼저 앱에서 사용자가 기능 플래그와 상호 작용하는 시점을 기록해야 합니다. 이를 기능 플래그 노출이라고 합니다. 사용자가 대조군에 속해 있더라도 테스트 중인 기능을 보았거나 볼 수 있었을 때마다 기능 플래그 노출 횟수를 기록해야 합니다.

기능 플래그 노출 횟수 로깅에 대해 자세히 알아보려면 [기능 플래그 생성]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions)을 참조하세요.

{% tabs %}
{% tab 웹 %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 기능 플래그 실험 만들기

### 1단계: 실험 만들기

1. **메시징** > **캠페인으로** 이동한 다음 **\+ 캠페인 만들기를** 선택합니다.
2. **기능 플래그 실험**을 선택합니다.
3. 캠페인에 명확하고 의미 있는 이름을 지정하세요.

### 2단계: 실험 변형 추가

다음으로 변형을 만듭니다. 각 이형 상품에 대해 켜거나 끄려는 기능 플래그를 선택한 다음 할당된 속성을 검토합니다.

기능의 영향을 테스트하려면 변형을 사용하여 트래픽을 두 개 이상의 그룹으로 분할하세요. 한 그룹의 이름을 'My control group'으로 지정하고 해당 그룹의 기능 플래그를 끕니다.

### 3단계: 속성 덮어쓰기(선택 사항)

특정 캠페인 변형을 수신하는 사용자에 대해 처음에 설정한 기본 속성을 덮어쓰도록 선택할 수 있습니다.

추가 기본 속성을 편집, 추가 또는 제거하려면 **메시징** > **기능 플래그**에서 기능 플래그 자체를 편집하세요. 이형 상품이 비활성화되면 SDK는 지정된 기능 플래그에 대한 빈 속성 개체를 반환합니다.

!['링크' 변수 키가 '/판매'로 덮어씌워진 '실험 변형' 섹션]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### 4단계: 타겟팅할 사용자 선택

세그먼트 또는 필터 중 하나를 사용하여 [타겟 사용자를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) 선택합니다. 예를 들어, **수신된 기능 플래그 변형** 필터를 사용하여 이미 A/B 테스트를 수신한 사용자를 리타겟팅할 수 있습니다.

![필터 그룹 검색창에 '수신된 기능 플래그 변형'이 강조 표시된 기능 플래그 실험의 '대상' 페이지.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
세그먼트 멤버십은 특정 사용자에 대한 기능 플래그가 새로 고쳐질 때 계산됩니다. 앱에서 기능 플래그를 새로 고치거나 새 세션을 시작할 때 변경 사항을 적용할 수 있습니다.
{% endalert %}

### 5단계: 배리언트 배포

실험의 백분율 분포를 선택합니다. 실험을 시작한 후에는 배포를 변경하지 않는 것이 모범 사례입니다.

### Step 6: 전환 할당

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환을 계산하는 기간을 최대 30일로 지정합니다.

### 7단계: 검토 및 시작

실험의 마지막 빌드를 완료한 후 세부 정보를 검토한 다음 **실험 시작을** 선택합니다.

## 결과 검토

기능 플래그 실험이 완료되면 실험에 대한 노출 데이터를 검토할 수 있습니다. **메시징** > **캠페인으로** 이동하여 기능 플래그 실험이 포함된 캠페인을 선택합니다.

### 캠페인 분석

**캠페인 분석은** 다음과 같은 실험의 성과에 대한 높은 수준의 개요를 제공합니다:

- 총 노출 수
- 고유 노출 수
- 기본 전환율
- 메시지에서 발생한 총 수익
- 예상 대상

또한 전달, 대상 및 전환에 대한 실험의 설정을 볼 수도 있습니다.

### 기능 플래그 실험 성능

**기능 플래그 실험 성과는** 다양한 차원에서 메시지가 얼마나 잘 수행되었는지를 보여줍니다. 표시되는 구체적인 메트릭은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. 각 이형 상품과 관련된 기능 플래그 값을 확인하려면 **미리 보기를** 선택합니다.
