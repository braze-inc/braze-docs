---
nav_title: 거래 이메일 캠페인
article_title: 거래 이메일 캠페인
page_order: 10

description: "이 참조 문서에서는 새로운 Braze 거래 이메일 캠페인을 생성하고 구성하는 방법을 다룹니다."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# 거래 이메일 캠페인

> Braze 거래 이메일은 발신자와 수신자 간의 합의된 거래를 촉진하기 위해 전송됩니다. 이 참조 문서에서는 Braze 대시보드에서 거래 이메일 캠페인을 생성하고 API 호출에 포함할 `campaign_id`을 생성하는 방법을 다룹니다 [`/transactional/v1/campaigns/{campaign_id}/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
Braze 거래 이메일은 선택된 Braze 패키지의 일부로만 제공됩니다. Braze 고객 성공 관리자에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support/)을 열어 자세한 내용을 확인하세요.
{% endalert %}

거래 이메일 캠페인 유형은 자동화된 비홍보 이메일 메시지를 전송하여 귀하와 고객 간의 합의된 거래를 촉진하기 위해 특별히 설계되었습니다. 여기에는 다음과 같은 정보가 포함됩니다:

- 주문 확인
- 비밀번호 재설정
- 청구 알림
- 배송 알림

요약하자면, 거래 이메일을 사용하여 서비스에서 단일 사용자에게 비즈니스에 중요한 알림을 신속하게 전송할 수 있습니다. 

{% alert important %}
거래 이메일은 추가 비용 없이 사용자에게 타겟팅할 수 있는 거래 캠페인과 다릅니다. 예를 들어, 거래 캠페인에는 사용자가 장바구니에 항목을 추가한 후 전송된 메시지가 포함될 수 있습니다. 자세한 내용은 [청중 타겟팅 옵션]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)을 확인하세요.
{% endalert %}

## 1단계: 새 캠페인 만들기

새로운 거래 이메일 캠페인을 만들려면 캠페인을 만들고 메시징 채널로 **거래 이메일**을 선택하세요.

\![거래 이메일 옵션이 강조 표시된 캠페인 만들기 드롭다운.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

이제 거래 이메일 캠페인을 구성하는 단계로 넘어갈 수 있습니다.

## 2단계: 캠페인 구성하기

거래 이메일 캠페인의 캠페인 생성 흐름은 [표준 이메일 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)에 비해 단순화되어 비즈니스에 중요한 거래 이메일이 모든 사용자에게 도달할 수 있도록 합니다.

그 결과, 다른 Braze 캠페인 유형에서 익숙할 수 있는 여러 설정이 이 캠페인 유형을 설정할 때 필요하지 않다는 것을 알 수 있습니다:

- **전송** 단계는 일정 옵션을 제거하여 단순화되었습니다. 거래 이메일은 항상 **전송** 페이지에 표시된 캠페인 ID를 사용하여 Braze REST API를 통해 트리거됩니다. 재적격성 제어 및 빈도 제한 설정과 같은 추가 설정도 제거되어 서비스가 전송 요청을 트리거할 때 모든 사용자가 이러한 중요한 거래 알림을 받을 수 있도록 확인합니다.
- **대상 청중** 단계가 제거되었습니다. 거래 이메일은 전체 사용자 기반을 자격이 있는 것으로 등록하므로(구독 취소한 사용자 포함) 필터나 세그먼트를 지정할 필요가 없습니다. 그 결과, 이 메시지를 받아야 할 사람에 적용할 논리가 있는 경우, 특정 사용자에게 메시지를 트리거하기 위해 Braze에 API 요청을 할지 결정하기 전에 해당 논리를 적용하는 것을 권장합니다.
- **전환** 단계가 제거되었습니다. 현재 거래 이메일은 전환 이벤트 추적을 지원하지 않습니다.

\![거래 이메일 캠페인을 만들기 위한 작성, 전송 및 확인 워크플로우.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

거래 이메일 캠페인을 구성하려면 다음 단계를 따르세요:

1. 결과를 찾을 수 있도록 설명적인 이름을 추가하세요. 메시지를 전송한 후 **캠페인** 페이지에서 결과를 찾을 수 있습니다.
2. 이메일을 작성하거나 템플릿에서 선택하세요.
3. 당신의 `campaign_id`을(를) 주목하세요. API 캠페인을 저장한 후, [거래 이메일 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) 문서에 명시된 대로 API 요청에 생성된 `campaign_id` 필드를 포함해야 합니다.
4. **캠페인 저장**을 클릭하면 API 캠페인을 시작할 준비가 완료됩니다!

{% alert note %}
거래 이메일 캠페인에 대한 원클릭 구독 취소 설정은 다른 이메일 캠페인과 유사하게 기본값으로 **작업공간 기본값 사용**으로 설정됩니다. 이것은 거래 메시징을 위한 것이므로, Braze는 원클릭 구독 취소를 추가하지 않습니다. 이 캠페인 유형에 원클릭 구독 취소를 추가하려면, **전송 정보** 아래에서 [이 설정 편집]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe)하세요.
{% endalert %}

### 거래 이메일에서 허용되지 않는 태그

`Connected Content` 및 `Promotion Code` Liquid 태그는 거래 이메일 캠페인 내에서 사용할 수 없습니다.

`Connected Content` 태그를 사용하면 Braze가 전송 과정 중에 외부 API 요청을 해야 하며, 요청하는 외부 서비스가 지연되고 있다면 메시지 전송 과정이 느려질 수 있습니다. 유사하게, `Promotion Code` 태그는 Braze가 전송하기 전에 프로모션의 가용성을 평가하기 위해 추가 처리를 수행해야 하며, 프로모션이 없을 경우 전송 과정이 느려질 수 있습니다.

결과적으로, 거래 이메일 캠페인의 어떤 필드에도 `Connected Content` 또는 `Promotion Code` 태그를 포함하는 것을 지원하지 않습니다.


