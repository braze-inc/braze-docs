---
nav_title: 인앱 메시지가 표시되지 않음
article_title: 인앱 메시지가 표시되지 않음
page_order: 1

page_type: solution
description: "이 도움말 문서에서는 인앱 메시지가 제대로 표시되지 않거나 렌더링되지 않는 문제 해결 방법을 안내합니다."
channel: in-app messages
---

# 인앱 메시지가 표시되지 않음

인앱 메시지가 제대로 표시되지 않거나 렌더링되지 않는 경우 여러 가지 방법으로 확인할 수 있습니다:

* [이벤트 트리거](#event-triggers)
* [메시지 노출 횟수](#message-impressions)
* [테스트](#run-tests)
* [세션 시간 초과](#session-timeout)
* [메시징 간격](#minimum-interval)

## 이벤트 트리거

캠페인이 세션 시작 또는 사용자 지정 이벤트에 의해 트리거되는 경우, 이 이벤트 또는 세션이 메시지를 트리거할 수 있을 만큼 자주 발생하는지 확인해야 합니다. 이 데이터는 [개요][1] (세션 데이터의 경우) 또는 [사용자 지정 이벤트][2] 페이지에서 확인할 수 있습니다:

![한 달 동안 즐겨찾기에 추가된 커스텀 이벤트가 발생한 횟수를 그래프로 보여주는 커스텀 이벤트 페이지][14]

## 메시지 노출 횟수

SDK 내에서 인앱 메시지 UI 또는 전달 메커니즘을 커스텀하려면 개발자가 인앱 메시지 노출 횟수를 수동으로 기록하는 방법을 활용해야 할 수 있습니다. 인앱 메시지 사용자 지정을 사용하는지 개발자에게 문의하세요.

## 테스트 실행

트리거 이벤트가 발생하지 않거나 메시지 자체가 표시되지 않는지 확인하는 것이 중요합니다. 테스트하려면 다른 작업(세션 시작 또는 다른 커스텀 이벤트 등)을 사용하여 메시지를 트리거하고 표시되는지 확인합니다. 이렇게 하면 데이터 문제일 가능성이 있는 경우 이를 격리하는 데 도움이 됩니다.

또는 다른 유형의 인앱 메시지 템플릿이나 이미지 크기를 사용해 보세요. 반드시 준수해야 하는 [인앱 메시지 사양][15]이 있습니다. 간혹 이미지가 너무 크면 인앱 메시지가 표시되지 않는 경우가 있습니다.

## 세션 시간 초과

세션 시간 초과를 사용자 지정했는지 확인하세요. 기본적으로 Braze는 세션이 시작될 때 서버에서 인앱 메시지를 검색합니다.

세션 시간 초과가 연장되면 귀하가 받을 수 있는 잠재적인 인앱 메시지를 새로고침할 수 있는 기간이 연장됩니다. 또한 캠페인이 세션 시작 시 트리거되도록 설정된 경우 새 세션을 등록하려면 적절한 시간이 경과했는지 확인해야 합니다. 예를 들어 세션 시간 초과를 30초로 사용자 지정했을 수 있습니다. 30초 이내에 앱을 열었다가 닫으면 세션 시작 시 트리거되는 다른 인앱 메시지를 받을 수 없습니다. 

다음 플랫폼의 세션 시간 초과를 사용자 지정하는 방법에 대해 자세히 알아보세요:
* [iOS][16]
* [Android][17]
* [웹][18]

## 최소 간격

인앱 메시지가 연속적으로 트리거되도록 허용하는 최소 간격이 있으므로 너무 빨리 트리거하려고 할 수 있습니다. 다음 플랫폼의 최소 간격에 대해 자세히 알아보세요: 
* [iOS][19]
* [Android][20]
* [웹][21]

간격은 사용자 지정할 수 있지만, 사용자에게 과도한 메시지가 전송되는 것을 방지하기 위해 간격을 설정할 수 있습니다.

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트: 2021년 7월 15일_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
