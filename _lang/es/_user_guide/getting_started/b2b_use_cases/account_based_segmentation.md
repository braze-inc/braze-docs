---
nav_title: Segmentación basada en cuentas
article_title: Configuración de la segmentación basada en cuentas
page_order: 2
page_type: reference
description: "Aprende a utilizar varias características de Braze para potenciar tus casos de uso de segmentación basada en cuentas B2B."
---

# Configuración de la segmentación basada en cuentas

> Esta página muestra cómo utilizar varias características de Braze para potenciar tus casos de uso de segmentación basada en cuentas B2B.

Puedes hacer la segmentación B2B basada en cuentas de dos formas, dependiendo de cómo configures tu [modelo de datos B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/):

- Cuando utilices [catálogos para tus objetos de negocio](#option-1-when-using-catalogs-for-your-business-objects)
- Cuando utilices [fuentes conectadas para tus objetos de negocio](#option-2-when-using-connected-sources-for-your-business-objects)

## Configuración de la segmentación B2B basada en cuentas

### Opción 1: Cuando utilices catálogos para tus objetos de negocio

#### Segmentación básica de plantillas SQL

Para ayudarte a empezar, hemos creado plantillas SQL básicas para una segmentación sencilla basada en cuentas.

Supongamos que quieres segmentar a los usuarios que son empleados de una cuenta de empresa objetivo. 

1. Ve a **Audiencia** > **Extensiones de segmento** > **Crear nueva extensión** > **Empezar con una plantilla** y selecciona la plantilla **Segmento de catálogo para eventos**. <br><br> !["Selecciona una plantilla" modal con opciones de segmento de catálogo para eventos o compras.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>El editor SQL se rellena automáticamente con una plantilla que une los datos de eventos de usuario con los datos del catálogo para segmentar a los usuarios que interactúan con determinados elementos del catálogo. <br><br>![Un editor SQL para una nueva extensión con una pestaña "Variables" abierta.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Utilice la pestaña **Variables** para proporcionar los campos necesarios para su plantilla antes de generar su segmento.<br><br>Para que Braze identifique a los usuarios en función de su compromiso con los artículos del catálogo, debe hacer lo siguiente:
- Selecciona un catálogo que contenga un campo de catálogo
- Selecciona un evento personalizado que contenga una propiedad de evento
- Haz coincidir los valores del campo del catálogo y de las propiedades del evento

##### Directrices sobre variables para casos de uso B2B

Selecciona las siguientes variables para un caso de uso de segmentación basada en cuentas B2B:

| Variable | Propiedad |
| --- | --- |
| Catálogo | Catálogo de cuentas |
| Campo del catálogo | ID |
| Evento personalizado | cuenta_vinculada |
| Propiedad de evento personalizado | id_cuenta |
| (En Filtrar resultados SQL) Campo del catálogo | Clasificación |
| (En Filtrar resultados SQL) Valor | Empresa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segmentación SQL sofisticada

Para una segmentación más sofisticada o compleja, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). Para ayudarte a empezar, aquí tienes algunas plantillas SQL que puedes utilizar para empezar con la segmentación basada en cuentas B2B:

1. Crea un segmento comparando dos filtros en un mismo catálogo (como los usuarios que trabajan en el sector de la restauración para una cuenta de nivel empresarial). Debes incluir el ID del catálogo y el ID del artículo.

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
2\. Crea un segmento comparando dos filtros a través de dos catálogos distintos (como los usuarios asociados a cuentas de empresa-objetivo que tienen una oportunidad abierta "Etapa 3").

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

### Opción 2: Cuando utilices fuentes conectadas para tus objetos de negocio

Para obtener información básica sobre cómo utilizar fuentes conectadas en la segmentación, consulta [Segmentos CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Utiliza las plantillas que se tratan en [Al utilizar catálogos](#option-1-when-using-catalogs-for-your-business-objects) para inspirarte sobre cómo dar formato a las tablas de origen, ya que puedes darles el formato que quieras.

## Utilizar tu extensión basada en cuentas en un segmento

Después de haber creado tu segmentación a nivel de cuenta en los pasos anteriores, puedes incorporar directamente esas extensiones de segmento a tus criterios de segmentación. También es fácil añadir criterios demográficos incrementales de los usuarios, como la función, la interacción con campañas anteriores, etc. Para más información, consulta [Utilizar tu extensión en un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment).

