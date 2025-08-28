---
nav_title: 8월
page_order: 5
noindex: true
page_type: update
description: "이 문서에는 2017년 8월의 릴리스 노트가 포함되어 있습니다."
---

# 2017년 8월

## 푸시 액션 버튼으로 업데이트

REST API 메시징 엔드포인트에 [푸시 실행 버튼]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons)에 대한 지원을 추가했습니다.

## Liquid 템플릿으로 업데이트

이제 다음을 기준으로 [메시지를 개인화할]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 수 있습니다:
- 전송받은 기기,
- 기기 ID,
- 이동통신사,
- IDFA,
- 모델,
- OS 및
- 플랫폼

## API 트리거 캔버스

이제 캠페인의 기존 엔드포인트와 일치하는 API 엔드포인트(전송, 예약, 업데이트, 삭제)를 통해 [캔버스를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) 트리거할 수 있으므로 마케팅을 더욱 자동화하고 최적화할 수 있습니다.

## 웹 푸시 액션 버튼

Chrome용 웹 SDK에 푸시 실행 버튼에 대한 지원을 추가하여 사용자에게 상황별 선택권을 제공함으로써 바쁜 일상을 간소화하여 인게이지먼트를 높일 수 있습니다. [푸시 알림에 대한 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)를 확인하세요.

## 새로운 API 엔드포인트

이메일 주소 또는 지정된 날짜 범위에서 하드 바운스를 가져올 수 있는 /email/hard_bounces와 예약된 캠페인 및 예약된 입력 캔버스가 시작될 다음 시간을 가져올 수 있는 messages/scheduled_broadcasts라는 새로운 API 엔드포인트를 노출했습니다. 이러한 새로운 엔드포인트를 통해 캠페인을 더욱 맞춤화하고 최적화할 수 있습니다. [API 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api)에 대해 자세히 알아보세요.

## 지오펜스

고객이 지정된 지리적 영역에 들어오고 나갈 때 실시간으로 메시지를 트리거할 수 있는 새로운 기능인 지오펜스를 추가하여 고객과 관련성 높은 개인화된 커뮤니케이션을 진행할 수 있습니다. [위치 마케팅]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/)에 대해 자세히 알아보세요.

## 이메일 편집기로 업데이트

새로운 이메일 편집기에 동적 자동 완성 기능을 추가하여 이제 Liquid를 사용할 때 고객의 실제 사용자 지정 속성 및 이벤트가 자동 완성되어 더욱 편리하게 사용할 수 있습니다. [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)에 대해 자세히 알아보세요.

## 최신 필터 업데이트

메시지를 수신하거나 상호 작용한 적이 없는 고객을 타겟팅할 수 있도록 "절대" 날짜 필터를 추가하여 고객 목록을 정리하고 이메일 전달 가능성을 보장할 수 있습니다. [필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters)에 대해 자세히 알아보세요.

## 캔버스로 업데이트

이제 각 캔버스 변형의 상단에 백분율을 추가하여 어떤 변형의 실적이 더 좋은지 한눈에 확인할 수 있습니다. [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)에 대해 자세히 알아보세요.

## 지능형 선택 기능이 있는 캔버스

이제 캔버스에 지능형 선택 기능이 추가되어 캔버스를 더욱 효율적으로 테스트할 수 있습니다. [Intelligence Suite]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)에 대해 자세히 알아보세요.

## 이메일 표시 이름으로 업데이트

이메일 표시 이름에 특수 UTF-8 문자를 지원하므로 고객에게 더욱 개인화된 이메일을 만들 수 있습니다. [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)에 대해 자세히 알아보세요.

## 참여 보고서 CSV 집계

이제 선택한 캠페인이나 캔버스 수에 관계없이 모든 캠페인과 모든 캔버스에 대한 통합 데이터를 두 개의 개별 파일로 받아볼 수 있으므로 필요한 데이터를 필요한 시점에 모두 확보할 수 있습니다. [참여 보고서]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/)에 대해 자세히 알아보세요.

> [2017년 9월 릴리즈 노트]({{site.baseurl}}/help/release_notes/2017/september/)에서 언급했듯이 이제 특정 기간의 데이터를 집계할 수 있을 뿐만 아니라 내보내기를 반복적으로 실행하도록 예약할 수도 있습니다.


