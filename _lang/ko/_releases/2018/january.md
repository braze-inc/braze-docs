---
nav_title: 1월
page_order: 12
noindex: true
page_type: update
description: "이 문서에는 2018년 1월의 릴리스 노트가 포함되어 있습니다."
---
# 2018년 1월

## CSS 인라이닝

이제 **이메일 설정**으로 이동하여 개별 이메일 메시지에 대해 [CSS 인라인]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining)을 켜거나 끌 수 있습니다.

## 새로운 세그먼트 필터

이제 다음 필터를 사용하여 세그먼트를 만들 수 있습니다:
- 캔버스 단계 수신
- 연/클릭한 캔버스 단계
- 마지막으로 수신된 특정 캔버스 단계

{% alert update %}
2019년 3월부터 `Received Canvas Step`은 `Received Message from Canvas Step`으로, `Last Received Specific Canvas Step`은 `Last Received Message from Specific Canvas Step`으로 이름이 변경되었습니다.
{% endalert %}

## 디바이스 ID를 사용하여 사용자 내보내기

이 엔드포인트는 이제 [익명 사용자 프로필을 내보낼]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint) 수 있는 기기 식별자를 매개변수로 허용합니다.

기기 ID를 사용하여 해당 기기의 모든 고객 프로필을 내보낼 수 있습니다.

## 참여 보고서 업데이트

이제 **푸시 오픈율** 및 **전환율과** 같은 추가 통계를 [참여 보고서에서]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports) 확인할 수 있습니다.

## Apple 푸시 인증서: .p8 파일 사용

이제 Apple 푸시 인증서를 업로드할 때 [p8 파일]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens)을 사용하여 iOS 푸시 자격 증명이 만료되지 않도록 할 수 있습니다.


