---
nav_title: 사용자 지정 이벤트 추적
article_title: Unity에 대한 커스텀 이벤트 추적
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "이 참조 문서는 Unity 플랫폼에서 커스텀 이벤트를 기록하는 방법을 다룹니다."

---

# 사용자 지정 이벤트 추적

> Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다.

구현하기 전에 [모범 사례][4]에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요. 또한 [이벤트 이름 지정 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)을 숙지하는 것이 좋습니다.

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze는 이벤트 속성정보의 `Dictionary`를 전달하여 커스텀 이벤트에 대한 메타데이터를 추가하는 기능도 지원합니다.

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

또한 REST API를 사용하여 이벤트를 기록할 수 있습니다. 자세한 내용은 [사용자 API][5] 설명서를 참조하세요.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
