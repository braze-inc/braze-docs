# Configurando o servidor MCP do Braze

> Aprenda como configurar o servidor MCP do Braze, para que você possa interagir com seus dados do Braze através de linguagem natural usando ferramentas como Claude e Cursor. Para mais informações gerais, veja [servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Chave de API do Braze | Uma chave de API do Braze com as permissões necessárias. Você criará uma nova chave quando [configurar seu servidor MCP do Braze](#create-api-key). |
| Cliente MCP | Atualmente, apenas [Claude](https://claude.ai/) e [Cursor](https://cursor.com/) são oficialmente suportados. Você precisará de uma conta para um desses clientes para usar o servidor MCP do Braze. |
| Terminal | Um aplicativo de terminal para que você possa executar comandos e instalar ferramentas. Use seu aplicativo de terminal preferido ou o que já está pré-instalado em seu computador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configurando o servidor MCP do Braze

### Etapa 1: Instalar `uv`

Primeiro, instale `uv`—uma [ferramenta de linha de comando da Astral](https://docs.astral.sh/uv/getting-started/installation/) para gerenciamento de dependências e manipulação de pacotes Python.

{% tabs local %}
{% tab MacOS e Linux %}
Abra seu aplicativo de terminal, cole o seguinte comando e pressione <kbd>Enter</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

A saída será semelhante ao seguinte:

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

A saída será semelhante ao seguinte:

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

### Etapa 2: Crie uma chave de API {#create-api-key}

O servidor Braze MCP suporta 38 endpoints somente leitura que não retornam dados dos perfis de usuários do Braze. Acesse **Configurações** > **APIs e Identificadores** > **Chaves de API** e crie uma nova chave com algumas ou todas as seguintes permissões.

{% details Lista de permissões somente leitura, não-PII %}
#### Campanhas

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canva

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Catálogos

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingestão de dados na nuvem

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Blocos de conteúdo

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Atributos personalizados

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Eventos

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPIs

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Mensagens

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Central de Preferências

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Compras

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segmentos

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Envios

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sessões

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Chaves de autenticação do SDK

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Inscrição

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Modelos

| Endpoint | Permissão Necessária |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Não reutilize uma chave de API existente—crie uma especificamente para seu cliente MCP. Além disso, atribua apenas permissões somente leitura, não-PII, pois os agentes podem tentar gravar ou excluir dados no Braze.
{% endalert %}

### Etapa 3: Obtenha seu identificador e endpoint

Quando você configurar seu cliente MCP, precisará do identificador da sua chave de API e do endpoint REST do seu espaço de trabalho. Para obter esses detalhes, volte para a página **Chaves de API** no dashboard—mantenha esta página aberta, para que você possa consultá-la durante [a próxima etapa](#configure-client).

![As 'Chaves de API' no Braze mostrando uma chave de API recém-criada e o endpoint REST do usuário.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Etapa 4: Configure seu cliente MCP {#configure-client}

Configure seu cliente MCP usando nosso arquivo de configuração pré-fornecido.

{% tabs %}
{% tab Claude %}
No [Claude Desktop](https://claude.ai/download), acesse **Configurações** > **Desenvolvedor** > **Editar Config**, em seguida, adicione o seguinte trecho:

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

Substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página **Chaves de API** no Braze. Sua configuração deve ser semelhante ao seguinte:

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

Quando terminar, salve a configuração e reinicie o Claude Desktop.
{% endtab %}

{% tab Cursor %}
No [Cursor](https://cursor.com/), acesse **Configurações** > **Ferramentas e Integrações** > **Ferramentas MCP** > **Adicionar MCP Personalizado**, em seguida, adicione o seguinte trecho:

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

Substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página **Chaves de API** no Braze. Sua configuração deve ser semelhante ao seguinte:

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

Quando você terminar, salve a configuração e reinicie o Cursor.
{% endtab %}
{% endtabs %}

### Etapa 5: Envie um prompt de teste

Agora que você configurou o servidor Braze MCP, tente enviar um prompt de teste para o seu cliente MCP. Para outros exemplos e melhores práticas, veja [Usando o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['Quais são minhas funções Braze disponíveis?' sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Quais são minhas funções Braze disponíveis' sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Solução de problemas

### Erros de terminal

#### `uvx` comando não encontrado

Se você receber um erro que `uvx` comando não encontrado, reinstale `uv` e reinicie seu terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` erro

Se você receber um `spawn uvx ENOENT` erros, pode ser necessário atualizar o caminho no arquivo de configuração do seu cliente. Primeiro, abra seu terminal e execute o seguinte comando:

```bash
which uvx
```

O comando deve retornar uma mensagem semelhante à seguinte:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copie a mensagem para sua área de transferência e abra [o arquivo de configuração do seu cliente](#configure-client). Substitua `"command": "uvx"` pelo caminho que você copiou, e então reinicie seu cliente. Por exemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### A instalação do pacote falha

Se a instalação do seu pacote falhar, tente instalar uma versão específica do Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuração do cliente

#### O cliente MCP não consegue encontrar o servidor Braze

1. Verifique se a sintaxe da configuração do seu cliente MCP está correta.
2. Reinicie seu cliente MCP após as alterações de configuração.
3. Verifique se `uvx` está no seu sistema `PATH`.

#### Erros de autenticação

1. Verifique se seu `BRAZE_API_KEY` está correto e ativo.
2. Certifique-se de que seu `BRAZE_BASE_URL` corresponde à sua instância Braze.
3. Verifique se sua chave de API tem as [permissões corretas](#create-api-key).

#### Timeouts de conexão ou erros de rede

1. Verifique se seu `BRAZE_BASE_URL` está correto para sua instância.
2. Verifique sua conexão de rede e configurações de firewall.
3. Certifique-se de que está usando HTTPS em sua URL base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
