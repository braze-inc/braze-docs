---
nav_title: mParticle by Rokt
article_title: mParticle by Rokt
alias: /partners/mparticle/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 mParticle과 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# mParticle by Rokt

{% multi_lang_include video.html ID="Njhqwd36gZM" align="right" %}

> mParticle의 고객 데이터 플랫폼은 데이터로 더 많은 성과를 낼 수 있도록 지원합니다. 노련한 마케터는 회사의 성장 스택 전반에 걸쳐 데이터를 오케스트레이션하는 데 mParticle을 사용하여 고객 여정의 주요 순간마다 앞서갈 수 있도록 합니다.

Braze와 mParticle의 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다.
- Braze 캠페인 및 캔버스 세분화를 위해 Braze에 mParticle 오디언스를 동기화합니다.
- 두 플랫폼 간에 데이터를 공유합니다. mParticle 키트 통합 및 서버 간 통합을 통해 수행할 수 있습니다.
- [커런츠를 통해 Braze 사용자 상호 작용을 통해 mParticle로 전송]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/)하여 전체 성장 스택에서 실행 가능하게 합니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| mParticle 계정 | 이 파트너십을 활용하려면 [mParticle 계정](https://app.mparticle.com/login)이 필요합니다. |
| 브레이즈 인스턴스 | Your Braze instance can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints) (for example, `US-01` or `US-02`). |
| Braze 앱 식별자 키 | 앱 식별자 키. <br><br>이는 **Braze 대시보드 > 설정 관리 > API 키** 내에서 찾을 수 있습니다. |
| 워크스페이스 REST API 키 | (서버-투-서버) A Braze REST API key<br><br>이것은 **Braze 대시보드 > 개발자 콘솔 > API 설정 > API 키** 내에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 오디언스

Braze와 mParticle의 파트너십을 사용하여 통합을 구성하고 리타겟팅을 위해 mParticle 오디언스를 Braze로 직접 가져와 한 시스템에서 다른 시스템으로 데이터를 완전하게 순환시킬 수 있습니다. 설정한 모든 통합은 계정의 데이터 포인트 볼륨 계산에 포함됩니다.

#### 오디언스 전달

mParticle은 '[세그먼트 전송 형식](#send_settings)' 구성 설정에 의해 제어되는 코호트 멤버십 속성을 설정하는 세 가지 방법을 제공합니다. 다음 섹션을 참조하여 각 옵션의 처리 방법을 확인하십시오:

- [단일 문자열 속성](#string)
- [단일 배열 속성](#array)
- [세그먼트당 하나의 속성](#per-segment)
- [단일 배열 속성과 단일 문자열 속성](#both-1)
- [단일 배열 속성과 세그먼트당 하나의 속성](#both-2)
- [단일 문자열 속성과 세그먼트당 하나의 속성](#both-3)
- [단일 배열 속성, 단일 문자열 속성 및 세그먼트당 하나의 속성](#multi)

##### 단일 문자열 속성 {#string}

mParticle는 `SegmentMembership`이라는 단일 커스텀 속성을 생성합니다. 이 속성의 값은 사용자와 일치하는 쉼표로 구분된 mParticle 오디언스 ID 문자열입니다. 이 오디언스 ID는 mParticle 대시보드의 **오디언스**에서 찾을 수 있습니다.

예를 들어, mParticle 오디언스 "Ibiza dreamers"가 오디언스 ID "11036"을 가지고 있다면, 이 사용자들을 필터 `SegmentMembership` — `matches regex` — `11036`로 세그먼트할 수 있습니다.

mParticle의 기본 옵션이지만, 대부분의 Braze 사용자는 Braze에서 세그먼트를 생성할 때 필터링 경험을 위해 [단일 배열 속성](#array)을 사용합니다.

{% alert important %}
이 솔루션은 여러 오디언스를 보유하고 있는 경우 권장되지 않습니다. 커스텀 속성은 최대 255자까지 가능하기 때문입니다. 따라서 이 방법을 사용하여 수십 또는 수백 개의 오디언스를 저장할 수 없습니다. 사용자당 코호트 수가 많은 경우 '세그먼트당 하나의 속성' 구성을 강력히 권장합니다.
{% endalert %}

![mParticle 세그먼트 membership][6]

##### 단일 배열 속성 {#array}

mParticle은 각 사용자에 대해 Braze의 단일 커스텀 배열 속성(`SegmentMembershipArray`)을 생성합니다. 이 속성의 값은 사용자와 일치하는 mParticle 오디언스 ID 배열입니다.

예를 들어, 사용자가 오디언스 ID가 '13053', '13052', '13051'인 세 개의 mParticle 오디언스의 구성원인 경우, `SegmentMembershipArray` - `includes value` - `13051` 필터를 사용하여 해당 오디언스 중 하나와 일치하는 사용자를 세분화할 수 있습니다.

{% alert note %}
Braze 배열 속성의 최대 길이는 25입니다. 사용자가 25명이 넘는 오디언스의 구성원인 경우, Braze에 의해 멤버십 정보가 잘립니다. 이 문제를 해결하려면 Braze 담당자에게 연락하여 최대 배열 길이 임계값을 늘리십시오.
{% endalert %}

##### 세그먼트당 하나의 속성 {#per-segment}

mParticle은 사용자가 속한 각 오디언스에 대해 부울 커스텀 속성을 생성합니다. 예를 들어, mParticle 오디언스가 'Possible Parisians'인 경우, 이 사용자는 `In Possible Parisians` - `equals` - `true` 필터로 세분화할 수 있습니다.

![mParticle 커스텀 속성][7]

##### 단일 배열 속성과 단일 문자열 속성 {#both-1}

mParticle은 단일 배열 속성과 단일 문자열 속성 모두에서 설명한 대로 속성을 전송합니다.

##### 단일 배열 속성과 세그먼트당 하나의 속성 둘 다 {#both-2}

mParticle은 단일 배열 속성과 세그먼트당 하나의 속성 모두에서 설명한 대로 속성을 전송합니다.

##### 단일 문자열 속성과 세그먼트당 하나의 속성 둘 다 {#both-3}

mParticle은 단일 문자열 속성과 세그먼트당 하나의 속성 모두에서 설명한 대로 속성을 전송합니다.

##### 단일 배열 속성, 단일 문자열 속성과 세그먼트당 하나의 속성 둘 다 {#multi}

mParticle은 단일 배열 속성, 단일 문자열 속성과 세그먼트당 하나의 속성 모두에서 설명한 대로 속성을 전송합니다.

#### 1단계: mParticle에서 오디언스 생성{#send_settings}

mParticle에서 오디언스를 생성하려면:

1. **오디언스** > **단일 작업 공간** > **\+ 새 오디언스**.
2. 오디언스를 위한 출력으로 Braze를 연결하려면 다음 필드를 제공해야 합니다.

| 필드 이름               | 설명                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API 키                  | Braze 대시보드의 **설정** > **API 키**에서 찾을 수 있습니다.<br><br>이전 탐색을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 찾을 수 있습니다. |
| API 키 운영 체제 | 어떤 운영 체제에 해당하는 Braze API 키를 선택하십시오. 이 선택은 오디언스 업데이트에서 전달되는 푸시 토큰의 유형을 제한합니다.                          |
| 세그먼트 보내기         | Braze로 오디언스를 보내는 방법. 자세한 내용은 [오디언스 전달](#forwarding-audiences) 섹션을 참조하세요.                                                          |
| 워크스페이스 REST API 키   | 전체 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.                                                        |
| 외부 ID 유형   | mParticle 사용자 ID 유형을 Braze에 외부 ID로 전달합니다. 기본값(고객 ID)으로 두는 것이 좋습니다.                                          |
| 이메일 ID 유형      | 이메일로 Braze에 전달할 mParticle 사용자 ID 유형.                                                                                                            |
| 브레이즈 인스턴스           | 어느 클러스터로 Braze 데이터가 전달될지 지정하십시오.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. 마지막으로, 오디언스를 **저장**합니다.

몇 분 내에 Braze로 동기화되는 오디언스가 표시되기 시작합니다. 오디언스 멤버십은 `external_ids`를 가진 사용자(즉, 익명 사용자가 아닌 사용자)에 대해서만 업데이트됩니다. Braze mParticle 오디언스를 생성하는 방법에 대한 자세한 내용은 [구성 설정](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)에 대한 mParticle 설명서를 참조하세요.

#### 2단계: Braze에서 세그먼트 사용자

Braze에서 이러한 사용자의 세그먼트를 만들려면 **세그먼트**에서 **참여**로 이동하여 세그먼트의 이름을 지정하십시오. 다음은 **Send segments as**에 대해 선택한 옵션에 따라 달라지는 두 가지 예입니다. 자세한 옵션은 [오디언스 전달](#forwarding-audiences.)을 참조하세요.

- **단일 배열 속성:** `SegmentMembershipArray`를 필터로 선택합니다. 다음으로, '값 포함' 옵션을 사용하고 원하는 오디언스 ID를 입력합니다. ![mParticle 세그먼트 필터 'SegmentMembershipArray'를 '값 포함'으로 설정하고 오디언스 ID를 입력합니다.][11]<br><br>
- **세그먼트당 하나의 속성:** 귀하의 커스텀 속성을 필터로 선택하십시오. 다음으로, '같음' 옵션을 사용하고 적절한 논리를 선택합니다. ![mParticle 세그먼트 필터 'in possible parisians'을 '같음' 및 'true'로 설정합니다.][8]

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

#### 연결 비활성화 및 삭제

mParticle는 Braze에서 세그먼트를 직접적으로 유지 관리하지 않기 때문에 해당 mParticle 오디언스 연결이 삭제되거나 비활성화될 때 세그먼트를 삭제하지 않습니다. 이런 일이 발생하면, mParticle은 각 사용자에서 오디언스를 제거하기 위해 Braze에서 오디언스 사용자 속성을 업데이트하지 않습니다.

삭제하기 전에 Braze 사용자에서 오디언스를 제거하려면, 오디언스 필터를 조정하여 강제로 오디언스 크기를 0으로 만든 후 오디언스를 삭제합니다. 오디언스 계산이 완료되어 사용자 수가 0명이 되면 오디언스를 삭제합니다. 그런 다음, 오디언스 멤버십은 단일 속성 옵션에 대해 Braze에서 `false`로 업데이트되거나 배열 형식에서 오디언스 ID를 제거합니다.

## 데이터 매핑

데이터는 [임베디드 키트 통합](#embedded-kit-integration)을 사용하여 Braze에 매핑될 수 있으며, mParticle을 통해 모바일 및 웹 앱을 Braze에 연결할 수 있습니다. [서버 간 API 통합](#server-api-integration)을 사용하여 서버 측 데이터를 Braze로 전달할 수도 있습니다.

어떤 접근 방식을 선택하든 Braze를 출력으로 설정해야 합니다.

### Braze 출력 설정을 구성하십시오

mParticle에서 **설정 > 출력 > 출력 추가**로 이동하여 **Braze**를 선택하고 Braze 키트 구성을 엽니다. 완료되면 **저장**합니다.

| 설정 이름 | 설명 |
| ------------ | ----------- |
| Braze 앱 식별자 키 | 귀하의 Braze 앱 식별자 키는 **설정** > **API 키**의 Braze 대시보드에서 찾을 수 있습니다. API 키는 플랫폼(iOS, Android, 웹)마다 다릅니다. |
| 외부 ID 유형 | mParticle 사용자 ID 유형을 Braze에 외부 ID로 전달합니다. 기본값(고객 ID)으로 두는 것이 좋습니다. |
| 이메일 ID 유형 | mParticle 사용자 ID 유형을 이메일로 Braze에 전달합니다. 기본값(이메일)으로 두는 것이 좋습니다. |
| 브레이즈 인스턴스 | Braze 데이터를 전달하는 클러스터로, 대시보드가 있는 클러스터와 동일해야 합니다. |
| 이벤트 스트림 전달 사용 | (서버 간) 활성화되면 모든 이벤트가 실시간으로 전달됩니다. 그렇지 않으면 모든 이벤트가 대량으로 전달됩니다. 이벤트 스트림 전달을 활성화하도록 선택할 때, Braze에 전달하는 데이터는 [사용량 제한]({{site.baseurl}}/api/api_limits/)을 준수해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][10]

### 임베디드 키트 통합

mParticle 및 Braze SDK는 내장 키트 통합을 통해 애플리케이션에 존재합니다. 하지만 직접적인 Braze 통합과 달리, mParticle에서 대부분의 Braze SDK 메서드를 대신 호출합니다. The mParticle methods you use to track user data will automatically be mapped to the Braze SDK methods. 

[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) 및 [웹](https://github.com/Appboy/integration-appboy)용 mParticle SDK에 대한 이러한 매핑은 오픈 소스이며 [mParticle의 GitHub 페이지](https://github.com/mparticle-integrations)에서 찾을 수 있습니다. 

임베디드 키트 SDK 통합을 통해 전체 기능 세트(푸시, 인앱 메시지 및 모든 관련 메시지 분석 추적)를 활용할 수 있습니다.

{% alert note %}
콘텐츠 카드 및 커스텀 인앱 메시지 통합의 경우 Braze SDK 메서드를 직접 호출합니다.
{% endalert %}

#### 1단계: mParticle SDK 통합

플랫폼 요구 사항에 따라 적절한 mParticle SDK를 앱에 통합합니다.

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### 2단계: mParticle의 Braze 이벤트 키트 통합을 완료하십시오

Braze SDK는 이 mParticle 통합을 위해 웹사이트나 앱에 직접 포함될 필요는 없지만, 앱에서 Braze로 데이터를 전달하기 위해 다음 mParticle Appboy 키트를 설치해야 합니다.

mParticle의 [Braze 이벤트 키트 통합 가이드](https://docs.mparticle.com/integrations/braze/event/#kit-integration)에서는 메시징 요구 사항(푸시, 위치 추적 등)에 따라 커스텀 mParticle 및 Braze 정렬 지침을 안내합니다.

#### 3단계: Braze 출력에 대한 연결 설정

mParticle에서 **연결 > 연결 > [원하는 플랫폼] > 출력 연결**로 이동하여 Braze를 출력으로 추가합니다. 완료되면 **저장**합니다.

![][3]

모든 연결 설정이 모든 플랫폼 및 통합 유형에 적용되는 것은 아닙니다. 연결 설정 및 적용되는 플랫폼에 대한 분석은 [mParticle 설명서](https://docs.mparticle.com/integrations/braze/event/#connection-settings)를 참조하세요.

### 서버 API 통합

mParticle의 서버 측 SDK(예: Ruby, Python 등)를 사용하는 경우 백엔드 데이터를 Braze로 라우팅하기 위한 애드온입니다. Braze와 이 서버 간 통합을 설정하려면 [mParticle의 설명서](https://docs.mparticle.com/guides/platform-guide/connections/)를 따르세요.

{% alert important %}
서버 간 통합은 인앱 메시징, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 메서드를 통해 사용할 수 없는 기기 수준 필드와 같이 자동으로 캡처된 데이터도 존재합니다. 

이 기능을 사용하려면 병렬 통합을 고려합니다.

서버 측 데이터를 Braze로 전달하려면 `external_id`를 포함해야 합니다. 익명 사용자는 전달되지 않습니다.
{% endalert %}

#### Braze 출력에 대한 연결 설정

mParticle에서 **연결 > 연결 > [원하는 플랫폼] > 출력 연결**로 이동하여 Braze를 출력으로 추가합니다. 완료되면 **저장**합니다. 

![][4]

모든 연결 설정이 모든 플랫폼 및 통합 유형에 적용되는 것은 아닙니다. 연결 설정 및 적용되는 플랫폼에 대한 분석은 [mParticle 설명서](https://docs.mparticle.com/integrations/braze/event/#connection-settings)를 참조하세요.

'향상된 사용자 속성' 또는 '향상된 사용자 ID'를 활성화하기 전에 [데이터 포인트 초과량](#potential-data-point-overages)을 검토하여 이러한 설정이 데이터 포인트 사용량에 어떤 영향을 미치는지 확인하는 것이 좋습니다.

### 데이터 매핑 세부사항

#### 데이터 유형
모든 데이터 유형이 두 플랫폼 간에 지원되는 것은 아닙니다.
- [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)는 문자열, 숫자, 부울 또는 날짜 오브젝트를 지원합니다. 배열이나 중첩된 객체를 지원하지 않습니다.
- [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)은 문자열, 숫자, 부울, 날짜 오브젝트 및 배열을 지원하지만 오브젝트나 중첩 오브젝트는 지원하지 않습니다. 

{% alert note %}
Braze는 `Time` 유형의 커스텀 속성에서 연도 0 이전 또는 3000년 이후의 타임스탬프를 지원하지 않습니다. Braze는 mParticle이 이러한 값을 보낼 때 수집하지만, 해당 값은 문자열로 저장됩니다.
{% endalert %}

#### 데이터 매핑

| mParticle 데이터 유형 | Braze 데이터 유형 | 설명 |
| ------------------- | --------------- | ----------- |
| 사용자 속성 (예약) | 표준 속성 | 예를 들어, mParticle의 `$FirstName` 예약 사용자 속성 키는 Braze의 `first_name` 표준 속성 필드에 매핑됩니다. |
| 사용자 속성 (기타) | 커스텀 속성 | mParticle에 전달된 모든 사용자 속성이 예약된 사용자 속성 키를 벗어나는 경우 Braze에 커스텀 속성으로 기록됩니다.<br><br>사용자 속성은 문자열, 숫자, 부울, 날짜 및 배열을 지원하지만 오브젝트나 중첩된 오브젝트는 지원하지 않습니다. |
| 사용자 지정 이벤트 | 사용자 지정 이벤트 | mParticle 커스텀 이벤트는 Braze에서 커스텀 이벤트로 인식됩니다. 이벤트 속성은 커스텀 이벤트 속성으로 전달됩니다.<br><br>Braze에 전달된 이벤트 속성정보로 전달되는 이벤트 속성은 문자열, 숫자, 부울 또는 날짜 오브젝트를 지원하지만 배열이나 중첩된 오브젝트는 지원하지 않습니다. |
| 구매 상거래 이벤트 | 구매 이벤트 | 구매 상거래 이벤트는 Braze 구매 이벤트에 매핑됩니다. <br><br>주문 수준 또는 제품 수준으로 구매를 기록려면 번들 상거래 이벤트 데이터에 대한 설정 값을 토글합니다. 예를 들어, `false`인 경우 두 개의 고유 제품, 프로모션 또는 노출 횟수를 포함하는 단일 수신 이벤트로 인해 적어도 두 개의 발신 Braze 이벤트가 발생합니다. `true`로 설정된 경우 중첩된 제품, 프로모션 또는 노출 횟수 배열을 각각 포함하는 단일 발신 이벤트가 발생합니다.<br><br>기록할 추가 상거래 필드에 대한 자세한 내용은 [mParticle 설명서](https://docs.mparticle.com/integrations/braze/event/#purchase-events)를 참조하세요. <br><br>'번들 상거래 이벤트 데이터'를 Braze에 구매 이벤트 속성정보로 전달되는 `false` 제품 속성으로 설정하면 문자열, 숫자, 부울 또는 날짜 오브젝트를 지원하지만 배열이나 중첩된 오브젝트는 지원하지 않습니다.|
| 모든 기타 상거래 이벤트 | 사용자 지정 이벤트 | 다른 모든 상거래 이벤트는 커스텀 이벤트로 매핑됩니다. <br><br>주문 수준 또는 제품 수준으로 구매를 기록려면 번들 상거래 이벤트 데이터에 대한 설정 값을 토글합니다. 예를 들어, `false`인 경우 두 개의 고유 제품, 프로모션 또는 노출 횟수를 포함하는 단일 수신 이벤트로 인해 적어도 두 개의 발신 Braze 이벤트가 발생합니다. `true`로 설정된 경우 중첩된 제품, 프로모션 또는 노출 횟수 배열을 각각 포함하는 단일 발신 이벤트가 발생합니다.<br><br>기본 상거래 가치 외에도, 제품 속성은 Braze 이벤트 속성정보로 기록됩니다. 기록할 추가 상거래 필드에 대한 자세한 내용은 [mParticle 설명서](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)를 참조하세요.<br><br>'번들 상거래 이벤트 데이터'를 Braze에 이벤트 속성정보로 전달되는 `false` 제품 속성으로 설정하면 문자열, 숫자, 부울 또는 날짜 오브젝트를 지원하지만 배열이나 중첩된 오브젝트는 지원하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 사용자 아이덴티티 매핑
각 mParticle 출력에 대해 Braze에 `external_id`로 보낼 외부 ID 유형을 선택할 수 있습니다. 기본값은 고객 ID이지만 `MPID`와 같은 다른 ID를 Braze에 `external_id`로 보낼 수 있습니다. 고객 ID가 아닌 식별자를 선택하면 Braze에서 데이터가 전송되는 방식에 영향을 미칠 수 있습니다. 

예를 들어, MPID를 Braze `external_id`에 매핑하면 다음과 같은 효과가 있습니다.
- MPID가 할당된시점의 특성상 모든 사용자는 세션 시작 시 `external_id`가 할당됩니다.
- 커런츠 설정은 MPID와 `external_id` 간의 데이터 유형 차이로 인해 추가 매핑이 필요할 수 있습니다.

### 지우기 요청(데이터 주체 요청) 전달

Braze로 데이터 주체 요청 출력을 구성하여 Braze로 지우기 요청을 전달합니다. Braze로 삭제 요청을 전달하려면 [mParticle의 설명서](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)를 따르세요.

## 잠재적인 데이터 포인트 초과

### 강화된 사용자 속성

#### 사용자 속성/ID 보강 활성화(서버 간 전용) {#enriched}

mParticle 연결 설정에서 Braze는 **보강된 사용자 속성 포함**을 끌 것을 권장합니다. 활성화된 경우, mParticle은 기존 프로필에서 사용 가능한 모든 사용자 속성(예: 표준 속성, 커스텀 속성 및 계산된 속성)을 기록된 각 이벤트에 대해 Braze로 전달합니다. 이로 인해 mParticle은 호출마다 Braze에 동일한 변경되지 않은 속성을 전송하기 때문에 데이터 포인트의 소비가 늘어납니다.

예를 들어, 사용자가 첫 번째 세션 동안 이름, 성, 전화번호를 추가하고 나중에 뉴스레터에 가입하면서 이메일 외에 동일한 정보를 추가하고 뉴스레터 가입 이벤트를 트리거하는 경우:
- 켜진 경우(기본값), 다섯 개의 데이터 포인트가 발생합니다(가입 이벤트, 이메일 주소, 이름, 성, 및 전화번호).
- 비활성화된 경우 두 개의 데이터 포인트가 발생합니다 (가입 이벤트 및 이메일 주소)

{% alert note %}
이 설정을 끄면 데이터 변경 여부를 확인하지 않습니다. 그러나 통합이 원래의 인바운드 배치에서 수신되지 않았거나 이벤트의 속성으로 명시적으로 설정되지 않은 사용자의 프로필에 있는 모든 사용자 속성을 보내지 못하게 할 것입니다. 여전히 델타만 Braze에 전달되는지 확인하는 것이 중요합니다.
{% endalert %}

#### 강화된 사용자 속성 끄기 고려 사항

**보강된 사용자 속성 포함**을 끌 때 주의해야 할 몇 가지 고려 사항이 있습니다.
1. 서버-투-서버 통합은 mParticle 이벤트 API를 사용하여 이벤트를 Braze로 전송합니다. 각 요청은 이벤트에 의해 트리거됩니다. 예를 들어, 이메일 주소를 업데이트할 때와 같이 사용자 속성이 변경되지만 특정 이벤트(예: 프로필 업데이트 커스텀 이벤트)와 연결되지 않은 경우, 새로운 값은 사용자에 의해 트리거된 다음 이벤트의 페이로드에서 '보강된 속성'으로 Braze와 같은 출력에만 전달됩니다. **보강된 사용자 속성 포함**이 꺼져 있으면 특정 이벤트와 관련되지 않은 이 새로운 속성 값은 Braze로 전달되지 않습니다.
  - 이를 해결하기 위해 업데이트된 특정 사용자 속성만 Braze에 전송하는 별도의 "사용자 속성 업데이트됨" 이벤트를 생성할 것을 권장합니다. 이 접근 방식을 사용하면 '사용자 속성 업데이트됨' 이벤트에 대해 추가 데이터 포인트를 여전히 기록하지만, 이 기능이 활성화된 모든 호출에서 모든 사용자 속성을 보내는 것보다 데이터 포인트 소비가 훨씬 적습니다.
2. 계산된 속성은 Braze에 보강된 사용자 속성으로 전달되므로 '보강된 사용자 속성'을 끄면 더 이상 Braze에 전달되지 않습니다. "Enriched User Attributes"가 꺼져 있을 때 계산된 속성을 Braze로 전달하려면 모든 속성을 푸시하지 않고도 [계산된 속성 피드](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)가 도움이 될 수 있습니다. 계산된 속성이 변경되면 피드는 Braze로 다운스트림 업데이트를 실행합니다. 

### Braze에 불필요하거나 중복된 데이터를 보내기
Braze는 속성이 Braze에 전달될 때마다 값이 변경되지 않더라도 데이터 포인트를 계산합니다. 이러한 이유로 Braze는 Braze 내에서 작업을 수행하는 데 필요한 데이터만 전달하고 속성의 델타만 전달되도록 권장합니다.

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[11]: {% image_buster /assets/img_archive/mparticle5.png %}
[5]: \#embedded-kit-통합
