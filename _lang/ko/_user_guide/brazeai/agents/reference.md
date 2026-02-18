---
nav_title: 참조
article_title: 상담원 참조
description: "Braze 에이전트에 대한 주요 세부 정보를 참조하세요."
page_order: 3
---

# 상담원 참조

> 커스텀 상담원을 만들 때 지침 및 출력 스키마와 같은 주요 설정에 대한 자세한 내용은 이 문서를 참조하세요. 소개는 [Braze 에이전트를]({{site.baseurl}}/user_guide/brazeai/agents/) 참조하세요.

{% alert important %}
Braze 커런츠는 현재 베타 버전입니다. 시작하는 데 도움이 필요하면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 모델

상담원을 설정할 때 응답을 생성하는 데 사용하는 모델을 선택할 수 있습니다. 두 가지 옵션이 있습니다: Braze 기반 모델을 사용하거나 자체 API 키를 가져오는 것입니다.

{% alert important %}
Braze 기반 **자동** 모델은 카탈로그 검색 및 사용자 세분화 멤버십과 같은 작업을 수행하기에 충분한 사고 능력을 갖춘 모델에 최적화되어 있습니다. 다른 모델을 사용하는 경우 사용 사례에 적합한 모델인지 테스트를 통해 확인하는 것이 좋습니다. 속도와 기능이 다른 모델에 다양한 수준의 세부 사항이나 단계별 사고를 제공하도록 [지침을](#writing-instructions) 조정해야 할 수도 있습니다.
{% endalert %}

### Option 1: Braze 구동 모델 사용

이 옵션은 별도의 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대규모 언어 모델(LLM)에 직접 액세스할 수 있습니다. 이 옵션을 사용하려면 Gemini 모델을 사용하는 **자동을** 선택합니다.

### Option 2: API 키 가져오기

이 옵션을 사용하면 OpenAI, Anthropic, AWS Bedrock 또는 Google Gemini와 같은 제공업체에 Braze 계정을 연결할 수 있습니다. LLM 제공업체로부터 API 키를 직접 가져오는 경우 토큰 비용은 Braze를 통하지 않고 제공업체를 통해 직접 청구됩니다.

{% alert important %}
레거시 모델은 몇 달 후에 단종되거나 더 이상 사용되지 않을 수 있으므로 최신 모델을 정기적으로 테스트하는 것이 좋습니다.
{% endalert %}

설정하려면 다음과 같이 하세요:

1. **파트너 통합** > **기술 파트너로** 이동하여 제공업체를 찾습니다.
2. 공급업체에서 받은 API 키를 입력합니다.
3. Select **Save**.

그런 다음 상담원에게 돌아가서 모델을 선택할 수 있습니다.

{% alert important %}
귀하가 Braze가 제공하는 LLM을 사용하는 경우, 해당 모델의 제공자는 귀하와 Braze 간의 데이터 처리 부록(DPA) 약관에 따라 Braze 하위 처리자 역할을 수행하게 됩니다. 회원님이 직접 API 키를 가져오기로 선택한 경우, 회원님과 Braze 간의 계약에 따라 LLM 구독의 제공업체는 타사 제공업체로 간주됩니다.  
{% endalert %}

## 작성 지침

안내는 상담원에게 제공하는 규칙이나 가이드라인입니다(시스템 프롬프트). 에이전트가 실행될 때마다 에이전트가 어떻게 작동해야 하는지 정의합니다. 시스템 지침은 최대 25KB까지 가능합니다.

다음은 메시징을 시작하는 데 도움이 되는 몇 가지 일반적인 모범 사례입니다:

1. 끝을 염두에 두고 시작하세요. 먼저 목표를 명시하세요.
2. 모델에게 역할 또는 페르소나를 지정합니다("귀하는 ...").
3. 명확한 컨텍스트와 제약 조건(오디언스, 길이, 어조, 형식)을 설정하세요.
4. 구조를 요청합니다("JSON/벌릿 목록/표 반환...").
5. 말하지 말고 보여주세요. 몇 가지 수준 높은 예시를 포함하세요.
6. 복잡한 작업을 순서대로 단계별로 나누기("1단계... 2단계...").
7. 추론을 장려합니다("내부적으로 단계를 검토한 다음 간결한 최종 답변을 제공" 또는 "결정에 대해 간략하게 설명").
8. 파일럿, 검사 및 반복. 작은 조정이 큰 품질 향상으로 이어질 수 있습니다.
9. 가장자리 케이스 처리, 가드레일 추가, 거부 지침 추가.
10. 재사용 및 확장을 위해 내부적으로 어떤 것이 효과적인지 측정하고 설명서를 작성하세요.

상담원이 구문 분석할 수 없는 응답을 수신할 경우 기본값을 포괄 응답으로 포함하는 것도 좋습니다. 이 오류 처리를 통해 상담원이 알 수 없는 결과 변수를 알려줄 수 있습니다. 예를 들어 상담원에게 '긍정' 또는 '부정' 감정 값만 묻는 대신 결정할 수 없는 경우 '잘 모르겠다'를 반환하도록 요청하세요.

### 간단한 프롬프트

이 예제 프롬프트는 설문조사 입력을 받아 간단한 감성 분석을 출력합니다:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### 복잡한 프롬프트 

이 예제 프롬프트는 사용자의 설문조사 입력을 받아 이를 하나의 감성 라벨로 분류합니다. 그런 다음 그 결과를 사용하여 사용자를 다른 캔버스 경로(예: 긍정적인 피드백 대 부정적인 피드백)로 라우팅하거나 향후 타겟팅을 위해 감성을 고객 프로필에 커스텀 속성으로 저장할 수 있습니다.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}

프롬프트 모범 사례에 대한 자세한 내용은 다음 모델 제공업체의 가이드를 참조하세요:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [인류학](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [쌍둥이자리](https://support.google.com/a/users/answer/14200040?hl=en)

### Using Liquid

상담원의 안내에 [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) 포함하면 응답에 개인화된 기능을 추가할 수 있습니다. 상담원이 가져오는 정확한 Liquid 변수를 지정하고 프롬프트의 컨텍스트에 포함시킬 수 있습니다. 예를 들어, "이름"을 명시적으로 작성하는 대신 Liquid 스니펫 {% raw %}`{{${first_name}}}`{% endraw %} 을 사용할 수 있습니다:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

상담원 **콘솔의** **로그** 섹션에서 상담원의 입력 및 출력에 대한 세부 정보를 검토하여 Liquid에서 어떤 값이 렌더링되는지 파악할 수 있습니다.

![지침에 Liquid가 있는 상담원에 대한 세부 정보입니다.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## 카탈로그 및 필드

상담원이 참조할 특정 카탈로그를 선택하여 관련성이 있는 경우 상담원에게 제품 및 기타 비사용자 데이터를 이해하는 데 필요한 컨텍스트를 제공하세요. 에이전트는 토큰 사용을 최소화하기 위해 도구를 사용하여 관련 항목만 찾아서 LLM으로 전송합니다.

![상담원이 검색할 '레스토랑' 카탈로그 및 "Loyalty_Program" 열이 선택되어 있습니다.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## 세그먼트 멤버십 컨텍스트 세분화

캔버스에서 에이전트를 사용할 때 에이전트가 각 사용자의 세그먼트 멤버십을 상호 참조할 수 있도록 최대 3개의 세그먼트를 선택할 수 있습니다. 상담원이 "로열티 사용자" 세그먼트에 대해 세그먼트 멤버십이 선택되어 있고 그 상담원이 캔버스에서 사용된다고 가정해 보겠습니다. 사용자가 상담원 단계를 입력하면 상담원은 각 사용자가 상담원 콘솔에서 지정한 각 세그먼트의 멤버인지 상호 참조하여 각 사용자의 멤버십(또는 비멤버십)을 LLM의 컨텍스트로 사용할 수 있습니다.

![상담원 멤버십 액세스 권한을 위해 선택한 "로열티 사용자" 세그먼트입니다.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## 브랜드 가이드라인

상담원이 응답할 때 준수할 [브랜드 가이드라인을]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) 선택할 수 있습니다. 예를 들어 상담원이 사용자에게 헬스장 멤버십 가입을 유도하는 SMS 문구를 생성하도록 하려면 이 필드를 사용하여 미리 정의한 굵은 글씨로 동기 부여를 위한 가이드라인을 참조할 수 있습니다.

## 온도

에이전트를 사용하여 사용자가 모바일 앱에 로그인하도록 유도하는 문구를 생성하는 것이 목표라면 에이전트가 더 창의적으로 문맥 변수의 미묘한 차이를 활용할 수 있도록 더 높은 온도를 설정할 수 있습니다. 상담원을 사용하여 감정 점수를 생성하는 경우에는 상담원이 부정적인 설문조사 응답을 추측하지 않도록 온도를 낮게 설정하는 것이 이상적일 수 있습니다. 이 설정을 테스트하고 시나리오에 맞게 상담원이 생성한 출력을 검토하는 것이 좋습니다.

{% alert note %}
현재 OpenAI에서는 온도가 지원되지 않습니다.
{% endalert %}