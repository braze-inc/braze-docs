> Saiba como usar o Query Builder, para que você possa gerar relatórios usando dados do Braze no Snowflake. O Criador de consultas vem com [modelos de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) de SQL pré-construídas para você começar, ou você pode escrever suas próprias consultas de SQL personalizadas para desbloquear ainda mais insights.

## Pré-requisitos

Você precisará de [ permissões "View IPI"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) para usar o Query Builder, pois ele permite acesso direto a alguns dados de clientes.

## Uso do Query Builder

### Etapa 1: Criar uma consulta de SQL

Para criar uma nova consulta, acesse **Análise de dados** > **Query Builder** e selecione **Criar consulta de SQL**.

![As opções "Query Template" e "SQL Editor" encontradas no menu suspenso "Create SQL Query".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Se precisar de inspiração ou ajuda para elaborar sua consulta, escolha **Query Template (Modelo de consulta** ) e selecione um [modelo pré-fabricado]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). Para começar com uma consulta em branco, selecione **SQL Editor**.

Seu relatório recebe automaticamente um nome com a data e a hora atuais. Passe o mouse sobre o nome e selecione <i class="fas fa-pencil" alt="Edit"></i> para dar à sua consulta de SQL um nome significativo.

![Um exemplo de relatório com o nome "Engajamento de canal para maio de 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Etapa 2: Crie sua consulta

Ao criar sua consulta, você pode optar por obter ajuda da IA ou criá-la por conta própria.

{% tabs local %}
{% tab Usando o BrazeAI %}
O Criador de consultas com IA usa o [GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para sua consulta. Para gerar SQL com o Criador de consultas com IA:

1. Depois de criar um relatório no Criador de consultas, selecione a guia **Criador de consultas com IA**.
2. Digite seu prompt ou selecione um prompt de amostra e selecione **Gerar** para traduzir seu prompt para SQL.
3. Revise o SQL gerado para ter certeza de que está correto e, em seguida, selecione **Insert into Editor (Inserir no editor**).

![O construtor de consultas de IA SQL.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Dicas

- Familiarize-se com as tabelas de dados disponíveis [do Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). A solicitação de dados que não existem nessas tabelas pode fazer com que o ChatGPT crie uma tabela falsa.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esse recurso. O não cumprimento dessas regras causará um erro.
- Você pode enviar até 20 prompts por minuto com o Criador de consultas com IA.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Por conta própria %}
Escreva sua consulta de SQL usando [a sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte a [referência da tabela]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obter uma lista completa das tabelas e colunas disponíveis para consulta.

Para visualizar os detalhes da tabela no Query Builder:

1. Na página **do Construtor de consultas**, abra o painel **Referência** e selecione **Tabelas de dados disponíveis** para visualizar as tabelas de dados disponíveis e seus nomes.
3. Selecione <i class="fas fa-chevron-down" alt=""></i> **See Details** para visualizar a descrição da tabela e as informações sobre as colunas da tabela, como os tipos de dados.
4. Para inserir o nome da tabela em seu SQL, selecione <i class="fas fa-copy" title="Copiar nome da tabela para o editor SQL"></i>.

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

#### Solução de problemas

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe em sua consulta de SQL
- Tempo limite de processamento (após 6 minutos)
    - Os relatórios que demorarem mais de 6 minutos para serem executados serão encerrados.
    - Se um relatório não atingir o tempo limite, tente limitar o intervalo de tempo em que está consultando os dados ou consulte um conjunto de dados mais específico.
{% endtab %}
{% endtabs %}

### Etapa 3: Gerar seu relatório

Quando terminar de criar sua consulta, selecione **Run Query (Executar consulta**). Se não houver erros ou [tempo limite do relatório](#report-timeouts), será gerado um arquivo CSV a partir da consulta.

Para baixar o relatório CSV, selecione **Exportar**.

![O Criador de consultas mostra os resultados da consulta modelo "Engajamento e receita do canal nos últimos 30 dias".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Cada relatório só pode gerar resultados uma vez por dia. Se você executar o mesmo relatório várias vezes em um único dia do calendário, verá os mesmos resultados em cada relatório.
{% endalert %}

## Relatar tempos limite

Os relatórios que demorarem mais de seis minutos para serem executados serão encerrados. Se esta for a primeira consulta que você está executando em algum tempo, ela poderá levar mais tempo para ser processada e, portanto, terá uma probabilidade maior de atingir o tempo limite. Se isso acontecer, tente executar o relatório novamente.

Se o seu relatório continuar a apresentar tempo limite após várias tentativas, [entre em contato com o Suporte]({{site.baseurl}}/help/support#braze-support).

## Dados e resultados

Todas as consultas apresentam dados dos últimos 60 dias. Quando você exportar seus resultados, eles conterão apenas até 1.000 linhas. Para relatórios que exigem grandes quantidades de dados, você pode usar ferramentas como o [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) ou o [endpoint da API de exportação]({{site.baseurl}}/api/endpoints/export).

## Créditos para Snowflake

Cada empresa tem 5 créditos Snowflake disponíveis por mês, compartilhados em todos os espaços de trabalho. Uma pequena parte de um crédito do Snowflake é usada sempre que você executa uma consulta ou prévia uma tabela.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre os recursos. Por exemplo, os créditos nas extensões de segmento do SQL e no Criador de Consultas são independentes um do outro.
{% endalert %}

O uso de crédito está correlacionado ao tempo de execução de sua consulta de SQL. Quanto maior for o tempo de execução, maior será a porção de crédito do Snowflake que uma consulta custará. O tempo de execução pode variar de acordo com a complexidade e o tamanho de suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Os créditos não são usados ao escrever, editar ou salvar relatórios no editor Braze SQL. Seus créditos serão redefinidos para 5 no primeiro dia de cada mês, às 12 horas UTC. Você pode monitorar o uso de seu crédito mensal na parte superior da página do Criador de consultas.

![Construtor de consultas que mostra a quantidade de créditos usados no mês atual.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Quando você atinge o limite de crédito, não pode executar consultas, mas pode criar, editar e salvar relatórios de SQL. Se quiser comprar mais créditos do Criador de consultas, entre em contato com o gerente da sua conta.
