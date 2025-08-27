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

지연은 캔버스를 더 깔끔하게 보이게 할 수 있습니다. 이 구성 요소를 사용하여 다른 단계를 정확한 날짜까지, 특정 날짜까지 또는 특정 요일까지 지연시킬 수도 있습니다. <br> ![A Delay step with a 1-day delay as the first step of a Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Creating a delay

지연을 만들려면 캔버스에 단계를 추가합니다. 사이드바에서 지연 구성 요소를 끌어서 놓거나 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **지연**을 선택합니다.

캔버스 여정에서 지연을 만들 때 고려해야 할 몇 가지 세부 사항이 있습니다.

- 지연 제한은 30일입니다.
- 지연 구성요소는 다음 단계에 하나만 연결할 수 있습니다.

### Personalized delays

{% alert important %}
Personalized delays and extended delays are in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

Select the **Personalize delay** toggle to set up a personalized delay for your users. You can use this with a [Context step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) to select the context variable to delay by.

Let's say you want to remind your customers to purchase toothpaste 30 days from now. Using a combination of a Context step and a Delay step, you can select this context variable to delay by. In this case, your Context step would have the following fields:

- **Context variable name:** product_reminder_interval
- **Data type:** Time
- **Value:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![The "product_reminder_interval" and its value.]({% image_buster /assets/img/context_step1.png %})

Next, because you want to remind your customers 30 days from now, you'll select **Until a specific day** as the delay option and select **Personalize delay** to use the information from your Context step. This means your users will be delayed until the selected Context variable.

![Example of using context variables with a Delay step to delay users based on the "product_reminder_interval".]({% image_buster /assets/img/context_step2.png %})

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

#### Considerations

##### Users won't receive past-dated steps or messages

사용자가 지연 단계로 진행할 때 선택한 날짜와 시간이 이미 지난 경우, 사용자는 캔버스를 종료합니다. There can be up to 31 days between the start of the Canvas and the dates chosen for "Wait until Exact Date" steps. 

{% alert important %}
If you're participating in the [Context step early access]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), you can set delays of up to 2 years.
{% endalert %}

For example, users won't receive steps or messages in these scenarios:
- A message is scheduled to send on May 3rd at 9 pm, but the Delay step expires on May 3rd at 9 am. 
- A Canvas step delays until a specific time in the user's local time zone, but the users don't have a time zone set on their user profile. The delay then defaults to the company time zone for these users, which has already passed the specified time. 
  
##### Users will exit if a subsequent Delay step is within a prior Delay step's timeline

If the Canvas has two Delay steps using "Wait until Exact Date" but the first Delay step is longer than the second Delay step, users will also exit the Canvas. 

For example, let's say a Canvas has these steps:
- Step 1: Message step
- Step 2: Delay step until December 13th at 10 pm
- Step 3: Message step
- Step 4: Delay step until December 13th at 7 pm
- Step 5: Message step
  
The users who enter Step 4 will exit the Canvas before receiving Step 5 because Step 4's delay is part of Step 2's timeframe.

{% endtab %}
{% tab Until a specific day of the week %}

**특정 요일까지** 옵션을 사용하면 특정 요일, 특정 시간까지 사용자를 단계에 머물게 할 수 있습니다. 예를 들어 목요일이 회사 표준 시간대인 오후 4시에 도착할 때까지 사용자를 다음 시간으로 연기할 수 있습니다. 

이를 성공적으로 구성하려면 사용자가 선택한 요일(예: 목요일)에 캔버스에 들어왔지만 지정된 시간이 지난 후에 캔버스에 들어갈 경우 어떤 일이 발생할지 선택해야 합니다. 사용자를 당일에 승급하거나 다음 주까지 보류하도록 선택할 수 있습니다.
{% endtab %}
{% endtabs %}

## 지연 단계 사용

6월 10일이라고 가정해 보겠습니다. 6월 11일에 사용자가 캔버스에 들어가서 예정된 프로모션에 대한 메시지를 받기를 원합니다. 그런 다음 현지 시간으로 6월 17일 오후 3시까지 캔버스에서 사용자를 붙잡아 두려고 합니다. 6월 17일 오후 3시(현지 시간)에 사용자에게 프로모션에 대한 알림 메시지를 보내려고 합니다.

The sequence of Canvas steps could look like the following:

1. 먼저 6월 11일에 사용자가 캔버스에 입장한 직후에 보내는 메시지 단계를 추가합니다.
2. 6월 17일 오후 1시(현지 시간)까지 사용자를 보류하는 지연 단계를 만듭니다.
3. 지연 단계를 즉시 메시지를 전송하는 다른 메시지 단계에 연결합니다.

### 캔버스 끝에 있는 지연 구성요소 {#delay-as-last-step}

If you add a Delay component to your Canvas and there are no subsequent steps, any user who reaches the last step will be automatically advanced out of the Canvas. 지연 단계의 시간이 아직 도달하지 않은 경우에도 마찬가지입니다. This means that users who have already reached the Delay step will not receive any messages you add after this step. 그러나 사용자가 지연 단계에 도달하지 않았는데 메시지가 추가되면 해당 메시지를 받게 됩니다.

## 지연 분석

Delay components have the following metrics available in the analytics view of an active or previously active Canvas.

| 측정기준 | 설명 |
|---|---|
| _Entered_ | 단계를 입력한 횟수를 반영합니다. 캔버스에 재자격이 있는 사용자가 지연 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| _Proceeded to Next Step_ | 캔버스에서 다음 단계로 진행된 항목 수를 반영합니다. |
| _Exited Canvas_ | 캔버스를 종료하고 다음 단계로 진행하지 않은 항목의 수를 반영합니다. |
| _Personalization Failed_ | Reflects the number of times a personalized message or content intended for a user couldn't be delivered due to the following:<br> {::nomarkdown}<ul><li>Delay value is in the past</li><li>Delay value is over 2 years into the future</li><li><b>After a duration</b> value isn't a number</li><li><b>Until a specific day</b> value isn't a date or date-formatted string</li></ul>{:/} <br>See [Personalization failed errors](#personaliztion-failed-errors) for more details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이러한 분석에 대한 시계열은 확장된 구성요소 보기에서 사용할 수 있습니다.

## Troubleshooting

### Personalization failed errors

If users aren't triggering a personalized delay, it could be because the Context step you set to qualify them for the Delay step is not working as you expected. When a [context variable is invalid]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), a user will continue through your Canvas without having their context set by the Context step. This can cause them to not qualify for steps later in your Canvas, such as personalized delays.

