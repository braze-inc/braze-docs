---
nav_title: Cloud Data Ingestion
article_title: Cloud Data Ingestion de Braze
alias: /cloud_ingestion/
description: "Cet article de référence décrit les sources de Cloud Data Ingestion de Braze, ainsi que les recommandations pour la configuration des données."
page_order: 0.1
toc_headers: h2
---

# Cloud Data Ingestion de Braze

> Braze Cloud Data Ingestion (CDI) vous permet de mettre en place une connexion directe depuis votre solution de stockage de données pour synchroniser les données utilisateur pertinentes et d'autres données non utilisateur vers Braze. Ces données peuvent ensuite être utilisées pour la personnalisation ou la segmentation afin d'alimenter vos cas d'utilisation marketing. L'intégration flexible de Cloud Data Ingestion prend en charge des structures de données complexes, notamment le JSON imbriqué et les tableaux d'objets.

## Fonctionnement

Avec Braze Cloud Data Ingestion (CDI), vous configurez une intégration entre votre instance d'entrepôt de données et l'espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d’une planification différente. Les synchronisations peuvent avoir lieu d’une fois toutes les 15 minutes à une fois par mois. Si vous avez besoin que les synchronisations se produisent à une fréquence supérieure à 15 minutes, contactez votre gestionnaire de satisfaction client ou envisagez d'utiliser les appels API REST pour l'ingestion de données en temps réel.

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. Chaque fois que la synchronisation s'exécute, les données mises à jour sont répercutées dans Braze.

### Trouver votre ID d'intégration

Vous trouverez votre ID d'intégration dans l'URL lorsque vous visualisez une intégration dans le tableau de bord de Braze. Naviguez vers **Paramètres des données** > **Ingestion de données dans le cloud** et sélectionnez une intégration. L'ID d'intégration apparaît dans l'URL au format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Par exemple, si votre URL est `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, votre ID d'intégration est `abc123xyz`. Vous pouvez utiliser cet ID lorsque vous effectuez des appels API pour déclencher des synchronisations ou en vérifier l'état.

## Cas d’utilisation

Grâce aux fonctionnalités d'ingestion de données de Braze Cloud, vous pouvez :

- Créez une intégration simple dans Braze directement depuis votre entrepôt de données ou solution de stockage de fichiers en quelques minutes seulement.
- Synchronisez en toute sécurité les données des utilisateurs, y compris les attributs, les événements et les achats de votre entrepôt de données vers Braze.
- Bouclez la boucle des données avec Braze en combinant l'ingestion de données dans le cloud avec le partage de données Currents ou Snowflake.

En outre, les [sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) sont une alternative à la copie zéro. Vous pouvez demander à Braze d'interroger directement votre entrepôt de données ou votre solution de stockage de fichiers pour construire des segments CDI, sans copier les données sous-jacentes dans Braze.

## Sources de données prises en charge

L'ingestion de données dans le nuage peut synchroniser des données provenant de :

   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Types de données prises en charge 

L'ingestion de données dans le nuage prend en charge les types de données suivants :

### Données utilisateur
- Attributs de l'utilisateur, y compris :
   - Attributs personnalisés imbriqués
   - Tableaux d’objets
   - État des abonnements
- Événements personnalisés
- Événements d’achat
- Demandes de suppression d'utilisateurs

### Objets non-utilisateurs
- Articles de catalogue

### Envoi de messages sans copie
- Sources connectées

## Identificateurs d'utilisateurs pour l'ingestion de données

Lors de la synchronisation des données utilisateur via Cloud Data Ingestion, vous pouvez identifier les utilisateurs à l'aide d'un ou plusieurs des types d'identifiants suivants. Chaque ligne de votre tableau source doit contenir une valeur pour un seul type d'identifiant à la fois, mais votre tableau peut inclure des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.

| Identifiant | Description |
|------------|-------------|
| `EXTERNAL_ID` | L'ID externe qui identifie le profil utilisateur à créer ou à mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant de l'utilisateur de Braze généré par le SDK de Braze. Il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données dans le cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. |
| `EMAIL` | L’adresse e-mail de l’utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. Si vous indiquez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour des informations détaillées sur la configuration des tables avec ces identifiants, reportez-vous à la documentation sur les [intégrations de l'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Utilisation de points de données

Pour les clients en facturation par points de données, la facturation par points de données pour l'ingestion de données dans le cloud équivaut à la facturation des mises à jour via le [point d'extrémité`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Pour plus d'informations, reportez-vous à la section [Points de données]({{site.baseurl}}/user_guide/data/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion compte dans la limite de débit disponible, donc si vous envoyez des données par une autre méthode, la limite de débit est combinée entre l'API Braze et Cloud Data Ingestion.
{% endalert %}

## Limites du produit

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Toutefois, vous ne pouvez configurer qu'une seule intégration par table ou vue.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Toute synchronisation comportant plus de 500 millions de nouvelles lignes est interrompue. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire satisfaction client Braze ou l'assistance Braze. |
| Attributs par rangée     | Chaque ligne doit contenir un seul ID d'utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau d'objets compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Les données utiles supérieures à 1 Mo sont rejetées et l'erreur "Payload was greater than 1MB" est consignée dans le journal de synchronisation avec l'ID externe associé et les données utiles tronquées. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connecte à votre entrepôt de données ou à votre environnement cloud dans n'importe quelle région ou fournisseur cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
