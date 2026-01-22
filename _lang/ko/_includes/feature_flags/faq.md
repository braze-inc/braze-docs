# Frequently asked questions

> 이 문서에서는 기능 플래그에 대해 몇 가지 자주 묻는 질문에 대한 답변을 제공합니다.

## 기능 및 지원

### Braze 기능 플래그는 어떤 플랫폼에서 지원되나요? {#platforms}

Braze는 iOS, Android 및 웹 플랫폼에서 기능 플래그를 지원하며, 다음 SDK 버전 요구 사항이 있습니다.

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

다른 플랫폼에서 지원이 필요하십니까? 팀에 이메일([feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com))을 보내주세요.

### 기능 플래그를 구현할 때 어느 정도의 노력이 필요한가요? {#level-of-effort}

기능 플래그는 몇 분 안에 생성 및 통합할 수 있습니다. 

필요한 대부분의 노력은 엔지니어링 팀이 출시하려는 새로운 기능을 빌드하는 작업과 관련됩니다. 하지만 기능 플래그를 추가하는 경우 앱 또는 웹사이트의 코드에서 `IF`/`ELSE` 문만큼이나 간단합니다.

{% tabs %}
{% tab 자바스크립트 %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### 기능 플래그가 마케팅 팀에 어떻게 도움이 될 수 있습니까? {#marketing-teams}

마케팅 Teams는 기능 플래그를 사용하여 제품 발표(예: 제품 출시 이메일)를 조정할 수 있습니다. 기능이 소수의 사용자에게만 활성화된 경우입니다.

예를 들어, Braze 기능 플래그를 사용하면 앱의 사용자 중 10%에게 새로운 고객 로열티 프로그램을 롤아웃하고, 캔버스 기능 플래그 단계를 사용하여 활성화된 동일한 10%의 사용자에게 이메일, 푸시 또는 기타 메시징을 보낼 수 있습니다. 

### 기능 플래그가 제품 팀에 어떻게 도움이 될 수 있습니까? {#product-teams}

제품 팀은 새로운 기능의 점진적 출시 또는 소프트 롤아웃을 수행하기 위해 기능 플래그를 사용할 수 있으며, 모든 사용자에게 제공하기 전에 핵심 성과 지표(KPI) 및 고객 피드백을 모니터링할 수 있습니다.

제품 팀은 [기능 플래그 속성정보]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties)를 사용하여 앱에서 딥링크, 텍스트, 이미지 또는 기타 동적 콘텐츠와 같은 콘텐츠를 원격으로 채울 수 있습니다.

캔버스 기능 플래그 단계를 사용하여 제품 Teams는 새로운 기능이 전환율에 미치는 영향을 기능이 비활성화된 사용자와 비교하여 측정하기 위해 A/B 분할 테스트를 실행할 수도 있습니다. 

### 기능 플래그가 엔지니어링 팀에 어떻게 도움이 될 수 있습니까? {#engineering-teams}

엔지니어링 팀은 기능 플래그를 사용하여 새로운 기능 출시에 내재된 위험을 줄이고 야간에 코드 수정 사항을 서둘러 배포해야 하는 상황을 피할 수 있습니다.

새로운 기능 플래그 이면에 숨겨진 코드를 릴리스함으로써, 팀은 Braze 대시보드에서 원격으로 해당 기능을 켜거나 꺼서 새로운 코드 푸시 또는 App Store 업데이트 승인 대기에서 발생하는 지연을 우회할 수 있습니다.

## 기능 롤아웃 및 타겟팅

### 기능 플래그를 특정 사용자 그룹에만 롤아웃할 수 있나요? {#target-users}

예. Braze에서 이메일 주소, `user_id` 또는 고객 프로필의 기타 속성으로 특정 사용자를 타겟팅하는 세그먼트를 생성합니다. 그런 다음, 해당 세그먼트의 100%에 기능 플래그를 배포합니다.

### 롤아웃 비율을 조정하면 이전에 활성화된 그룹으로 버킷된 사용자에게 어떤 영향을 주나요? {#random-buckets}

기능 플래그 롤아웃은 여러 기기 및 세션에서 사용자에게 일관되게 유지됩니다.

- 기능 플래그가 무작위 사용자 중 10%에게 롤아웃되면, 해당 10%는 기능 플래그의 수명 동안 활성화된 상태로 유지됩니다.
- 롤아웃을 10%에서 20%로 늘리면 동일한 10%가 활성화된 상태로 유지되고, 새로운 추가 10%의 사용자가 활성화된 그룹에 추가됩니다.
- 롤아웃을 20%에서 10%로 낮추면 원래 10%의 사용자만 활성화된 상태로 유지됩니다.

이 전략은 사용자가 앱에서 일관된 경험을 이용하도록 도와주며 여러 세션에서 변동되지 않도록 합니다. 물론 기능을 0%로 비활성화하면 모든 사용자가 기능 플래그에서 제거됩니다. 버그를 발견하거나 기능을 완전히 비활성화해야 할 때 유용합니다.

## 기술 주제

### 기능 플래그를 사용하여 Braze SDK가 초기화되는 시점을 제어할 수 있나요? {#initialization}

아니요. 현재 사용자의 기능 플래그를 다운로드하고 동기화하려면 SDK를 초기화해야 합니다. 즉, 기능 플래그를 사용하여 Braze에서 생성되거나 추적되는 사용자를 제한할 수 없습니다.

### SDK는 기능 플래그를 얼마나 자주 새로 고치나요? {#refresh-frequency}

기능 플래그는 세션 시작 시, 활성 사용자 변경 시 새로 고쳐집니다. 기능 플래그는 SDK의 [새로 고침 메서드]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing)를 사용하여 수동으로 새로 고칠 수도 있습니다. 기능 플래그 새로 고침은 5분에 한 번의 속도로 제한됩니다(변경 가능).

바람직한 데이터 관행에서는 기능 플래그를 너무 빨리 새로 고치지 않도록 권장합니다(너무 빠르면 잠재적 사용량 제한이 적용됨). 따라서 사용자가 새로운 기능과 상호 작용하기 전에 새로 고치거나 필요한 경우 앱에서 주기적으로 새로 고치는 것이 가장 좋습니다.

### 사용자가 오프라인 상태일 때 기능 플래그를 사용할 수 있습니까? {#offline}

네, 기능 플래그가 새로 고쳐진 후에는 사용자의 기기에 로컬로 저장되며 오프라인 상태에서도 접근할 수 있습니다.

### 세션 중간에 기능 플래그가 새로 고침되면 어떻게 되나요? {#listen-for-updates}

기능 플래그는 세션 중간에 새로 고침될 수 있습니다. 특정 변수나 구성 설정이 변경될 경우 앱을 업데이트해야 하는 시나리오가 있을 수 있습니다. UI 렌더링 방식의 급격한 변화를 피하기 위해 앱을 업데이트하지 않는 다른 시나리오도 있습니다.

이를 제어하려면 기능 플래그의 [업데이트를 수신 대기]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates)하고 변경할 기능 플래그에 따라 앱을 다시 렌더링할지 여부를 결정합니다. 

### 글로벌 제어 그룹에 속한 사용자가 기능 플래그 실험을 받지 못하는 이유는 무엇인가요?

[글로벌 제어 그룹에]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) 속한 사용자에게는 기능 플래그를 활성화할 수 없습니다. 즉, 글로벌 제어 그룹에 속한 사용자도 기능 플래그 실험에 참여할 수 없습니다.

## 추가 질문이 있으신가요?

질문이나 피드백이 있습니까? 팀에 이메일([feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com))을 보내주세요.

