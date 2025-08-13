---
nav_title: 결정 분할 
article_title: 결정 분할 
alias: /decision_split/
page_order: 2
page_type: reference
description: "이 참조 문서에서는 캔버스에서 의사 결정 분할을 만들고 사용하는 방법에 대해 설명합니다."
tool: Canvas

---

# 결정 분할 

> 캔버스의 의사 결정 분할 구성 요소를 사용하면 사용자에게 개인화된 실시간 경험을 제공할 수 있습니다.

![A Decision Split step named "Push enabled?" for users who aren't push enabled and users who are push enabled.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

이 구성 요소는 사용자가 쿼리와 일치하는지 여부에 따라 캔버스 분기를 만드는 데 사용할 수 있습니다.

## 의사 결정 분할 만들기 

To create a decision split in your workflow, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Decision Split**.

### 분할 정의

사용자를 어떻게 분할하고 싶으신가요? You can use [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) and filters to draw the line. 기본적으로 `true` 또는 `false` 쿼리를 만들어 사용자를 평가한 다음 사용자를 한 단계 또는 다른 단계로 유도하는 것입니다. 하나 이상의 세그먼트 또는 하나의 필터를 사용해야 합니다. 세그먼트와 필터를 모두 사용할 필요는 없습니다.

![A Decision Split step with the filter "Push Enabled is true" selected.]({% image_buster /assets/img/define-split-2.png %}){: style="max-width:90%;"}

{% alert note %}
By default, segments and filters for a Decision Split step are checked right after receiving a previous step, unless you add a delay.
{% endalert %} 

## 분할 사용

의사 결정 분할을 사용하면 사용자가 특정 메시징 채널을 사용하여 메시지를 수신하는지 여부를 포함하여 세그먼트 또는 속성을 기반으로 사용자의 경로를 구분하는 데 도움이 될 수 있습니다!

온보딩 플로우를 만든다고 가정해 보겠습니다. 가입 시 환영 이메일로 시작하게 될 것입니다. 그런 다음 이틀 후 푸시를 사용하도록 설정한 사용자에게만 푸시 메시지를 보내려고 합니다. 그 후 모든 사용자는 가입한 지 3일 후에 또 다른 이메일을 받게 됩니다. 또한 결정 분할을 사용하여 푸시를 사용 설정하지 않은 사용자에게 인앱 메시지를 보내 푸시를 사용 설정하도록 유도할 수도 있습니다.

경로 중 하나를 따라가는 단계가 없는 경우 해당 경로로 이동한 사용자는 캔버스를 종료합니다. 

![A Decision Split step named "Push enabled?" for users who aren't push enabled and those who are. For users who aren't push enabled, they'll experience a 3-day delay then receive an email message. For users who are push enabled, they will experience a 1-day delay, receive a push notification followed by a 2-day delay, then they'll receive the same email message as the users who aren't push enabled.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## 분석

이 단계의 분석에 대한 설명은 다음 표를 참조하세요:

| 측정기준 | 설명 |
|---|---|
| _Entered_ | 단계를 입력한 총 횟수입니다. 캔버스에 재자격이 있고 사용자가 결정 분할 단계를 두 번 입력하는 경우 두 개의 항목이 기록됩니다. |
| _Yes_ | 지정된 기준을 충족하고 '예' 경로로 진행된 항목의 수입니다. |
| _No_ | 지정된 기준을 충족하지 못하고 "아니오" 경로로 진행된 항목 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

