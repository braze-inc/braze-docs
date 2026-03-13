---
nav_title: Cloud Data Ingestion
article_title: Cloud Data Ingestion de Braze
alias: /cloud_ingestion/
description: "Cet article de référence décrit les sources de Cloud Data Ingestion de Braze, ainsi que les recommandations pour la configuration des données."
page_order: 0.1
toc_headers: h2
---

# Cloud Data Ingestion de Braze

> Braze Cloud Ingestion de données (CDI) vous permet de configurer une connexion directe depuis votre solution de stockage de données afin de synchroniser les données utilisateur pertinentes et d'autres données non utilisateur vers Braze. Ces données peuvent ensuite être utilisées à des fins de personnalisation ou de segmentation pour optimiser vos cas d'utilisation marketing. L'intégration flexible de Cloud Data Ingestion prend en charge les structures de données complexes, y compris les JSON imbriqués et les tableaux d'objets.

## Fonctionnement

Avec Braze Cloud Data Ingestion (CDI), vous configurez une intégration entre votre instance d'entrepôt de données et l'espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d’une planification différente. Les synchronisations peuvent avoir lieu d’une fois toutes les 15 minutes à une fois par mois. Si vous avez besoin que les synchronisations se produisent à une fréquence supérieure à 15 minutes, contactez votre gestionnaire de satisfaction client ou envisagez d'utiliser les appels API REST pour l'ingestion de données en temps réel.

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, toutes les données mises à jour sont reflétées dans Braze.

### Identifier votre ID d'intégration

Vous pouvez trouver votre ID d'intégration dans l'URL lorsque vous consultez une intégration dans le tableau de bord de Braze. Veuillez vous rendre dans **Paramètres des données** > **Ingestion de données dans le cloud** et sélectionner une intégration. L'ID d'intégration apparaît dans l'URL au format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Par exemple, si votre URL est `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, votre ID d'intégration est `abc123xyz`. Vous pouvez utiliser cet ID lorsque vous effectuez des appels API pour servir de déclencheur à des synchronisations ou vérifier l'état de la synchronisation.

## Cas d’utilisation

Grâce aux fonctionnalités d'ingestion de données de Braze Cloud, vous pouvez :

- Créez une intégration simple dans Braze directement depuis votre entrepôt de données ou solution de stockage de fichiers en quelques minutes seulement.
- Synchronisez en toute sécurité les données utilisateur, y compris les attributs, les événements et les achats, depuis votre entrepôt de données vers Braze.
- Fermez la boucle de données avec Braze en combinant l'ingestion de données avec Currents ou Snowflake Data Sharing.

De plus, [les sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) constituent une alternative sans copie. Vous pouvez demander à Braze d'interroger directement votre entrepôt de données ou votre solution de stockage de fichiers afin de créer des segments CDI, sans avoir à copier les données sous-jacentes vers Braze.

## Sources de données prises en charge

L'ingestion de données peut synchroniser les données provenant de :

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

### Objets non utilisés
- Articles de catalogue

### Envoi de messages sans copie
- Sources connectées

## Identifiants utilisateur pour l'ingestion de données

Lors de la synchronisation des données utilisateur via l'ingestion de données, vous pouvez identifier les utilisateurs à l'aide d'un ou plusieurs des types d'identifiants suivants. Chaque ligne de votre table source doit contenir une valeur pour un seul type d'identifiant à la fois, mais votre table peut inclure des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.

| Identifiant | Description |
|------------|-------------|
| `EXTERNAL_ID` | L'ID externe qui identifie le profil utilisateur à créer ou à mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`. |
| `BRAZE_ID` | Identifiant utilisateur Braze généré par le SDK Braze. Il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'ingestion de données. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. |
| `EMAIL` | L’adresse e-mail de l’utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. Si vous indiquez à la fois votre adresse e-mail et votre numéro de téléphone, l'adresse e-mail sera utilisée comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour obtenir des informations détaillées sur la configuration des tables avec ces identifiants, veuillez vous référer à la documentation [sur les intégrations de l'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Utilisation de points de données

Pour les clients bénéficiant d'une facturation basée sur les points de données, la facturation par point de donnée pour l'ingestion de données correspond à la facturation des mises à jour via [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)l'[endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Pour plus d'informations, reportez-vous à la section [Points de données]({{site.baseurl}}/user_guide/data/data_points/). 

{% alert important %}
Braze Cloud Data Ingestion compte dans la limite de débit disponible, donc si vous envoyez des données par une autre méthode, la limite de débit est combinée entre l'API Braze et Cloud Data Ingestion.
{% endalert %}

## Limites du produit

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d’intégrations | Le nombre d’intégrations que vous pouvez définir n’est pas limité. Cependant, vous ne pouvez configurer qu'une seule intégration par table ou vue.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Toute synchronisation comportant plus de 500 millions de nouvelles lignes est interrompue. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire satisfaction client Braze ou l'assistance Braze. |
| Attributs par rangée     | Chaque ligne doit contenir un seul ID d'utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau d'objets compte pour un attribut). |
| Taille de la charge utile           | Chaque ligne peut contenir une charge utile allant jusqu'à 1 Mo. Les charges utiles supérieures à 1 Mo sont rejetées et l'erreur « La charge utile était supérieure à 1 Mo » est consignée dans le journal de synchronisation avec l'ID externe associé et la charge utile tronquée. |
| Type de données              | Vous pouvez synchroniser les attributs utilisateurs via l’ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connecte à votre entrepôt de données ou à votre environnement cloud, quelle que soit la région ou le fournisseur de services cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
