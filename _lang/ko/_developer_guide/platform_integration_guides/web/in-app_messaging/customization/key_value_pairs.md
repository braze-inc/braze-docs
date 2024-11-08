---
nav_title: 키-값 쌍
article_title: 웹용 인앱 메시지 키-값 쌍
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "이 문서에서는 인앱 메시징 키-값 페어를 활용하여 웹 애플리케이션에 정보를 표시하는 방법을 다룹니다."

---

# 키-값 쌍

> 이 문서에서는 인앱 메시징 키-값 페어를 활용하여 웹 애플리케이션에 정보를 표시하는 방법을 다룹니다.

인앱 메시지 오브젝트는 키-값 페어를 `extras` 속성정보로 전달할 수 있습니다. 인앱 메시지 캠페인을 생성할 때 대시보드의 **설정**에서 지정됩니다. 사이트에서 추가 처리를 위해 인앱 메시지와 함께 데이터를 전송하는 데 사용할 수 있습니다. 예를 들어, 다음과 같습니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
