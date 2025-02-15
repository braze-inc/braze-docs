---
nav_title: 사용자 지정 이벤트 추적
article_title: 웹용 사용자 지정 이벤트 추적
platform: Web
page_order: 2
page_type: reference
description: "이 문서에서는 사용자 지정 이벤트를 추적하고 해당 이벤트에 웹용 속성을 추가하는 방법에 대해 설명합니다."

---

# 사용자 지정 이벤트 추적

> Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요. 또한 [이벤트 이름 지정 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) 숙지하는 것이 좋습니다.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

자세한 내용은 [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) 문서를 참조하세요.

## 속성정보 추가 {#properties-events}

선택적으로 사용자 지정 이벤트와 함께 속성 개체를 전달하여 사용자 지정 이벤트에 대한 메타데이터를 추가할 수 있습니다.

속성은 키-값 쌍으로 정의됩니다. 키는 문자열이며 값은 `string`, `numeric`, `boolean` 또는 [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) 오브젝트일 수 있습니다.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

자세한 내용은 [`logCustomEvent()` 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 참조하세요.

