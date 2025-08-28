---
nav_title: 7월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2016년 7월의 릴리스 노트가 포함되어 있습니다."
---

# 2016년 7월

## 오류 유형별로 개발자 콘솔의 오류 로그 필터링하기

이번 업그레이드를 통해 개발자 콘솔의 메시지 오류 로그를 사용하여 Braze 연동 관련 문제를 더 쉽게 해결할 수 있습니다. 이 사용성 업데이트를 통해 메시지 오류 로그를 유형별로 필터링하고 특정 연동 문제를 훨씬 쉽게 찾고 식별할 수 있습니다.

## 마지막 제거 추적 푸시 전송에 대한 타임스탬프 추가

Braze는 고객의 앱에 무음 푸시를 보내 응답하는 기기를 확인하여 제거를 감지합니다. 이 기능은 제거 추적이 마지막으로 실행된 시점을 나타내는 눈에 잘 띄지 않는 타임스탬프를 추가합니다. 이 타임스탬프는 제거 추적이 구성된 설정 페이지에서 찾을 수 있습니다. [제거 추적 해제]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)에 대해 자세히 알아보세요.

![추적 제거 확인란]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## 웹훅 테스트 개선 사항 추가

이제 캠페인을 라이브로 설정하기 전에 Braze에서 라이브 웹훅 메시지를 테스트 전송할 수 있습니다. 테스트 메시지를 보내면 안전한 샌드박스 환경에서 메시지와 서버 엔드포인트가 올바르게 구성되었는지 확인할 수 있습니다. [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)에 대해 자세히 알아보세요.

## 캠페인 수신자에게 수신되는 메시지 변형 CSV 내보내기 추가

캠페인 수신자 CSV 내보내기에 수신된 메시지 변형을 나타내는 열을 추가했습니다. Braze에서 [데이터 내보내기]({{site.baseurl}}/user_guide/data/export_braze_data/)에 대해 자세히 알아보세요.

## 노출 수에 대한 대략적인 제한

인앱 메시지가 일정 횟수 이상 노출 횟수가 다성되면 Braze는 사용자가 메시지를 수신할 수 있는 자격을 더 이상 허용하지 않습니다. [노출 횟수에 대한 대략적인 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap) 설정에 대해 자세히 알아보세요.

![IAM 노출 캡]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})

