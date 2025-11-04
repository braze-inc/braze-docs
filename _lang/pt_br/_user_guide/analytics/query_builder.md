---
nav_title: Criador de consultas
article_title: Criador de consultas
page_order: 15
description: "Este artigo de referência descreve como criar relatórios usando dados do Braze do Snowflake no Query Builder."
tool: Reports
alias: /query_builder/
---

# Criador de consultas

> O Query Builder gera relatórios usando dados do Braze no Snowflake. O Query Builder vem com [modelos de consulta]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL pré-criados para você começar, ou você pode escrever suas próprias consultas SQL personalizadas para obter ainda mais insights.

Como o Query Builder permite acesso direto a alguns dados do cliente, você só pode acessar o Query Builder se tiver a [permissão]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)"View PII".

## Execução de relatórios no Query Builder

Para executar um relatório do Query Builder:

1. Vá para **Analytics** > **Query Builder**.
2. Selecione **Criar consulta SQL**. Se você precisar de inspiração ou ajuda para elaborar sua consulta, selecione **Query Template (Modelo de consulta** ) e escolha um modelo na lista. Caso contrário, selecione **SQL Editor** para ir direto ao editor.
3. Seu relatório recebe automaticamente um nome com a data e a hora atuais. Passe o mouse sobre o nome e selecione <i class="fas fa-pencil" alt="Edit"></i> para dar à sua consulta SQL um nome significativo.
4. Escreva sua consulta SQL no editor ou [obtenha ajuda da IA](#ai-query-builder) na guia **AI Query Builder**. Se estiver escrevendo seu próprio SQL, consulte [Como escrever consultas SQL personalizadas](#custom-sql) para obter requisitos e recursos.
5. Selecione **Run Query (Executar consulta**).
6. Salve sua consulta.
7. Para fazer o download de um CSV de seu relatório, selecione **Exportar**.

\![Query Builder mostrando os resultados da consulta modelo "Envolvimento e receita do canal nos últimos 30 dias".]({% image_buster /assets/img_archive/query_builder.png %})

Os resultados de cada relatório podem ser gerados uma vez por dia. Se você executar o mesmo relatório mais de uma vez em um dia do calendário, verá os mesmos resultados em ambos os relatórios.

### Modelos de consulta

Acesse os modelos de consulta selecionando **Criar consulta SQL** > **Modelo de consulta** ao criar um relatório pela primeira vez.

Consulte [Modelos de consulta]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) para obter uma lista dos modelos disponíveis.

### Período de tempo dos dados

Todas as consultas apresentam dados dos últimos 60 dias.

### Fuso horário do Query Builder

O fuso horário padrão para consulta ao nosso banco de dados Snowflake é UTC. Como resultado, pode haver algumas discrepâncias de dados entre sua página **Email Channel Engagement** (que segue o fuso horário de sua empresa) e os resultados do Query Builder.

Para converter o fuso horário nos resultados da consulta, adicione o seguinte SQL à consulta e personalize-o de acordo com o fuso horário de sua empresa:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### Histórico de consultas

A seção **Histórico de consultas** no Query Builder exibe as consultas executadas anteriormente para ajudá-lo a rastrear e reutilizar seu trabalho. O histórico de consultas é retido por sete dias, o que significa que as consultas com mais de sete dias são automaticamente removidas.

Se for necessário auditar o uso da consulta por períodos mais longos ou manter registros além de sete dias, recomendamos exportar ou salvar resultados de consultas importantes antes que eles expirem.

## Geração de SQL com o AI Query Builder

O AI Query Builder aproveita [o GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar o SQL para sua consulta.

\![O criador de consultas SQL AI.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Para gerar SQL com o AI Query Builder:

1. Depois de criar um relatório no Query Builder, selecione a guia **AI Query Builder**.
2. Digite seu prompt ou selecione um prompt de amostra e selecione **Generate** para traduzir seu prompt em SQL.
3. Revise o SQL gerado para ter certeza de que está correto e, em seguida, selecione **Insert into Editor (Inserir no editor**).

### Dicas

- Familiarize-se com as [tabelas de dados]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponíveis [do Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). A solicitação de dados que não existem nessas tabelas pode fazer com que o ChatGPT crie uma tabela falsa.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esse recurso. O não cumprimento dessas regras causará um erro.
- Você pode enviar até 20 prompts por minuto com o AI Query Builder.

### Como meus dados são usados e enviados para a OpenAI?
<!-- Contact Legal for changes. -->

Para gerar seu SQL, o Braze enviará seus prompts para a plataforma de API da OpenAI. Todas as consultas enviadas ao OpenAI pelo Braze são anônimas, o que significa que o OpenAI não poderá identificar de quem a consulta foi enviada, a menos que você inclua informações exclusivamente identificáveis no conteúdo que fornecer. Conforme detalhado nos [Compromissos da Plataforma de API da Open](https://openai.com/policies/api-data-usage-policies)AI, os dados enviados à API da OpenAI via Braze não são usados para treinar ou aprimorar seus modelos e serão excluídos após 30 dias. Certifique-se de aderir às políticas da OpenAI relevantes para você, incluindo a [Política de Uso](https://openai.com/policies/usage-policies). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA. 

## Escrever consultas SQL personalizadas {#custom-sql}

Escreva sua consulta SQL usando [a sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte a [referência da tabela]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obter uma lista completa das tabelas e colunas disponíveis para consulta.

Para visualizar os detalhes da tabela no Query Builder:

1. Na página **Query Builder**, abra o painel **Reference (Referência)** e selecione **Available Data Tables (Tabelas de dados disponíveis** ) para visualizar as tabelas de dados disponíveis e seus nomes.
3. Selecione <i class="fas fa-chevron-down" alt=""></i> **See Details** para visualizar a descrição da tabela e as informações sobre as colunas da tabela, como os tipos de dados.
4. Para inserir o nome da tabela em seu SQL, selecione <i class="fas fa-copy" title="Copiar nome da tabela para o editor SQL"></i>.

Para usar consultas pré-escritas fornecidas pelo Braze, selecione **Query Template (Modelo de consulta** ) ao criar um relatório pela primeira vez no Query Builder.

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
| `CANVAS_ID` | Nome da tela |
| `CANVAS_VARIATION_API_ID` | Nome da variante de tela |
| `CAMPAIGN_ID` | Nome da campanha |
{: .reset-td-br-1 .reset-td-br-2 }

Essa consulta recupera todos os três IDs e suas colunas de nome associadas com um máximo de 100 linhas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Preencher automaticamente o nome da variante da campanha

Se você quiser que o nome da variante da campanha seja preenchido automaticamente, inclua o nome da coluna `MESSAGE_VARIATION_API_ID` em sua consulta, como neste exemplo:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Solução de problemas

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe em sua consulta SQL
- Tempo limite de processamento (após 6 minutos)
    - Os relatórios que demorarem mais de 6 minutos para serem executados serão encerrados.
    - Se um relatório não atingir o tempo limite, tente limitar o intervalo de tempo em que está consultando os dados ou consulte um conjunto de dados mais específico.

## Uso de variáveis

Use variáveis para usar tipos de variáveis predefinidas no SQL para fazer referência a valores sem precisar copiar manualmente o valor. Por exemplo, em vez de copiar manualmente o ID de uma campanha para o editor SQL, você pode usar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para selecionar diretamente uma campanha em um menu suspenso na guia **Variables (Variáveis** ).

Depois que uma variável for criada, ela aparecerá na guia **Variables (Variáveis** ) do relatório do Query Builder. Os benefícios do uso de variáveis SQL incluem:

- Economize tempo criando uma variável de campanha para selecionar em uma lista ao criar seu relatório, em vez de colar os IDs de campanha.
- Troque os valores adicionando variáveis que lhe permitam reutilizar o relatório para casos de uso ligeiramente diferentes no futuro (como um evento personalizado diferente).
- Reduza o erro do usuário ao editar seu SQL, reduzindo a quantidade de edição necessária para cada relatório. Os colegas de equipe que se sentem mais à vontade com o SQL podem criar relatórios que podem ser usados por colegas de equipe menos técnicos.

### Diretrizes

As variáveis devem obedecer à seguinte sintaxe Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, em que `type` deve ser um dos tipos aceitos e `name` pode ser qualquer coisa que você escolher. Os rótulos dessas variáveis têm como padrão o nome da variável.

Por padrão, todas as variáveis são obrigatórias (e o relatório não será executado a menos que os valores das variáveis sejam selecionados), exceto o intervalo de datas, cujo padrão é os últimos 30 dias quando o valor não é fornecido.

### Tipos de variáveis

Os seguintes tipos de variáveis são aceitos:

- [Número](#number)
- [Intervalo de datas](#date-range)
- [Mensagens](#messaging)
- [Produtos](#products)
- [Eventos personalizados](#custom-events)
- [Propriedades de eventos personalizados](#custom-event-properties)
- [Espaço de trabalho](#workspace)
- [Catálogos](#catalogs)
- [Campos do catálogo](#catalog-fields)
- [Opções](#options)
- [Segmentos](#segments)
- [Cordas](#string)
- [Tags](#tags)

#### Número

- **Valor de reposição:** O valor fornecido, como `5.5`
- **Exemplo de uso:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Intervalo de datas

Se estiver usando `start_date` e `end_date`, eles devem ter o mesmo nome para que você possa usá-los como um intervalo de datas.

##### Valores de exemplo

O tipo de intervalo de datas pode ser relativo, data de início, data de término ou intervalo de datas.

Todos os quatro tipos são mostrados se `start_date` e `end_date` forem usados com o mesmo nome. Se apenas um for usado, somente os tipos relevantes serão exibidos.

| Tipo de intervalo de datas | Descrição | Valores necessários |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data de início | Especifica uma data de início | Requer `start_date` |
| Data final | Especifica uma data final | Requer `end_date` |
| Intervalo de datas | Especifica uma data inicial e uma data final | Requer os sites `start_date` e `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Valor de reposição:** Substitui `start_date` e `end_date` por um carimbo de data/hora Unix em segundos para uma data especificada em UTC, como `1696517353`.
- **Exemplo de uso:** Para todas as variáveis relativas, data de início, data de término e intervalo de datas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Você pode usar `start_date` ou `end_date` se não quiser um intervalo de datas.

#### Mensagens

Todas as variáveis de mensagens devem compartilhar o mesmo identificador quando você quiser unir o estado delas em um grupo.

##### Tela

Para selecionar um Canvas. Compartilhar o mesmo nome com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) que permite selecionar Canvas ou campanha.

- **Valor de reposição:** ID da tela BSON
- **Exemplo de uso:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Telas

Para selecionar várias telas. Compartilhar o mesmo nome com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

- **Valor de reposição:** Telas IDs BSON
- **Exemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campanha

Para selecionar uma campanha. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variáveis** para selecionar Canvas ou campanha.

- **Valor de reposição:** ID BSON da campanha
- **Exemplo de uso:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campanhas

Para campanhas de seleção múltipla. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variáveis** para selecionar Canvas ou campanha.

- **Valor de reposição:** Campanhas IDs BSON
- **Exemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de campanha

Para selecionar as variantes de campanha que pertencem à campanha selecionada. Ele deve ser usado em conjunto com uma variável de campanha ou de campanhas.

- **Valor de reposição:** IDs de API de variantes de campanha, cadeias de caracteres delimitadas por vírgulas, como `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de tela

Para selecionar as variantes do Canvas que pertencem a um Canvas escolhido. Ele deve ser usado com uma variável Canvas ou Canvases.

- **Valor de reposição:** IDs de API das variantes do Canvas, cadeias de caracteres delimitadas por vírgulas, como em `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Etapa da tela

Para selecionar uma etapa do Canvas que pertença a um Canvas escolhido. Ele deve ser usado com uma variável Canvas.

- **Valor de reposição:** ID da API da etapa do Canvas
- **Exemplo de uso:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Etapas do Canvas

Para selecionar as etapas do Canvas que pertencem aos Canvases escolhidos. Ele deve ser usado com uma variável Canvas ou Canvases.

- **Valor de reposição:** IDs de API das etapas do Canvas
- **Exemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
