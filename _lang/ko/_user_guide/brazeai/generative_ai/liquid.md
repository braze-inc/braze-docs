---
nav_title: Liquid 코드
article_title: BrazeAI로 Liquid 코드 생성하기
description: "이 글에서는 AI Liquid 어시스턴트의 작동 방식과 이를 사용하여 메시징에 사용할 Liquid 스니펫을 생성하는 방법을 다룹니다."
page_type: reference
page_order: 0.0
---

# <sup>BrazeAITM으로</sup> Liquid 코드 생성하기

> <sup>BrazeAITM</sup> Liquid Assistant는 메시지 콘텐츠를 개인화하는 데 필요한 Liquid를 생성하는 데 도움을 주는 <sup>BrazeAITM</sup> 기반의 채팅 어시스턴트입니다.

## <sup>BrazeAITM</sup> Liquid 어시스턴트 정보

<sup>BrazeAITM</sup> Liquid Assistant는 마케팅 요구 사항에 맞는 효과적인 Liquid 코드를 작성할 수 있도록 설계되었습니다. Liquid 구문과 마케터가 메시징에서 Liquid를 활용하는 방법에 대해 학습한 AI는 개인화된 콘텐츠 제작의 뉘앙스를 잘 이해하고 있습니다.

또한, 커스텀 속성 이름(예: “favourite_color”) )과 데이터 유형(예: 부울 및 문자열)을 <sup>BrazeAITM</sup> Liquid 어시스턴트에 제공하면 메시지를 정확하게 타겟팅하고 목표에 맞게 조정할 수 있습니다. 또한 브랜드 가이드라인을 생성하면 <sup>BrazeAITM</sup> Liquid 어시스턴트는 브랜드 가이드라인을 사용하여 생성된 결과물을 더 잘 개인화하고 브랜드 보이스에 맞게 콘텐츠를 커스텀할 수 있습니다. 회원님이 생성한 브랜드 가이드라인은 회원님이 직접 사용할 수 있도록 콘텐츠를 개인화하는 데만 사용됩니다.

## 지원되는 채널

생성할 때 <sup>BrazeAITM</sup> Liquid Assistant를 사용할 수 있습니다: 
- SMS 메시지
- 푸시 알림
- HTML 이메일 메시지
- 캔버스

{% alert note %}
어시스턴트는 템플릿이 아닌 이메일 메시지에서 작동합니다. 이미 구축된 이메일 메시징에서 가장 잘 작동합니다.
{% endalert %}

## Liquid 코드 생성하기

<sup>BrazeAITM</sup> Liquid 어시스턴트를 실행하려면 메시지 작성기에서 AI 어시스턴트 아이콘을 선택합니다.

AI 어시스턴트가 있는 메시지 작성기.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

포함된 프롬프트 중 하나를 선택하거나 텍스트 상자에 직접 입력할 수 있습니다.

{% tabs local %}
{% tab use app activity %}
**앱 활동 사용** 프롬프트는 앱이 마지막으로 사용된 시간에 따라 다른 메시지를 보낼 수 있도록 Liquid 코드를 생성합니다. 어시스턴트가 보다 정확한 결과를 생성할 수 있도록 후속 질문을 할 수 있습니다.

!"[앱 활동 사용" 프롬프트의 출력 예시.]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
이 프롬프트는 이벤트가 발생할 때까지 남은 시간이 포함된 메시지를 전송하는 Liquid 코드를 생성합니다. 이벤트 날짜와 시간에 대한 세부 정보를 입력하라는 메시지가 표시됩니다.

"카운트다운 추가" 프롬프트의 출력 예시입니다.]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
메시지함에 콘텐츠가 있을 때 이 메시지가 표시됩니다. Liquid로 메시지를 개인화하기 위해 선택할 수 있는 옵션 목록을 생성합니다. 

"영감을 주세요" 프롬프트의 출력 예시입니다.]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
이 메시지는 메시지 작성기에 콘텐츠가 있을 때 표시됩니다. 어시스턴트가 코드를 더 효율적이고 읽기 쉽게 만들어 주길 원할 때 선택하세요.

!"[내 Liquid 개선" 프롬프트의 출력 예시.]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Liquid 코드를 생성하려면 **작성기 업데이트를** 선택합니다.

\![AI 도우미 창에 프롬프트가 제공됩니다.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
**재생성을** 선택하여 동일한 프롬프트를 사용하여 다른 메시지를 생성할 수 있습니다. 메시지를 삭제하고 이전 메시지로 되돌리려면 **업데이트 실행 취소를** 선택합니다.

## Liquid 속성 {#supported-attributes}

다음 속성은 현재 <sup>BrazeAITM</sup> Liquid Assistant의 베타 버전입니다:

| 기준 | 지식 유형 | 지식 유형
| - | - |
| Liquid( `for` 루프, `if` 문, 수학 및 기타 포함) | 코딩 | 코딩
| 기본 및 표준 사용자 속성 > 속성 > 기여도
| 이러한 데이터 유형이 있는 커스텀 속성: {::nomarkdown}<ul><li>부울</li><li>숫자</li><li>문자열</li><li>배열</li><li>시간</li></ul>{:/} | 속성 | 기여도
| 연결된 콘텐츠 | 코딩 | 코딩
{: .reset-td-br-1 .reset-td-br-2 }

## 모범 사례

<sup>BrazeAITM</sup> Liquid Assistant를 위한 효과적인 프롬프트를 작성하는 데 도움이 필요하면 모범 사례를 확인하세요:

### 자연어 사용

<sup>BrazeAITM</sup> Liquid 어시스턴트는 자연어를 이해하도록 훈련되었습니다. 도움을 요청할 때 동료와 대화하듯 채팅하세요. 이렇게 하면 어시스턴트가 사용자의 요구 사항을 더 쉽게 이해하고 정확한 지원을 제공할 수 있습니다.

### 컨텍스트 제공

컨텍스트를 제공하면 <sup>BrazeAITM</sup> Liquid 어시스턴트가 프로젝트를 둘러싼 더 큰 그림을 이해하는 데 도움이 됩니다. 다음과 같은 문맥을 포함하면 도움이 됩니다:

- 회사명 및 업종
- 블랙 프라이데이 또는 연말 세일과 같이 진행 중인 캠페인
- 클릭률 증가와 같은 목표와 같은 목표
- 메시징에 포함할 특정 커스텀 속성

프롬프트에 컨텍스트를 포함하면 어시스턴트가 사용자의 필요에 더 잘 맞도록 응답을 조정하는 데 도움이 됩니다. 캠페인, 메시지 요약 또는 브레인스토밍 설명서의 세부 정보를 포함시켜 어시스턴트가 빠르게 이해할 수 있도록 할 수도 있습니다.

### 구체적이어야 합니다.

<sup>BrazeAITM</sup> Liquid Assistant는 후속 질문을 할 수 있지만, 미리 세부 정보를 제공하면 더 정확한 결과를 더 빨리 얻을 수 있습니다. 다음과 같은 세부 정보를 포함하는 것이 좋습니다:

- 메시징에 대한 알려진 기본 설정 또는 요구 사항
- 메시지 수신자의 응답이 없거나 대체 메시지 옵션과 같은 상황을 처리하는 방법에 대한 지침
- 연결된 콘텐츠를 사용하는 Liquid, API 엔드포인트에 대한 설명서, 샘플 API 응답 또는 둘 다를 요청하는 경우

### 창의력 발휘하기

<sup>BrazeAITM</sup> Liquid Assistant가 메시징을 어떻게 향상시킬 수 있는지 알아보세요. 창의성이 더 많은 참여로 이어질 수 있으므로 다양한 프롬프트와 아이디어로 실험해 보세요.

## 프롬프트 예시

다음은 시작하는 데 도움이 되는 몇 가지 예시입니다:

{% tabs local %}
{% tab gaining knowledge %}
- Liquid란 무엇이며, Braze 내에서 마케팅 캠페인의 개인화를 강화하는 데 어떻게 도움이 될 수 있나요?
- Liquid에서 인구 통계 정보나 과거 구매 내역 등 마케팅 메시지를 개인화하기 위해 사용할 수 있는 데이터 유형에는 어떤 것이 있나요?
{% endtab %}

{% tab personalizing dynamic content %}
- 고객의 로열티 상태에 따라 다른 콘텐츠를 보여주는 메시지를 생성하세요. 로열티 상태를 알 수 없는 경우 대체 메시지를 보내세요.
- 사용자가 즐겨 찾는 제품과 마지막 구매 날짜를 포함하는 동적 메시지를 작성합니다. 마지막 구매가 없는 경우 메시지를 중단합니다.
- 남은 시간 카운트다운이 포함된 메시지를 다른 사람이 클릭하도록 유도하려면 Write me Liquid를 사용하세요. 오퍼가 만료된 경우 메시지를 중단합니다.
- 사용자가 카트에 남은 품목이 있는지 다시 돌아와서 결제하도록 유도하는 메시지를 작성할 수 있도록 도와주세요.
- 고객의 국가에 따라 메시지를 개인화하려면 Liquid를 작성하세요. 메시징에 국가 이름을 입력하고 싶습니다. 둘 중 하나라도 없는 경우 링크를 클릭하여 프로필을 업데이트하도록 제안하세요.
- 사용자의 이름으로 환영 메시지를 개인화하고 사용자의 성별에 따라 다른 문구를 작성하려면 어떻게 해야 하나요?
- 커스텀 속성( “CUSTOM_ATTRIBUTE_NAME“ )과 그 값에 따라 다양한 메시지를 표시하려면 Liquid를 작성하세요. 보낼 수 있는 옵션은 6가지가 있습니다. 커스텀 속성에 대한 값이 없는 경우 플레이스홀더 메시지를 보내려고 합니다.
{% endtab %}

{% tab handling outliers %}
- 참여율과 전환율을 높이기 위해 마케팅 캠페인에서 Liquid를 어떻게 사용했는지 몇 가지 예를 들어 주시겠어요?
- 유기한 장바구니 알림이나 개인화된 프로모션과 같이 여름 세일을 위한 문자 메시지에서 Liquid의 일반적인 사용 사례는 무엇인가요?
{% endtab %}
{% endtabs %}

{% alert tip %}
흥미로운 메시지나 경험이 있다면 [피드백 세션을](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) 예약하여 알려주세요.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
