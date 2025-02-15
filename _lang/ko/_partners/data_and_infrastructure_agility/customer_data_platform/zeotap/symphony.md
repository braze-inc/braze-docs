---
nav_title: Zeotap Symphony
description: "이 참조 문서에서는 ID 확인, 인사이트 및 보강 기능을 제공하는 차세대 고객 데이터 플랫폼인 Zeotap와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zoetap Symphony

Braze와 Zoetap Symphony 통합을 통해 실시간 오케스트레이션을 생성하고 이메일 및 푸시 알림 캠페인을 실행할 수 있습니다.

- Braze를 통해 개인화된 이메일을 전송할 수 있는 사용자에 따라 Zeotap을 통해 이름과 성을 전송합니다.
- Zeotap을 통해 실시간으로 커스텀 이벤트 또는 구매 이벤트를 전송하면 사용자가 Braze 내에서 캠페인 트리거를 생성하여 고객을 타겟팅할 수 있습니다

{% alert note %}
이메일 마케팅 캠페인을 생성하려면 Zeotap 카탈로그에서 `Email Raw`에 원시 이메일을 매핑하여 Zeotap에서 온보딩합니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 클라이언트 이름 | 이것은 귀하의 Braze 계정에 대한 클라이언트 이름입니다. Braze 콘솔로 이동하여 찾을 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 인스턴스 | 귀하의 Braze 인스턴스는 Braze 온보딩 매니저에게서 얻을 수 있거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 통합

이 섹션에서는 Braze와 통합할 수 있는 두 가지 방법에 대한 정보를 제공합니다:

### 방법 1
이 방법에서는 다음 작업을 수행해야 합니다:
1. 웹사이트나 앱에서 Braze SDK를 통합합니다.
2. Symphony를 통해 Braze와 Zeotap을 통합합니다.

- `User traits`는 **전송할 데이터** 탭 아래 해당 Braze 필드에 매핑되어야 합니다. `Event` 및 `Purchase` 속성을 매핑하면 Braze 내에서 이벤트가 중복됩니다.
- Braze SDK를 설정하는 동안 구성된 `User ID`에 `External ID`를 매핑합니다.

통합이 성공적으로 설정되면 Symphony를 통해 Braze로 전송된 커스텀 속성을 기반으로 이메일 및 푸시 알림 캠페인을 생성할 수 있습니다.

### 방법 2
이 방법에서는 Symphony를 통해 Braze를 Zeotap과 통합할 수 있습니다.

- 이 방법에서는 인앱 메시징, 뉴스피드, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다.
- Zeotap은 Zeotap 카탈로그에서 사용할 수 있는 `hashed email`을 `External ID`에 매핑할 것을 권장합니다.

통합이 성공적으로 설정되면 Symphony를 통해 Braze로 전송된 커스텀 속성을 기반으로 이메일 캠페인만 생성할 수 있습니다.

## Braze로의 데이터 흐름 및 지원되는 식별자

데이터는 [user track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) API를 사용하여 Zeotap에서 Braze로 흐를 것입니다. 다음 요점은 데이터 흐름을 요약합니다:

1. Zeotap은 고객 프로필 속성, 커스텀 속성, 커스텀 이벤트 및 구매 필드를 전송합니다.
2. 관련된 모든 Zeotap 카탈로그 필드를 **전송할 데이터** 탭 아래의 Braze 필드에 매핑합니다.
3. 그 데이터는 Braze에 업로드됩니다.

[전송할 데이터](#data-to-send-tab) 섹션 아래 다양한 속성에 대한 세부 정보를 찾을 수 있습니다.

## 대상 설정

Symphony에서 필터를 적용하거나 사용자에 대한 조건을 추가한 후, Braze의 **대상으로 전송** 아래에서 활성화할 수 있습니다. 새 창이 열리고 여기에서 대상을 설정할 수 있습니다. **사용 가능한 대상** 목록에서 기존 대상을 사용할 수 있거나 새로 생성할 수 있습니다.

#### 새 대상 추가
다음 단계를 수행하여 새 대상을 추가합니다.
1. **새 대상 추가**를 클릭합니다.
2. **Braze**을 검색하세요.
3. **클라이언트 이름**, **API 키**, 및 **인스턴스**를 추가하고 대상을 저장합니다.

대상이 생성되고 **사용 가능한 대상** 아래에서 사용 가능합니다.

#### 워크플로 수준 입력 추가
대상을 생성한 후 다음으로, 아래에 언급된 대로 워크플로 수준의 입력을 추가해야 합니다.
1. 검색 기능을 사용하여 사용 가능한 대상 목록에서 대상을 선택합니다.
2. **클라이언트 이름**, **API 키**, 및 **인스턴스** 필드는 대상을 생성할 때 입력한 값에 따라 자동으로 채워집니다.
3. 이 워크플로우 노드에 대해 생성하려는 **오디언스 이름**을 입력하세요. 이는 Braze에 **커스텀 속성**으로 전송됩니다.
4. **전송할 데이터** 탭에서 대상에 대한 카탈로그 매핑을 완료합니다. 아래에서 매핑을 수행하는 방법에 대한 세부 정보를 찾을 수 있습니다.

#### 전송할 데이터 탭
**전송할 데이터** 탭을 사용하면 Braze로 전송할 수 있는 Braze 필드에 Zeotap 카탈로그 필드를 매핑할 수 있습니다. 매핑은 다음 방법 중 하나로 수행할 수 있습니다:
- **정적 매핑** \- Zeotap이 이메일, 전화번호, 이름, 성(이름) 등과 같은 관련 Braze 필드에 자동으로 매핑하는 특정 필드가 있습니다.<br>
- **드롭다운 선택** \- 드롭다운 메뉴에 제공된 Braze 필드에 Zeotap에서 수집된 관련 필드를 매핑합니다.<br>![Zeotap에서 설정한 다양한 사용자 특성(예: 언어, 구/군/시, 생일 등).][3]{: style="max-width:70%;"}<br>
- **커스텀 데이터 입력** \- 관련 Zeotap 필드에 매핑된 커스텀 데이터를 추가하고 Braze로 전송합니다.<br>!["로열티_points"를 Zeotap에서 사용자 특성으로 선택합니다.][4]{: style="max-width:70%;"}

## 지원되는 속성
이 섹션에서 모든 Braze 필드의 세부 정보를 찾을 수 있습니다.

| Braze 필드 | 매핑 유형 | 설명 |
| --- | --- | --- |
| 외부 ID | 드롭다운 선택 | 여러 기기와 플랫폼 전반에서 사용자를 추적하기 위해 Braze에서 정의한 지속적인 `User ID`입니다. `User ID`를 `External ID`에 매핑하는 것이 좋습니다. 그렇지 않으면 Zeotap이 사용자 별칭으로 이메일을 전송할 수 있습니다.<br><br>Zeotap은 Zeotap 카탈로그에서 사용할 수 있는 `hashed email`을 `External ID`에 매핑할 것을 권장합니다.|
| 이메일 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `Email Raw`에 매핑됩니다. |
| 전화 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `Mobile Raw`에 매핑됩니다.<br><br>• Braze는 `E.164` 형식의 전화번호를 허용합니다. Zeotap은 변환을 수행하지 않습니다. 따라서 지정된 형식으로 전화번호를 수집해야 합니다. 추가 정보는 [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/)를 참조하십시오. |
| 이름 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `First Name`에 매핑됩니다. |
| 성 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `Last Name`에 매핑됩니다. |
| 성별 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `Gender`에 매핑됩니다. |
| 사용자 지정 이벤트 이름 | 정적 매핑 | 이는 Zeotap 카탈로그에서 `Event Name`에 매핑됩니다.<br><br>커스텀 이벤트 이름 및 커스텀 이벤트 타임스탬프 모두를 커스텀 이벤트를 캡처하기 위해 매핑해야 합니다. 커스텀 이벤트는 둘 중 하나가 매핑되지 않으면 처리할 수 없습니다. 자세한 내용은 [이벤트 객체](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object)를 참조하십시오. |
| 커스텀 이벤트 타임스탬프 | 정적 매핑 | 이는 Zeotap 카탈로그의 `Event Timestamp`에 매핑됩니다.<br><br>커스텀 이벤트 이름 및 커스텀 이벤트 타임스탬프 모두를 커스텀 이벤트를 캡처하기 위해 매핑해야 합니다. 커스텀 이벤트는 둘 중 하나가 매핑되지 않으면 처리할 수 없습니다. 자세한 내용은 [이벤트 객체](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object)를 참조하십시오. |
| 이메일 가입 | 드롭다운 선택 | `Email Marketing Preference` 필드를 온보딩하고 이에 매핑합니다.<br><br>Zeotap은 다음 세 가지 값을 보냅니다:<br>• `opted_in` - 사용자가 이메일 마케팅 환경 설정에 명시적으로 등록했음을 나타냅니다<br>• `unsubscribed` - 사용자가 이메일 메시지를 명시적으로 옵트아웃했음을 나타냅니다.<br>• `subscribed` - 사용자가 옵트인이나 옵트아웃을 하지 않았음을 나타냅니다. |
| 푸시 가입 | 드롭다운 선택 | `Push Marketing Preference` 필드를 온보딩하고 이에 매핑합니다.<br><br>Zeotap은 다음 세 가지 값을 보냅니다:<br>• `opted_in` - 사용자가 푸시 마케팅 환경 설정에 명시적으로 등록했음을 나타냅니다.<br>• `unsubscribed` - 사용자가 푸시 메시지를 명시적으로 옵트아웃했음을 나타냅니다.<br>• `subscribed` - 사용자가 옵트인도 옵트아웃도 하지 않았음을 나타냅니다 |
| 이메일 오픈 추적 활성화 | 드롭다운 선택 | 관련 `Marketing Preference` 필드를 매핑합니다.<br><br>true로 설정하면 이 사용자에게 전송하는 모든 향후 이메일에 오픈 추적 픽셀이 추가됩니다. |
| 이메일 클릭 추적 활성화 | 드롭다운 선택 | 관련 `Marketing Preference` 필드를 매핑합니다.<br><br>true로 설정하면 이 사용자에게 보내는 모든 향후 이메일 내의 모든 링크에 대해 클릭 추적이 활성화됩니다. |
| 제품 ID | 드롭다운 선택 | • 구매 작업 식별자`(Product Name/Product Category)`. 자세한 내용은 [구매 대상](https://www.braze.com/docs/api/objects_filters/purchase_object/)을 참조하십시오.<br>• 관련 속성을 Zeotap 카탈로그에 온보드하고 매핑합니다.<br><br>`Product ID`, `Currency`, `Price`는 Braze에서 구매 이벤트를 캡처하기 위해 매핑해야 합니다. 구매 이벤트는 세 가지 중 하나라도 놓치면 진행할 수 없습니다. 자세한 내용은 [구매 객체](https://www.braze.com/docs/api/objects_filters/purchase_object/#purchase-object)를 참조하십시오. |
| 통화 | 드롭다운 선택 | • 구매 작업을 위한 통화 속성.<br>• 지원되는 형식은 `ISO 4217 Alphabetic Currency Code`입니다.<br>• 올바르게 형식화된 통화 데이터를 Zeotap 카탈로그에 온보딩하고 이에 매핑합니다.<br><br>`Product ID`, `Currency`, `Price`는 Braze에서 구매 이벤트를 캡처하기 위해 매핑해야 합니다. 구매 이벤트는 세 가지 중 하나라도 놓치면 진행할 수 없습니다. |
| 가격 | 드롭다운 선택 | • 구매 작업에 대한 가격 속성.<br>• 관련 속성을 Zeotap 카탈로그에 온보드하고 매핑합니다.<br><br>`Product ID`, `Currency`, `Price`는 Braze에서 구매 이벤트를 캡처하기 위해 매핑해야 합니다. 구매 이벤트는 세 가지 중 하나라도 놓치면 진행할 수 없습니다. |
| 수량 | 드롭다운 선택 | • 구매 작업에 대한 수량 속성.<br>• 관련 속성을 Zeotap 카탈로그에 온보드하고 매핑합니다. |
| 국가 | 드롭다운 선택 | 온보딩하는 `Country` 카탈로그 필드에 매핑니다. |
| 도시 | 드롭다운 선택 | 온보딩하는 `City` 카탈로그 필드에 매핑니다. |
| 언어 | 드롭다운 선택 | • 허용되는 형식은 `ISO-639-1` 표준입니다 (예: en).<br>• 올바르게 형식화된 언어를 탑재하고 이에 매핑합니다. |
| 생년월일 | 드롭다운 선택 | 온보딩하는 `Date of Birth` 필드에 매핑합니다. |
| 커스텀 속성 | 커스텀 데이터 입력 | 어떠한 사용자 속성이든 커스텀 데이터 입력에 매핑한 후, Braze로 전송합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Braze 콘솔에서 데이터 보기

워크플로에서 전송 및 게시할 관련 속성을 매핑한 후에 정의된 기준에 따라 이벤트가 Braze로 전송되기 시작합니다. Braze 콘솔에서 이메일 ID 또는 외부 ID로 검색할 수 있습니다.

![][2]

다양한 속성이 Braze 내 사용자 대시보드의 다른 섹션에 포함됩니다.
- **프로필** 탭에는 사용자 속성이 포함되어 있습니다.
- **커스텀 속성** 탭에는 사용자가 정의한 커스텀 속성이 포함되어 있습니다.
- **커스텀 이벤트** 탭에는 사용자가 정의한 커스텀 이벤트가 포함되어 있습니다.
- **구매** 탭에는 사용자가 일정 기간 동안 수행한 구매가 포함됩니다.

## 캠페인 생성

사용자는 Braze 내에서 캠페인을 생성하고 실시간 또는 예약된 시간에 따라 사용자를 활성화할 수 있습니다. 캠페인은 사용자가 수행한 작업(커스텀 이벤트, 구매) 또는 사용자 속성을 기반으로 트리거될 수 있습니다.

[1]: {% image_buster /assets/img/zeotap/zeotap5.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap6.jpg %}
[3]: {% image_buster /assets/img/zeotap/zeotap7.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap8.png %}