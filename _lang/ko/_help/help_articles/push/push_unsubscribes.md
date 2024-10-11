---
nav_title: 푸시 수신 거부 추적
article_title: 푸시 수신 거부 추적
page_type: solution
description: "이 도움말 문서에서는 푸시 수신 거부 추적에 대한 몇 가지 팁을 제공합니다."
channel: push
---

# 푸시 수신 거부 추적 기술

푸시 수신 거부 여부는 Apple 또는 Google과 같은 제공업체의 사용자 푸시 상태 업데이트에 따라 달라집니다. 이러한 업데이트는 드물고 예측하기 어려울 수 있습니다. 따라서 푸시 구독 취소는 푸시 캠페인 분석의 지표로 포함되지 않습니다. 

하지만 수동으로 푸시 수신 취소를 추적하면 알림 빈도 및 콘텐츠 관련성에 대한 사용자 반응에 대한 귀중한 인사이트를 얻을 수 있습니다. 다음은 푸시 수신 거부 추적을 위한 두 가지 옵션입니다.

## 옵션 1: 세그먼트 필터 사용

해결 방법으로 세그먼트를 생성하여 푸시가 활성화되지 않은 사용자, 즉 구독 또는 옵트인하지 않았고 [포그라운드 푸시 토큰]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)이 없는 사용자를 식별할 수 있습니다. 예를 들어 Android 앱에서 구독 취소 횟수를 확인하려면 다음 세그먼트의 조합을 사용합니다. 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![테스트(Android) 앱에 대해 "앱에 백그라운드 또는 포그라운드 푸시 사용" 필터가 있는 세그먼트 빌더 섹션이 거짓이고 "제거됨" 필터가 선택되어 도달 가능한 사용자 2,393명을 표시합니다.]({% image_buster /assets/img/push_unsub_segment_example.png %})

세분화 필터는 대략적인 기준이며 날짜 및 캠페인에 구체적으로 연결될 수 없습니다.

## 옵션 2: 사용자 지정 이벤트 사용

{% alert important %}
구독 변경에 대한 사용자 지정 이벤트를 기록하면 [데이터 포인트가]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count) 소모된다는 점에 유의하세요. 또는 세그먼트 필터를 사용하여 푸시를 사용 설정하지 않은 사용자를 식별하고 타겟팅할 수 있습니다.
{% endalert %}

다른 해결 방법으로는 사용자의 푸시 사용 설정 상태가 `true` 또는 `false`인지에 따라 푸시 수신 거부 커스텀 이벤트를 생성하여 이 지표를 추적하는 것이 좋습니다.

_마지막 업데이트 2024년 6월 13일_
