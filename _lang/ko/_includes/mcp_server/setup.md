# Braze MCP 서버 설정하기

> Claude 및 Cursor와 같은 도구를 사용하여 자연어를 통해 Braze 데이터와 상호 작용할 수 있도록 Braze MCP 서버를 설정하는 방법을 알아보세요. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건

Before you start, you'll need the following:

| Prerequisite | 설명 |
|--------------|-------------|
| Braze API 키 | 필요한 권한이 있는 Braze API 키입니다. [Braze MCP 서버를 설정할](#create-api-key) 때 새 키를 생성하게 됩니다. |
| MCP 클라이언트 | 현재는 [클로드와](https://claude.ai/) [커런츠만](https://cursor.com/) 공식적으로 지원됩니다. 이러한 클라이언트 중 하나에 대한 계정이 있어야 Braze MCP 서버를 사용할 수 있습니다. |
| 터미널 | 명령을 실행하고 도구를 설치할 수 있는 터미널 앱입니다. 선호하는 터미널 앱 또는 컴퓨터에 사전 설치된 앱을 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Braze MCP 서버 설정하기

### 1단계: 설치 `uv`

먼저, 종속성 관리 및 Python 패키지 처리를 위한 [Astral의 명령줄 툴인](https://docs.astral.sh/uv/getting-started/installation/) `uv`을 설치합니다.

{% tabs local %}
{% tab MacOS 및 Linux %}
터미널 애플리케이션을 열고 다음 명령을 붙여넣은 다음 <kbd>Enter</kbd> 키를 누릅니다.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

출력은 다음과 비슷합니다:

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
 Windows PowerShell을 열고 다음 명령을 붙여넣은 다음 <kbd>Enter</kbd> 키를 누릅니다.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

출력은 다음과 비슷합니다:

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

### 2단계: API 키 만들기 {#create-api-key}

Braze MCP 서버는 Braze 사용자 프로필에서 데이터를 반환하지 않는 38개의 읽기 전용 엔드포인트를 지원합니다. **설정** > **API 및 식별자** > **API 키로** 이동하여 다음 권한 중 일부 또는 전부를 가진 새 키를 만듭니다.

{% details 읽기 전용, 비 PII 권한 목록 %}
#### 캠페인

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 카탈로그

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 클라우드 데이터 수집

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 콘텐츠 블록

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Custom Attributes

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Events

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPI

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Messages

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 환경설정 센터

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Purchases

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 세그먼트

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Sends

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### 세션

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 소프트웨어 개발 키트 인증 키

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 구독

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Templates

| Endpoint | 필요한 권한 |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
기존 API 키를 재사용하지 말고 MCP 클라이언트를 위해 특별히 생성하세요. 또한 상담원이 Braze에서 데이터를 쓰거나 삭제하려고 시도할 수 있으므로 읽기 전용, PII가 아닌 권한만 할당하세요.
{% endalert %}

### 3단계: 식별자 및 엔드포인트 가져오기

MCP 클라이언트를 구성할 때 API 키의 식별자와 워크스페이스의 REST 엔드포인트가 필요합니다. 이러한 세부 정보를 얻으려면 대시보드의 **API 키** 페이지로 돌아가서 이 페이지를 열어두면 [다음 단계에서](#configure-client) 참조할 수 있습니다.

![새로 생성된 API 키와 사용자의 REST 엔드포인트를 보여주는 Braze의 'API 키']({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### 4단계: MCP 클라이언트 구성하기 {#configure-client}

미리 제공된 구성 파일을 사용하여 MCP 클라이언트를 구성하세요.

{% tabs %}
{% tab Claude %}
[클로드 데스크톱에서](https://claude.ai/download) **설정** > **개발자** > **구성 편집으로** 이동한 다음 다음 스니펫을 추가합니다:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "key-identifier",
        "BRAZE_BASE_URL": "rest-endpoint"
      }
    }
  }
}
```

`key-identifier` 및 `rest-endpoint` 을 Braze의 **API 키** 페이지에서 해당 값으로 바꿉니다. 구성은 다음과 비슷해야 합니다:

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

완료했으면 구성을 저장하고 Claude Desktop을 다시 시작합니다.
{% endtab %}

{% tab 커서 %}
[커서에서](https://cursor.com/) **설정** > **도구 및 통합** > **MCP 도구** > **커스텀 MCP 추가로** 이동한 다음 다음 스니펫을 추가합니다:

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

`key-identifier` 및 `rest-endpoint` 을 Braze의 **API 키** 페이지에서 해당 값으로 바꿉니다. 구성은 다음과 비슷해야 합니다:

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

완료했으면 구성을 저장하고 커서를 다시 시작합니다.
{% endtab %}
{% endtabs %}

### 5단계: 테스트 프롬프트 보내기

이제 Braze MCP 서버를 설정했으니 MCP 클라이언트에 테스트 프롬프트를 전송해 보세요. 다른 예제 및 모범 사례는 [Braze MCP 서버 사용]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?"라는 질문에 대한 답변이 Claude에서 이루어지고 있습니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab 커서 %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가'를 묻고 답하는 커서 (]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## 문제 해결

### 터미널 오류

#### `uvx` 명령을 찾을 수 없음

`uvx` 명령을 찾을 수 없다는 오류가 표시되면 `uv` 을 다시 설치하고 터미널을 다시 시작하세요.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` 오류

`spawn uvx ENOENT` 오류가 발생하면 클라이언트의 설정 파일에서 파일 경로를 업데이트해야 할 수 있습니다. 먼저 터미널을 열고 다음 명령을 실행합니다:

```bash
which uvx
```

명령은 다음과 유사한 메시지를 반환해야 합니다:

```bash
/Users/alex-lee/.local/bin/uvx
```

메시지를 클립보드에 복사하고 [클라이언트의 설정 파일을](#configure-client) 엽니다. `"command": "uvx"` 을 복사한 경로로 바꾼 다음 클라이언트를 다시 시작합니다. For example:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### 패키지 설치 실패

패키지 설치에 실패하면 특정 Python 버전을 대신 설치해 보세요.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### 클라이언트 구성

#### MCP 클라이언트가 Braze 서버를 찾을 수 없습니다.

1. MCP 클라이언트 구성 구문이 올바른지 확인합니다.
2. 구성을 변경한 후 MCP 클라이언트를 다시 시작하세요.
3. `uvx` 가 시스템에 있는지 확인 `PATH`.

#### 인증 오류

1. `BRAZE_API_KEY` 주소가 올바르고 활성화되어 있는지 확인합니다.
2. `BRAZE_BASE_URL` 이 Braze 인스턴스와 일치하는지 확인합니다.
3. API 키에 [올바른 권한이](#create-api-key) 있는지 확인하세요.

#### 연결 시간 초과 또는 네트워크 오류

1. `BRAZE_BASE_URL` 이 인스턴스에 맞는지 확인합니다.
2. 네트워크 연결 및 방화벽 설정을 확인하세요.
3. 기본 URL에 HTTPS를 사용하고 있는지 확인하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
