---
nav_title: Variáveis SQL
article_title: Variáveis SQL do Query Builder
page_order: 2
page_type: reference
description: "Saiba como usar variáveis no Query Builder, para que você possa reutilizar suas consultas e evitar a codificação de dados em seu código."
tool: Reports
---

# Variáveis SQL do Query Builder

> Saiba como usar variáveis SQL no Query Builder, para que você possa reutilizar suas consultas e evitar a codificação de dados em seu código.

## Por que usar variáveis SQL?

Os benefícios do uso de variáveis SQL incluem:

- Economize tempo criando uma variável de campanha para selecionar em uma lista ao criar seu relatório, em vez de colar os IDs de campanha.
- Troque os valores adicionando variáveis que lhe permitam reutilizar o relatório para casos de uso ligeiramente diferentes no futuro (como um evento personalizado diferente).
- Reduza o erro do usuário ao editar seu SQL, reduzindo a quantidade de edição necessária para cada relatório. Os colegas de equipe que se sentem mais à vontade com o SQL podem criar relatórios que podem ser usados por colegas de equipe menos técnicos.

## Uso de variáveis

### Etapa 1: Adicionar uma variável

Para adicionar uma variável à sua consulta, use a seguinte sintaxe:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Substitua o seguinte:

| Espaço reservado      | Descrição                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | O tipo de variável predefinida que você gostaria de usar, como `campaign` ou `catalog_fields`. Para obter a lista completa, consulte [Tipos de variáveis compatíveis](#variable-types). |
| `custom_label` | O rótulo usado para identificar a variável na guia **Variables (Variáveis** ) do Query Builder. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

No exemplo a seguir, o número total de usuários entre o primeiro e o último dia de um mês é consultado para uma campanha. Cada variável receberá um valor na próxima etapa.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Etapa 2: Atribuir um valor

Por padrão, a guia **Variables (Variáveis** ) não é exibida no Query Builder. Ele só aparece depois de adicionar sua primeira variável à consulta. Lá, você poderá atribuir um valor a ele. Os valores específicos que você pode escolher dependerão do [tipo](#variable-types) da variável específica.

No exemplo a seguir, a campanha "Summer Feature Launch" é atribuída como um valor, juntamente com o primeiro e o último dias de junho de 2025.

A guia "Variable" (Variável) no Query Builder mostra o exemplo dado.]({% image_buster /assets/img/query_builder_example.png %})

## Tipos de variáveis gerais {#variable-types}

### Número

`number` pode ser usada em combinação com outras variáveis que não sejam strings. Aceita qualquer número positivo ou negativo, inclusive números decimais, como `5.5`.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Cordas

Para alterar valores de cadeias repetitivas entre execuções de relatórios. Use essa variável para evitar a codificação de um valor várias vezes em seu SQL.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Lista {#list}

Para selecionar em uma lista de opções.

{% tabs local %}
{% tab choose one %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choose multiple %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Botão de rádio

Para mostrar opções como botões de rádio em vez de um menu suspenso de seleção na guia **Variables (Variáveis** ). Isso não pode ser usado isoladamente - deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

\![Um exemplo de botão de rádio renderizado no Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Seleção múltipla

Para saber se o menu suspenso de seleção permite uma seleção única ou múltipla. Isso não pode ser usado isoladamente - deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

\![Um exemplo de lista de seleção múltipla renderizada no Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Opções 

Para fornecer a lista de opções selecionáveis na forma de um rótulo e valor. O rótulo é o que é exibido e o valor é o que substitui a variável quando a opção é selecionada. Isso não pode ser usado isoladamente - deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Tipos de variáveis específicas do Brasil

### Intervalo de datas

Para exibir um calendário para selecionar datas. Substitua `start_date` e `end_date` por um carimbo de data/hora Unix em segundos para uma data especificada em UTC, como `1696517353`. Opcionalmente, você pode definir apenas um `start_date` ou `end_date` para exibir apenas uma única data no calendário. Se os rótulos dos sites `start_date` e `end_date` não coincidirem, eles serão tratados como duas datas separadas, em vez de um intervalo de datas.

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Você pode definir o intervalo de datas para qualquer uma das seguintes opções. Se ambos `start_date` e `end_date` forem usados e compartilharem o mesmo rótulo, todas as opções serão mostradas. Caso contrário, se apenas uma for usada, somente a opção especificada será exibida.

| Opção | Descrição | Valores necessários |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data de início | Especifica uma data de início | Requer `start_date` |
| Data final | Especifica uma data final | Requer `end_date` |
| Intervalo de datas | Especifica uma data inicial e uma data final | Requer os sites `start_date` e `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seu Liquid será usado para exibir um calendário dentro do intervalo de datas fornecido:

\![Um exemplo de calendário renderizado no Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campanhas

{% tabs local %}
{% tab one campaign %}
Para selecionar uma campanha. Compartilhar o mesmo rótulo com um Canvas resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple campaigns %}
Para campanhas de seleção múltipla. O compartilhamento do mesmo rótulo com um Canvas resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

- **Valor de reposição:** Campanhas IDs BSON

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campaign variants %}
Para selecionar as variantes de campanha que pertencem à campanha selecionada. Ele deve ser usado em conjunto com uma variável de campanha ou de campanhas.

- **Valor de reposição:** IDs de API de variantes de campanha, cadeias de caracteres delimitadas por vírgulas, como `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas as variáveis de campanha e do Canvas devem usar os mesmos identificadores para sincronizar estados em um único grupo.
{% endalert %}

### Telas

{% tabs local %}
{% tab one canvas %}
Para selecionar um Canvas. Compartilhar o mesmo rótulo com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) que permite selecionar Canvas ou campanha.

- **Valor de reposição:** ID da tela BSON

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvases %}
Para selecionar várias telas. Compartilhar o mesmo rótulo com uma campanha resultará em um botão de opção na guia **Variables (Variáveis** ) para selecionar Canvas ou campanha.

- **Valor de reposição:** Telas IDs BSON

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab canvas variants %}
Para selecionar as variantes do Canvas que pertencem a um Canvas escolhido. Ele deve ser usado com uma variável Canvas ou Canvases. Defina uma ou mais IDs de API de variantes do Canvas, como uma cadeia de caracteres separada por vírgulas, como em `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab one canvas step %}
Para selecionar uma etapa do Canvas que pertença a um Canvas escolhido. Ele deve ser usado com uma variável Canvas.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvas steps %}
Para selecionar as etapas do Canvas que pertencem aos Canvases escolhidos. Ele deve ser usado com uma variável Canvas ou Canvases.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas as variáveis de campanha e do Canvas devem usar os mesmos identificadores para sincronizar estados em um único grupo.
{% endalert %}

### Produtos

`products` é usado para selecionar um ou mais produtos do painel de controle do Braze.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab example %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Eventos personalizados

Selecione um ou mais eventos personalizados ou propriedades de eventos personalizados em uma lista.

{% tabs local %}
{% tab event %}
`custom_events` é usado para selecionar um ou mais eventos personalizados do painel do Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab properties %}
`custom_event_properties` é usado para selecionar uma ou mais propriedades do evento personalizado atualmente selecionado.  Requer um conjunto de variáveis `custom_events`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espaço de trabalho

`workspace` é usado para selecionar um único espaço de trabalho no painel do Braze.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catálogos

Selecione um ou mais catálogos ou campos de catálogos em uma lista.

{% tabs local %}
{% tab catologs %}
`catalogs` é usado para selecionar um ou mais catálogos no painel de controle do Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab catolog fields %}
`catalog_fields` é usado para definir um ou mais campos do catálogo atualmente selecionado. Requer um conjunto de variáveis `catalogs`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segmentos

Para selecionar segmentos que têm [o rastreamento do Analytics]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) ativado. Defina isso como a ID analítica do segmento, que corresponde às IDs armazenadas na coluna `user_segment_membership_ids` nas tabelas em que essa coluna está disponível.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Tags

Para selecionar tags para campanhas e Canvases. Defina como Campaigns and Canvases (Campanhas e telas) com IDs BSON separadas por vírgula e com aspas simples que estão associadas às tags selecionadas.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Metadados variáveis

Os metadados podem ser anexados a uma variável para alterar seu comportamento, anexando os metadados com um caractere pipe ( | ) após o rótulo da variável. A ordem dos metadados não importa e você pode anexar qualquer número deles. Além disso, todos os tipos de metadados podem ser usados para qualquer variável, exceto os metadados especiais que são específicos para determinadas variáveis (isso será indicado nesses casos). O uso de todos os metadados é opcional e é usado para alterar o comportamento da variável padrão.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Booleano

Para saber se o valor de uma variável está preenchido. Isso é útil para variáveis opcionais em que você deseja interromper uma condição se o valor de uma variável não for preenchido. Pode ser definido como `true` ou `false`, dependendo do valor da outra variável.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` e `name` referem-se à variável referenciada. Por exemplo, para causar curto-circuito na seguinte variável opcional: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visível

Para saber se as variáveis estão visíveis. Todas as variáveis são visíveis por padrão na guia **Variables (Variáveis** ), onde você pode inserir valores.

Há diversas variáveis especiais cujo valor depende de outra variável, como, por exemplo, se outra variável tem um valor. Essas variáveis especiais são marcadas como não visíveis para que não sejam exibidas na guia **Variáveis**.

{% tabs %}
{% tab usage %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Necessário

Para saber se as variáveis são obrigatórias por padrão. Um valor vazio para uma variável geralmente leva a uma consulta incorreta.

{% tabs %}
{% tab usage %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Pedido

Para selecionar a posição da variável na guia **Variáveis**.

{% tabs %}
{% tab usage %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Incluir cotações

{% tabs local %}
{% tab single quotes %}
Para cercar os valores de uma variável com aspas simples.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab double quotes %}
Para envolver os valores de uma variável com aspas duplas.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espaço reservado

Para especificar o texto do espaço reservado mostrado no campo de entrada da variável.

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Descrição

Para especificar o texto de descrição mostrado no campo de entrada da variável.

{% tabs %}
{% tab usage %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valor padrão

Para especificar o valor padrão da variável quando nenhum valor for especificado.

{% tabs %}
{% tab usage %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Ocultar rótulo

Para ocultar o rótulo da variável.

{% tabs %}
{% tab usage %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
