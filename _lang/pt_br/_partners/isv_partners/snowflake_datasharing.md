---
nav_title: Compartilhamento de dados do Snowflake
hidden: true
---

# Integração do compartilhamento de dados do Snowflake

> Quando o Snowflake Data Share for usado como um método de integração, o Braze fornecerá um compartilhamento para sua instância do Snowflake em nome do cliente. Esse compartilhamento incluirá automaticamente todos os eventos de engajamento com mensagens e de comportamento do usuário.

Os compartilhamentos são provisionados por cliente após o cliente adquirir um direito de compartilhamento de dados do Snowflake. Quando um cliente solicita um compartilhamento de dados, o Braze adiciona um compartilhamento ao espaço de trabalho do cliente, e o cliente pode usar a interface de usuário de autoatendimento para adicionar os dados relevantes da conta Snowflake do parceiro.

![]({% image_buster /assets/img/snowflake.png %})

Depois que o compartilhamento é provisionado, todos os dados ficam imediatamente acessíveis a partir da instância do Snowflake como um compartilhamento de dados de entrada.

![]({% image_buster /assets/img/snowflake2.png %})

Na sua instância do Snowflake, você verá um compartilhamento por região. Cada tabela tem uma coluna, `app_group_id`, que é efetivamente uma chave de locatário para a Braze. À medida que novos clientes forem adicionados a uma ação dentro da mesma região, eles aparecerão como diferentes `app_group_ids` dentro das tabelas existentes.

{% alert important %}
A Braze hospeda todos os dados de nível de usuário nas regiões AWS US East-1 e EU-Central (Frankfurt) do Snowflake. Embora a Braze possa compartilhar entre regiões, é mais econômico para os clientes se compartilharmos com `US-EAST-1` e/ou `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Baixe os [esquemas de tabelas brutas]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) aqui ou use esse conjunto de [dados de eventos de amostra](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponíveis no mercado do Snowflake para se familiarizar com os eventos compartilhados.
{% endalert %}

## Tratamento de eventos duplicados

Espera-se que haja duplicatas, mas todos os eventos têm um identificador exclusivo, a coluna ID. As duplicatas podem ser removidas com `select distinct(id)`.

## Alterações interruptivas e não interruptivas

### Alterações não interruptivas

Alterações não interruptivas podem ocorrer a qualquer momento e geralmente trazem novas funcionalidades. Exemplos de alterações não interruptivas:
- Adição de uma nova tabela ou visualização
- Adição de uma coluna a uma tabela ou exibição existente

{% alert important %}
Como as novas colunas são consideradas não interruptivas, a Braze recomenda enfaticamente listar de modo explícito as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Como alternativa, talvez você queira criar exibições que nomeiem explicitamente as colunas e, em seguida, consultar essas exibições em vez das tabelas diretamente.
{% endalert %}

### Mudanças significativas

Quando possível, as mudanças interruptivas serão precedidas de um anúncio e de um período de migração. Exemplos de mudanças significativas incluem:
- Remoção de uma tabela ou exibição
- Remoção de uma coluna de uma tabela ou exibição existente
- Alteração do tipo ou da capacidade de anulação de uma coluna existente

## Quando as tabelas SNAPSHOTS e CHANGELOGS são atualizadas

As tabelas SNAPSHOTS e CHANGELOGS rastreiam as alterações em campanhas e canvas. Entender quando essas tabelas são atualizadas é importante para consultar as variações mais recentes de mensagens e as configurações do Canva.

### CHANGELOGS_CAMPAIGN_SHARED

Uma linha é adicionada ao site `CHANGELOGS_CAMPAIGN_SHARED` quando:
- A campanha é lançada, OU
- Qualquer um dos seguintes campos do snapshottable é alterado:
  - Nome
  - Ações (incluindo alterações no conteúdo das mensagens)
  - Comportamentos de conversão

{% alert important %}
Salvar ou atualizar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você lança a campanha ou aplica as alterações de rascunho pós-lançamento à campanha ativa.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` é derivado de `CHANGELOGS_CAMPAIGN_SHARED`. Essa tabela extrai e organiza a coluna de ações de `CHANGELOGS_CAMPAIGN_SHARED` em registros de variação de mensagens individuais. Ele é atualizado adequadamente quando o site `CHANGELOGS_CAMPAIGN_SHARED` é atualizado.

### CHANGELOGS_CANVAS_SHARED

Uma linha é adicionada ao site `CHANGELOGS_CANVAS_SHARED` quando:
- O Canva é lançado, OU
- Qualquer um dos seguintes campos do snapshottable é alterado:
  - Nome
  - Comportamentos de conversão
  - Variações (porcentagem, atribuições da primeira etapa, nomes das variações)

{% alert important %}
Salvar ou atualizar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você inicia o Canvas ou aplica as alterações de rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` é derivado de `CHANGELOGS_CANVAS_SHARED`. Essa tabela usa o mesmo padrão de extração que `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` e é atualizada de acordo quando `CHANGELOGS_CANVAS_SHARED` é atualizado.

### SNAPSHOTS_CANVAS_STEP_SHARED

Uma linha é adicionada ao site `SNAPSHOTS_CANVAS_STEP_SHARED` quando:
- O Canva é lançado, OU
- O Canva ativo é atualizado (rascunho pós-lançamento aplicado), OU
- Qualquer um dos seguintes campos do snapshottable é alterado:
  - Nome
  - Ações (incluindo alterações no conteúdo da mensagem em variações de mensagens)

{% alert important %}
Salvar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você inicia o Canvas ou aplica as alterações de rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Uma linha é adicionada ao site `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` quando:
- O Canva é lançado, OU
- O Canva ativo é atualizado (rascunho pós-lançamento aplicado), OU
- Qualquer um dos seguintes campos do snapshottable é alterado:
  - Nome

{% alert important %}
Salvar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você inicia o Canvas ou aplica as alterações de rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

## Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR)

{% include partners/snowflake_pii_gdpr.md %}