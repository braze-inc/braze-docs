---
nav_title: 기능 인식 및 새 앱 버전
article_title: 기능 인식 및 새 앱 버전
page_order: 9
page_type: reference
description: "이 참고 문서에서는 새로운 기능이나 버전을 출시할 때 사용자가 이를 잘 알고 흥미를 가질 수 있도록 하는 방법에 대해 설명합니다."
tool: Campaigns

---

# 기능 인식 및 새 앱 버전

> 이 참조 문서에서는 Braze 플랫폼을 사용하여 고객에게 앱의 새로운 기능과 버전에 대한 최신 정보를 제공하는 방법에 대해 설명합니다. 

앱을 지속적으로 업데이트하고 개선하기 위해 열심히 노력하고 있으며, 사용자들이 이러한 흥미로운 새 기능과 새로운 앱 버전을 경험하기를 원합니다. 사용자에게 아직 사용하지 않은 새로운 기능에 대해 알려주고 앱을 탐색하여 제공하는 기능을 최대한 활용하도록 유도하는 방법을 알아보세요.

기능 인지도 캠페인은 앱의 기능을 지속적으로 개선하면서 사용자가 앱에 계속 참여하도록 유도할 수 있는 좋은 방법입니다.  사용자를 최신 상태로 유지하는 것은 사용자의 활동을 유지하고, 평점을 높이고, 사용자 인게이지먼트를 보장하는 좋은 방법입니다.

## 가장 최신 앱 버전으로 필터링

Braze SDK는 사용자의 최신 앱 버전을 자동으로 추적합니다. 이러한 버전은 필터 및 세그먼트에서 메시지 또는 캠페인을 수신할 사용자를 결정하는 데 사용할 수 있습니다.

![캠페인 구축 워크플로우의 타겟 사용자 단계에 있는 타겟팅 옵션 패널입니다. 추가 필터 섹션에는 "안드로이드 스톱워치(안드로이드)의 최신 앱 버전 번호가 3.7.0(134.0.0.0) 미만입니다."가 포함됩니다.]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

### 앱 버전 번호

**앱 버전 번호** 필터를 사용하여 앱의 버전과 빌드 번호로 사용자를 분류할 수 있습니다. 

이 필터는 다양한 앱 버전을 대상으로 수치 비교를 지원합니다. 예를 들어 앱 버전이 "아래", "위", "같음"인 사용자를 타겟팅하여 앱 업그레이드가 필요한 새로운 기능을 홍보하는 데 유용할 수 있습니다.

이 새로운 필터는 각 이전 버전을 명시적으로 나열하거나 정규표현식을 사용해야 하는 기존 "앱 버전 이름" 필터를 대체할 수 있습니다.

**작동 방식**

* 앱의 앱 버전에서 전송된 `major.minor.patch` 버전의 각 부분은 정수로 비교됩니다.
* 메이저 숫자가 같으면 마이너 숫자를 비교하는 등의 방식으로 비교합니다.

**중요**

* 안드로이드 앱은 사람이 읽을 수 있는 [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName)과 내부 [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode())를 모두 가지고 있습니다. 앱 버전 번호 필터는 앱 스토어가 릴리스될 때마다 증가하기 때문에 `versionCode`를 사용합니다.
* 특히 앱의 `versionName` 및 `versionCode` 필드가 모두 Braze 대시보드에서 볼 수 있기 때문에 동기화되지 않을 경우 혼란을 야기할 수 있습니다. 모범 사례로 앱의 `versionName` 및 `versionCode`가 함께 증가되는지 확인하세요.
* 사람이 읽을 수 있는 `versionName` 필드를 기준으로 필터링해야 하는 경우(일반적이지 않음) 앱 버전 이름 필터를 사용하세요.

#### SDK 요구 사항

이 필터의 값은 Braze Android SDK v3.6.0+ 및 iOS SDK v3.21.0+부터 수집됩니다. 이 필터에는 SDK 요구 사항이 있지만, 이 기능을 사용하면 앱의 하위(이전) 버전을 사용하는 사용자를 타겟팅할 수 있습니다!

안드로이드의 경우, 이 버전 번호는 앱의 [패키지 롱 버전 코드](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode())를 기반으로 합니다.

iOS의 경우, 이 버전 번호는 앱의 [짧은 버전 문자열](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring)을 기반으로 합니다.

{% alert tip %}
이 필터는 사용자가 지원되는 Braze SDK 버전으로 앱을 업그레이드한 후 값을 채웁니다. 그때까지는 필터를 선택해도 버전이 표시되지 않습니다.
{% endalert %}

#### 사용 사례

다음 시나리오에서는 먼저 앱의 버전 `2.0.0`에서 이 필터를 지원하는 Braze SDK로 업그레이드했다고 가정해 보겠습니다.

Braze가 앱 2.0.0 버전에서 데이터를 수신하면 이전 버전 또는 이후 버전의 사용자를 타겟팅할 수 있습니다.

| 필터  | 사용자의 앱 버전  | 결과 |
:------------- | :----------- | :---------|
| 2.0.0 미만 | 1.0.0 | 사용자가 해당 세그먼트에 속하지만 Braze SDK가 "앱 버전 번호" 필터를 지원하지 않는 경우입니다. |
| 2.0.0 이상 | 2.5.1 | 사용자와 향후 모든 설치는 세그먼트에 포함됩니다. |
| 2.0.0 이상 | 1.9.9 | 사용자가 세그먼트에 속하지 않습니다. |
| 2.0.0보다 작거나 같음 | 3.0.1 | 사용자가 세그먼트에 속하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 앱 버전 이름

"앱 버전 이름" 필터를 사용하여 앱의 사용자 대면 "빌드 이름"을 기준으로 사용자를 분류할 수 있습니다. 

이 필터는 'is', 'is not' 및 정규식을 사용한 일치를 지원합니다. 예를 들어 "1.2.3-test-build" 버전이 아닌 앱을 보유한 사용자를 타겟팅할 수 있습니다.

안드로이드의 경우, 이 버전 이름은 앱의 [패키지 버전 이름](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName)을 기반으로 합니다. iOS의 경우, 이 버전 이름은 앱의 [짧은 버전 문자열](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring)을 기반으로 합니다.

### 사용하지 않은 기능

새 앱 버전을 출시하고 새로운 기능을 도입하면 사용자가 새로운 콘텐츠를 인지하지 못할 수 있습니다. 기능 인식 캠페인을 실행하면 사용자에게 새로운 기능이나 한 번도 사용해 본 적이 없는 기능에 대해 알릴 수 있는 좋은 방법입니다. 이를 위해, 귀하는 앱 내에서 특정 작업을 완료한 적이 없는 사용자에게 할당된 [커스텀 속성]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data)을 생성하거나 특정 작업을 추적하기 위해 [커스텀 이벤트]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data)를 사용해야 합니다. 이 속성(또는 이벤트)을 사용하여 캠페인을 보내려는 사용자를 세분화할 수 있습니다.

{% alert tip %}
오디언스의 특정 부분을 리타겟팅하고 싶으신가요? 사용자의 이전 행동을 활용하여 캠페인을 리타겟팅하는 방법을 알아보려면 [캠페인 리타겟팅]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/)을 확인하세요.
{% endalert %}


