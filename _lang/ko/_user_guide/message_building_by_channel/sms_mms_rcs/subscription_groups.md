---
nav_title: "Subscription groups"
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

> 구독 그룹은 Braze를 통해 SMS, MMS 및 RCS 메시지를 전송하기 위한 기반입니다. 구독 그룹은 특정 유형의 메시징 목적에 사용되는 [발신 엔티티]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)(RCS 인증 발신자, SMS 짧은 코드, SMS 긴 코드 또는 SMS 영숫자 발신자 ID 등)의 모음입니다. 예를 들어, 브랜드에서 트랜잭션 및 프로모션 SMS 메시지를 모두 전송할 계획이 있는 경우, Braze 대시보드 내에서 별도의 발신 전화번호 풀을 가진 두 개의 구독 그룹을 설정해야 합니다.

## 구독 그룹 상태

SMS 및 RCS 사용자에게는 `subscribed`와 `unsubscribed` 두 가지 구독 상태가 있습니다. 사용자의 구독 상태는 구독 그룹 수준에서 관리되며 구독 그룹 간에 공유되지 않습니다. 따라서 사용자가 트랜잭션 구독 그룹에는 `subscribed`이면서 프로모션 구독 그룹에는 `unsubscribed`일 수 있습니다. 브랜드 입장에서 이러한 상태 분리를 통해 사용자에게 관련 SMS 및 RCS 메시지를 계속 보낼 수 있습니다.

| 상태 | 정의 |
| --------- | ---------- |
| 가입됨 | 사용자가 특정 구독 그룹에서 SMS 및 RCS를 수신하겠다고 명시적으로 확인한 상태입니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 옵트인 키워드 응답을 문자로 전송하여 구독할 수 있습니다. SMS, RCS 또는 둘 다를 수신하려면 SMS 또는 RCS 구독 그룹에 가입되어 있어야 합니다. |
| 탈퇴됨 | 사용자가 SMS 및 RCS 구독 그룹과 해당 구독 그룹 내의 발신 전화번호로부터의 메시징을 명시적으로 거부한 상태입니다. 옵트아웃 키워드 응답을 문자로 전송하여 탈퇴하거나, 브랜드가 [Braze 구독 API]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)를 통해 사용자를 탈퇴 처리할 수 있습니다. SMS 및 RCS 구독 그룹에서 탈퇴한 사용자는 해당 구독 그룹에 속한 발신 전화번호로부터 더 이상 SMS 또는 RCS를 수신하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 사용자 상태 설정

고객 프로필에서 전화번호가 업데이트되면 새 전화번호는 해당 사용자의 구독 그룹 상태를 상속받습니다. 전화번호가 Braze에 이미 존재하는 번호로 업데이트되면 기존 전화번호의 구독 상태가 상속됩니다.

예를 들어, 사용자 A가 여러 구독 그룹에 가입된 전화번호를 가지고 있고 그 전화번호가 사용자 B에게 추가되면, 사용자 B는 동일한 구독 그룹에 가입됩니다. 사용자가 기존 구독을 상속받지 않도록 하려면 사용자가 번호를 변경할 때마다 Braze REST API를 통해 이전 번호의 구독 그룹을 재설정할 수 있습니다. 여러 사용자가 이 전화번호를 공유하는 경우 모두 구독이 취소됩니다.

또한, 이전 사용자의 전화번호 구독 상태는 해당 전화번호가 현재 고객 프로필에 연결되어 있지 않더라도 상속될 수 있습니다. 예를 들어, 사용자가 전화번호 `123-456-7890`을 가지고 구독 그룹에 가입한 후 전화번호를 삭제하면, `123-456-7890`에 연결된 구독 상태는 유지되며 나중에 해당 번호가 다시 할당될 때 적용됩니다.

사용자의 구독 그룹 상태를 설정하려면 다음 방법 중 하나를 사용하세요:

- **REST API:** 고객 프로필은 Braze REST API를 사용하여 [`/subscription/status/set` 엔드포인트]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)로 프로그래밍 방식으로 설정할 수 있습니다.
- **SDK 통합:** 사용자는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) 또는 [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)에서 `addToSubscriptionGroup` 메서드를 사용하여 이메일 또는 SMS 및 RCS 구독 그룹에 추가할 수 있습니다.
- **사용자 옵트인/옵트아웃 시 자동 처리:** 사용자가 기본 옵트인 또는 옵트아웃 [키워드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)를 문자로 보내면, Braze가 자동으로 사용자의 구독 상태를 설정하고 업데이트합니다.
- **사용자 가져오기**: **사용자 가져오기**를 통해 이메일 또는 SMS 및 RCS 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때는 CSV에 `subscription_group_id`와 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)를 참조하세요.

### 사용자 그룹 확인

사용자의 구독 그룹을 확인하려면 다음 방법 중 하나를 사용하세요:

- **고객 프로필:** 사이드바에서 **사용자 검색**을 선택하여 Braze 대시보드에서 개별 고객 프로필에 접근할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 ID로 고객 프로필을 조회할 수 있습니다. 고객 프로필 내 참여 탭에서 사용자의 SMS 및 RCS 구독 그룹을 확인할 수 있습니다. 
- **REST API:** Braze REST API를 사용하여 [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)에서 개별 고객 프로필의 구독 그룹을 확인할 수 있습니다. 

## 구독 그룹으로 메시지 전송

Braze를 통해 SMS 또는 RCS 캠페인을 시작하려면 **SMS/MMS/RCS 배리언트** 드롭다운에서 구독 그룹을 선택하세요. 선택하면 캠페인 또는 캔버스에 오디언스 필터가 자동으로 추가되어, 선택한 구독 그룹에 `subscribed`된 사용자만 타겟 오디언스에 포함됩니다.

{% alert important %}
국제 [통신 규정 준수 및 지침]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)에 따라, Braze는 선택한 구독 그룹에 가입하지 않은 사용자에게 SMS 또는 RCS를 절대 전송하지 않습니다.  
{% endalert %}

![구독 그룹 드롭다운이 열려 있고 사용자가 "SMS용 메시징 서비스 A"를 강조 표시한 상태의 SMS 작성기입니다.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## 구독 그룹 활성화

SMS, MMS 또는 RCS에 대한 구독 그룹을 활성화하려면 다음을 참조하세요:

{% tabs local %}
{% tab SMS %}
SMS 온보딩 과정에서 Braze 온보딩 매니저가 대시보드 계정에 대한 구독 그룹을 설정합니다. 필요한 구독 그룹 수를 결정하고 적절한 발신 전화번호를 구독 그룹에 추가하기 위해 함께 협력합니다. 구독 그룹 설정 소요 시간은 추가하는 전화번호 유형에 따라 다릅니다. 예를 들어, 짧은 코드 신청은 8~12주 정도 걸리는 반면, 긴 코드는 하루 안에 설정할 수 있습니다. Braze 대시보드 설정에 대한 질문이 있으면 Braze 담당자에게 문의하여 고객지원을 받으세요.  
{% endtab %}

{% tab MMS %}
MMS 메시지를 보내려면 구독 그룹 내에서 하나 이상의 번호가 MMS 전송이 가능하도록 활성화되어 있어야 합니다. 이는 구독 그룹 옆에 있는 태그로 표시됩니다. 

!["SMS용 메시징 서비스 A"가 강조 표시된 구독 그룹 드롭다운입니다. 항목 앞에 "MMS" 태그가 붙어 있습니다.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCS 메시지를 전송하려면 먼저 구독 그룹 내에 RCS 인증 발신자가 있어야 합니다. 

RCS 인증 발신자를 추가하는 방법은 두 가지입니다:
- 기존 구독 그룹에 추가
- 새 RCS 구독 그룹 생성
선택은 주로 관심 있는 RCS 활용 사례에 따라 달라집니다. 

통합 방식에 따라, Braze가 기존 SMS 구독 그룹에 RCS 인증 발신자를 추가하거나 새로운 구독 그룹을 설정할 수 있습니다. 어느 경우든, 고객 성공 매니저가 원활하고 효율적인 SMS 트래픽 업그레이드를 안내해 드립니다.
{% endtab %}
{% endtabs %}

## SMS 트래픽을 RCS로 마이그레이션

별도의 SMS 및 RCS 구독 그룹이 있는 경우, 한 단계 캔버스를 사용하여 사용자를 SMS에서 RCS로 마이그레이션할 수 있습니다. 

Braze는 처음에 소규모 사용자를 대상으로 RCS 전송을 테스트한 후, 시간이 지남에 따라 더 많은 사용자를 RCS 구독 그룹으로 마이그레이션하는 것을 권장합니다. 예를 들어, SMS 구독 그룹에 1,000,000명의 사용자가 구독되어 있다면, 먼저 모든 사용자를 새 구독 그룹으로 마이그레이션한 다음 50,000~100,000명(5~10%)의 소규모 오디언스로 세분화하여 RCS 메시지를 테스트하는 방식을 고려할 수 있습니다.

### 1단계: 캔버스를 생성하고 진입 스케줄을 작성하세요

캔버스를 생성하고 쉽게 식별할 수 있는 이름(예: "SMS-RCS 구독 그룹 사용자 전환")을 지정하세요. 그런 다음, 편리한 시간에 캠페인을 스케줄하세요.

### 2단계: 오디언스를 정의하세요

다음 방법 중 하나를 사용하여 오디언스를 정의하세요. 그런 다음 **발송 설정** 단계로 이동하여 **구독하거나 옵트인한 사용자**를 선택하세요.

| 방법                          | 설명                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **세그먼트 생성**         | 구독 그룹의 모든 사용자 또는 세분화 필터(예: 무작위 5~10%)를 사용한 하위 집합을 포함하는 세그먼트를 구축하세요. 세그먼트는 현재 사용자 기반을 반영하기 위해 각 발송 전에 업데이트됩니다.        |
| **캠페인 또는 캔버스 필터 적용** | 캠페인 또는 캔버스의 **타겟 오디언스** 단계에서 오디언스를 세분화하세요. 페이지를 떠나지 않고 타겟팅 옵션을 조정할 수 있어 유연성이 높아집니다.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3단계: 사용자 업데이트 단계를 구성하세요

캔버스에 사용자 업데이트 단계를 추가하세요. 해당 단계에서 **고급 JSON 편집기**를 열고 다음을 입력하세요(고유 사용자 식별자 필드에는 `braze_id` 필드를 사용하는 것을 권장합니다):

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

![앞서 언급한 JSON 코드를 포함하는 "사용자 업데이트 오브젝트"입니다.]({% image_buster /assets/img/sms/user_update_object.png %})

### 4단계: 캔버스를 테스트하세요

더 넓은 오디언스에게 전송하기 전에 [캔버스를 테스트]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/)하여 예상대로 작동하는지 확인하는 것을 강력히 권장합니다.

### 5단계: 캔버스를 시작하세요

캔버스를 성공적으로 테스트한 후, 사용자 하위 집합을 대상으로 시작하세요!

사용자가 성공적으로 마이그레이션되었는지 확인하려면 업데이트된 개별 고객 프로필 몇 개를 확인하는 것이 좋습니다. **참여** 탭에서 **연락처 설정**을 찾아 스크롤하여 사용자가 구독한 구독 그룹을 확인하세요. RCS 구독 그룹 토글이 켜져 있어야 합니다.