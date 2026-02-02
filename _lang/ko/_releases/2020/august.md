---
nav_title: 8월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2020년 8월의 릴리스 노트가 포함되어 있습니다."
---
# 8월

## 외부 ID 마이그레이션 엔드포인트

Braze는 두 개의 새로운 외부 ID 마이그레이션 엔드포인트를 출시했습니다. 이러한 엔드포인트를 통해 고객은 Braze API를 활용하여 사용자의 Braze 외부 ID의 이름을 변경하거나 제거할 수 있습니다. 이러한 엔드포인트를 활용하여 다른 이름 지정 스키마를 가진 사용자를 마이그레이션하는 동시에 해당 사용자의 기록 데이터를 유지할 수 있습니다. [`users.external_ids.rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) 및 [`users.external_ids.remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) 엔드포인트에 대한 자세한 내용은 Braze 설명서를 참고하세요.

## Predictive Churn

Braze의 Predictive Suite은 머신 러닝을 직접 손에 넣을 수 있습니다. [예측 이탈]({{site.baseurl}}/user_guide/brazeai/predictive_suite/)을 시작으로, 그 어느 때보다 쉽게 데이터를 효과적으로 활용하고 Braze 플랫폼 내에서 원활하게 조치를 취할 수 있습니다. 이를 통해 특정 고객층의 이탈 위험을 예측하는 맞춤형 머신러닝 모델을 만든 다음, 머신러닝이 위험하다고 판단한 사용자에게 너무 늦기 전에 메시지를 보낼 수 있습니다. 

이 기능의 미리보기는 8월 초에 해당되는 Braze 고객의 대시보드에 표시될 예정입니다. 전체 기능을 이용하려면 계정 관리자에게 문의하세요.

## 커런츠 추적 기술 속성정보 업데이트

특정 커런츠 메시지 인게이지먼트 이벤트 내에서 추적 기술 속성정보 `canvas_variation_name` 및 `canvas_step_name`이 추가되었습니다. 전체 목록은 [메시지 참여 이벤트 용어집과]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) [커런츠 변경 로그에서]({{site.baseurl}}/user_guide/data/braze_currents/) 확인하세요.

## Amazon 개인화 파트너십

Amazon Personalize는 머신 러닝을 사용하여 웹사이트와 애플리케이션에 대한 고품질 추천을 생성합니다. Amazon 개인화를 사용하면 실시간 개인화된 상품 및 콘텐츠 추천과 타겟 마케팅 프로모션을 통해 고객 참여를 향상시킬 수 있습니다. 자세한 내용은 [Amazon 개인화]({{site.baseurl}}/partners/amazon_personalize/) 문서를 참조하세요.

## Vizbee 파트너십

Vizbee를 사용하면 집에 있는 모든 스마트폰과 스마트 TV를 하나의 원활한 기기로 통합하여 뛰어난 사용자 경험을 제공할 수 있습니다. Vizbee는 알림, 딥링크, 이메일과 같은 기존 모바일 앱 마케팅 채널을 활용하여 모든 CTV 기기(예: Roku, FireTV, 삼성 TV, LG TV 등)에서 시청자를 확보하고 참여를 유도할 수 있도록 지원합니다. 자세한 내용은 [Vizbee]({{site.baseurl}}/partners/message_orchestration/deeplinking/vizbee_for_tv_deeplinking/) 설명서를 참조하십시오. 

## Bluedot 파트너십

Bluedot은 앱에 정확하고 간단한 지오펜싱을 제공하는 위치 플랫폼입니다. Bluedot의 SDK를 사용하여 더 스마트하게 메시지를 보내고, 모바일 주문 체크인을 자동화하고, 워크플로를 최적화하고, 마찰 없는 경험을 만들 수 있습니다. 자세한 내용은 [Bluedot]({{site.baseurl}}/partners/data_augmentation/contextual_location/bluedot/#bluedot) 설명서를 참조하세요. 

## 파트너십 반복

Iterate는 브랜드와 같은 모양과 느낌의 스마트하고 사용자 친화적인 설문조사 도구를 제공하여 고객으로부터 쉽게 학습할 수 있도록 도와줍니다. 자세한 내용은 [반복하기]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/) 문서를 참조하세요. 
