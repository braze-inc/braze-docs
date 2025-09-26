---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "이 페이지는 마케터가 다양한 이메일 클라이언트와 모바일 장치의 관점에서 이메일을 볼 수 있도록 하는 기능인 받은편지함 비전을 설정하는 방법을 다룹니다."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> 받은편지함 비전을 사용하면 다양한 이메일 클라이언트 및 모바일 기기의 관점에서 이메일을 볼 수 있습니다. 예를 들어, Inbox Vision을 사용하여 어두운 모드와 밝은 모드 간의 차이를 테스트하여 이메일이 정확하게 설정되었는지 확인할 수 있습니다.

{% alert important %}
일반적으로, 귀하의 이메일은 사용자 프로필 정보와 같은 템플릿 정보를 기반으로 하는 경우 Inbox Vision과 함께 작동하지 않습니다. 이 기능을 사용하여 이메일을 보낼 때 Braze은 빈 사용자로 템플릿을 작성하기 때문입니다.<br><br>Make sure you've added default values to any Liquid in your email message. If no default values are provided, you may receive a false positive or the test may fail to run.
{% endalert %}

## Inbox Vision에서 이메일 테스트

이러한 미리 보기를 보려면 이메일에 제목란과 유효한 발신 도메인이 포함되어야 합니다. 이메일이 데스크톱과 모바일 기기에서 어떻게 다르게 렌더링되는지 염두에 두세요. 이러한 미리 보기를 보면서 콘텐츠를 검토하고 이메일이 의도한 대로 표시되는지 확인할 수 있습니다.

받은편지함 비전에서 이메일 메시지를 테스트하려면 다음과 같이 하세요.

1. 끌어서 놓기 편집기 또는 HTML 이메일 편집기로 이동합니다.
2. 편집기에서 **미리보기 및 테스트**를 선택하십시오.
3. **받은편지함 비전** 선택.
4. **실행 받은편지함 비전**. 이 작업은 완료하는 데 2분에서 10분 정도 걸릴 수 있습니다.
5. 다음으로, 미리보기를 더 자세히 보기 위해 타일을 선택하세요. 이 미리보기는 다음 섹션으로 그룹화됩니다: **웹 클라이언트**, **애플리케이션 클라이언트** 및 **모바일 클라이언트**.

![Overview of Inbox Vision for the HTML editor.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. 템플릿에 필요한 경우 변경하십시오.
7\. **테스트를 다시 실행**하여 업데이트된 미리보기를 확인하십시오.

{% alert note %}
Inbox Vision isn't supported if your email message includes [abort logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) as these emails are rendered as static content.
{% endalert %}

### 사용자로 미리보기

무작위 사용자로 이메일을 미리 보기할 때, 사용자와 관련된 특정 설정이나 속성(예: 이름이나 선호도)은 현재 또는 미래의 미리 보기를 위해 저장되지 않습니다. When you select a custom user, the preview shown in Inbox Vision may differ from the message preview elsewhere since this option uses specific user data to create the preview

## 코드 분석

코드 분석은 Braze가 HTML에 존재할 수 있는 문제를 강조하여 각 문제의 발생 횟수를 표시하고 어떤 HTML 요소가 지원되지 않는지에 대한 인사이트를 제공하는 방식입니다.

### 코드 분석 정보 보기

이 정보는 **Inbox Vision** 탭에서 <i class="fas fa-list"></i> **목록 보기**를 선택하면 확인할 수 있습니다. 이 목록 보기는 HTML 이메일 템플릿에서만 사용할 수 있습니다. 끌어서 놓기 이메일 템플릿을 사용하는 경우에는 미리 보기를 확인하여 가능한 문제를 해결하세요.

![Example code analysis on the Inbox Vision preview.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
특정 이메일 클라이언트의 미리보기보다 코드 분석이 더 빨리 표시되는 경우가 있습니다. 이는 Braze가 이메일이 받은 편지함에 도착할 때까지 기다렸다가 스크린샷을 찍기 때문입니다.
{% endalert %}

## 스팸 테스트

스팸 테스트는 이메일이 스팸 폴더에 도착할지 고객의 받은 편지함에 도착할지 예측합니다. 스팸 테스트는 Gmail.com 및 Outlook.com과 같은 주요 인터넷 서비스 제공업체(ISP) 필터뿐만 아니라 IronPort, SpamAssassin, Barracuda 와 같은 주요 스팸 필터에서 실행됩니다 .

### 스팸 테스트 결과 보기

스팸 테스트 결과를 확인하려면 다음을 수행하십시오:

1. **받은편지함 비전** 섹션에서 **스팸 테스트** 탭을 선택하세요. **스팸 테스트 결과** 표에는 스팸 필터 이름, 상태 및 유형이 나열됩니다.

![세 개의 열이 있는 스팸 테스트 결과 표입니다: 이름, 상태 및 유형. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. 이 결과를 검토하고 이메일 캠페인에 대한 조정을 합니다.
3\. 스팸 테스트 결과를 새로 고치려면 **테스트 다시 실행**을 선택하세요.

## Accessibility testing

Accessibility testing in Inbox Vision highlights accessibility issues that may exist with your email to provide insight into which elements are not meeting accessibility standards. It analyzes your email content against some Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG is a set of internationally recognized technical standards developed by the World Wide Web Consortium (W3C) to make web content more accessible to people with disabilities. 

### How it works

When you run an Inbox Vision test, the tool automatically checks for common email accessibility issues in the [WCAG 2.2 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), such as missing alt text, insufficient color contrast, and improper heading structure, then categorizes the severity of each issue to help you prioritize fixes. 

{% alert important %}
Accessibility Testing may be used to support Customer's compliance efforts of regulations or laws such as the [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers), however Customer acknowledges that Braze makes no representations or warranties with respect to whether or not use of Accessibility Testing satisfies Customer's compliance obligations, and disclaims all liability in relation thereto.
{% endalert %}

### Viewing accessibility testing results

Accessibility testing will generate results for each rule as passed, failed, or needs review in the **Accessibility Testing** tab. Each rule is categorized using POUR (Perceivable, Operable, Understandable, Robust), which are the four main principles behind WCAG.

#### POUR categories

Issues are categorized under the four foundational [POUR principles](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceivable, Operable, Understandable, and Robust. Each principle addresses a different aspect of accessible design.

| Principle | Definition |
| --- | --- |
| Perceivable | Information and user interface components must be presentable to users in ways they can perceive.<br><br>Users must be able to perceive the information being presented (it can't be invisible to all of their senses). |
| Operable | User interface components and navigation must be operable.<br><br>Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). |
| Understandable | Information and the operation of the user interface must be understandable.<br><br>Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). |
| Robust | Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.<br><br>Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Severity levels

Inbox Vision classifies accessibility issues by severity to help you prioritize remediation efforts.

| Status | Definition |
| --- | --- |
| Critical | Issues that can block access to content or functionality for users with disabilities. These are the most severe and should be prioritized for fixing. |
| Serious | Issues that can cause significant barriers but may not completely block access. These should be addressed promptly. |
| Moderate | Issues that may cause some difficulty for users with disabilities, but are less likely to block access entirely. |
| Minor | Issues that have a relatively low impact on accessibility and may cause only minor inconvenience. |
| Needs review | Unable to detect if there might be an issue or not. This can occur when we are unable to determine the contrast ratio as the text is placed on a background image. This will need to be manually reviewed because it cannot be automatically determined. |
| Passed | Passed WCAG A, AA, or accessibility best practice. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
The email drag-and-drop editor currently does not support setting a document `<title>` element. As a result, the accessibility scanner will always fail this check.<br><br>
We're tracking this limitation for future improvements. If this affects your workflows or your users, [share your feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) so we can prioritize the most impactful fixes.
{% endalert %}

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}

## 테스트 정확도

모든 테스트는 실제 이메일 클라이언트를 통해 실행됩니다. Braze는 모든 렌더링이 가능한 한 정확한지 확인하기 위해 열심히 노력합니다. 이메일 클라이언트에서 지속적으로 문제가 발생하면 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요.
