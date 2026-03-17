---
nav_title: LLM으로 구축하기
article_title: LLM을 활용한 구축
page_order: 4
description: "Braze 설명서를 통해 AI 코딩 어시스턴트 사용법을 익히고 SDK 통합 워크플로우를 가속화하세요."
platform:
  - Web
  - React Native
---

# LLM을 활용한 구축

> AI 코딩 어시스턴트를 활용하여 Braze 통합 워크플로우를 가속화하세요. Context7을 통해 IDE를 Braze Docs MCP 서버에 연결하고, 개발 환경 내에서 정확하고 최신 소프트웨어 개발 키트 가이드를 직접 확인하세요.

AI 코딩 어시스턴트는 통합 코드 작성, 문제 해결, Braze 소프트웨어 개발 키트 기능 탐색을 도와줄 수 있습니다. 단, 올바른 컨텍스트를 제공할 때에만 가능합니다. Braze Docs MCP 서버는 AI 어시스턴트에 Braze 설명서에 대한 직접적인 접근 권한을 제공하여, 최신 소프트웨어 개발 키트 참조 자료를 기반으로 정확한 코드 스니펫을 생성하고 기술적 질문에 답변할 수 있도록 합니다.

## Braze 문서 MCP에 연결하기

[Context7은](https://context7.com/braze-inc/braze-docs) AI 어시스턴트와 Braze 설명서 라이브러리 사이의 가교 역할을 합니다. IDE의 MCP 구성에 Context7을 추가하면 AI 어시스턴트가 전체 Braze 설명서를 조회하여 관련 소프트웨어 개발 키트 참조 자료, 코드 예제 및 통합 가이드를 필요할 때마다 즉시 검색할 수 있습니다.

### Context7 설정하기

Context7을 통해 AI 어시스턴트를 Braze 문서 MCP에 연결하려면 IDE의`mcp.json`  파일에 다음 구성을 추가하십시오.

{% tabs %}
{% tab Cursor %}
[커서](https://cursor.com/)에서 **설정** > **도구 및 통합** > **MCP 도구** > **커스텀 MCP 추가로** 이동한 후 다음 스니펫을 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

설정을 저장하고 커서를 다시 시작하십시오. AI 어시스턴트(AI assistant)는 프롬프트에  `use context7`를 포함하면 Context7을 통해 Braze 설명서를 참조할 수 있습니다.
{% endtab %}

{% tab Claude %}
Claude Desktop에서 **설정** > **개발자** > **구성 편집**으로 이동한 후, 다음 내용을 파일에`claude_desktop_config.json` 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

설정을 저장하고 Claude Desktop을 다시 시작하십시오.
{% endtab %}

{% tab VS Code %}
다음 내용을 VS Code의`settings.json`  또는`.vscode/mcp.json`  파일에 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

설정을 저장하고 VS Code를 다시 시작하세요.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7은 [Braze MCP 서버]({{site.baseurl}}/developer_guide/mcp_server/)와 다릅니다. Context7은 AI 어시스턴트에게 **Braze 설명서에** 대한 접근 권한을 제공하며, Braze MCP 서버는 캠페인, 세그먼트, 분석과 같은 **Braze 워크스페이스 데이터에** 대한 읽기 전용 접근 권한을 제공합니다. 두 가지를 함께 사용하면 보다 완벽한 AI 지원 개발 환경을 경험할 수 있습니다.
{% endalert %}

## Braze 소프트웨어 개발 키트를 위한 작성 프롬프트

Context7을 설정한 후, 프롬프트에  를 `use context7`포함시켜 AI 어시스턴트가 Braze 설명서를 컨텍스트로 불러오도록 지시하세요. 다음 예시는 일반적인 소프트웨어 개발 키트 작업에 효과적인 프롬프트를 작성하는 방법을 보여줍니다.

### 리액트 네이티브 SDK

이 프롬프트는 [Braze React Native 소프트웨어]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) [개발]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) 키트의 일반적인 통합 작업을 보여줍니다.

#### 소프트웨어 개발 키트 초기화

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### 커스텀 이벤트 로깅에서 속성을 가진 이벤트 로깅

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### 푸시 알림 설정

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### 인앱 메시지 처리

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### 웹 SDK

이 프롬프트는 [Braze 웹 SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)의 일반적인 통합 작업을 보여줍니다.

#### 소프트웨어 개발 키트 초기화

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### 커스텀 이벤트 및 구매 추적

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### 웹 푸시 등록

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### 사용자 속성 관리

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## 일반 텍스트 설명서

Braze 개발자 설명서는 AI 도구 및 대규모 언어 모델(LLM)에 최적화된 일반 텍스트 파일로 이용할 수 있습니다. 이 파일들은 HTML 렌더링의 부담 없이 AI 어시스턴트가 구문 분석하고 이해할 수 있는 형식으로 Braze 설명서를 제공합니다.

| 파일 | 설명 |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | Braze 개발자 설명서의 제목과 설명을 포함한 색인 사용 가능한 설명서를 찾기 위한 출발점으로 이 내용을 활용하십시오. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | 단일 일반 텍스트 파일로 제공되는 완전한 Braze 개발자 설명서로, LLM(대규모 언어 모델)이 소비할 수 있도록 포맷팅되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

이 파일들은 AI 도구가 접근할 수 있도록 설명서를 만드는 새로운 표준인 [llms.txt](https://llmstxt.org/)표준을 따릅니다. 이러한 파일들을 프롬프트에서 직접 참조하거나, 내용을 LLM에 붙여넣어 컨텍스트로 활용할 수 있습니다.
