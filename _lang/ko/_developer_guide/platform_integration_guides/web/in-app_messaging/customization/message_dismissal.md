---
nav_title: 메시지 삭제
article_title: 웹용 인앱 메시지 삭제
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "이 문서에서는 웹 애플리케이션의 인앱 메시지 삭제에 대해 설명합니다."

---

# 메시지 삭제

> 이 문서에서는 웹 애플리케이션의 인앱 메시지 해제를 처리하는 방법에 대해 설명합니다.

기본적으로 인앱 메시지가 표시될 때 이스케이프 버튼을 누르거나 페이지의 회색 배경을 클릭하면 메시지가 해제됩니다. `requireExplicitInAppMessageDismissal` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 `true`로 구성하여 이 동작을 방지하고 메시지를 해제하려면 명시적으로 버튼을 클릭해야 합니다. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

