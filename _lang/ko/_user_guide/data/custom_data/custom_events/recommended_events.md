---
nav_title: 추천 이벤트
article_title: 추천 이벤트
alias: /recommended_events/
page_type: reference
description: "이 참고 문서에서는 이커머스 이벤트를 위해 Braze에서 제공하는 권장 이벤트에 대해 설명합니다."
---

# 추천 이벤트

> 추천 이벤트는 가장 일반적인 이커머스 사용 사례에 매핑됩니다. 추천 이벤트를 사용하면 사전 구축된 캔버스 템플릿, 고객 라이프사이클에 매핑되는 보고 대시보드 등을 잠금 해제할 수 있습니다.

예를 들어, 사용자가 카트에 제품을 추가, 제거 또는 업데이트한 시점을 캡처하기 위해 "cart_updated" 또는 "update_to_cart"라는 사용자 지정 이벤트를 생성할 수 있습니다. 추천 이벤트의 경우, Braze는 이 이벤트에 대해 정의된 이름과 관련 속성이 포함된 이벤트 템플릿을 제공합니다.

{% alert important %}
추천 이벤트는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 고객 성공 관리자에게 문의하세요. <br><br>새로운 [Shopify 커넥터를]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/) 활용하는 경우 이러한 권장 이벤트는 통합을 통해 자동으로 사용할 수 있습니다.
{% endalert %}

## How it works

Braze는 모든 추천 이벤트에 특별한 유효성 검사를 적용하며, 일부 추천 이벤트에는 특별한 사후 처리 작업이 있습니다. 특정 업계 추천 이벤트의 경우, 캠페인과 캔버스를 위한 새로운 액션 기반 트리거와 같은 특별한 처리를 지원할 수 있습니다.

추천 이벤트는 [사용자 지정 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events)와 유사하게 작동합니다. 커런츠에서 추천 이벤트를 내보내고, 차단 목록에 추가하고, 리포팅에 사용할 수 있습니다. 또한 [Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) 또는 [`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 사용하여 이러한 이벤트를 추적하기 위해 데이터를 Braze로 전송할 수도 있습니다.

### 이커머스 추천 이벤트

[전자상거래 추천]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) 이벤트는 추천 이벤트를 기반으로 합니다. 이러한 전자상거래 추천 이벤트는 제품 보기, 카트 업데이트, 결제 프로세스 시작 등 고객이 수행한 작업을 추적합니다. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`

#### 전자상거래 캔버스 템플릿

[이커머스]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) 전용 [사용 사례에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) Braze Canvas의 사전 제작된 템플릿을 사용하여 필수 전략을 구현하는 방법에 대한 더 많은 아이디어를 확인하세요.

## Frequently asked questions

### 추천 이벤트는 사용자 지정 이벤트와 동일한가요?

아니요. Braze는 추천 이벤트에 대한 의견 데이터 스키마를 정의합니다. 여기에는 Braze에서 유효성 검사 프로세스를 거치는 필수 및 선택적 이벤트 속성이 포함됩니다. 사용자 [지정 이벤트는]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 추적하려는 앱이나 웹사이트에서 사용자가 수행한 특정 작업 또는 업데이트입니다. 이벤트 이름과 이벤트가 추적하는 대상을 사용자 지정할 수 있습니다.

### 추천 이벤트의 이름을 사용자 지정할 수 있나요?

아니요. 추천 이벤트에는 표준화된 이벤트 이름과 속성이 있습니다. 이러한 표준화는 데이터 전반에서 일관성을 유지하는 데 도움이 됩니다.

### 구매 이벤트를 사용하여 구매를 기록할 수 있나요?

이커머스 추천 이벤트가 출시됨에 따라 Braze는 향후 기존 구매 이벤트를 단계적으로 폐지할 예정입니다. 현재 구매 이벤트를 사용 중인 경우 지원 중단 계획에 대한 사전 공지를 받게 됩니다. 한편, 공식 지원 중단일까지는 구매 이벤트를 계속 이용할 수 있습니다.