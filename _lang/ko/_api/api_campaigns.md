---
nav_title: API 캠페인
article_title: API 캠페인
page_order: 5
description: "이 참조 문서에서는 API 호출에 포함할 캠페인_id를 생성하는 방법과 해당 캠페인을 구성하는 방법에 대해 설명합니다."
page_type: reference
tool: Campaigns

---
# API 캠페인

> 이 참조 문서에서는 API 호출에 포함할 `campaign_id` 을 생성하는 방법과 해당 캠페인을 구성하는 방법에 대해 설명합니다.

API 캠페인은 일반적으로 트랜잭션 메시징에 사용됩니다. [API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 캠페인을 생성할 때( [API 트리거 캠페인이]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 아닌) Braze 대시보드는 캠페인 보고를 위한 분석을 추적할 수 있는 `campaign_id` 를 생성하는 데만 사용됩니다. 캠페인의 각 이형 상품마다 다른 메시지 이형 상품 ID를 생성할 수도 있습니다. 

그런 다음 해당 정보를 개발팀에 전송하여 API 요청에 사용할 수 있도록 합니다.
- 캠페인 카피
- 오디언스 멤버십
- 자산

캠페인이 시작되면 대시보드에서 결과를 확인할 수 있습니다. API 캠페인은 대시보드를 통해 완전히 생성된 캠페인과 동일한 세부 보고 및 리타겟팅 옵션이 있는 Braze [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 사용합니다.

{% alert warning %}
API 캠페인은 일반적으로 트랜잭션이므로 글로벌 컨트롤 그룹에 속한 사용자를 포함하여 모든 사용자가 API 캠페인을 사용할 수 있습니다. 이러한 전송에는 [원클릭 목록 수신 거부]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) 헤더가 추가되지 않습니다. 모든 API 캠페인에 원클릭 목록 수신 거부 헤더를 추가하려면 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 새 캠페인 만들기

**메시징** > **캠페인으로** 이동하여 **캠페인 만들기를** 선택한 다음 **API 캠페인을** 선택합니다. 이제 API 캠페인 구성으로 넘어갈 수 있습니다.

[API 트리거 캠페인은]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) API 캠페인과 다릅니다.

## 캠페인 구성

캠페인을 구성하려면 다음 단계를 수행합니다:

1. 메시지를 보낸 후 캠페인 페이지에서 결과를 확인할 수 있도록 설명이 포함된 제목을 추가하세요.
2. **메시지 추가를** 클릭하고 API 캠페인에 포함할 메시지 유형을 추가합니다. 이렇게 하면 포함하는 각 채널마다 다른 `campaign_id` 및 메시지 변형 ID를 생성할 수 있습니다. 
3. 선택 사항으로 전환 이벤트를 추가하여 특정 액션 또는 캠페인 목표에 대한 사용자 전환을 추적할 수 있습니다.
4. **캠페인 저장을** 클릭하면 API 캠페인을 시작할 준비가 완료됩니다!

## API 호출

API 캠페인을 저장한 후 API 요청에 다음을 포함합니다. 
- [메시지 보내기 엔드포인트에]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints) 명시된 곳에 API 요청과 함께 생성된 `campaign_id` 필드가 있습니다.
- 캠페인에 포함된 각 플랫폼에 대한 [메시지 개체입니다]({{site.baseurl}}/api/objects_filters/#messaging-objects). 메시지 개체에서 메시지 변형 ID를 입력합니다. 이렇게 하면 해당 이형 상품에서 통계를 수집하고 표시하도록 지정됩니다. 지원되는 메시지 개체는 다음과 같습니다: Android, 콘텐츠 카드, 이메일, iOS, Kindle, SMS/MMS, 웹 푸시 및 웹훅.


