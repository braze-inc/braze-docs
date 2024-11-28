---
nav_title: "Extensões de segmento do SQL"
article_title: Extensões de segmento do SQL
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "Este artigo descreve como criar uma extensão de segmento SQL usando consultas do Snowflake."
tool: Segments
---

# Extensões de segmento do SQL

> Você pode gerar uma extensão de segmento usando consultas de SQL do Snowflake de dados [do Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/). O SQL pode ajudá-lo a desbloquear novos casos de uso de segmentos porque oferece a flexibilidade de descrever as relações entre os dados de maneiras que não são possíveis por meio de outros recursos de segmentação.

Como as extensões de segmento padrão, você pode consultar eventos dos últimos dois anos (730 dias) em sua extensão de segmento SQL.

## Tipos de extensões de segmento SQL

Há dois tipos de editores SQL para escolher ao criar sua extensão de segmento SQL: o SQL Editor e o Incremental SQL Editor.

- **Criação de extensões com o SQL Editor (atualização completa):** Toda vez que seu segmento for atualizado, o Braze consultará todos os dados disponíveis para atualizar seu segmento, o que usará mais créditos do que as atualizações incrementais. As extensões de atualização completa podem regenerar automaticamente a associação diariamente, mas não podem ser atualizadas usando a atualização incremental.
- **Criação de extensões com o Incremental SQL Editor (atualização incremental):** A atualização incremental calcula apenas os dados dos últimos dois dias, o que é mais econômico e usa menos créditos a cada vez. Ao criar um segmento SQL de atualização incremental, você pode configurá-lo para regenerar automaticamente a associação diariamente. <br><br>O principal benefício das extensões com atualização incremental é que você pode configurar seu segmento para atualizar automaticamente a associação diariamente. Os segmentos criados com nosso editor SQL regular só podem ter sua associação atualizada manualmente. Isso ajuda a reduzir o custo de uma atualização diária de dados para as extensões de segmento do SQL.

{% alert tip %}
Você pode fazer uma atualização manual completa em todos os segmentos SQL criados em qualquer um dos editores SQL.
{% endalert %}

## Criação de extensões de segmento SQL

{% tabs local %}
{% tab Atualização completa %}

Para criar uma extensão de segmento SQL totalmente atualizada:

1. Acesse **Público** > **Extensões de segmento**.
{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Engajamento** > **Segmentos** > **Extensões de segmento**.
{% endalert %}

{:start="2"}
2\. Clique em **Create New Extension (Criar nova extensão** ) e selecione **Full refresh (Atualização completa**).<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. Adicione um nome para sua extensão de segmento e insira seu SQL. Consulte a seção [Escrevendo SQL](#writing-sql) para obter os requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de segmento SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4\. Salve sua extensão de segmento.

{% endtab %}
{% tab Atualização incremental %}

O editor SQL de atualização incremental permite que as agregações de consultas do usuário ocorram por data para um evento dentro de um determinado período de tempo. Para criar uma extensão de segmento SQL de atualização incremental:

1. Acesse **Público** > **Extensões de segmento**.
{% alert note %}

Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Engajamento** > **Segmentos** > **Extensões de segmento**.
{% endalert %}

{:start="2"}
2\. Clique em **Create New Extension (Criar nova extensão** ) e selecione **Incremental refresh (Atualização incremental)**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. Adicione um nome para sua extensão de segmento e insira seu SQL. Consulte a seção [Escrevendo SQL](#writing-sql) para obter os requisitos e recursos.<br><br>
   ![Editor SQL mostrando um exemplo de extensão de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4\. Se desejar, selecione **Regenerate Extension Daily (Regenerar extensão diariamente**).<br><br>
   ![Caixa de seleção para regenerar a extensão diariamente.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Quando selecionado, o Braze atualizará automaticamente a associação ao segmento todos os dias. Isso significa que todos os dias, à meia-noite no fuso horário da sua empresa (com uma possível postergação de uma hora), o Braze verificará se há novos usuários no seu segmento e os adicionará automaticamente ao seu segmento. Se uma extensão de segmento não tiver sido usada em 7 dias, a Braze pausará automaticamente a regeneração diária. Uma extensão de segmento não utilizada é aquela que não faz parte de uma campanha ou de um Canvas (a campanha ou o Canvas não precisa estar ativo para que a extensão seja considerada "usada").<br><br>
5\. Salve sua extensão de segmento.

{% endtab %}

{% tab Gerador de IA SQL %}

{% alert note %}
O gerador de IA SQL está atualmente disponível como um recurso beta. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar dessa avaliação beta.
{% endalert %}

O gerador de IA SQL aproveita [o GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para seu segmento SQL.

![Gerador de IA SQL com o prompt "Usuários que receberam uma notificação no mês passado"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Para usar o gerador de IA SQL, faça o seguinte:

1. Clique em **Launch IA SQL Generator** depois de criar um [segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) usando a atualização completa ou incremental.
2. Digite seu prompt e clique em **Generate (Gerar** ) para traduzir seu prompt em SQL.
3. Revise o SQL gerado para ter certeza de que está correto e, em seguida, salve o segmento.

### Exemplos de prompts
- Usuários que receberam um e-mail no último mês
- Usuários que fizeram menos de cinco compras no último ano

### Dicas
- Familiarize-se com as tabelas de dados disponíveis [do Snowflake]({{site.baseurl}}/sql_segments_tables/). A solicitação de dados que não existem nessas tabelas pode fazer com que o ChatGPT crie uma tabela falsa.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) para esse recurso. O não cumprimento dessas regras causará um erro. Por exemplo, seu código SQL deve selecionar a coluna `user_id`. Iniciar seu prompt com "users who" pode ajudar.
- Você pode enviar até 20 prompts por minuto com o IA SQL Generator.

### Como meus dados são usados e enviados para a OpenAI?

Para gerar seu SQL, a Braze enviará seus prompts para a API Platform da OpenAI. Todas as consultas enviadas pela Braze à OpenAI são anônimas, o que significa que a OpenAI não poderá identificar o remetente da consulta, a menos que você inclua informações exclusivamente identificáveis no conteúdo fornecido. Conforme detalhado nos [Compromissos da Plataforma de API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Siga às políticas da OpenAI relevantes para você, incluindo a [Política de Uso](https://openai.com/policies/usage-policies). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA.
{% endtab %}
{% endtabs %}

{% alert note %}
As consultas de SQL que demorarem mais de 20 minutos para serem executadas serão encerradas.
{% endalert %}

Quando a extensão terminar de processar, você poderá [criar um segmento][4] usando sua extensão de segmento e direcionar esse novo segmento com suas campanhas e Canvas.

## Escrevendo SQL

Sua consulta de SQL deve ser escrita usando [a sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consulte a [referência da tabela]({{site.baseurl}}/sql_segments_tables/) para obter uma lista completa das tabelas e colunas disponíveis para consulta.

{% alert important %}
Observe que as tabelas disponíveis para consulta contêm apenas dados de eventos. Se desejar consultar os atributos do usuário, deverá combinar seu segmento SQL com filtros de atributos personalizados do [segmentador clássico]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
{% endalert %} 

{% tabs %}
{% tab Editor SQL %}

Além disso, seu SQL deve obedecer às seguintes regras:

- Escreva uma única instrução SQL. Não inclua nenhum ponto e vírgula.
- Seu SQL deve selecionar apenas uma coluna: a coluna `user_id`. Isso significa que seu SQL deve conter:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Não é possível consultar usuários com zero eventos, o que significa que qualquer consulta para usuários que tenham feito um evento menos de X vezes precisaria seguir essa solução alternativa:
   1. Escreva uma consulta para selecionar usuários que tenham o evento MAIS de X vezes.
   2. Ao fazer referência à extensão de segmento em seu segmento, selecione `doesn't include` para inverter o resultado.

{% endtab %}
{% tab Editor SQL incremental %}

Todas as consultas de atualização incremental consistem em duas partes: uma consulta e detalhes do esquema.

1. No editor, escreva uma consulta que selecione `user_id`s de sua tabela desejada.
2. Adicione detalhes do esquema selecionando um **Operador**, **Número de vezes** e **Período de tempo** nos campos acima do editor. A consulta verificará se a soma da coluna agregada atende a uma determinada condição especificada pelos espaços reservados {% raw %}`{{operator}}` e `{{number of times}}`{% endraw %}. Isso funciona de forma semelhante ao fluxo de trabalho para a criação de extensões de segmento clássicas.<br><br>
   - **Operador:** Indique se o evento ocorreu mais do que, menos do que ou igual a um número de ocorrências.<br>
   ![Campo do operador com "Mais de" selecionado.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Número de vezes:** Quantas vezes você gostaria de avaliar o evento em relação ao operador.<br>
   ![Número de vezes com "5" inserido.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Período:** Número de dias, de 1 a 730, em que você deseja verificar as instâncias do evento. Esse período de tempo se refere a dias passados em relação ao dia atual. O exemplo a seguir mostra a consulta de usuários que realizaram o evento mais de 5 vezes nos últimos 365 dias.<br>
   ![Campo de período de tempo com "365" inserido.]({% image_buster /assets/img_archive/sql_segments_period.png %})

No exemplo a seguir, o segmento resultante conteria usuários que realizaram o evento `favorited` mais de 3 vezes nos últimos 30 dias, após uma data especificada.

![Editor SQL mostrando um exemplo de extensão de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Prévia SQL de uma extensão de segmento SQL incremental.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### Regras adicionais

Além disso, sua consulta de atualização incremental deve obedecer às seguintes regras:

- Escreva uma única instrução SQL. Não inclua nenhum ponto e vírgula.
- Seu segmento SQL incremental seria capaz de se referir a apenas um único evento. Seus menus suspensos para data e contagem referem-se ao evento escolhido.
- Seu SQL deve ter as seguintes colunas: `user_id`, `$start_date`, e uma função de agregação (como `COUNT`). Qualquer SQL salvo sem esses três campos resultará em um erro.

{% alert tip %}
Os segmentos de atualização incremental levam em conta eventos tardios, que são eventos que ocorreram há mais de dois dias (por exemplo, eventos SDK que não foram enviados no momento em que foram capturados).
{% endalert %}

{% endtab %}
{% endtabs %}

## Pré-visualização de resultados

Antes de salvar, você pode executar uma prévia de sua consulta. As prévias de consultas são automaticamente limitadas a 100 linhas e atingem o tempo limite após 60 segundos. O requisito da coluna `user_id` não se aplica ao executar uma prévia.

Para extensões de segmento SQL incrementais, a prévia não incluirá os critérios adicionais de seu operador, o número de vezes e os campos de período de tempo.

## Gerenciamento de extensões de segmento do SQL

Na página **Extensões de segmento**, os segmentos gerados usando SQL são indicados com <i class="fas fa-code" alt="SQL Segment Extension"></i> ao lado do nome.

Selecione uma extensão de segmento SQL para visualizar onde a extensão está sendo usada, arquivar a extensão ou [atualizar manualmente a associação do segmento](#refreshing-segment-membership).

![A seção Uso de mensagens do editor SQL mostra onde o segmento SQL está sendo usado.][3]

### Atualização da associação de segmentos

Para atualizar a associação de segmentos de qualquer extensão de segmento criada usando o SQL, abra a extensão de segmento e selecione **Refresh (Atualizar**). Somente as extensões de segmento SQL de atualização incremental podem ser regeneradas automaticamente (se selecionadas).

{% alert tip %}
Se tiver criado um segmento no qual espera que os usuários entrem e saiam regularmente, atualize manualmente a extensão de segmento que ele usa antes de direcionar esse segmento em uma campanha ou Canva.
{% endalert %}

## Monitoramento do uso de seus SQL Segments

Cada espaço de trabalho da Braze tem 5 créditos Snowflake disponíveis por mês. Se precisar de mais créditos, entre em contato com o gerente da sua conta. Os créditos são usados sempre que você atualiza, ou salva e atualiza, a associação de um SQL Segment. Os créditos não são usados quando você executa prévias em um SQL Segment ou salva ou atualiza uma extensão de segmento clássica.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre os recursos. Por exemplo, os créditos nas extensões de segmento do SQL e no Criador de Consultas são independentes um do outro.
{% endalert %}

O uso de crédito está correlacionado ao tempo de execução de sua consulta de SQL. Quanto mais longo for o tempo de execução, mais créditos a consulta custará. O tempo de execução pode variar de acordo com a complexidade e o tamanho de suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Para economizar créditos, faça uma prévia de sua consulta para garantir que ela esteja correta antes de salvar a extensão de segmento SQL.

Seus créditos serão redefinidos para 5 no primeiro dia de cada mês, às 12 horas UTC. Você pode monitorar o uso do seu crédito durante o mês no painel de uso de créditos. Na página **Extensões de segmento**, clique em <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![Painel Uso de crédito do SQL na página Extensões de segmento do SQL][5]{: style="max-width:60%"}

O seguinte ocorrerá quando seus créditos chegarem a zero:

- Todas as extensões de segmento do SQL configuradas para atualização automática deixam de ser atualizadas, afetando a associação desses segmentos e todas as campanhas ou telas direcionadas a esses segmentos.
- Você só pode salvar novas extensões de segmento do SQL como rascunhos durante o restante do mês.

Todos os usuários da empresa que criaram um SQL Segment e os administradores da sua empresa receberão um envio de e-mail de notificação quando você tiver usado 50%, 80% e 100% dos seus créditos. Depois que seus créditos forem redefinidos no início do mês seguinte, você poderá criar mais SQL Segments, e as atualizações automáticas serão retomadas.

Se quiser comprar mais créditos do SQL Segment ou extensões de segmento adicionais, entre em contato com o gerente da sua conta.

## Solução de problemas

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe em sua consulta de SQL
- O SQL não segue as [regras do SQL](#writing-sql)
- Tempo limite de processamento (após 20 minutos)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
