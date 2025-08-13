---
nav_title: Shopify 개요
article_title: "Shopify 개요"
description: "이 참조 문서에서는 글로벌 커머스 회사인 Shopify와 Braze 간 파트너십을 간략히 설명합니다. 이를 통해 Shopify 스토어와 Braze를 원활하게 연결하여 일부 Shopify 웹훅을 Braze로 전달할 수 있습니다. Braze의 크로스채널 전략과 캔버스를 활용하여 고객이 구매를 완료하도록 넛지하거나 이전 구매를 기반으로 사용자를 리타겟팅합니다."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Shopify 개요

> [Shopify는](https://www.shopify.com/) 모든 규모의 소매 비즈니스를 시작, 성장, 마케팅 및 관리할 수 있는 신뢰할 수 있는 도구를 제공하는 선도적인 글로벌 상거래 기업입니다. Shopify는 안정성을 위해 설계된 플랫폼과 서비스를 통해 전 세계 소비자에게 더 나은 쇼핑 경험을 제공하는 동시에 모든 사람에게 더 나은 상거래를 제공합니다.

Shopify와 Braze 통합을 통해 Shopify 스토어를 연결하여 Shopify 데이터를 Braze에 원활하게 전달할 수 있습니다. 크로스 채널 전략과 Braze의 캔버스를 활용하여 새로운 리드의 참여를 유도하고, 신규 고객에게 메시지를 보내거나, 결제 중단 메시지를 통해 사용자를 리타겟팅하여 구매를 완료하도록 유도할 수 있습니다.


{% alert important %}
A new version of the Shopify integration will be released in phases starting April, based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**The older version of the integration will be deprecated on August 28, 2025. You must update to the newer version of the integration before August 28, 2025.**<br><br>**New Braze customers:** Starting April 2025, Braze will be gradually rolling out the new Shopify connector for new onboardings and upgrading existing customers. To learn more about the new standard integration, refer to [Shopify standard integration]({{site.baseurl}}/shopify_standard_integration/).<br><br>**Existing Braze customers:** Starting in February 2025, we will contact you with an upgrade guide to help you transition to the newer Shopify integration.  We will organize customers into groups (cohorts) based on your Shopify store and how you use Braze external IDs to facilitate a smooth and personalized upgrade experience. You will be notified when your cohort is ready to upgrade.<br><br>**Upgrading to this newer version will cause breaking changes.** You will be guided through a review process on the Braze dashboard to help you and your development team address these changes before you upgrade.
{% endalert %}

## 지원되는 기능

- Braze 웹 SDK를 통해 현장 행동 및 익명 사용자 추적
- Braze 웹 SDK를 통해 Braze의 Shopify 고객 동기화 및 조정 지원
- Shopify 고객 데이터 동기화
- Shopify 이메일 및 SMS 구독자 옵트인 가입 상태 수집
- 과거 Shopify 구매 데이터 백필 
- Shopify 카탈로그 동기화 
- 인앱 메시지를 채널로 사용 

## 지원되는 사용 사례 

- 구매 경로 캠페인 및 캔버스 사용자 여정. 다음을 포함합니다. 
  - 유기 찾아보기 
  - 방치된 장바구니 
  - 중단된 결제 
- 구매 후 캠페인 및 캔버스 사용자 여정. 다음을 포함합니다.
  - 주문 확인 
  - 주문 처리 업데이트 
  - 주문 취소 
  - 주문 환불
- 제품 추천
- 교차 판매 및 상향 판매
- [재입고]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## 요구 사항

| 요구 사항 | 설명 |
| --- | --- |
| Shopify 스토어 | 활성 [Shopify](https://www.shopify.com/) 스토어가 있습니다.<br><br>작업 공간당 하나의 Shopify 스토어를 연결할 수 있습니다. 여러 스토어를 하나의 워크스페이스에 연결하는 데 관심이 있는 경우 고객 성공 매니저에게 문의하여 Shopify 멀티 스토어 베타에 참여합니다. |
| Shopify 사용자 권한 | Shopify 스토어에 대한 권한은 다음 중 하나입니다:{::nomarkdown}<ul><li>스토어 소유자</li><li>직원</li><li>모든 일반 및 온라인 스토어 설정과 이러한 추가 관리자 권한이 있는 회원입니다:<ul><li>주문</li><li>보기( <b>제품</b> 아래에 위치)</li><li>고객</li><li>설정 관리</li><li>직원 및 협업자가 개발한 앱 보기</li><li>앱 및 채널 관리 및 설치</li></ul></li></ul>{:/} |
| Braze 웹 SDK 구현 | 현장 행동 및 익명 사용자를 추적하려면 기본 Shopify 통합을 통해 또는 수동으로 Braze 웹 SDK를 구현해야 합니다. <br><br>구현 옵션에 대한 자세한 내용은 [Shopify 사이트에서 웹 SDK 구현]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)을 참조하세요. |
| 이벤트 속성 세분화 사용 | Shopify 이벤트 속성을 세분화할 수 있는지 확인하려면 고객 성공 관리자 또는 [Braze 지원팀에]({{site.baseurl}}/braze_support/) 문의하여 Braze 대시보드에 이벤트 속성 세분화가 설정되어 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 }

## 일반 데이터 보호 규정(GDPR)

고객에 의해 또는 고객을 대신해 Braze 서비스에 제출된 개인 데이터와 관련하여, Braze는 데이터 처리자이며 고객은 데이터 관리자입니다. 따라서 Braze는 고객의 지시에 의해서만 이러한 개인 데이터를 처리하며, 해당되는 경우 고객에게 데이터 주체의 요청을 통지합니다. 데이터 관리자인 고객은 데이터 주체의 요청에 직접 응답합니다. Braze 플랫폼에서 Shopify 통합의 일부로, Braze는 [Shopify의 GDPR 웹훅](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app)을 자동으로 수신합니다. 그러나 Braze 고객은 당사의 [GDPR 규정 준수]({{site.baseurl}}/dp-technical-assistance/) 정책에 따라 [Braze SDK]({{site.baseurl}}/developer_guide/home/) 또는 [REST API를]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 사용하여 Shopify 고객의 데이터 주체 요청에 응답할 최종적인 책임이 있습니다.
