# Braze MCP 서버

> 안전한 읽기 전용 연결로 Claude, Cursor와 같은 AI 도구가 데이터를 변경하지 않고도 질문에 답하고, 트렌드를 분석하고, 인사이트를 제공할 수 있도록 해주는 Braze MCP 서버에 대해 알아보세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 모델 컨텍스트 프로토콜(MCP)이란 무엇인가요?

​모델 컨텍스트 프로토콜(MCP)은 AI 에이전트가 다른 플랫폼의 데이터에 연결하여 작업할 수 있도록 하는 표준입니다. 크게 두 부분으로 구성되어 있습니다:

- **MCP 클라이언트:** AI 에이전트가 실행되는 애플리케이션(예: 커서 또는 클로드).
- **MCP 서버:** AI가 사용할 수 있는 도구와 액세스할 수 있는 데이터를 정의하는 Braze와 같은 다른 플랫폼에서 제공하는 서비스입니다.

## Braze MCP 서버 정보

Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, 에이전트, 어시스턴트, 챗봇과 같은 AI 툴을 Braze에 직접 연결하여 캔버스 및 캠페인 분석, 커스텀 속성, 세그먼트 등과 같은 집계된 데이터를 읽을 수 있도록 할 수 있습니다. Braze MCP 서버는 다음과 같은 용도에 적합합니다:

- Braze 컨텍스트가 필요한 AI 기반 도구 구축.
- 다단계 상담원 워크플로우를 만드는 CRM 엔지니어링.
- 자연어 쿼리를 실험하는 기술 마케팅 담당자.

Braze MCP 서버는 Braze 사용자 프로필에서 데이터를 반환하지 않는 38개의 읽기 전용 엔드포인트를 지원합니다. 이러한 엔드포인트 중 일부만 Braze API 키에 할당하도록 선택하여 상담원이 액세스할 수 있는 데이터를 더욱 제한할 수 있습니다.

{% alert warning %}
API 키에 읽기 전용이 **아닌** 권한을 할당하지 마세요. 상담원이 Braze에서 데이터를 쓰거나 삭제하려고 시도하면 의도하지 않은 결과가 발생할 수 있습니다.
{% endalert %}

## 사용 예

클로드나 커서와 같은 도구를 사용하여 자연어를 통해 Braze와 상호작용할 수 있습니다. 다른 예제 및 모범 사례는 [Braze MCP 서버 사용]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?"라는 질문에 대한 답변이 Claude에서 이루어지고 있습니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab 커서 %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가'를 묻고 답하는 커서 (]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## 자주 묻는 질문(FAQ) {#faq}

### 어떤 MCP 클라이언트가 지원되나요?

현재는 [클로드와](https://claude.ai/) [커런츠만](https://cursor.com/) 공식적으로 지원됩니다. 이러한 클라이언트 중 하나에 대한 계정이 있어야 Braze MCP 서버를 사용할 수 있습니다.

### MCP 클라이언트는 어떤 Braze 데이터에 액세스할 수 있나요?

MCP 클라이언트는 PII를 검색하도록 구축되지 않은 읽기 전용 엔드포인트에만 액세스할 수 있습니다. 이들은 Braze에서 데이터를 조작할 수 없습니다.

### MCP 클라이언트가 Braze 데이터를 조작할 수 있나요?

아니요. MCP 서버는 PII가 아닌 읽기 전용 데이터를 처리하는 도구만 노출합니다.

### Braze에 타사 MCP 서버를 사용할 수 있나요?

Braze 데이터에 서드파티 MCP 서버를 사용하는 것은 권장하지 않습니다. [PyPi에서](https://pypi.org/project/braze-mcp-server/) 호스팅되는 공식 Braze MCP 서버만 사용하세요.

### Braze MCP 서버가 PII 또는 쓰기 권한을 제공하지 않는 이유는 무엇인가요?

데이터를 보호하는 동시에 혁신을 인에이블먼트하기 위해 일반적으로 PII를 반환하지 않는 읽기 전용 엔드포인트로 제한되도록 서버를 구축했습니다. 이렇게 하면 위험을 줄이면서 가치 있는 사용 사례를 지원할 수 있습니다.

### API 키를 재사용할 수 있나요?

아니요. MCP 클라이언트에 대한 새 API 키를 만들어야 합니다. AI 도구에는 사용자에게 익숙한 권한만 부여하고 높은 수준의 권한은 피하세요.

### Braze MCP 서버는 로컬로 호스팅되나요, 아니면 원격으로 호스팅되나요?

현재 Braze 커런츠 서버는 현지에서 호스팅되고 있습니다.

### 커서가 함수만 나열하는 이유는 무엇인가요?

질문 모드인지 상담원 모드인지 확인하세요. MCP 서버를 사용하려면 상담원 모드에 있어야 합니다.

### 상담원이 잘못된 답변을 반환하면 어떻게 해야 하나요?

커서와 같은 도구로 작업할 때는 사용하는 모델을 변경해 볼 수 있습니다. 예를 들어 자동으로 설정한 경우 특정 모델로 변경하고 사용 사례에 가장 적합한 성능/성과를 내는 모델을 찾기 위해 실험해 보세요. 새 채팅을 시작하고 프롬프트를 다시 시도해 볼 수도 있습니다. 

문제가 지속되면 [mcp-product@braze.com](mailto:mcp-product@braze.com) 으로 이메일을 보내 알려주세요. 가능하면 상담원이 어떤 통화를 시도했는지 확인할 수 있도록 동영상을 포함하고 통화 기능을 확장하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
