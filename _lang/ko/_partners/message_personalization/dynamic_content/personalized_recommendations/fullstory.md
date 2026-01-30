---
nav_title: 전체 스토리
article_title: 전체 스토리
description: "이 참고 문서에서는 Braze와 풀스토리의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# 전체 스토리

풀스토리의 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 의사 결정을 내릴 수 있도록 지원합니다. 풀스토리의 특허 기술은 디지털 행동 데이터를 분석 스택에 주입하여 양질의 행동 데이터를 대규모로 활용함으로써 모든 디지털 방문을 유용한 인사이트로 전환합니다. 

*이 통합은 풀스토리에서 유지 관리합니다.*

## 이 통합 정보
Braze에서 풀스토리 인사이트를 활용하여 사용자의 웹사이트 또는 앱 경험을 순간순간 사진으로 구축하여 하이퍼컨텍스트 메시징을 전달할 수 있습니다. 풀스토리의 세션 요약 API를 사용하면 사용자의 브라우징 행동에 대한 자세한 메타데이터를 캡처하여 Braze 메시징에 사용할 수 있으며, 이는 특히 캔버스와 같은 다단계 메시징 여정에서 활용할 때 강력하게 활용될 수 있습니다. 

풀스토리의 세션 요약 데이터의 실시간 가치는 연결된 콘텐츠를 통해 가장 잘 활용됩니다. 캔버스 컨텍스트 단계에서 연결된 콘텐츠를 사용하면 사용자의 캔버스 여정 전반에 걸쳐 풀스토리의 데이터를 저장하여 이후의 모든 캔버스 단계에서 사용할 수 있습니다. 이렇게 하면 커스텀 이벤트 및 속성을 통해 이 데이터를 Braze 고객 프로필에 쓸 필요가 없습니다. 

다음 예시에서는 캔버스 컨텍스트 데이터를 에이전트 AI 캔버스 단계에서 활용하여 사용자가 유기한 장바구니를 다시 집어들도록 유도하는 최적의 메시지를 생성합니다. 그러나 데이터를 활용하여 메시지를 직접 개인화하거나, 오디언스 경로를 통해 사용자의 여정을 파악하거나, 후속 메시징 단계에서 사용되는 카피 또는 자산을 결정할 수 있습니다.

## 사용 사례

![Braze와의 풀스토리 통합 사용 사례를 보여주는 다이어그램]({% image_buster /assets/img/fullstory/1.png %})

## 필수 조건

시작하기 전에 다음이 필요합니다:

|Requirement     | 설명 |                        
|-----------------------|-----------------|
| 풀스토리 세션 API 인증 토큰   | 아래 1단계를 참조하세요.  | 
| Braze 커넥티드 콘텐츠 인증 토큰 인에이블먼트 | 얼리 액세스에 대한 아래 참고 사항을 참조하세요. |
| Braze 캔버스 컨텍스트 단계 |얼리 액세스에 대한 아래 참고 사항을 참조하세요. |
| 인에이블된 Braze AI 에이전트 단계 | 얼리 액세스에 대한 아래 참고 사항을 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## 풀스토리 통합하기

### 1단계: 세션 요약 API 인에이블먼트를 위한 풀스토리 설정하기

#### A: 세션 요약 API 엔드포인트에 대한 [인증 토큰](https://developer.fullstory.com/server/authentication/) 가져오기

풀스토리 API 키를 만들려면 풀스토리 플랫폼으로 이동한 다음 **설정** > **API 키로** 이동합니다. **표준** 권한 수준을 선택하고 키 값은 한 번만 표시되므로 즉시 복사합니다.

#### B: 세션 요약 프로필 ID 생성하기

[풀스토리의 안내에](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles) 따라 전용 엔드포인트를 사용하여 세션 요약 프로필을 만듭니다. 여기에서 세션 요약 응답이 Braze에 제공할 데이터의 종류를 정의할 수 있습니다.
이 요청에 대한 응답으로 풀스토리는 세션 "프로필 ID"를 제공합니다. 이 프로필 ID는 다음 사용 사례에서 사용되는 연결된 콘텐츠 요청 본문의 핵심 구성 요소입니다.


### 2단계: 연결된 콘텐츠 토큰 인증 만들기
1. Braze에서 **설정 > 워크스페이스 설정 > 연결된 콘텐츠 > 자격 증명 추가 > 토큰 인증으로** 이동합니다. 

2. 인증의 이름을 "fullstory"로 지정합니다.

3. 헤더 키 "Authorization"을 추가합니다. 이전 단계에서 제공한 헤더 값 풀스토리를 입력합니다. 

4. 허용된 도메인 아래에 "api.fullstory.com"를 제출합니다.

![자격 증명 편집 필드를 보여주는 Braze 스크린샷]({% image_buster /assets/img/fullstory/2.png %})

## Use case: 풀스토리 세션 요약 데이터와 Braze 캔버스 컨텍스트 단계 및 AI 에이전트를 활용하여 동적 메시지 여정을 생성합니다.

풀스토리의 [활성화 스트림을](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) 사용하면 주요 사용자 인터랙션 직후에 Braze 캔버스를 트리거할 수 있습니다. 이 통합의 힘은 고유한 `client_session_id` ( {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %})을 통해 액세스할 수 있으며, 시스템이 Fullstory에서 Braze로 자동으로 전달합니다. 이 ID는 키 역할을 하여 Braze가 사용자가 경험한 전체 세션 요약을 정확하게 가져올 수 있도록 합니다. 

캔버스 컨텍스트 단계와 연결된 콘텐츠를 활용하면 이 ID를 사용하여 풀스토리에 API를 요청하고 세션 데이터를 검색하여 나중에 여정에서 사용할 수 있도록 변수로 저장할 수 있습니다. 

![세션 요약을 검색하기 위해 컨텍스트 변수 `summary_result` 가 생성되고 연결된 콘텐츠로 채워져 풀스토리로 호출되는 것을 보여주는 Braze 캔버스 컨텍스트 단계의 스크린샷입니다.]({% image_buster /assets/img/fullstory/3.png %})

앞서 만든 권한 부여 토큰을 사용하여 다음 요청 구조를 사용하여 세션 요약 데이터를 가져옵니다. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 응답은 Liquid 태그로 저장됩니다 {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. 이후 캔버스 단계에서 이 컨텍스트 태그를 사용합니다.
{% endalert %}

이 단계에서 캔버스는 사용자 세션에 대한 전체 메시지 페이로드가 포함된 연결된 콘텐츠 호출에 대한 응답에 액세스할 수 있습니다.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

나중에 사용자의 캔버스 여정에서 컨텍스트 Liquid 태그를 사용하여 위의 개체에서 사용 가능한 모든 데이터를 활용할 수 있습니다. 다음 단계는 [AI 에이전트](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step) 캔버스 단계에서 이 데이터를 사용하는 방법을 보여줍니다.

{% alert Note %}
예기치 않은 동작을 방지하려면 컨텍스트 단계 뒤에 오디언스 경로 단계를 포함하면 컨텍스트 태그가 비어 있어 연결된 콘텐츠 호출이 실패했거나 정보가 반환되지 않았음을 나타내는 경우 사용자를 컨텍스트에서 제외할 수 있습니다.

![Braze 오디언스 단계 스크린샷]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## 풀스토리의 페이로드를 분석하고 사용 사례에 적합한 카피를 생성할 수 있는 AI 에이전트를 생성하세요.

[Braze의 에이전트 가이드는]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) 사용자가 AI 에이전트를 만드는 방법을 간략하게 설명합니다. 풀스토리가 트리거한 캔버스에 AI 에이전트 단계를 삽입하고 위에서 설명한 캔버스 컨텍스트 단계를 포함하면, 사용자는 다양한 용도로 AI 에이전트 풀스토리의 세션 요약 데이터를 제공할 수 있습니다. 

이 예제에서는 이 데이터를 사용하여 AI 에이전트가 콘텐츠 카드에 사용할 적절한 메시지 카피를 생성하여 사용자가 버려진 장바구니로 돌아오도록 유도할 수 있도록 합니다.

![프롬프트가 표시된 Braze 에이전트 컨텍스트 크리에이터 스크린샷]({% image_buster /assets/img/fullstory/4.png %})

이 단계에서 만든 컨텍스트 Liquid 태그의 이름은 앞서 만든 AI 에이전트 단계에서 사용한 컨텍스트 Liquid 태그와 동일한 이름을 사용합니다. 

사용 사례에 따라 필요한 프롬프트는 다르지만 효과적인 상담원 프롬프트를 만들기 위한 모범 사례는 상담원 *만들기에서* [작성 지침을]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) 참조하세요. 


캔버스에서 AI 에이전트 단계를 선택한 다음 드롭다운 메뉴에서 생성된 '세션 컨텍스트' 에이전트를 선택합니다. 출력을 변수(이 경우 "메시지")로 저장하고, Liquid 태그를 사용하여 메시지 사본에 배치할 수 있습니다 {% raw %}`{{context.${message}.message}}`{% endraw %}.

![프롬프트와 함께 Braze 에이전트 컨텍스트 캔버스 단계 스크린샷]({% image_buster /assets/img/fullstory/5.png %})

AI 에이전트가 만든 사본을 활용하는 메시지 단계를 만듭니다. 이 단계에서 Liquid 태그를 사용합니다. 

{% alert Note %}

풀스토리의 세션 요약 API는 민감한 식별 가능한 사용자 데이터를 반환할 수 있습니다. PII(개인 식별 정보)를 처리하는 동안 규정 준수를 보장하려면 이 사용 사례를 활용하기 전에 풀스토리 데이터 캡처 규칙에 PII가 제외되어 있는지 확인하세요.

{% endalert %}