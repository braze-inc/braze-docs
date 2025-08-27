---
nav_title: 테스트 이메일에서 HTML 렌더링
article_title: 테스트 이메일에서 HTML 렌더링
page_order: 2

page_type: solution
description: "이 도움말 문서는 테스트 이메일에서 HTML 렌더링 문제를 해결하는 방법을 안내합니다."
channel: email
---

# 테스트 이메일에서 HTML 렌더링 문제 해결

[테스트 이메일]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)이 이상해 보이면 먼저 HTML 설정을 확인하는 것이 좋습니다. 다음으로, 이러한 문제를 확인할 수 있습니다:
* [확장 충돌](#check-conflicts)
* [이메일 렌더링](#check-rendering)
* [CSS 인라이닝](#switch-css-inlining)

### 확장 충돌

일부 브라우저 확장 프로그램은 이메일 편집기에서 문제를 일으킬 수 있습니다. 한 가지 예는 [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en))가 Google Chrome과 함께 사용될 때입니다. 이 확장 프로그램 중 하나를 사용 중인 경우 다음 중 하나를 수행해야 합니다. 
- 브라우저 확장 프로그램으로 Grammarly가 없는 브라우저에서 Braze 이메일을 편집합니다
- 귀하의 Braze 계정 매니저에게 연락하여 이메일 편집기를 HTML 전용 또는 일반 텍스트로 전환하도록 요청하십시오. 

일반 텍스트 보기에서는 ```WYSIWYG``` (보이는 대로 편집) 편집기가 제거되므로, 이 요청을 하기 전에 모든 팀원이 HTML에 익숙한지 먼저 확인해야 합니다.

### 이메일 렌더링

이메일은 브라우저와 이메일 클라이언트에 따라 다르게 렌더링되므로, 문제가 발생하는 브라우저와 이메일 클라이언트를 주의 깊게 확인하세요.

- [받은편지함 Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)을 사용하여 이메일을 미리 보고, 다양한 브라우저와 이메일 클라이언트에서 이메일이 어떻게 보이는지 확인하세요.
- 어떤 브라우저나 이메일 클라이언트가 문제를 일으키는지 확인한 후, 개발자 팀에게 HTML을 수정하고 해당 브라우저나 이메일 클라이언트를 수용할 수 있도록 편집해야 한다고 알려주세요.

### CSS 인라이닝

받은편지함 비전의 미리보기가 여전히 Braze로 전송된 것과 일치하지 않는 경우가 있습니다. 이것은 Braze 및 기타 도구에 의해 수행되는 CSS 인라인 차이로 인해 발생할 수 있습니다. 이 경우라고 의심되면 Braze 계정 매니저에게 CSS 인라이닝을 끄도록 요청하세요.

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 날짜: 2021년 12월 21일_

