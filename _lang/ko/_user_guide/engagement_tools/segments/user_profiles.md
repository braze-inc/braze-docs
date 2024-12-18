---
nav_title: 사용자 프로필
article_title: 사용자 프로필
page_order: 5
page_type: reference
tool: 
  - Dashboard
description: "이 참고 문서에서는 대시보드에서 고객 프로필에 액세스하는 방법, 프로필 사용 사례 및 각 프로필에 포함된 내용에 대해 설명합니다."

---

# 사용자 프로필

> 사용자 프로필은 특정 사용자에 대한 정보를 찾을 수 있는 좋은 방법입니다. 사용자와 관련된 모든 영구 데이터는 사용자 프로필에 저장됩니다.

## 프로필 액세스

사용자의 프로필에 액세스하려면 **사용자 검색** 페이지로 이동하여 다음 중 하나로 사용자를 검색합니다:

- 외부 사용자 ID
- 이메일
- 전화번호
- 푸시 토큰
- "[user_alias]:[alias_name]" 형식의 사용자 별칭, 예: "amplitude_id:user_123"

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **사용자 검색**은 **사용자 검색이며** **사용자** 아래에서 찾을 수 있습니다.
{% endalert %}

일치하는 항목이 발견되면 Braze SDK를 통해 해당 사용자에 대해 기록한 정보를 확인할 수 있습니다. 그렇지 않으면 검색에서 여러 사용자 프로필이 반환되는 경우 각 프로필을 개별적으로 병합하거나 일괄 사용자 병합을 수행할 수 있습니다. 전체 안내는 [중복 사용자]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/)를 참조하세요.

![검색 결과에는 "검색 조건과 일치하는 사용자가 여러 명입니다"라는 배너와 이전 및 다음이라고 표시된 두 개의 버튼이 표시됩니다.][1]

## 사용 사례

고객 프로필은 사용자의 인게이지먼트 기록, 세그먼트 멤버십, 기기 및 운영 체제에 대한 정보에 쉽게 액세스할 수 있기 때문에 문제 해결 및 테스트에 유용한 리소스입니다.

예를 들어 사용자가 문제를 신고했는데 어떤 기기 및 운영 체제를 사용 중인지 잘 모르는 경우 [개요 탭을](#overview-tab) 사용하여 이메일이나 사용자 ID만 있으면 이 정보를 찾을 수 있습니다. 또한 사용자의 언어를 확인할 수 있으므로 예상대로 작동하지 않는 [다국어 캠페인의][13] 문제를 해결하는 데 유용할 수 있습니다.

[참여 탭을](#engagement-tab) 사용하여 특정 사용자가 캠페인을 수신했는지 확인할 수 있습니다. 또한 이 특정 사용자가 캠페인을 수신한 경우 언제 캠페인을 수신했는지 확인할 수 있습니다. 또한 사용자가 특정 세그먼트에 속하는지 여부와 사용자가 푸시, 이메일 또는 둘 다에 옵트인했는지 여부를 확인할 수 있습니다. 이 정보는 문제 해결에 유용합니다. 예를 들어, 사용자가 예상한 캠페인을 받지 못했거나 예상하지 못한 캠페인을 받은 경우 이 정보를 확인해야 합니다.

## 사용자 프로필의 요소

사용자 프로필에는 네 가지 주요 섹션이 있습니다.

- **개요:** 사용자, 세션 데이터, 커스텀 속성, 커스텀 이벤트, 구매 및 사용자가 가장 최근에 로그인한 기기에 대한 기본 정보입니다.
- **참여:** 사용자의 연락처 설정, 수신한 캠페인, 세그먼트, 커뮤니케이션 통계, 설치 경로 및 무작위 버킷 번호에 대한 정보입니다.
- **메시징 기록:** 지난 30일 동안 이 사용자의 최근 메시징 관련 이벤트입니다.

### 개요 탭 {#overview-tab}

**개요** 탭에는 사용자와 앱 또는 웹사이트와의 상호 작용에 대한 기본 정보가 포함되어 있습니다.

| 개요 카테고리 | 포함 사항 |
| --- | --- |
| 프로필 | 성별, 연령대, 위치, 언어, 로캘, 시간대, 생일을 입력합니다. |
| 세션 개요 | 세션 수, 첫 번째 세션과 마지막 세션이 언제인지, 어떤 앱에서 사용했는지 등을 확인할 수 있습니다. |
| 사용자 지정 속성 | 이 사용자에게 귀속되는 커스텀 속성 및 중첩 커스텀 속성을 포함한 관련 값입니다. |
| 최근 기기 | 로그인한 기기 수, 각 기기에 대한 세부 정보 및 관련 광고 ID(있는 경우). |
| 사용자 지정 이벤트 | 이 사용자가 수행한 커스텀 이벤트, 횟수, 각 이벤트를 마지막으로 수행한 시간. |
| 구매 | 이 사용자의 평생 매출 속성, 마지막 구매, 총 구매 횟수, 각 구매 목록이 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 데이터에 대한 자세한 내용은 [사용자 데이터 수집][12]을 참조하세요.

![][2]

### 인게이지먼트 탭 {#engagement-tab}

**참여** 탭에는 Braze를 사용하여 보낸 메시지와 사용자의 상호작용에 대한 정보가 포함되어 있습니다.

| 참여 카테고리 | 포함 사항 |
| --- | --- |
| 연락처 설정 | 이메일, SMS, 푸시의 구독 상태 및 이 사용자가 이 세 가지 채널에 대해 연결된 구독 그룹입니다. 이 섹션에는 푸시 토큰에 대한 변경 로그 정보도 포함되어 있습니다. 구독 및 옵트인 설정 방법에 대한 자세한 내용은 [이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) 및 [푸시를]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) 참조하세요. |
| 수신된 캠페인 | 이 사용자가 수신한 캠페인 및 시기. 목록에서 캠페인을 선택하여 확인합니다. |
| 세그먼트 | 이 사용자가 포함된 세그먼트입니다. 목록에서 세그먼트를 선택하면 해당 세그먼트를 볼 수 있습니다. |
| 커뮤니케이션 통계 | 이 사용자가 각 채널에서 마지막으로 메시지를 받은 시기입니다. |
| 설치 속성 | 사용자가 앱을 설치한 방법과 시기에 대한 정보입니다. [사용자 설치 이해]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/)에 대해 자세히 알아보세요. |
| 기타 | 사용자의 [무작위 버킷 번호]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/)입니다. |
| 캔버스 메시지 수신 | 이 사용자가 수신한 캔버스 메시지와 시기. 목록에서 메시지를 선택하면 해당 메시지를 볼 수 있습니다. |
| 예측 | 이 사용자에 대한 [이탈 예측]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn) 및 [이벤트 예측]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases) 점수입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

### 메시징 내역 탭

고객 프로필의 **메시지 내역** 탭에는 지난 30일 동안 개별 사용자의 최근 메시징 관련 이벤트(약 40개)가 표시됩니다. 이러한 이벤트에는 사용자가 보낸, 받은, 상호작용한 메시지 등이 포함됩니다. 이 탭의 데이터는 사용자가 병합된 후에는 업데이트되지 않는다는 점에 유의하세요.

{% alert note %}
이 표에 대한 피드백이 있거나 특정 이벤트를 보고 싶다면 "메시징 기록 탭 피드백"이라는 제목으로 [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) 으로 이메일을 보내주세요.
{% endalert %}

![][5]

#### 이벤트 보기 및 이해

**메시징 기록** 테이블의 각 이벤트에 대해 메시징 채널, 이벤트 유형, 이벤트가 발생한 타임스탬프, 관련 캠페인 또는 캔버스 메시지, 사용자의 디바이스 데이터를 확인할 수 있습니다. 특정 이벤트를 필터링하려면 **필터**를 클릭하고 목록에서 이벤트를 선택합니다.

##### 메시지 인게이지먼트 이벤트

이메일, SMS, 푸시, 인앱 메시지, 콘텐츠 카드 및 웹훅에 사용할 수 있는 메시지 인게이지먼트 이벤트는 다음과 같습니다. 특정 이벤트가 추적되는 방법에 대해 자세히 알아보려면 [메시지 인게이지먼트 이벤트 용어집]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events)을 참조하세요.

| 채널 | 사용 가능한 참여 이벤트 |
| --- | --- |
| 이메일 | 반송<br>클릭<br>전달<br>스팸으로 표시<br>열기( [이메일 열기 이벤트에 대한 참고 사항](#note-on-email-open-event) 참조)<br>발송<br>소프트바운스<br>구독취소 |
| SMS | 이동통신사 발송<br>전달<br>전달 실패<br>인바운드 수신<br>거부<br>발송 |
| 푸시 | 반송<br>영향받은 열람<br>iOS 포그라운드<br>열기<br>발송 |
| 인앱 메시지 | 클릭<br>노출 |
| 콘텐츠 카드 | 클릭<br>무시<br>노출<br>발송 |
| 웹훅 | 발송 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### 메시지 중단 이벤트

메시지 중단 이벤트는 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages)의 조건부 로직 또는 Liquid 렌더링 시간 초과로 인해 사용자에게 전송된 메시지가 중단된 경우에 발생합니다.

다음 채널에서 이벤트 취소를 사용할 수 있습니다.

- 이메일
- SMS
- 푸시
- 웹훅

현재 인앱 메시지 및 콘텐츠 카드에는 이벤트 중단 기능을 사용할 수 없습니다.

##### 주파수 제한 이벤트

주파수 제한 이벤트는 사용자가 메시지를 수신할 자격이 있지만 [주파수 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 설정으로 인해 실제로 메시지를 수신하지 못한 경우에 발생합니다. **설정** > **최대 게재빈도 설정**에서 최대 게재빈도 설정을 커스텀할 수 있습니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 **참여** > **글로벌 메시지 설정에서** 빈도 제한을 관리할 수 있습니다.
{% endalert %}

##### 빈 대상

일부 메시지 전송 내역에 빈 수신처("—"로 표시됨)가 있는 메시지 전송이 표시될 수 있습니다. 이는 콘텐츠 카드 및 웹훅과 같은 일부 채널이 메시지 전송 시 디바이스 데이터를 수집하지 않기 때문입니다.

콘텐츠 카드 전송은 카드를 볼 수 있을 때 기록됩니다. 콘텐츠 카드는 여러 기기에서 볼 수 있으므로 전송 시 디바이스 데이터는 기록되지 않습니다. 대신, 이 정보는 노출 시(카드를 실제로 볼 때) 기록됩니다. 웹훅은 디바이스가 아닌 시스템 엔드포인트로 전송되므로 디바이스 데이터는 적용되지 않습니다.

#### 이메일 열기 이벤트에 대한 참고 사항 {#note-on-email-open-event}

이메일 열람 추적은 Braze를 포함한 모든 도구에서 오류가 발생하기 쉽습니다. 다양한 이메일 클라이언트에서 제공하는 다양한 개인 정보 보호 기능으로 이미지의 자동 로딩을 차단하거나 서버에서 사전에 이미지를 로드하기 때문에 이메일 열기 이벤트는 오탐과 오탐에 모두 취약합니다.

이메일 열람 통계는 여러 제목란의 효과를 비교하는 등 총체적으로 유용할 수 있지만, 개별 사용자에 대한 개별 열람 이벤트가 의미가 있다고 가정해서는 안 됩니다.


[1]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
[2]: {% image_buster /assets/img_archive/user_profile2.png %}
[3]: {% image_buster /assets/img_archive/profiles_engagement_tab.png %}
[5]: {% image_buster /assets/img_archive/profiles_messaging_history_tab.png %}

[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
