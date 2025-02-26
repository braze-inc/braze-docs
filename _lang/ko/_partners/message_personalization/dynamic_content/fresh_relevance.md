---
nav_title: 새로운 관련성
article_title: 새로운 관련성
description: "이 참조 기사에서는 Braze와 다재다능한 개인화 플랫폼인 Fresh Relevance 간의 파트너십을 설명합니다. 이 플랫폼을 사용하면 Braze 캠페인 및 캔버스에 관련 제품을 포함할 수 있습니다."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# 새로운 관련성

> [Fresh Relevance][1]는 상업 중심의 비즈니스가 손쉽게 맞춤형 크로스채널 경험을 만들 수 있도록 지원하는 다재다능한 개인화 솔루션입니다. 플랫폼은 시간을 절약하고 기술 스택과 통합되며 IT 팀에 의존하지 않고도 웹사이트, {앱}, 이메일, SMS 및 광고 전반에 걸쳐 전환을 촉진하는 개인화된 고객 경험을 제공할 수 있도록 지원합니다.

Braze와 Fresh Relevance 통합을 통해 다음을 수행할 수 있습니다:
* 트리거된 고급 이메일 캠페인(예: 가격 인하, 재입고, 다단계 찾아보기 또는 장바구니 유기 메시지)을 전송합니다.
* 트리거된 이메일에 개인화된 콘텐츠를 포함합니다(예: 고객이 찾아본 제품이나 동일한 카테고리 내의 항목을 기반으로 한 제품 추천).
* 인공지능 기반 추천, 카운트다운 시간, 실시간 날씨 예보, 소셜 미디어 피드 등을 활용하여 대량 이메일 캠페인을 개인화합니다.
* 데이터 캡처 팝업을 통해 수집된 새 연락처로 이메일 데이터베이스를 확장하세요.
* Braze 이메일 링크에서 도착한 웹사이트 방문자를 식별합니다.

## 전제 조건

| 요구 사항 | 설명 |
|-------------| ----------- |
| Fresh Relevance 계정  | 이 파트너십을 활용하려면 Fresh Relevance 계정이 필요합니다. |
| Braze REST API 키 | 아래 나열된 엔드포인트에 충분한 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][3]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 캠페인 ID | 이메일을 보내는 데 사용하려는 기본값 Braze 캠페인. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Fresh Relevance에서 통합을 설정하려면 **메시징 채널**에서 Braze 채널을 생성하고 필요한 경우 적절한 Fresh Relevance 트리거 또는 콘텐츠에서 채널을 사용해야 합니다. 

단계별 지침은 Fresh Relevance에 로그인하고 [설명서][2]를 따르십시오.

Fresh Relevance 시스템은 제공된 API 키를 사용하여 Braze와 통신합니다. 완전한 통합은 다음 Braze API 엔드포인트를 사용합니다:

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/