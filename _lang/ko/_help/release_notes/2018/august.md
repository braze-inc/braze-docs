---
nav_title: 8월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2018년 8월의 릴리스 노트가 포함되어 있습니다."
---
# 2018년 8월

## iOS 12 알림 그룹

최근 iOS 12 릴리스에서는 애플리케이션에 대한 알림 그룹화(Android 알림 채널과 유사)를 지원합니다. [Braze에서는 메시지 작성기를 사용하여 iOS에서 이 그룹화 기능을 활용할 수 있습니다.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## 푸시 스토리 트리거링

이제 푸시 스토리 슬라이드의 특정 페이지 클릭을 기반으로 사용자를 리타겟팅할 수 있습니다. **캠페인과 상호 작용한 캠페인**에 대한 추가 필터를 사용합니다.

## 익명 사용자의 S3 및 Azure 데이터 이벤트

이제 Amazon S3 및 Microsoft Azure로 데이터를 내보내는 고객은 익명 사용자의 이벤트를 포함할 수 있습니다. 이 기능은 새로 생성된 모든 통합에 대해 기본적으로 켜짐으로 설정되지만 기존 통합에 대해서는 꺼진 상태로 유지됩니다. 궁금한 점이 있으면 계정 매니저에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support/)을 개설하세요.

## 믹스패널 코호트 통합

이제 Braze와 Mixpanel을 모두 사용하는 고객은 [Mixpanel 코호트를 통합하여 세그먼트 필터로 Braze에 보낼]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import) 수 있습니다. 한 번 수동 내보내기를 설정하거나 2시간마다 동적 내보내기를 설정할 수 있습니다. 업데이트된 각 사용자는 데이터 포인트로 계산되지만 Mixpanel은 마지막 동기화 이후의 변경 사항만 전송합니다.

