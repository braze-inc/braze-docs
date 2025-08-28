---
nav_title: 11월
page_order: 1
noindex: true
page_type: update
description: "이 문서에는 2021년 11월의 릴리스 노트가 포함되어 있습니다."
---
# 2021년 11월

## 클릭 투 오픈 비율 보고 지표
Braze는 [보고서 작성기에서]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 수 있는 새로운 이메일 지표인 클릭 후 열기 비율을 추가했습니다. 이 메트릭은 클릭된 열린 이메일의 비율을 나타냅니다.

## 머신 오픈 보고 메트릭

새로운 이메일 지표인 [머신 오픈]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)은 이메일에 대한 캔버스 및 캠페인 분석 페이지에서 사용할 수 있습니다. 이 메트릭은 사람이 아닌 사람이 열어본 이메일(예: Apple 서버에서 열어본 이메일)을 식별하며, 전체 열어본 이메일의 하위 집합으로 표시됩니다.

## random_bucket_number Liquid 변수
메시지 개인화를 위해 [지원되는 Liquid 변수]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) 목록에 `random_bucket_number` 변수가 추가되었습니다. 

## iOS 15 리치 푸시 알림 가이드라인
iOS 리치 문서에 알림 상태 및 텍스트 잘림 변수에 대한 분석 정보를 포함한 새로운 [iOS 푸시 알림 가이드라인]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)이 추가되었습니다.

## 웹훅 및 커넥티드 콘텐츠에 대해 EU에서 화이트리스트에 등록할 IP
[웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 및 커넥티드 콘텐츠 문서에 EU에서 웹훅 및 [커넥티드 콘텐츠에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) 대해 화이트리스트에 추가할 IP가 추가되었습니다. 이러한 새로운 IP에는 `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188`, `3.70.107.88`이 포함됩니다.

## 구매 엔드포인트 내보내기
Braze에 새로운 [`/purchases/product_list` 엔드포인트]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)가 추가되었습니다. 이 엔드포인트는 제품 ID의 페이지가 매겨진 목록을 반환합니다.

## 새로운 Braze 파트너십

### Adobe - 고객 데이터 플랫폼
Braze와 [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe)의 통합을 통해 브랜드는 Adobe 데이터(커스텀 속성 및 세그먼트)를 실시간으로 Braze에 연결하고 매핑할 수 있습니다. 그런 다음 브랜드는 이 데이터를 기반으로 조치를 취하여 해당 사용자에게 개인화된 타겟팅 경험을 제공할 수 있습니다. 

### BlueConic - 고객 데이터 플랫폼
Braze 사용자는 [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic)을 통해 데이터를 영구적인 개별 프로필로 통합한 다음 고객 생애주기 오케스트레이션, 모델링 및 분석, 디지털 제품 및 경험, 오디언스 기반 수익화 등 광범위한 성장 중심 이니셔티브를 지원하기 위해 고객 터치포인트와 시스템 전반에서 이를 동기화할 수 있습니다.

### Worthy - 동적 콘텐츠
Braze와 [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy)의 통합을 통해 Worthy의 드래그 앤 드롭 동적 콘텐츠 에디터를 사용하여 개인화된 풍부한 인앱 경험을 손쉽게 제작하고 Braze를 통해 전달할 수 있습니다.

### 유도 - 동적 콘텐츠
[Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) 및 Braze 통합을 통해 캠페인의 구성 요소를 덮어쓰고 유도 경험으로 대체할 수 있습니다. Braze의 데이터는 Judo 경험에서 개인화된 콘텐츠를 지원하기 위해 사용될 수 있습니다. 사용자 이벤트와 경험에서 얻은 데이터는 기여도 및 타겟팅을 위해 Braze에 피드백될 수 있습니다.

### Line - 메시징
[Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line)과 Braze 통합을 통해 Braze 웹훅, 고급 세분화, 개인화 및 트리거 기능을 활용하여 [Line 메시징 API](https://developers.line.biz/en/docs/messaging-api/overview/)를 통해 라인에서 사용자에게 메시지를 보낼 수 있습니다.

### RevenueCat - 결제
[RevenueCat과]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) Braze의 통합을 통해 고객의 구매 및 구독 생애주기 이벤트를 여러 플랫폼에서 자동으로 동기화할 수 있습니다. 이를 통해 무료 평가판 사용 중 옵트아웃한 고객과 소통하거나 청구 문제가 있는 고객에게 알림을 보내는 등 고객의 구독 라이프사이클 단계에 따라 반응하는 캠페인을 구축할 수 있습니다.

### Punchh - 로열티
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)는 선물 및 로열티 목적으로 Braze와 제휴하여 두 플랫폼에서 데이터를 동기화했습니다. Braze에 게시된 데이터는 세분화에 사용할 수 있으며, Braze에서 설정한 웹훅 템플릿을 통해 사용자 데이터를 다시 Punchh로 동기화할 수 있습니다.  