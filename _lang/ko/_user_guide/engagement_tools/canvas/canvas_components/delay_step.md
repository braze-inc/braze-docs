---
nav_title: 지연 
article_title: 지연 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "이 참조 문서에서는 관련 메시지를 추가하지 않고도 캔버스에 지연을 추가하는 방법에 대해 설명합니다."
tool: Canvas

---

# 지연

> 지연 컴포넌트를 사용하면 캔버스에 독립형 지연을 추가할 수 있습니다. 관련 메시지를 추가하지 않고도 캔버스에 지연을 추가할 수 있습니다. 

지연은 캔버스를 더 깔끔하게 보이게 할 수 있습니다. 이 구성 요소를 사용하여 다른 단계를 정확한 날짜까지, 특정 날짜까지 또는 특정 요일까지 지연시킬 수도 있습니다. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## 지연 만들기

지연을 만들려면 캔버스에 단계를 추가합니다. 사이드바에서 지연 구성 요소를 끌어서 놓거나 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **지연**을 선택합니다.

캔버스 여정에서 지연을 만들 때 고려해야 할 몇 가지 세부 사항이 있습니다.

- 지연 제한은 30일입니다.
- 지연 구성요소는 다음 단계에 하나만 연결할 수 있습니다.

### Personalized delays

{% alert important %}
Personalized delays and extended delays are in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

Select the **Personalize delay** toggle to set up a personalized delay for your users. You can use this with a [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) to select the context variable to delay by.

다음과 같은 경우 Braze는 해당 단계에서 사용자를 종료합니다:

- 컨텍스트 변수는 어떤 값으로도 반환되지 않습니다.
- 임베디드 커넥티드 콘텐츠 호출이 실패했습니다.
- 컨텍스트 변수 유형이 일치하지 않습니다.

Let's say we want to remind our customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, we can select this context variable to delay by. In this case, our Context step would have the following fields:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.][2]

Next, because we want to remind our customers 30 days from now, we'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from our Context step. This means our users will be delayed until the selected Context variable.

![Example of using context variables with a Delay step to delay users based on the "product_reminder_interval".][3]

#### Extended delays

You can now extend Delay steps up to two years. For example, if you're onboarding new users for your app, you can add an extended delay for two months before sending a Message step to nudge the users who haven't started a session.

### 시간 지연 옵션

캔버스에서 다음 메시지가 표시되기 전 지연 유형을 선택할 수 있습니다. 사용자가 지정된 기간이 지날 때까지 지연되도록 설정하거나 특정 날짜 및 시간까지 사용자를 지연시킬 수 있습니다.

{% tabs %}
  {% tab 일정 기간 후 %}

  **기간 후** 옵션을 사용하면 설정된 시간(초, 분, 시간, 일, 주) 또는 특정 시간 동안 사용자를 지연시킬 수 있습니다. 예를 들어 사용자를 4시간 또는 하루 동안 지연시킬 수 있습니다.
  
  '일'과 '달력 일수'를 계산하는 방법의 차이에 유의하세요.
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  또한 **특정 시간에를** 선택하여 사용자가 캔버스에서 진행할 시기를 지정할 수도 있습니다. 이 옵션은 사용자가 지연 단계를 입력한 시간을 고려합니다. 이 시간이 설정에 구성된 시간을 초과하는 경우 지연 시간에 시간이 더 추가됩니다. 예를 들어 오늘이 12월 11일이고 지연 단계가 1주일 **후** 오전 8시(UTC)로 설정되어 있다고 가정해 보겠습니다. 사용자가 12월 4일에 지연 단계에 진입하는 경우, 원래 오전 8시(한국 시간 기준) 이전에 지연 단계에 진입했다면 오늘 지연 단계에서 해제되어 여정을 계속할 수 있습니다. 이 시간 이후에 지연 단계에 진입하면 사용자는 다음 날(이 시간의 다음 발생)까지 지연됩니다. 

  {% endtab %}
  {% tab 특정 날짜까지 %}

  **특정 날짜까지** 옵션을 사용하면 특정 날짜 및 시간까지 사용자를 단계에 유지시킬 수 있습니다.

  {% alert important %}
  사용자가 지연 단계로 진행할 때 선택한 날짜와 시간이 이미 지난 경우, 사용자는 캔버스를 종료합니다. 캔버스 시작과 '정확한 날짜까지 기다리기' 단계에서 선택한 날짜 사이에는 최대 31일이 지나야 합니다.
  {% endalert %}
  {% endtab %}
  {% tab 특정 요일까지 %}

  **특정 요일까지** 옵션을 사용하면 특정 요일, 특정 시간까지 사용자를 단계에 머물게 할 수 있습니다. 예를 들어 목요일이 회사 표준 시간대인 오후 4시에 도착할 때까지 사용자를 다음 시간으로 연기할 수 있습니다. 

  이를 성공적으로 구성하려면 사용자가 선택한 요일(예: 목요일)에 캔버스에 들어왔지만 지정된 시간이 지난 후에 캔버스에 들어갈 경우 어떤 일이 발생할지 선택해야 합니다. 사용자를 당일에 승급하거나 다음 주까지 보류하도록 선택할 수 있습니다.
  {% endtab %}
{% endtabs %}

## 지연 단계 사용

6월 10일이라고 가정해 보겠습니다. 6월 11일에 사용자가 캔버스에 들어가서 예정된 프로모션에 대한 메시지를 받기를 원합니다. 그런 다음 현지 시간으로 6월 17일 오후 3시까지 캔버스에서 사용자를 붙잡아 두려고 합니다. 6월 17일 오후 3시(현지 시간)에 사용자에게 프로모션에 대한 알림 메시지를 보내려고 합니다.

캔버스 단계의 순서는 다음과 같습니다:

1. 먼저 6월 11일에 사용자가 캔버스에 입장한 직후에 보내는 메시지 단계를 추가합니다.
2. 6월 17일 오후 1시(현지 시간)까지 사용자를 보류하는 지연 단계를 만듭니다.
3. 지연 단계를 즉시 메시지를 전송하는 다른 메시지 단계에 연결합니다.

### 캔버스 끝에 있는 지연 구성요소 {#delay-as-last-step}

캔버스에 지연 구성 요소를 추가했지만 지연 구성 요소 뒤에 더 이상 단계가 없는 경우, 마지막 단계에 도달한 사용자는 자동으로 캔버스 밖으로 진행됩니다. 지연 단계의 시간이 아직 도달하지 않은 경우에도 마찬가지입니다. 즉, 이미 지연 단계에 도달한 사용자의 경우 지연 단계 이후에 추가하는 메시지를 받지 못합니다. 그러나 사용자가 지연 단계에 도달하지 않았는데 메시지가 추가되면 해당 메시지를 받게 됩니다.

## 지연 분석

지연은 활성 캔버스 또는 이전에 활성 캔버스의 분석 보기에서 세 가지 통계를 사용할 수 있습니다.

| 측정기준 | 설명 |
|---|---|
| `Entered` | 단계를 입력한 횟수를 반영합니다. 캔버스에 재자격이 있는 사용자가 지연 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| `Proceeded to Next Step` | 캔버스에서 다음 단계로 진행된 항목 수를 반영합니다. |
| `Exited Canvas` | 캔버스를 종료하고 다음 단계로 진행하지 않은 항목의 수를 반영합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이러한 분석에 대한 시계열은 확장된 구성요소 보기에서 사용할 수 있습니다.

[1]: {% image_buster /assets/img/canvas_delay.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}
