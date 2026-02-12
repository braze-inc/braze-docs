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

> 받은편지함 비전을 사용하면 다양한 이메일 클라이언트와 모바일 기기의 관점에서 이메일을 볼 수 있습니다. 예를 들어 다크 모드와 라이트 모드의 차이를 테스트하여 이메일이 의도한 대로 렌더링되는지 확인할 수 있습니다.

{% alert important %}
이메일 콘텐츠가 사용자 프로필 데이터와 같은 템플릿 정보에 의존하는 경우 받은편지함 비전이 작동하지 않을 수 있습니다. 이 기능을 위해 이메일을 보낼 때 Braze는 빈 사용자를 템플릿으로 설정합니다.<br><br>이메일 메시지에 있는 모든 Liquid에 기본값을 추가하세요. 기본값이 없으면 오탐이 발생하거나 테스트가 실패할 수 있습니다.
{% endalert %}

## 고려 사항

일반적으로 이메일 콘텐츠가 고객 프로필 정보와 같은 템플릿 정보에 의존하는 경우 받은편지함 비전에서 이메일이 작동하지 않습니다. 이 기능을 사용하여 이메일을 보낼 때 Braze가 빈 사용자를 템플릿으로 만들기 때문입니다.

받은편지함 비전을 실행하기 전에 기본값 또는 이메일 메시지의 Liquid에 값을 추가하여 이 문제를 해결할 수 있습니다. 받은편지함 비전에서 테스트를 완료하면 원본 이메일 메시지가 나타납니다. 값을 제공하지 않으면 테스트에서 미리 보기를 성공적으로 렌더링하지 못할 수 있습니다.

회사에서 받은편지함 비전으로 미리 볼 수 있는 이메일 수에 제한이 있습니다. 받은편지함 비전의 **이메일 미리 보기** 탭에서 이를 모니터링할 수 있습니다.

미리보기를 보려면 제목란과 유효한 발신 도메인을 포함하세요. 데스크톱과 모바일 렌더링의 차이점을 염두에 두어야 합니다. 미리 보기를 사용하여 이메일이 의도한 대로 표시되는지 확인합니다.

받은편지함에서 이메일 메시지를 테스트하려면:

1. 끌어서 놓기 편집기 또는 HTML 이메일 편집기로 이동합니다.
2. 편집기에서 **미리보기 & 테스트를** 선택합니다.
3. **받은편지함 비전** 선택.
4. **실행 받은편지함 비전**. 이 작업에는 최대 10분이 소요됩니다.
5. 다음으로, 미리보기를 더 자세히 보기 위해 타일을 선택하세요. 이 미리보기는 다음 섹션으로 그룹화됩니다: **웹 클라이언트**, **애플리케이션 클라이언트** 및 **모바일 클라이언트**.

![미리 볼 이메일 클라이언트를 선택하는 옵션입니다.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. **실행 받은편지함 비전**. 이 작업은 완료하는 데 2분에서 10분 정도 걸릴 수 있습니다.

{% alert note %}
받은편지함 비전은 [중단 로직이]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) 포함된 이메일 메시지를 지원하지 않습니다. 이러한 이메일은 정적 콘텐츠로 렌더링되기 때문입니다.
{% endalert %}

### 사용자로 미리보기

무작위 사용자로 미리 볼 때 받은편지함 비전은 사용자별 설정이나 속성(예: 이름 또는 환경설정)을 저장하지 않습니다. 커스텀 사용자를 선택하면 받은편지함 비전 미리보기는 특정 사용자 데이터를 사용하기 때문에 다른 미리보기와 다를 수 있습니다.

## 코드 분석

코드 분석은 잠재적인 HTML 문제를 강조하고, 발생 횟수를 표시하며, 지원되지 않는 HTML 요소를 표시합니다.

### 코드 분석 정보 보기

**받은편지함 비전** 탭에서 <i class="fas fa-list"></i> **목록 보기를** 선택하면 이 정보를 확인할 수 있습니다. 목록 보기는 HTML 이메일 템플릿에서만 사용할 수 있습니다. 드래그 앤 드롭 템플릿의 경우 미리 보기를 사용하여 문제를 해결하세요.

![받은편지함 비전 미리 보기의 코드 분석 예시.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Braze는 스크린샷을 찍기 전에 이메일이 도착할 때까지 기다리기 때문에 특정 클라이언트에 대한 코드 분석이 미리보기보다 빠르게 나타날 수 있습니다.
{% endalert %}

## 스팸 테스트

스팸 테스트는 이메일이 스팸 폴더에 도착할지 받은편지함에 도착할지 예측합니다. Braze는 주요 스팸 필터(IronPort, SpamAssassin, Barracuda) 및 주요 ISP 필터(Gmail.com, Outlook.com)에 대한 테스트를 실행합니다.

### 스팸 테스트 결과 보기

스팸 테스트 결과를 확인하려면 다음과 같이 하세요:

1. **받은편지함 비전** 섹션에서 **스팸 테스트** 탭을 선택하세요. **스팸 테스트 결과** 표에는 스팸 필터 이름, 상태 및 유형이 나열됩니다.
2. 이 결과를 검토하고 이메일 캠페인을 조정하세요.
3. 스팸 테스트 결과를 새로 고치려면 **테스트 다시 실행**을 선택하세요.

## Accessibility testing

접근성 테스트는 이메일의 잠재적인 접근성 문제를 강조하고 어떤 요소가 표준을 충족하지 못하는지 보여줍니다. Braze는 웹 콘텐츠의 접근성을 높이기 위해 W3C에서 개발한 국제적으로 인정된 표준인 웹 콘텐츠 접근성 지침[(WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)에 따라 콘텐츠를 분석합니다.

### 작동 방식

받은편지함 비전을 실행하면 Braze는 [WCAG 2.2 AA 규칙 세트에서](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) 일반적인 접근성 문제(예: 대체 텍스트 누락, 색상 대비 부족, 부적절한 제목 구조)를 자동으로 확인하고 심각도를 분류하여 수정 우선순위를 정할 수 있도록 도와줍니다. 

{% alert important %}
접근성 테스트는 [유럽 접근성 법과](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) 같은 규정 또는 법률에 대한 고객의 준수 노력을 지원하기 위해 사용될 수 있지만, 고객은 접근성 테스트의 사용이 고객의 준수 의무를 충족하는지 여부와 관련하여 Braze가 어떠한 진술이나 보증을 하지 않으며 이와 관련한 모든 책임을 부인함을 인정합니다.
{% endalert %}

### Viewing accessibility testing results

접근성 테스트는 **접근성 테스트** 탭에서 각 규칙에 대해 합격, 불합격 또는 검토 필요 등의 결과를 생성합니다. Braze는 WCAG의 네 가지 원칙인 POUR(인식 가능, 조작 가능, 이해 가능, 강건성)를 사용하여 각 규칙을 분류합니다.

#### POUR categories

받은편지함 비전은 네 가지 기본 [POUR 원칙에](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) 따라 문제를 분류합니다: Perceivable, Operable, Understandable, and Robust.

| Principle | Definition |
| --- | --- |
| Perceivable | Information and user interface components must be presentable to users in ways they can perceive.<br><br>Users must be able to perceive the information being presented (it can't be invisible to all of their senses). |
| Operable | User interface components and navigation must be operable.<br><br>Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). |
| Understandable | Information and the operation of the user interface must be understandable.<br><br>Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). |
| Robust | Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.<br><br>Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Severity levels

받은편지함 비전은 접근성 문제를 심각도별로 분류하여 해결 우선순위를 정할 수 있도록 도와줍니다.

| 상태 | Definition |
| --- | --- |
| Critical | Issues that can block access to content or functionality for users with disabilities. These are the most severe and should be prioritized for fixing. |
| Serious | Issues that can cause significant barriers but may not completely block access. These should be addressed promptly. |
| Moderate | Issues that may cause some difficulty for users with disabilities, but are less likely to block access entirely. |
| Minor | Issues that have a relatively low impact on accessibility and may cause only minor inconvenience. |
| Needs review | Unable to detect if there might be an issue or not. This can occur when we are unable to determine the contrast ratio as the text is placed on a background image. 자동으로 결정할 수 없으므로 수동으로 검토해야 합니다. |
| Passed | Passed WCAG A, AA, or accessibility best practice. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
드래그 앤 드롭 편집기는 설명서 `<title>` 요소 설정을 지원하지 않으므로 접근성 스캐너는 항상 이 검사에 실패합니다.<br><br>이 제한 사항은 향후 개선을 위해 추적하고 있습니다. 워크플로 또는 사용자에 영향을 미치는 경우, 영향력 있는 수정의 우선순위를 정할 수 있도록 [피드백을 공유해]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) 주세요.
{% endalert %}

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}

## Best practices

### 이메일 가입자 목록 검토하기

[이메일 인사이트 대시보드를]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) 참조하여 가입자가 가장 많이 참여하는 기기 유형과 제공업체를 파악하세요. 브라우저, 기기 모델 등 더 세분화된 정보가 필요한 경우 [커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터 또는 [쿼리 작성기를]({{site.baseurl}}/user_guide/analytics/query_builder) 활용하여 사용자의 최근 이메일 참여에 대한 세부 정보를 검색할 수 있습니다.

그렇지 않으면 Braze의 기본값은 일반 업계 및 전문가 데이터를 기반으로 한 상위 20개 미리보기로 설정되며, 이는 가입자가 이메일에 참여하는 대부분의 위치를 포괄합니다. 데이터 분석이 다른 인기 있는 미리 보기를 가리키는 경우, 받은편지함 비전을 실행할 때마다 미리 보기의 기본값 세트를 정의할 수 있습니다.

### 의미 있는 미리 보기 및 영향을 받는 미리 보기 선택

비즈니스가 주로 미국에 기반을 둔 경우 GMX.de 과 같은 해외 미리보기와 같은 특정 미리보기가 있을 수 있으며, 이 미리보기는 소수의 사용자만 사용할 수 있습니다. 가입자에게 큰 영향을 미치는 받은편지함의 우선순위를 정하여 최적화하고, 영향력이 큰 편지함에 대해서는 미리 보기를 예약하는 것이 좋습니다.

특정 미리 보기에 영향을 주는 수정 작업을 할 때는 영향을 받는 미리보기만 선택하여 사용하지 않는 미리보기가 소비되는 것을 방지하세요.

### 최종 이메일 버전에서 받은편지함 비전을 실행합니다.

이메일 메시지가 프로덕션 준비가 완료되었거나 거의 완료되었을 때 받은편지함 비전을 실행하는 것이 좋습니다. 이렇게 하면 이메일이 최종 완성되어 사용자에게 전송될 준비가 되기 전에 여러 번의 반복을 거치기 때문에 생성되는 미리보기의 수를 줄일 수 있습니다.

한 번 편집하거나 변경할 때마다 받은편지함 비전을 실행하면 미리보기를 빠르게 사용할 수 있습니다. 먼저 이메일을 모두 변경한 다음 받은편지함 비전을 실행하여 모든 변경 사항이 여러 환경의 이메일 렌더링에 어떤 영향을 미치는지 미리 보는 것이 좋습니다.

Braze는 실제 이메일 클라이언트를 통해 테스트를 실행하고 렌더링이 정확한지 확인하기 위해 노력합니다. 클라이언트에서 지속적으로 문제가 발생하면 [지원 티켓을]({{site.baseurl}}/braze_support/) 만드세요.
