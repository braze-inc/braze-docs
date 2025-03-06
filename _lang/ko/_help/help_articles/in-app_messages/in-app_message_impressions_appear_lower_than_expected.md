---
nav_title: 낮은 인앱 메시지 노출 수
article_title: 낮은 인앱 메시지 노출 수
page_order: 2

page_type: solution
description: "이 도움말 문서에서는 인앱 메시지 노출 수가 원하는 수준보다 낮은 경우 취할 수 있는 조치에 대해 설명합니다."
channel: in-app messages
---
# 낮은 인앱 메시지 노출 수

노출 수가 원하는 것보다 낮다면 다음 사항을 확인하는 것이 좋습니다:
* [세그먼트 크기](#segment-size)
* [변경 로그](#segment-changelogs)
* [테스트 실행](#run-tests)
* [이벤트 트리거](#event-triggers)
* [메시지 노출 횟수](#message-impressions)

## 세그먼트 크기

캠페인의 세그먼트 크기가 의도한 오디언스를 반영하는지 확인하는 것이 중요합니다. 오디언스를 제한하고 캠페인 노출 수를 줄이는 필터가 적용되었을 수 있습니다.

## 세그먼트 변경 로그

이전과 비교하여 노출 수가 낮다면 론칭 이후 의도치 않게 세그먼트나 캠페인을 변경한 것이 아닌지 확인하세요. 세그먼트 및 캠페인 변경 로그를 통해 변경된 사항, 변경을 수행한 사람, 변경이 발생한 시점에 대한 인사이트를 얻을 수 있습니다.

![사용자가 마지막으로 캠페인을 본 이후 7가지 변경 사항이 포함된 캠페인 세부 정보 페이지의 변경 로그 보기 링크][10]

## 테스트 실행

명백한 문제를 빠르게 파악하는 방법은 캠페인을 복제하고 자신의 사용자 ID 또는 이메일을 타겟팅한 다음 캠페인을 실행하는 것입니다. 메시지 트리거(세션 시작, 사용자 지정 이벤트 등)를 수행한 후 메시지를 올바르게 수신했는지 확인합니다. 그런 다음 대시보드로 이동하여 페이지를 새로고침하여 노출이 올바르게 기록되었는지 확인합니다. 그렇지 않다면 구현에 문제가 있을 가능성이 높습니다.

## 이벤트 트리거

캠페인이 세션 시작 또는 사용자 지정 이벤트에 의해 트리거되는 경우, 이 이벤트 또는 세션이 메시지를 트리거할 수 있을 만큼 자주 발생하는지 확인해야 합니다. 이 데이터는 [개요][1] (세션 데이터의 경우) 또는 [사용자 지정 이벤트][2] 페이지에서 확인할 수 있습니다:

![한 달 동안 즐겨찾기에 추가된 커스텀 이벤트가 발생한 횟수를 그래프로 보여주는 커스텀 이벤트 페이지][11]

## 메시지 노출 횟수

SDK 내에서 인앱 메시지 UI 또는 전달 메커니즘을 커스텀하려면 개발자가 인앱 메시지 노출 횟수를 수동으로 기록하는 방법을 활용해야 할 수 있습니다. 인앱 메시지 사용자 지정을 사용하는지 개발자에게 문의하세요:
  * [iOS][12] 
  * [Android][13] 

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 5월 6일, 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/ {{site.baseurl}}/developer_
 [13]:{{site.baseurl}}guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
