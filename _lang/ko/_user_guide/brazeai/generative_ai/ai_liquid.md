---
nav_title: BrazeAI Liquid 어시스턴트
article_title: BrazeAI Liquid 어시스턴트
description: "이 문서에서는 AI Liquid 어시스턴트의 작동 방식과 이를 사용하여 메시징용 Liquid 스니펫을 생성하는 방법에 대해 설명합니다."
page_type: reference
page_order: 5
---

# BrazeAI<sup>TM</sup> Liquid 어시스턴트

> <sup>BrazeAITM</sup> Liquid 어시스턴트는 메시지 콘텐츠를 개인화하는 데 필요한 Liquid를 생성하는 데 도움을 주는 <sup>BrazeAITM</sup> 기반의 채팅 도우미입니다.

<sup>BrazeAITM</sup> Liquid 어시스턴트를 사용하면 템플릿에서 Liquid를 생성하고, 개인화된 Liquid 제안을 받고, 기존 Liquid를 최적화하여 <sup>BrazeAITM</sup>의 지원을 받아 최적화할 수 있습니다. 어시스턴트는 사용된 Liquid를 설명하는 주석도 제공하므로 Liquid에 대한 이해를 높이고 직접 작성하는 방법을 배울 수 있습니다.

## 지원 채널

생성할 때 <sup>BrazeAITM</sup> 리퀴드 어시스턴트를 사용할 수 있습니다: 
- SMS 메시지
- 푸시 알림
- HTML 이메일 메시지
    - 어시스턴트는 템플릿이 아닌 이메일 메시지에서 작동하며 이미 작성된 이메일 메시지에서 가장 잘 작동합니다.
- 캔버스

## 작동 방식

<sup>BrazeAITM</sup> Liquid 어시스턴트는 마케팅 요구 사항에 맞는 효과적인 Liquid 코드를 작성할 수 있도록 설계되었습니다. Liquid 구문과 마케터가 메시지에서 Liquid를 활용하는 방법을 모두 학습한 AI는 개인화된 콘텐츠 제작의 뉘앙스를 잘 이해하고 있습니다. 또한, 커스텀 속성 이름(예: "favourite_color")과 데이터 유형(예: 부울 및 문자열)을 <sup>BrazeAITM</sup> Liquid 어시스턴트에 제공하면 BrazeAI<sup>TM</sup> Liquid 어시스턴트가 메시지를 정확하게 타겟팅하고 목표에 맞게 조정할 수 있습니다. 또한 브랜드 가이드라인을 생성하면 <sup>BrazeAITM</sup> Liquid 어시스턴트는 브랜드 가이드라인을 사용하여 생성된 결과물을 더 잘 커스텀하고 자체 브랜드 목소리에 맞게 콘텐츠를 맞춤 설정할 수 있습니다. 회원님이 생성한 브랜드 가이드라인은 회원님이 직접 사용할 수 있도록 콘텐츠를 맞춤 설정하는 데만 사용됩니다. 

## Liquid 코드 생성

<sup>BrazeAITM</sup> Liquid 어시스턴트를 실행하려면 메시지 작성기에서 AI 어시스턴트 아이콘을 선택합니다.

![AI 어시스턴트가 포함된 메시지 작성기.][1]{: style="max-width:50%;"}

[제공된 프롬프트](#provided-prompts)를 선택하거나 텍스트 상자에 직접 입력할 수 있습니다. Liquid 코드를 생성하려면 **작성기 업데이트**를 선택합니다.

![프롬프트가 제공되는 AI 어시스턴트 창입니다.][2]{: style="max-width:50%;"}
 
**재생성**을 선택하여 동일한 프롬프트를 사용하여 다른 메시지를 생성할 수 있습니다. 메시지를 제거하고 이전 메시지로 되돌리려면 **업데이트 실행 취소**를 선택합니다.

### 제공된 프롬프트

<sup>BrazeAITM</sup> Liquid 어시스턴트를 사용하는 동안 Liquid를 시작하는 데 도움이 되는 다양한 프롬프트가 표시될 수 있습니다. 몇 가지 프롬프트는 다음과 같습니다.

#### 앱 활동 사용

**앱 활동 사용** 프롬프트는 앱이 마지막으로 사용된 시간에 따라 다른 메시지를 보낼 수 있도록 Liquid 코드를 생성합니다. 어시스턴트가 보다 정확한 결과를 생성할 수 있도록 후속 질문을 할 수 있습니다.

!["앱 활동 사용" 프롬프트의 출력 예시입니다.][3]{: style="max-width:45%;"}

#### 카운트다운 추가

이 프롬프트는 이벤트 발생까지 남은 시간이 포함된 메시지를 전송하는 Liquid 코드를 생성합니다. 이벤트 날짜와 시간에 대한 세부 정보를 입력하라는 메시지가 표시됩니다.

!["카운트다운 추가" 프롬프트의 출력 예시입니다.][4]{: style="max-width:45%;"}

#### 영감 얻기

메시지 상자에 콘텐츠가 있을 때 이 메시지가 표시됩니다. Liquid로 메시지를 맞춤 설정하기 위해 선택할 수 있는 옵션 목록을 생성합니다. 

!["영감을 주세요" 프롬프트의 출력 예시입니다.][5]{: style="max-width:45%;"}

#### 내 Liquid 개선하기

메시지 작성기에 콘텐츠가 있을 때 이 메시지가 표시됩니다. 어시스턴트가 코드를 더 효율적이고 읽기 쉽게 만들어 주길 원할 때 이 옵션을 선택하세요.

!["내 Liquid 개선" 프롬프트의 출력 예시입니다.][6]{: style="max-width:45%;"}

## 베타 버전에서 지원되는 속성

| 기준 | 지식 유형 | 지식 유형
| - | - |
| Liquid( `for` 루프, `if` 문, 수학 및 기타 포함) | 코딩 | 코딩
| 기본 및 표준 사용자 속성 | 속성 > 속성
| 이러한 데이터 유형이 있는 커스텀 속성: {::nomarkdown}<ul><li>부울</li><li>숫자</li><li>문자열</li><li>배열</li><li>시간</li></ul>{:/} | 속성 |
| 연결된 콘텐츠 | 코딩 |
{: .reset-td-br-1 .reset-td-br-2 }

## 내 데이터는 어떻게 사용되어 OpenAI로 전송되나요?

메시지 콘텐츠를 수정하거나 생성하기 위해 Braze는 <sup>BrazeAITM</sup> AI 어시스턴트에 제출한 프롬프트, 메시지 콘텐츠 및/또는 브랜드 가이드라인(생성하기로 결정한 경우)을 OpenAI의 API 플랫폼으로 전송합니다. Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로, 사용자가 제공하는 콘텐츠에 고유 식별 정보를 포함하지 않는 한 OpenAI는 해당 쿼리가 누구로부터 전송되었는지 확인할 수 없습니다. [OpenAI의 API 플랫폼 약정](https://openai.com/policies/api-data-usage-policies)에 명시된 바와 같이, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 학습하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. [사용 정책](https://openai.com/policies/usage-policies) 및 [공유 및 게시 정책을](https://openai.com/policies/sharing-publication-policy) 포함하여 본인과 관련된 OpenAI의 정책을 준수해야 합니다. Braze는 AI가 생성한 콘텐츠와 관련하여 어떠한 종류의 보증도 하지 않습니다.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
