---
nav_title: 사용자 선택 리마인더 메시징
article_title: 사용자 선택 리마인더 메시징
page_order: 5
page_type: reference
description: "이 참조 문서에서는 Braze 랜딩 페이지, 커스텀 속성, 캠페인을 사용하여 사용자가 다가오는 이벤트나 약속에 대한 개인화된 리마인더 메시지에 가입할 수 있도록 하는 방법을 안내합니다."
---

# 사용자 선택 리마인더 메시징

> Braze [랜딩 페이지]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/), 커스텀 속성, 캠페인을 사용하여 사용자가 다가오는 이벤트나 약속에 대한 리마인더 메시지를 언제 받을지 선택할 수 있도록 합니다. 이 접근 방식을 사용하면 기술 지식이 없는 Braze 사용자도 리마인더 가입 페이지의 콘텐츠를 생성하고 편집할 수 있으며, 사용자가 선택한 환경설정은 모든 Braze 기반 메시징에서 세분화, 타겟팅, 개인화를 구동할 수 있습니다.

이 접근 방식을 사용하면 다음을 수행할 수 있습니다:

- 사용자가 다가오는 이벤트를 기준으로 리마인더 메시지 날짜를 직접 선택할 수 있습니다.
- Braze 랜딩 페이지를 사용하여 사용자로부터 직접 환경설정을 수집하고 고객 프로필에 기록합니다—별도의 백엔드가 필요하지 않습니다.
- 사용자가 선택한 날짜에 메시지를 전송하여 메시징이 관련성 있고 권한 기반으로 유지됩니다.
- 메시지 지연, 후속 리타겟팅, A/B 테스트 등 추가 Braze 기능으로 사용 사례를 확장할 수 있습니다.

## 필수 조건

이 가이드를 완료하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| 랜딩 페이지 액세스 | Braze에서 [랜딩 페이지]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)를 생성할 수 있는 액세스 및 권한. |
| HTML 및 JavaScript 지식 | 랜딩 페이지를 커스터마이즈하기 위한 HTML 및 JavaScript에 대한 기본적인 이해. [옵션 B](#option-b-personal-dates-custom-code-block)에만 필요합니다. |
| Liquid 지식 | 개인화된 변수를 템플릿화하기 위한 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)에 대한 기본적인 이해. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: 랜딩 페이지를 생성하고 메시지에서 링크하기

먼저 [Braze 랜딩 페이지를 생성]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)합니다. 그런 다음 사용자를 랜딩 페이지로 연결하는 메시지(예: 이메일)를 생성합니다.

{% raw %}
랜딩 페이지 활동을 수신자의 고객 프로필에 자동으로 연결하려면 Braze 메시지에서 페이지로 링크할 때 `{% landing_page_url %}` Liquid 태그를 사용합니다. 예를 들어:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

사용자가 이 링크를 클릭하면 Braze가 자동으로 사용자를 식별하므로, 제출한 환경설정이 기존 프로필에 기록됩니다—수동 URL 파라미터가 필요하지 않습니다. 전체 안내는 [양식을 통한 사용자 추적]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/)을 참조하세요.

## 2단계: 랜딩 페이지에서 환경설정 수집하기

사용자 환경설정을 수집하는 방법은 공유 날짜를 수집하는지 개인 날짜를 수집하는지에 따라 달라집니다. 사용 사례에 맞는 옵션을 선택하세요.

### 옵션 A: 공유 날짜 (드래그 앤 드롭 양식 블록)

많은 사용자가 동일한 날짜를 공유하는 이벤트(예: 공휴일 또는 스포츠 이벤트)의 경우, 드래그 앤 드롭 에디터의 내장 [**체크박스** 양식 블록]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)을 사용하여 환경설정을 수집합니다. 각 체크박스는 양식이 제출될 때 사용자 프로필에 부울 커스텀 속성(`true` 또는 `false`)을 기본적으로 설정합니다—커스텀 코드가 필요하지 않습니다.

예를 들어, 커스텀 속성 `super_bowl_2026_reminder`에 매핑되는 "슈퍼볼 2026 리마인더"라는 레이블의 체크박스를 추가합니다. 사용자가 체크박스를 선택하고 양식을 제출하면 Braze가 다음과 같이 설정합니다:

```
super_bowl_2026_reminder = true
```

이러한 부울 속성은 [세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/)에서 직접 사용하여 타겟 오디언스를 구축할 수 있습니다.

### 옵션 B: 개인 날짜 (커스텀 코드 블록)

각 사용자에게 고유한 날짜(예: 생일 또는 기념일)의 경우, 랜딩 페이지에서 [**커스텀 코드** 블록]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks)을 사용하여 날짜를 캡처하고 `lpBridge` API를 사용하여 Braze에 기록합니다. 이 접근 방식은 날짜 입력(또는 선택기)을 제공하며, 드래그 앤 드롭 양식 블록이 지원하지 않는 [중첩 고객 속성 오브젝트 배열]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/)에 환경설정을 저장할 수 있습니다.

사용자가 {% raw %}`{% landing_page_url %}`{% endraw %} Liquid 태그를 통해 도착하면 Braze가 이미 사용자를 알고 있으므로, 스크립트는 다음만 수행하면 됩니다:

1. 양식 제출 버튼 클릭을 감지합니다.
2. 커스텀 입력에서 날짜 값을 읽습니다.
3. `lpBridge` API를 사용하여 중첩 고객 속성을 설정하고 데이터를 Braze로 플러시합니다.

중첩 고객 속성 오브젝트 배열을 사용하여 이러한 환경설정을 저장합니다. 이 구조를 사용하면 사용자당 여러 리마인더를 저장하고 나중에 `next_reminder_name` 또는 `last_reminder_date`와 같은 파생 필드를 추가할 수 있습니다.

#### 예제 스크립트

다음 예제 스크립트는 기본 버튼 동작을 비활성화하고 버튼 클릭 시 커스텀 메서드를 실행합니다. 요소 ID와 속성 값을 자신의 것으로 교체하세요.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

랜딩 페이지 구성요소의 요소 ID를 찾으려면 페이지를 미리보기하고 마우스 오른쪽 버튼을 클릭한 다음 브라우저에서 **검사**를 선택합니다. HTML에서 버튼 및 메시지 구성요소의 ID를 찾습니다.

## 3단계: 리마인더 메시지 설정 및 트리거하기

랜딩 페이지를 통해 커스텀 속성을 수집한 후, 다가오는 이벤트에 대해 사용자에게 메시지를 보내는 캠페인을 생성합니다.

### 옵션 A: 공유 날짜 {#step-3-option-a-shared-dates}

부울 커스텀 속성을 사용한 경우([2단계](#option-a-shared-dates-dnd-form-blocks)의 옵션 A), 해당 속성을 세그먼트 필터로 사용하여 리마인더 메시지의 오디언스를 구축합니다. 그런 다음 이벤트 전에 스케줄된 새 캠페인을 생성하여 선택한 콘텐츠로 이 그룹을 타겟팅합니다.

### 옵션 B: 개인 날짜 {#step-3-option-b-personal-dates}

중첩 고객 속성을 사용한 경우([2단계](#option-b-personal-dates-custom-code-block)의 옵션 B), **중첩 고객 속성** 오디언스 필터를 사용하여 특정 기간 내에 리마인더 날짜가 있는 모든 사용자를 선택합니다—예를 들어, 지금부터 이틀 후.

지속적으로 리마인더를 보내려면 매일 반복되는 캠페인을 설정하여 매일 해당 기간 내에 다가오는 리마인더가 있는 사용자가 메시지를 받도록 합니다.

## 4단계: 통합 확인하기

설정을 완료한 후 통합을 확인합니다:

1. 랜딩 페이지 링크를 자신에게 보내고 양식을 작성합니다.
2. Braze 대시보드에서 고객 프로필로 이동하여 커스텀 속성이 표시되는지 확인합니다.
3. 프로필에 테스트 리마인더 메시지를 보내고 개인화된 세부 정보가 올바르게 렌더링되는지 확인합니다.
4. 캠페인을 시작할 때 결과를 면밀히 모니터링합니다.

## 고려 사항

- 날짜 기반 커스텀 속성을 사용하여 메시지를 보내는 방법에 대한 자세한 예제는 [REST API 메시징 가이드]({{site.baseurl}}/developer_guide/rest_api/messaging/)의 이메일 사용 사례를 참조하세요.
- 랜딩 페이지를 복제하거나 필드를 교체하면 구성요소 ID가 변경됩니다. 새 ID를 반영하도록 커스텀 코드 블록을 업데이트하세요.
- 중첩 고객 속성은 오브젝트 배열의 각 키에 대해 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)를 소비합니다. 커스텀 속성 오브젝트를 null로 업데이트하는 것도 데이터 포인트를 소비합니다.
- 이 가이드에 제시된 코드는 설명을 위한 예제입니다. 프로덕션에 배포하기 전에 환경 내에서 모든 코드와 구성요소를 철저히 테스트하세요.