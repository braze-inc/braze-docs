---
nav_title: 위치 데이터 확인
article_title: 위치 데이터 확인
page_order: 1
page_type: solution
description: "이 도움말 문서에서는 사용 가능한 위치가 없는 경우 도움이 될 수 있는 빠른 확인 방법을 안내합니다."
tool: Location
---

# 위치 데이터 확인

Braze는 기본적으로 SDK를 통해 사용자의 가장 최근 위치를 캡처합니다. 일반적으로 "최근 위치"는 사용자가 가장 최근에 앱을 사용한 위치를 의미합니다. Braze 백그라운드 위치 데이터를 전송하면 더 세분화된 데이터를 사용할 수 있습니다.

사용 가능한 위치가 없는 경우 두 가지 빠른 확인을 통해 데이터 수집 및 날짜 전송을 확인할 수 있습니다.

## 데이터 수집

앱이 위치 데이터를 수집하고 있는지 확인합니다:

- iOS의 경우, 이는 사용자가 사용자 여정의 어느 시점에서 메시지를 통해 위치 데이터 공유에 옵트인한다는 의미입니다. 
- Android의 경우 앱 설치 시 앱이 미세 또는 거친 위치 권한을 요청하는지 확인합니다.

사용자 위치 데이터가 Braze로 전송되고 있는지 확인하려면 **위치 사용 가능** 필터를 사용하세요. 이 필터를 사용하면 '가장 최근 위치'를 가진 사용자의 비율을 확인할 수 있습니다.

![]({% image_buster /assets/img_archive/trouble7.png %})

## 데이터 전송

개발자가 위치 데이터를 Braze에 전달하고 있는지 확인하세요. 일반적으로 위치 데이터 전달은 사용자가 권한을 부여한 후 SDK에서 자동으로 처리되지만, 개발자가 Braze에서 위치 추적을 비활성화했을 수 있습니다. 위치 추적에 대한 자세한 내용은 다음에서 확인할 수 있습니다:
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트: 2022년 11월 16일_

