---
nav_title: 테스트
article_title: 인앱 메시지 테스트하기
page_order: 4.5
description: "이 참고 문서에서는 인앱 메시지 테스트의 가치와 테스트 방법, 전송 전 고려해야 할 사항 체크리스트에 대해 설명합니다."
channel:
  - in-app messages
  
---

# 인앱 메시지 테스트

> 캠페인을 보내기 전에 항상 인앱 메시지를 테스트하는 것이 매우 중요합니다. 미리보기 및 테스트 기능은 인앱 메시지를 살펴볼 수 있는 두 가지 방법을 제공합니다. 메시지를 미리 보고 작성할 때 시각화할 수 있으며, 본인 또는 특정 사용자의 기기로 테스트 메시지를 보낼 수도 있습니다. 두 가지를 모두 활용하는 것이 좋습니다.

## 미리 보기

인앱 메시지를 작성하면서 미리 볼 수 있습니다. 이를 통해 사용자의 관점에서 최종 메시징이 어떻게 보일지 시각화할 수 있습니다.

{% alert warning %}
**미리보기에서** 메시징의 보기가 사용자 기기의 실제 렌더링과 동일하지 않을 수 있습니다. 항상 기기에 테스트 메시지를 전송하여 미디어, 카피, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하는 것이 좋습니다.
{% endalert %}

### 인앱 메시지 생성 미리보기

메시징이 무작위 사용자, 특정 사용자 또는 커스텀 사용자에게 어떻게 보일지 미리 볼 수 있습니다. 메시징에 개인화 또는 여러 언어가 포함된 경우 후자의 두 가지 기능이 특히 유용합니다. 또한 모바일 기기 또는 태블릿용 메시지를 미리 보고 사용자가 어떤 경험을 하게 될지 더 잘 파악할 수 있습니다.

인앱 메시지를 구축할 때 작성 탭을 클릭하면 메시지가 어떻게 보일지 미리 볼 수 있습니다. 사용자가 선택되지 않았으므로 본문 섹션에 추가된 Liquid는 is.]({%image_buster /assets/img/in-app-message-preview.png %})로 표시됩니다.

Braze는 3세대 인앱 메시지를 지원합니다. 지원하는 세대에 따라 메시지를 전송할 기기를 세밀하게 조정할 수 있습니다.

\![인앱 메시지를 미리 볼 때 세대 간 전환.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## 테스트

{% alert warning %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 기기에서 푸시를 인에이블먼트해야 합니다. <br><br>예를 들어 테스트 메시지가 표시되기 전에 알림을 탭하려면 iOS 기기에서 푸시 알림을 인에이블해야 합니다.
{% endalert %}

### 사용자로서 메시지 미리보기

**테스트** 탭에서 사용자가 된 것처럼 메시지를 미리 볼 수도 있습니다. 특정 사용자, 임의의 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다.

\![인앱 메시지 구축 시 테스트 탭. "사용자로 메시지 미리보기"가 "커스텀 사용자"로 설정되어 있으며 사용 가능한 프로필 필드가 구성 가능한 옵션으로 표시됩니다.]({% image_buster /assets/img/iam-user-preview.png %})

{% alert important %}
테스트 전송으로 인해 각 수신자에게 두 개 이상의 인앱 메시지가 전송될 수 있습니다.
{% endalert %}

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우의 [기본 속성 값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) 고려하셨나요?
- 카피가 명확하고 간결하며 정확한가요?
- 버튼이 사용자가 어디로 이동해야 하는지 안내하나요?

## 접근성 스캐너

접근성 모범 사례를 지원하기 위해 Braze는 기존 HTML 편집기를 사용하여 만든 인앱 메시지 콘텐츠를 접근성 표준에 따라 자동으로 검사합니다. 이 스캐너는[WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)(웹 콘텐츠 접근성 지침) 표준을 충족하지 않을 수 있는 콘텐츠를 식별하는 데 도움이 됩니다. WCAG는 장애인의 웹 콘텐츠 접근성을 높이기 위해 월드와이드웹 컨소시엄(W3C)에서 개발한 국제적으로 인정된 기술 표준입니다.

\![접근성 검사 결과]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
인앱 메시지 접근성 스캐너는 커스텀 HTML로 구축된 메시지에서만 실행됩니다.
{% endalert %}

### 작동 방식

스캐너는 커스텀 HTML 메시징에 대해 자동으로 실행되며 전체 [WCAG 2.1 AA 규칙 세트에](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) 대해 전체 HTML 메시지를 평가합니다. 플래그가 지정된 각 이슈에 대해 표시됩니다:

- 관련된 특정 HTML 요소
- 접근성 문제에 대한 설명
- 추가 컨텍스트 또는 수정 지침에 대한 링크

### 자동화 접근성 테스트 이해하기

{% multi_lang_include accessibility/automated_testing.md %}





