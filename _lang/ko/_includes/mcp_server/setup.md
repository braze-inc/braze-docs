# Braze MCP 서버 설정하기

> Braze 데이터와 상호작용할 수 있도록 Braze MCP 서버를 설정하는 방법을 배우세요. Claude 및 Cursor와 같은 도구를 사용하여 자연어로 상호작용할 수 있습니다. 더 일반적인 정보는 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}을 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건

Before you start, you'll need the following:

| Prerequisite | 설명 |
|--------------|-------------|
| Braze API 키 | 필요한 권한이 있는 Braze API 키입니다. Braze MCP 서버를 [설정할 때](#create-api-key) 새 키를 생성합니다. |
| MCP 클라이언트 | [Claude](https://claude.ai/), [Cursor](https://cursor.com/), 및 [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli)가 공식적으로 지원됩니다. Braze MCP 서버를 사용하려면 이러한 클라이언트 중 하나에 대한 계정이 있어야 합니다. |
| 터미널 | 명령을 실행하고 도구를 설치할 수 있는 터미널 앱입니다. 선호하는 터미널 앱이나 컴퓨터에 미리 설치된 앱을 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Braze MCP 서버 설정하기

### 1단계: 설치 `uv`

먼저, `uv`—의존성 관리 및 Python 패키지 처리를 위한 [명령줄 도구 by Astral](https://docs.astral.sh/uv/getting-started/installation/)를 설치하세요.

{% tabs local %}
{% tab MacOS and Linux %}
터미널 애플리케이션을 열고, 다음 명령을 붙여넣은 후 <kbd>Enter</kbd>를 누르세요.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

출력은 다음과 유사합니다:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Windows PowerShell을 열고, 다음 명령을 붙여넣은 후 <kbd>Enter</kbd>를 누르세요.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

출력은 다음과 유사합니다:

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### 2단계: API 키 생성 {#create-api-key}

Braze MCP 서버는 Braze 사용자 프로필에서 데이터를 반환하지 않는 38개의 읽기 전용 엔드포인트를 지원합니다. **설정** > **API 및 식별자** > **API 키**로 이동하여 다음 권한 중 일부 또는 모두를 가진 새 키를 생성하세요.

{% details List of read-only, non-PII permissions %}
#### 캠페인

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 카탈로그

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 클라우드 데이터 수집

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 콘텐츠 블록

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Custom Attributes

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Events

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPI

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Messages

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 환경설정 센터

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Purchases

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 세그먼트

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Sends

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### 세션

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### SDK 인증 키

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 구독

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Templates

| Endpoint | 필수 권한 |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
기존 API 키를 재사용하지 마십시오. MCP 클라이언트 전용으로 하나를 생성하십시오. 또한, 에이전트가 Braze에서 데이터를 쓰거나 삭제하려고 할 수 있으므로 읽기 전용 비PII 권한만 부여하십시오.
{% endalert %}

### 3단계: 식별자 및 엔드포인트 가져오기

MCP 클라이언트를 구성할 때 API 키의 식별자와 작업 공간의 REST 엔드포인트가 필요합니다. 이 세부정보를 얻으려면 대시보드의 **API 키** 페이지로 돌아가십시오. 이 페이지를 열어 두어 [다음 단계](#configure-client) 동안 참조할 수 있습니다.

![Braze의 'API 키'에서 새로 생성된 API 키와 사용자의 REST 엔드포인트를 보여줍니다.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### 4단계: MCP 클라이언트 구성 {#configure-client}

미리 제공된 구성 파일을 사용하여 MCP 클라이언트를 구성하십시오.

{% tabs %}
{% tab Claude %}
[Claude Desktop](https://claude.ai/download) 커넥터 디렉토리를 사용하여 MCP 서버를 설정하십시오. 

1. Claude Desktop에서 **설정** > **커넥터** > **커넥터 찾아보기** > **데스크탑 확장** > **Braze MCP 서버** > **설치**로 이동하십시오.
2. API 키와 기본 URL을 입력하십시오.
3. 구성을 저장하고 Claude Desktop을 재시작하십시오.

{% endtab %}

{% tab Cursor %}
[커서](https://cursor.com/)에서 **설정** > **도구 및 통합** > **MCP 도구** > **사용자 정의 MCP 추가**로 이동한 다음 다음 스니펫을 추가하십시오:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

`key-identifier`과 `rest-endpoint`를 Braze의 **API 키** 페이지에서 해당 값으로 교체하십시오. 구성이 다음과 유사해야 합니다:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

작업이 끝나면 구성을 저장하고 커서를 재시작하십시오.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI는 `~/.gemini/settings.json`에서 사용자 설정을 읽습니다. 이것이 존재하지 않으면 터미널에서 다음을 실행하여 생성할 수 있습니다:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

다음으로, 터미널 프롬프트에서 `@BZXXXXXXXX` 앞의 정확한 문자열로 `yourname`을(를) 교체하십시오. 그런 다음, Braze의 **API 키** 페이지에서 해당 값을 사용하여 `key-identifier`과 `rest-endpoint`를 교체하십시오. 

구성이 다음과 유사해야 합니다:

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

작업이 끝나면 구성을 저장하고 Gemini CLI를 재시작하십시오. 그런 다음, Gemini에서 Braze MCP 서버가 나열되어 있고 도구와 스키마가 사용 가능하다는 것을 확인하기 위해 다음 명령을 실행하십시오:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

사용 가능한 도구와 스키마가 있는 `braze` 서버가 나열되어야 합니다.

{% endtab %}
{% endtabs %}

### 5단계: 테스트 프롬프트 보내기

Braze MCP 서버를 설정한 후, MCP 클라이언트에 테스트 프롬프트를 보내보십시오. 기타 예제 및 모범 사례는 [Braze MCP 서버 사용하기]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}를 참조하십시오.

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'가 Claude에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'가 Cursor에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![내가 사용할 수 있는 Braze 기능은 무엇인가요?가 Gemini CLI에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## 문제 해결

### 터미널 오류

#### `uvx` 명령을 찾을 수 없습니다

`uvx` 명령을 찾을 수 없다는 오류가 발생하면 `uv`를 재설치하고 터미널을 재시작하십시오.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` 오류

`spawn uvx ENOENT` 오류가 발생하면 클라이언트의 구성 파일에서 파일 경로를 업데이트해야 할 수 있습니다. 먼저, 터미널을 열고 다음 명령을 실행하십시오:

```bash
which uvx
```

명령은 다음과 유사한 메시지를 반환해야 합니다:

```bash
/Users/alex-lee/.local/bin/uvx
```

메시지를 클립보드에 복사하고 [클라이언트의 구성 파일](#configure-client)을(를) 엽니다. `"command": "uvx"`를 복사한 경로로 교체한 후, 클라이언트를 재시작하십시오. For example:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### 패키지 설치가 실패합니다

패키지 설치가 실패하면 특정 Python 버전을 대신 설치해 보십시오.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### 클라이언트 구성

#### MCP 클라이언트가 Braze 서버를 찾을 수 없습니다

1. MCP 클라이언트 구성 구문이 올바른지 확인하십시오.
2. 구성 변경 후 MCP 클라이언트를 다시 시작하십시오.
3. `uvx`이(가) 시스템 `PATH`에 있는지 확인하십시오.

#### 인증 오류

1. `BRAZE_API_KEY`이(가) 올바르고 활성 상태인지 확인하십시오.
2. `BRAZE_BASE_URL`이(가) Braze 인스턴스와 일치하는지 확인하십시오.
3. API 키에 [올바른 권한](#create-api-key)이 있는지 확인하십시오.

#### 연결 시간 초과 또는 네트워크 오류

1. `BRAZE_BASE_URL`이(가) 인스턴스에 대해 올바른지 확인하십시오.
2. 네트워크 연결 및 방화벽 설정을 확인하십시오.
3. 기본 URL에서 HTTPS를 사용하고 있는지 확인하십시오.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
