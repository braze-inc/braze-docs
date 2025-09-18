---
nav_title: Quikly
article_title: Quikly
description: "이 참조 문서에서는 Braze 고객 여정 내 이벤트에서 전환을 가속화할 수 있는 긴급 마케팅 플랫폼인 Quickly와 Braze 간의 파트너십을 설명합니다."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly][1], 긴급 마케팅 플랫폼은 심리학을 활용하여 소비자를 동기 부여하여 브랜드가 주요 마케팅 이니셔티브에 대한 반응을 즉시 증가시킬 수 있도록 합니다.

_This integration is maintained by Quikly._

## 통합 정보

Braze와 Quikly의 파트너십을 통해 Braze 고객 여정 내 이벤트의 전환을 가속화할 수 있습니다. Quikly는 긴급 심리를 사용하여 소비자를 재미있고 즉각적인 방식으로 동기 부여함으로써 이를 수행합니다. 예를 들어, 브랜드는 Quikly를 사용하여 새로운 이메일 및 SMS 구독자를 Braze에 직접 추가하거나 모바일 앱 다운로드와 같은 다른 주요 마케팅 목표를 달성하도록 유도할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Quikly 계정 | 이 파트너십을 활용하려면 [Quikly][1] 브랜드 파트너 계정이 필요합니다. |
| Braze REST API 키 | `users.track`, `subscription.status.set`, `users.export.ids`, `subscription.status.get` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][2]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Quikly API 키 (선택 사항) | 클라이언트 성공 매니저(웹훅 전용)가 제공한 Quikly API 키. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Quikly를 통해 브랜드에서는 이메일 또는 SMS 유치를 가속화하고 가입자가 Braze 내에서 직접 퍼스트파티 데이터를 제공하도록 유도합니다. Braze를 사용하여 휴면 고객을 재활성화하고 유지하는 Quikly 활성화를 통해 해당 오디언스를 타겟팅할 수도 있습니다. 또한 마케터는 이 통합을 사용하여 고유한 리워드 구조로 특정 고객 여정 이벤트를 장려할 수 있습니다. 

예를 들어, 다음과 같습니다.
 - 소비자가 [Quikly Hype][3]에서 매력적인 리워드를 받을 기회를 옵트인하면 며칠 동안 기대감과 인게이지먼트를 높일 수 있습니다. 퍼스트파티 데이터는 자동으로 Braze에 푸시됩니다.
 - 새로운 이메일 및 SMS 구독자의 획득을 가속화하고 소비자의 응답 속도, 다른 사람들과의 순위, 무작위 또는 시간이나 수량이 소진되기 전에 고유하고 실시간으로 제공되는 [Quikly Swap][4]을(를) 사용하십시오.
 - 웹훅을 사용하여 고객 여정의 특정 단계를 고유한 보상 구조로 동기부여하세요.
 - Quikly 활성화에 참여할 때 고객 프로필에 커스텀 속성 또는 이벤트를 적용합니다.

## 통합

아래에서는 이메일 유치, SMS 유치 커스텀 속성, 웹훅과 같은 네 가지 다른 통합을 설명합니다. 선택하는 통합은 Quikly 활성화 및 사용 사례에 따라 다릅니다.

{% tabs %}
{% tab 이메일 유치 %}

### 이메일 유치

Quikly 활성화가 고객 이메일 주소 또는 프로필 데이터를 수집하는 경우, 유일한 필수 단계는 Quikly에 REST API 키와 엔드포인트를 제공하는 것입니다. Quikly는 이 데이터를 Braze에 전달하도록 브랜드 계정을 구성합니다. 추가 사용자 속성을 포함하고 싶다면, Quikly에 API 자격 증명을 제공할 때 이를 언급합니다.

다음은 Quikly에서 이 워크플로를 실행하는 방법에 대한 개요입니다.
1. Quikly 활성화에 참여하면 Quikly는 주어진 `email_address`에 사용자가 존재하는지 확인하기 위해 [내보내기 PI]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)를 사용하여 사용자 조회를 예약합니다.
2. 사용자를 기록하거나 업데이트하십시오.
  - 사용자가 존재하는 경우:
    - 새 프로필을 만들지 마십시오.
    - 원하는 경우 Quikly는 사용자가 활성화에 참여했음을 나타내기 위해 고객 프로필에 커스텀 속성을 기록할 수 있습니다.
  - 사용자가 존재하지 않는 경우:
    - Quikly creates an alias-only profile via the Braze [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), setting the user's email as the user alias to reference that user in the future (as the user won't have an external ID).
    - 원하는 경우 Quikly는 이 프로필이 Quikly 활성화에 참여했음을 나타내기 위해 커스텀 이벤트를 기록할 수 있습니다.

{% details /users/track request %}

#### 요청 헤더
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### 요청 본문
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS 획득 %}

### SMS 구독

Quikly 활성화는 고객으로부터 직접 휴대폰 번호를 수집하고 새로운 SMS 가입을 시작할 수 있습니다. 이 통합을 활성화하려면 `subscription_group_id`를 Quikly 클라이언트 성공 매니저에게 제공합니다. 구독 그룹의 `subscription_group_id`에 액세스하려면 **구독 그룹** 페이지로 이동하십시오.

Quikly는 고객의 전화번호를 사용하여 가입 조회를 수행하고 SMS 가입이 이미 존재하는 경우 활성화 시 자동으로 크레딧을 부여합니다. 그렇지 않으면 새 가입이 시작되고 가입 상태가 확인된 후 고객에게 크레딧이 제공됩니다.

고객이 Quikly를 통해 휴대폰 번호와 동의를 제공할 때 전체 워크플로는 다음과 같습니다.
1. Quikly는 [구독 그룹 상태]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)를 사용하여 주어진 `phone`가 `subscription_group_id`에 구독되어 있는지 확인하는 구독 조회를 수행합니다. 가입이 존재하면 Quikly 활성화에서 사용자에게 크레딧을 제공합니다. 추가 조치는 필요하지 않습니다.
2. Quikly는 [식별자 엔드포인트로 고객 프로필 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)를 사용하여 주어진 `email_address`에 고객 프로필이 존재하는지 확인합니다. If no user exists, create an alias-only profile via the Braze [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), setting the user's email as the user alias to reference that user in the future (as the user won't have an external ID).
3. [사용자의 구독 그룹 상태 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)를 사용하여 구독 상태를 업데이트하십시오.

기존의 이중 옵트인 SMS 가입 워크플로를 지원하기 위해, Quikly는 위의 워크플로 대신 Braze에 커스텀 이벤트를 보낼 수 있습니다. 이 경우, 가입 상태를 직접 업데이트하는 대신, [커스텀 이벤트가 이중 옵트인 프로세스를 트리거]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/)하고 가입 상태를 주기적으로 모니터링하여 Quikly 활성화에서 크레딧을 부여하기 전에 사용자가 완전히 옵트인했는지 확인합니다.

{% alert important %}
Braze는 `/users/track` 엔드포인트를 통해 새로운 사용자를 생성할 때 Braze가 고객 프로필을 완전히 생성할 수 있도록 관련 구독 그룹에 사용자를 추가하기 전에 약 2분의 지연을 제공해야 함을 권장합니다.
{% endalert %}

{% details 상세한 /subscription/status/set 요청 %}
#### 요청 헤더
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### 요청 본문
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab 커스텀 속성 %}
### 사용자 지정 속성

Braze 구현에 따라 추가 처리 위해 Braze를 통해 Quikly 활성화 내 이벤트를 계단식으로 처리할 수도 있습니다. 예를 들어, Quikly 활성화에서 달성한 레벨이나 인센티브에 따라 커스텀 사용자 속성을 적용하여, 앱을 열거나 웹사이트에 로그인할 때 관련된 콘텐츠 카드를 표시할 수 있습니다. Quikly는 이러한 통합을 구현하기 위해 귀하와 직접 협력할 것입니다.

{% endtab %}
{% tab 웹훅 %}
### 웹훅
웹훅을 사용하여 고객 여정의 특정 이벤트에 대한 인센티브를 트리거합니다. 예를 들어, 사용자가 앱에 로그인하거나 푸시 알림을 켜거나 매장 찾기 기능을 사용할 때 Braze 이벤트가 있는 경우, 특정 Quikly 활성화의 구성에 따라 해당 사용자에게 커스텀 제안을 트리거하는 웹훅을 사용할 수 있습니다. 예제 전술로, 작업(예: 앱에 로그인)을 수행하는 처음 X명의 사용자에게 커스텀 오퍼로 리워드를 제공하거나 시간이 지남에 따라 가치가 감소하는 오퍼를 제공하여 즉각적인 반응을 유도하는 전략이 포함됩니다.

### Braze에서 Quikly 웹훅을 생성하세요

향후 캠페인 또는 캔버스를 위한 Quikly 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿**으로 이동하십시오. 

새 캠페인을 만들 때 Braze에서 **웹훅**을 선택하여 일회성 Quikly 웹훅 캠페인을 만들거나 기존 템플릿을 사용할 수 있습니다.

**빈 템플릿**을 선택하고, 웹훅 URL 및 요청 본문에 다음을 입력하십시오:
- **웹훅 URL**: https://api.quikly.com/webhook/braze
- **요청 본문**: JSON 키/값 쌍

#### 요청 헤더 및 메서드

권한 부여를 위해 Quikly에 `HTTP Header`가 필요합니다.

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### 요청 본문

***JSON 키/값 쌍***을 선택하고 다음 쌍을 추가하십시오:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### 요청 미리보기

**미리보기** 패널에서 요청을 미리 보거나 `Test` 탭으로 이동합니다. 여기서 무작위 사용자, 기존 사용자 또는 고유한 사용자를 선택하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 고객지원
질문이 있으시면 Quikly의 클라이언트 성공 매니저에게 문의하십시오.


[1]: https://www.quikly.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.quikly.com/urgency-marketing/platform/product-overview/hype
[4]: https://www.quikly.com/urgency-marketing/platform/product-overview/swap
