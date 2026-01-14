---
nav_title: 상담원 만들기
article_title: 커스텀 상담원 만들기
description: "상담원을 만드는 방법, 시작하기 전에 준비해야 할 사항, 메시징, 의사 결정 및 데이터 관리 전반에 걸쳐 상담원을 활용하는 방법에 대해 알아보세요."
alias: /creating-agents/
---

# 커스텀 상담원 만들기

> 커스텀 상담원을 만드는 방법, 시작하기 전에 준비해야 할 사항, 메시징, 의사 결정 및 고객 데이터 관리 전반에 걸쳐 상담원을 활용하는 방법에 대해 알아보세요. 자세한 내용은 [Braze 에이전트를]({{site.baseurl}}/user_guide/brazeai/agents) 참조하세요. 

{% alert important %}
Braze 커런츠는 현재 베타 버전입니다. 시작하는 데 도움이 필요하면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 전제 조건

시작하기 전에 다음이 필요합니다:

- 워크스페이스에서 **상담원 콘솔에** 액세스합니다. 이 옵션이 보이지 않는다면 Braze 관리자에게 문의하세요.  
- 커스텀 AI 에이전트를 만들고 편집할 수 있는 권한. 
- 상담원이 달성하기를 원하는 목표에 대한 아이디어입니다. Braze 에이전트는 다음 작업을 지원할 수 있습니다:  
   - **메시징:** 제목란, 헤드라인, 제품 내 카피 또는 기타 콘텐츠를 생성합니다.  
   - **의사 결정:** 행동, 환경설정 또는 커스텀 속성을 기반으로 캔버스에서 사용자를 라우팅하세요.  
   - **데이터 관리:** 값을 계산하거나, 카탈로그 항목을 보강하거나, 프로필 필드를 새로고침할 수 있습니다.  

## 작동 방식

에이전트를 만들 때 에이전트의 목적을 정의하고 에이전트가 어떻게 작동해야 하는지에 대한 가드레일을 설정합니다. 유지 시간이 지나면 에이전트를 Braze에 배포하여 개인화된 사본을 생성하고, 실시간 의사 결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다. 대시보드에서 언제든지 상담원을 일시 중지하거나 업데이트할 수 있습니다.

## 상담원 만들기

커스텀 상담원을 만들려면 다음과 같이 하세요:  

1. Braze 대시보드에서 **상담원 콘솔** > **상담원 관리로** 이동합니다.  
2. **상담원 만들기를** 선택합니다.  
3. 팀이 목적을 이해하는 데 도움이 되는 이름과 설명을 입력하세요.  
4. 상담원이 사용할 [모델을](#models) 선택합니다.  

Braze에서 커스텀 상담원을 만들기 위한 상담원 콘솔 인터페이스입니다. 화면에 상담원 이름과 설명을 입력하고 모델을 선택할 수 있는 필드가 표시됩니다.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. 상담원에게 지침을 제공합니다. 지침은 [작성 지침을](#writing-instructions) 참조하세요.
6. [상담원](#testing-your-agent) 출력을 [테스트하고](#testing-your-agent) 필요에 따라 지침을 조정합니다.
7. 준비가 완료되면 상담원 **생성을** 선택하여 상담원을 활성화합니다. 

## 다음 단계

이제 에이전트를 사용할 준비가 되었습니다! 자세한 내용은 [상담원 배포하기를]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/) 참조하세요. 

## 참조

### 모델

상담원을 설정할 때 응답을 생성하는 데 사용할 모델을 선택합니다. 두 가지 옵션이 있습니다:

#### 옵션 1: Braze 구동 모델 사용

이 옵션은 별도의 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대규모 언어 모델(LLM)에 직접 액세스할 수 있습니다. 이 옵션을 사용하려면 **자동을** 선택합니다.

{% alert note %}
Braze 기반 LLM을 사용하는 경우 베타 기간 동안에는 비용이 발생하지 않습니다. 호출은 하루에 50,000회, 총 500,000회 실행으로 제한됩니다. 자세한 내용은 [제한 사항을]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) 참조하세요.
{% endalert %}

#### 옵션 2: API 키 가져오기

이 옵션을 사용하면 OpenAI, Anthropic, AWS Bedrock 또는 Google Gemini와 같은 제공업체에 Braze 계정을 연결할 수 있습니다. LLM 제공업체로부터 API 키를 직접 가져오는 경우, 비용은 Braze가 아닌 제공업체를 통해 직접 청구됩니다.

설정하려면 다음과 같이 하세요:
1. **파트너 통합** > **기술 파트너로** 이동하여 제공업체를 찾습니다.
2. 공급업체에서 받은 API 키를 입력합니다.
3. **저장을** 선택합니다.

그런 다음 상담원에게 돌아가서 모델을 선택할 수 있습니다.

### 작성 지침

안내는 상담원에게 제공하는 규칙이나 가이드라인입니다(시스템 프롬프트). 에이전트가 실행될 때마다 에이전트가 어떻게 작동해야 하는지 정의합니다. 시스템 지침은 최대 10KB까지 가능합니다.

{% tabs %}
{% tab Best practices %}

다음은 메시징을 시작하는 데 도움이 되는 몇 가지 일반적인 모범 사례입니다:

1. 끝을 염두에 두고 시작하세요. 먼저 목표를 명시하세요.
2. 모델에게 역할 또는 페르소나를 지정합니다("귀하는 ...").
3. 명확한 컨텍스트와 제약 조건(오디언스, 길이, 어조, 형식)을 설정하세요.
4. 구조를 요청합니다("JSON/벌릿 목록/표 반환...").
5. 말하지 말고 보여주세요. 몇 가지 수준 높은 예시를 포함하세요.
6. 복잡한 작업을 순서대로 단계별로 나누기("1단계... 2단계...").
7. 추론을 장려합니다("큰 소리로 생각한 다음 대답하기").
8. 파일럿, 검사 및 반복. 작은 조정이 큰 품질 향상으로 이어질 수 있습니다.
9. 가장자리 케이스 처리, 가드레일 추가, 거부 지침 추가.
10. 재사용 및 확장을 위해 내부적으로 어떤 것이 효과적인지 측정하고 설명서를 작성하세요.

프롬프트 모범 사례에 대한 자세한 내용은 다음 모델 제공업체의 가이드를 참조하세요:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [인류학](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [쌍둥이자리](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

이 예제 프롬프트는 설문조사 입력을 받아 간단한 감성 분석을 출력합니다:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

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
{% enddetails %}

{% endtab %}
{% endtabs %}


#### 상담원 테스트  

**라이브 프리뷰** 창은 구성 환경 내에서 나란히 있는 패널로 표시되는 상담원의 인스턴스입니다. 에이전트를 만들거나 업데이트하는 동안 이를 사용하여 최종 사용자와 유사한 방식으로 에이전트를 테스트할 수 있습니다. 이 단계를 통해 예상한 대로 작동하는지 확인할 수 있으며, 라이브를 시작하기 전에 미세 조정할 수 있습니다.

커스텀 상담원을 테스트하기 위한 라이브 프리뷰 창을 보여주는 상담원 콘솔. 인터페이스에는 예시 고객 데이터가 있는 샘플 입력 필드, 테스트 실행 버튼, 상담원 출력이 표시되는 응답 영역이 표시됩니다.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. **샘플 입력** 필드에 상담원이 처리할 실제 시나리오를 반영하는 고객 데이터나 고객 응답의 예시를 입력합니다. 
2. **테스트 실행을** 선택합니다. 에이전트가 구성에 따라 실행되고 응답을 표시합니다. 테스트 실행은 일일 및 총 호출 한도에 포함됩니다.

비판적인 시각으로 결과물을 검토하세요. 다음 질문을 고려하세요:

- 카피가 브랜드에 어울리는 느낌인가요? 
- 의사 결정 로직이 의도한 대로 고객을 라우팅하나요? 
- 계산된 값이 정확한가요? 

뭔가 이상하다고 느껴지면 상담원의 구성을 업데이트하고 다시 테스트하세요. 몇 가지 다른 입력을 실행하여 에이전트가 여러 시나리오, 특히 데이터가 없거나 잘못된 응답과 같은 엣지 케이스에 어떻게 적응하는지 확인하세요.

