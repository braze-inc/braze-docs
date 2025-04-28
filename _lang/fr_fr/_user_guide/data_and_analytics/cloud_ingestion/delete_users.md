---
nav_title: Supprimer des utilisateurs avec CDI 
article_title: "Supprimer des utilisateurs avec l'ingestion de données en nuage"
page_order: 30
page_type: reference
description: "Cet article de référence fournit un aperçu du processus de suppression des utilisateurs avec Cloud Data Ingestion."

---

# Supprimer des utilisateurs avec Cloud Data Ingestion

Les synchronisations de suppression d'utilisateur sont prises en charge pour toutes les sources de données Cloud Data Ingestion disponibles. 

## Configuration de l'intégration 

Suivez le processus standard pour [créer une nouvelle intégration dans le tableau de bord de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) pour l'entrepôt de données auquel vous souhaitez vous connecter. Assurez-vous d'inclure un rôle qui peut accéder au tableau de suppression. Sur la page **Créer une importation d'une synchronisation**, définissez le **Type de données** sur **Supprimer des utilisateurs**. Cela permettra de s'assurer que les actions appropriées sont prises lors de l'exécution de l'intégration pour supprimer les utilisateurs.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configuration des données sources 

Les tables sources pour les suppressions d'utilisateurs doivent inclure un ou plusieurs types d'identifiants d'utilisateurs et un horodatage `UPDATED_AT`. Les colonnes de données utiles ne sont pas prises en charge pour les données de suppression de l'utilisateur.

### `UPDATED_AT`

Ajoutez un horodatage `UPDATED_AT` à votre tableau source. Cet horodatage indique l'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze ne synchronisera que les lignes qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.

### Colonnes d'identification de l'utilisateur

Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant : soit `external_id`, soit la combinaison de `alias_name` et `alias_label`, soit `braze_id`. Un tableau source peut contenir des colonnes pour un, deux ou les trois types d'identifiants.
- `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
- `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
- `BRAZE_ID` : L’identifiant d’utilisateur Braze. Il est généré par le SDK Braze et les nouveaux utilisateurs ne peuvent pas être créés à l’aide d’un ID Braze via l’ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. 

{% alert important %}
N'incluez pas de colonne `PAYLOAD` dans votre tableau pour la suppression de l'utilisateur. Pour éviter la suppression accidentelle et permanente d'utilisateurs, la synchronisation échouera si une colonne "payload" est fournie dans la table source. Toute autre colonne est autorisée mais sera ignorée par Braze.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```json
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
Créez une table avec les champs suivants :

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| DATE/HEURE | REQUIS |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
{% endtab %}

{% tab Databricks %}
Créez une table avec les champs suivants :

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| DATE/HEURE | REQUIS |
| `EXTERNAL_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_NAME`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `ALIAS_LABEL`| CHAÎNE DE CARACTÈRES | NULLABLE |
| `BRAZE_ID`| CHAÎNE DE CARACTÈRES | NULLABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### Fonctionnement

Avec Braze Cloud Data Ingestion, vous configurez une intégration entre votre instance d'entrepôt de données et l'espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d’une planification différente. Les synchronisations peuvent avoir lieu d’une fois toutes les 15 minutes à une fois par mois. Pour les clients qui ont besoin de synchronisations plus fréquentes que 15 minutes, adressez-vous à votre gestionnaire de satisfaction client, ou envisagez d'utiliser les appels API REST pour l'ingestion de données en temps réel.

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et supprime les profils utilisateurs correspondants sur votre tableau de bord Braze. 

{% alert warning %}
La suppression des profils utilisateur ne peut pas être annulée. Cette action supprimera définitivement les utilisateurs susceptibles de provoquer des écarts dans vos données. Pour plus d'informations, reportez-vous à la section [Supprimer un profil utilisateur]({{site.baseurl}}/help/help_articles/api/delete_user/).
{% endalert %}

<br><br>