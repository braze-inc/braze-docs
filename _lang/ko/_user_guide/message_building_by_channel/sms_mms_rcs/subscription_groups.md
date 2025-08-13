---
nav_title: "구독 그룹"
article_title: SMS 및 RCS 구독 그룹
page_order: 1
description: "이 참조 문서에서는 SMS, MMS 및 RCS 채널에 대한 구독 그룹, 구독 상태 및 구독 그룹 설정 프로세스를 다룹니다."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# SMS 및 RCS 구독 그룹

> 구독 그룹은 Braze를 통해 SMS, MMS 및 RCS 메시지를 전송하는 기반입니다. 구독 그룹은 특정 유형의 메시징 목적을 위해 사용되는 [발신 엔티티]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (RCS 인증 발신자, SMS 단축 코드, SMS 긴 코드 또는 SMS 알파벳 발신자 ID와 같은)의 모음입니다. 예를 들어, 브랜드에서 거래 및 프로모션 SMS 메시지를 모두 전송할 계획이 있는 경우, Braze 대시보드 내에서 별도의 전송 전화번호 풀을 가진 두 개의 구독 그룹을 설정해야 합니다.

## 구독 그룹 상태

SMS 및 RCS 사용자에게는 두 가지 구독 상태가 있습니다: `subscribed` 및 `unsubscribed`. 사용자의 구독 상태는 구독 그룹 수준에 있으며 구독 그룹 간에 공유되지 않으므로 사용자는 거래 구독 그룹에 `subscribed`일 수 있지만 프로모션 구독 그룹에는 `unsubscribed`일 수 있습니다. 브랜드의 경우 이러한 상태 분리는 사용자가 관련 SMS 및 RCS 메시지를 계속 받을 수 있도록 보장합니다.

| 상태 | 정의 |
| --------- | ---------- |
| 가입됨 | 사용자는 특정 구독 그룹에서 SMS 및 RCS를 수신하고 싶다는 것을 명시적으로 확인했습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 옵트인 키워드 응답을 문자로 전송하여 구독할 수 있습니다. 사용자는 SMS, RCS 또는 둘 다를 수신하기 위해 SMS 또는 RCS 구독 그룹에 가입해야 합니다. |
| 탈퇴됨 | 사용자는 귀하의 SMS 및 RCS 구독 그룹과 구독 그룹 내의 발신 전화번호로부터 메시징을 명시적으로 탈퇴했습니다. 사용자는 탈퇴 키워드 응답을 문자로 보내 탈퇴할 수 있으며, 브랜드는 [Braze 구독 API]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).를 통해 사용자를 탈퇴시킬 수 있습니다. SMS 및 RCS 구독 그룹에서 탈퇴한 사용자는 더 이상 구독 그룹에 속한 발신 전화번호로부터 SMS 또는 RCS를 수신하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 사용자의 상태 설정

사용자 프로필에서 전화번호가 업데이트되면 새 전화번호는 사용자의 가입 그룹 상태를 상속받습니다. 전화번호가 Braze에 이미 존재하는 번호로 업데이트되면 기존 전화번호의 구독 상태가 상속됩니다.

예를 들어 사용자 A가 여러 가입 그룹에 가입되어 있는 전화번호를 가지고 있는데 그 전화번호가 사용자 B에게 추가되면 사용자 B는 동일한 가입 그룹에 가입됩니다. 사용자가 기존 구독을 상속받지 않도록 하려면 사용자가 번호를 변경할 때마다 Braze REST API를 통해 이전 번호의 구독 그룹을 재설정할 수 있습니다. 여러 사용자가 이 전화번호를 공유하면 모두 구독이 취소됩니다.

사용자의 구독 그룹 상태를 설정하려면 다음 방법 중 하나를 사용하십시오:

- **Rest API:** 사용자 프로필은 Braze REST API를 사용하여 [`/subscription/status/set` 엔드포인트]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)에 의해 프로그래밍 방식으로 설정할 수 있습니다.
- **SDK 통합** 사용자는 `addToSubscriptionGroup` 방법을 사용하여 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) 또는 [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)의 이메일 또는 SMS 및 RCS 구독 그룹에 추가될 수 있습니다.
- **사용자 옵트인/옵트아웃 시 자동으로 처리됩니다:** 사용자가 기본 옵트인 또는 옵트아웃 [키워드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)를 문자로 보내면 Braze는 자동으로 사용자의 구독 상태를 설정하고 업데이트합니다.
- **사용자 가져오기**: 사용자는 **사용자 가져오기**를 통해 이메일 또는 SMS 및 RCS 구독 그룹에 추가될 수 있습니다. 구독 그룹 상태를 업데이트할 때는 CSV에 `subscription_group_id` 와 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) 참조하세요.

### 사용자의 그룹 확인

사용자의 구독 그룹을 확인하려면 다음 방법 중 하나를 사용하십시오:

- **사용자 프로필:** 개별 사용자 프로필은 사이드바에서 **사용자 검색**를 선택하여 Braze 대시보드를 통해 접근할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 아이디로 사용자 프로필을 조회할 수 있습니다. 사용자 프로필 내에서 참여 탭 아래에서 사용자의 SMS 및 RCS 구독 그룹을 볼 수 있습니다. 
- **Rest API:** 개별 사용자 프로필 구독 그룹은 [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트에서]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) Braze REST API를 사용하여 볼 수 있습니다. 

## 구독 그룹으로 메시지 전송

Braze를 통해 SMS 또는 RCS 캠페인을 시작하려면 **SMS/MMS/RCS 변형** 드롭다운에서 구독 그룹을 선택하십시오. 오디언스 필터가 선택되면 캠페인 또는 캔버스에 자동으로 추가되어 선택한 구독 그룹의 `subscribed` 사용자만 타겟 대상에 포함되도록 합니다.

{% alert important %}
국제 [통신 준수 및 지침]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)에 따라, Braze는 선택된 구독 그룹에 가입하지 않은 사용자에게 SMS 또는 RCS를 절대 전송하지 않습니다.  
{% endalert %}

![구독 그룹 드롭다운이 열려 있고 사용자가 "SMS용 메시징 서비스 A"를 강조 표시한 SMS 작성기.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## 구독 그룹 활성화

SMS, MMS 또는 RCS에 대한 구독 그룹을 활성화하려면 다음을 참조하십시오:

{% tabs local %}
{% tab 문자 메시지 %}
SMS 온보딩 과정에서 Braze 온보딩 관리자가 대시보드 계정에 대한 구독 그룹을 설정합니다. 필요한 구독 그룹 수를 결정하고 적절한 발신 전화번호를 구독 그룹에 추가하기 위해 고객과 협력합니다. 가입 그룹을 설정하는 타임라인은 추가하는 전화번호 유형에 따라 다릅니다. 예를 들어, 짧은 코드 애플리케이션은 8~12주 정도 걸리는 반면, 긴 코드는 하루 안에 설정할 수 있습니다. Braze 대시보드 설정에 대해 궁금한 점이 있으면 Braze 담당자에게 문의하여 지원을 받으세요.  
{% endtab %}

{% tab MMS %}
MMS 메시지를 보내려면 구독 그룹 내에서 하나 이상의 번호가 MMS를 보낼 수 있도록 설정되어 있어야 합니다. 이는 구독 그룹 옆에 있는 태그로 표시됩니다. 

!["SMS용 메시징 서비스 A"가 강조 표시된 구독 그룹 드롭다운이 표시됩니다. 항목은 태그 "MMS"로 접두사가 붙습니다.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCS 인증 발신자가 RCS 메시지를 전송하기 전에 구독 그룹 내에 있어야 합니다. 

RCS 인증 발신자를 추가하는 방법은 두 가지가 있습니다:
- 기존 구독 그룹에 추가
- 새 RCS 구독 그룹 생성
선택은 주로 관심 있는 RCS 사용 사례에 따라 다릅니다. 

통합에 따라, Braze는 기존 SMS 구독 그룹에 RCS 인증 발신자를 추가하거나 새로운 구독 그룹을 설정할 수 있습니다. 어느 경우든, 고객 성공 매니저가 원활하고 효율적인 SMS 트래픽 업그레이드를 안내할 것입니다.
{% endtab %}
{% endtabs %}

## SMS 트래픽을 RCS로 마이그레이션

별도의 SMS 및 RCS 구독 그룹이 있는 경우, 사용자를 SMS에서 RCS로 한 단계 Canvas를 사용하여 마이그레이션할 수 있습니다. 

Braze는 처음에 소규모 사용자에게 RCS를 전송하는 테스트를 권장하며, 시간이 지남에 따라 더 많은 사용자를 RCS 구독 그룹으로 마이그레이션할 수 있습니다. 예를 들어, SMS 구독 그룹에 1,000,000명의 사용자가 구독하고 있다면, 먼저 모든 사용자를 새로운 구독 그룹으로 마이그레이션한 다음, RCS 메시지를 테스트하기 위해 50,000에서 100,000명(5-10%)의 소규모 오디언스를 세분화하는 것처럼 보일 수 있습니다.

### 1단계: Canvas를 생성하고 진입 일정을 작성하십시오.

Canvas를 생성하고 쉽게 식별할 수 있는 이름(예: "SMS-RCS 구독 그룹 사용자 전송")을 지정하십시오. 그런 다음, 편리한 시간에 캠페인을 예약하십시오.

### 2단계: 대상을 정의하십시오.

다음 방법 중 하나를 사용하여 대상을 정의하십시오. 다음으로, **전송 설정** 단계로 이동하여 **구독하거나 선택한 사용자**를 선택하십시오.

| 방법                          | 설명                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **세그먼트를 생성**         | 구독 그룹의 모든 사용자 또는 세분화 필터를 사용하여 하위 집합을 포함하는 세그먼트를 구축하십시오(e.g., 무작위로 5-10%). 세그먼트는 현재 사용자 기반을 반영하기 위해 각 전송 전에 업데이트됩니다.        |
| **캠페인 또는 Canvas 필터 적용** | 캠페인 또는 Canvas의 **대상 오디언스** 단계에서 대상을 세분화하십시오. 페이지를 떠나지 않고 타겟팅 옵션을 조정하여 유연성을 더하십시오.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3단계: 사용자 업데이트 단계를 구성하십시오.

Canvas에 사용자 업데이트 단계를 추가하십시오. 단계에서 **고급 JSON 편집기**를 열고 다음을 입력하십시오(고유 사용자 식별자 필드에는 `braze_id` 필드를 사용하는 것이 좋습니다):

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

!["사용자 업데이트 객체"가 이전에 언급된 JSON 코드를 포함합니다.]({% image_buster /assets/img/sms/user_update_object.png %})

### 4단계: Canvas를 테스트하십시오.

우리는 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/)을(를) 테스트하여 예상대로 작동하는지 확인할 것을 강력히 권장합니다. 이를 더 넓은 오디언스에게 전송하기 전에 확인하세요.

### 5단계: 캔버스를 실행합니다

캔버스를 성공적으로 테스트한 후, 사용자 하위 집합을 위해 이를 출시하세요!

사용자가 성공적으로 마이그레이션되었는지 확인하려면 업데이트된 몇 개의 개별 사용자 프로필을 확인하는 것이 좋습니다. **참여** 탭에서 **연락처 설정**을(를) 찾아 사용자가 구독한 구독 그룹을 보려면 스크롤하세요. RCS 구독 그룹 토글이 이제 켜져 있어야 합니다.
