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

> 받은편지함 비전은 다양한 이메일 클라이언트와 모바일 장치의 관점에서 이메일을 볼 수 있게 해줍니다. 예를 들어, 다크 모드와 라이트 모드의 차이를 테스트하여 이메일이 의도한 대로 렌더링되는지 확인할 수 있습니다.

{% alert important %}
받은편지함 비전은 이메일 내용이 고객 프로필 데이터와 같은 템플릿 정보를 의존하는 경우 작동하지 않을 수 있습니다. Braze는 이 기능을 위해 이메일을 보낼 때 빈 사용자를 템플릿화합니다.<br><br>이메일 메시지의 Liquid에 기본값을 추가하세요. 기본값이 없으면 잘못된 긍정 결과를 받거나 테스트가 실패할 수 있습니다.
{% endalert %}

## 고려 사항

일반적으로 이메일 내용이 템플릿 정보, 즉 고객 프로필 정보에 의존하는 경우 이메일은 받은편지함 비전과 함께 작동하지 않습니다. 이는 Braze가 이 기능을 사용하여 이메일을 보낼 때 빈 사용자를 템플릿화하기 때문입니다.

받은편지함 비전을 실행하기 전에 이메일 메시지의 Liquid에 기본값이나 값을 추가하여 이 문제를 해결할 수 있습니다. 받은편지함 비전에서 테스트를 마치면 원래 이메일 메시지가 나타납니다. 값이 제공되지 않으면 미리보기를 성공적으로 렌더링하지 못할 수 있습니다.

귀사의 회사는 받은편지함 비전으로 미리볼 수 있는 이메일 수에 제한이 있습니다. 이것은 받은편지함 비전의 **이메일 미리보기** 탭에서 모니터링할 수 있습니다.

미리보기를 보려면 제목란과 유효한 발신 도메인을 포함하세요. 데스크탑과 모바일 렌더링 차이에 유의하세요. 미리보기를 사용하여 이메일이 의도한 대로 나타나는지 확인하세요.

받은편지함 비전에서 이메일 메시지를 테스트하려면:

1. 끌어서 놓기 편집기 또는 HTML 이메일 편집기로 이동합니다.
2. 편집기에서 **미리보기 & 테스트**를 선택하세요.
3. **받은편지함 비전** 선택.
4. **실행 받은편지함 비전**. 이 작업은 최대 10분이 소요됩니다.
5. 다음으로, 미리보기를 더 자세히 보기 위해 타일을 선택하세요. 이 미리보기는 다음 섹션으로 그룹화됩니다: **웹 클라이언트**, **애플리케이션 클라이언트** 및 **모바일 클라이언트**.

![미리보기를 위해 이메일 클라이언트를 선택하는 옵션.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. **실행 받은편지함 비전**. 이 작업은 완료하는 데 2분에서 10분 정도 걸릴 수 있습니다.

{% alert note %}
Inbox Vision은 [abort logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages)을 포함하는 이메일 메시지를 지원하지 않습니다. 이러한 이메일은 정적 콘텐츠로 렌더링됩니다.
{% endalert %}

### 사용자로 미리보기

무작위 사용자로 미리보기할 때, Inbox Vision은 사용자 특정 설정이나 속성(예: 이름 또는 선호도)을 저장하지 않습니다. 사용자 정의 사용자를 선택하면 Inbox Vision 미리보기가 다른 미리보기와 다를 수 있습니다. 이는 특정 사용자 데이터를 사용하기 때문입니다.

## 코드 분석

코드 분석은 잠재적인 HTML 문제를 강조 표시하고, 발생 횟수를 보여주며, 지원되지 않는 HTML 요소를 나타냅니다.

### 코드 분석 정보 보기

이 정보를 **Inbox Vision** 탭에서 <i class="fas fa-list"></i> **목록 보기**를 선택하여 찾으십시오. 목록 보기는 HTML 이메일 템플릿에만 사용할 수 있습니다. 드래그 앤 드롭 템플릿의 경우, 문제를 해결하기 위해 미리보기를 사용하십시오.

![받은편지함 비전 미리 보기의 코드 분석 예시.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
코드 분석은 특정 클라이언트에 대한 미리보기보다 더 빠르게 나타날 수 있습니다. 이는 Braze가 이메일이 도착할 때까지 스크린샷을 찍지 않기 때문입니다.
{% endalert %}

## 스팸 테스트

스팸 테스트는 이메일이 스팸 폴더나 받은편지함에 도착할지를 예측합니다. Braze는 주요 스팸 필터(IronPort, SpamAssassin, Barracuda)와 주요 ISP 필터(Gmail.com, Outlook.com)를 통해 테스트를 실행합니다.

### 스팸 테스트 결과 보기

스팸 테스트 결과를 확인하려면:

1. **받은편지함 비전** 섹션에서 **스팸 테스트** 탭을 선택하세요. **스팸 테스트 결과** 표에는 스팸 필터 이름, 상태 및 유형이 나열됩니다.
2. 이 결과를 검토하고 이메일 캠페인에 대한 조정을 하십시오.
3. 스팸 테스트 결과를 새로 고치려면 **테스트 다시 실행**을 선택하세요.

## Accessibility testing

접근성 테스트는 이메일의 잠재적인 접근성 문제를 강조 표시하고 어떤 요소가 기준을 충족하지 않는지 보여줍니다. Braze는 콘텐츠를 선택된 웹 콘텐츠 접근성 지침([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/))에 대해 분석합니다. 이는 W3C에서 개발한 국제적으로 인정받는 기준 세트로 웹 콘텐츠를 더 접근 가능하게 만듭니다.

### 작동 방식

Inbox Vision을 실행할 때, Braze는 [WCAG 2.2 AA 규칙 세트](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa)의 일반적인 접근성 문제(예: 누락된 대체 텍스트, 불충분한 색상 대비, 부적절한 제목 구조)를 자동으로 확인하고 심각도를 분류하여 수정 우선 순위를 정하는 데 도움을 줍니다. 

{% alert important %}
접근성 테스트는 고객의 [유럽 접근성 법](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers)과 같은 규정 또는 법률 준수를 지원하는 데 사용될 수 있습니다. 그러나 고객은 Braze가 접근성 테스트 사용이 고객의 준수 의무를 충족하는지 여부에 대해 어떠한 진술이나 보증도 하지 않으며, 이에 대한 모든 책임을 부인함을 인정합니다.
{% endalert %}

### Viewing accessibility testing results

접근성 테스트는 **접근성 테스트** 탭에서 각 규칙에 대해 통과, 실패 또는 검토 필요로 결과를 생성합니다. Braze는 WCAG의 네 가지 원칙인 POUR(인지 가능, 작동 가능, 이해 가능, 견고함)을 사용하여 각 규칙을 분류합니다.

#### POUR categories

Inbox Vision은 네 가지 기본 [POUR 원칙](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility)에 따라 문제를 분류합니다: Perceivable, Operable, Understandable, and Robust.

| Principle | Definition |
| --- | --- |
| Perceivable | Information and user interface components must be presentable to users in ways they can perceive.<br><br>Users must be able to perceive the information being presented (it can't be invisible to all of their senses). |
| Operable | User interface components and navigation must be operable.<br><br>Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). |
| Understandable | Information and the operation of the user interface must be understandable.<br><br>Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). |
| Robust | Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.<br><br>Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Severity levels

Inbox Vision은 심각도에 따라 접근성 문제를 분류하여 수정 우선 순위를 정하는 데 도움을 줍니다.

| 상태 | Definition |
| --- | --- |
| Critical | Issues that can block access to content or functionality for users with disabilities. These are the most severe and should be prioritized for fixing. |
| Serious | Issues that can cause significant barriers but may not completely block access. These should be addressed promptly. |
| Moderate | Issues that may cause some difficulty for users with disabilities, but are less likely to block access entirely. |
| Minor | Issues that have a relatively low impact on accessibility and may cause only minor inconvenience. |
| Needs review | Unable to detect if there might be an issue or not. This can occur when we are unable to determine the contrast ratio as the text is placed on a background image. 수동으로 검토해야 합니다. 자동으로 결정할 수 없습니다. |
| Passed | Passed WCAG A, AA, or accessibility best practice. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
드래그 앤 드롭 편집기는 문서 `<title>` 요소 설정을 지원하지 않으므로 접근성 스캐너는 항상 이 검사를 실패합니다.<br><br>이 제한 사항은 향후 개선 사항으로 추적됩니다. 이것이 귀하의 작업 흐름이나 사용자에게 영향을 미친다면, [피드백을 공유하세요]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) 우리가 영향력 있는 수정을 우선시할 수 있도록.
{% endalert %}

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}

## Best practices

### 이메일 가입자 목록을 검토하세요.

가장 인기 있는 기기 유형과 가입자가 참여하는 제공업체를 확인하기 위해 [이메일 인사이트 대시보드]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard)를 참조하세요. 브라우저, 기기 모델 등과 같은 더 세부적인 정보가 필요하다면, [커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터나 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder)를 활용하여 사용자의 최근 이메일 참여에 대한 이 수준의 세부 정보를 검색할 수 있습니다.

그렇지 않으면, Braze는 일반 산업 및 전문가 데이터를 기반으로 상위 20개 미리보기를 기본값으로 설정하며, 이는 귀하의 가입자가 이메일과 상호작용하는 대부분의 경우를 포함합니다. 데이터 분석이 다른 더 인기 있는 미리보기를 가리킨다면, Inbox Vision을 실행할 때마다 기본 미리보기 세트를 정의할 수 있습니다.

### 의미 있는 미리보기와 영향을 받은 미리보기를 선택하세요.

귀하의 비즈니스가 주로 미국에 기반하고 있다면, GMX.de과 같은 국제 미리보기와 같이 소수의 사용자만 사용하는 특정 미리보기가 있을 수 있습니다. 상당한 가입자 영향을 미치는 받은편지함을 우선시하고 최적화하며, 더 높은 영향력을 미치는 받은편지함을 위해 미리보기를 예약하는 것을 권장합니다.

특정 미리보기에 영향을 미치는 수정을 할 때는 사용하지 않는 미리보기를 소모하지 않도록 영향을 받은 미리보기만 선택해야 합니다.

### 최종 이메일 버전에서 Inbox Vision을 실행하세요.

이메일 메시지가 생산 준비가 되었거나 그에 가까울 때 Inbox Vision을 실행하는 것을 권장합니다. 이렇게 하면 이메일이 최종화되고 사용자에게 전송될 준비가 되기 전에 여러 번의 반복을 거치므로 생성된 미리보기 수를 줄일 수 있습니다.

단일 편집이나 변경을 할 때마다 Inbox Vision을 실행하면 미리보기를 빠르게 소모할 수 있습니다. 먼저 이메일에 필요한 모든 변경을 한 다음, Inbox Vision을 실행하여 모든 변경이 다양한 환경에서 이메일 렌더링에 어떻게 영향을 미칠 수 있는지 미리보기를 권장합니다.

Braze는 실제 이메일 클라이언트를 통해 테스트를 실행하고 렌더링이 정확하도록 작업합니다. 클라이언트에서 지속적으로 문제가 발생하면 [지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.
