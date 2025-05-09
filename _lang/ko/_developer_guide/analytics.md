---
nav_title: 분석
article_title: Braze SDK에 대한 분석
page_order: 2.6
description: "Braze SDK의 분석에 대해 알아보세요. Braze가 수집하는 데이터, 커스텀 이벤트와 커스텀 속성의 차이점, 그리고 분석 관리를 위한 모범 사례를 더 잘 이해할 수 있습니다."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
---

# 분석

> Braze SDK의 분석에 대해 알아보세요. Braze가 수집하는 데이터, 커스텀 이벤트와 커스텀 속성의 차이점, 그리고 분석 관리를 위한 모범 사례를 더 잘 이해할 수 있습니다.

{% alert tip %}
Braze 구현 중에 팀과 마케팅 목표에 대해 논의하여 추적하려는 데이터와 Braze로 추적하는 방법을 최선으로 결정하세요. 예를 들어, 이 가이드의 끝에 있는 [택시/라이드 공유 앱](#example-case) 사례 연구를 참조하세요.
{% endalert %}

## 자동으로 수집된 데이터

특정 사용자 데이터(예: 처음 사용한 앱, 마지막으로 사용한 앱, 총 세션 수, 기기 OS 등)는 SDK에서 자동으로 수집됩니다. 통합 가이드에 따라 SDK를 구현하면 이 [기본 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) 기능을 활용할 수 있습니다. 이 목록을 확인하면 사용자에 대한 동일한 정보를 두 번 이상 저장하지 않도록 하는 데 도움이 됩니다. 세션 시작과 종료를 제외한 다른 모든 자동 추적 데이터는 데이터 포인트 할당에 포함되지 않습니다.

특정 데이터 항목의 기본 수집을 차단하는 프로세스를 허용 목록에 추가하려면 [SDK 프라이머]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/)를 참조하세요.

## 사용자 지정 이벤트

커스텀 이벤트는 사용자가 수행한 작업으로, 애플리케이션과의 가치 있는 사용자 상호 작용을 추적하는 데 가장 적합합니다. 커스텀 이벤트를 기록하면 구성 가능한 지연 시간으로 후속 캠페인을 얼마든지 트리거할 수 있으며, 해당 이벤트의 최신 수준 및 빈도에 따라 다음과 같은 세분화 필터를 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 사용자 지정 이벤트가 **X회 이상** 발생했는지 확인합니다. | **초과** | **번호** |
| 사용자 지정 이벤트가 **X 횟수 미만으로** 발생했는지 확인합니다. | **미만** | **번호** |
| 커스텀 이벤트가 **정확히 X회** 발생했는지 확인합니다. | **정확히** | **번호** |
| 사용자 지정 이벤트가 **X 날짜 이후에** 마지막으로 발생했는지 확인합니다. | **이후** | **시간** |
| 사용자 지정 이벤트가 **X 날짜 이전에** 마지막으로 발생했는지 확인합니다. | **전에** | **시간** |
| 사용자 지정 이벤트가 마지막으로 발생한 지 **X일이 넘었는지** 확인합니다. | **초과** | **이전 일수**(양수) |
| 사용자 지정 이벤트가 마지막으로 발생한 **날짜가 X일 미만인지** 확인합니다. | **미만** | **이전 일수**(양수) |
| 커스텀 이벤트가 **X회(최대 = 50) 초과**하여 발생했는지 확인합니다. | **초과** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 커스텀 이벤트가 **X회(최대 = 50) 미만으로** 발생했는지 확인합니다 | **미만** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 커스텀 이벤트가 **정확히 X회(최대 = 50)만큼** 발생했는지 확인합니다 | **정확히** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze는 세분화를 위해 이러한 이벤트가 발생한 횟수와 각 사용자가 마지막으로 수행한 시간을 기록합니다. **사용자 지정 이벤트** 분석 페이지에서 각 사용자 지정 이벤트의 발생 빈도를 집계하여 볼 수 있을 뿐만 아니라 시간 경과에 따른 세그먼트별로 더 자세히 분석할 수 있습니다. 캠페인이 마지막으로 전송된 시간을 나타내기 위해 Braze에서 시계열에 겹쳐 표시하는 회색 선을 보고 캠페인이 커스텀 이벤트 활동에 어떤 영향을 미쳤는지 확인하는 데 특히 유용합니다.

![신용 카드를 추가하고 30일 동안 검색한 사용자에 대한 통계를 보여주는 사용자 지정 이벤트 분석 그래프.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
사용자 지정 [속성을 증가시키면]({{site.baseurl}}/api/endpoints/messaging/) 사용자 지정 이벤트와 유사한 사용자 행동에 대한 카운터를 유지할 수 있습니다. 그러나 시계열에서 커스텀 속성 데이터는 볼 수 없습니다. 시계열로 분석할 필요가 없는 사용자 행동은 이 방법을 통해 기록해야 합니다.
{% endalert %}

### 사용자 지정 이벤트 스토리지

모든 고객 프로필 데이터(커스텀 이벤트, 커스텀 속성, 커스텀 데이터)는 해당 프로필이 활성화되어 있는 동안 저장됩니다.

### 사용자 지정 이벤트 속성

사용자 지정 이벤트 속성을 사용하면 Braze에서 사용자 지정 이벤트 및 구매에 대한 속성을 설정할 수 있습니다. 그런 다음, 이러한 속성정보를 사용하여 트리거 조건을 추가로 검증하여 메시징의 개인화를 강화하며, 원시 데이터 내보내기를 통해 보다 정교한 분석을 생성할 수 있습니다. 속성정보 값은 문자열, 숫자, 부울 또는 시간 오브젝트일 수 있습니다. 그러나 속성 값은 배열 객체가 될 수 없습니다.

예를 들어, 전자상거래 애플리케이션이 사용자가 장바구니를 포기할 때 메시지를 보내고 싶다면, 사용자 장바구니의 `cart_value`의 커스텀 이벤트 속성을 추가하여 타겟 오디언스를 개선하고 캠페인 개인화를 증가시킬 수 있습니다.

![장바구니를 포기하고 장바구니 값을 100 이상 200 미만으로 남겨둔 사용자에게 캠페인을 전송하는 사용자 지정 이벤트 예제]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

사용자 지정 이벤트 속성을 사용하여 메시징 템플릿 내에서 개인화할 수도 있습니다. 트리거 이벤트와 함께 [액션 기반 전달을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) 사용하는 모든 캠페인은 해당 이벤트의 사용자 지정 이벤트 속성을 사용하여 메시징 개인화를 수행할 수 있습니다. 게임 애플리케이션이 레벨을 완료한 사용자에게 메시지를 보내려는 경우, 사용자가 해당 레벨을 완료하는 데 걸린 시간을 속성으로 추가하여 메시지를 개인화할 수 있습니다. 이 예에서는 [조건부 논리를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) 사용하여 세 개의 서로 다른 세그먼트에 대해 메시지를 개인화합니다. ``time_spent``라는 커스텀 이벤트 속성은 ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``를 호출하여 메시지에 포함될 수 있습니다.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

커스텀 이벤트 속성은 메시징을 개인화하거나 세분화된 실행 기반 전달 캠페인을 구축하는 데 도움이 되도록 설계되었습니다. 이벤트 속성의 최신성과 빈도를 기반으로 세그먼트를 생성하고 싶다면 고객 성공 매니저 또는 지원 팀에 문의하세요.

## 사용자 지정 속성

커스텀 속성은 표준 속성보다 훨씬 더 구체적으로 사용자를 타겟팅할 수 있는 매우 유연한 툴입니다. 사용자 지정 속성은 사용자에 대한 브랜드별 정보를 저장하는 데 유용합니다. 커스텀 속성에 대한 시계열 정보는 저장하지 않으므로 이전 커스텀 이벤트 예제처럼 이에 기반한 그래프는 얻을 수 없습니다.

### 사용자 지정 속성 저장소

모든 고객 프로필 데이터(커스텀 이벤트, 커스텀 속성, 커스텀 데이터)는 해당 프로필이 활성화되어 있는 동안 저장됩니다.

### 사용자 지정 속성 데이터 유형

사용자 지정 속성으로 저장할 수 있는 데이터 유형은 다음과 같습니다:

#### 문자열(영숫자)

문자열 속성은 즐겨 찾는 브랜드, 전화번호 또는 애플리케이션 내에서 마지막으로 검색한 문자열과 같은 사용자 입력을 저장하는 데 유용합니다. 문자열 속성은 최대 255자입니다.

다음 표에서는 문자열 속성에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 문자열 속성이 입력한 문자열과 **정확히 일치하는지** 확인합니다.| **EQUALS** | **문자열** |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분 일치**하는지 확인합니다. | **정규식 일치** | **문자열** **OR** **정규식** |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분 일치하지 않는지** 확인합니다. | **정규식과 일치하지 않습니다.** | **문자열** **OR** **정규식** |
| 문자열 속성이 입력한 문자열과 **일치하지 않는지** 확인합니다.| **동일하지 않음** | **문자열** |
| 사용자 프로필에 문자열 **속성이** 있는지 확인합니다. | **비어 있음** | **N/A** |
| 사용자 프로필에 문자열 속성이 **없는지** 확인합니다. | **비어 있지 않음** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
**정규식과 일치하지 않음** 필터를 사용하여 세분화할 때는 해당 고객 프로필에 값이 할당된 커스텀 속성이 이미 존재해야 합니다. Braze는 사용자를 적절하게 타겟팅하기 위해 '또는' 로직을 사용하여 커스텀 속성이 비어 있는지 확인할 것을 제안합니다.
{% endalert %}

{% alert tip %}
정규표현식 필터를 사용하는 방법에 대한 자세한 내용은 [Perl 호환 정규표현식(PCRE)](http://www.regextester.com/pregsyntax.html)의 이 설명서를 참조하세요.
<br>
정규식에 대한 추가 리소스:
- [Braze를 사용한 정규식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [정규식 디버거 및 테스터](https://regex101.com/)
- [정규식 튜토리얼](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### 배열

배열 속성은 사용자에 대한 관련 정보 목록을 저장하는 데 유용합니다. 예를 들어, 사용자가 마지막으로 시청한 100개의 콘텐츠를 배열에 저장하면 특정 관심사를 세분화할 수 있습니다.

사용자 지정 속성 배열은 1차원 집합이며, 다차원 배열은 지원되지 않습니다. **사용자 지정 속성 배열에 요소를 추가하면 해당 요소가 이미 존재하지 않는 한 배열의 끝에 추가되며, 이 경우 현재 위치에서 배열의 끝으로 이동합니다.** 예를 들어 `['hotdog','hotdog','hotdog','pizza']` 배열을 가져온 경우 배열 속성에 `['hotdog', 'pizza']`로 표시됩니다. 고유 값만 지원되기 때문입니다.

배열에 최대 요소 개수가 포함된 경우 첫 번째 요소는 삭제되고 새 요소가 끝에 추가됩니다. 다음은 웹 SDK의 배열 동작을 보여주는 예제 코드의 일부입니다.

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

커스텀 속성 배열의 최대 요소 개수 기본값은 25개입니다. 개별 배열의 최대치는 Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 최대 100개로 늘릴 수 있습니다. 이 최대 한도를 늘리려면 고객 서비스 관리자에게 문의하세요. 최대 요소 수를 초과하는 배열은 최대 요소 수를 포함하도록 잘립니다.

다음 표에서는 배열 속성에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 배열 속성에 입력한 값과 **정확히 일치하는 값이 포함**되었는지 확인합니다.| **가치 포함** | **문자열** |
| 배열 속성에 입력한 값과 **정확히 일치하는 값이 포함되지 않았는지** 확인합니다.| **값은 포함되지 않습니다.** | **문자열** |
| 배열 속성에 입력된 값 **또는** 정규표현식과 **부분 일치하는 값이 포함**되었는지 확인합니다. | **정규식 일치** | **문자열** **OR** **정규식** |
| 배열 속성에 **값이** 있는지 확인 | **값 포함** | **N/A** |
| 배열 속성이 **비어** 있는지 확인 | **비어 있음** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
당사는 [Perl 호환 정규식(PCRE)을](http://www.regextester.com/pregsyntax.html) 사용합니다.
{% endalert %}

#### 날짜

시간 속성은 특정 작업이 마지막으로 수행된 시간을 저장하는 데 유용하므로 사용자에게 콘텐츠별 재참여 메시지를 제공할 수 있습니다.

{% alert note %}
사용자 지정 이벤트 또는 구매 이벤트가 발생한 마지막 날짜는 자동으로 기록되며, 사용자 지정 시간 속성을 통해 중복으로 기록되어서는 안 됩니다.
{% endalert %}

상대 날짜(예: 1일 이상 이전, 2일 미만 이전)를 사용하는 날짜 필터는 하루를 24시간으로 계산합니다. 이 필터를 사용하여 실행하는 모든 캠페인에는 24시간 단위로 모든 사용자가 포함됩니다. 예를 들어, 1일 이상 이전에 마지막으로 사용한 앱은 캠페인이 실행된 정확한 시간부터 '24시간 넘게 앱을 마지막으로 사용한' 모든 사용자를 캡처합니다. 더 긴 날짜 범위로 설정된 캠페인도 마찬가지입니다. 활성화 후 5일은 이전 120시간을 의미합니다.

다음 표에서는 시간 속성에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 시간 속성이 **선택한 날짜** **이전**인지 확인합니다.| **전에** | **캘린더 날짜 선택기** |
| 시간 속성이 **선택한 날짜** **이후인지** 확인합니다.| **이후** | **캘린더 날짜 선택기** |
| 시간 속성이 **X일을 초과**한 **이전** 시점인지 확인합니다. | **초과** | **일수** |
| 시간 속성이 **X일 미만**의 **이전** 시점인지 확인합니다.| **미만** | **일수** |
| 시간 속성이 **향후 X일을 초과**한 **향후 일수**인지 확인합니다. | **향후 초과** | **향후 일수** |
| 시간 속성이 **X일 미만**의 **향후 일수**인지 확인합니다. | **미만** | **향후 일수**  |
| 사용자 **프로필에** 시간 속성이 있는지 확인합니다. | **비어 있음** | **N/A** |
| 사용자 프로필에 시간 속성이 **없는지** 확인합니다. | **비어 있지 않음** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 숫자 {#integers}

숫자 속성은 다양한 사용 사례가 있습니다. 증분 숫자 커스텀 속성은 특정 작업이나 이벤트가 발생한 횟수를 저장하는 데 유용합니다. 표준 번호는 신발 사이즈, 허리 사이즈 또는 사용자가 특정 제품 기능이나 카테고리를 조회한 횟수를 기록하는 등 다양한 용도로 활용됩니다.

{% alert note %}
이 방법으로 지출한 금액을 기록해서는 안 됩니다. 오히려 [구매 방법]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking)을 통해 기록해야 합니다.
{% endalert %}

다음 표에서는 숫자 속성에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 숫자 속성이 **숫자** **이상인지** 확인합니다.| **초과** | **숫자** |
| 숫자 속성이 **숫자보다** **작은** 지 확인합니다.| **미만** | **숫자** |
| 숫자 속성이 **정확히** **숫자인지** 확인합니다.| **정확히** | **숫자** |
| 숫자 속성이 **숫자**와 **같지 않은지** 확인합니다.| **동일하지 않음** | **숫자** |
| 고객 프로필에 숫자 속성이 **존재**하는지 확인합니다. | **존재** | **N/A** |
| 숫자 속성이 고객 프로필에 **존재하지 않는지** 확인합니다. | **존재하지 않음** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 부울(참/거짓)

부울 속성은 가입 상태 및 사용자에 대한 간단한 기타 이진 데이터를 저장하는 데 유용합니다. 제공되는 입력 옵션을 사용하면 해당 속성에 대한 기록이 아직 기록되지 않은 사용자 외에도 변수를 부울로 명시적으로 설정한 사용자를 찾을 수 있습니다.

다음 표에서는 부울 속성에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 부울 값이 **존재**하는지 확인합니다. | **IS**  | **참**, **거짓**, **참 또는 설정되지 않음** 또는 **거짓 또는 설정되지 않음** |
| 사용자 프로필에 부울 값이 **있는지** 확인합니다. | **존재**  | **N/A** |
| 사용자 프로필에 부울 값이 **없는지** 확인합니다. | **존재하지 않음**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 구매 이벤트 / 수익 추적

구매 방법을 사용하여 인앱 구매를 기록하면 각 개별 고객 프로필에 대한 생애주기 가치(LTV)가 설정됩니다. 이 데이터는 매출 페이지에서 시계열 그래프로 확인할 수 있습니다.

다음 표에서는 구매 이벤트에 사용할 수 있는 세분화 옵션에 대해 설명합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 총 지출 금액이 **숫자**보다 **큰지** 확인합니다.| **다음보다 큼** | **숫자** |
| 총 지출 금액이 **숫자**보다 **적은지** 확인합니다.| **미만** | **숫자** |
| 총 지출 **금액이 정확한** **수치인지** 확인합니다.| **정확히** | **숫자** |
| **X 날짜 이후에** 마지막으로 구매가 발생했는지 확인합니다. | **이후** | **시간** |
| **X 날짜 이전에** 마지막으로 구매가 발생했는지 확인합니다. | **전에** | **시간** |
| 마지막 구매가 **X일 전에** 발생했는지 확인합니다. | **초과** | **시간** |
| 마지막으로 구매한 날짜가 **X일 미만인지** 확인합니다. | **미만** | **시간** |
| 구매가 **X(최대 = 50)회 이상** 발생했는지 확인합니다. | **초과** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 구매가 **X(최대 = 50) 횟수 미만으로** 발생했는지 확인합니다. | **미만** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 구매가 **정확히 X회(최대 = 50)**만큼 발생했는지 확인합니다. | **정확히** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
특정 구매가 발생한 횟수를 기준으로 세분화하려면 해당 구매를 [증분 커스텀 속성](#integers)으로 개별적으로 기록해야 합니다.
{% endalert %}

## 택시/차량 공유 앱 사용 사례 {#example-case}

이 예제에서는 어떤 사용자 데이터를 수집할지 결정하려는 차량 공유 앱을 생각해 보겠습니다. 다음 질문과 브레인스토밍 프로세스는 마케팅팀과 개발팀이 따라야 할 훌륭한 모델입니다. 이 연습이 끝나면 두 팀 모두 목표를 달성하기 위해 수집할 올바른 커스텀 이벤트와 속성을 파악할 수 있습니다.

**사례 질문 #1: 목표는 무엇인가요?**

목표는 간단합니다. 사용자는 앱을 통해 택시를 호출하는 것입니다.

**사례 질문 #2: 앱 설치부터 목표 사이의 중간 단계는 무엇인가요?**

1. 사용자는 등록 절차를 시작하고 개인 정보를 입력해야 합니다.
2. 사용자는 SMS를 통해 받은 앱에 코드를 입력하여 등록 절차를 완료하고 인증해야 합니다.
3. 택시를 호출해야 합니다.
4. 택시를 호출하려면 검색 시 택시를 이용할 수 있어야 합니다.

이러한 작업은 다음과 같은 사용자 지정 이벤트로 태그를 지정할 수 있습니다:

- 등록 시작
- 등록 완료
- 성공적인 택시 호출
- 택시 호출 실패

이벤트를 구현한 후 이제 다음 캠페인을 실행할 수 있습니다:

1. 등록을 시작했지만 특정 시간 내에 등록 완료 이벤트가 트리거되지 않은 사용자에게 메시지를 보냅니다.
2. 등록을 완료한 사용자에게 축하 메시지를 보냅니다.
3. 택시 호출에 실패한 사용자(일정 시간 내에 성공적인 택시 호출이 없는 사용자)에게 사과와 프로모션 크레딧을 보냅니다.
4. 택시 호출에 성공한 횟수가 많은 우수 고객에게 프로모션을 보내 충성도에 대한 감사의 마음을 전합니다.

이외에도 다양한 기능이 있습니다!

**사례 질문 #3: 메시징을 알리기 위해 사용자에 대해 알아야 할 다른 정보로 무엇이 있나요?**

- 프로모션 크레딧이 있는지 여부는?
- 드라이버에게 평균적으로 어떤 평점을 주나요?
- 사용자를 위한 고유한 프로모션 코드가 있나요?

그런 다음 이러한 특성에 다음과 같은 사용자 지정 속성으로 태그를 지정할 수 있습니다:

- 프로모션 크레딧 잔액(십진수 유형)
- 평균 운전자 평점(번호 유형)
- 고유 프로모션 코드(문자열 유형)

이러한 속성을 추가하면 사용자에게 다음과 같은 캠페인을 보낼 수 있습니다:

1. 7일 동안 로그인하지 않았지만 프로모션 크레딧이 있는 사용자에게 크레딧이 존재하며 앱으로 돌아와서 크레딧을 사용해야 한다는 사실을 알려주세요!
2. 낮은 운전자 평점을 준 사용자에게 메시지를 보내 라이딩이 만족스럽지 않은 이유를 직접 확인하고 고객 피드백을 받습니다.
3. [메시지 템플릿 및 개인화 기능을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) 사용하여 고유 프로모션 코드 속성을 사용자를 대상으로 하는 메시지에 끌어다 놓을 수 있습니다.

## 모범 사례

### 일반적인 모범 사례

#### 이벤트 속성 사용

- 커스텀 이벤트 이름은 사용자가 수행하는 작업을 설명하는 내용으로 지정합니다.
- 이벤트에 대한 중요한 데이터를 표현하기 위해 사용자 지정 이벤트 속성을 충분히 활용하세요.
- 예를 들어, 50개의 서로 다른 영화를 각각 시청할 때마다 별도의 사용자 지정 이벤트를 캡처하는 것보다 단순히 영화 시청을 이벤트로 캡처하고 영화 이름이 포함된 이벤트 속성을 갖는 것이 더 효과적일 수 있습니다.

### 개발 모범 사례

#### 모든 사용자에 대한 사용자 ID 설정

각 사용자에 대해 사용자 ID를 설정해야 합니다. 사용자가 앱을 열었을 때 변경되지 않고 액세스할 수 있어야 합니다. 이 식별자를 제공하는 것이 **좋습니다**. 그러면 다음과 같은 기능을 수행할 수 있습니다.

- 여러 기기와 플랫폼에서 사용자를 추적하여 행동 및 인구 통계 데이터의 품질을 개선합니다.
- [사용자 데이터 API를]({{site.baseurl}}/api/endpoints/user_data/) 사용하여 사용자에 대한 데이터를 가져옵니다.
- 일반 메시지와 트랜잭션 메시지 모두에 대한 [메시징 API로]({{site.baseurl}}/api/endpoints/messaging/) 특정 사용자를 타겟팅하세요.

사용자 ID는 512자 미만이어야 하며, 쉽게 알아낼 수 없는 비공개 항목이어야 합니다(예: 일반 이메일 주소나 사용자 이름이 아님). 이러한 식별자를 사용할 수 없는 경우, Braze는 사용자에게 고유 식별자를 할당하지만 사용자 ID에 나열된 기능은 사용할 수 없습니다. 개인과 연결된 고유 식별자가 없는 사용자에 대해서는 사용자 ID를 설정하지 않아야 합니다. 기기 식별자를 전달해도 Braze에서 기본적으로 제공하는 자동 익명 사용자 추적 기능과 비교했을 때 아무런 이점이 없습니다. 다음은 적합한 사용자 아이디와 부적합한 사용자 아이디의 몇 가지 예입니다.

다음은 사용자 ID로 적합한 옵션입니다.

- 해시된 이메일 주소 또는 고유 사용자 이름
- 고유 데이터베이스 식별자

사용자 아이디로 사용해서는 안 됩니다:

- 기기 ID
- 난수 또는 세션 ID
- 고유하지 않은 모든 ID
- 이메일 주소
- 다른 타사 공급업체의 사용자 ID

{% multi_lang_include sdk_auth_alert.md %}

#### 사용자 지정 이벤트 및 속성에 읽기 쉬운 이름 부여

구현 후 1~2년이 지나 Braze를 사용하기 시작한 마케터인데 추가 컨텍스트 없이 'usr_no_acct' 같은 이름으로 가득 찬 드롭다운 목록을 읽는다면 부담스러울 수 있습니다. 이벤트와 속성에 식별 가능하고 읽기 쉬운 이름을 부여하면 플랫폼의 모든 사용자가 더 쉽게 작업할 수 있습니다. 다음 모범 사례를 고려하세요:

- 숫자 문자로 사용자 지정 이벤트를 시작하지 마세요. 드롭다운 목록은 알파벳순으로 정렬되며 숫자로 시작하면 원하는 필터로 분류하기가 더 어려워집니다.
- 가능한 한 모호한 약어나 전문 용어를 사용하지 마세요.
  - 예: 코드 내에서 사용자의 국가에 대한 변수 이름으로 `usr_ctry`를 사용해도 괜찮지만, 대시보드를 사용하는 마케터가 명확하게 이해할 수 있도록 하려면 커스텀 속성을 `user_country`와 같은 이름으로 Braze에 전송해야 합니다.

#### 속성이 변경될 때만 로그 기록

전달된 속성에 이전에 저장된 속성과 동일한 값이 포함되어 있더라도 Braze에 전달된 모든 속성을 데이터 포인트로 계산합니다. 데이터가 변경될 때만 로깅하면 데이터 포인트의 중복 사용을 방지하고 불필요한 API 호출을 피해 보다 원활한 환경을 지원할 수 있습니다.

#### 이벤트 이름을 프로그래밍 방식으로 생성하지 마십시오.

이벤트 이름을 계속 새로 만들면 사용자를 의미 있게 세분화하는 것이 불가능해집니다. 일반적으로 '강남 스타일 시청' 또는 '기사 읽기: 미드타운 맨해튼의 점심 명소 10위'와 같이 매우 구체적인 이벤트 대신 '동영상 시청' 또는 '기사 읽기'와 같은 일반적인 이벤트를 캡처하는 것이 좋습니다. 이벤트에 대한 특정 데이터는 이벤트 이름의 일부가 아닌 이벤트 속성정보로 포함되어야 합니다.

### 기술적 한계 및 제약

커스텀 이벤트를 구현할 때는 다음과 같은 한계와 제약 조건에 유의하세요.

#### 길이 제약 조건

255자 이상의 모든 커스텀 이벤트, 커스텀 속성 이름(키) 및 커스텀 이벤트 문자열 값은 잘립니다. 앱의 네트워크 및 배터리 성능을 개선하기 위해 가능한 한 짧게 설정하는 것이 가장 이상적입니다. 가능하면 50자로 제한합니다.

#### 콘텐츠 제약 조건
다음 콘텐츠는 속성 및 이벤트에서 프로그래밍 방식으로 트리밍됩니다. 다음을 사용하지 않도록 주의하세요:

- 선행 및 후행 공백
- 줄바꿈
- 전화번호 내 숫자가 아닌 모든 문자
  - 예: "(732) 178-1038"은 "7321781038"로 축약됩니다.
- 공백이 아닌 문자는 공백으로 변환해야 합니다.
- 사용자 지정 이벤트의 접두사로 $를 사용해서는 안 됩니다.
- 잘못된 UTF-8 인코딩 값
  -  "내 \\x80 필드"는 "내 필드"로 압축됩니다.

#### 예약 키

다음 키는 예약되어 있으며 커스텀 이벤트 속성으로 사용할 수 없습니다:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### 가치 정의

- 정수 값은 64비트임
- 소수점은 기본적으로 소수점 이하 15자리입니다.

### 일반 이름 필드 구문 분석하기

사용자에 대해 하나의 일반 이름 필드만 존재하는 경우(예: 'JohnDoe'), 이 전체 제목을 사용자의 이름 속성에 할당할 수 있습니다. 공백을 사용하여 사용자의 이름과 성을 모두 구문 분석할 수도 있지만, 후자의 방법은 일부 사용자의 이름이 잘못 지정될 수 있는 잠재적 위험이 있습니다.
