# Configuração do servidor Braze MCP

> Saiba como configurar o servidor Braze MCP para que você possa interagir com seus dados Braze por meio de linguagem natural usando ferramentas como Claude e Cursor. Para saber mais sobre informações gerais, consulte [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Chave de API do Braze | Uma chave de API do Braze com as permissões necessárias. Você criará uma nova chave ao [configurar seu servidor Braze MCP](#create-api-key). |
| Cliente MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) e [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) são oficialmente compatíveis. Você deve ter uma conta em um desses clientes para usar o servidor Braze MCP. |
| Terminal | Um app de terminal para que você possa executar comandos e instalar ferramentas. Use seu app de terminal preferido ou o que está pré-instalado em seu computador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuração do servidor Braze MCP

### Etapa 1: Instalar `uv`

Primeiro, instale o `uv`, uma [ferramenta de linha de comando da Astral](https://docs.astral.sh/uv/getting-started/installation/) para gerenciamento de dependências e manipulação de pacotes Python.

{% tabs local %}
{% tab MacOS and Linux %}
Abra seu aplicativo de terminal, cole o seguinte comando e pressione <kbd>Enter</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

A saída é semelhante à seguinte:

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
 Abra o Windows PowerShell, cole o seguinte comando e pressione <kbd>Enter</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

A saída é semelhante à seguinte:

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

### Etapa 2: Criar uma chave de API {#create-api-key}

O servidor MCP da Braze suporta 38 pontos de extremidade somente leitura que não retornam dados de perfis de usuários da Braze. Acesse **Settings** > **APIs and Identifiers** > **API Keys** e crie uma nova chave com algumas ou todas as permissões a seguir.

{% details List of read-only, non-PII permissions %}
#### Campanhas

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canva

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Catálogos

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingestão de dados na nuvem

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Blocos de conteúdo

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Atributos personalizados

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Eventos

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPIs

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Mensagens

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Central de Preferências

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Compras

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segmentos

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Envios

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sessões

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Chaves de autenticação do SDK

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Inscrição

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Modelos

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Não reutilize uma chave de API existente - crie uma especificamente para seu cliente MCP. Além disso, atribua apenas permissões somente de leitura e sem IPI, pois os agentes podem tentar gravar ou excluir dados no Braze.
{% endalert %}

### Etapa 3: Obtenha seu identificador e ponto de extremidade

Ao configurar seu cliente MCP, você precisará do identificador da chave de API e do endpoint REST do seu espaço de trabalho. Para obter esses detalhes, volte à página **Chaves de API** no dashboard - mantenha essa página aberta para que você possa consultá-la na [próxima etapa](#configure-client).

![As "Chaves de API" no Braze mostram uma chave de API recém-criada e o endpoint REST do usuário.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Etapa 4: Configure seu cliente MCP {#configure-client}

Configure seu cliente MCP usando o arquivo de configuração fornecido previamente.

{% tabs %}
{% tab Claude %}
Configure seu servidor MCP usando o diretório do conector do [Claude Desktop](https://claude.ai/download). 

1. No Claude Desktop, acesse **Configurações** > **Conectores** > **Procurar conectores** > **Extensões de desktop** > **Braze MCP Server** > **Instalar**.
2. Digite sua chave de API e o URL de base.
3. Salve a configuração e reinicie o Claude Desktop.

{% endtab %}

{% tab Cursor %}
No [Cursor](https://cursor.com/), acesse **Configurações** > **Ferramentas e integrações** > **Ferramentas MCP** > **Adicionar MCP personalizado** e, em seguida, adicione o seguinte snippet:

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

Substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página **Chaves de API** no Braze. Sua configuração deve ser semelhante à seguinte:

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

Quando terminar, salve a configuração e reinicie o Cursor.
{% endtab %}
{% tab Gemini CLI %}
A CLI do Gemini lê as configurações do usuário em `~/.gemini/settings.json`. Se ele não existir, você poderá criá-lo executando o seguinte no terminal:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Em seguida, substitua `yourname` pela string exata antes de `@BZXXXXXXXX` no prompt do terminal. Em seguida, substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página de **chaves de API** no Braze. 

Sua configuração deve ser semelhante à seguinte:

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

Quando terminar, salve a configuração e reinicie a CLI do Gemini. Em seguida, no Gemini, execute os seguintes comandos para verificar se o servidor Braze MCP está listado e se as ferramentas e o esquema estão disponíveis para uso:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Você deverá ver o servidor `braze` listado com as ferramentas e o esquema disponíveis para uso.

{% endtab %}
{% endtabs %}

### Etapa 5: Enviar um prompt de teste

Depois de configurar o servidor Braze MCP, tente enviar um prompt de teste para seu cliente MCP. Para obter outros exemplos e práticas recomendadas, consulte [Usando o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!["Quais são as minhas funções disponíveis no Braze?" sendo perguntado e respondido em Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Quais são minhas funções Braze disponíveis" sendo perguntadas e respondidas no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Quais são as minhas funções Braze disponíveis? que estão sendo perguntadas e respondidas na CLI do Gemini.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Solução de problemas

### Erros no terminal

#### `uvx` comando não encontrado

Se você receber um erro informando que o comando `uvx` não foi encontrado, reinstale o `uv` e reinicie o terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` erro

Se você receber um erro `spawn uvx ENOENT`, talvez seja necessário atualizar o caminho do arquivo no arquivo de configuração do seu cliente. Primeiro, abra seu terminal e execute o seguinte comando:

```bash
which uvx
```

O comando deve retornar uma mensagem semelhante à seguinte:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copie a mensagem para a área de transferência e abra [o arquivo de configuração do seu cliente](#configure-client). Substitua `"command": "uvx"` pela jornada que você copiou e reinicie o cliente. Por exemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Falha na instalação do pacote

Se a instalação do pacote falhar, tente instalar uma versão específica do Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuração do cliente

#### O cliente MCP não consegue encontrar o servidor Braze

1. Verifique se a sintaxe da configuração do cliente MCP está correta.
2. Reinicie o cliente MCP após as alterações de configuração.
3. Verifique se `uvx` está em seu sistema `PATH`.

#### Erros de autenticação

1. Verifique se o endereço `BRAZE_API_KEY` está correto e ativo.
2. Verifique se o endereço `BRAZE_BASE_URL` corresponde à sua instância do Braze.
3. Verifique se sua chave de API tem as [permissões corretas](#create-api-key).

#### Tempo limite de conexão ou erros de rede

1. Verifique se o endereço `BRAZE_BASE_URL` está correto para sua instância.
2. Verifique sua conexão de rede e as configurações de firewall.
3. Verifique se você está usando HTTPS em seu URL de base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
