---
nav_title: variáveis SQL
article_title: Variáveis do Construtor de Consultas SQL
page_order: 2
page_type: reference
description: "Aprenda a usar variáveis no Construtor de Consultas, para que você possa reutilizar suas consultas e evitar codificar dados diretamente em seu código."
tool: Reports
---

# Variáveis do Construtor de Consultas SQL

> Aprenda a usar variáveis SQL no Construtor de Consultas, para que você possa reutilizar suas consultas e evitar codificar dados diretamente em seu código.

## Por que usar variáveis SQL?

Os benefícios de usar variáveis SQL incluem:

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
| `variable_type`   | O tipo de variável pré-definido que você gostaria de usar, como `campaign` ou `catalog_fields`. Para a lista completa, veja [Tipos de variáveis suportadas](#variable-types). |
| `custom_label` | O rótulo usado para identificar a variável na aba **Variáveis** do seu Construtor de Consultas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

No exemplo a seguir, o número total de usuários entre o primeiro e o último dia de um mês é consultado para uma campanha. Cada variável será atribuída a um valor na próxima etapa.

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

Por padrão, a aba **Variáveis** não é exibida no Construtor de Consultas. Ela só aparece após adicionar sua primeira variável à consulta. Lá, você poderá atribuir um valor a ela. Os valores específicos que você pode escolher dependerão do [tipo](#variable-types) dessa variável específica.

No exemplo a seguir, a campanha "Lançamento de Recursos de Verão" é atribuída como um valor, junto com os primeiros e últimos dias de junho de 2025.

![A aba "Variável" no Construtor de Consultas mostrando o exemplo dado.]({% image_buster /assets/img/query_builder_example.png %})

## Tipos de variáveis gerais {#variable-types}

### Número

`number` pode ser usado em combinação com outras variáveis que não são string. Aceita qualquer número positivo ou negativo, incluindo números decimais, como `5.5`.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### String

Para alterar os valores repetitivos da string entre as execuções do relatório. Use essa variável para evitar a codificação de um valor várias vezes em seu SQL.

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

Para mostrar opções como botões de rádio em vez de um menu suspenso de seleção na guia **Variables (Variáveis** ). Isso não pode ser usado sozinho—deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Um exemplo de botão de opção renderizado no Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Seleção múltipla

Para saber se o menu suspenso de seleção permite uma seleção única ou múltipla. Isso não pode ser usado sozinho—deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Um exemplo de lista de múltipla seleção renderizada no Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Opções 

Para fornecer a lista de opções selecionáveis na forma de um rótulo e valor. O rótulo é o que é exibido e o valor é o que substitui a variável quando a opção é selecionada. Isso não pode ser usado sozinho—deve ser usado em combinação com uma [lista](#list).

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Tipos de variáveis específicos do Braze

### Período

Para exibir um calendário para selecionar datas. Substitua `start_date` e `end_date` por um timestamp Unix em segundos para uma data especificada em UTC, como `1696517353`. Opcionalmente, você pode definir apenas um `start_date` ou `end_date` para exibir apenas uma única data no calendário. Se os rótulos do seu `start_date` e `end_date` não coincidirem, eles serão tratados como duas datas separadas, em vez de um intervalo de datas.

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Você pode definir o intervalo de datas para qualquer uma das seguintes opções. Se ambos `start_date` e `end_date` forem usados e compartilharem o mesmo rótulo, todas as opções serão exibidas. Caso contrário, se apenas um for usado, então apenas a opção especificada será exibida.

| Opção | Descrição | Valores necessários |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data inicial | Especifica uma data de início | Requer `start_date` |
| Data final | Especifica uma data final | Requer `end_date` |
| Período | Especifica uma data inicial e uma data final | Requer os sites `start_date` e `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seu Liquid será usado para exibir um calendário dentro do intervalo de datas dado:

![Um exemplo de calendário renderizado no Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campanhas

{% tabs local %}
{% tab one campaign %}
Para selecionar uma campanha. Compartilhar o mesmo rótulo com um Canvas resultará em um botão de opção dentro da aba **Variáveis** para selecionar Canvas ou campanha.

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
Para campanhas de seleção múltipla. Compartilhar o mesmo rótulo com um Canvas resultará em um botão de opção dentro da aba **Variáveis** para selecionar Canvas ou campanha.

- **Valor de substituição:** IDs BSON de campanhas

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
Para selecionar variantes de campanha que pertencem à campanha selecionada. Ele deve ser usado em conjunto com uma variável de campanha ou de campanhas.

- **Valor de substituição:** IDs da API de variantes de campanha, strings delimitadas por vírgulas, como `api-id1, api-id2`.

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
Todas as variáveis de campanha e Canvas devem usar os mesmos identificadores para sincronizar estados dentro de um único grupo.
{% endalert %}

### Canvas

{% tabs local %}
{% tab one canvas %}
Para selecionar um Canva. Compartilhar o mesmo rótulo com uma campanha resultará em um botão de opção dentro da aba **Variáveis** para selecionar Canvas ou campanha.

- **Valor de substituição:** ID do BSON da tela

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
Para selecionar várias telas. Compartilhar o mesmo rótulo com uma campanha resultará em um botão de opção dentro da aba **Variáveis** para selecionar Canvas ou campanha.

- **Valor de substituição:** Canvas IDs BSON

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
Para selecionar as variantes do Canvas que pertencem a um Canvas escolhido. Ele deve ser usado com uma variável Canvas ou Canvases. Defina para um ou mais IDs de API de variantes Canvas, como uma string separada por vírgulas, como em `api-id1, api-id2`.

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
Para selecionar uma etapa do Canva que pertença a um Canvas escolhido. Ele deve ser usado com uma variável Canva.

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
Todas as variáveis de campanha e Canvas devem usar os mesmos identificadores para sincronizar estados dentro de um único grupo.
{% endalert %}

### Produtos

`products` é usado para selecionar um ou mais produtos do painel do Braze.

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

Selecione um ou mais eventos personalizados ou propriedades de eventos personalizados de uma lista.

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
`custom_event_properties` é usado para selecionar uma ou mais propriedades do evento personalizado atualmente selecionado.  Requer uma variável `custom_events` definida.

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

`workspace` é usado para selecionar um único espaço de trabalho do painel do Braze.

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

Selecione um ou mais catálogos ou campos de catálogo de uma lista.

{% tabs local %}
{% tab catalogs %}
`catalogs` é usado para selecionar um ou mais catálogos do painel do Braze.

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

{% tab catalog fields %}
`catalog_fields` é usado para definir um ou mais campos do catálogo atualmente selecionado. Requer uma variável `catalogs` definida.

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

Para selecionar segmentos que tenham [a análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) ativada. Defina isso para o ID de análise de segmento, que corresponde aos IDs armazenados na coluna `user_segment_membership_ids` nas tabelas onde essa coluna está disponível.

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

Para selecionar tags para campanhas e telas. Defina para Campanhas e Canvases com IDs BSON separados por vírgulas entre aspas simples que estão associados às tags selecionadas.

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

Metadados podem ser anexados a uma variável para alterar seu comportamento, adicionando os metadados com um caractere pipe ( | ) após o rótulo da variável. A ordem dos metadados não importa e você pode anexar qualquer número deles. Além disso, todos os tipos de metadados podem ser usados para qualquer variável, exceto os metadados especiais que são específicos para determinadas variáveis (isso será indicado nesses casos). O uso de todos os metadados é opcional e é usado para alterar o comportamento padrão da variável.

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

Para saber se o valor de uma variável está preenchido. Isso é útil para variáveis opcionais onde você deseja interromper uma condição se o valor de uma variável não estiver preenchido. Pode ser definido como `true` ou `false` dependendo do valor da outra variável.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` e `name` referem-se à variável referenciada. Por exemplo, para interromper o seguinte variável opcional: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

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

### Obrigatória

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

### Incluir aspas

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

Para especificar o texto de espaço reservado mostrado no campo de entrada da variável.

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Descrição

Para especificar o texto de descrição mostrado abaixo do campo de entrada da variável.

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
