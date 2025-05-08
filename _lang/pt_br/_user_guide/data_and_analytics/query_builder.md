---
nav_title: Criador de consultas
article_title: Criador de consultas
page_order: 15
page_type: reference
description: "Este artigo de referência descreve como criar relatórios usando dados da Braze do Snowflake no Query Builder."
tool: Reports
---

# Criador de consultas

> O Construtor de consultas gera relatórios usando dados do Braze no Snowflake. O Criador de consultas vem com [modelos de consultas]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/query_templates/) de SQL pré-construídas para você começar, ou você pode escrever suas próprias consultas de SQL personalizadas para desbloquear ainda mais insights.

Como o Criador de consultas permite acesso direto a alguns dados de clientes, você só pode acessar o Criador de consultas se tiver a [permissão]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/) "Ver IPI".

## Execução de relatórios no Query Builder

Para executar um relatório do Query Builder:

1. Acesse **Análise de dados** > **Criador de consultas**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **o Query Builder** em **Data**.
{% endalert %}

{:start="2"}
2\. Selecione **Create SQL Query (Criar consulta de SQL**). Se precisar de inspiração ou ajuda para elaborar sua consulta, selecione **Query Template (Modelo de consulta** ) e escolha um modelo da lista. Caso contrário, selecione **Editor de SQL** para ir direto ao editor.
3\. Seu relatório recebe automaticamente um nome com a data e a hora atuais. Passe o mouse sobre o nome e selecione <i class="fas fa-pencil" alt="Edit"></i> para dar à sua consulta de SQL um nome significativo.
4\. Escreva sua consulta de SQL no editor ou [obtenha ajuda da IA](#ai-query-builder) na guia **IA Query Builder**. Se estiver escrevendo seu próprio SQL, consulte [Como escrever consultas de SQL personalizadas](#custom-sql) para obter requisitos e recursos.
5\. Selecione **Executar consulta**.
6\. Salve sua consulta.
7\. Para baixar um CSV de seu relatório, selecione **Exportar**.

![O Criador de consultas mostra os resultados da consulta modelo "Engajamento e receita do canal nos últimos 30 dias".]({% image_buster /assets/img_archive/query_builder.png %})

Os resultados de cada relatório podem ser gerados uma vez por dia. Se você executar o mesmo relatório mais de uma vez em um dia do calendário, verá os mesmos resultados em ambos os relatórios.

### Modelos de consulta

Acesse os modelos de consulta selecionando **Criar consulta de SQL** > **Modelo de consulta** ao criar um relatório pela primeira vez.

Consulte [Modelos de consulta]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/query_templates/) para obter uma lista dos modelos disponíveis.

### Período de dados

Todas as consultas apresentam dados dos últimos 60 dias. 

## Geração de SQL com o Criador de consultas com IA

O Criador de consultas com IA usa o [GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para sua consulta.

![][2]{: style="max-width:60%;" }

Para gerar SQL com o Criador de consultas com IA:

1. Depois de criar um relatório no Criador de consultas, selecione a guia **Criador de consultas com IA**.
2. Digite seu prompt ou selecione um prompt de amostra e selecione **Gerar** para traduzir seu prompt para SQL.
3. Revise o SQL gerado para ter certeza de que está correto e, em seguida, selecione **Insert into Editor (Inserir no editor**).

### Dicas

- Familiarize-se com as tabelas de dados disponíveis [do Snowflake]({{site.baseurl}}/sql_segments_tables/). A solicitação de dados que não existem nessas tabelas pode fazer com que o ChatGPT crie uma tabela falsa.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esse recurso. O não cumprimento dessas regras causará um erro.
- Você pode enviar até 20 prompts por minuto com o Criador de consultas com IA.

### Como meus dados são usados e enviados para a OpenAI?
<!-- Contact Legal for changes. -->

Para gerar seu SQL, a Braze enviará seus prompts para a API Platform da OpenAI. Todas as consultas enviadas pela Braze à OpenAI são anônimas, o que significa que a OpenAI não poderá identificar o remetente da consulta, a menos que você inclua informações exclusivamente identificáveis no conteúdo fornecido. Conforme detalhado nos [Compromissos da Plataforma de API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Siga às políticas da OpenAI relevantes para você, incluindo a [Política de Uso](https://openai.com/policies/usage-policies). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA. 

## Escrever consultas de SQL personalizadas {#custom-sql}

Escreva sua consulta de SQL usando [a sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte a [referência da tabela]({{site.baseurl}}/sql_segments_tables/) para obter uma lista completa das tabelas e colunas disponíveis para consulta.

Para visualizar os detalhes da tabela no Query Builder:

1. Na página **do Construtor de consultas**, abra o painel **Referência** e selecione **Tabelas de dados disponíveis** para visualizar as tabelas de dados disponíveis e seus nomes.
3. Selecione <i class="fas fa-chevron-down" alt=""></i> **See Details** para visualizar a descrição da tabela e as informações sobre as colunas da tabela, como os tipos de dados.
4. Para inserir o nome da tabela em seu SQL, selecione <i class="fas fa-copy" title="Copiar nome da tabela para o editor SQL"></i>.

Para usar consultas pré-escritas fornecidas pelo Braze, selecione **Modelo de consulta** ao criar um relatório pela primeira vez no Query Builder.

Restringir sua consulta a um período de tempo específico o ajudará a gerar resultados mais rapidamente. A seguir, um exemplo de consulta que obtém o número de compras e a receita gerada na última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Essa consulta recupera o número de envios de e-mail no último mês:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Se você consultar `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, suas colunas de nome associadas serão automaticamente incluídas na tabela de resultados. Não é necessário incluí-los na própria consulta `SELECT`.

| Nome do ID | Coluna de nome associado |
| --- | --- |
| `CANVAS_ID` | Nome do canva |
| `CANVAS_VARIATION_API_ID` | Nome da variante da tela |
| `CAMPAIGN_ID` | Nome da campanha |
{: .reset-td-br-1 .reset-td-br-2 }

Essa consulta recupera todos os três IDs e suas colunas de nome associadas com um máximo de 100 linhas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Solução de problemas

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe em sua consulta de SQL
- Tempo limite de processamento (após 6 minutos)
    - Os relatórios que demorarem mais de 6 minutos para serem executados serão encerrados.
    - Se um relatório não atingir o tempo limite, tente limitar o intervalo de tempo em que está consultando os dados ou consulte um conjunto de dados mais específico.

## Uso de variáveis

Use variáveis para usar tipos de variáveis predefinidas no SQL para fazer referência a valores sem precisar copiar manualmente o valor. Por exemplo, em vez de copiar manualmente o ID de uma campanha para o editor SQL, você pode usar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para selecionar diretamente uma campanha em um menu suspenso na guia **Variables (Variáveis** ).

![][3]

Depois que uma variável for criada, ela aparecerá na guia **Variáveis** de seu relatório do Criador de consultas. Os benefícios do uso de variáveis SQL incluem:

- Economize tempo criando uma variável de campanha para selecionar em uma lista ao criar seu relatório, em vez de colar os IDs de campanha.
- Troque os valores adicionando variáveis que lhe permitam reutilizar o relatório para casos de uso ligeiramente diferentes no futuro (como um evento personalizado diferente).
- Reduza o erro do usuário ao editar seu SQL, reduzindo a quantidade de edição necessária para cada relatório. Os colegas de equipe que se sentem mais à vontade com o SQL podem criar relatórios que podem ser usados por colegas de equipe menos técnicos.

### Diretrizes

As variáveis devem obedecer à seguinte sintaxe Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, em que `type` deve ser um dos tipos aceitos e `name` pode ser qualquer coisa que você escolher. Os rótulos dessas variáveis têm como padrão o nome da variável.

Por padrão, todas as variáveis são obrigatórias (e o relatório não será executado a menos que os valores das variáveis sejam selecionados), exceto o intervalo de datas, cujo padrão é os últimos 30 dias quando o valor não é fornecido.

### Tipos de variáveis

Os seguintes tipos de variáveis são aceitos:

- [Número](#number)
- [Período](#date-range)
- [Envio de mensagens](#messaging)
- [Produtos](#products)
- [Eventos personalizados](#custom-events)
- [Propriedades de eventos personalizados](#custom-event-properties)
- [Espaço de trabalho](#workspace)
- [Catálogos](#catalogs)
- [Campos do catálogo](#catalog-fields)
- [Opções](#options)
- [Segmentos](#segments)
- [String](#string)
- [Tags](#tags)

#### Número

- **Valor de substituição:** O valor fornecido, como `5.5`
- **Exemplo de uso:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Período

![][4]{: style="max-width:50%;"}

Se estiver usando `start_date` e `end_date`, eles devem ter o mesmo nome para que você possa usá-los como um intervalo de datas.

##### Valores de exemplo

O tipo de intervalo de datas pode ser relativo, data inicial, data final ou intervalo de datas.

Todos os quatro tipos são mostrados se `start_date` e `end_date` forem usados com o mesmo nome. Se apenas um for usado, somente os tipos relevantes serão exibidos.

| Tipo de intervalo de datas | Descrição | Valores necessários |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data inicial | Especifica uma data de início | Requer `start_date` |
| Data final | Especifica uma data final | Requer `end_date` |
| Período | Especifica uma data inicial e uma data final | Requer os sites `start_date` e `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Valor de substituição:** Substitui `start_date` e `end_date` por um carimbo de data/hora Unix em segundos para uma data especificada em UTC, como `1696517353`.
- **Exemplo de uso:** Para todas as variáveis relativas, data de início, data de término e intervalo de datas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Você pode usar `start_date` ou `end_date` se não quiser um intervalo de datas.

#### Envio de mensagens

Todas as variáveis de envio de mensagens devem compartilhar o mesmo identificador quando você quiser unir o estado delas em um grupo.

![][5]{: style="max-width:50%;"}

##### Canva

Para selecionar um Canva. Compartilhar o mesmo nome com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canva ou campanha.

- **Valor de substituição:** ID do BSON da tela
- **Exemplo de uso:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvas

Para selecionar várias telas. Compartilhar o mesmo nome com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canva ou campanha.

- **Valor de substituição:** Canvas IDs BSON
- **Exemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campanha interrompida

Para selecionar uma campanha. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

- **Valor de substituição:** ID BSON da campanha
- **Exemplo de uso:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campanhas

Para campanhas de seleção múltipla. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

- **Valor de substituição:** IDs BSON de campanhas
- **Exemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de campanha

Para selecionar variantes de campanha que pertencem à campanha selecionada. Ele deve ser usado em conjunto com uma variável de campanha ou de campanhas.

- **Valor de substituição:** IDs da API de variantes de campanha, strings delimitadas por vírgulas, como `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes da tela

Para selecionar as variantes do Canvas que pertencem a um Canvas escolhido. Ele deve ser usado com uma variável Canvas ou Canvases.

- **Valor de substituição:** IDs de API das variantes do canva, strings delimitadas por vírgulas, como em `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Etapa do canva

Para selecionar uma etapa do Canva que pertença a um Canvas escolhido. Ele deve ser usado com uma variável Canva.

- **Valor de substituição:** ID da API da etapa do canva
- **Exemplo de uso:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Etapas do canva

Para selecionar as etapas do Canvas que pertencem aos Canvases escolhidos. Ele deve ser usado com uma variável Canvas ou Canvases.

- **Valor de substituição:** IDs da API das etapas do canva
- **Exemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### Produtos

Para selecionar uma lista de nomes de produtos.

- **Valor de substituição:** Os nomes dos produtos são colocados entre aspas simples e separados por vírgulas, como em `product1, product2`
- **Exemplo de uso:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### Eventos personalizados

Para selecionar uma lista de eventos personalizados.

- **Valor de substituição:** Os nomes de propriedades de eventos personalizados são separados por vírgulas, como em `event1, event2`
- **Exemplo de uso:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### Propriedades de eventos personalizados

Para selecionar uma lista de nomes de propriedades de eventos personalizados. Ela deve ser usada com a variável de eventos personalizados.

- **Valor de substituição:** Os nomes de propriedades de eventos personalizados são separados por vírgulas, como em `property1, property2`
- **Exemplo de uso:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### Espaço de trabalho

Para selecionar um espaço de trabalho.

- **Valor de substituição:** ID BSON do espaço de trabalho
- **Exemplo de uso:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### Catálogos

Para selecionar catálogos.

- **Valor de substituição:** IDs BSON do catálogo
- **Exemplo de uso:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### Campos do catálogo

Para selecionar os campos do catálogo. Ela deve ser usada com a variável catalogs.

- **Valor de substituição:** Nomes de campos do catálogo
- **Exemplo de uso:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### Opções {#options}

Para selecionar em uma lista de opções.

- **Valor de substituição:** O valor das opções selecionadas
- **Exemplo de uso:**
    - Para selecionar o menu suspenso: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` permite especificar se o usuário final pode selecionar mais de uma opção
    - Para o botão de rádio: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### Segmentos

Para selecionar segmentos que tenham [a análise de dados]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/) ativada.

- **Valor de substituição:** A ID de análise de dados do segmento, que corresponde às IDs armazenadas na coluna `user_segment_membership_ids` nas tabelas em que essa coluna está disponível.
- **Exemplo de uso:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### String

Para alterar os valores repetitivos da string entre as execuções do relatório. Use essa variável para evitar a codificação de um valor várias vezes em seu SQL.

- **Valor de substituição:** A string como está, sem as aspas ao redor
- **Exemplo de uso:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### Tags

Para selecionar tags para campanhas e telas.

- **Valor de substituição:** Campanhas e telas com IDs BSON separadas por vírgula e com aspas simples que estão associadas às tags selecionadas
- **Exemplo de uso:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### Metadados variáveis

Os metadados podem ser anexados a uma variável para alterar seu comportamento, anexando os metadados com um caractere pipe ( | ) após o nome da variável. A ordem dos metadados não importa e você pode anexar qualquer número deles. Além disso, todos os tipos de metadados podem ser usados para qualquer variável, exceto os metadados especiais que são específicos para determinadas variáveis (isso será indicado nesses casos). O uso de todos os metadados é opcional e é usado para alterar o comportamento da variável padrão.

**Exemplo de uso:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### Visível

Para saber se as variáveis estão visíveis. Todas as variáveis são visíveis por padrão na guia **Variables (Variáveis** ), onde você pode inserir valores.

Há diversas variáveis especiais cujo valor depende de outra variável, como, por exemplo, se outra variável tem um valor. Essas variáveis especiais são marcadas como não visíveis para que não sejam exibidas na guia **Variáveis**.

**Exemplo de uso:** `visible: ‘false’`

#### Obrigatória

Para saber se as variáveis são obrigatórias por padrão. Um valor vazio para uma variável geralmente leva a uma consulta incorreta.

**Exemplo de uso:** `required: ‘false’`

#### Pedido

Para selecionar a posição da variável na guia **Variáveis**.

**Exemplo de uso:** `order: ‘1’`

#### Incluir aspas simples

Para cercar os valores de uma variável com aspas simples.

**Exemplo de uso:** `include_quotes: ‘true’`

#### Incluir aspas duplas

Para envolver os valores de uma variável com aspas duplas.

**Exemplo de uso:** `include_double_quotes: ‘true’`

#### Seleção múltipla

Para saber se o menu suspenso de seleção permite uma seleção única ou múltipla. Por enquanto, você pode incluir esses metadados somente se usar a variável [Options](#options).

**Exemplo de uso:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### Botão de rádio

Para mostrar opções como botões de rádio em vez de um menu suspenso de seleção na guia **Variables (Variáveis** ). Você pode incluir esses metadados somente se usar a variável [Options](#options).

**Exemplo de uso:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### Opções 

Para fornecer a lista de opções selecionáveis na forma de um rótulo e valor. O rótulo é o que é exibido e o valor é o que substitui a variável quando a opção é selecionada. Você pode incluir esses metadados somente se usar a variável [Options](#options).

**Exemplo de uso:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### Espaço reservado

Para especificar o texto do espaço reservado mostrado no campo de entrada da variável.

**Exemplo de uso:** `placeholder: ‘enter some value’`

#### Descrição

Para especificar o texto de descrição mostrado no campo de entrada da variável.

**Exemplo de uso:** `description: ‘some description’`

#### Valor padrão

Para especificar o valor padrão da variável quando nenhum valor for especificado.

**Exemplo de uso:** `default_value: ‘5’`

#### Ocultar rótulo

Para ocultar o rótulo do nome da variável. O nome da variável é usado como um rótulo padrão.

**Exemplo de uso:** `hide_label: ‘true’`

### Variáveis especiais

As seguintes variáveis podem ser usadas com outras variáveis:

#### Presença ou ausência do valor de outra variável

Para saber se o valor de uma variável está preenchido. Isso é útil para variáveis opcionais em que você deseja interromper uma condição se o valor de uma variável não for preenchido.

- **Valor de substituição:** `true` ou `false`, dependendo do valor da outra variável
- **Exemplo de uso:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` e `name` referem-se à variável referenciada. Por exemplo, para causar curto-circuito na seguinte variável opcional: {% raw %}`{{campaigns.${messaging}}`, você pode usar o seguinte:
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## Tempo limite do relatório

Os relatórios que demorarem mais de seis minutos para serem executados serão encerrados. Se esta for a primeira consulta que você está executando em algum tempo, ela poderá levar mais tempo para ser processada e, portanto, terá uma probabilidade maior de atingir o tempo limite. Se isso acontecer, tente executar o relatório novamente.

Se um relatório expirar ou apresentar erros mesmo após uma nova tentativa, entre em contato com [o Suporte]({{site.baseurl}}/help/support#braze-support).

## Dados e resultados

Os resultados e as exportações de resultados são tabelas que podem conter até 1.000 linhas. Para relatórios que exigem grandes quantidades de dados, use outra ferramenta, como o [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) ou [as APIs de exportação]({{site.baseurl}}/api/endpoints/export) do Braze.

## Monitoramento do uso do Query Builder

Cada espaço de trabalho da Braze tem 5 créditos Snowflake disponíveis por mês. Uma pequena parte de um crédito do Snowflake é usada sempre que você executa uma consulta ou prévia uma tabela.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre os recursos. Por exemplo, os créditos nas extensões de segmento do SQL e no Criador de Consultas são independentes um do outro.
{% endalert %}

O uso de crédito está correlacionado ao tempo de execução de sua consulta de SQL. Quanto maior for o tempo de execução, maior será a porção de crédito do Snowflake que uma consulta custará. O tempo de execução pode variar de acordo com a complexidade e o tamanho de suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Os créditos não são usados ao escrever, editar ou salvar relatórios no editor Braze SQL. Seus créditos serão redefinidos para 5 no primeiro dia de cada mês, às 12 horas UTC. Você pode monitorar o uso de seu crédito mensal na parte superior da página do Criador de consultas.

![O Construtor de consultas mostra a quantidade de créditos usados no mês atual.][1]{: style="max-width:60%;"}

Quando você atinge o limite de crédito, não pode executar consultas, mas pode criar, editar e salvar relatórios de SQL. Se quiser comprar mais créditos do Criador de consultas, entre em contato com o gerente da sua conta.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
