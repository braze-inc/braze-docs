---
nav_title: 사용자 지정 이벤트 추적
article_title: Roku용 사용자 지정 이벤트 추적
platform: Roku
page_order: 2
page_type: reference
description: "이 페이지에서는 Braze SDK를 통해 Roku의 커스텀 이벤트를 기록하는 방법을 다룹니다."

---

# 사용자 지정 이벤트 추적

> Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다. 또한 [이벤트 이름 지정 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)을 숙지하는 것이 좋습니다.

## 사용자 지정 이벤트 추가

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### 속성정보 추가

사용자 지정 이벤트와 함께 속성 사전을 전달하여 사용자 지정 이벤트에 대한 메타데이터를 추가할 수 있습니다.

속성은 키-값 쌍으로 정의됩니다.  키는 `String` 오브젝트이고 값은 `String` 또는 `Integer`일 수 있습니다.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
