---
nav_title: 트랜잭션 이메일 캠페인
article_title: 트랜잭션 이메일 캠페인
page_order: 10

description: "이 참조 문서에서는 새로운 Braze 거래 이메일 캠페인을 만들고 구성하는 방법을 설명합니다."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# 트랜잭션 이메일 캠페인

> Braze 거래 이메일은 발신자와 수신자 간에 합의된 거래를 진행하기 위해 전송됩니다. 이 참조 문서에서는 Braze 대시보드에서 트랜잭션 이메일 캠페인을 생성하고 [`/transactional/v1/campaigns/{campaign_id}/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)에 대한 API 호출에 포함할 `campaign_id`를 생성하는 방법을 설명합니다.

{% alert important %}
Braze 트랜잭션 이메일은 일부 Braze 패키지의 일부로만 사용할 수 있습니다. 자세한 내용은 Braze 고객 성공 관리자에게 문의하거나 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요.
{% endalert %}

거래 이메일 캠페인 유형은 판매자와 고객 간의 합의된 거래를 촉진하기 위해 자동화된 비프로모션 이메일 메시지를 전송하기 위해 특별히 고안된 유형입니다. 여기에는 다음과 같은 정보가 포함됩니다:

- 주문 확인
- 비밀번호 재설정
- 청구 알림
- 배송 알림

즉, 트랜잭션 이메일을 사용하여 속도가 가장 중요한 단일 사용자를 대상으로 서비스에서 발생하는 비즈니스 크리티컬 알림을 보낼 수 있습니다. 

{% alert important %}
트랜잭션 이메일은 추가 비용 없이 사용자를 타겟팅하는 데 사용할 수 있는 트랜잭션 캠페인과는 다릅니다. 예를 들어 트랜잭션 캠페인에는 사용자가 장바구니에 상품을 추가한 후 전송되는 메시지가 포함될 수 있습니다. Check out [audience targeting options]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) for more information.
{% endalert %}

## 1단계: 새 캠페인 만들기

새 트랜잭션 이메일 캠페인을 만들려면 캠페인을 만들고 메시징 채널로 **트랜잭션 이메일**을 선택합니다.

![Create Campaign dropdown with the highlighted option for transactional email.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

이제 거래 이메일 캠페인 구성으로 넘어갈 수 있습니다.

## 2단계: 캠페인 구성

거래 이메일 캠페인의 캠페인 생성 흐름은 [표준 이메일 캠페인에]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) 비해 간소화되어 비즈니스에 중요한 거래 이메일이 모든 사용자에게 도달할 수 있도록 합니다.

따라서 이 캠페인 유형을 설정할 때는 다른 Braze 캠페인 유형에서 익숙한 몇 가지 설정이 필요하지 않습니다.

- **배달** 단계가 간소화되어 예약 옵션이 제거되었습니다. 트랜잭션 이메일은 항상 **배달** 페이지에 표시된 캠페인 ID를 사용하여 Braze REST API를 통해 트리거됩니다. 서비스에서 전송 요청을 트리거할 때 모든 사용자가 이러한 중요한 트랜잭션 알림에 도달할 수 있는지 확인하기 위해 재자격 제어 및 최대 게재빈도 설정과 같은 추가 설정도 제거되었습니다.
- The **Target Audiences** step has been removed. 트랜잭션 이메일은 전체 사용자층(수신 거부한 사용자 포함)을 적격 사용자로 등록하므로 필터나 세그먼트를 지정할 필요가 없습니다. 따라서 이 메시지를 수신해야 하는 대상에 적용할 로직이 있는 경우, 특정 사용자에게 메시지를 트리거하기 위해 Braze에 API 요청을 할 것인지 결정하기 전에 해당 로직을 적용하는 것이 좋습니다.
- **전환** 단계가 제거되었습니다. 현재 트랜잭션 이메일은 전환 이벤트 추적을 지원하지 않습니다.

![Compose, Delivery, and Confirm workflow to create a Transactional Email campaign.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

거래 이메일 캠페인을 구성하려면 다음 단계를 따르세요:

1. 메시지를 보낸 후 **캠페인** 페이지에서 결과를 찾을 수 있도록 설명이 포함된 이름을 추가하세요.
2. 이메일을 작성하거나 템플릿에서 선택합니다.
3. 본인의 `campaign_id`를 메모하세요. API 캠페인을 저장한 후에는 [트랜잭션 이메일 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) 문서에 명시된 곳에 생성된 `campaign_id` 필드를 API 요청에 포함시켜야 합니다.
4. **캠페인 저장**을 클릭하면 API 캠페인을 시작할 준비가 완료됩니다!

{% alert note %}
트랜잭션 이메일 캠페인의 원클릭 목록 수신 거부 설정은 다른 이메일 캠페인과 마찬가지로 기본적으로 **워크스페이스 기본값 사용**으로 설정되어 있습니다. 트랜잭션 메시징을 위한 것이므로 Braze는 원클릭 수신 거부 기능을 추가하지 않습니다. 이 캠페인 유형에 원클릭 수신 거부 기능을 추가하려면 **정보 보내기에서** [이 설정을 편집합니다]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe).
{% endalert %}

### 트랜잭션 이메일에서 허용되지 않는 태그

`Connected Content` 및 `Promotion Code` Liquid 태그는 트랜잭션 이메일 캠페인 내에서 사용할 수 없습니다.

`Connected Content` 태그를 사용하면 전송 프로세스 중에 Braze가 아웃바운드 API 요청을 해야 하므로, 요청하는 외부 서비스에 지연이 발생하면 메시지 전송 프로세스가 느려질 수 있습니다. 마찬가지로 `Promotion Code` 태그는 전송 전에 프로모션의 가용성을 평가하기 위해 Braze가 추가 처리를 수행해야 하므로 사용할 수 없는 경우 전송 프로세스가 느려질 수 있습니다.

따라서 트랜잭션 이메일 캠페인의 어떤 필드에도 `Connected Content` 또는 `Promotion Code` 태그를 포함하는 것을 지원하지 않습니다.


