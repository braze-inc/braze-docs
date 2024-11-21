---
nav_title: 노출 횟수 및 클릭 기록
article_title: 노출 횟수 및 클릭 기록
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "이 문서에서는 웹 애플리케이션에 대한 인앱 메시지 노출 및 클릭을 기록하는 방법을 다룹니다."

---

# 노출 횟수 및 클릭 기록

> 이 문서에서는 웹 애플리케이션에 대한 인앱 메시지 노출 및 클릭을 기록하는 방법을 다룹니다.

인앱 메시지 [노출 횟수](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) 및 [클릭](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) 기록은 `showInAppMessage` 또는 `automaticallyShowInAppMessage` 메서드를 사용할 때 자동으로 수행됩니다.

두 방법 중 하나를 사용하지 않고 직접 UI 코드를 사용하여 메시지를 수동으로 표시하는 경우, 분석을 기록하려면 다음 방법을 사용하십시오:

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(inAppMessage);
// Registers that a user has clicked on the specified in-app message with the Braze server.
braze.logInAppMessageClick(inAppMessage);
// Registers that a user has clicked a specified in-app message button with the Braze server.
braze.logInAppMessageButtonClick(button, inAppMessage);
// Registers that a user has clicked on a link in an HTML in-app message with the Braze server.
braze.logInAppMessageHtmlClick(inAppMessage, buttonId?, url?)
```


