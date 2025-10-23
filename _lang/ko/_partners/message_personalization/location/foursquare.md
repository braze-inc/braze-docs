---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "이 참고 문서에서는 위치를 기반으로 실시간 이벤트 트리거를 제공하는 Braze와 위치 데이터 플랫폼인 Foursquare의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="오른쪽" %}

> [Foursquare](https://foursquare.com/)는 Braze 캠페인에서 위치 데이터 타겟팅을 제공하는 위치 데이터 플랫폼입니다. iOS 및 Android 앱에서 Foursquare의 Pilgrim SDK를 사용하여 위치를 기반으로 실시간 이벤트 트리거를 제공하면, Foursquare의 강력한 지리적 타겟팅 기능을 활용하여 Braze에서 관련성 높은 개인화된 메시징을 전송할 수 있습니다.

_This integration is maintained by Foursquare._

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Foursquare 계정 | 이 파트너십을 이용하려면 Foursquare 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze 작업 공간 및 앱 ID | Braze 작업 공간과 앱 ID는 [개발자 콘솔에서]({{site.baseurl}}/api/api_key/) 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

두 플랫폼을 통합하려면 두 SDK를 통합하고 일치하는 사용자 필드를 매핑해야 합니다. Pilgrim SDK를 통합하면 기기 또는 웹훅으로 위치 이벤트를 수신합니다. 

### 1단계: 사용자 ID 필드 매핑

두 SDK 간에 필드를 올바르게 매핑하기 위해 Braze SDK에서 [`changeUser` 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids)를 사용하고 Pilgrim SDK에서 [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)의 `setUserId` 메서드를 사용하여 두 시스템에서 동일한 사용자 ID를 설정합니다.

### 2단계: Pilgrim 콘솔 구성
![An image of the Pilgrim console asking for Group ID, Android App ID, and iOS App ID.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Braze 개발자 콘솔에서 작업 공간과 앱 ID를 찾습니다. 그런 다음, Foursquare Pilgrim 콘솔에 Braze REST API 키와 앱 ID를 입력합니다.

Pilgrim 콘솔을 구성하면 Pilgrim SDK가 위치 이벤트를 기록하고 이를 Braze에 전달하여 자격을 갖춘 고객을 리타겟팅하고 세분화할 수 있습니다. 자세한 내용은 [Foursquare 개발자 사이트](https://developer.foursquare.com/)를 참조하세요.

{% alert important %}
Pilgrim SDK를 사용하려면 위치 서비스를 활성화해야 합니다.
{% endalert %}

## 메시지 트리거

통합이 설정되면 Pilgrim SDK에서 생성된 위치 이벤트에 따라 작동하는 캠페인 또는 캔버스를 설정할 수 있습니다. 이 통합 경로는 사용자가 관심 장소에 진입한 직후에 실시간 메시징 또는 사용자가 떠난 후 감사 메시지나 미리 알림과 같은 지연된 후속 커뮤니케이션에 적합합니다.

설정된 위치를 기준으로 메시지를 보내는 캠페인을 보내려면 다음과 같이 하세요:
- **액션 기반 전달로** 전송하는 Braze 캠페인 또는 캔버스 만들기
- 트리거의 경우 다음 스크린샷과 같이 `locationType`에 대한 이벤트 속성정보 필터와 함께 `arrival`의 커스텀 이벤트를 사용합니다.

!['커스텀 이벤트 수행' 옵션으로 '도착'이 선택된 전달 단계의 실행 기반 캠페인. 여기서 'locationType'은 'home'과 같습니다.]({% image_buster /assets/img_archive/action-based-campaign.png %})

## 리타겟팅

사용자를 리타겟팅하려면 Pilgrim SDK를 사용하여 Braze 사용자의 고객 프로필에서 `last_location` 커스텀 속성을 설정합니다. 그런 다음, `matches regex` 비교를 사용하여 실제 특정 위치에 방문한 사용자를 리타겟팅할 수 있습니다. 예를 들어, 최근에 피자 매장을 방문한 모든 사용자를 세분화할 수 있습니다.

!['last_location'이 'Pizza Place'인 타겟 사용자 단계의 실행 기반 캠페인.]({% image_buster /assets/img_archive/last-location-segment.png %})

또한 특정 시간대에 특정 유형의 장소를 방문한 사용자를 Foursquare의 `primaryCategoryId` 를 기반으로 Braze에서 세분화할 수도 있습니다. 리타겟팅 사용 사례에 이 데이터 포인트를 활용하려면, 오디언스 세분화 프로세스 중에 `primaryCategoryId`를 이벤트 속성정보로 기록합니다. Foursquare API 및 Pilgrim SDK에서 사용하는 사용자 및 속성정보를 식별하려면 [Foursquare 개발자 사이트](https://developer.foursquare.com/)를 참조하세요.


