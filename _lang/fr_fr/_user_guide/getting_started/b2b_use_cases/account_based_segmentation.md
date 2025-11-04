---
nav_title: Segmentation basée sur les comptes
article_title: "Mise en place d'une segmentation basée sur les comptes"
page_order: 2
page_type: reference
description: "Apprenez à utiliser les différentes fonctionnalités de Braze pour alimenter vos cas d'utilisation de segmentation basée sur les comptes B2B."
---

# Mise en place d'une segmentation basée sur les comptes

> Cette page montre comment utiliser diverses fonctionnalités de Braze pour alimenter vos cas d'utilisation de segmentation basée sur les comptes B2B.

Vous pouvez effectuer une segmentation B2B basée sur les comptes de deux manières, selon la façon dont vous configurez votre [modèle de données B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/):

- Lorsque vous utilisez des [catalogues pour vos objets de gestion](#option-1-when-using-catalogs-for-your-business-objects)
- Lorsque vous utilisez des [sources connectées pour vos objets de gestion](#option-2-when-using-connected-sources-for-your-business-objects)

## Mise en place d'une segmentation B2B basée sur les comptes

### Option 1 : Lorsque vous utilisez des catalogues pour vos objets de gestion

#### Segmentation des modèles SQL de base

Pour vous aider à démarrer, nous avons créé des modèles SQL de base pour une segmentation simple basée sur les comptes.

Supposons que vous souhaitiez segmenter les utilisateurs qui sont des employés d'un compte d'entreprise cible. 

1. Allez dans **Audience** > **Extensions de segments** > **Créer une nouvelle extension** > **Commencer avec un modèle** et sélectionnez le modèle **Segmentation de catalogue pour les événements**. <br><br> !modale "Select a Template" avec des options de segmentation du catalogue pour les événements ou les achats.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>L'éditeur SQL s'enrichit automatiquement d'un modèle qui associe les données d'événement utilisateur aux données du catalogue afin de segmenter les utilisateurs qui s'intéressent à certains articles du catalogue. <br><br>Un éditeur SQL pour une nouvelle extension avec un onglet "Variables" ouvert.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Utilisez l'onglet **Variables** pour fournir les champs nécessaires à votre modèle avant de générer votre segmentation.<br><br>Pour que Braze identifie les utilisateurs en fonction de leur engagement avec les éléments du catalogue, vous devez procéder comme suit :
- Sélectionnez un catalogue qui contient un champ de catalogue
- Sélectionnez un événement personnalisé qui contient une propriété d'événement
- Faites correspondre les valeurs des propriétés des champs et des événements de votre catalogue.

##### Lignes directrices sur les variables pour les cas d'utilisation B2B

Sélectionnez les variables suivantes pour un cas d'utilisation de segmentation B2B basée sur les comptes :

| Variable | Propriété |
| --- | --- |
| Catalogue | Catalogue des comptes |
| Champ du catalogue | ID |
| Événement personnalisé | account_linked |
| Propriétés d'événement personnalisé | account_id |
| (sous Filtrer les résultats SQL) Champ du catalogue | Classification |
| (sous Filtrer les résultats SQL) Valeur | Entreprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segmentation SQL sophistiquée

Pour une segmentation plus sophistiquée ou plus complexe, reportez-vous à [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). Pour vous aider à démarrer, voici quelques modèles SQL que vous pouvez utiliser pour vous aider à prendre une longueur d'avance avec la segmentation basée sur les comptes B2B :

1. Créez un segment comparant deux filtres dans un même catalogue (par exemple, les utilisateurs qui travaillent dans le secteur de la restauration pour un compte de niveau entreprise). Vous devez inclure l'ID du catalogue et l'ID de l'article.

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
2\. Créez un segment comparant deux filtres dans deux catalogues distincts (par exemple, les utilisateurs associés à des comptes cibles d'entreprise qui ont une opportunité ouverte de "stade 3").

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

### Option 2 : Lorsque vous utilisez des sources connectées pour vos objets de gestion

Pour savoir comment utiliser les sources connectées dans la segmentation, reportez-vous à [CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Utilisez les modèles décrits dans la section [Utilisation des catalogues](#option-1-when-using-catalogs-for-your-business-objects) pour vous inspirer de la manière de formater les tables sources, car vous pouvez les formater comme vous le souhaitez.

## Utilisation de votre extension basée sur le compte dans un segment

Après avoir créé votre segmentation au niveau du compte dans les étapes ci-dessus, vous pouvez directement intégrer ces extensions de segments dans vos critères de ciblage. Il est également facile d'ajouter des critères démographiques supplémentaires pour les utilisateurs, tels que le rôle, l'engagement dans des campagnes précédentes, etc. Pour plus d'informations, reportez-vous à la section [Utilisation de votre extension dans une segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment).

