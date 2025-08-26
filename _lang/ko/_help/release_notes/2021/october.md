---
nav_title: 10월
page_order: 2
noindex: true
page_type: update
description: "이 문서에는 2021년 10월의 릴리스 노트가 포함되어 있습니다."
---
 
# 2021년 10월

## 데이터 포인트 사용량 대시보드

**총 데이터 포인트 사용량** 대시보드를 사용하여 계약 할당량과 관련된 데이터 포인트 사용 속도를 추적하세요. 이 대시보드는 계약, 현재 청구 주기, 회사 청구 데이터 및 워크스페이스 청구 데이터에 대한 정보를 제공합니다. 자세한 내용은 [청구서]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard)를 참조하세요.

## 세그먼트 확장 재생성으로 변경

2022년 2월 1일부터는 사용하지 않는 [세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)에 대해 매일 확장을 재생성하는 설정이 자동으로 해제됩니다. Braze는 다음 기준을 충족하는 확장을 사용되지 않은 확장으로 정의합니다.

- 활성 캠페인, 캔버스 또는 세그먼트에 사용되지 않음
- 비활성(임시저장본, 중지되었거나 아카이브된 상태) 캠페인, 캔버스 또는 세그먼트에 사용되지 않음
- 7일이 넘도록 수정되지 않음

Braze는 이 설정이 꺼지면 회사 연락처와 생성자에게 확장을 알립니다. 매일 확장 프로그램을 재생성하는 옵션은 언제든지 다시 설정할 수 있습니다.

## Android 고급 구현 가이드

### 콘텐츠 카드

이 선택 사항인 고급 [구현 가이드]({{site.baseurl}}/developer_guide/content_cards/)에서는 콘텐츠 카드 코드 고려사항, 유니티 팀이 구축한 세 가지 맞춤 사용 사례, 함께 제공되는 코드 스니펫, 노출 횟수, 클릭 수 및 해제 로깅에 대한 지침을 다룹니다.

### 인앱 메시징

이 선택적 고급 [구현 가이드]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)는 인앱 메시지 코드 고려사항, 저희 팀이 구축한 세 가지 사용자 지정 사용 사례 및 함께 제공되는 코드 스니펫을 다룹니다.

### 푸시 알림

이 선택 사항인 고급 [구현 가이드에서는]({{site.baseurl}}/developer_guide/push_notifications/examples/?sdktab=android) 사용자 지정 `FirebaseMessagingService` 하위 클래스를 활용하여 푸시 메시지를 최대한 활용하는 방법에 대해 설명합니다. 저희 팀이 구축한 커스텀 사용 사례와 함께 제공되는 코드 스니펫, 로깅 분석에 대한 안내가 포함되어 있습니다.

## 새로운 Braze 파트너십

### Adobe - 고객 데이터 플랫폼

Adobe Experience Platform을 기반으로 구축된 Adobe의 실시간 고객 데이터 플랫폼(실시간 CDP)은 기업이 여러 기업 소스의 알려진 데이터와 익명 데이터를 통합하여 모든 채널과 디바이스에서 개인화된 고객 경험을 실시간으로 제공하는 데 사용할 수 있는 고객 프로필을 생성할 수 있도록 지원합니다.

Braze와 [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/) CDP 통합을 통해 브랜드는 Adobe 데이터(사용자 지정 속성 및 세그먼트)를 실시간으로 Braze에 연결하고 매핑할 수 있습니다. 그런 다음 브랜드는 이 데이터를 기반으로 조치를 취하여 해당 사용자에게 개인화된 타겟팅 경험을 제공할 수 있습니다. 

### Shopify - 전자상거래

[Shopify는]({{site.baseurl}}/partners/shopify/) 모든 규모의 소매 비즈니스를 시작, 성장, 마케팅 및 관리할 수 있는 신뢰할 수 있는 도구를 제공하는 선도적인 글로벌 상거래 기업입니다. Braze와 Shopify 통합을 통해 브랜드는 Shopify 스토어를 Braze와 원활하게 연결하여 일부 Shopify 웹훅을 Braze로 전달할 수 있습니다. Braze의 크로스채널 전략과 캔버스를 활용하여 결제 중단 메시징으로 사용자를 리타겟팅하고 고객이 구매를 완료하도록 넛지하거나 이전 구매를 기반으로 사용자를 리타겟팅할 수 있습니다.