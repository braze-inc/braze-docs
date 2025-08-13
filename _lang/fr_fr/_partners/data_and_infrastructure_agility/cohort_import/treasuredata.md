---
nav_title: Treasure data
article_title: Importation de cohortes Treasure data
description: "Cet article de référence décrit la fonctionnalité d'importation de cohortes Treasure data."
page_type: partner
search_tag: Partner

---
# Importation de cohortes Treasure data

> Cet article décrit comment importer des cohortes d'utilisateurs de Treasure Data vers Braze afin de pouvoir envoyer des campagnes ciblées basées sur des données qui peuvent n'exister que dans votre entrepôt.

{% alert important %}
Cette fonctionnalité est actuellement en version bêta. Pour plus d'informations, contactez vos conseillers Treasure Data et Braze.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Treasure data | Un compte [Treasure data](https://www.treasuredata.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'importation des données Braze | Ces données peuvent être saisies dans le tableau de bord de Braze à partir de **Partner Integrations** > **Technology Partners**, puis sélectionnez **Treasure Data**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Adresse IP statique de Treasure data | L'adresse IP statique de Treasure Data est le point d'accès et la source du lien de cette intégration. Pour déterminer l'adresse IP statique, contactez votre gestionnaire en satisfaction client de Treasure Data ou l’assistance technique de Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de l'importation de données

### Étape 1 : Obtenez votre clé d'importation des données Braze

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Treasure Data**. Ici, vous trouverez votre endpoint REST et générerez la clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.

### Étape 2 : Créer une connexion de données

Avant de créer votre connexion de données dans Treasure data, vous devez vous authentifier. Tout d'abord, sélectionnez **Centre des intégrations**, puis **Catalogue**.

![Catalogue du centre d’intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

Recherchez l'intégration Braze dans le **catalogue**, puis survolez l'icône et sélectionnez **Créer une authentification**. Saisissez vos informations d'identification, nommez votre authentification, puis sélectionnez **Terminé**.

![Catalogue du centre d’intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### Étape 3 : Définissez l'audience de votre cohorte

Synchronisez vos cohortes avec Braze par le biais d'une activation dans l'**Audience Studio** ou en exécutant une requête dans le **Data Workbench.**

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

{% tabs local %}
{% tab Atelier de données %}
#### Étape 3.1 : Définissez votre requête

{% alert note %}
Les colonnes de la requête doivent être spécifiées avec les noms de colonnes et le type de données exacts. Les colonnes de la requête doivent inclure au moins une des valeurs suivantes : `user_ids`, `device_ids` ou la colonne d’alias Braze correspondant à la configuration dans l’IU. Seuls les profils utilisateurs existant dans Braze seront ajoutés à une cohorte. L'importation d'une cohorte ne crée pas de nouveaux profils utilisateurs.
{% endalert %}

1. Naviguez vers **Data Workbench** > **Queries**.
2. Sélectionnez **Nouvelle requête**.
3. Exécutez la requête pour valider l'ensemble des résultats.

![Catalogue du centre d’intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Cas d'utilisation : Synchronisation des cohortes par identifiant

{% subtabs local %}
{% subtab Syncing External IDs %}
Voici un exemple de tableau dans Treasure data :

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
Le nom de la colonne doit être `user_ids` ou la synchronisation échouera.
{% endalert %}

Pour synchroniser les cohortes à l'aide de l'ID externe, exécutez la requête suivante :

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces alias d'utilisateurs seront ajoutés à la cohorte dans Braze :

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Voici un exemple de tableau dans Treasure data :

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

Pour synchroniser les cohortes à l'aide de l'alias d'utilisateur, exécutez la requête suivante :

```sql
SELECT
  email
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces alias d'utilisateurs seront ajoutés à la cohorte dans Braze :

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Voici un exemple de tableau dans Treasure data :

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
Le nom de la colonne doit être `device_ids` ou la synchronisation échouera.
{% endalert %}

Pour synchroniser les cohortes à l'aide de l'ID de l'appareil, exécutez la requête suivante :

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces ID d'appareils seront ajoutés à la cohorte dans Braze :

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Étape 3.2 : Spécifiez le ciblage de l'exportation des résultats

Une fois la requête créée, sélectionnez **Exporter les résultats**. Vous pouvez sélectionner une authentification existante, telle que celle créée dans les dernières étapes, ou créer une nouvelle authentification à utiliser pour la sortie. 

![Catalogue du centre d’intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| Exportation du mappage des résultats |	Description	| 
| ----------- | ----------- |
| ID de la cohorte	| Il s'agit de l'identifiant de la cohorte du backend qui sera envoyé à Braze. 	|
| Nom de la cohorte (facultatif)	| C'est le nom qui apparaîtra dans le filtre de cohorte de l'outil de segmentation de Braze. Si ce paramètre n'est pas défini, la valeur `Cohort ID` sera utilisée comme `Cohort Name`.	|
| Fonctionnement	| Utilisé pour déterminer si la requête doit ajouter ou supprimer des profils de la cohorte dans Braze.	| 
| Alias (facultatif) | Lorsqu'il est défini, le nom de la colonne correspondante dans votre requête sera envoyé en tant que `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées en tant que `alias_name`.	| 
| Nombre de fils | Nombre d'appels API simultanés. |

Suivez [les étapes de Treasure data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) pour configurer votre exportation en fonction de votre cas d'utilisation.

#### Étape 3.3 : Exécuter la requête

Enregistrez la requête en lui donnant un nom et exécutez-la, ou exécutez simplement la requête. Une fois la requête terminée avec succès, le résultat de la requête est automatiquement exporté vers Braze.

{% endtab %}
{% tab Audience Studio %}
#### Étape 3.1 : Créer une activation

Créez un nouveau segment ou choisissez un segment existant à synchroniser avec Braze en tant que cohorte. Dans le segment, sélectionnez **Créer l’activation**.

#### Étape 3.2 : Complétez vos données d'activation

![Détails de l'activation des intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| Réglage des détails de l'activation |	Description	| 
| ----------- | ----------- |
| Nom de l'activation	| Le nom de votre activation.	|
| Description de l'activation| Une brève description de l'activation.	|
| Authentification	| Choisissez l'authentification de la cohorte Braze créée à l'étape 2.	| 
| ID de la cohorte	| Il s'agit de l'identifiant de la cohorte du backend qui sera envoyé à Braze. 	|
| Nom de la cohorte (facultatif)	| C'est le nom qui apparaîtra dans le filtre de cohorte de l'outil de segmentation de Braze. Si ce paramètre n'est pas défini, la valeur `Cohort ID` sera utilisée comme `Cohort Name`.	|
| Fonctionnement	| Utilisé pour déterminer si la requête doit ajouter ou supprimer des profils de la cohorte dans Braze.	| 
| Alias (facultatif) | Lorsqu'il est défini, le nom de la colonne correspondante dans votre requête sera envoyé en tant que `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées en tant que `alias_name`.	| 
| Nombre de fils | Nombre d'appels API simultanés. |

#### Étape 3.3 : Établir le mappage des sorties

![Mappage des sorties d’activation des intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| Mappage des sorties d'activation |	Description	| 
| ----------- | ----------- |
| Colonnes d'attributs	| Déterminez les colonnes de votre base de données de segments qui seront mappées en tant qu'identifiants lors de la synchronisation des profils vers une cohorte Braze.	|
| Générateur de chaînes de caractères| Le générateur de caractères n'est pas nécessaire pour l'intégration de Braze.	|

{% alert important %}
 - Si vous utilisez `device_id` comme identifiant, le **nom de la colonne de sortie** doit être `device_ids`.
 - Lorsque vous utilisez des alias comme identifiant, le **nom de la colonne de sortie** doit être le nom de la colonne correspondante dans votre requête sera envoyé sous la forme `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées sous la forme `alias_name`.
 - Si vous utilisez `external_id` comme identifiant, le **nom de la colonne de sortie** doit être `user_ids`.
{% endalert %}

Tous les noms de colonnes non pertinents ou mal nommés seront ignorés. Vous pouvez choisir d'utiliser plus d'un identifiant dans vos synchronisations.

#### Étape 3.4 : Définissez votre planification d'activation

Définissez la planification de la synchronisation souhaitée et enregistrez votre activation.

![Planning de l’activation des intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Étape 4 : Créer un segment Braze à partir de l'exportation des données Treasure data

Dans Braze, naviguez vers **Segments**, créez un nouveau segment et sélectionnez **Cohortes Treasure Data** comme filtre. À partir de là, vous pouvez choisir la cohorte Treasure Data que vous souhaitez inclure. Une fois votre segment de cohorte Treasure Data créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un canvas.

![Catalogue du centre d’intégrations de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.
