---
nav_title: 8월
page_order: 4
noindex: true
page_type: update
description: "이 문서에는 2021년 8월의 릴리스 노트가 포함되어 있습니다."
---

# 2021년 8월

## Google 오디언스 동기화

Braze [오디언스 싱크와 Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) 통합을 통해 브랜드는 크로스채널 고객 여정의 도달 범위를 Google 검색, Google 쇼핑, 지메일, 유튜브, Google 디스플레이로 확장할 수 있습니다. 퍼스트파티 고객 데이터를 사용하면 동적 행동 트리거, 세분화 등을 기반으로 광고를 안전하게 전달할 수 있습니다. 일반적으로 메시지를 트리거하는 데 사용하는 모든 기준(예: 푸시, 이메일, SMS 등)을 Braze 캔버스의 일부로 사용하여 Google의 고객 일치를 통해 해당 사용자에게 광고를 트리거할 수 있습니다.

## 모범 사례 iOS SDK 통합 가이드

이 선택 사항 [iOS 통합 SDK 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk)는 iOS SDK와 핵심 구성 요소를 애플리케이션에 처음 통합할 때 설정 모범 사례에 대한 단계별 여정을 안내합니다. 이 가이드는 나머지 프로덕션 코드에서 Braze iOS SDK에 대한 모든 종속성을 분리하는 `BrazeManager.swift` 도움말 파일을 빌드하여 전체 애플리케이션에서 하나의 `import AppboyUI` 도움말 파일을 생성하는 데 도움이 됩니다. 이 접근 방식은 과도한 SDK 가져오기로 인해 발생하는 문제를 제한하여 코드를 쉽게 추적, 디버그 및 변경할 수 있도록 합니다. 

## 예측 기반 구매

예측 구매는 마케터에게 구매 가능성을 기반으로 사용자를 식별하고 메시지를 전달할 수 있는 강력한 도구를 제공합니다. 구매 예측을 생성하면 Braze는 [그라데이션 부스트 의사 결정 트리를](https://en.wikipedia.org/wiki/Gradient_boosting) 사용하여 머신러닝 모델을 학습시켜 이전 구매 활동에서 학습하고 향후 구매 활동을 예측합니다. 자세한 내용은 [예측 구매]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) 문서를 참조하세요. 

## 드래그 앤 드롭 편집기

Braze Email을 사용하면 새로운 [드래그 앤 드롭 편집 환경을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/) 사용하여 캠페인이나 캔버스에서 완전히 맞춤화된 개인 이메일 메시지를 만들 수 있습니다. 이제 사용자는 편집기 블록을 이메일로 드래그하여 보다 직관적으로 사용자 지정할 수 있습니다. 

## 사용자 별칭 가져오기

`external_id`가 없는 사용자를 타겟팅하려면 [사용자 별칭이 있는 사용자 목록을 가져올]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) 수 있습니다. 별칭은 대체 고유 사용자 식별자 역할을 합니다. 앱에 가입하거나 계정을 만들지 않은 익명 사용자를 대상으로 마케팅하려는 경우 유용할 수 있습니다. 

## iOS 15 업그레이드 가이드

이 [iOS 15 업그레이드 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/)는 iOS 15(WWDC21)에 도입된 변경 사항과 Braze iOS SDK 통합에 필요한 업그레이드 단계를 간략하게 설명합니다.

## Android 12 업그레이드 가이드

이 [안드로이드 12 업그레이드 가이드]({{site.baseurl}}/developer_guide/platforms/android/android_13/)에서는 Android 12(2021)에 도입된 관련 변경 사항과 Braze Android SDK 통합에 필요한 업그레이드 단계를 설명합니다.

## A2P 10DLC

A2P 10DLC는 미국에서 기업이 표준 10자리 긴 코드(10DLC) 전화번호를 통해 A2P(애플리케이션 대 개인) 유형의 메시징을 보낼 수 있는 시스템을 말합니다. 10자리 긴 코드는 전통적으로 개인 간(P2P) 트래픽을 위해 설계되어 기업이 제한된 처리량과 강화된 필터링에 의해 제약을 받게 됩니다. 이 서비스는 이러한 문제를 완화하여 전반적인 메시지 전달력을 개선하고 브랜드가 링크와 클릭 유도 문안을 포함한 메시지를 대규모로 전송할 수 있도록 지원하며 원치 않는 메시지로부터 소비자를 더욱 보호할 수 있습니다. 

현재 미국 긴 코드를 보유하고 있거나 미국 고객에게 전송하기 위해 사용하는 모든 고객은 10DLC에 긴 코드를 등록해야 합니다. 10DLC의 세부 사항과 필요한 이유에 대해 자세히 알아보려면 [10DLC 전용 문서]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/)를 참조하세요.

## 2단계 인증 초기화

2단계 인증을 통해 로그인하는 데 문제가 있는 사용자는 회사 관리자에게 연락하여 [2단계 인증을 재설정할]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset) 수 있습니다.

## 새로운 Braze 파트너십

### Hightouch - 워크플로 자동화

Braze와 [하이터치]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) 통합을 통해 데이터 웨어하우스의 최신 고객 데이터로 Braze에서 더 나은 캠페인을 구축할 수 있습니다. 고객에게 관련성 있고 시의적절한 상호작용을 제공하려면 정확하고 최신의 Braze 계정 데이터에 크게 의존해야 합니다. 데이터 웨어하우스의 고객 데이터를 Braze에 자동으로 동기화하면 더 이상 데이터 일관성에 대해 걱정할 필요가 없으며, 세계 최고 수준의 고객 경험을 구축하는 데 집중할 수 있습니다.

### Transcend - 데이터 프라이버시 및 규정 준수

Braze와 [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/)는 파트너십을 통해 사용자는 수십 개의 데이터 시스템에서 데이터를 조율하여 개인정보 보호 요청을 자동화할 수 있습니다. 궁극적으로 이는 팀이 GDPR 및 CCPA와 같은 규정을 준수하고 개인이 자신의 데이터에 대해 주도권을 가질 수 있도록 도와줍니다.

### Tinyclues - 코호트 가져오기

고객 경험을 해치지 않으면서 캠페인 수와 수익을 늘릴 수 있는 잠재고객 구축 기능과 온라인과 오프라인에서 CRM 캠페인의 성과를 추적할 수 있는 분석 기능을 제공하는 [Tinyclues입니다]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/). Braze와 Tinyclues의 통합은 사용자에게 더 나은 CRM 계획 및 전략의 길을 열어주며, 사용자 친화적인 UI를 통해 더 많은 타겟팅 캠페인을 보내고, 새로운 제품 기회를 찾고, 매출을 확대할 수 있도록 지원합니다.

### optilyz - 다이렉트 메일

[optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/)는 보다 고객 중심적이고 지속 가능하며 수익성 있는 다이렉트 메일 캠페인을 운영할 수 있는 다이렉트 메일 자동화 플랫폼으로, 유럽 전역의 수백 개 기업이 사용하고 있으며 편지, 엽서, 셀프 메일러를 크로스채널 마케팅에 통합하고 캠페인을 자동화하고 개인화할 수 있도록 지원합니다. optilyz와 Braze 웹훅 통합을 사용하여 고객에게 다이렉트 메일을 보낼 수 있습니다.