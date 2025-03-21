---
nav_title: 모범 사례
article_title: 캔버스 모범 사례
page_order: 1
description: "이 문서는 캔버스 및 캔버스 플로우를 사용하여 사용자 여정을 생성하고 커스텀하는 모범 사례를 제공합니다."
tool: Canvas

---

# 캔버스 모범 사례

> 이 문서는 캔버스 및 캔버스 플로우를 사용하여 사용자 여정을 생성하고 커스텀하는 모범 사례를 제공합니다.

## 귀하의 목적을 확인하세요

무엇, 누구, 그리고 왜에 대해 파고들어 보세요!
- 사용자가 무엇을 달성하도록 돕고 있습니까?
- 당신이 도달하려고 하는 사용자는 누구입니까?
- 왜 이 캔버스를 만들고 있습니까?

## 섞고 맞추세요

Unlock new combinations of user journeys with [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/).
- 사용자를 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/)로 분할하고 다른 워크플로를 구축하십시오.
- 사용자 여정을 [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 단계로 간격을 두세요.
- 캔버스 흐름의 원하는 위치에 [독립형 메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 추가하세요. 

## 더 풍부한 메시지 만들기

더 풍부한 메시지로 사용자를 끌어들이세요.

- Build [in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) for onboarding Canvases to make the most out of your first impression.
- Introduce [Content Cards]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) in a Canvas journey for promotional offers and push notifications.

## 사용자 여정을 테스트하세요

대조군을 포함하여 캔버스 메시징의 영향을 확인하세요. 이렇게 하면 캔버스가 어떻게 수신되었는지 이해할 수 있습니다!

- 캔버스의 각 단계를 이름 지어 사용자 여정을 식별하세요.
- 사용자 여정에서 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 구성 요소를 활용하여 사용자를 생성한 다른 경로에 무작위로 할당합니다. 
- 지연 및 메시지 단계를 통해 사용자 여정을 다양화하여 가장 효과적인 경로를 발견하세요.
- [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)을(를) 확인하여 사용자 여정의 각 구성 요소의 성능을 확인하세요.
- [Edit your Canvas]({{site.baseurl}}/post-launch_edits/) after the initial launch.

## Scheduling your Canvases

{% alert note %}
Canvas will prevent you from using scheduled send with a time that has already passed. However, it's possible to launch a Canvas during the exact same minute that the campaign is scheduled (or in the seconds before). This can lead to the Canvas missing the scheduled entry time and users not entering the Canvas. We recommend sending Canvases immediately in the event that any campaigns are edited within minutes of the scheduled send time.
{% endalert %}

For Canvas steps, consider the following details when scheduling your Canvas:

- Schedule changes will only apply to users who aren't already waiting to receive the step.
- Audience changes by default apply to all users, unless you schedule changes to apply to users who aren't waiting to receive the step.
- Editing a Canvas that is scheduled to deliver as soon as deployed and selecting **Update** will essentially cause it to be sent.
