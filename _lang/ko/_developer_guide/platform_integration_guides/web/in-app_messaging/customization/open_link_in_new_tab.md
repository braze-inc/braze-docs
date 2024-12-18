---
nav_title: 새 탭에서 링크 열기
article_title: 웹용 새 탭에서 인앱 메시지 링크 열기
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "이 문서에서는 웹 애플리케이션의 새 탭에서 열리도록 인앱 메시지 링크를 설정하는 방법에 대해 설명합니다."

---

# 새 탭에서 링크 열기

> 이 문서에서는 웹 애플리케이션의 새 탭에서 열리도록 인앱 메시지 링크를 설정하는 방법에 대해 설명합니다.

인앱 메시지 링크를 새 탭에서 열도록 설정하려면 `openInAppMessagesInNewTab` 옵션을 `true`로 설정하여 인앱 메시지 클릭 시 모든 링크가 새 탭 또는 새 창에서 열리도록 합니다.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
