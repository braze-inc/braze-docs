---
nav_title: 테스트
article_title: 인앱 메시지 테스트
page_order: 4.5
description: "이 참고 문서에서는 인앱 메시지 테스트의 가치와 테스트 방법, 전송 전에 고려해야 할 사항의 체크리스트에 대해 설명합니다."
channel:
  - in-app messages
  
---

# 인앱 메시지 테스트

> 캠페인을 보내기 전에 항상 인앱 메시지를 테스트하는 것이 매우 중요합니다. 미리보기 및 테스트 기능을 통해 인앱 메시지를 살펴볼 수 있는 두 가지 방법이 있습니다. 메시지를 미리 보고 작성할 때 시각화할 수 있으며, 본인 또는 특정 사용자의 기기로 테스트 메시지를 보낼 수도 있습니다. 두 가지를 모두 활용하는 것이 좋습니다.

## 미리보기

인앱 메시지를 작성할 때 미리 볼 수 있습니다. 이렇게 하면 사용자의 관점에서 최종 메시지가 어떻게 보일지 시각화할 수 있습니다.

{% alert warning %}
**미리보기**에서 메시지의 보기가 사용자 기기에서 실제 렌더링되는 것과 동일하지 않을 수 있습니다. 미디어, 카피, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하기 위해 항상 기기에 테스트 메시지를 보내는 것이 좋습니다.
{% endalert %}

### 인앱 메시지 생성 미리보기

메시지가 무작위 사용자, 특정 사용자 또는 커스텀 사용자에게 어떻게 보일지 미리 볼 수 있습니다. 후자의 두 가지 기능은 메시지에 개인화 또는 여러 언어가 포함된 경우 특히 유용합니다. 또한 모바일 기기 또는 태블릿용 메시지를 미리 보고 사용자가 어떤 경험을 하게 될지 더 잘 파악할 수 있습니다.

![인앱 메시지를 작성할 때 작성 탭에서 메시지가 어떻게 표시될지 미리 볼 수 있습니다. A user is not selected, so the Liquid added in the body section displays as is.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze는 3세대 인앱 메시지를 사용할 수 있습니다. 지원하는 세대에 따라 메시지를 전송할 기기를 세밀하게 조정할 수 있습니다.

![Switching between generations when previewing an in-app message.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## 테스트

{% alert warning %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 기기에서 푸시를 사용하도록 설정해야 합니다. <br><br>예를 들어 테스트 메시지가 표시되기 전에 알림을 탭하려면 iOS 기기에서 푸시를 사용하도록 설정해야 합니다.
{% endalert %}

### 사용자로서 메시지 미리보기

**테스트** 탭에서 사용자가 된 것처럼 메시지를 미리 볼 수도 있습니다. 특정 사용자, 무작위 사용자 또는 커스텀 사용자를 선택할 수 있습니다.

![인앱 메시지 작성 시 테스트 탭을 클릭합니다. "Preview message as user" is set to "Custom User" with available profile fields appearing as configurable options.]({% image_buster /assets/img/iam-user-preview.png %})

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? 리퀴드가 정보를 반환하지 않는 경우의 [기본 속성 값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) 고려했나요?
- 카피가 명확하고 간결하며 정확한가요?
- 버튼이 사용자가 어디로 이동해야 하는지 안내하나요?

## Accessibility scanner

To support accessibility best practices, Braze automatically scans the content of in-app messages created using the traditional HTML editor against accessibility standards. This scanner helps identify content that may not meet Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) standards. WCAG is a set of internationally recognized technical standards developed by the World Wide Web Consortium (W3C) to make web content more accessible to people with disabilities.

![Accessibility scan results]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
The in-app message accessibility scanner only runs on messages built with custom HTML.
{% endalert %}

### How it works

The scanner runs automatically on custom HTML messages and evaluates your entire HTML message against the full [WCAG 2.1 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). For each flagged issue, it shows:

- The specific HTML element involved
- A description of the accessibility issue
- A link to additional context or remediation guidance

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}





