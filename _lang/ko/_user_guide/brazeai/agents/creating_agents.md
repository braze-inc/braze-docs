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

## 필수 조건

Before you start, you'll need the following:

- 워크스페이스에서 **상담원 콘솔에** 액세스합니다. 이 옵션이 보이지 않는다면 Braze 관리자에게 문의하세요.  
- 커스텀 AI 에이전트를 만들고 편집할 수 있는 권한. 
- 상담원이 달성하기를 원하는 목표에 대한 아이디어입니다. Braze 에이전트는 다음 작업을 지원할 수 있습니다:  
   - **메시징:** 제목란, 헤드라인, 제품 내 카피 또는 기타 콘텐츠를 생성합니다.  
   - **의사 결정:** 행동, 환경설정 또는 커스텀 속성을 기반으로 캔버스에서 사용자를 라우팅하세요.  
   - **데이터 관리:** 값을 계산하거나, 카탈로그 항목을 보강하거나, 프로필 필드를 새로고침할 수 있습니다.  

## 작동 방식

에이전트를 만들 때 에이전트의 목적을 정의하고 에이전트가 어떻게 작동해야 하는지에 대한 가드레일을 설정합니다. 유지 시간이 지나면 에이전트를 Braze에 배포하여 개인화된 사본을 생성하고, 실시간 의사 결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다. 대시보드에서 언제든지 상담원을 일시 중지하거나 업데이트할 수 있습니다.

다음 사용 사례는 커스텀 상담원을 활용하는 몇 가지 방법을 보여줍니다.

| Use case | 설명 |
| --- | --- |
| 고객 피드백 처리 | 사용자 피드백을 상담원에게 전달하여 감정을 분석하고 공감할 수 있는 후속 메시지를 생성하세요. 가치가 높은 사용자의 경우 상담원이 응답을 에스컬레이션하거나 특전을 제공할 수 있습니다. |
| 콘텐츠 현지화하기 | 글로벌 캠페인의 경우 카탈로그 텍스트를 다른 언어로 번역하거나 지역별 채널의 경우 톤과 길이를 조정할 수 있습니다. 예를 들어 '클래식 클럽마스터 선글라스'를 스페인어로 '가파스 데 솔 클래식 클럽마스터'로 번역하거나 SMS 캠페인에 대한 설명을 줄이세요. |
| 리뷰 또는 피드백 요약 | 긍정, 중립, 부정과 같은 감정 점수를 할당하거나 "대부분의 고객이 착용감이 좋다고 언급하지만 배송이 느리다는 점에 유의하세요"와 같은 짧은 텍스트 요약을 작성하는 등 감정이나 피드백을 새로운 필드에 요약하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 상담원 만들기

커스텀 상담원을 만들려면 다음과 같이 하세요:  

1. Braze 대시보드에서 **상담원 콘솔** > **상담원 관리로** 이동합니다.  
2. **상담원 만들기를** 선택합니다.  
3. 팀이 목적을 이해하는 데 도움이 되는 이름과 설명을 입력하세요.
4. 상담원이 사용할 [모델을](#models) 선택합니다.  

![Braze에서 커스텀 상담원을 만들기 위한 상담원 콘솔 인터페이스입니다. 화면에 상담원 이름과 설명을 입력하고 모델을 선택할 수 있는 필드가 표시됩니다.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5\. 상담원에게 지침을 제공합니다. 지침은 [작성 지침을](#writing-instructions) 참조하세요.
6\. [상담원](#testing-your-agent) 출력을 [테스트하고](#testing-your-agent) 필요에 따라 지침을 조정합니다.
7\. 준비가 완료되면 상담원 **생성을** 선택하여 상담원을 활성화합니다. 

이제 에이전트를 사용할 준비가 되었습니다! 자세한 내용은 [상담원 배포하기를]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/) 참조하세요.

## 모델

상담원을 설정할 때 응답을 생성하는 데 사용하는 모델을 선택할 수 있습니다. 두 가지 옵션이 있습니다: Braze 기반 모델을 사용하거나 자체 API 키를 가져오는 것입니다.

{% alert important %}
Braze 기반 **자동** 모델을 사용할 경우, 카탈로그 검색 및 사용자 세그먼트화 멤버십과 같은 작업을 수행하기에 충분한 사고 능력을 가진 모델에 최적화했습니다. 다른 모델을 사용하는 경우 사용 사례에 적합한 모델인지 테스트를 통해 확인하는 것이 좋습니다. 속도와 기능이 다른 모델에 다양한 수준의 세부 사항이나 단계별 사고를 제공하도록 [지침을](#writing-instructions) 조정해야 할 수도 있습니다.
{% endalert %}

### Option 1: Braze 구동 모델 사용

이 옵션은 별도의 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대규모 언어 모델(LLM)에 직접 액세스할 수 있습니다. 이 옵션을 사용하려면 Gemini 모델을 사용하는 **자동을** 선택합니다.

### Option 2: API 키 가져오기

이 옵션을 사용하면 OpenAI, Anthropic, AWS Bedrock 또는 Google Gemini와 같은 제공업체에 Braze 계정을 연결할 수 있습니다. LLM 제공업체에서 API 키를 가져오는 경우 토큰 비용은 Braze가 아닌 제공업체를 통해 직접 청구됩니다.

{% alert important %}
레거시 모델은 몇 달 후에 단종되거나 사용되지 않을 수 있으므로 최신 모델을 정기적으로 테스트하는 것이 좋습니다.
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
7. 추론을 장려합니다("큰 소리로 생각한 다음 대답하기").
8. 파일럿, 검사 및 반복. 작은 조정이 큰 품질 향상으로 이어질 수 있습니다.
9. 가장자리 케이스 처리, 가드레일 추가, 거부 지침 추가.
10. 재사용 및 확장을 위해 내부적으로 어떤 것이 효과적인지 측정하고 설명서를 작성하세요.

상담원이 구문 분석할 수 없는 응답을 수신할 경우 기본값을 포괄 응답으로 포함하는 것도 좋습니다. 이 오류 처리를 통해 상담원이 알 수 없는 결과 변수를 알려줄 수 있습니다. 예를 들어 상담원에게 '긍정' 또는 '부정' 감정 값만 요청하는 대신 결정할 수 없는 경우 '잘 모르겠다'를 반환하도록 요청하세요.

### 간단한 프롬프트

이 예제 프롬프트는 설문조사 입력을 받아 간단한 감성 분석을 출력합니다:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
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

### 출력 형식

**출력 형식** 필드를 사용하여 필드를 수동으로 구조화하거나 JSON을 사용하여 상담원의 출력을 구성하고 정의할 수 있습니다. 

- **Fields:** 일관되게 사용할 수 있는 코드 없이 상담원 출력을 적용하는 방법입니다. 
- **JSON:** JSON 스키마 내에서 변수와 객체를 중첩할 수 있는 정확한 출력 형식을 만들기 위한 코드 접근 방식입니다.

#### 필드

응답자가 레스토랑의 최신 아이스크림 맛을 추천할 가능성이 얼마나 되는지 알아보기 위해 간단한 피드백 설문조사에 응답 형식을 지정한다고 가정해 보겠습니다. 다음 필드를 설정하여 출력 형식을 구성할 수 있습니다:

| 필드 이름 | 값
| --- | --- |
| **likelihood_score** | 숫자 |
| **설명** | 텍스트 |
| **confidence_score** | 숫자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![상담원 콘솔에 가능성 점수, 설명 및 신뢰도 점수에 대한 세 가지 출력 필드가 표시됩니다.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### JSON 스키마

레스토랑 체인에서 가장 최근의 식사 경험에 대한 사용자 피드백을 수집하고 싶다고 가정해 보겠습니다. 출력 형식으로 **JSON 스키마를** 선택하고 다음 JSON을 삽입하여 감성 변수 및 추론 변수를 포함하는 데이터 객체를 반환할 수 있습니다.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

카탈로그에서 JSON 출력이 있는 에이전트를 사용하려고 하면 스키마를 따르지 않습니다. 대신 [정의된 출력 필드를](#fields) 사용하는 것이 좋습니다.

{% alert important %}
출력 형식은 현재 Claude AI에서 지원되지 않습니다. 인간 키를 사용하는 경우에는 상담원 프롬프트에 구조를 수동으로 추가하는 것이 좋습니다.
{% endalert %}

## 선택적 설정

### 브랜드 가이드라인

상담원이 응답할 때 준수할 [브랜드 가이드라인을]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) 선택할 수 있습니다. 예를 들어 상담원이 사용자에게 헬스장 멤버십 가입을 유도하는 SMS 문구를 생성하도록 하려면 이 필드를 사용하여 미리 정의한 굵은 글씨로 동기 부여를 위한 가이드라인을 참조할 수 있습니다.

### 카탈로그

상담원이 참조할 특정 카탈로그를 선택하여 관련성이 있는 경우 상담원에게 제품 및 기타 비사용자 데이터를 이해하는 데 필요한 컨텍스트를 제공하세요.

![상담원이 검색할 '레스토랑' 카탈로그 및 "Loyalty_Program" 열이 선택되어 있습니다.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### 세그먼트 멤버십 컨텍스트 세분화

캔버스에서 에이전트를 사용할 때 에이전트가 각 사용자의 세그먼트 멤버십을 상호 참조할 수 있도록 최대 3개의 세그먼트를 선택할 수 있습니다. 상담원이 "로열티 사용자" 세그먼트에 대해 세그먼트 멤버십이 선택되어 있고 그 상담원이 캔버스에서 사용된다고 가정해 보겠습니다. 사용자가 상담원 단계를 입력하면 상담원은 각 사용자가 상담원 콘솔에서 지정한 각 세그먼트의 멤버인지 상호 참조하여 각 사용자의 멤버십(또는 비멤버십)을 LLM의 컨텍스트로 사용할 수 있습니다.

![상담원 멤버십 액세스 권한을 위해 선택한 "로열티 사용자" 세그먼트입니다.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### 온도

에이전트를 사용하여 사용자가 모바일 앱에 로그인하도록 유도하는 문구를 생성하는 것이 목표라면 에이전트가 더 창의적으로 문맥 변수의 미묘한 차이를 활용할 수 있도록 더 높은 온도를 설정할 수 있습니다. 상담원을 사용하여 감정 점수를 생성하는 경우에는 상담원이 부정적인 설문조사 응답을 추측하지 않도록 온도를 낮게 설정하는 것이 이상적일 수 있습니다. 이 설정을 테스트하고 시나리오에 맞게 상담원이 생성한 출력을 검토하는 것이 좋습니다.

{% alert note %}
현재 OpenAI에서는 온도가 지원되지 않습니다.
{% endalert %}

## 에이전트를 테스트하세요.

**라이브 프리뷰** 창은 구성 환경 내에서 나란히 있는 패널로 표시되는 상담원의 인스턴스입니다. 에이전트를 만들거나 업데이트하는 동안 이를 사용하여 최종 사용자와 유사한 방식으로 에이전트를 테스트할 수 있습니다. 이 단계를 통해 예상한 대로 작동하는지 확인할 수 있으며, 라이브를 시작하기 전에 미세 조정할 수 있습니다.

![커스텀 상담원을 테스트하기 위한 라이브 프리뷰 창이 표시된 상담원 콘솔. 인터페이스에는 예시 고객 데이터가 있는 샘플 입력 필드, 테스트 실행 버튼, 상담원 출력이 표시되는 응답 영역이 표시됩니다.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. **샘플 입력** 필드에 상담원이 처리할 실제 시나리오를 반영하는 고객 데이터나 고객 응답의 예시를 입력합니다. 
2. **테스트 실행을** 선택합니다. 에이전트는 구성에 따라 실행되고 응답을 표시합니다. 테스트 실행은 일일 실행 한도에 포함됩니다.

비판적인 시각으로 결과물을 검토하세요. 다음 질문을 고려하세요:

- 카피가 브랜드에 어울리는 느낌인가요? 
- 의사 결정 로직이 의도한 대로 고객을 라우팅하나요? 
- 계산된 값이 정확한가요? 

뭔가 이상하다고 느껴지면 상담원의 구성을 업데이트하고 다시 테스트하세요. 몇 가지 다른 입력을 실행하여 에이전트가 여러 시나리오, 특히 데이터가 없거나 잘못된 응답과 같은 엣지 케이스에 어떻게 적응하는지 확인하세요.

### 상담원 모니터링

상담원의 **로그** 탭에서 캔버스 및 카탈로그에서 발생하는 실제 상담원 통화를 모니터링할 수 있습니다. 날짜 범위, 결과(성공 또는 실패) 또는 통화 위치 등의 정보로 필터링할 수 있습니다.

![상담원 무작위 스포츠 배정 로그(상담원이 언제 어디서 전화를 받았는지 포함)에 대한 로그입니다.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

특정 상담원 통화에 대한 **보기를** 선택하여 입력, 출력 및 사용자 ID를 확인합니다.

![에이전트 도시 트렌드 및 추천 예약에 대한 로그입니다. 세부정보 패널에는 입력 프롬프트, 출력 응답 및 연결된 사용자 ID가 표시됩니다.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
