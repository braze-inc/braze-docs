---
nav_title: AI Liquid Assistant
article_title: AI Liquid Assistant
description: "이 기사에서는 Sage AI Liquid Assistant가 작동하는 방식과 메시징을 위한 Liquid 스니펫을 생성하는 방법에 대해 다룰 것입니다."
page_type: reference
page_order: 5
---

# AI Liquid 보조

> Sage AI Liquid Assistant는 Sage AI에 의해 구동되는 채팅 어시스턴트로, 메시지 내용을 개인화하는 데 필요한 Liquid를 생성하는 데 도움을 줍니다. 

AI Liquid Assistant를 사용하면 템플릿에서 Liquid를 생성하고, 개인화된 Liquid 제안을 받고, Sage AI의 지원으로 기존 Liquid를 최적화할 수 있습니다. AI Liquid Assistant는 사용된 Liquid을 설명하는 주석도 제공하므로 Liquid에 대한 이해를 높이고 직접 작성하는 방법을 배울 수 있습니다.

{% alert important %}
AI Liquid Assistant는 현재 푸시 및 SMS 채널을 적극적으로 사용하는 제한된 수의 고객을 대상으로 베타 버전으로 제공되고 있습니다. 베타에 고려되는 것에 관심이 있으시면 고객 성공 매니저에게 연락하거나 이 [포털 카드](https://braze.productboard.com/entity-detail/features/27273918)에 관심을 표시하십시오.
{% endalert %}

## 작동 방식

AI Liquid Assistant는 마케팅 요구에 맞춘 효과적인 Liquid 코드를 작성하는 데 도움을 주도록 설계되었습니다. Liquid 구문과 마케터들이 메시지에서 Liquid을 사용하는 방법에 대해 훈련된 우리 AI는 개인화된 콘텐츠를 작성하는 미묘한 차이를 이해합니다. 또한, AI Liquid Assistant에 커스텀 속성 이름(예: `favourite_color`) 및 데이터 유형(예: boolean 또는 문자열)을 제공함으로써, AI Assistant는 메시지가 목표에 맞게 정확하게 타겟팅되도록 보장합니다.

## Liquid 코드 생성 중

AI Liquid 도우미를 실행하려면 메시지 작성기에서 AI 도우미 아이콘을 선택하세요.

![메시지 작성기 with the AI assistant.][1]{: style="max-width:50%;"}

[제공된 프롬프트](#provided-prompts)를 선택하거나 텍스트 상자에 직접 입력할 수 있습니다. Liquid 코드를 생성하려면 **Update composer**를 선택하십시오.

![AI 어시스턴트 창에 제공된 프롬프트가 있습니다.][2]{: style="max-width:50%;"}
 
동일한 프롬프트를 사용하여 **다시 생성**을 선택하여 다른 메시지를 생성할 수 있습니다. 메시지를 제거하고 이전 메시지로 되돌리려면 **업데이트 실행 취소**를 선택하세요.

### 제공된 프롬프트

AI Liquid Assistant를 사용하는 동안 Liquid를 시작하는 데 도움이 되는 다양한 프롬프트를 볼 수 있습니다. 일부 프롬프트는 아래에 나열되어 있습니다.

#### 앱 활동 사용

**앱 사용 활동** 프롬프트는 앱이 마지막으로 사용된 시점을 기준으로 다양한 메시지를 보낼 수 있도록 Liquid 코드를 생성합니다. 후속 질문을 요청받을 수 있으므로 도우미가 더 정확한 결과를 생성할 수 있습니다.

![앱 활동 사용 프롬프트의 예시 출력입니다.][3]{: style="max-width:45%;"}

#### 카운트다운 추가

이 프롬프트는 이벤트가 발생할 때까지 남은 시간을 메시지로 보내는 Liquid 코드를 생성합니다. 이벤트 날짜와 시간에 대한 세부 정보를 제공하라고 요청할 것입니다.

!["카운트다운 추가" 프롬프트의 예시 출력입니다.][4]{: style="max-width:45%;"}

#### 영감을 주세요

이 프롬프트는 메시지 상자에 내용이 있을 때 나타납니다. 옵션 목록을 생성하여 Liquid로 메시지를 개인화할 수 있습니다. 

![“영감을 주세요” 프롬프트의 예시 출력입니다.][5]{: style="max-width:60%;"}

#### 내 Liquid 개선하기

메시지 작성기에 내용이 있을 때 이 프롬프트가 나타납니다. 선택하면 도우미가 코드 를 더 효율적이고 읽기 쉽게 만들 수 있습니다.

![Liquid "Improve my Liquid" 프롬프트의 예시 출력입니다.][6]{: style="max-width:45%;"}

## 베타에서 지원되는 속성

| 기준 | 지식 유형 |
| - | - |
| Liquid (including `for` loops, `if` statements, math, and others) | 코딩 |
| 기본값 및 표준 사용자 속성 | 속성 |
| 커스텀 속성 that have any of these 데이터 types: {::nomarkdown}<ul><li>불리언</li><li>숫자</li><li>문자열</li><li>배열</li><li>시간</li></ul>{:/} | 속성 |
| 연결된 콘텐츠 | 코딩 |
{: .reset-td-br-1 .reset-td-br-2 }

## 내 데이터는 어떻게 사용되고 OpenAI로 전송되나요?

메시지 콘텐츠를 수정하거나 생성하려면 Braze가 Liquid AI Assistant에 제출된 프롬프트, 메시지 및 콘텐츠를 OpenAI의 API 플랫폼에 보냅니다. Braze에서 OpenAI로 전송된 모든 쿼리는 익명화되므로, 제공한 콘텐츠에 고유하게 식별 가능한 정보가 포함되지 않는 한 OpenAI는 쿼리를 보낸 사람을 식별할 수 없습니다. [OpenAI의 API 플랫폼 약속](https://openai.com/policies/api-data-usage-policies)에 자세히 설명된 바와 같이, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 훈련하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. OpenAI의 정책 중 귀하와 관련된 정책, [사용 정책](https://openai.com/policies/usage-policies) 및 [공유 및 출판 정책](https://openai.com/policies/sharing-publication-policy)을 준수해야 합니다. Braze는 AI 생성 콘텐츠에 대해 어떠한 종류의 보증도 하지 않습니다

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}