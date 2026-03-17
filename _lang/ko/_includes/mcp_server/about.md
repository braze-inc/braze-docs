# 브레이즈 MCP 서버

> 브레이즈 MCP 서버에 대해 알아보세요. 이는 Claude 및 Cursor와 같은 AI 도구가 비PII 브레이즈 데이터에 접근하여 질문에 답하고, 트렌드를 분석하며, 데이터를 변경하지 않고 통찰력을 제공할 수 있는 안전한 읽기 전용 연결입니다.

{% multi_lang_include mcp_server/beta_alert.md %}

## 모델 컨텍스트 프로토콜(MCP)이란?

​모델 컨텍스트 프로토콜 또는 MCP는 AI 에이전트가 다른 플랫폼의 데이터에 연결하고 작업할 수 있도록 하는 표준입니다. 주요 두 가지 부분이 있습니다:

- **MCP 클라이언트:** AI 에이전트가 실행되는 애플리케이션, 예를 들어 Cursor 또는 Claude입니다.
- **MCP 서버:** AI가 사용할 수 있는 도구와 접근할 수 있는 데이터를 정의하는 브레이즈와 같은 다른 플랫폼에서 제공하는 서비스입니다.

## 브레이즈 MCP 서버에 대한 정보

[브레이즈 MCP 서버 설정 후]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, AI 도구인 에이전트, 어시스턴트 및 챗봇을 브레이즈에 직접 연결하여 캔버스 및 캠페인 분석, 커스텀 속성, 세그먼트 등과 같은 집계된 데이터를 읽을 수 있습니다. 브레이즈 MCP 서버는 다음에 적합합니다:

- 브레이즈 컨텍스트가 필요한 AI 기반 도구 구축.
- 다단계 에이전트 워크플로우를 만드는 CRM 엔지니어.
- 자연어 쿼리를 실험하는 기술 마케터.

브레이즈 사용자 프로필에서 데이터를 반환하지 않는 38개의 읽기 전용 엔드포인트를 지원합니다. 에이전트가 접근할 수 있는 데이터를 추가로 제한하기 위해 이러한 엔드포인트 중 일부만 브레이즈 API 키에 할당하도록 선택할 수 있습니다.

{% alert warning %}
API 키에 **읽기 전용이 아닌** 권한을 할당하지 마십시오. 에이전트가 브레이즈에서 데이터를 쓰거나 삭제하려고 시도할 수 있으며, 이는 의도하지 않은 결과를 초래할 수 있습니다.
{% endalert %}

## 사용 예

Braze와 상호작용할 수 있습니다. Claude나 Cursor와 같은 도구를 사용하여 자연어로. 다른 예제와 모범 사례는 [Braze MCP 서버 사용하기]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}를 참조하세요.

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'라는 질문이 Claude에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'라는 질문이 Cursor에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## 자주 묻는 질문(FAQ) {#faq}

### 어떤 MCP 클라이언트가 지원되나요?

오직 [Claude](https://claude.ai/)와 [Cursor](https://cursor.com/)만 공식적으로 지원됩니다. Braze MCP 서버를 사용하려면 이 클라이언트 중 하나에 대한 계정이 있어야 합니다.

### 내 MCP 클라이언트가 어떤 Braze 데이터에 접근할 수 있나요?

MCP 클라이언트는 PII를 검색하기 위해 구축되지 않은 읽기 전용 엔드포인트에만 접근할 수 있습니다. 그들은 Braze의 데이터를 조작할 수 없습니다.

### 내 MCP 클라이언트가 Braze 데이터를 조작할 수 있나요?

아니요. MCP 서버는 비-PII, 읽기 전용 데이터만 처리하는 도구를 노출합니다.

### Braze에 대해 서드파티 MCP 서버를 사용할 수 있나요?

Braze 데이터에 대해 서드파티 MCP 서버를 사용하는 것은 권장되지 않습니다. 오직 [PyPi](https://pypi.org/project/braze-mcp-server/)에 호스팅된 공식 Braze MCP 서버만 사용하세요.

### 왜 Braze MCP 서버는 PII나 쓰기 접근을 제공하지 않나요?

데이터를 보호하면서 혁신을 가능하게 하기 위해, 서버는 읽기 전용이며 일반적으로 PII를 반환하지 않는 엔드포인트로 제한됩니다. 이것은 귀중한 사용 사례를 지원하면서 위험을 줄입니다.

### 내 API 키를 재사용할 수 있나요?

아니요. MCP 클라이언트를 위해 새로운 API 키를 생성해야 합니다. AI 도구에 접근할 수 있는 권한은 자신이 편안하게 느끼는 것만 주고, 높은 권한은 피하세요.

### Braze MCP 서버는 로컬에 호스팅되나요, 아니면 원격에 호스팅되나요?

Braze MCP 서버는 로컬에 호스팅됩니다.

### 왜 Cursor는 함수만 나열하고 있나요?

당신이 ask 모드인지 agent 모드인지 확인하세요. MCP 서버를 사용하려면 agent 모드에 있어야 합니다.

### 에이전트가 잘못된 것처럼 보이는 답변을 반환할 때는 어떻게 해야 하나요?

Cursor와 같은 도구를 사용할 때는 사용 중인 모델을 변경해 보세요. 예를 들어, 자동으로 설정되어 있다면 특정 모델로 변경하고 어떤 모델이 사용 사례에 가장 적합한지 실험해 보세요. 새로운 채팅을 시작하고 프롬프트를 다시 시도해 볼 수도 있습니다. 

문제가 지속되면 [mcp-product@braze.com](mailto:mcp-product@braze.com)로 이메일을 보내 알려주세요. 가능하다면 비디오를 포함하고 호출 함수의 범위를 확장하여 에이전트가 시도한 호출을 볼 수 있도록 해주세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
