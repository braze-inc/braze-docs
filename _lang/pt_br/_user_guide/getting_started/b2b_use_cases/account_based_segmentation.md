---
nav_title: Segmentação baseada em contas
article_title: Configuração da segmentação baseada em contas
page_order: 2
page_type: reference
description: "Saiba como usar vários recursos do Braze para potencializar seus casos de uso de segmentação baseada em contas B2B."
---

# Configuração da segmentação baseada em contas

> Esta página mostra como usar vários recursos do Braze para potencializar seus casos de uso de segmentação baseada em contas B2B.

Você pode fazer a segmentação baseada em contas B2B de duas maneiras, dependendo de como você configurou seu [modelo de dados B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/):

- Ao usar [catálogos para seus business objects](#option-1-when-using-catalogs-for-your-business-objects)
- Ao usar [fontes conectadas para seus business objects](#option-2-when-using-connected-sources-for-your-business-objects)

## Configuração da segmentação baseada em contas B2B

### Opção 1: Ao usar catálogos para seus business objects

#### Segmentação básica de modelos SQL

Para ajudá-lo a começar, criamos modelos básicos de SQL para segmentação simples baseada em contas.

Digamos que você queira segmentar os usuários que são funcionários de uma conta corporativa de destino. 

1. Vá para **Audience** > **Segment Extensions** > **Create New Extension** > **Start with a template** e selecione o modelo **Catalog segment for events**. <br><br> \!["Select a Template" modal com opções de segmento de catálogo para eventos ou compras.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>O editor SQL é preenchido automaticamente com um modelo que une os dados de eventos do usuário aos dados do catálogo para segmentar os usuários que se envolvem com determinados itens do catálogo. <br><br>\![Um editor SQL para uma nova extensão com uma guia "Variables" aberta.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Use a guia **Variables (Variáveis** ) para fornecer os campos necessários para seu modelo antes de gerar seu segmento.<br><br>Para que o Braze identifique os usuários com base no envolvimento deles com os itens do catálogo, é necessário fazer o seguinte:
- Selecione um catálogo que contenha um campo de catálogo
- Selecione um evento personalizado que contenha uma propriedade de evento
- Corresponder os valores de propriedade do campo e do evento de seu catálogo

##### Diretrizes de variáveis para casos de uso B2B

Selecione as seguintes variáveis para um caso de uso de segmentação baseada em contas B2B:

| Variável | Propriedade |
| --- | --- |
| Catálogo | Catálogo de contas |
| Campo de catálogo | Id |
| Evento personalizado | account_linked |
| Propriedade de evento personalizado | account_id |
| (Em Filtrar resultados SQL) Campo do catálogo | Classificação |
| (Em Filtrar resultados SQL) Valor | Empresa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segmentação SQL sofisticada

Para obter uma segmentação mais sofisticada ou complexa, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). Para ajudá-lo a começar, aqui estão alguns modelos de SQL que você pode usar para ajudá-lo a obter uma vantagem inicial com a segmentação baseada em contas B2B:

1. Crie um segmento comparando dois filtros em um único catálogo (por exemplo, usuários que trabalham no setor de restaurantes para uma conta de nível empresarial). Você deve incluir a ID do catálogo e a ID do item.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
; 
```

{: start="2"}
2\. Crie um segmento comparando dois filtros em dois catálogos separados (como usuários associados a contas-alvo empresariais que tenham uma oportunidade aberta de "Estágio 3").

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### Opção 2: Ao usar fontes conectadas para seus business objects

Para obter informações básicas sobre como usar fontes conectadas na segmentação, consulte [Extensões de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Use os modelos abordados em [Quando usar catálogos](#option-1-when-using-catalogs-for-your-business-objects) para se inspirar em como formatar as tabelas de origem, pois você pode formatá-las da maneira que quiser.

## Usar sua extensão baseada em conta em um segmento

Depois de criar a segmentação no nível da conta nas etapas acima, você poderá incluir diretamente essas Extensões de Segmento em seus critérios de segmentação. Também é fácil acrescentar critérios demográficos incrementais do usuário, como função, envolvimento com campanhas anteriores e muito mais. Para obter mais informações, consulte [Uso de sua extensão em um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment).

