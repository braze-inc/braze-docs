---
nav_title: "구독 그룹"
article_title: SMS 및 RCS 구독 그룹
page_order: 1
description: "이 참고 문서에서는 SMS, MMS 및 RCS 채널의 구독 그룹, 구독 상태 및 구독 그룹 설정 프로세스에 대해 설명합니다."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# SMS 및 RCS 구독 그룹

> 구독 그룹은 Braze를 통해 SMS, MMS, RCS 메시지를 전송하기 위한 기반입니다. 구독 그룹은 특정 유형의 메시징 목적에 사용되는 [발신자]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (예: RCS 인증 발신자, SMS 짧은 코드, SMS 긴 코드 또는 SMS 영숫자 발신자 ID)의 모음입니다. 예를 들어, 브랜드에서 트랜잭션 및 홍보용 SMS 메시징을 모두 보낼 계획이 있는 경우, 별도의 발신 전화번호 풀을 가진 두 개의 구독 그룹을 Braze 대시보드 내에 설정해야 합니다.

## 구독 그룹 상태

SMS 및 RCS 사용자의 구독 상태는 `subscribed` 와 `unsubscribed` 두 가지입니다. 사용자의 구독 상태는 구독 그룹 수준에서 유지되며 구독 그룹 간에 공유되지 않으므로 트랜잭션 구독 그룹에서는 `subscribed` 사용자이지만 프로모션 구독 그룹에서는 `unsubscribed` 사용자가 될 수 있습니다. 브랜드 입장에서는 이러한 상태 분리를 통해 사용자에게 관련성 있는 SMS 및 RCS 메시지를 계속 보낼 수 있습니다.

| 상태 | 정의 |
| --------- | ---------- |
| 가입한 가입자 | 사용자가 특정 구독 그룹으로부터 SMS 및 RCS 수신을 원한다고 명시적으로 확인했습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 옵트인 키워드 응답을 문자로 전송하여 가입할 수 있습니다. 사용자는 SMS, RCS 또는 둘 다 수신하려면 SMS 또는 RCS 구독 그룹에 가입해야 합니다. |
| 탈퇴됨 | 사용자가 명시적으로 SMS 및 RCS 구독 그룹 및 구독 그룹 내 발신 전화번호의 메시징 수신을 옵트아웃한 경우. 사용자는 옵트아웃 키워드 응답을 문자로 보내 탈퇴하거나 브랜드가 [Braze 구독 API]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)]를 통해 구독을 취소할 수 있습니다. SMS 및 RCS 구독 그룹에서 탈퇴한 사용자는 더 이상 해당 구독 그룹에 속한 발신 전화번호로부터 SMS 또는 RCS를 받지 않게 됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 사용자 상태 설정하기

고객 프로필에서 전화번호가 업데이트되면 새 전화번호는 해당 사용자의 구독 그룹 상태를 상속받습니다. 전화 번호가 Braze에 이미 존재하는 번호로 업데이트되면 기존 전화 번호의 가입 상태가 상속됩니다.

예를 들어 사용자 A가 여러 구독 그룹에 가입한 전화번호를 가지고 있는데 그 전화번호가 사용자 B에게 추가되면 사용자 B는 동일한 구독 그룹에 가입하게 됩니다. 사용자가 기존 구독을 상속받지 않도록 하려면 사용자가 번호를 변경할 때마다 Braze REST API를 통해 이전 번호의 구독 그룹을 재설정할 수 있습니다. 여러 사용자가 이 휴대폰 번호를 공유하면 모두 탈퇴 처리됩니다.

사용자의 구독 그룹 상태를 설정하려면 다음 방법 중 하나를 사용합니다:

- **REST API:** 고객 프로필은 Braze REST API를 사용하여 [\`/subscription/status/set\` 엔드포인트(]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) )에서 프로그래밍 방식으로 설정할 수 있습니다.
- **SDK 통합** 사용자는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) 또는 [웹의](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) 경우 `addToSubscriptionGroup` 방법을 사용하여 이메일 또는 SMS 및 RCS 구독 그룹에 추가할 수 있습니다.
- **사용자 옵트인/옵트아웃 시 자동으로 처리됩니다:** 사용자가 기본값인 옵트인 또는 옵트아웃 [키워드를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) 문자로 보내면 Braze는 자동으로 사용자의 구독 상태를 설정하고 업데이트합니다.
- **사용자 가져오기**: **사용자 가져오기를** 통해 이메일 또는 SMS 및 RCS 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때 CSV에 `subscription_group_id` 와 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) 참조하세요.

### 사용자 그룹 확인

사용자의 구독 그룹을 확인하려면 다음 방법 중 하나를 사용합니다:

- **고객 프로필:** 개별 사용자 프로필은 사이드바에서 **사용자 검색을** 선택하여 Braze 대시보드에서 액세스할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 ID로 고객 프로필을 조회할 수 있습니다. 고객 프로필의 참여 탭에서 사용자의 SMS 및 RCS 구독 그룹을 볼 수 있습니다. 
- **REST API:** 개별 고객 프로필 구독 그룹은 [목록 사용자의 구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [목록 사용자의 구독 그룹 상태 엔드포인트에서]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) Braze REST API를 사용하여 볼 수 있습니다. 

## 구독 그룹으로 메시지 보내기

Braze를 통해 SMS 또는 RCS 캠페인을 시작하려면 **SMS/MMS/RCS 배리언트** 드롭다운에서 구독 그룹을 선택합니다. 오디언스 필터가 선택되면 캠페인 또는 캔버스에 자동으로 추가되어 선택한 구독 그룹의 사용자 `subscribed` 만 타겟 오디언스에 포함되도록 합니다.

{% alert important %}
국제 [통신 규정 및 지침을]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) 준수하기 위해 Braze는 선택한 구독 그룹에 가입하지 않은 사용자에게는 절대로 SMS 또는 RCS를 보내지 않습니다.  
{% endalert %}

구독 그룹 드롭다운이 열려 있고 사용자가 'SMS용 메시지 서비스 A'를 강조 표시한 메시지 작성기.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## 구독 그룹 인에이블먼트하기

SMS, MMS 또는 RCS에 대한 구독 그룹을 인에이블먼트하려면 다음을 참조하세요:

{% tabs local %}
{% tab SMS %}
SMS 온보딩 과정에서 Braze 온보딩 매니저가 대시보드 계정에 대한 구독 그룹을 설정합니다. 필요한 구독 그룹 수를 결정하고 적절한 발신 전화번호를 구독 그룹에 추가하기 위해 고객과 협력합니다. 구독 그룹을 설정하는 타임라인은 추가하는 전화번호 유형에 따라 달라집니다. 예를 들어 짧은 코드 애플리케이션은 8~12주 정도 걸리는 반면, 긴 코드는 하루 안에 설정할 수 있습니다. Braze 대시보드 설정에 대해 궁금한 점이 있으면 담당자에게 문의하여 지원을 받으세요.  
{% endtab %}

{% tab MMS %}
MMS 메시지를 보내려면 구독 그룹 내에서 하나 이상의 번호가 MMS를 보낼 수 있도록 인에이블먼트되어 있어야 합니다. 이는 구독 그룹 옆에 있는 태그로 표시됩니다. 

!"[SMS용 메시징 서비스 A"가 강조 표시된 구독 그룹 드롭다운. 항목 앞에는 "MMS" 태그가 붙습니다.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCS 메시지를 보내려면 먼저 구독 그룹 내에 RCS 인증 발신자가 있어야 합니다. 

RCS 인증 발신자를 추가하는 방법은 두 가지가 있습니다:
- 기존 구독 그룹에 추가하기
- 새 RCS 구독 그룹 만들기
선택은 주로 관심 있는 RCS 사용 사례에 따라 달라집니다. 

통합에 따라 Braze는 RCS 인증 발신자를 기존 SMS 구독 그룹에 추가하거나 새 구독 그룹을 설정할 수 있습니다. 두 경우 모두 고객 성공 매니저가 원활하고 효율적인 SMS 트래픽 업그레이드를 안내해 드립니다.
{% endtab %}
{% endtabs %}

## SMS 트래픽을 RCS로 마이그레이션하기

SMS와 RCS 구독 그룹이 분리되어 있는 경우 원스텝 캔버스를 사용하여 사용자를 SMS에서 RCS로 마이그레이션할 수 있습니다. 

처음에는 소수의 사용자에게 RCS를 테스트 전송하고 시간이 지남에 따라 더 많은 사용자를 RCS 구독 그룹으로 마이그레이션할 것을 Braze는 권장합니다. 예를 들어 1,000,000명의 사용자가 SMS 구독 그룹에 가입한 경우, 먼저 모든 사용자를 새 구독 그룹으로 마이그레이션한 다음 50,000~100,000명(5~10%)의 소규모 오디언스로 세분화하여 RCS 메시지를 테스트할 수 있습니다.

### 1단계: 캔버스를 만들고 참가 일정 작성하기

캔버스를 만들고 식별자가 쉽게 알 수 있는 이름을 지정합니다(예: "SMS-RCS 구독 그룹 사용자 전송"). 그런 다음 편한 시간에 캠페인을 예약하세요.

### 2단계: 오디언스 정의하기

다음 방법 중 하나를 사용하여 오디언스를 정의합니다. 다음으로 **설정 보내기** 단계로 이동하여 **가입하거나 옵트인한 사용자를** 선택합니다.

| 방법                          | 설명                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **세그먼트 만들기**         | 세분화 필터(e.g., 무작위 5~10%)를 사용하여 구독 그룹 또는 하위 집합의 모든 사용자를 포함하는 세그먼트를 구축합니다. 세그먼트는 현재 사용자 기반을 반영하기 위해 매번 전송 전에 업데이트됩니다.        |
| **캠페인 또는 캔버스 필터 적용하기** | 캠페인 또는 캔버스 단계의 **타겟 오디언스에서 오** 디언스를 구체화하세요. 페이지에서 나가지 않고도 타겟팅 옵션을 조정하여 유연성을 높일 수 있습니다.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3단계: 사용자 업데이트 단계 구성

캔버스에 사용자 업데이트 단계를 추가합니다. 이 단계에서 **고급 JSON 편집기를** 열고 다음을 입력합니다(고유 사용자 식별자 필드의 경우 `braze_id` 필드를 사용하는 것이 좋습니다):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

앞서 설명한 JSON 코드가 포함된 "사용자 업데이트 개체".]({% image_buster /assets/img/sms/user_update_object.png %})

### 4단계: 캔버스 테스트하기

더 많은 오디언스에게 보내기 전에 [캔버스를 테스트하여]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) 예상대로 작동하는지 확인하는 것이 좋습니다.

### 5단계: 캔버스 시작하기

캔버스를 성공적으로 테스트했으면 이제 일부 사용자를 대상으로 캔버스를 출시하세요!

사용자가 성공적으로 마이그레이션되었는지 확인하려면 업데이트된 몇 가지 개별 고객 프로필을 확인하는 것이 좋습니다. **참여** 탭에서 **연락처 설정을** 찾아 스크롤하여 사용자가 가입한 구독 그룹을 확인합니다. 이제 RCS 구독 그룹 토글이 켜져 있을 것입니다.
