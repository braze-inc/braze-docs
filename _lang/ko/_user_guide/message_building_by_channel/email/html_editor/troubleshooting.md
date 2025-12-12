---
nav_title: 문제 해결
article_title: 문제 해결
page_order: 9
description: "이 도움말 기사는 HTML 이메일 문제를 해결하는 방법을 안내합니다."
channel: email
---

# 문제 해결 

## 테스트 이메일에서 HTML이 잘못 렌더링됨

만약 당신의 [테스트 이메일]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)이 이상하게 보인다면, 먼저 HTML 설정을 확인하는 것을 권장합니다. 다음으로, 다음 문제를 확인할 수 있습니다:
* [확장 프로그램 충돌](#check-conflicts)
* [이메일 렌더링](#check-rendering)
* [CSS 인라인화](#switch-css-inlining)

### 확장 프로그램 충돌

특정 브라우저 확장 프로그램이 우리의 이메일 편집기에 문제를 일으킬 수 있습니다. 한 예로는 Google Chrome에서 사용할 때 [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)가 있습니다. 이러한 확장 프로그램 중 하나를 사용하고 있다면, 다음 중 하나를 선택해야 합니다: 
- Grammarly가 브라우저 확장 프로그램으로 없는 브라우저에서 Braze 이메일 편집
- Braze 계정 관리자에게 연락하여 이메일 편집기를 HTML 전용 또는 일반 텍스트로 전환해 달라고 요청합니다. 

일반 텍스트 보기에서는 ```WYSIWYG``` (보는 것이 얻는 것) 편집기가 제거되므로, 이 요청을 하기 전에 모든 팀원이 HTML에 익숙한지 먼저 확인해야 합니다.

### 이메일 렌더링

이메일은 브라우저와 이메일 클라이언트에 따라 다르게 렌더링되므로, 문제가 발생하는 브라우저와 이메일 클라이언트를 주의 깊게 살펴보세요.

- 다양한 브라우저와 이메일 클라이언트에서 이메일이 어떻게 보이는지 확인하기 위해 [인박스 비전]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)을 사용하여 이메일을 미리 봅니다.
- 어떤 브라우저나 이메일 클라이언트가 문제를 일으키는지 확인한 후, 개발 팀에게 알려서 그들이 HTML을 수정하고 해당 브라우저나 이메일 클라이언트에 맞게 편집해야 한다고 알리세요.

### CSS 인라인화

인박스 비전의 미리보기가 브레이즈와 함께 전송된 내용과 일치하지 않는 경우가 있습니다. 이는 브레이즈와 다른 도구에서 수행되는 CSS 인라인 처리의 차이로 인해 발생할 수 있습니다. 이 경우일 수 있다고 의심되면 CSS 인라인 처리를 끄십시오.

아직 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 열어보세요.
