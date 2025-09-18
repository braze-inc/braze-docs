---
nav_title: Sendbird
article_title: Sendbird
description: "이 참조 문서에서는 사용자가 Sendbird 플랫폼에서 인앱 알림을 받을 수 있도록 하는 선도적인 인앱 메시징 솔루션인 Sendbird와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird][4] 알림은 마케터와 제품 관리자에게 지속적이고 상호작용하는 일방향 메시지로 고객과 앱 내에서 소통할 수 있는 강력한 새로운 채널을 제공합니다. 이 메시지는 모든 커뮤니케이션에 사용할 수 있으며 주로 프로모션 및 거래 목적으로 사용됩니다.

_This integration is maintained by Sendbird._

## 통합 정보

Braze 및 Sendbird 통합을 통해 Braze 사용자는 다음을 수행할 수 있습니다:
* Utilize Braze segmentation and triggering capabilities to initiate personalized in-app notifications.
* Sendbird 알림 플랫폼에서 맞춤 인앱 알림을 생성하고, 이를 앱 환경 내에서 전달하여 사용자 인게이지먼트를 높일 수 있습니다.

Braze와 Sendbird Notifications의 공동 기능을 활용하여 기업은 효과적인 인앱 알림 전략을 통해 고객 참여를 높이고 더 높은 전환율을 달성할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sendbird 계정 | 이 파트너십을 활용하려면 Sendbird 계정이 필요합니다. |
| Sendbird UIKit | [iOS][2] 또는 [Android][3] 앱에 Sendbird UIKit이 설치되어 있어야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

![][13]

Braze 및 Sendbird 알림 통합은 고객 참여를 증대하고 뛰어난 사용자 경험을 제공하기 위한 다양한 사용 사례를 제공합니다.

- **마케팅**: 사용자의 선호도에 맞춘 개인화된 프로모션 및 추천을 통해 타겟팅 캠페인을 강화하고, 브라우징 기록 또는 과거 구매 내역을 기반으로 한 독점 할인과 같은 혜택을 제공합니다.
- **트랜잭션**: 주문 상태, 배송 세부 정보 및 예상 전달 시간에 대한 알림을 포함하여 주문, 전달, 청구 및 결제에 대한 실시간 업데이트를 통해 고객 커뮤니케이션을 향상시킵니다.

## 통합

### 1단계: 알림 템플릿 만들기

[Sendbird 템플릿][7]을 사용하면 각 채널에 대해 여러 템플릿을 작성하고 사용하여 개인화된 인앱 알림을 보낼 수 있습니다. 템플릿은 코드를 작성하지 않고 Sendbird 대시보드에서 생성 및 사용자 지정할 수 있습니다.

![][10]

### 2단계: Sendbird 대시보드에서 Braze 통합 설정

**Sendbird 대시보드**에서 애플리케이션을 선택하고 **알림 > 통합**으로 이동한 다음, **Braze** 섹션 아래의 **추가**를 클릭합니다. 여기에서 Braze REST API 키와 Braze REST 엔드포인트가 필요합니다.

모든 필드를 제공한 후, 통합을 완료하고 통합 엔드포인트 및 API 토큰에 액세스하려면 **저장**을 클릭하십시오.

### 3단계: Sendbird 알림 빌더 설치

다음으로, [Sendbird 알림 빌더][6]를 설치해야 합니다. 이 Google Chrome 확장을 사용하면 Braze 대시보드에서 Sendbird를 통해 사용자 지정된 알림을 보낼 수 있습니다.

![][12]

#### Sendbird 자격 증명을 확장 프로그램에 추가

확장 프로그램을 설치한 후 브라우저의 도구 모음에서 Sendbird 아이콘을 클릭하고 **설정**을 선택합니다. 여기에서 **Sendbird Notification Builder**에서 찾은 앱 ID와 API 토큰을 제공하십시오.

### 4단계: Sendbird 사용자 ID를 Braze 사용자 ID에 매핑

Sendbird 사용자 ID는 통합을 사용하기 위해 [커스텀 속성][5]으로 Braze 고객 프로필에 추가되어야 합니다. CSV 파일을 통해 [사용자 가져오기][8] 페이지에서 사용자 프로필을 업로드하고 업데이트할 수 있습니다. 또는 Braze 사용자 ID를 Sendbird 사용자 ID로 사용할 수 있습니다.

### 5단계: 웹훅 템플릿을 설정하세요

Braze에서 **템플릿 및 미디어**에서 **웹훅 템플릿**으로 이동하여 **Sendbird 웹훅 템플릿**을 선택합니다. 이 템플릿은 Sendbird 알림 빌더 확장을 설치한 경우에만 사용할 수 있습니다.

{% raw %}
1. 템플릿 이름을 제공하고 필요에 따라 Teams 및 태그를 추가하십시오.
2. Sendbird 대시보드에서 실시간 또는 배치 엔드포인트를 복사하여 **웹훅 URL**에 붙여넣습니다.
3. **수신자** 필드에서 <i class="fas fa-plus"></i> 아이콘을 클릭하고 Sendbird 사용자 ID에 매핑된 사용자 속성을 삽입합니다.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` 사용자가 Sendbird 사용자 ID로 커스텀 속성 `sendbird_id`를 사용하는 경우.
    - `{{ '{{' }}${user_id}}}` 사용자가 Braze 사용자 ID를 Sendbird 사용자 ID로 사용하는 경우.
4. **설정** 탭에서 `SENDBIRD_API_TOKEN`을(를) Sendbird 대시보드의 알림 API 토큰으로 교체하십시오.
5. 템플릿을 저장합니다.
{% endraw %}

## 이 통합 사용

### 캠페인

1. Braze 대시보드에서 **캠페인** 페이지에서 **캠페인 생성** > **웹훅**을 클릭합니다.
2. 위에서 만든 웹훅 템플릿을 선택하세요. 캠페인에는 배치 엔드포인트를 사용하는 것이 좋습니다.
3. 템플릿의 변수를 **작성** 탭에서 편집하여 사용자 정의합니다.

### 캔버스

1. 새로운 캔버스 또는 기존 캔버스에서 **메시지** 구성 요소를 추가합니다. 
2. 구성 요소를 열고 **웹훅**을(를) **메시징 채널**에서 선택합니다.
3. 위에서 만든 웹훅 템플릿을 선택하세요. 실시간 엔드포인트를 캔버스에 사용하는 것이 좋습니다.
4. 템플릿의 변수를 **작성** 탭에서 편집하여 사용자 정의합니다.

## 사용자 지정

### 전달 및 열람 상태 추적

알림 전달 및 열림 상태 이벤트를 캠페인의 전환 지표와 통합하려면 Braze 대시보드에서 커스텀 이벤트를 추가하세요.

1. Braze 대시보드에서 **설정 > 설정 관리 > 커스텀 이벤트**로 이동하여 **\+ 커스텀 이벤트 추가**를 클릭합니다.
2. 커스텀 이벤트를 만든 후, **속성 관리**를 클릭하고, "status"라는 속성을 추가한 다음 속성 유형으로 "문자열"을 선택합니다.
3. 캠페인 또는 캔버스에서 알림을 작성할 때 **이벤트 이름** 필드에 커스텀 이벤트 이름을 입력합니다.

이 커스텀 이벤트는 각 알림에 대해 두 번 트리거됩니다(메시지가 전송될 때와 사용자가 메시지를 열 때).
- 메시지가 전송되면 `SENT` 상태로 커스텀 이벤트가 트리거됩니다.
- 메시지가 읽히면 `READ` 상태로 커스텀 이벤트가 트리거됩니다.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit
[3]: https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit
[4]: https://sendbird.com/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[6]: https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji
[7]: https://sendbird.com/docs/notifications/v1/templates
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[10]: {% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %}
[11]: {% image_buster /assets/img/sendbird/sendbird-dashboard-integrations.png %}
[12]: {% image_buster /assets/img/sendbird/sendbird-notification-builder.png %}
[13]: {% image_buster /assets/img/sendbird/use-cases.png %}